#!/usr/bin/env python3
"""
P3 — Quota Estimator para MiniMax (sliding window de 5 horas)
Estima quantos prompts restam na janela atual com base no histórico de execuções.
Uso: python3 quota_estimator.py [--json] [--update]

Saída padrão:
  REMAINS:XX — estimativa de prompts restantes

Com --json:
  {"remains": XX, "used_in_window": XX, "window_start": "HH:MM", "estimated": true}

Com --update:
  Escreve a estimativa em /root/.config/morfeu/minimax_quota.json
"""

import sys
import os
import json
import time
import glob
from datetime import datetime, timedelta

RUNS_DIR = "/root/.openclaw/cron/runs/"
QUOTA_FILE = "/root/.config/morfeu/minimax_quota.json"
QUOTA_MAX = 100
WINDOW_HOURS = 5

def count_prompts_in_window():
    """Conta execuções de LLM nas últimas WINDOW_HOURS horas."""
    cutoff = time.time() - (WINDOW_HOURS * 3600)
    count = 0

    if not os.path.exists(RUNS_DIR):
        return 0

    for rf in glob.glob(RUNS_DIR + "*.jsonl"):
        try:
            with open(rf) as f:
                for line in f:
                    try:
                        d = json.loads(line.strip())
                        ts = d.get("ts") or d.get("startedAt") or 0
                        if isinstance(ts, str):
                            ts = int(ts) / 1000 if len(ts) > 10 else int(ts)
                        else:
                            ts = float(ts)
                            if ts > 1e12:
                                ts = ts / 1000

                        if ts < cutoff:
                            continue

                        # Contar apenas execuções que realmente rodaram LLM
                        # (jobs com status ok ou error, não skipped/no_reply)
                        status = d.get("status", "")
                        if status in ("ok", "error"):
                            count += 1
                    except Exception:
                        continue
        except Exception:
            continue

    return count

def main():
    json_mode = "--json" in sys.argv
    update_mode = "--update" in sys.argv

    used = count_prompts_in_window()
    remains = max(0, QUOTA_MAX - used)
    window_start = (datetime.now() - timedelta(hours=WINDOW_HOURS)).strftime("%H:%M")

    result = {
        "remains": remains,
        "used_in_window": used,
        "quota_max": QUOTA_MAX,
        "window_hours": WINDOW_HOURS,
        "window_start": window_start,
        "estimated": True,
        "updated_at": datetime.now().isoformat()
    }

    if update_mode:
        os.makedirs(os.path.dirname(QUOTA_FILE), exist_ok=True)
        with open(QUOTA_FILE, "w") as f:
            json.dump(result, f, indent=2)

    if json_mode:
        print(json.dumps(result))
    else:
        print(f"REMAINS:{remains}")
        if used > 0:
            print(f"  Usados nas últimas {WINDOW_HOURS}h: {used}/{QUOTA_MAX}")
            print(f"  Janela iniciou às: {window_start}")

    # Alerta se pouco restante
    if remains < 15:
        print(f"⚠️ ALERTA: Apenas {remains} prompts restantes na janela!")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
