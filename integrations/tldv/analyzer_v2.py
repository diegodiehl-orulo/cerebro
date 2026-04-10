#!/usr/bin/env python3
"""
analyzer_v2.py — Estágio 3 do pipeline tl;dv
Análise LLM de cada reunião a partir do SUMMARY (não do transcript).
Cruza com memória existente e extrai: decisões, aprendizados, riscos, tarefas.

Input:  memory/meetings/summaries/{id}.json
Output: memory/meetings/analysis/{id}_v2.md
"""
import json, sys, os
from pathlib import Path
from datetime import datetime

SUMMARY_DIR = Path("/root/.openclaw/workspace/memory/meetings/summaries")
ANALYSIS_DIR = Path("/root/.openclaw/workspace/memory/meetings/analysis")
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

# Ler memória relevante se existir
def load_memory_context() -> str:
    ctx = []
    
    # People
    people_file = Path("/root/.openclaw/workspace/memory/people.md")
    if people_file.exists():
        ctx.append(f"=== PEOPLE ===\n{people_file.read_text(encoding='utf-8')[:2000]}")
    
    # Pending
    pending_file = Path("/root/.openclaw/workspace/memory/pending.md")
    if pending_file.exists():
        ctx.append(f"=== PENDING ===\n{pending_file.read_text(encoding='utf-8')[:2000]}")
    
    # Lessons
    lessons_file = Path("/root/.openclaw/workspace/memory/lessons.md")
    if lessons_file.exists():
        ctx.append(f"=== LESSONS ===\n{lessons_file.read_text(encoding='utf-8')[:2000]}")
    
    return "\n\n".join(ctx)


def build_prompt(summary: dict, memory_context: str) -> str:
    """Constrói o prompt de análise a partir do summary estruturado."""
    
    meta = summary.get("metadata", {})
    blocks = summary.get("blocks", [])
    actions = summary.get("action_items_raw", [])
    
    participants = meta.get("participants", [])
    duration = meta.get("duration_min", 0)
    mid = summary.get("meeting_id", "?")
    
    # Preparar blocos como texto legível
    blocks_text = ""
    for i, b in enumerate(blocks[:30]):  # máximo 30 blocos
        mins = b["start_sec"] // 60
        segs = b["start_sec"] % 60
        speakers = ", ".join(b["speakers"][:3])
        topic = b["topic_hint"][:100]
        preview = b["content_preview"][:200]
        blocks_text += f"\n## Bloco {i+1} [{mins}:{segs:02d}] ({speakers}) — {topic}\n{preview}\n"
    
    # Preparar ações brutas
    actions_text = ""
    for a in actions[:10]:
        mins = a["timestamp"] // 60
        segs = a["timestamp"] % 60
        actions_text += f"- [{mins}:{segs:02d}] {a['speaker']}: {a['text'][:200]}\n"
    
    prompt = f"""Você é o Morfeu, estrategista-chefe e gestor de projetos de Diego Diehl (Diretor Comercial da Órulo).
Analise esta reunião e extraia informação acionável.

=== DADOS DA REUNIÃO ===
ID: {mid}
Participantes: {", ".join(participants)}
Duração: {duration} minutos
Blocks temáticos: {len(blocks)}
Ações brutas identificadas: {len(actions)}


=== MEMÓRIA EXISTENTE (contexto para cruzar) ===
{memory_context[:3000] if memory_context else "(sem contexto prévio)"}


=== BLOCOS TEMÁTICOS DA REUNIÃO ===
{blocks_text}


=== AÇÕES BRUTAS IDENTIFICADAS (verificar, nãoaceitar como fato) ===
{actions_text if actions_text else "(nenhuma ação explícita detectada)"}


=== SUA TAREFA ===

Responda EXATAMENTE neste formato (sem variações):

**REUNIÃO:** [nome ou tema identificado]
**DATA:** [data se disponível]
**PARTICIPANTES:** [lista]
**DURAÇÃO:** [X minutos]

### RESUMO
- [3-5 bullets do que foi discutido]

### TAREFA(S)
- [ ] **[DONO]** Texto da ação | Prazo: [se mencionado]

### DECISÃO(ÕES)
- [bullet da decisão tomada]

### RISCO(S) / BLOQUEIO(S)
- [bullet do risco]

### FEEDBACK / APRENDIZADO
- [bullet de aprendizado ou padrão identificado]

### PRÓXIMO PASSO
- [1-2 bullets: próximo passo claro com dono e prazo se possível]

---

REGRAS:
- Máximo 4 linhas por seção
- Bullets • (não use -, *, numbers)
- DONO em maiúscula entre colchetes quando identificado
- Se não houver decisão, escrever "Nenhuma decisão registrada"
- Se não houver risco, escrever "Nenhum risco identificado"
- Interpretar o sentido das falas (transcrição pode ter erros)
- Ações identificadas no raw são sugestões — validar antes de listar como tarefa
- Contexto: Órulo = proptech SaaS B2B para mercado de lançamentos imobiliários
- Se reunião for sobre tema já discutido antes, mencioná-lo e cruzar com memória
"""
    return prompt


