#!/bin/bash
# tldv_daily.sh — rotinas diárias tl;dv (digest + task generation + index)
# Roda todos os dias às 08h via cron OpenClaw

export TLDV_API_KEY="69f9a821-7286-46e8-a64c-7c1f20a01576"
export PYTHONPATH=/root/.openclaw/workspace/integrations
WORKDIR=/root/.openclaw/workspace/integrations/tldv
LOGDIR=/root/.openclaw/workspace/logs

DATE_SINCE=$(date -d '1 day ago' +%Y-%m-%d)
TS=$(date +%Y%m%d_%H%M%S)

echo "[$TS] === TL;DV DAILY ==="

# 1. Digest
echo "[$TS] Pipeline digest..."
python3 $WORKDIR/pipeline.py \
  --stage digest \
  --since $DATE_SINCE \
  --verbose >> $LOGDIR/tldv_digest_$TS.log 2>&1

# 2. Task generation
echo "[$TS] Task generation..."
python3 $WORKDIR/task_generator.py \
  --since $DATE_SINCE >> $LOGDIR/tldv_tasks_$TS.log 2>&1

# 3. Index rebuild
echo "[$TS] Index rebuild..."
python3 $WORKDIR/indexer.py --rebuild >> $LOGDIR/tldv_indexer_$TS.log 2>&1

echo "[$TS] === DONE ==="
