#!/bin/bash
# tldv_daily.sh — rotinas diárias tl;dv (digest + task generation + index)
# Roda todos os dias às 08h via cron

source "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/integrations/tldv/_boot.sh"

DATE_SINCE=$(date -d '1 day ago' +%Y-%m-%d)
TS=$(date +%Y%m%d_%H%M%S)

echo "[$TS] === TL;DV DAILY ==="
echo "[$TS] WORKSPACE=$WORKSPACE"

# 1. Digest
echo "[$TS] Pipeline digest..."
python3 "$TLDV_DIR/pipeline.py" \
  --stage digest \
  --since "$DATE_SINCE" \
  --verbose >> "$LOGDIR/tldv_digest_$TS.log" 2>&1

# 2. Task generation
echo "[$TS] Task generation..."
python3 "$TLDV_DIR/task_generator.py" \
  --since "$DATE_SINCE" >> "$LOGDIR/tldv_tasks_$TS.log" 2>&1

# 3. Index rebuild
echo "[$TS] Index rebuild..."
python3 "$TLDV_DIR/indexer.py" --rebuild >> "$LOGDIR/tldv_indexer_$TS.log" 2>&1

echo "[$TS] === DONE ==="
