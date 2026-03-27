#!/bin/bash
# backup_diego.sh — Backup diário do workspace do Morfeu para Google Drive
# Cron: 0 2 * * * (02:00 BRT = 05:00 UTC)
# Destino: Google Drive pasta 1F4RKBw6XuQQUGeTjnGneaSXTR7JnagbH (Ambiente de Trabalho - Open Claw IA)

set -euo pipefail

TIMESTAMP=$(date +%Y-%m-%d)
BACKUP_NAME="morfeu-backup-${TIMESTAMP}.tar.gz"
TMP_DIR="/tmp/morfeu_backup"
BACKUP_FILE="${TMP_DIR}/${BACKUP_NAME}"
FOLDER_ID="1F4RKBw6XuQQUGeTjnGneaSXTR7JnagbH"
LOG_PREFIX="[backup_diego] $(date '+%Y-%m-%d %H:%M:%S')"

echo "${LOG_PREFIX} Iniciando backup..."

# Criar diretório temporário
mkdir -p "${TMP_DIR}"

# Criar arquivo tar.gz com os diretórios importantes
tar -czf "${BACKUP_FILE}" \
    --exclude="/root/.openclaw/workspace/scripts/deprecated" \
    /root/.openclaw/workspace/ \
    /root/.config/morfeu/ \
    /root/.config/gcalcli/ \
    2>/dev/null || true

BACKUP_SIZE=$(du -sh "${BACKUP_FILE}" | cut -f1)
echo "${LOG_PREFIX} Arquivo criado: ${BACKUP_NAME} (${BACKUP_SIZE})"

# Upload para Google Drive via gog
echo "${LOG_PREFIX} Fazendo upload para Google Drive..."
gog-morfeu drive upload "${BACKUP_FILE}" --parent "${FOLDER_ID}" --name "${BACKUP_NAME}" 2>&1

echo "${LOG_PREFIX} Backup concluído com sucesso."

# Limpar arquivo temporário
rm -f "${BACKUP_FILE}"
rmdir "${TMP_DIR}" 2>/dev/null || true
