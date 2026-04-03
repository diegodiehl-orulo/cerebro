#!/bin/bash
# Health check: sync-cerebro
# Roda diariamente — só notifica se houver problema

LOG="/root/.openclaw/logs/sync-cerebro.log"
CEREBRO="/root/.openclaw/cerebro"
WORKSPACE="/root/.openclaw/workspace"
LAST_RUN_WINDOW=9000  # ~2.5h em segundos

# 1. Verificar se log existe e tem OK recente
if [ ! -f "$LOG" ]; then
  echo "[HEALTH] ERRO: log não encontrado: $LOG"
  exit 1
fi

LAST_OK=$(grep -c "Sync cerebro -> workspace done" "$LOG" 2>/dev/null || echo 0)
if [ "$LAST_OK" -eq 0 ]; then
  echo "[HEALTH] ERRO: nenhum sync bem-sucedido no log"
  exit 1
fi

# 2. Verificar se cerebro está acessível e commiteado
cd "$CEREBRO"
git rev-parse --verify HEAD >/dev/null 2>&1 || {
  echo "[HEALTH] ERRO: repo cerebro inacessível"
  exit 1
}

# 3. Verificar se workspace tem arquivos (não está vazio)
WS_COUNT=$(find "$WORKSPACE" -maxdepth 1 -name "*.md" | wc -l)
if [ "$WS_COUNT" -lt 5 ]; then
  echo "[HEALTH] ERRO: workspace com poucos arquivos ($WS_COUNT)"
  exit 1
fi

# 4. Verificar se último push/pull do repo não é muito antigo (>7 dias)
LAST_COMMIT_EPOCH=$(git log -1 --format=%ct origin/main 2>/dev/null || echo 0)
NOW_EPOCH=$(date +%s)
DAYS_SINCE=$(( (NOW_EPOCH - LAST_COMMIT_EPOCH) / 86400 ))

if [ "$DAYS_SINCE" -gt 7 ]; then
  echo "[HEALTH] ATENÇÃO: último commit há $DAYS_SINCE dias (repo pode estar parado)"
  exit 1
fi

echo "[HEALTH] OK — sync cerebro: $LAST_OK syncs no log | último commit: ${DAYS_SINCE}d | workspace: ${WS_COUNT} arquivos"
exit 0
