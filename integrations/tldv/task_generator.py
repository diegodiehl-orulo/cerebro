#!/usr/bin/env python3
"""
task_generator.py — Gera tarefas estruturadas a partir de análises tl;dv
======================================================================

Lê cada análise em memory/meetings/analysis/ e gera:
  - tasks/generated-from-meetings/{meetingId}.json   (tarefa por reunião)
  - tasks/generated-from-meetings/{meetingId}.md      (humano)
  - tasks/consolidated/{YYYY-MM}.json                (visão por mês)
  - tasks/consolidated/by_owner.json                  (por responsável)

Resumo final com:
  - tarefas críticas
  - tarefas sem dono
  - tarefas sem prazo
  - bloqueios recorrentes

Uso:
  python3 task_generator.py                # processa todas
  python3 task_generator.py --dry-run     # mostra o que faria
  python3 task_generator.py --meeting-id X # só uma reunião
  python3 task_generator.py --since YYYY-MM-DD  # só após data
  python3 task_generator.py --consolidated-only  # só consolida
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace")
ANALYSIS_DIR = WORKSPACE / "memory/meetings/analysis"
TASKS_DIR = WORKSPACE / "tasks"
GENERATED_DIR = WORKSPACE / "memory/meetings/tasks"  # per-meeting task outputs
CONSOLIDATED_DIR = TASKS_DIR / "consolidated"
LEDGER_FILE = WORKSPACE / "memory/meetings/ledger/tasks_ledger.json"
LOG_FILE = WORKSPACE / "logs/tldv_task_generator.log"

os_environ = __import__('os').environ
os_environ.setdefault("TLDV_API_KEY", "69f9a821-7286-46e8-a64c-7c1f20a01576")


def log(msg):
    ts = datetime.now().isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


# ── Classificador de tarefa ────────────────────────────────────────────────────

class TaskClassifier:
    """
    Classifica cada item de análise em tipo de tarefa.
    Diferencia:
      - EXPLÍCITA: mencionada como ação, com verbo de comando
      - FOLLOW_UP: alguém precisa dar retorno
      - DECISION_PENDING: depende de decisão de alguém
      - INFO_NEEDED: precisa de mais contexto antes de virar tarefa
    """

    EXPLICT_verbs = {
        "criar", "definir", "agendar", "marcar", "enviar", "mandar",
        "preparar", "elaborar", "desenvolver", "implementar", "revisar",
        "atualizar", "construir", "fazer", "realizar", "conectar",
        "programar", "confirmar", "validar", "testar", "documentar",
        "registrar", "analisar", "estudar", "avaliar", "organizar",
    }

    FOLLOW_UP_verbs = {
        "verificar", "checar", "conferir", "acompanhar", "追问",
        "cobrar", "follow-up", "dar retorno", "retornar", "feedback",
    }

    DECISION_markers = {
        "depende de", "aguarda", "aguardando", "precisa decidir",
        "decisão do", "aprovação", "confirmar com", "validar com",
    }

    def __init__(self, text: str):
        self.text = text.strip()
        self.lower = self.text.lower()
        self.first_word = self.lower.split()[0] if self.lower.split() else ""

    def classify(self) -> str:
        if self._is_explicit():
            return "EXPLICITA"
        if self._is_follow_up():
            return "FOLLOW_UP"
        if self._is_decision_pending():
            return "DECISION_PENDING"
        if self._is_info_needed():
            return "INFO_NEEDED"
        return "OBSERVACAO"

    def _is_explicit(self) -> bool:
        # Verbo explícito no início
        if self.first_word in self.EXPLICT_verbs:
            return True
        # Padrão "verb [subject]"
        pattern = r"^(criar|definir|agendar|enviar|preparar|implementar|revisar|atualizar|construir|fazer|realizar|confirmar|validar|documentar|registrar|analisar|programar)"
        if re.search(pattern, self.lower):
            return True
        # Checklist markers: "- [ ]", "TODO:"
        if re.search(r"^[-*]\s*\[[ x]\]", self.text):
            return True
        if re.search(r"^todo:", self.lower):
            return True
        return False

    def _is_follow_up(self) -> bool:
        for v in self.FOLLOW_UP_verbs:
            if v in self.lower:
                return True
        return False

    def _is_decision_pending(self) -> bool:
        for m in self.DECISION_markers:
            if m in self.lower:
                return True
        return False

    def _is_info_needed(self) -> bool:
        question_words = ["quem", "quando", "onde", "como", "por que", "qual", "que "]
        if any(w in self.lower for w in question_words):
            return len(self.text) < 40  # Curta + pergunta = precisa contexto
        return False

    def priority(self) -> str:
        """Infere prioridade."""
        high_markers = ["urgente", "crítico", "bloqueante", "imediato", "hoje", "agora", "[high]"]
        medium_markers = ["semana", "[medium]", "prioridade média", "em breve"]
        if any(m in self.lower for m in high_markers):
            return "HIGH"
        if any(m in self.lower for m in medium_markers):
            return "MEDIUM"
        return "MEDIUM"  # default

    def owner(self) -> str | None:
        """Extrai responsável se mencionado."""
        patterns = [
            r"@\(?([A-Z][a-z]+ [A-Z][a-z]+)\)?",  # @(Diego Diehl)
            r"dono:?\s*([A-Z][a-z]+)",              # Dono: Diego
            r"responsável:?\s*([A-Z][a-z]+)",
            r"Owner:?\s*([A-Z][a-z]+)",
        ]
        for p in patterns:
            m = re.search(p, self.text)
            if m:
                return m.group(1).strip()
        return None

    def deadline(self) -> str | None:
        """Extrai prazo se mencionado."""
        # Data ISO: 2026-04-30
        m = re.search(r"(\d{4}-\d{2}-\d{2})", self.text)
        if m:
            return m.group(1)
        # Data BR: 30/04/2026
        m = re.search(r"(\d{2}/\d{2}/\d{4})", self.text)
        if m:
            return m.group(1)
        return None

    def area(self) -> str:
        """Infere área/projeto."""
        area_markers = {
            "WS1": ["ws1", "ws-1", "comunicação", "corretor", "marketing"],
            "WS2": ["ws2", "ws-2", "dl", "dl→pago", "jornada"],
            "WS3": ["ws3", "ws-3", "praça", "território", "venda"],
            "WS4": ["ws4", "ws-4", "crm", "bitrix"],
            "WS5": ["ws5", "ws-5", "evento", "marketing"],
            "WS6": ["ws6", "ws-6", "embaixador", "embaixadora"],
            "WS7": ["ws7", "ws-7", "modelo econômico", "mrr", "faturamento"],
            "Produto": ["produto", "z2a", "platform", "feature"],
            "Comercial": ["venda", "pipeline", "forecast", "cliente"],
            "Gente": ["time", "contratação", "onboard", "treinamento"],
            "Financeiro": ["financeiro", "pagamento", "recebível", "cri"],
        }
        text_lower = self.lower
        for area, markers in area_markers.items():
            if any(m in text_lower for m in markers):
                return area
        return "Geral"


# ── Tarefa estruturada ─────────────────────────────────────────────────────────

def build_task(item: dict, meeting_id: str, happened_at: str, task_id: str, 
               raw_category: str) -> dict:
    """Constrói tarefa estruturada a partir de um item de análise."""
    text = item.get("description") or item.get("text", "")
    classifier = TaskClassifier(text)

    return {
        "id": task_id,
        "title": text[:100],
        "description": text,
        "owner": item.get("owner") or classifier.owner(),
        "deadline": item.get("deadline") or classifier.deadline(),
        "priority": item.get("priority") or classifier.priority(),
        "area": item.get("area") or classifier.area(),
        "project": item.get("project") or None,
        "type": classifier.classify(),
        "status": "OPEN",
        "source_meeting": meeting_id,
        "source_category": raw_category,
        "source_date": happened_at[:10] if happened_at else None,
        "dependencies": item.get("dependencies") or [],
        "completion_criteria": item.get("completion_criteria") or None,
        "confidence": item.get("confidence") or "MEDIUM",
        "blocking_factor": item.get("blocking_factor") or None,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }


# ── Deduplicação ─────────────────────────────────────────────────────────────

def signature(task: dict) -> str:
    """Assinatura de dedup: área + título limpo."""
    title = re.sub(r"\s+", " ", task["title"].lower())
    title = re.sub(r"[^a-zà-ÿ0-9 ]", "", title)
    return f"{task.get('area','X')}:{title[:60]}"


def load_seen_sigs() -> set:
    sigs_file = WORKSPACE / "memory/meetings/ledger/task_sigs.txt"
    if sigs_file.exists():
        return set(sigs_file.read_text().splitlines())
    return set()


def save_seen_sigs(sigs: set):
    sigs_file = WORKSPACE / "memory/meetings/ledger/task_sigs.txt"
    sigs_file.parent.mkdir(parents=True, exist_ok=True)
    sigs_file.write_text("\n".join(sorted(sigs)))


# ── Per-meeting task file ────────────────────────────────────────────────────

def generate_meeting_tasks(meeting_id: str, analysis: dict) -> list[dict]:
    """Gera tarefas estruturadas para uma reunião."""
    happened = analysis.get("happened_at", "")
    tasks = []
    task_num = 1

    all_items = []

    # Tarefas explícitas
    for t in analysis.get("tasks", []):
        t["_cat"] = "task"
        all_items.append(t)

    # Open items
    for o in analysis.get("open_items", []):
        o["_cat"] = "open_item"
        all_items.append(o)

    # Próximo passo
    nxt = analysis.get("recommended_next_step") or {}
    if nxt.get("action"):
        all_items.append({
            "description": nxt["action"],
            "owner": nxt.get("owner"),
            "deadline": nxt.get("deadline"),
            "priority": "HIGH",
            "_cat": "recommended_next_step",
        })

    # Critical questions (como follow-up)
    for q in analysis.get("critical_questions", []):
        all_items.append({
            "description": q.get("question", ""),
            "owner": q.get("owner"),
            "deadline": q.get("answer_required_by"),
            "priority": "MEDIUM",
            "_cat": "critical_question",
        })

    # Risks high/medium (podem virar ação)
    for r in analysis.get("risks_and_alerts", []):
        if r.get("severity") in ("high", "medium"):
            all_items.append({
                "description": f"[RISCO] {r.get('description','')}",
                "owner": r.get("owner"),
                "priority": r.get("severity", "medium").upper(),
                "_cat": "risk",
            })

    # Dedup only intra-meeting (sigs from previous meetings are NOT checked)
    seen_in_meeting = set()

    for item in all_items:
        raw_cat = item.pop("_cat", "?")
        text = item.get("description") or item.get("text", "")
        if not text or len(text) < 10:
            continue

        task = build_task(item, meeting_id, happened,
                          f"T{meeting_id[:8]}-{task_num:03d}", raw_cat)
        sig = signature(task)

        # Intra-meeting dedup only
        if sig in seen_in_meeting:
            continue
        seen_in_meeting.add(sig)
        tasks.append(task)
        task_num += 1

    return tasks


def write_meeting_output(meeting_id: str, tasks: list[dict], analysis: dict):
    """Escreve .json e .md por reunião."""
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    # JSON
    out_json = {
        "meeting_id": meeting_id,
        "meeting_name": analysis.get("name", "?"),
        "happened_at": analysis.get("happened_at", ""),
        "tasks": tasks,
        "summary": {
            "total": len(tasks),
            "by_priority": {
                "HIGH": len([t for t in tasks if t["priority"] == "HIGH"]),
                "MEDIUM": len([t for t in tasks if t["priority"] == "MEDIUM"]),
                "LOW": len([t for t in tasks if t["priority"] == "LOW"]),
            },
            "by_type": {
                t["type"]: len([x for x in tasks if x["type"] == t["type"]])
                for t in tasks
            },
            "without_owner": len([t for t in tasks if not t["owner"]]),
            "without_deadline": len([t for t in tasks if not t["deadline"]]),
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    with open(GENERATED_DIR / f"{meeting_id}.json", "w", encoding="utf-8") as f:
        json.dump(out_json, f, indent=2, ensure_ascii=False)

    # Markdown
    lines = [
        f"# Tarefas — {analysis.get('name', meeting_id)}",
        f"**Data:** {analysis.get('happened_at', '')[:10]} | "
        f"**Tarefas:** {len(tasks)} | "
        f"**Sem dono:** {len([t for t in tasks if not t['owner']])}",
        "",
        "---",
        "",
        "## Por Prioridade",
        "",
    ]
    for priority in ["HIGH", "MEDIUM", "LOW"]:
        pts = [t for t in tasks if t["priority"] == priority]
        if pts:
            lines.append(f"### {priority} ({len(pts)})")
            for t in pts:
                owner = f"@({t['owner']})" if t["owner"] else "_(sem dono)_"
                deadline = f"⏰ {t['deadline']}" if t["deadline"] else "_(sem prazo)_"
                area = f"[{t['area']}]" if t["area"] else ""
                lines.append(f"- **{t['title'][:80]}**")
                lines.append(f"  - ID: `{t['id']}` | {owner} | {deadline} | {area}")
                lines.append(f"  - Tipo: `{t['type']}` | Origem: `{t['source_category']}`")

    if tasks:
        lines.append("")
        lines.append("## Detalhamento")
        for t in tasks:
            lines.append(f"### `{t['id']}`")
            lines.append(f"**{t['title']}**")
            lines.append(f"- Dono: {t['owner'] or 'N/A'}")
            lines.append(f"- Prazo: {t['deadline'] or 'não definido'}")
            lines.append(f"- Prioridade: {t['priority']}")
            lines.append(f"- Área: {t['area']}")
            lines.append(f"- Tipo: {t['type']}")
            lines.append(f"- Status: {t['status']}")
            lines.append(f"- Critério de conclusão: {t['completion_criteria'] or 'não definido'}")
            lines.append(f"- Bloqueio: {t['blocking_factor'] or 'nenhum'}")
            lines.append(f"- Fonte: [{t['source_meeting']}](/{t['source_date']}) `({t['source_category']})`")

    lines.append("")
    lines.append(f"*Gerado em {datetime.now().strftime('%d/%m %H:%M')} | tl;dv pipeline*")

    with open(GENERATED_DIR / f"{meeting_id}.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ── Consolidação ─────────────────────────────────────────────────────────────

def consolidate(all_tasks: list[dict]) -> dict:
    """Gera visões consolidadas."""

    # Por mês
    by_month = defaultdict(list)
    for t in all_tasks:
        month = (t.get("source_date") or "0000-00")[:7]
        by_month[month].append(t)

    # Por dono
    by_owner = defaultdict(list)
    for t in all_tasks:
        owner = t.get("owner") or "_SEM_DONO_"
        by_owner[owner].append(t)

    # Estatísticas
    stats = {
        "total": len(all_tasks),
        "HIGH": len([t for t in all_tasks if t["priority"] == "HIGH"]),
        "MEDIUM": len([t for t in all_tasks if t["priority"] == "MEDIUM"]),
        "LOW": len([t for t in all_tasks if t["priority"] == "LOW"]),
        "EXPLICITA": len([t for t in all_tasks if t["type"] == "EXPLICITA"]),
        "FOLLOW_UP": len([t for t in all_tasks if t["type"] == "FOLLOW_UP"]),
        "DECISION_PENDING": len([t for t in all_tasks if t["type"] == "DECISION_PENDING"]),
        "without_owner": len([t for t in all_tasks if not t.get("owner")]),
        "without_deadline": len([t for t in all_tasks if not t.get("deadline")]),
    }

    return {
        "stats": stats,
        "by_month": {m: len(v) for m, v in sorted(by_month.items(), reverse=True)},
        "by_owner": {o: len(v) for o, v in sorted(by_owner.items(), key=lambda x: -len(x[1]))},
        "tasks": all_tasks,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def write_consolidated(consolidated: dict):
    """Escreve visões consolidadas."""
    CONSOLIDATED_DIR.mkdir(parents=True, exist_ok=True)

    # Full consolidated JSON
    with open(CONSOLIDATED_DIR / "all_tasks.json", "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)

    # By owner
    by_owner_data = {
        "stats": consolidated["stats"],
        "by_owner": {
            owner: {
                "count": len(tasks),
                "HIGH": len([t for t in tasks if t["priority"] == "HIGH"]),
                "MEDIUM": len([t for t in tasks if t["priority"] == "MEDIUM"]),
                "without_deadline": len([t for t in tasks if not t.get("deadline")]),
                "tasks": sorted(tasks, key=lambda t: (t["priority"] != "HIGH", t.get("deadline") or "z"))
            }
            for owner, tasks in _group_by_owner(consolidated["tasks"]).items()
        },
        "generated_at": consolidated["generated_at"],
    }
    with open(CONSOLIDATED_DIR / "by_owner.json", "w", encoding="utf-8") as f:
        json.dump(by_owner_data, f, indent=2, ensure_ascii=False)

    # Monthly
    for month, tasks in _group_by_month(consolidated["tasks"]).items():
        month_file = CONSOLIDATED_DIR / f"{month}.json"
        with open(month_file, "w", encoding="utf-8") as f:
            json.dump({
                "month": month,
                "tasks": tasks,
                "count": len(tasks),
                "generated_at": consolidated["generated_at"],
            }, f, indent=2, ensure_ascii=False)


def _group_by_owner(tasks: list[dict]) -> dict:
    by = defaultdict(list)
    for t in tasks:
        by[t.get("owner") or "_SEM_DONO_"].append(t)
    return dict(by)


def _group_by_month(tasks: list[dict]) -> dict:
    by = defaultdict(list)
    for t in tasks:
        by[(t.get("source_date") or "0000-00")[:7]].append(t)
    return dict(sorted(by.items(), reverse=True))


# ── Resumo executivo ──────────────────────────────────────────────────────────

def generate_summary(all_tasks: list[dict], analysis_count: int) -> str:
    """Gera sumário em markdown."""
    lines = [
        "# tl;dv — Resumo de Tarefas Geradas",
        f"**Reuniões processadas:** {analysis_count}",
        f"**Gerado em:** {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        "",
        "---",
        "",
        f"## Visão Geral ({len(all_tasks)} tarefas)",
        "",
        f"| Prioridade | Qtd |",
        f"|---|---|",
        f"| 🔴 HIGH | {len([t for t in all_tasks if t['priority']=='HIGH'])} |",
        f"| 🟡 MEDIUM | {len([t for t in all_tasks if t['priority']=='MEDIUM'])} |",
        f"| 🟢 LOW | {len([t for t in all_tasks if t['priority']=='LOW'])} |",
        "",
        "---",
        "",
    ]

    # Críticas (HIGH + sem dono ou sem prazo)
    critical = [t for t in all_tasks
                if t["priority"] == "HIGH"
                and (not t.get("owner") or not t.get("deadline"))]
    if critical:
        lines += ["## 🔴 Críticas (HIGH + sem dono ou sem prazo)", ""]
        for t in critical[:10]:
            lines.append(f"- **{t['title'][:80]}**")
            lines.append(f"  - ID: `{t['id']}` | Sem dono: {not t.get('owner')} | Sem prazo: {not t.get('deadline')}")
            lines.append(f"  - Área: {t['area']} | Origem: [{t['source_meeting'][:12]}...](/{t.get('source_date','?')})")
        lines.append("")

    # Sem dono
    no_owner = [t for t in all_tasks if not t.get("owner")]
    if no_owner:
        lines += ["## ⚠️ Sem Dono (priorizar atribuição)", ""]
        for t in sorted(no_owner, key=lambda x: x["priority"] != "HIGH")[:15]:
            prio_emoji = "🔴" if t["priority"] == "HIGH" else "🟡"
            lines.append(f"- {prio_emoji} **{t['title'][:80]}**")
            lines.append(f"  - `{t['id']}` | {t['area']} | Tipo: {t['type']}")
        lines.append("")

    # Sem prazo
    no_deadline = [t for t in all_tasks if not t.get("deadline") and t.get("owner")]
    if no_deadline:
        lines += ["## ⚠️ Sem Prazo (definir urgência)", ""]
        for t in sorted(no_deadline, key=lambda x: x["priority"] != "HIGH")[:15]:
            owner = f"@({t['owner']})" if t['owner'] else ""
            prio_emoji = "🔴" if t["priority"] == "HIGH" else "🟡"
            lines.append(f"- {prio_emoji} **{t['title'][:80]}** {owner}")
            lines.append(f"  - `{t['id']}` | Área: {t['area']}")
        lines.append("")

    # Decisões pendentes
    decisions = [t for t in all_tasks if t["type"] == "DECISION_PENDING"]
    if decisions:
        lines += ["## 🗳️ Decisões Pendentes", ""]
        for t in decisions[:10]:
            lines.append(f"- **{t['title'][:80]}**")
            lines.append(f"  - {t.get('owner') or 'Dono não definido'} | {t['area']}")
        lines.append("")

    # Follow-ups
    followups = [t for t in all_tasks if t["type"] == "FOLLOW_UP"]
    if followups:
        lines += ["## 🔄 Follow-ups", ""]
        for t in followups[:10]:
            lines.append(f"- **{t['title'][:80]}**")
            lines.append(f"  - {t.get('owner') or '?'} | Deadline: {t.get('deadline') or 'a definir'}")
        lines.append("")

    # Bloqueios recorrentes
    blocks = defaultdict(int)
    for t in all_tasks:
        if t.get("blocking_factor"):
            blocks[t["blocking_factor"]] += 1
    if blocks:
        lines += ["## 🚧 Bloqueios Recorrentes", ""]
        for block, count in sorted(blocks.items(), key=lambda x: -x[1])[:10]:
            lines.append(f"- ({count}x) {block}")
        lines.append("")

    # Por dono
    by_owner = _group_by_owner(all_tasks)
    if by_owner:
        lines += ["## 👤 Por Responsável", ""]
        for owner, tasks in sorted(by_owner.items(), key=lambda x: -len(x[1]))[:15]:
            high = len([t for t in tasks if t["priority"] == "HIGH"])
            lines.append(f"- **{owner}**: {len(tasks)} tarefas"
                         + (f" 🔴{high} HIGH" if high else ""))

    lines += ["", f"*Gerado por Morfeu | {len(all_tasks)} tarefas de {analysis_count} reuniões*"]
    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def load_ledger() -> dict:
    if LEDGER_FILE.exists():
        with open(LEDGER_FILE) as f:
            return json.load(f)
    return {"generated": [], "total_tasks": 0}


def save_ledger(ledger: dict):
    LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f, indent=2)


def main():
    import os as _os
    _os.environ.setdefault("TLDV_API_KEY", "69f9a821-7286-46e8-a64c-7c1f20a01576")

    parser = argparse.ArgumentParser(description="Task generator from tl;dv analyses")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--meeting-id", type=str, default="")
    parser.add_argument("--since", type=str, default="", help="YYYY-MM-DD")
    parser.add_argument("--consolidated-only", action="store_true")
    args = parser.parse_args()

    since_dt = None
    if args.since:
        since_dt = datetime.fromisoformat(args.since)

    ledger = load_ledger()
    generated_ids = set(ledger.get("generated", []))

    # Load analyses
    if args.meeting_id:
        all_analyses = [(ANALYSIS_DIR / f"{args.meeting_id}.json", args.meeting_id)]
    else:
        all_analyses = [(p, p.stem) for p in sorted(ANALYSIS_DIR.glob("*.json"))]

    pending = [
        (p, mid) for p, mid in all_analyses
        if mid not in generated_ids
    ]

    if args.consolidated_only:
        analyses_to_process = []
    elif args.meeting_id:
        analyses_to_process = all_analyses
    else:
        analyses_to_process = pending

    if not analyses_to_process and not args.consolidated_only:
        log("Nenhuma análise nova para processar.")
        return

    all_tasks = []
    processed = 0

    for path, meeting_id in analyses_to_process:
        try:
            with open(path) as f:
                analysis = json.load(f)
        except Exception as e:
            log(f"Erro lendo {meeting_id}: {e}")
            continue

        happened = analysis.get("happened_at", "")
        if since_dt and happened:
            try:
                dt = datetime.fromisoformat(happened.replace("Z", "+00:00"))
                if dt < since_dt:
                    continue
            except Exception:
                pass

        if not args.consolidated_only:
            tasks = generate_meeting_tasks(meeting_id, analysis)
            if not args.dry_run:
                write_meeting_output(meeting_id, tasks, analysis)
            log(f"  {meeting_id}: {len(tasks)} tarefas geradas"
                + (" (DRY)" if args.dry_run else ""))
            all_tasks.extend(tasks)

        ledger["generated"].append(meeting_id)
        processed += 1

    if not args.consolidated_only:
        save_ledger(ledger)

    # Load existing tasks for consolidated view
    for p in GENERATED_DIR.glob("*.json"):
        mid = p.stem
        if mid == "all_tasks":  # skip consolidated
            continue
        if args.since:
            # skip already counted
            pass
        try:
            with open(p) as f:
                data = json.load(f)
                all_tasks.extend(data.get("tasks", []))
        except Exception:
            pass

    # Consolidated
    if all_tasks:
        consolidated = consolidate(all_tasks)
        if not args.dry_run:
            write_consolidated(consolidated)
        summary = generate_summary(all_tasks, processed or len(all_analyses))
        summary_file = CONSOLIDATED_DIR / "SUMMARY.md"
        if not args.dry_run:
            summary_file.write_text(summary)
        log(f"Consolidado: {len(all_tasks)} tarefas | Sem dono: {consolidated['stats']['without_owner']} | Sem prazo: {consolidated['stats']['without_deadline']}")
        print(f"\n{summary}")

    log(f"Task generator finalizado. Processados: {processed} | Total tarefas: {len(all_tasks)}")


if __name__ == "__main__":
    main()
