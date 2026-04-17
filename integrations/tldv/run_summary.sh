#!/bin/bash
# run_summary.sh — Estágio 2: resumo automático diário
# Roda todo dia às 7h via cron
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_boot.sh"

cd "$WORKSPACE"
python3 "$TLDV_DIR/summarizer.py" >> "$LOGDIR/tldv_summary.log" 2>&1
echo "$(date): Done" >> "$LOGDIR/tldv_summary.log"
