#!/bin/bash
# analyzer_runner.sh — Loop sequencial resiliente do analyzer tl;dv
# Roda em foreground ou via nohup; trata erros individualmente, não para.
#
# Uso:
#   nohup bash analyzer_runner.sh >> "$LOGDIR/tldv_analyzer_runner.log" 2>&1 &
#   tail -f "$WORKSPACE/logs/tldv_analyzer_runner.log"
#
# Para matar: pkill -f analyzer_runner.sh

set -u

# Boot: workspace + .env + PYTHONPATH
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_boot.sh"

ANALYZER="$TLDV_DIR/analyzer.py"
LEDGER="$WORKSPACE/memory/meetings/ledger/analyzed_ledger.json"
PENDING_FILE="$WORKSPACE/memory/meetings/ledger/analyze_pending_2026.json"
ANALYSIS_DIR="$WORKSPACE/memory/meetings/analysis"
LOG="$LOGDIR/tldv_analyzer_runner.log"

mkdir -p "$(dirname "$LOG")" "$ANALYSIS_DIR"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG"
}

load_pending() {
    if [ ! -f "$PENDING_FILE" ]; then
        log "Arquivo de pendentes não encontrado: $PENDING_FILE"
        exit 1
    fi
    PENDING_FILE_ENV="$PENDING_FILE" LEDGER_ENV="$LEDGER" python3 - <<'EOF'
import json, os
from pathlib import Path

ledger_file = Path(os.environ["LEDGER_ENV"])
analyzed = set()
if ledger_file.exists():
    with open(ledger_file) as f:
        analyzed = set(json.load(f).get("analyzed", []))

pending_file = Path(os.environ["PENDING_FILE_ENV"])
pending_ids = []
if pending_file.exists():
    all_pending = json.loads(pending_file.read_text())
    pending_ids = [mid for mid in all_pending if mid not in analyzed]

print(f"{len(pending_ids)}")
for mid in pending_ids:
    print(mid)
EOF
}

save_ledger() {
    LEDGER_ENV="$LEDGER" python3 - <<'EOF'
import json, os, datetime
from pathlib import Path

ledger_file = Path(os.environ["LEDGER_ENV"])
if ledger_file.exists():
    with open(ledger_file) as f:
        data = json.load(f)
else:
    data = {"analyzed": [], "failed": [], "stats": {"analyzed": 0, "failed": 0}}

for mid in os.environ.get('ANALYZED_IDS', '').split(','):
    mid = mid.strip()
    if mid and mid not in data.get('analyzed', []):
        data.setdefault('analyzed', []).append(mid)
for mid in os.environ.get('FAILED_IDS', '').split(','):
    mid = mid.strip()
    if mid and mid not in data.get('failed', []):
        data.setdefault('failed', []).append(mid)

data.setdefault('stats', {})
data['stats']['analyzed'] = len(data.get('analyzed', []))
data['stats']['failed'] = len(data.get('failed', []))
data['last_run'] = datetime.datetime.now().isoformat()

tmp = ledger_file.with_suffix('.tmp')
tmp.parent.mkdir(parents=True, exist_ok=True)
with open(tmp, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
tmp.replace(ledger_file)
print("Ledger atualizado")
EOF
}

log "=== ANALYZER RUNNER INICIADO ==="
log "WORKSPACE: $WORKSPACE | PID: $$"

PENDING_OUTPUT=$(load_pending)
TOTAL_PENDING=$(echo "$PENDING_OUTPUT" | head -1)
IDS=$(echo "$PENDING_OUTPUT" | tail -n +2)

log "Meetings pendentes: $TOTAL_PENDING"

count=0
analyzed_ids=""
failed_ids=""
errors_seq=0

for mid in $IDS; do
    count=$((count+1))

    if [ -f "$ANALYSIS_DIR/${mid}.json" ]; then
        log "[$count/$TOTAL_PENDING] $mid — ja existe (pulando)"
        continue
    fi

    log "[$count/$TOTAL_PENDING] Processando $mid..."

    output=$(timeout 600 python3 "$ANALYZER" --meeting-id "$mid" 2>&1)
    rc=$?

    if echo "$output" | grep -q "\[OK\]"; then
        analyzed_ids="${analyzed_ids},${mid}"
        errors_seq=0
        log "  -> OK"
    else
        failed_ids="${failed_ids},${mid}"
        errors_seq=$((errors_seq+1))
        log "  -> ERRO (rc=$rc): $(echo "$output" | tail -2)"
        if [ $errors_seq -ge 5 ]; then
            log "ALERTA: 5 erros seguidos. Pausando 60s..."
            sleep 60
            errors_seq=0
        fi
    fi

    if [ $((count % 25)) -eq 0 ]; then
        export ANALYZED_IDS="$analyzed_ids"
        export FAILED_IDS="$failed_ids"
        save_ledger
        analyzed_ids=""
        failed_ids=""
        log "Checkpoint salvo ($count processados)"
    fi

    sleep 5
done

if [ -n "$analyzed_ids" ] || [ -n "$failed_ids" ]; then
    export ANALYZED_IDS="$analyzed_ids"
    export FAILED_IDS="$failed_ids"
    save_ledger
fi

log "=== ANALYZER RUNNER FINALIZADO ==="
log "Total processados: $count"
log "Erros consecutivos finais: $errors_seq"
