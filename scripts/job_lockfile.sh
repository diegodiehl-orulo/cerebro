#!/bin/bash
# P3 — Lockfile para controle de overlap entre jobs LLM
# Uso: source job_lockfile.sh <JOB_ID>
# Garante que apenas 1 instância do job rode por vez.
# Exemplo: source /root/.openclaw/workspace/scripts/job_lockfile.sh "revisao-semanal"

JOB_ID="${1:-unknown}"
LOCKFILE="/tmp/morfeu-job-${JOB_ID}.lock"
MAX_AGE_SECONDS=360  # 6 minutos — se lock for mais antigo, considera travado e remove

# Verificar se lock existe e se está fresco
if [ -f "$LOCKFILE" ]; then
    LOCK_AGE=$(( $(date +%s) - $(stat -c %Y "$LOCKFILE" 2>/dev/null || echo 0) ))
    if [ "$LOCK_AGE" -lt "$MAX_AGE_SECONDS" ]; then
        echo "🔒 Job '$JOB_ID' já está em execução (lock age: ${LOCK_AGE}s). Saindo."
        exit 0
    else
        echo "⚠️ Lock antigo detectado (${LOCK_AGE}s). Removendo e prosseguindo."
        rm -f "$LOCKFILE"
    fi
fi

# Criar lock
echo "$$" > "$LOCKFILE"

# Cleanup automático ao sair
trap "rm -f $LOCKFILE; echo '🔓 Lock liberado: $JOB_ID'" EXIT

echo "✅ Lock adquirido: $JOB_ID (PID $$)"
