#!/usr/bin/env python3
"""
persister.py — Camada de persistência de análises tl;dv
========================================================
Lê análises de memory/meetings/analysis/ e persite conteúdo útil em:
  - memory/decisions.md
  - memory/lessons.md
  - memory/pending.md (merge)
  - memory/projects.md (merge)
  - memory/risks.md
  - memory/preferences.md
  - memory/commercial_context.md
  - docs/meeting-derived-updates/ (patches prontos)

Uso:
  python3 persister.py              # processa todas as análises
  python3 persister.py --dry-run    # mostra o que faria
  python3 persister.py --limit 5    # testa com 5
  python3 persister.py --since YYYY-MM-DD  # só análises após data
"""

import hashlib
import json
import re
import sys
import argparse
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DIRS, LEDGERS, WORKSPACE  # noqa: E402

# ── Paths ────────────────────────────────────────────────────────────────────

ANALYSIS_DIR  = DIRS["analysis"]
LEDGER_FILE   = LEDGERS["persisted"]
UPDATES_DIR   = DIRS["updates"]
LOG_FILE      = DIRS["logs"] / "tldv_persister.log"

# Only DIRECT write targets. pending.md and projects.md have specific formats
# — we generate patches for them instead.
DIRECT_TARGETS = {
    "decision":    WORKSPACE / "memory" / "decisions.md",
    "lesson":      WORKSPACE / "memory" / "lessons.md",
    "risk":        WORKSPACE / "memory" / "risks.md",
    "preference":  WORKSPACE / "memory" / "preferences.md",
    "context":     WORKSPACE / "memory" / "commercial_context.md",
}
# These get patches only — do NOT write directly
PATCH_ONLY = {"pending", "project"}
ALL_CATS = set(DIRECT_TARGETS.keys()) | PATCH_ONLY

# ── Log ─────────────────────────────────────────────────────────────────────

def log(msg: str):
    ts = datetime.now().isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


# ── Deduplicação ─────────────────────────────────────────────────────────────

def _normalize_text(text: str) -> str:
    """
    Normalização mais forte para dedup semântica:
      - lowercase
      - sem acentos (NFD + strip combining)
      - sem pontuação (mantém letras/dígitos/espaço)
      - colapsa whitespace
      - remove stopwords muito comuns que não diferenciam sentido
    """
    t = text.strip().lower()
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    stopwords = {"a", "o", "e", "de", "do", "da", "em", "um", "uma",
                 "para", "por", "com", "que", "no", "na", "os", "as",
                 "the", "of", "and", "to", "in", "for", "on", "at"}
    t = " ".join(w for w in t.split() if w not in stopwords)
    return t


class DedupStore:
    """
    Hash-based dedup: evita registrar mesmo conteúdo duas vezes.
    Usa SHA256 do texto normalizado como fingerprint.
    """

    def __init__(self, hash_file: Path):
        self.hash_file = hash_file
        self.seen: set[str] = set()
        if hash_file.exists():
            self.seen = set(hash_file.read_text().splitlines())

    def is_new(self, text: str) -> bool:
        normalized = _normalize_text(text)
        if not normalized:
            return False
        h = hashlib.sha256(normalized.encode()).hexdigest()[:32]
        if h in self.seen:
            return False
        self.seen.add(h)
        return True

    def save(self):
        self.hash_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.hash_file, "w") as f:
            f.write("\n".join(sorted(self.seen)))


def load_persisted_ledger() -> dict:
    if LEDGER_FILE.exists():
        with open(LEDGER_FILE) as f:
            return json.load(f)
    return {"persisted": [], "skipped": 0, "written": 0, "dedup": 0}


def save_persisted_ledger(ledger: dict):
    LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = LEDGER_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(ledger, f, indent=2)
    tmp.replace(LEDGER_FILE)


# ── Leitura de análise ─────────────────────────────────────────────────────────

def load_analysis(meeting_id: str) -> dict | None:
    path = ANALYSIS_DIR / f"{meeting_id}.json"
    if not path.exists():
        return None
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


