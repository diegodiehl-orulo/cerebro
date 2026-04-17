#!/usr/bin/env python3
"""
enricher.py — Pipeline de enriquecimento de reuniões tl;dv.

Responsabilidades:
1. Listar reuniões em memory/meetings/raw/ ainda não enriquecidas
2. Para cada uma: buscar transcript + notes via API
3. Salvar transcript em memory/meetings/transcripts/{id}.json
4. Salvar notes em memory/meetings/notes/{id}.json
5. Gerar consolidado normalizado em memory/meetings/normalized/{id}.json
6. Atualizar ledger de enriquecimento

Uso:
    PYTHONPATH=/root/.openclaw/workspace/integrations \
    TLDV_API_KEY="sua_chave" \
    python3 integrations/tldv/enricher.py [--limit N] [--dry-run] [--meeting-id ID]

Flags de status (no consolidado):
    transcript_status: pending | available | unavailable | error
    notes_status:     pending | available | unavailable | error
    analysis_status:  not_started | ready | enriched
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DIRS, LEDGERS, LOCKS, WORKSPACE  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s — %(message)s",
)
logger = logging.getLogger("tldv.enricher")

# ── Paths ────────────────────────────────────────────────────────────────────

RAW_DIR = DIRS["raw"]
TX_DIR = DIRS["transcripts"]
NOTES_DIR = DIRS["notes"]
NORM_DIR = DIRS["normalized"]
LEDGER_FILE = LEDGERS["enriched"]
LEDGER_LOCK = LOCKS["enricher"]
LOG_DIR = DIRS["logs"]
PENDING_RETRY_FILE = LEDGERS["pending_retry"]

# ── Helpers ────────────────────────────────────────────────────────────────────

def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_raw_meetings():
    """Retorna lista de IDs de reuniões em raw/."""
    return [p.stem for p in RAW_DIR.glob("*.json")]


def load_raw(meeting_id: str) -> dict | None:
    """Carrega dados brutos de uma reunião."""
    path = RAW_DIR / f"{meeting_id}.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


def load_enriched_ledger() -> dict:
    if not LEDGER_FILE.exists():
        return {
            "enriched": [],
            "failed": [],
            "pending": [],
            "last_run": None,
            "stats": {"total": 0, "enriched": 0, "failed": 0, "skipped": 0},
        }
    with open(LEDGER_FILE) as f:
        return json.load(f)


def save_enriched_ledger(ledger: dict) -> None:
    LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = LEDGER_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
    tmp.replace(LEDGER_FILE)


def load_pending_retry() -> dict:
    """Lista de reuniões com transcript pending (204) — para reprocessar depois."""
    if not PENDING_RETRY_FILE.exists():
        return {}
    try:
        with open(PENDING_RETRY_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_pending_retry(pending: dict) -> None:
    PENDING_RETRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = PENDING_RETRY_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(pending, f, indent=2, ensure_ascii=False)
    tmp.replace(PENDING_RETRY_FILE)


def mark_for_retry(meeting_id: str, reason: str) -> None:
    """Registra meeting como pendente de retry (transcript ainda em processamento)."""
    pending = load_pending_retry()
    entry = pending.get(meeting_id, {"attempts": 0})
    entry["attempts"] = entry.get("attempts", 0) + 1
    entry["last_attempt"] = now_iso()
    entry["reason"] = reason
    pending[meeting_id] = entry
    save_pending_retry(pending)


def clear_retry(meeting_id: str) -> None:
    pending = load_pending_retry()
    if meeting_id in pending:
        del pending[meeting_id]
        save_pending_retry(pending)


def mark_lock():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LEDGER_LOCK, "w") as f:
        f.write(now_iso())


def clear_lock():
    if LEDGER_LOCK.exists():
        LEDGER_LOCK.unlink()


# ── Fetchers ──────────────────────────────────────────────────────────────────

def fetch_transcript(client, meeting_id: str) -> dict:
    """
    Busca transcript. Retorna dict com status e dado ou erro.
    None do client = transcript pendente (204). Não é erro.
    """
    try:
        data = client.get_transcript(meeting_id)
        if data is None:
            return {"status": "pending", "data": None, "reason": "transcript not ready (204)"}
        entries = data.get("data", [])
        if not entries:
            return {"status": "unavailable", "data": None, "reason": "empty transcript"}
        return {"status": "available", "data": data, "entry_count": len(entries)}
    except PermissionError as e:
        return {"status": "error", "data": None, "reason": f"auth_error: {e}"}
    except FileNotFoundError as e:
        return {"status": "unavailable", "data": None, "reason": f"not_found: {e}"}
    except Exception as e:
        return {"status": "error", "data": None, "reason": f"unexpected: {e}"}


def fetch_notes(client, meeting_id: str) -> dict:
    """
    Busca notes. Retorna dict com status e dado ou erro.
    None do client = notes vazias ou 204.
    """
    try:
        data = client.get_notes(meeting_id)
        if data is None:
            return {"status": "unavailable", "data": None, "reason": "notes empty or not ready"}
        return {"status": "available", "data": data}
    except PermissionError as e:
        return {"status": "error", "data": None, "reason": f"auth_error: {e}"}
    except FileNotFoundError as e:
        return {"status": "unavailable", "data": None, "reason": f"not_found: {e}"}
    except Exception as e:
        return {"status": "error", "data": None, "reason": f"unexpected: {e}"}


# ── Normalizer ────────────────────────────────────────────────────────────────

def normalize(meeting_id: str, raw: dict, tx_result: dict, notes_result: dict) -> dict:
    """
    Monta objeto normalizado com:
    - metadados da reunião
    - transcript (se disponível)
    - notes (se disponíveis)
    - flags de status
    - timestamps de coleta
    """
    collected_at = now_iso()

    # ── Transcript ──────────────────────────────────────────────────────────
    tx_status = tx_result["status"]
    tx_data = tx_result.get("data")
    tx_reason = tx_result.get("reason")

    tx_summary = None
    if tx_status == "available" and tx_data:
        entries = tx_data.get("data", [])
        speakers = list({e.get("speaker") for e in entries if e.get("speaker")})
        total_words = sum(len(e.get("text", "").split()) for e in entries)
        tx_summary = {
            "entry_count": len(entries),
            "speakers": speakers,
            "total_words_estimate": total_words,
            "duration_start": min((e.get("startTime", 0) for e in entries), default=0),
            "duration_end": max((e.get("endTime", 0) for e in entries), default=0),
        }

    # ── Notes ──────────────────────────────────────────────────────────────
    notes_status = notes_result["status"]
    notes_data = notes_result.get("data")
    notes_reason = notes_result.get("reason")

    notes_summary = None
    topics_list = []
    if notes_status == "available" and notes_data:
        structured = notes_data.get("structuredNotes", [])
        topics_list = notes_data.get("topics", [])
        notes_summary = {
            "note_count": len(structured),
            "topic_count": len(topics_list),
            "has_markdown": bool(notes_data.get("markdownContent")),
        }

    # ── Flags de status ────────────────────────────────────────────────────
    tx_flag = tx_status  # pending | available | unavailable | error
    notes_flag = notes_status  # pending | available | unavailable | error

    # analysis_status: not_started enquanto não enriquecemos com IA
    if tx_flag == "available" or notes_flag == "available":
        analysis_flag = "ready"
    elif tx_flag == "unavailable" and notes_flag == "unavailable":
        analysis_flag = "not_started"
    else:
        analysis_flag = "ready"  # mesmo com erro parcial, marcamos ready

    # ── Montagem ───────────────────────────────────────────────────────────
    normalized = {
        # Metadados da reunião
        "meeting_id": meeting_id,
        "name": raw.get("name"),
        "happened_at": raw.get("happenedAt"),
        "duration_seconds": raw.get("duration"),
        "duration_minutes": round(raw.get("duration", 0) / 60, 1),
        "organizer": raw.get("organizer"),
        "invitees": raw.get("invitees"),
        "url": raw.get("url"),
        "template": raw.get("template"),
        "conference_id": raw.get("extraProperties", {}).get("conferenceId"),

        # Status flags
        "transcript_status": tx_flag,
        "notes_status": notes_flag,
        "analysis_status": analysis_flag,

        # Transcript
        "transcript": tx_data if tx_status == "available" else None,
        "transcript_summary": tx_summary,
        "transcript_unavailable_reason": tx_reason if tx_flag in ("unavailable", "error") else None,

        # Notes
        "notes": notes_data if notes_status == "available" else None,
        "notes_summary": notes_summary,
        "notes_unavailable_reason": notes_reason if notes_flag in ("unavailable", "error") else None,
        "topics": topics_list,

        # Timestamps
        "collected_at": collected_at,
        "meeting_saved_at": raw.get("_saved_at", None),  # será adicionado se não existir

        # Info de proveniência
        "_schema_version": "1.0",
        "_enriched_at": collected_at,
    }

    return normalized


# ── Pipeline ──────────────────────────────────────────────────────────────────

def process_meeting(client, meeting_id: str, dry_run: bool = False) -> dict:
    """Processa uma reunião: fetch + normalizar + salvar."""
    result = {"id": meeting_id, "tx_status": None, "notes_status": None, "outcome": None}

    # 1. Carregar raw
    raw = load_raw(meeting_id)
    if not raw:
        result["outcome"] = "missing_raw"
        return result

    # 2. Fetch transcript
    tx_result = fetch_transcript(client, meeting_id)
    result["tx_status"] = tx_result["status"]

    # 3. Fetch notes
    notes_result = fetch_notes(client, meeting_id)
    result["notes_status"] = notes_result["status"]

    if dry_run:
        result["outcome"] = "dry_run"
        return result

    # 4. Salvar transcript
    tx_path = TX_DIR / f"{meeting_id}.json"
    notes_path = NOTES_DIR / f"{meeting_id}.json"
    norm_path = NORM_DIR / f"{meeting_id}.json"

    if tx_result["status"] == "available" and tx_result.get("data"):
        with open(tx_path, "w", encoding="utf-8") as f:
            json.dump(tx_result["data"], f, indent=2, ensure_ascii=False)

    # 5. Salvar notes
    if notes_result["status"] == "available" and notes_result.get("data"):
        with open(notes_path, "w", encoding="utf-8") as f:
            json.dump(notes_result["data"], f, indent=2, ensure_ascii=False)

    # 6. Gerar normalizado
    norm = normalize(meeting_id, raw, tx_result, notes_result)
    with open(norm_path, "w", encoding="utf-8") as f:
        json.dump(norm, f, indent=2, ensure_ascii=False)

    result["outcome"] = "enriched"
    return result


def run(max_meetings: int | None = None, dry_run: bool = False, meeting_id: str | None = None):
    """
    Rotina principal de enriquecimento.

    Args:
        max_meetings: limite de reuniões a processar (None = todas não enriquecidas)
        dry_run: se True, não salva nada
        meeting_id: se fornecido, processa apenas essa reunião
    """
    start_time = datetime.now(timezone.utc)
    logger.info("=== ENRICHMENT tl;dv INICIADO | %s | dry_run=%s ===",
                 start_time.isoformat(), dry_run)

    if LEDGER_LOCK.exists():
        logger.warning("Lock encontrado — enriquecimento anterior pode estar rodando.")
        logger.warning("Remova %s se não houver processo em execução.", LEDGER_LOCK)
        return

    if not dry_run:
        mark_lock()

    try:
        from tldv.client import TldvClient
        client = TldvClient()

        # ── Identificar reuniões a processar ─────────────────────────────────
        if meeting_id:
            targets = [meeting_id]
            logger.info("Processando reunião específica: %s", meeting_id)
        else:
            all_raw = set(load_raw_meetings())
            ledger = load_enriched_ledger()
            already_enriched = set(ledger.get("enriched", []))
            # Incluir pendentes (204) para retry — eles saem do raw pool quando enriquecidos.
            pending_retry = set(load_pending_retry().keys())
            targets = sorted((all_raw - already_enriched) | pending_retry)
            logger.info("Reuniões em raw/: %d | Já enriquecidas: %d | Pending retry: %d | A processar: %d",
                        len(all_raw), len(already_enriched), len(pending_retry), len(targets))

        if not targets:
            logger.info("Nenhuma reunião para enriquecer. Ledger mantido.")
            return

        if max_meetings:
            targets = targets[:max_meetings]
            logger.info("Limitando a %d reuniões.", max_meetings)

        # ── Processar ───────────────────────────────────────────────────────
        ledger = load_enriched_ledger()
        enriched_count = 0
        error_count = 0
        skipped = 0

        for i, mid in enumerate(targets, 1):
            outcome = process_meeting(client, mid, dry_run=dry_run)

            if outcome["outcome"] == "dry_run":
                logger.info("  [%d/%d] DRY RUN: %s | tx=%s | notes=%s",
                            i, len(targets), mid, outcome["tx_status"], outcome["notes_status"])
                continue

            if outcome["outcome"] == "missing_raw":
                logger.warning("  [%d/%d] SKIP (raw ausente): %s", i, len(targets), mid)
                skipped += 1
                continue

            tx = outcome["tx_status"]
            notes = outcome["notes_status"]

            if tx == "available" or notes == "available":
                enriched_count += 1
                ledger["enriched"].append(mid)
                clear_retry(mid)
                logger.info("  [%d/%d] ✓ ENRICHED: %s | tx=%s | notes=%s",
                            i, len(targets), mid, tx, notes)
            elif tx == "pending" or notes == "pending":
                # 204: transcript ainda em processamento — agendar retry, não marcar failed
                mark_for_retry(mid, f"tx={tx} notes={notes}")
                logger.info("  [%d/%d] ⏳ PENDING (retry futuro): %s | tx=%s | notes=%s",
                            i, len(targets), mid, tx, notes)
            else:
                error_count += 1
                ledger["failed"].append(mid)
                logger.warning("  [%d/%d] ✗ FAILED: %s | tx=%s | notes=%s",
                               i, len(targets), mid, tx, notes)

            # Progress checkpoint
            if i % 50 == 0:
                logger.info("  → Checkpoint: %d/%d processadas", i, len(targets))

        # ── Finalização ──────────────────────────────────────────────────────
        elapsed = (datetime.now(timezone.utc) - start_time).total_seconds()

        if not dry_run:
            ledger["last_run"] = now_iso()
            ledger["stats"]["total"] = len(ledger["enriched"]) + len(ledger.get("failed", []))
            ledger["stats"]["enriched"] = len(ledger["enriched"])
            ledger["stats"]["failed"] = len(ledger.get("failed", []))
            ledger["stats"]["skipped"] = skipped
            save_enriched_ledger(ledger)

        logger.info("=== ENRICHMENT FINALIZADO | %ds | enriched: %d | errors: %d | skipped: %d ===",
                     int(elapsed), enriched_count, error_count, skipped)

    except Exception as e:
        logger.error("Erro fatal no enrichment: %s", e)
        raise
    finally:
        if not dry_run:
            clear_lock()


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Enriquecimento de reuniões tl;dv")
    parser.add_argument("--limit", type=int, default=None,
                        help="Limite de reuniões a processar (default: todas)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Mostra o que faria sem salvar nada")
    parser.add_argument("--meeting-id", type=str, default=None,
                        help="Processar apenas uma reunião específica")
    args = parser.parse_args()

    api_key = os.environ.get("TLDV_API_KEY")
    if not api_key:
        logger.error("TLDV_API_KEY não definida no ambiente.")
        sys.exit(1)

    run(max_meetings=args.limit, dry_run=args.dry_run, meeting_id=args.meeting_id)


if __name__ == "__main__":
    main()
