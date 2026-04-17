#!/bin/bash
# run_summary.sh — Estágio 2: resumo automático diário
# Roda todo dia às 7h via cron
cd /root/.openclaw/workspace
: "${TLDV_API_KEY:?TLDV_API_KEY não definida no ambiente (ver .env.example)}"
export TLDV_API_KEY
PYTHONPATH=/root/.openclaw/workspace/integrations \
python3 integrations/tldv/summarizer.py >> logs/tldv_summary.log 2>&1
echo "$(date): Done" >> logs/tldv_summary.log