# ── Classificador de conteúdo ──────────────────────────────────────────────────

def extract_items(analysis: dict) -> dict[str, list[dict]]:
    """
    Extrai e classifica todos os itens acionáveis de uma análise.
    Retorna dict por categoria.
    """
    meeting_id = analysis.get("meeting_id", "?")
    happened = analysis.get("happened_at", "")
    source = f"[{meeting_id}](/{happened[:7]})" if happened else f"[{meeting_id}]"

    items: dict[str, list[dict]] = {
        "decision": [], "lesson": [], "pending": [],
        "project": [], "risk": [], "preference": [], "context": []
    }

    # ── Decisões ──────────────────────────────────────────────────────────
    for d in analysis.get("decisions", []):
        if d.get("confidence") in ("confirmed", "likely"):
            desc = d.get("description", "").strip()
            if len(desc) < 10:
                continue
            items["decision"].append({
                "text": desc,
                "source": source,
                "confidence": d.get("confidence", "?"),
                "decision_maker": d.get("decision_maker"),
                "meeting_id": meeting_id,
            })

    # ── Tarefas (geram pending + project) ─────────────────────────────────
    for t in analysis.get("tasks", []):
        desc = t.get("description", "").strip()
        if len(desc) < 10:
            continue
        owner = t.get("owner")
        deadline = t.get("deadline")
        priority = t.get("priority", "medium")
        src = f"{source} | Prioridade: {priority}"
        if owner:
            src += f" | Dono: {owner}"
        if deadline:
            src += f" | Prazo: {deadline}"

        if priority == "high":
            items["pending"].append({
                "text": f"[HIGH] {desc}",
                "source": src,
                "owner": owner,
                "deadline": deadline,
                "meeting_id": meeting_id,
            })
        else:
            items["pending"].append({
                "text": desc,
                "source": src,
                "owner": owner,
                "deadline": deadline,
                "meeting_id": meeting_id,
            })

    # ── Open items ─────────────────────────────────────────────────────────
    for o in analysis.get("open_items", []):
        desc = o.get("description", "").strip()
        if len(desc) < 10:
            continue
        status = o.get("status", "open")
        owner = o.get("owner")
        deadline = o.get("deadline")
        src = f"{source} | Status: {status}"
        if owner:
            src += f" | Dono: {owner}"
        items["pending"].append({
            "text": desc,
            "source": src,
            "owner": owner,
            "deadline": deadline,
            "meeting_id": meeting_id,
        })

    # ── Riscos ─────────────────────────────────────────────────────────────
    for r in analysis.get("risks_and_alerts", []):
        desc = r.get("description", "").strip()
        if len(desc) < 10:
            continue
        severity = r.get("severity", "medium")
        rtype = r.get("type", "operational")
        mitigation = r.get("mitigation") or ""
        src = f"{source} | Severidade: {severity} | Tipo: {rtype}"
        items["risk"].append({
            "text": desc,
            "source": src,
            "severity": severity,
            "rtype": rtype,
            "mitigation": mitigation,
            "meeting_id": meeting_id,
        })

    # ── Oportunidades (commercial context) ────────────────────────────────
    for op in analysis.get("opportunities", []):
        desc = op.get("description", "").strip()
        if len(desc) < 10:
            continue
        impact = op.get("potential_impact", "medium")
        owner = op.get("owner", "a definir")
        items["context"].append({
            "text": desc,
            "source": f"{source} | Impacto: {impact} | Dono: {owner}",
            "impact": impact,
            "meeting_id": meeting_id,
        })

    # ── Critical questions ─────────────────────────────────────────────────
    for q in analysis.get("critical_questions", []):
        desc = q.get("question", "").strip()
        if len(desc) < 10:
            continue
        owner = q.get("owner", "a definir")
        deadline = q.get("answer_required_by")
        src = f"{source} | Pergunta crítica"
        if owner:
            src += f" | Dono: {owner}"
        items["pending"].append({
            "text": f"[PERGUNTA] {desc}",
            "source": src,
            "owner": owner,
            "deadline": deadline,
            "meeting_id": meeting_id,
        })

    # ── Lições aprendidas ──────────────────────────────────────────────────
    # Riscos com severity=high/medium viram lição
    for r in analysis.get("risks_and_alerts", []):
        if r.get("severity") in ("high", "medium"):
            desc = r.get("description", "").strip()
            if len(desc) > 15:
                items["lesson"].append({
                    "text": f"Evitar: {desc}",
                    "source": f"{source} | Tipo: {r.get('type','?')}",
                    "meeting_id": meeting_id,
                })

    # ── Documentary suggestions ────────────────────────────────────────────
    for ds in analysis.get("documentary_suggestions", []):
        action = ds.get("action", "").strip()
        if len(action) < 10:
            continue
        dest = ds.get("destination", "a definir")
        priority = ds.get("priority", "medium")
        items["context"].append({
            "text": f"[DOC] {action}",
            "source": f"{source} | Destino: {dest} | Prioridade: {priority}",
            "meeting_id": meeting_id,
        })

    # ── Preferred next step (vira project ou pending) ─────────────────────
    nxt = analysis.get("recommended_next_step") or {}
    nxt_action = nxt.get("action", "").strip()
    if nxt_action and len(nxt_action) > 10:
        owner = nxt.get("owner")
        deadline = nxt.get("deadline")
        items["pending"].append({
            "text": f"[PRÓXIMO PASSO] {nxt_action}",
            "source": f"{source} | Recomendado",
            "owner": owner,
            "deadline": deadline,
            "meeting_id": meeting_id,
        })

    return items