def call_llm(prompt: str) -> str:
    """Chama o LLM MiniMax via API."""
    try:
        import urllib.request, urllib.error
        
        API_KEY = os.environ.get("MINIMAX_API_KEY", "")
        if not API_KEY:
            # Tentar do cofre ou .env
            API_KEY = "69f9a821-7286-46e8-a64c-7c1f20a01576"  # placeholder
        
        url = "https://api.minimaxi.chat/v1/text/chatcompletion_v2"
        payload = json.dumps({
            "model": "MiniMax-Text-01",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1500,
            "temperature": 0.3
        }).encode()
        
        req = urllib.request.Request(
            url, data=payload,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            method="POST"
        )
        
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
            return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[ERRO LLM: {e}]"


def analyze_summary(summary: dict, memory_context: str) -> str:
    """Gera análise completa de uma reunião."""
    
    mid = summary.get("meeting_id", "?")
    prompt = build_prompt(summary, memory_context)
    
    print(f"  🔄 Analisando {mid}...")
    
    result = call_llm(prompt)
    
    # Salvar resultado
    out_file = ANALYSIS_DIR / f"{mid}_v2.md"
    header = f"""# ANÁLISE — {mid}
**Summary:** memory/meetings/summaries/{mid}.json  
**Gerado:** {datetime.now().isoformat()}  
**Stage:** analysis_v2 (LLM)

---

"""
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(header + result)
    
    return result


def main(meeting_id: str = None):
    memory_context = load_memory_context()
    print(f"ANÁLISE V2 — memory context carregado ({len(memory_context)} chars)")
    
    if meeting_id:
        ids = [meeting_id]
    else:
        existing = set(p.stem.replace("_v2","") for p in ANALYSIS_DIR.glob("*_v2.md"))
        ids = [p.stem for p in SUMMARY_DIR.glob("*.json") if p.stem not in existing]
    
    print(f"{len(ids)} reuniões para analisar")
    
    for mid in ids:
        summary_file = SUMMARY_DIR / f"{mid}.json"
        if not summary_file.exists():
            print(f"  ○ Sem summary: {mid}")
            continue
        
        try:
            with open(summary_file) as f:
                summary = json.load(f)
        except Exception as e:
            print(f"  ✗ Erro leitura {mid}: {e}")
            continue
        
        try:
            result = analyze_summary(summary, memory_context)
            print(f"  ✅ {mid}: análise gerada")
        except Exception as e:
            print(f"  ✗ Erro análise {mid}: {e}")
    
    print(f"\nPronto. Análises em {ANALYSIS_DIR}")


if __name__ == "__main__":
    mid = sys.argv[1] if len(sys.argv) > 1 else None
    main(mid)
