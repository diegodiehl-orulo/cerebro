#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tl;dv Meeting Analyzer -- Morfeu
================================
Para cada reuniao normalizada em memory/meetings/normalized/, gera:
  - memory/meetings/analysis/{meetingId}.md  (relatorio humano)
  - memory/meetings/analysis/{meetingId}.json (dados maquina)

Uso:
  python3 analyzer.py                    # processa todos os nao-analisados
  python3 analyzer.py --limit 5           # apenas 5 reunioes
  python3 analyzer.py --meeting-id ID   # uma reuniao especifica
  python3 analyzer.py --dry-run         # mostra o que faria sem rodar
  python3 analyzer.py --reanalysis      # refaz mesmo ja analisados

Modelo: minimax/MiniMax-M2.7 (fallback: google/gemini-2.0-flash)
Retry: exponential backoff 1s -> 2s -> 4s para rate limit.
"""

import argparse
import json
import os
import sys
import time
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Paths
WORKSPACE   = Path("/root/.openclaw/workspace")
NORMALIZED  = WORKSPACE / "memory/meetings/normalized"
ANALYSIS    = WORKSPACE / "memory/meetings/analysis"
LEDGER_FILE = WORKSPACE / "memory/meetings/ledger/analyzed_ledger.json"

DEFAULT_MODEL = "minimax/MiniMax-M2.7"
FALLBACK_MODEL = "google/gemini-2.0-flash"
MAX_RETRIES = 3
LEDGER_VERSION = "1.0"

# LLM Call

def call_llm(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """
    Chama o modelo via openclaw agent --agent morfeu.
    Implementa retry com exponential backoff para rate limit.
    """
    import subprocess

    for attempt in range(MAX_RETRIES):
        try:
            result = subprocess.run(
                [
                    "openclaw", "agent",
                    "--agent", "morfeu",
                    "--message", prompt,
                    "--timeout", "90",
                ],
                capture_output=True,
                text=True,
                timeout=120,
            )
            if result.returncode == 0:
                output = result.stdout.strip()
                if not output:
                    raise RuntimeError("Resposta vazia do modelo.")
                return output
            stderr = result.stderr.lower()
            if "rate" in stderr or "429" in stderr or "too many requests" in stderr:
                wait = 2 ** attempt
                print(f"  [WARN] Rate limit (attempt {attempt+1}), retry em {wait}s...")
                time.sleep(wait)
                continue
            raise RuntimeError(f"openclaw agent falhou (rc={result.returncode}): {result.stderr[:200]}")
        except subprocess.TimeoutExpired:
            if attempt < MAX_RETRIES - 1:
                wait = 2 ** attempt
                print(f"  [WARN] Timeout (attempt {attempt+1}), retry em {wait}s...")
                time.sleep(wait)
                continue
            raise

    raise RuntimeError("LLM indisponivel apos todas as tentativas.")


# Build Prompt

MEETING_ANALYSIS_SYSTEM = (
    "Voce eh o Morfeu, assistente de gestao comercial da Orulo.\n"
    "Analise reunioes de negocio com rigor executivo.\n"
    "Todo texto gerado deve ser em portugues brasileiro.\n\n"
    "Regras absolutas:\n"
    "- NUNCA invente nomes de pessoas, prazos ou dados nao presentes no input.\n"
    "- Se faltam dados, diga explicitamente e marque confidence como low.\n"
    "- Phrasing vamos, aprovado, decidido, concordamos -> confidence confirmed.\n"
    "- Phrasing eu acho que, seria o caso de -> confidence likely.\n"
    "- Phrasing eu sugeriria, seria interessante -> confidence uncertain.\n"
    "- max 300 caracteres no executive_summary.\n"
    "- IDs: D1, D2... para decisoes | O1, O2... para pendencias | "
    "T1, T2... para tarefas | Q1, Q2... para perguntas | "
    "R1, R2... para riscos | OP1, OP2... para oportunidades | "
    "DS1, DS2... para sugestoes doc | M1, M2... para memorias.\n"
    "- owners: usar nome da pessoa quando mencionada em contexto de acao."
)

# JSON schema (escaped braces for .format())
_JSON_SCHEMA = """{
  "meeting_id": "string",
  "name": "string",
  "happened_at": "ISO8601",
  "analysis_version": "1.0",
  "analysis_generated_at": "ISO8601",
  "executive_summary": "string (max 300 chars) - o que importa saber em 30 segundos",
  "context": {
    "purpose": "string - por que a reuniao aconteceu",
    "main_agenda_items": ["array de strings"],
    "participants_and_roles": { "name": "papel percebido na reuniao" },
    "meeting_type": "directive|review|strategy|operational|cadence|one_on_one|client|partner|internal",
    "notes_limitation": "string|null - se transcript ausente, explicar impacto na analise"
  },
  "decisions": [
    {
      "id": "D1",
      "description": "string",
      "decision_maker": "string|null",
      "confidence": "confirmed|likely|uncertain",
      "source": "transcript|notes|both"
    }
  ],
  "open_items": [
    {
      "id": "O1",
      "description": "string",
      "owner": "string|null",
      "deadline": "ISO8601|null",
      "status": "open|blocked|pending_response",
      "source": "transcript|notes|both",
      "blocking_factor": "string|null"
    }
  ],
  "tasks": [
    {
      "id": "T1",
      "description": "string",
      "owner": "string|null",
      "deadline": "string|null",
      "priority": "high|medium|low",
      "status": "generated|assigned|confirmed",
      "source": "transcript|notes|both"
    }
  ],
  "critical_questions": [
    {
      "id": "Q1",
      "question": "string",
      "context": "string - por que esta pergunta eh relevante",
      "answer_required_by": "string|null",
      "owner": "string|null"
    }
  ],
  "risks_and_alerts": [
    {
      "id": "R1",
      "description": "string",
      "type": "operational|financial|relationship|strategic|compliance",
      "severity": "high|medium|low",
      "mitigation": "string|null",
      "source": "transcript|notes|both"
    }
  ],
  "opportunities": [
    {
      "id": "OP1",
      "description": "string",
      "potential_impact": "high|medium|low",
      "owner": "string|null",
      "source": "transcript|notes|both"
    }
  ],
  "documentary_suggestions": [
    {
      "id": "DS1",
      "action": "string - o que registrar",
      "destination": "string - arquivo ou sistema destino",
      "priority": "high|medium|low",
      "reason": "string"
    }
  ],
  "memories_to_register": [
    {
      "id": "M1",
      "memory": "string - fato ou contexto a registrar na memoria",
      "category": "person|project|process|decision|preference|relationship|lesson",
      "confidence": "high|medium|low"
    }
  ],
  "recommended_next_step": {
    "action": "string",
    "owner": "string|null",
    "deadline": "string|null",
    "reason": "string - por que este eh o proximo passo mais importante"
  },
  "analysis_confidence": {
    "transcript_available": true|false,
    "notes_available": true|false,
    "topics_available": true|false,
    "overall": "high|medium|low",
    "gaps": ["string - o que nao foi possivel analisar"]
  },
  "raw_topics_from_tldv": ["array - topics que o tldv IA extraiu"]
}"""

MEETING_ANALYSIS_USER_TEMPLATE = (
    "Analise a reuniao abaixo e retorne exatamente o JSON descrito abaixo "
    "(sem markdown, sem Explanation, apenas o JSON puro).\n\n"
    "## Estrutura JSON obrigatoria:\n\n"
    "{schema}\n\n"
    "## Dados da reuniao:\n\n"
    "**ID:** {meeting_id}\n"
    "**Nome:** {name}\n"
    "**Data:** {happened_at}\n"
    "**Duracao (minutos):** {duration_minutes}\n"
    "**Organizador:** {organizer}\n"
    "**Participantes:** {invitees}\n\n"
    "**TOPICOS (tldv AI):**\n"
    "{topics_text}\n\n"
    "**NOTAS ESTRUTURADAS:**\n"
    "{notes_text}\n\n"
    "**TRANSCRIPT (resumo - {word_count} palavras estimadas):**\n"
    "{transcript_text}\n\n"
    "Retorne SOMENTE o JSON."
)


def build_prompt(data: dict) -> tuple[str, str]:
    """Retorna (system_prompt, user_prompt)."""
    meeting_id = data["meeting_id"]
    ts = data.get("transcript_summary") or {}
    ns = (data.get("notes") or {}).get("structuredNotes") or []
    tp = data.get("topics") or []

    word_count = ts.get("total_words_estimate", 0) if isinstance(ts, dict) else 0

    # Transcript text
    if data.get("transcript"):
        raw = data["transcript"]
        if isinstance(raw, dict):
            raw = raw.get("data", raw)
        if isinstance(raw, list):
            raw = " ".join(f"[{s.get('speaker','?')}] {s.get('text','')}" for s in raw[:200])
        transcript_text = str(raw)[:8000]
    elif ts:
        transcript_text = json.dumps(ts, ensure_ascii=False)[:8000]
    else:
        transcript_text = "[TRANSCRIPT INDISPONIVEL]"

    # Notes text
    if ns:
        notes_text = "\n".join(
            f"- {n.get('timestamp','')}s: {n.get('text','')}"
            for n in ns[:100]
        )
    else:
        notes_text = "[NOTAS INDISPONIVEIS]"

    # Topics text
    if tp:
        topics_text = "\n".join(
            f"- [{t.get('order','')}] {t.get('title','')}: {t.get('summary','')}"
            for t in tp[:30]
        )
    else:
        topics_text = "[TOPICOS INDISPONIVEIS]"

    # Participants
    invitees = data.get("invitees") or []
    organizer = data.get("organizer") or {}
    participants = {}
    if organizer.get("name"):
        participants[organizer["name"]] = "Organizador"
    for inv in invitees:
        if isinstance(inv, dict) and inv.get("name"):
            participants[inv["name"]] = inv.get("role", "Participante")
        elif isinstance(inv, str):
            participants[inv] = "Participante"

    user_prompt = MEETING_ANALYSIS_USER_TEMPLATE.format(
        schema=_JSON_SCHEMA,
        meeting_id=meeting_id,
        name=data.get("name", "Sem nome"),
        happened_at=data.get("happened_at", ""),
        duration_minutes=round(data.get("duration_minutes", 0), 1),
        organizer=organizer.get("name", "Desconhecido"),
        invitees=", ".join(
            p.get("name", str(p)) for p in invitees
        ) or "Nao identificados",
        topics_text=topics_text,
        notes_text=notes_text,
        transcript_text=transcript_text,
        word_count=word_count,
    )

    return MEETING_ANALYSIS_SYSTEM, user_prompt


# Parse LLM Output

def parse_llm_json(raw: str) -> dict:
    """Extrai JSON puro da saida do LLM, removendo markdown fences."""
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
    raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw.strip(), strict=False)


# Markdown Renderer

def render_markdown(data: dict) -> str:
    meeting_id   = data["meeting_id"]
    name         = data["name"]
    happened_at  = data["happened_at"]
    meeting_type = data.get("context", {}).get("meeting_type", "internal")
    conf         = data.get("analysis_confidence", {})
    dur_min      = round(data.get("context", {}).get("duration_minutes", 0), 1)

    try:
        dt = datetime.fromisoformat(happened_at.replace("Z", "+00:00"))
        date_str = dt.strftime("%d/%m/%Y")
    except Exception:
        date_str = happened_at[:10] if happened_at else "N/A"

    t_ico  = "OK" if conf.get("transcript_available") else "NO"
    n_ico  = "OK" if conf.get("notes_available")      else "NO"
    conf_map = {"high": "HIGH", "medium": "MED", "low": "LOW"}
    conf_str = conf_map.get(conf.get("overall", "low"), "MED")

    lines = [
        f"# {name}",
        f"**Data:** {date_str} | **Duracao:** {dur_min}m | **Tipo:** {meeting_type}",
        "",
        "---",
        "",
        "## A. Resumo Executivo",
        data.get("executive_summary", ""),
        "",
        "---",
        "",
        "## B. Contexto e Leitura",
        f"**Objetivo:** {data.get('context', {}).get('purpose', 'N/A')}",
        f"**Participantes:** {format_participants(data.get('context', {}).get('participants_and_roles', {}))}",
        f"**Tipo:** {meeting_type}",
    ]

    limitation = data.get("context", {}).get("notes_limitation")
    if limitation:
        lines.append(f"**Limitacoes:** {limitation}")

    agenda = data.get("context", {}).get("main_agenda_items", [])
    if agenda:
        lines.append(f"**Agenda principal:** {', '.join(agenda)}")

    # C. Decisions
    lines += ["", "---", "", "## C. Decisoes Identificadas"]
    decisions = data.get("decisions", [])
    if not decisions:
        lines.append("- Nenhuma decisao identificada.")
    for d in decisions:
        dm = f"@{d['decision_maker']}" if d.get("decision_maker") else ""
        lines.append(f"- **[{d['id']}]** {d['description']} -- {dm} | {d['confidence'].capitalize()}")

    # D. Open Items
    lines += ["", "---", "", "## D. Pendencias em Aberto"]
    items = data.get("open_items", [])
    if not items:
        lines.append("- Nenhuma pendencia identificada.")
    for o in items:
        owner = f"@{o['owner']}" if o.get("owner") else ""
        deadline = o.get("deadline") or "sem prazo"
        blocked = f"Bloqueado por: {o['blocking_factor']}" if o.get("blocking_factor") else ""
        lines.append(f"- **[{o['id']}]** {o['description']} -- {owner} | {deadline} | {blocked}")

    # E. Tasks
    lines += ["", "---", "", "## E. Tarefas Geradas"]
    tasks = data.get("tasks", [])
    if not tasks:
        lines.append("- Nenhuma tarefa identificada.")
    for t in tasks:
        owner = f"@{t['owner']}" if t.get("owner") else ""
        deadline = t.get("deadline") or "sem prazo"
        lines.append(f"- **[{t['id']}]** {t['description']} -- {owner} | {deadline} | Prioridade: {t['priority'].capitalize()}")

    # F. Critical Questions
    lines += ["", "---", "", "## F. Perguntas Criticas"]
    qs = data.get("critical_questions", [])
    if not qs:
        lines.append("- Nenhuma pergunta critica identificada.")
    for q in qs:
        owner = f"@{q['owner']}" if q.get("owner") else ""
        by = f"Responder até: {q['answer_required_by']}" if q.get("answer_required_by") else "Sem prazo definido"
        lines.append(f"- **[{q['id']}]** {q['question']} -- contexto: {q['context']} | {by} {owner}")

    # G. Risks
    lines += ["", "---", "", "## G. Riscos e Alertas"]
    risks = data.get("risks_and_alerts", [])
    if not risks:
        lines.append("- Nenhum risco identificado.")
    sev_map = {"high": "[HIGH]", "medium": "[MED]", "low": "[LOW]"}
    for r in risks:
        sev = sev_map.get(r["severity"], "[MED]")
        mit = f"Mitigacao: {r['mitigation']}" if r.get("mitigation") else ""
        lines.append(f"- **[{r['id']}]** {r['type']} | Severidade: {sev} {r['description']} | {mit}")

    # H. Opportunities
    lines += ["", "---", "", "## H. Oportunidades"]
    ops = data.get("opportunities", [])
    if not ops:
        lines.append("- Nenhuma oportunidade identificada.")
    for op in ops:
        owner = f"Dono: @{op['owner']}" if op.get("owner") else ""
        lines.append(f"- **[{op['id']}]** {op['description']} -- Impacto: {op['potential_impact'].upper()} | {owner}")

    # I. Documentary Suggestions
    lines += ["", "---", "", "## I. Sugestoes de Atualizacao Documental"]
    ds = data.get("documentary_suggestions", [])
    if not ds:
        lines.append("- Nenhuma sugestao documental.")
    pri_map = {"high": "[HIGH]", "medium": "[MED]", "low": "[LOW]"}
    for d in ds:
        pri = pri_map.get(d["priority"], "[MED]")
        lines.append(f"- **[{d['id']}]** {pri} {d['action']} -> {d['destination']} | Razao: {d['reason']}")

    # J. Memories
    lines += ["", "---", "", "## J. Memorias a Registrar"]
    mems = data.get("memories_to_register", [])
    if not mems:
        lines.append("- Nenhuma memoria a registrar.")
    for m in mems:
        lines.append(f"- **[{m['id']}]** {m['memory']} -- categoria: {m['category']} | Confianca: {m['confidence']}")

    # K. Recommended Next Step
    rns = data.get("recommended_next_step") or {}
    lines += ["", "---", "", "## K. Proximo Passo Recomendado"]
    if rns.get("action"):
        owner = f"@{rns['owner']}" if rns.get("owner") else ""
        deadline = rns.get("deadline") or "sem prazo"
        lines += [
            f"**Acao:** {rns['action']}",
            f"**Dono:** {owner} | **Prazo:** {deadline}",
            f"**Por que:** {rns['reason']}",
        ]
    else:
        lines.append("- Nenhum proximo passo identificado.")

    # Footer
    generated_at = (data.get("analysis_generated_at", "")[:16].replace("T", " ") or "N/A")
    lines += [
        "",
        "---",
        f"[Analise gerada em: {generated_at} | Confianca: {conf_str} | Transcript: {t_ico} Notes: {n_ico}]",
    ]
    return "\n".join(lines)


def format_participants(participants: dict) -> str:
    if not participants:
        return "Nao identificados"
    return ", ".join(f"{name} ({role})" for name, role in participants.items())


# Ledger

def load_ledger() -> dict:
    if LEDGER_FILE.exists():
        return json.loads(LEDGER_FILE.read_text())
    return {"version": LEDGER_VERSION, "analyzed": []}


def save_ledger(ledger: dict) -> None:
    LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
    LEDGER_FILE.write_text(json.dumps(ledger, indent=2, ensure_ascii=False))


def is_analyzed(ledger: dict, meeting_id: str) -> bool:
    return meeting_id in ledger.get("analyzed", [])


# Analyze Single Meeting

def analyze_meeting(
    meeting_id: str,
    reanalysis: bool = False,
    dry_run: bool = False,
) -> dict:
    """
    Retorna dict com keys: status, meeting_id, detail.
    status: 'analyzed' | 'skipped' | 'error' | 'dry-run'
    """
    normalized_path = NORMALIZED / f"{meeting_id}.json"
    if not normalized_path.exists():
        return {"status": "error", "meeting_id": meeting_id,
                "detail": "Arquivo normalizado nao encontrado"}

    data = json.loads(normalized_path.read_text())

    ledger = load_ledger()
    if not reanalysis and is_analyzed(ledger, meeting_id):
        return {"status": "skipped", "meeting_id": meeting_id,
                "detail": "Ja analisada"}

    # BLOCK: if API returned 404 (not_found), mark as analyzed so pipeline skips forever
    if data.get("not_found"):
        logger.error(f"Meeting {meeting_id} returned 404 in API — blocking permanently")
        if meeting_id not in ledger["analyzed"]:
            ledger["analyzed"].append(meeting_id)
            LEDGER_FILE.write_text(json.dumps(ledger, indent=2))
        return {"status": "blocked", "meeting_id": meeting_id,
                "detail": "404_not_found_API"}

    if dry_run:
        return {"status": "dry-run", "meeting_id": meeting_id,
                "detail": "Dry run -- nao executa analise"}

    # Availability flags
    ts_available = bool(data.get("transcript_summary") or data.get("transcript"))
    ns_available = bool((data.get("notes") or {}).get("structuredNotes"))
    tp_available  = bool(data.get("topics"))

    # Build prompts
    system_prompt, user_prompt = build_prompt(data)

    # LLM call
    print(f"  [INFO] Chamando LLM ({DEFAULT_MODEL})...")
    raw = call_llm(f"{system_prompt}\n\n{user_prompt}")
    if not raw:
        return {"status": "error", "meeting_id": meeting_id,
                "detail": "LLM retornou resposta vazia"}

    # Parse JSON
    try:
        parsed = parse_llm_json(raw)
    except json.JSONDecodeError as e:
        return {"status": "error", "meeting_id": meeting_id,
                "detail": f"JSON parse error: {e}\nRaw: {raw[:300]}"}

    # Enrich metadata
    parsed["meeting_id"] = meeting_id
    parsed["name"] = data.get("name") or parsed.get("name") or "Sem nome"
    parsed["happened_at"] = data.get("happened_at") or parsed.get("happened_at") or ""
    parsed["analysis_version"] = "1.0"
    parsed["analysis_generated_at"] = datetime.now(timezone.utc).isoformat()

    # Analysis confidence
    parsed.setdefault("analysis_confidence", {})
    ac = parsed["analysis_confidence"]
    ac["transcript_available"] = ts_available
    ac["notes_available"] = ns_available
    ac["topics_available"] = tp_available
    if not ts_available and not ns_available:
        ac["overall"] = "low"
        ac.setdefault("gaps", []).append("Transcript e notas indisponiveis -- analise limitada")
    elif not ts_available:
        ac["overall"] = "medium"
        ac.setdefault("gaps", []).append("Transcript indisponivel -- analise baseada em notas")

    # Context
    parsed["context"] = parsed.get("context") or {}
    parsed["context"]["duration_minutes"] = round(data.get("duration_minutes", 0), 1)
    if not parsed["context"].get("participants_and_roles"):
        invitees = data.get("invitees") or []
        organizer = data.get("organizer") or {}
        participants = {}
        if organizer.get("name"):
            participants[organizer["name"]] = "Organizador"
        for inv in invitees:
            if isinstance(inv, dict) and inv.get("name"):
                participants[inv["name"]] = inv.get("role", "Participante")
            elif isinstance(inv, str):
                participants[inv] = "Participante"
        parsed["context"]["participants_and_roles"] = participants

    if not ts_available and ns_available:
        parsed["context"]["notes_limitation"] = (
            "Transcript nao disponivel. Analise feita com base nas notas estruturadas "
            "do tldv, que podem nao capturar toda a nuança da conversa."
        )
    elif not ts_available:
        parsed["context"]["notes_limitation"] = (
            "Transcript e notas estruturadas indisponiveis. "
            "Dados muito limitados para analise confiavel."
        )
    else:
        parsed["context"]["notes_limitation"] = None

    # raw_topics_from_tldv
    if not parsed.get("raw_topics_from_tldv"):
        tp = data.get("topics") or []
        parsed["raw_topics_from_tldv"] = [t.get("title", "") for t in tp if t.get("title")]

    # Write outputs
    ANALYSIS.mkdir(parents=True, exist_ok=True)
    json_path = ANALYSIS / f"{meeting_id}.json"
    json_path.write_text(json.dumps(parsed, indent=2, ensure_ascii=False))
    md_path = ANALYSIS / f"{meeting_id}.md"
    md_path.write_text(render_markdown(parsed), encoding="utf-8")

    # Update ledger
    ledger = load_ledger()
    if meeting_id not in ledger["analyzed"]:
        ledger["analyzed"].append(meeting_id)
    save_ledger(ledger)

    return {"status": "analyzed", "meeting_id": meeting_id,
            "detail": str(json_path)}


# CLI

def main() -> None:
    parser = argparse.ArgumentParser(
        description="tl;dv Meeting Analyzer - Morfeu",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--limit", type=int, default=0,
                        help="Limite de reunioes a processar")
    parser.add_argument("--meeting-id", type=str, default="",
                        help="Processar uma reuniao especifica")
    parser.add_argument("--dry-run", action="store_true",
                        help="Mostrar o que faria sem rodar")
    parser.add_argument("--reanalysis", action="store_true",
                        help="Refaz mesmo ja analisados")
    args = parser.parse_args()

    ANALYSIS.mkdir(parents=True, exist_ok=True)

    # Single meeting mode
    if args.meeting_id:
        result = analyze_meeting(
            args.meeting_id,
            reanalysis=args.reanalysis,
            dry_run=args.dry_run,
        )
        icons = {
            "analyzed": "OK", "skipped": "SKIP",
            "error": "ERR", "dry-run": "DRY",
        }
        icon = icons.get(result["status"], "?")
        print(f"[{icon}] {result['meeting_id']}: {result['detail']}")
        sys.exit(0 if result["status"] != "error" else 1)

    # Batch mode
    ledger = load_ledger()
    all_ids = sorted(p.stem for p in NORMALIZED.glob("*.json"))

    if args.reanalysis:
        to_process = all_ids
    else:
        to_process = [mid for mid in all_ids if not is_analyzed(ledger, mid)]

    if not to_process:
        print("Nenhuma reuniao para processar.")
        sys.exit(0)

    if args.limit:
        to_process = to_process[: args.limit]

    print(f"[INFO] {len(to_process)} reuniao(oes) para processar "
          f"(dry_run={args.dry_run}, reanalysis={args.reanalysis})")
    print()

    results = []
    for mid in to_process:
        print(f"[RUN] {mid}")
        result = analyze_meeting(mid, reanalysis=args.reanalysis, dry_run=args.dry_run)
        icons = {
            "analyzed": "OK", "skipped": "SKIP",
            "error": "ERR", "dry-run": "DRY",
        }
        icon = icons.get(result["status"], "?")
        print(f"  [{icon}] {result['detail']}")
        results.append(result)
        print()

    analyzed = sum(1 for r in results if r["status"] == "analyzed")
    skipped  = sum(1 for r in results if r["status"] == "skipped")
    errors   = sum(1 for r in results if r["status"] == "error")
    print(f"[SUMMARY] {analyzed} analisadas | {skipped} puladas | {errors} erros")


if __name__ == "__main__":
    main()