# ── Formatadores ───────────────────────────────────────────────────────────────

def fmt_decision(item: dict) -> str:
    maker = f" @({item['decision_maker']})" if item.get("decision_maker") else ""
    return f"- [{item['text']}]{maker} — {item['source']} [{item['confidence']}]"


def fmt_lesson(item: dict) -> str:
    return f"- {item['text']} — {item['source']}"


def fmt_pending(item: dict) -> str:
    owner = f"@({item.get('owner','?')})" if item.get("owner") else ""
    deadline = f" | Prazo: {item['deadline']}" if item.get("deadline") else ""
    return f"- {item['text']} {owner}{deadline} — {item['source']}"


def fmt_project(item: dict) -> str:
    owner = f"@({item.get('owner','?')})" if item.get("owner") else ""
    return f"- {item['text']} {owner} — {item['source']}"


def fmt_risk(item: dict) -> str:
    return (f"- [{item['severity'].upper()}] [{item['rtype']}] "
            f"{item['text']} — {item['source']}")


def fmt_preference(item: dict) -> str:
    return f"- {item['text']} — {item['source']}"


def fmt_context(item: dict) -> str:
    return f"- {item['text']} — {item['source']}"


# ── Writers ───────────────────────────────────────────────────────────────────

def ensure_header(path: Path, title: str, headers: dict):
    """Garante que arquivo existe com header se necessário."""
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {title}\n", f"\n*Gerado automaticamente em {datetime.now().date()}*\n"]
    with open(path, "w") as f:
        f.write("\n".join(lines))


