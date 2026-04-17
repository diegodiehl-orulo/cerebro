#!/usr/bin/env python3
"""
tl;dv Meeting Indexer -- Morfeu
==============================
Indexa todas as analises em memory/meetings/analysis/ e permite buscar por:
  - speaker (quem palestrou / foi mencionado)
  - area/topic (WS1 / WS2 / etc.)
  - periodo (from:YYYY-MM-DD to:YYYY-MM-DD)
  - decision / decisions (reuniões com decisões)
  - risk HIGH
  - confidence:CONF
  - "texto livre" (busca em summary+decisions+tasks)

Uso:
  python3 indexer.py                    # mostra stats
  python3 indexer.py --rebuild         # reconstrói índice
  python3 indexer.py --search "Gustavo from:2026-01 to:2026-03"
  python3 indexer.py --search "decision"
  python3 indexer.py --json            # output JSON puro
"""

import json, sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DIRS, WORKSPACE  # noqa: E402

ANALYSIS_DIR = DIRS["analysis"]
INDEX_FILE = DIRS["ledger"] / "meeting_index.json"

# ─────────────────────────────────────────
# 1. LEITURA
# ─────────────────────────────────────────

def load_analysis(path: Path) -> dict | None:
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None

# ─────────────────────────────────────────
# 2. EXTRAÇÃO POR REUNIÃO
# ─────────────────────────────────────────

def extract_meeting_record(meeting_id: str, data: dict) -> dict:
    """Extrai todos os campos indexáveis de uma análise."""
    happened_at = data.get("happened_at", "")
    if happened_at:
        try:
            dt = datetime.fromisoformat(happened_at.replace("Z", "+00:00"))
            happened_at = dt.strftime("%Y-%m-%d")
        except ValueError:
            pass

    summary = data.get("executive_summary", "") or ""
    decisions = data.get("decisions", []) or []
    tasks = data.get("tasks", []) or []
    risks = data.get("risks_and_alerts", []) or []
    questions = data.get("critical_questions", []) or []
    opportunities = data.get("opportunities", []) or []
    memories = data.get("memories_to_register", []) or []
    speakers = data.get("speakers", []) or []
    tags = data.get("tags", []) or []
    raw_topics = data.get("raw_topics_from_tldv", []) or []

    # Inferir area de tags ou raw_topics
    area = data.get("area", "") or ""
    if not area and tags:
        area = tags[0] if isinstance(tags[0], str) else ""
    if not area and raw_topics:
        area = raw_topics[0] if isinstance(raw_topics[0], str) else ""

    # Texto livre
    free_text_parts = [summary]
    for d in decisions:
        free_text_parts.append(d.get("description", ""))
    for t in tasks:
        free_text_parts.append(t.get("description", ""))
    for r in risks:
        free_text_parts.append(r.get("description", ""))
    free_text = " ".join(filter(None, free_text_parts)).lower()

    return {
        "meeting_id": meeting_id,
        "title": data.get("name", meeting_id),
        "happened_at": happened_at,
        "organizer": data.get("organizer", ""),
        "speakers": speakers,
        "area": area,
        "summary": summary,
        "word_count": data.get("word_count", 0),
        "analysis_confidence": data.get("analysis_confidence", {}).get("level", "?"),
        "decisions_count": len(decisions),
        "tasks_count": len(tasks),
        "risks_count": len(risks),
        "decisions": [
            {
                "id": d.get("id", ""),
                "description": d.get("description", ""),
                "owner": d.get("owner", "") or d.get("decision_maker", ""),
                "confidence": d.get("confidence", "uncertain"),
            }
            for d in decisions
        ],
        "tasks": [
            {
                "id": t.get("id", ""),
                "description": t.get("description", ""),
                "owner": t.get("owner", ""),
                "priority": t.get("priority", "MEDIUM"),
                "type": t.get("type", ""),
            }
            for t in tasks
        ],
        "risks": [
            {
                "id": r.get("id", ""),
                "description": r.get("description", ""),
                "severity": r.get("severity", "medium"),
                "owner": r.get("owner", ""),
            }
            for r in risks
        ],
        "questions": [q.get("text", "") or q.get("question", "") for q in questions],
        "opportunities": [o.get("description", "") for o in opportunities],
        "memories": [m.get("memory", "") for m in memories],
        "tags": tags,
        "free_text": free_text,
    }

