#!/usr/bin/env python3
"""
queue_processor.py — Consome fila de webhooks e dispara pipeline por reunião
==========================================================================

Responsabilidade:
- Lê eventos de /memory/meetings/queue/
- Para cada evento: rodar enrich + analyze da reunião específica
- Atualiza status do evento
- Deleta após sucesso (ou move para .failed/)

Uso:
  python3 queue_processor.py              # processa fila inteira
  python3 queue_processor.py --dry-run    # mostra o que faria
  python3 queue_processor.py --limit 5    # limita a 5 eventos
  python3 queue_processor.py --meeting-id ID  # força reprocessamento de 1 reunião
"""

import argparse
import json
import os
import subprocess
import sys
import time
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s — %(message)s",
)
logger = logging.getLogger("tldv.queue_processor")

WORKSPACE = Path("/root/.openclaw/workspace")
QUEUE_DIR = WORKSPACE / "memory/meetings/queue"
PROCESSED_DIR = WORKSPACE / "memory/meetings/queue/processed"
FAILED_DIR = WORKSPACE / "memory/meetings/queue/failed"
LOG_FILE = WORKSPACE / "logs/tldv_queue_processor.log"

os.environ.setdefault("TLDV_API_KEY", "69f9a821-7286-46e8-a64c-7c1f20a01576")
os.environ.setdefault("PYTHONPATH", "/root/.openclaw/workspace/integrations")

ENRICH_SCRIPT = WORKSPACE / "integrations/tldv/enricher.py"
ANALYZE_SCRIPT = WORKSPACE / "integrations/tldv/analyzer.py"


def log(msg):
    ts = datetime.now().isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def run_script(script: Path, meeting_id: str, dry_run: bool = False) -> tuple[bool, str]:
    """Roda enrich ou analyze para um meeting_id. Retorna (success, output)."""
    cmd = ["python3", str(script), "--meeting-id", meeting_id]
    if dry_run:
        return True, f"[dry-run] would run: {' '.join(cmd)}"

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            env={
                "TLDV_API_KEY": os.environ["TLDV_API_KEY"],
                "PYTHONPATH": os.environ["PYTHONPATH"],
            },
        )
        if result.returncode == 0 and "[OK]" in result.stdout:
            return True, result.stdout.strip()
        return False, f"rc={result.returncode}: {result.stderr[:200]}"
    except subprocess.TimeoutExpired:
        return False, "timeout 300s"
    except Exception as e:
        return False, str(e)


def process_event(event: dict, dry_run: bool = False) -> dict:
    """Processa um evento: enrich + analyze. Retorna resultado."""
    event_id = event.get("id", "?")
    meeting_id = event.get("meetingId", "?")
    event_type = event.get("eventType", "?")
    outcome = {
        "event_id": event_id,
        "meeting_id": meeting_id,
        "event_type": event_type,
        "enrich_ok": False,
        "analyze_ok": False,
        "errors": [],
    }

    log(f"Processando evento {event_id} | {event_type} | meeting={meeting_id}")

    # Etapa 1: enrich
    if dry_run:
        log(f"  [DRY] enrich {meeting_id}")
        outcome["enrich_ok"] = True
    else:
        ok, out = run_script(ENRICH_SCRIPT, meeting_id, dry_run)
        outcome["enrich_ok"] = ok
        if not ok:
            outcome["errors"].append(f"enrich: {out}")
            log(f"  ✗ enrich failed: {out}")
        else:
            log(f"  ✓ enrich OK")

    # Etapa 2: analyze (só se enrich ok)
    if outcome["enrich_ok"] or dry_run:
        if dry_run:
            log(f"  [DRY] analyze {meeting_id}")
            outcome["analyze_ok"] = True
        else:
            ok, out = run_script(ANALYZE_SCRIPT, meeting_id, dry_run)
            outcome["analyze_ok"] = ok
            if not ok:
                outcome["errors"].append(f"analyze: {out}")
                log(f"  ✗ analyze failed: {out}")
            else:
                log(f"  ✓ analyze OK")

    # Etapa 3: persist
    if not dry_run and outcome["enrich_ok"]:
        try:
            persist_cmd = ["python3", str(WORKSPACE / "integrations/tldv/persister.py")]
            subprocess.run(persist_cmd, capture_output=True, timeout=60, env={
                "PYTHONPATH": os.environ["PYTHONPATH"],
            })
            log(f"  ✓ persister OK")
        except Exception as e:
            outcome["errors"].append(f"persister: {e}")
            log(f"  ! persister error: {e}")

    outcome["processed_at"] = datetime.now().isoformat()
    return outcome


def move_event(event_file: Path, outcome: dict):
    """Move evento para processed/ ou failed/."""
    dest_dir = PROCESSED_DIR if not outcome["errors"] else FAILED_DIR
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / event_file.name
    with open(dest, "w") as f:
        json.dump(outcome, f, indent=2, ensure_ascii=False)
    event_file.unlink()
    log(f"  → {dest_dir.name}/{dest.name}")


def list_pending_events() -> list[Path]:
    """Lista eventos pendentes na fila."""
    if not QUEUE_DIR.exists():
        return []
    return sorted(
        [p for p in QUEUE_DIR.glob("*.json") if not p.name.startswith(".")]
    )


def run(dry_run: bool = False, limit: int = 0, meeting_id: str = ""):
    """
    Modo normal: processa fila de eventos.
    meeting_id: força reprocessamento direto de uma reunião.
    """
    log(f"=== QUEUE PROCESSOR INICIADO | dry={dry_run} | limit={limit} | meeting={meeting_id} ===")

    if meeting_id:
        # Reprocessamento específico — não usa webhook queue
        log(f"Forçando reprocessamento de {meeting_id}")
        fake_event = {
            "id": f"manual-{meeting_id}",
            "meetingId": meeting_id,
            "eventType": "ManualTrigger",
        }
        result = process_event(fake_event, dry_run=dry_run)
        log(f"Resultado: enrich={result['enrich_ok']} analyze={result['analyze_ok']} errors={len(result['errors'])}")
        return

    events = list_pending_events()
    if not events:
        log("Nenhum evento na fila.")
        return

    if limit:
        events = events[:limit]

    log(f"Processando {len(events)} eventos...")

    for event_path in events:
        try:
            event = json.loads(event_path.read_text())
        except Exception as e:
            log(f"Erro lendo {event_path.name}: {e}")
            continue

        result = process_event(event, dry_run=dry_run)
        if not dry_run:
            move_event(event_path, result)

        # Pausa entre eventos
        if not dry_run:
            time.sleep(3)

    log("=== QUEUE PROCESSOR FINALIZADO ===")


def main():
    parser = argparse.ArgumentParser(description="Queue processor tl;dv")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--meeting-id", type=str, default="",
                        help="Força reprocessamento de reunião específica (ignora fila)")
    args = parser.parse_args()
    run(dry_run=args.dry_run, limit=args.limit, meeting_id=args.meeting_id)


if __name__ == "__main__":
    main()
