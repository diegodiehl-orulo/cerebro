#!/bin/bash
# Sync cerebro (GitHub) <-> workspace
# Bidirectional: pull + commit + push entre workspace e GitHub
# Commit automático antes de push — garante que nenhuma alteração local fique para trás

WORKSPACE="/root/.openclaw/workspace"
LOG="/root/.openclaw/logs/sync-cerebro.log"
SSH_CMD="ssh -i ~/.ssh/id_ed25519_morfeu_vps"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

cd "$WORKSPACE"

# Pull: atualiza workspace com último commit do GitHub
GIT_SSH_COMMAND="$SSH_CMD" git pull origin master 2>&1 >> "$LOG"

# Commit automático de alterações locais (se houver)
if ! git diff-index --quiet HEAD 2>/dev/null; then
    git add -A
    git commit -m "auto-sync: ${TIMESTAMP}" 2>&1 >> "$LOG"
    echo "[${TIMESTAMP}] Commit automático feito" >> "$LOG"
fi

# Push: sobe alterações para o GitHub
GIT_SSH_COMMAND="$SSH_CMD" git push origin master 2>&1 >> "$LOG"

echo "[${TIMESTAMP}] Sync done — pull + commit + push" >> "$LOG"