# ─────────────────────────────────────────
# 3. BUILD DO ÍNDICE
# ─────────────────────────────────────────

def build_index() -> dict:
    print("[indexer] Building meeting index...")
    files = sorted(ANALYSIS_DIR.glob("*.json"))
    print(f"[indexer] Found {len(files)} analysis files")

    index = {
        "generated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "total_meetings": 0,
        "meetings": {},
        "by_speaker": {},
        "by_area": {},
        "by_date": {},
        "by_keyword": {},
        "decisions_by_confidence": {"confirmed": [], "likely": [], "uncertain": []},
        "tasks_by_priority": {"HIGH": [], "MEDIUM": [], "LOW": []},
        "risks_by_severity": {"high": [], "medium": [], "low": []},
    }

    for f in files:
        mid = f.stem
        data = load_analysis(f)
        if not data:
            continue

        record = extract_meeting_record(mid, data)
        index["meetings"][mid] = record
        index["total_meetings"] += 1

        # by_speaker
        for sp in record["speakers"]:
            sp_lower = sp.lower()
            if sp_lower not in index["by_speaker"]:
                index["by_speaker"][sp_lower] = []
            index["by_speaker"][sp_lower].append(mid)

        # by_area
        area = record.get("area", "")
        if area:
            al = area.lower()
            if al not in index["by_area"]:
                index["by_area"][al] = []
            index["by_area"][al].append(mid)

        # by_date (YYYY-MM)
        if record["happened_at"]:
            ym = record["happened_at"][:7]
            if ym not in index["by_date"]:
                index["by_date"][ym] = []
            index["by_date"][ym].append(mid)

        # decisions_by_confidence
        for d in record["decisions"]:
            conf = d["confidence"]
            if conf in index["decisions_by_confidence"]:
                index["decisions_by_confidence"][conf].append(mid)

        # tasks_by_priority
        pri = record["tasks"][0]["priority"].upper() if record["tasks"] else ""
        if pri in index["tasks_by_priority"]:
            index["tasks_by_priority"][pri].append(mid)

        # risks_by_severity
        for r in record["risks"]:
            sev = r["severity"].lower()
            if sev in index["risks_by_severity"]:
                index["risks_by_severity"][sev].append(mid)

        # by_keyword — termos >= 3 chars
        words = set(w for w in record["free_text"].split() if len(w) >= 3)
        for word in words:
            if word not in index["by_keyword"]:
                index["by_keyword"][word] = []
            index["by_keyword"][word].append(mid)

    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"[indexer] Done: {index['total_meetings']} meetings | "
          f"{len(index['by_speaker'])} speakers | "
          f"{len(index['by_area'])} areas | "
          f"{len(index['by_keyword'])} keywords")
    return index

# ─────────────────────────────────────────
# 4. BUSCA
# ─────────────────────────────────────────

def load_index() -> dict:
    if not INDEX_FILE.exists():
        return build_index()
    with open(INDEX_FILE) as f:
        return json.load(f)

def apply_date_filter(results: dict, from_date: str | None, to_date: str | None) -> dict:
    if not from_date and not to_date:
        return results
    filtered = {}
    for mid, rec in results.items():
        dt = rec.get("happened_at", "")
        if from_date and dt < from_date:
            continue
        if to_date and dt > to_date:
            continue
        filtered[mid] = rec
    return filtered

