#!/bin/bash
# analyzer_batch.sh — processa uma fatia de meetings via analyzer.py
# Uso: ./analyzer_batch.sh <slice_num> <slice_file>
SLICE_NUM=$1
SLICE_FILE=$2
LOG_PREFIX="[SLICE-${SLICE_NUM}]"

export TLDV_API_KEY="69f9a821-7286-46e8-a64c-7c1f20a01576"
export PYTHONPATH="/root/.openclaw/workspace/integrations"
ANALYZER="/root/.openclaw/workspace/integrations/tldv/analyzer.py"
LEDGER="/root/.openclaw/workspace/memory/meetings/ledger/analyzed_ledger.json"
LOG="/root/.openclaw/workspace/logs/tldv_analyzer_slice${SLICE_NUM}.log"

echo "$LOG_PREFIX Iniciando slice ${SLICE_NUM} ($(wc -l < "$SLICE_FILE") meetings)" | tee -a "$LOG"
echo "$LOG_PREFIX PID=$$" | tee -a "$LOG"

count=0
errors=0
while IFS= read -r mid; do
    count=$((count+1))
    if [ -f "$LEDGER" ] && grep -q "\"$mid\"" "$LEDGER" 2>/dev/null; then
        echo "$LOG_PREFIX [SKIP $count] $mid (ja analisado)" | tee -a "$LOG"
        continue
    fi
    echo "$LOG_PREFIX [RUN $count] $mid" >> "$LOG"
    output=$(
        timeout 180 python3 "$ANALYZER" --meeting-id "$mid" 2>&1
    ) >> "$LOG" 2>&1
    if echo "$output" | grep -q "\[OK\]"; then
        echo "$LOG_PREFIX [OK $count] $mid" | tee -a "$LOG"
    else
        errors=$((errors+1))
        echo "$LOG_PREFIX [ERR $count] $mid — $output" | tee -a "$LOG"
    fi
    # small pause to avoid hammering
    sleep 1
done < "$SLICE_FILE"

echo "$LOG_PREFIX Finalizado. Processados: $count | Erros: $errors" | tee -a "$LOG"
