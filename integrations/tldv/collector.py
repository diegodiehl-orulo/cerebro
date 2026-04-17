#!/usr/bin/env python3
"""
collector.py — Rotina de coleta de reuniões do tl;dv.

Responsabilidades:
1. Listar reuniões recentes via GET /meetings (paginação automática)
2. Comparar com ledger de processados
3. Para cada reunião nova: buscar detalhes completos e salvar em memory/meetings/raw/{id}.json
4. Atualizar ledger ao final

Uso:
    PYTHONPATH=/root/.openclaw/workspace/integrations \
    TLDV_API_KEY="sua_chave" \
    python3 integrations/tldv/collector.py [--pages N] [--dry-run]
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime as dt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DIRS, LEDGERS, LOCKS, WORKSPACE  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s — %(message)s",
)
logger = logging.getLogger("tldv.collector")

# ── Paths ────────────────────────────────────────────────────────────────────

RAW_DIR = DIRS["raw"]
TRANSCRIPT_DIR = DIRS["transcripts"]
LEDGER_FILE = LEDGERS["processed"]
LEDGER_LOCK = LOCKS["collector"]

# ── Ledger ────────────────────────────────────────────────────────────────────

def load_ledger() -> dict:
    """Carrega ledger existente ou retorna dict vazio."""
    if not LEDGER_FILE.exists():
        return {"processed": [], "last_run": None, "stats": {"total": 0, "new": 0, "errors": 0}}
    with open(LEDGER_FILE) as f:
        return json.load(f)


def save_ledger(ledger: dict) -> None:
    """Salva ledger de forma atômica."""
    LEDGER_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = LEDGER_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)
    tmp.replace(LEDGER_FILE)


def mark_processing():
    """Cria lock para indicar que coleta está rodando."""
    LEDGER_LOCK.parent.mkdir(parents=True, exist_ok=True)
    with open(LEDGER_LOCK, "w") as f:
        f.write(dt.utcnow().isoformat())


def clear_processing():
    """Remove lock."""
    if LEDGER_LOCK.exists():
        LEDGER_LOCK.unlink()


# ── Collector ─────────────────────────────────────────────────────────────────

def fetch_meetings_page(client, page: int, page_size: int = 50) -> dict:
    """Busca uma página de reuniões."""
    logger.info("Buscando página %d (pageSize=%d)", page, page_size)
    result = client.list_meetings(page=page, page_size=page_size)
    meetings = result.get("results", [])
    total = result.get("total", 0)
    pages = result.get("pages", 1)
    logger.info("  → %d reuniões nesta página (página %d/%d, total %d)", 
                 len(meetings), page, pages, total)
    return {"meetings": meetings, "total": total, "pages": pages}


def fetch_meeting_detail(client, meeting_id: str) -> dict | None:
    """Busca detalhes completos de uma reunião."""
    try:
        detail = client.get_meeting(meeting_id)
        logger.info("  ✓ Detalhes: %s", meeting_id)
        return detail
    except Exception as e:
        logger.warning("  ✗ Erro ao buscar detalhes de %s: %s", meeting_id, e)
        return None


def save_meeting(meeting_data: dict) -> bool:
    """Salva reunião em arquivo próprio. Retorna True se salvou, False se já existia."""
    meeting_id = meeting_data.get("id")
    if not meeting_id:
        logger.warning("Reunião sem ID, ignorada")
        return False

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    filepath = RAW_DIR / f"{meeting_id}.json"

    if filepath.exists():
        logger.debug("  ○ Já existe: %s", meeting_id)
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(meeting_data, f, indent=2, ensure_ascii=False)
    logger.info("  ★ Nova salva: %s", meeting_id)
    return True


def _backfill_all_transcripts(client) -> dict:
    """
    Varre todas as reuniões salvas em raw/ e coleta transcript
    para qualquer uma que ainda não tenha sido salva em transcripts/.
    Retorna dict com 'saved' e 'total'.
    """
    tx_dir = DIRS["transcripts"]
    tx_dir.mkdir(parents=True, exist_ok=True)

    existing = set(p.stem for p in tx_dir.glob("*.txt"))
    raw_ids = [p.stem for p in DIRS["raw"].glob("*.json")]
    need_tx = [mid for mid in raw_ids if mid not in existing]

    saved = 0
    for mid in need_tx:
        if save_transcript(client, mid):
            saved += 1

    return {"saved": saved, "total": len(need_tx)}


def save_transcript(client, meeting_id: str) -> bool:
    """
    Busca transcript completo via GET /meetings/{id}/transcript e salva.
    Retorna True se salvou, False se já existia ou falhou.
    """
    TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = TRANSCRIPT_DIR / f"{meeting_id}.txt"

    if out_file.exists():
        logger.debug("  ○ Transcript já existe: %s", meeting_id)
        return False

    try:
        raw = client.get_transcript(meeting_id)
        if not raw:
            logger.warning("  ○ Transcript vazio/pendente: %s", meeting_id)
            return False

        # get_transcript retorna dict com chave 'data': list of entries
        entries = raw.get("data") or []

        lines = []
        for entry in entries:
            text = entry.get("text", "") if isinstance(entry, dict) else str(entry)
            speaker = entry.get("speaker", "?") if isinstance(entry, dict) else "?"
            start = entry.get("startTime", 0) if isinstance(entry, dict) else 0
            if text:
                m, s = divmod(start, 60)
                lines.append(f"[{m:02d}:{s:02d}] {speaker}: {text}")

        content = "\n".join(lines)
        if content.strip():
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info("  ★ Transcript salvo: %s (%d entries, %d chars)",
                        meeting_id, len(entries), len(content))
            return True
        else:
            logger.warning("  ○ Transcript vazio: %s", meeting_id)
            return False
    except Exception as e:
        logger.warning("  ✗ Erro transcript %s: %s", meeting_id, e)
        return False


def run(max_pages: int | None = None, dry_run: bool = False, page_size: int = 50):
    """
    Rotina principal de coleta.

    Args:
        max_pages: limite de páginas (None = todas)
        dry_run: se True, não salva nada nem atualiza ledger
        page_size: itens por página
    """
    start_time = dt.utcnow()
    logger.info("=== COLETA tl;dv INICIADA | %s | dry_run=%s ===", 
                 start_time.isoformat(), dry_run)

    # Verificar lock
    if LEDGER_LOCK.exists():
        logger.warning("Lock encontrado — coleta anterior pode estar rodando. "
                       "Remova %s se não houver processo em execução.", LEDGER_LOCK)
        logger.warning("Abortando para evitar duplicidade.")
        return

    # Setup
    if not dry_run:
        mark_processing()

    try:
        from tldv.client import TldvClient
        client = TldvClient()

        # ── Passo 1: Listar reuniões ──────────────────────────────────────────
        logger.info("Passo 1/3: Listando reuniões...")
        first_page = fetch_meetings_page(client, page=1, page_size=page_size)
        total = first_page["total"]
        pages = first_page["pages"]

        all_meetings = first_page["meetings"]

        if max_pages:
            pages_to_fetch = min(max_pages, pages)
        else:
            pages_to_fetch = pages

        if pages > 1:
            logger.info("Total de páginas: %d. Buscando %s...", 
                        pages, "todas" if not max_pages else f"{max_pages} (limitado)")
            for p in range(2, pages_to_fetch + 1):
                result = client.list_meetings(page=p, page_size=page_size)
                all_meetings.extend(result.get("results", []))

        logger.info("  → Total de reuniões listadas: %d", len(all_meetings))

        # ── Passo 2: Filtrar novas ────────────────────────────────────────────
        logger.info("Passo 2/3: Identificando reuniões novas...")
        ledger = load_ledger()
        processed_ids = set(ledger.get("processed", []))
        new_ids = [m["id"] for m in all_meetings if m["id"] not in processed_ids]

        logger.info("  → Já processadas: %d", len(processed_ids))
        logger.info("  → Novas nesta execução: %d", len(new_ids))

        if not new_ids:
            logger.info("Nenhuma reunião nova.")

        # ── Backfill: transcripts de reuniões já salvas que ainda não têm ───────────
        logger.info("Passo 3b/3b: Backfill de transcripts pendentes...")
        tx_saved = 0
        tx_skipped = 0
        for meeting_id in new_ids:
            if save_transcript(client, meeting_id):
                tx_saved += 1
            else:
                tx_skipped += 1
        logger.info("  → %d transcripts salvos (%d já existiam)", tx_saved, tx_skipped)

        # ── Também fazer backfill de TODAS as reuniões já salvas em raw/ ──────────
        tx_backfill = _backfill_all_transcripts(client)
        logger.info("  → Backfill total: %d transcripts salvos de %d reuniões em raw/",
                    tx_backfill["saved"], tx_backfill["total"])

        # ── Passo 3: Buscar detalhes e salvar ─────────────────────────────────
        logger.info("Passo 3/3: Buscando detalhes e salvando (%s)...", 
                     "DRY RUN" if dry_run else "live")

        new_count = 0
        error_count = 0

        for meeting_id in new_ids:
            if dry_run:
                logger.info("  [dry-run] would fetch: %s", meeting_id)
                new_count += 1
                continue

            detail = fetch_meeting_detail(client, meeting_id)
            if detail is None:
                error_count += 1
                continue

            saved = save_meeting(detail)
            if saved:
                new_count += 1
            # Sempre buscar transcript — mesmo se meeting já existia
            tx_saved = save_transcript(client, meeting_id)
            if tx_saved:
                logger.info("  ★ Transcript novo: %s", meeting_id)

            # Atualizar ledger incrementally (a cada 10 itens)
            if new_count % 10 == 0:
                ledger["processed"].append(meeting_id)
                logger.info("  → Ledger parcial: %d processadas", new_count)

        # ── Finalização ───────────────────────────────────────────────────────
        elapsed = (dt.utcnow() - start_time).total_seconds()

        if not dry_run:
            # Adicionar IDs processados ao ledger
            ledger["processed"].extend(new_ids)
            ledger["last_run"] = dt.utcnow().isoformat()
            ledger["stats"]["total"] = len(ledger["processed"])
            ledger["stats"]["new"] = ledger["stats"].get("new", 0) + new_count
            ledger["stats"]["errors"] = ledger["stats"].get("errors", 0) + error_count
            save_ledger(ledger)

        logger.info("=== COLETA FINALIZADA | %ds | novas: %d | erros: %d ===", 
                     int(elapsed), new_count, error_count)

    except Exception as e:
        logger.error("Erro fatal na coleta: %s", e)
        raise
    finally:
        if not dry_run:
            clear_processing()


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Coleta reuniões do tl;dv")
    parser.add_argument("--pages", type=int, default=None,
                        help="Número máximo de páginas a buscar (default: todas)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Lista reuniões novas sem salvar nada")
    parser.add_argument("--page-size", type=int, default=50,
                        help="Itens por página (default: 50)")
    args = parser.parse_args()

    api_key = os.environ.get("TLDV_API_KEY")
    if not api_key:
        logger.error("TLDV_API_KEY não definida no ambiente.")
        logger.error("Defina com: export TLDV_API_KEY='sua-chave-aqui'")
        sys.exit(1)

    run(max_pages=args.pages, dry_run=args.dry_run, page_size=args.page_size)


if __name__ == "__main__":
    main()