def search(index: dict, query: str) -> list[dict]:
    """
    Formatos aceitos:
      speaker:NOME       — reuniões de/sobre um speaker
      area:AREA          — reuniões de uma area/WS
      from:YYYY-MM-DD    — desde data
      to:YYYY-MM-DD      — até data
      decision(s)        — reuniões com decisões
      decision confirmed — decisões confirmed
      task HIGH          — tarefas HIGH
      risk HIGH          — riscos HIGH
      confidence:CONF    — decisões com confidence X
      "texto livre"      — interseção de palavras em summary+decisions+tasks
    """
    query = query.strip()
    results = {}
    q_lower = query.lower()

    # ── Parse date filters ──
    from_date = None
    to_date = None
    parts = q_lower.split()
    keyword_parts = []
    for part in parts:
        if part.startswith("from:"):
            from_date = part[5:]
        elif part.startswith("to:"):
            to_date = part[3:]
        else:
            keyword_parts.append(part)

    remaining = " ".join(keyword_parts).strip()

    # ── Special queries ──
    if remaining.startswith("speaker:"):
        name = remaining[8:].strip()
        mids = index["by_speaker"].get(name, [])
        results = {mid: index["meetings"][mid] for mid in mids if mid in index["meetings"]}

    elif remaining.startswith("area:"):
        area = remaining[5:].strip()
        mids = index["by_area"].get(area, [])
        results = {mid: index["meetings"][mid] for mid in mids if mid in index["meetings"]}

    elif remaining == "decision" or remaining == "decisions":
        # Todas reuniões com pelo menos 1 decisão
        results = {
            mid: rec for mid, rec in index["meetings"].items()
            if rec.get("decisions_count", 0) > 0
        }

    elif remaining == "decision confirmed":
        mids = index["decisions_by_confidence"].get("confirmed", [])
        results = {mid: index["meetings"][mid] for mid in mids if mid in index["meetings"]}

    elif remaining == "task high":
        mids = index["tasks_by_priority"].get("HIGH", [])
        results = {mid: index["meetings"][mid] for mid in mids if mid in index["meetings"]}

    elif remaining == "risk high":
        mids = index["risks_by_severity"].get("high", [])
        results = {mid: index["meetings"][mid] for mid in mids if mid in index["meetings"]}

    elif remaining.startswith("confidence:"):
        conf = remaining[11:].strip()
        mids = index["decisions_by_confidence"].get(conf, [])
        results = {mid: index["meetings"][mid] for mid in mids if mid in index["meetings"]}

    elif remaining.startswith("from:") or remaining.startswith("to:"):
        # Só filtro de data — todas as reuniões no período
        for mid, rec in index["meetings"].items():
            results[mid] = rec

    else:
        # ── Free text: interseção de palavras (>= 3chars) ──
        words = [w for w in remaining.split() if len(w) >= 3]
        if not words:
            return []
        for word in words:
            mids = index["by_keyword"].get(word, [])
            if not mids:
                return []
            if not results:
                results = {mid: None for mid in mids}
            else:
                results = {mid: None for mid in mids if mid in results}
        results = {mid: index["meetings"][mid] for mid in results if mid in index["meetings"]}

    # ── Apply date filter ──
    results = apply_date_filter(results, from_date, to_date)
    return list(results.values())

def format_results(records: list[dict], max_results: int = 10) -> str:
    if not records:
        return "Nenhum resultado."
    out = [f"**{len(records)} resultado(s)**\n"]
    for rec in records[:max_results]:
        date = rec.get("happened_at", "???")
        title = rec.get("title", rec["meeting_id"])[:50]
        decisions = rec.get("decisions_count", 0)
        tasks = rec.get("tasks_count", 0)
        risks = rec.get("risks_count", 0)
        area = rec.get("area", "")
        area_str = f" | Area: {area}" if area else ""
        out.append(
            f"• **{date}** — {title}\n"
            f"  D:{decisions} T:{tasks} R:{risks}{area_str} | ID: `{rec['meeting_id']}`"
        )
    if len(records) > max_results:
        out.append(f"_...e mais {len(records) - max_results}_")
    return "\n".join(out)

# ─────────────────────────────────────────
# 5. MAIN
# ─────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="tl;dv Meeting Indexer")
    parser.add_argument("--rebuild", action="store_true", help="Força rebuild do índice")
    parser.add_argument("--search", type=str, default=None, help="Query de busca")
    parser.add_argument("--json", action="store_true", help="Output JSON puro")
    parser.add_argument("--limit", type=int, default=10, help="Máx resultados")
    args = parser.parse_args()

    if args.rebuild or not INDEX_FILE.exists():
        idx = build_index()
    else:
        idx = load_index()

    if args.search:
        results = search(idx, args.search)
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            print(format_results(results, args.limit))
    else:
        print(f"Index: {idx['total_meetings']} reuniões | "
              f"{len(idx['by_speaker'])} speakers | "
              f"{len(idx['by_area'])} areas | "
              f"{len(idx['by_keyword'])} keywords")
        print(f"Index file: {INDEX_FILE}")

if __name__ == "__main__":
    main()
