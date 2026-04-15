# JOB: Validação P1-A — Constraint Check Simplificado
**Frequência:** Seg-Sex 07h30 e 17h30 BRT
**Modelo:** minimax/MiniMax-M2.5
**Timeout:** 60s

---

## REGRA CRÍTICA
⚠️ Execute SOMENTE com MiniMax. Se outro modelo for necessário → NO_REPLY.

---

## O QUE FAZER

Checar se os jobs críticos executaram recentemente. Se não executaram → alertar Diego.

## JOBS CRÍTICOS A MONITORAR

| Job ID | Nome | Status esperado |
|--------|------|-----------------|
| `19741391` | Daily Briefing | Último OK após 08:45 seg-sex |
| `2fd44846` | tldv-digest-diario | Último OK após 08:00 diário |
| `aa1c9ef9` | sync-cerebro Health | Último OK nas últimas 2h |

## EXECUÇÃO

```bash
# Verificar cron state via health scripts
python3 /root/.openclaw/workspace/scripts/sync-cerebro-health.sh
echo "health exit: $?"
```

## DECISÃO

1. Se health script retorna exit 0 → NÃO ALERTAR (está rodando)
2. Se health script retorna exit != 0 → Alerta simples:
```
⚠️ *Constraint Check — [data]*
🔴 Sync GitHub pode estar com problema
👉 Verificar: cron rodou? credencial expirou?
```
3. Jobs da lista com consecutiveErrors >= 3 → 1 linha de alerta por job
4. Se tudo ok → **NO_REPLY**

---

## REGRAS
- Simplicidade: 1 alerta = 1 job = 1 linha
- Não tentar ler outputs complexos — só checar se executou OK
- Output máximo: 3 linhas por execução