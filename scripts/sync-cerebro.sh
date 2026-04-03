#!/bin/bash
# Sync cerebro (GitHub) <-> workspace
# Bidirectional: pull + push entre workspace e GitHub
# Push sobe alterações do workspace pro GitHub

WORKSPACE="/root/.openclaw/workspace"
LOG="/root/.openclaw/logs/sync-cerebro.log"
SSH_CMD="ssh -i ~/.ssh/id_ed25519_morfeu_vps"

cd "$WORKSPACE"

# Pull: atualiza workspace com último commit do GitHub
GIT_SSH_COMMAND="$SSH_CMD" git pull origin master 2>&1 >> "$LOG"

# Push: sobe alterações locais para o GitHub
GIT_SSH_COMMAND="$SSH_CMD" git push origin master 2>&1 >> "$LOG"

echo "[$(date)] Sync done — pull + push" >> "$LOG"
