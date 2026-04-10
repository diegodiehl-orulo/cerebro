#!/bin/bash
# run_summary.sh — Estágio 2: resumo automático diário
# Roda todo dia às 7h via cron
cd /root/.openclaw/workspace
TLDV_API_KEY="69f9a821-7286-46e8-a64c-7c1f20a01576" \
PYTHONPATH=/root/.openclaw/workspace/integrations \
python3 integrations/tldv/summarizer.py >> logs/tldv_summary.log 2>&1
echo "$(date): Done" >> logs/tldv_summary.log
