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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DIRS, WORKSPACE, MINIMAX_URL, MINIMAX_MODEL, require_minimax_key, LLM_TIMEOUT  # noqa: E402

SUMMARY_DIR = DIRS["summaries"]
ANALYSIS_DIR = DIRS["analysis"]
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

# Ler memória relevante se existir
def load_memory_context() -> str:
    ctx = []

    for fname in ["memory/people.md", "memory/pending.md", "memory/lessons.md"]:
        f = WORKSPACE / fname
        if f.exists():
            content = f.read_text(encoding="utf-8")
            ctx.append(f"=== {fname} ===\n{content[:2000]}")

    return "\n\n".join(ctx)


def call_llm(prompt: str) -> str:
    """Chama o LLM MiniMax via API (endpoint /v1/chat/completions)."""
    try:
        import urllib.request, json

        api_key = require_minimax_key()
        payload = json.dumps({
            "model": MINIMAX_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1500,
            "temperature": 0.3
        }).encode()

        req = urllib.request.Request(
            MINIMAX_URL, data=payload,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            method="POST"
        )

        with urllib.request.urlopen(req, timeout=LLM_TIMEOUT) as resp:
            result = json.loads(resp.read())
            choice = result.get("choices", [{}])[0]
            return choice.get("message", {}).get("content", "")
    except Exception as e:
        return f"[ERRO LLM: {e}]"


def build_prompt(summary: dict, memory_context: str) -> str:
    """Constrói o prompt de análise a partir do summary estruturado."""

    meta = summary.get("metadata", {})
    blocks = summary.get("blocks", [])
    actions = summary.get("action_items_raw", [])

    participants = meta.get("participants", [])
    duration = meta.get("duration_min", 0)
    mid = summary.get("meeting_id", "?")

    blocks_text = ""
    for i, b in enumerate(blocks[:25]):
        mins, sec = divmod(b["start_sec"], 60)
        speakers = ", ".join(b["speakers"][:3])
        topic = b["topic_hint"][:100]
        preview = b["content_preview"][:200]
        blocks_text += f"\n## Bloco {i+1} [{mins}:{sec:02d}] ({speakers})\n{preview}\n"

    actions_text = ""
    for a in actions[:8]:
        mins, sec = divmod(a["timestamp"], 60)
        actions_text += f"- [{mins}:{sec:02d}] {a['speaker']}: {a['text'][:200]}\n"

    prompt = f"""Você é o Morfeu, estrategista-chefe e gestor de projetos de Diego Diehl (Diretor Comercial da Órulo).
Analise esta reunião e extraia informação acionável.

=== DADOS DA REUNIÃO ===
ID: {mid}
Participantes: {", ".join(participants)}
Duração: {duration} minutos
Blocks temáticos: {len(blocks)}

=== MEMÓRIA EXISTENTE (contexto para cruzar) ===
{memory_context[:3000] if memory_context else "(sem contexto prévio)"}

=== BLOCOS TEMÁTICOS DA REUNIÃO ===
{blocks_text}

=== AÇÕES BRUTAS IDENTIFICADAS (validar antes de listar) ===
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

### PRÓXIMO PASSO
- [1-2 bullets: próximo passo claro com dono e prazo se possível]

REGRAS:
- Máximo 4 linhas por seção
- DONO em maiúscula entre colchetes quando identificado
- Se não houver decisão, escrever "Nenhuma decisão registrada"
- Se não houver risco, escrever "Nenhum risco identificado"
- Interpretar o sentido das falas (transcrição pode ter erros)
- Ações identificadas no raw são sugestões — validar antes de listar como tarefa
- Contexto: Órulo = proptech SaaS B2B para mercado de lançamentos imobiliários
"""
    return prompt


def analyze_summary(summary: dict, memory_context: str) -> str:

    mid = summary.get("meeting_id", "?")
    prompt = build_prompt(summary, memory_context)

    print(f"  🔄 Analisando {mid}...")

    result = call_llm(prompt)

    out_file = ANALYSIS_DIR / f"{mid}_v2.md"
    header = (
        f"# ANÁLISE — {mid}\n"
        f"**Summary:** memory/meetings/summaries/{mid}.json\n"
        f"**Gerado:** {datetime.now().isoformat()}\n"
        f"**Stage:** analysis_v2 (LLM)\n\n---\n\n"
    )
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(header + result)

    return result


def main(meeting_id: str = None):
    memory_context = load_memory_context()
    print(f"ANÁLISE V2 — context carregado ({len(memory_context)} chars)")

    if meeting_id:
        ids = [meeting_id]
    else:
        existing = {p.stem.replace("_v2", "") for p in ANALYSIS_DIR.glob("*_v2.md")}
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
            if "[ERRO" in result:
                print(f"  ⚠️ {mid}: {result}")
            else:
                print(f"  ✅ {mid}: análise gerada")
        except Exception as e:
            print(f"  ✗ Erro análise {mid}: {e}")

    print(f"\nPronto. Análises em {ANALYSIS_DIR}")


if __name__ == "__main__":
    mid = sys.argv[1] if len(sys.argv) > 1 else None
    main(mid)
