#!/bin/bash
# Sync cerebro (GitHub) <-> workspace
# Bidirectional: pull + commit + push
# REGRA: se tree estiver suja, PARA e AVISA — não commit forçado
# REGRA: saída mínima, timestamps em formato legível

WORKSPACE="/root/.openclaw/workspace"
LOG="/root/.openclaw/logs/sync-cerebro.log"
SSH_CMD="ssh -i ~/.ssh/id_ed25519_morfeu_vps"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

cd "$WORKSPACE"

# Pull: atualiza workspace com último commit do GitHub
echo "[${TIMESTAMP}] Pull started" >> "$LOG"
GIT_SSH_COMMAND="$SSH_CMD" git pull origin master 2>&1 >> "$LOG"
if [ $? -ne 0 ]; then
    echo "[${TIMESTAMP}] ERRO no pull — aborting sync" >> "$LOG"
    exit 1
fi

# Verifica se tree está suja ANTES de commitar qualquer coisa
if ! git diff-index --quiet HEAD 2>/dev/null; then
    echo "[${TIMESTAMP}] ATENÇÃO: alterações locais sem commit — sync aguardando" >> "$LOG"
    echo "[${TIMESTAMP}] PARAR: não commitar com tree suja" >> "$LOG"
    exit 0  # sair OK mas sem push — problema do health check detectar
fi

# Push: sobe alterações para o GitHub (só se tree estiver limpa)
GIT_SSH_COMMAND="$SSH_CMD" git push origin master 2>&1 >> "$LOG"
if [ $? -ne 0 ]; then
    echo "[${TIMESTAMP}] ERRO no push" >> "$LOG"
    exit 1
fi

echo "[${TIMESTAMP}] Sync done" >> "$LOG"