def append_to_file(path: Path, lines: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        f.write("\n".join(lines) + "\n")


def generate_patch(category: str, items: list[dict], source: str) -> Path:
    """Gera patch sugerido em docs/meeting-derived-updates/"""
    UPDATES_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    patch_file = UPDATES_DIR / f"{ts}_{category}.md"
    lines = [
        f"# Patch: {category} — {ts}",
        f"**Origem:** {source}",
        f"**Itens:** {len(items)}",
        "",
    ]
    fmt_map = {
        "decision": fmt_decision, "lesson": fmt_lesson,
        "pending": fmt_pending, "project": fmt_project,
        "risk": fmt_risk, "preference": fmt_preference, "context": fmt_context,
    }
    fmt = fmt_map.get(category, fmt_context)
    for item in items:
        lines.append(fmt(item))
    with open(patch_file, "w") as f:
        f.write("\n".join(lines) + "\n")
    return patch_file


# ── Main ───────────────────────────────────────────────────────────────────────

def run(dry_run: bool = False, limit: int = 0, since: str = ""):
    dedup = DedupStore(WORKSPACE / "memory/meetings/ledger/persister_hashes.txt")
    ledger = load_persisted_ledger()
    persisted_ids = set(ledger.get("persisted", []))
    since_dt = None
    if since:
        since_dt = datetime.fromisoformat(since)

    # Coletar análises
    all_analyses = sorted(ANALYSIS_DIR.glob("*.json"))
    if limit:
        all_analyses = all_analyses[:limit]

    targets = [p for p in all_analyses
               if p.stem not in persisted_ids
               and (not since_dt or True)]  # filter by date below

    if not targets:
        log("Nenhuma análise nova para processar.")
        return

    log(f"Processando {len(targets)} análises...")

    # Acumular por categoria
    aggregated: dict[str, list[dict]] = {
        "decision": [], "lesson": [], "pending": [],
        "project": [], "risk": [], "preference": [], "context": []
    }
    new_items_total = 0

    for path in targets:
        mid = path.stem
        analysis = load_analysis(mid)
        if not analysis:
            continue

        happened = analysis.get("happened_at", "")
        if since_dt and happened:
            try:
                dt = datetime.fromisoformat(happened.replace("Z","+00:00"))
                if dt < since_dt:
                    continue
            except Exception:
                pass

        items = extract_items(analysis)
        for cat, cat_items in items.items():
            new = [i for i in cat_items if dedup.is_new(i["text"])]
            if new:
                aggregated[cat].extend(new)
                new_items_total += len(new)

        ledger["persisted"].append(mid)

    log(f"Novos itens únicos: {new_items_total} (dedup: {len(targets)*3 - new_items_total} duplicatas filtradas)")

    if dry_run:
        log("DRY RUN — nada escrito.")
        for cat, items in aggregated.items():
            if items:
                log(f"  [{cat}] {len(items)} itens novos")
        return

    fmt_map = {
        "decision": fmt_decision, "lesson": fmt_lesson,
        "risk": fmt_risk, "preference": fmt_preference, "context": fmt_context,
        "pending": fmt_pending, "project": fmt_project,
    }

    written = 0
    for cat, items in aggregated.items():
        if not items:
            continue

        path = DIRECT_TARGETS.get(cat)
        # Direct write: só para arquivos sem formato fixo
        if path:
            lines = []
            existing_norm = ""
            if path.exists():
                existing_norm = _normalize_text(path.read_text())
            for item in items:
                item_norm = _normalize_text(item["text"])
                if item_norm and item_norm in existing_norm:
                    ledger["dedup"] += 1
                    continue
                lines.append(fmt_map[cat](item))
                existing_norm += " " + item_norm  # detecta colisões dentro do batch
                written += 1
            if lines:
                ensure_header(path, cat.title() + "s", {})
                append_to_file(path, lines)
                log(f"  [WRITE] {len(lines)} → {path.name}")

        # Sempre gera patch (Diego revisa antes de aplicar)
        patch_path = generate_patch(cat, items, f"{len(items)} análises")
        log(f"  [PATCH] {cat}: {len(items)} → {patch_path.name}")

    ledger["written"] = ledger.get("written", 0) + written
    save_persisted_ledger(ledger)
    dedup.save()

    log(f"Persister finalizado. Total escrito: {written} | "
        f"Total no ledger: {len(ledger['persisted'])} | "
        f"Dedup: {ledger['dedup']}")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Persister tl;dv → memória")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--since", type=str, default="",
                        help="Processar análises após YYYY-MM-DD")
    args = parser.parse_args()
    run(dry_run=args.dry_run, limit=args.limit, since=args.since)


if __name__ == "__main__":
    main()
