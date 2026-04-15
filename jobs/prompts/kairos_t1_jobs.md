# JOB: KAIROS T1 — Jobs com Falha Recorrente
**Schedule:** Seg-Sex 10h00 BRT
**Timeout:** 60s
**Modelo:** minimax/MiniMax-M2.5
**Gate:** remains ≥ 30

---

## O QUE FAZER

Checar se algum job falhou 3x ou mais nas últimas 24h.

## EXECUÇÃO

Executar via cron API ou logs locais:

```bash
# Verificar cron jobs com consecutiveErrors >= 3
# Se usar cron list API, buscar state.consecutiveErrors >= 3

# Alternativa: ler logs de jobs
ls /root/.openclaw/workspace/logs/*.log 2>/dev/null | head -20
```

## DECISÃO

Se encontrar job com 3x+ falha:
```
⚠️ KAIROS — Job com falha recorrente
🔴 Job: [nome] falhou [N]x nas últimas 24h
👉 Verificar: job travado, quota esgotada ou credencial expirou?
```

Se não encontrar: **NO_REPLY**