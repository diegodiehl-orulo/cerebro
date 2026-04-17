#!/bin/bash
# _boot.sh — source'd pelos scripts tl;dv para inicializar ambiente.
# Descobre WORKSPACE via path do script, carrega .env, exporta PYTHONPATH.
#
# Uso nos scripts:
#   source "$(dirname "$0")/_boot.sh"
# Ou:
#   source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/_boot.sh"
#
# Após source, as seguintes variáveis estão disponíveis:
#   WORKSPACE         — raiz do cerebro
#   TLDV_DIR          — integrations/tldv
#   LOGDIR            — logs/
#   TLDV_API_KEY      — obrigatório (via env ou .env)
#   MINIMAX_API_KEY   — opcional (para analyzer_v2/summarizer)

# _boot.sh vive em integrations/tldv/, então WORKSPACE = ../.. (posição fixa).
# CEREBRO_HOME sobrescreve se definido.
_BOOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -n "${CEREBRO_HOME:-}" ]; then
    WORKSPACE="$CEREBRO_HOME"
elif [ -d "$_BOOT_DIR/../.." ] && [ -d "$_BOOT_DIR/../../integrations/tldv" ]; then
    WORKSPACE="$(cd "$_BOOT_DIR/../.." && pwd)"
elif [ -d "/root/.openclaw/workspace" ]; then
    WORKSPACE="/root/.openclaw/workspace"
else
    echo "[_boot.sh] ERRO: não consegui descobrir WORKSPACE. Defina CEREBRO_HOME." >&2
    return 1 2>/dev/null || exit 1
fi
export WORKSPACE
export CEREBRO_HOME="$WORKSPACE"

# Carrega .env (sem sobrescrever vars já definidas)
if [ -f "$WORKSPACE/.env" ]; then
    set -a
    while IFS='=' read -r key value; do
        [ -z "$key" ] && continue
        case "$key" in \#*) continue ;; esac
        value="${value%\"}"; value="${value#\"}"
        value="${value%\'}"; value="${value#\'}"
        if [ -z "${!key+x}" ]; then
            export "$key=$value"
        fi
    done < <(grep -v '^\s*$' "$WORKSPACE/.env" | grep -v '^\s*#')
    set +a
fi

export TLDV_DIR="$WORKSPACE/integrations/tldv"
export LOGDIR="$WORKSPACE/logs"
export PYTHONPATH="$WORKSPACE/integrations${PYTHONPATH:+:$PYTHONPATH}"

mkdir -p "$LOGDIR"

# Validação mínima (warn, não bloqueia — alguns scripts rodam sem a API key, ex. task_generator)
if [ -z "${TLDV_API_KEY:-}" ]; then
    echo "[_boot.sh] WARN: TLDV_API_KEY não definida (defina em $WORKSPACE/.env)" >&2
fi
