#!/bin/bash
# run_tldv.sh — Runner unificado e inteligente da rotina tl;dv.
#
# Substitui run_tldv_2026.sh e run_tldv_lote1.sh (listas hardcoded, paths
# quebrados, segredos inline). Agora:
#
#   • Workspace auto-detectado (portável entre máquinas)
#   • Secrets via .env (nunca em git)
#   • Modos: full | collect | enrich | analyze | persist | tasks | digest | retry
#   • Filtros: --since, --limit, --ids-file, --meeting-id
#   • Health check antes de começar (fail-fast se API inacessível)
#   • Resumo no final (novas, falhas, pendentes de retry)
#
# Exemplos:
#   ./run_tldv.sh                              # pipeline completo (collect→persist)
#   ./run_tldv.sh full                         # idem
#   ./run_tldv.sh analyze --since 2026-04-01   # só analisa desde data X
#   ./run_tldv.sh retry                        # reprocessa pendentes de 204
#   ./run_tldv.sh tasks                        # regera tarefas consolidadas
#   ./run_tldv.sh meeting <id>                 # pipeline completo para 1 ID
#   ./run_tldv.sh ids --ids-file lista.txt    # analisa cada ID do arquivo

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/integrations/tldv/_boot.sh"

# ── Args parsing ─────────────────────────────────────────────────────────────
MODE="${1:-full}"
shift || true

SINCE=""
LIMIT=""
IDS_FILE=""
MEETING_ID=""
DRY_RUN=""
VERBOSE=""

while [ $# -gt 0 ]; do
    case "$1" in
        --since)       SINCE="$2"; shift 2 ;;
        --limit)       LIMIT="$2"; shift 2 ;;
        --ids-file)    IDS_FILE="$2"; shift 2 ;;
        --meeting-id)  MEETING_ID="$2"; shift 2 ;;
        --dry-run)     DRY_RUN="--dry-run"; shift ;;
        --verbose|-v)  VERBOSE="--verbose"; shift ;;
        *)             # meeting ID posicional (modo "meeting <id>")
                       if [ -z "$MEETING_ID" ] && [ "$MODE" = "meeting" ]; then
                           MEETING_ID="$1"
                           shift
                       else
                           echo "Flag desconhecida: $1" >&2
                           exit 2
                       fi
                       ;;
    esac
done

# ── Logger ───────────────────────────────────────────────────────────────────
TS="$(date +%Y%m%d_%H%M%S)"
LOG="$LOGDIR/tldv_run_${MODE}_${TS}.log"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }

log "=== run_tldv.sh INICIADO ==="
log "Mode: $MODE | Workspace: $WORKSPACE"
[ -n "$SINCE" ]      && log "Since: $SINCE"
[ -n "$LIMIT" ]      && log "Limit: $LIMIT"
[ -n "$MEETING_ID" ] && log "Meeting: $MEETING_ID"
[ -n "$IDS_FILE" ]   && log "IDs file: $IDS_FILE"
[ -n "$DRY_RUN" ]    && log "DRY RUN"

# ── Health check ─────────────────────────────────────────────────────────────
health_check() {
    if [ -z "${TLDV_API_KEY:-}" ]; then
        log "ERRO: TLDV_API_KEY ausente. Defina em $WORKSPACE/.env ou export direto."
        return 1
    fi
    log "Health check tl;dv API..."
    if python3 "$TLDV_DIR/test_health.py" >> "$LOG" 2>&1; then
        log "  ✓ API acessível"
        return 0
    fi
    log "  ✗ API inacessível — abortando"
    return 1
}

# ── Runners ──────────────────────────────────────────────────────────────────
run_full() {
    health_check || return 1
    local args="--stage collect,enrich,analyze,persist"
    [ -n "$SINCE" ]  && args="$args --since $SINCE"
    [ -n "$DRY_RUN" ] && args="$args $DRY_RUN"
    [ -n "$VERBOSE" ] && args="$args $VERBOSE"
    python3 "$TLDV_DIR/pipeline.py" $args 2>&1 | tee -a "$LOG"
}

run_stage() {
    local stage="$1"
    health_check || return 1
    local args="--stage $stage"
    [ -n "$SINCE" ]  && args="$args --since $SINCE"
    [ -n "$DRY_RUN" ] && args="$args $DRY_RUN"
    [ -n "$VERBOSE" ] && args="$args $VERBOSE"
    python3 "$TLDV_DIR/pipeline.py" $args 2>&1 | tee -a "$LOG"
}

run_meeting() {
    if [ -z "$MEETING_ID" ]; then
        log "ERRO: --meeting-id ou posicional obrigatório para modo 'meeting'"
        return 2
    fi
    health_check || return 1
    python3 "$TLDV_DIR/pipeline.py" --meeting-id "$MEETING_ID" 2>&1 | tee -a "$LOG"
}

run_ids() {
    if [ -z "$IDS_FILE" ] || [ ! -f "$IDS_FILE" ]; then
        log "ERRO: --ids-file com caminho válido obrigatório para modo 'ids'"
        return 2
    fi
    health_check || return 1
    local count=0 ok=0 fail=0 skip=0
    while IFS= read -r mid; do
        mid="$(echo "$mid" | tr -d '[:space:]')"
        [ -z "$mid" ] && continue
        case "$mid" in \#*) continue ;; esac
        count=$((count+1))
        local analysis_file="$WORKSPACE/memory/meetings/analysis/${mid}.json"
        if [ -f "$analysis_file" ]; then
            log "[$count] $mid — já analisado, skip"
            skip=$((skip+1))
            continue
        fi
        log "[$count] $mid — processando"
        if python3 "$TLDV_DIR/pipeline.py" --meeting-id "$mid" >> "$LOG" 2>&1; then
            ok=$((ok+1))
        else
            fail=$((fail+1))
            log "  ✗ falha ($mid)"
        fi
        sleep "${TLDV_RATE_LIMIT_PAUSE:-3}"
    done < "$IDS_FILE"
    log "IDs processados: total=$count ok=$ok fail=$fail skip=$skip"
}

run_retry() {
    # Reprocessa reuniões que ficaram em pending (transcript 204).
    local pending_file="$WORKSPACE/memory/meetings/ledger/enrich_pending_retry.json"
    if [ ! -f "$pending_file" ]; then
        log "Sem fila de retry em $pending_file"
        return 0
    fi
    local count
    count=$(python3 -c "import json; d=json.load(open('$pending_file')); print(len(d))")
    log "Retry: $count reuniões pendentes (204)"
    health_check || return 1
    python3 "$TLDV_DIR/enricher.py" 2>&1 | tee -a "$LOG"
    python3 "$TLDV_DIR/pipeline.py" --stage analyze,persist 2>&1 | tee -a "$LOG"
}

# ── Dispatch ─────────────────────────────────────────────────────────────────
case "$MODE" in
    full)                     run_full ;;
    collect|enrich|analyze|persist|digest) run_stage "$MODE" ;;
    tasks)                    python3 "$TLDV_DIR/task_generator.py" ${SINCE:+--since $SINCE} 2>&1 | tee -a "$LOG" ;;
    meeting)                  run_meeting ;;
    ids)                      run_ids ;;
    retry)                    run_retry ;;
    health)                   health_check ;;
    config)                   python3 "$TLDV_DIR/config.py" ;;
    *)
        cat <<EOF
Uso: $0 <mode> [opts]

Modos:
  full              pipeline completo (collect→enrich→analyze→persist) [default]
  collect           só baixa reuniões novas da API
  enrich            só enriquece (transcript + notes)
  analyze           só analisa reuniões enriquecidas (LLM)
  persist           só persiste análises em memory/*.md
  digest            gera digest consolidado
  tasks             regera tarefas consolidadas (task_generator)
  meeting <id>      pipeline completo para 1 reunião
  ids --ids-file F  processa cada ID do arquivo F (um por linha, # = comentário)
  retry             reprocessa pendentes de 204 (transcript pending)
  health            testa conectividade tl;dv API
  config            imprime configuração atual (paths + status das secrets)

Opções:
  --since YYYY-MM-DD   filtra por data
  --limit N            limita quantidade processada
  --meeting-id ID      id explícito (alternativa ao posicional em 'meeting')
  --dry-run            mostra o que faria sem executar
  --verbose            log detalhado
EOF
        exit 2
        ;;
esac

RC=$?
log "=== run_tldv.sh FINALIZADO (rc=$RC) ==="
exit $RC
