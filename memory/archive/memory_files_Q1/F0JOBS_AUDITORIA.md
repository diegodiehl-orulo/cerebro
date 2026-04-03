# FASE 0 — AUDITORIA DE JOBS
## Executado: 2026-04-03

### Jobs com erros consecutivos (requerem atenção)

| Job | Erros | Tipo | Ação necessária |
|-----|-------|------|----------------|
| validacao_p1a (Seg-Sex 07h30/17h30) | 2 | timeout | Revisar prompt ou aumentar timeout |
| vendas-daily-18h | 2 | timeout | Script precisa de DRI ou remoção |
| health-sync-cerebro (09h) | 2 | timeout | Verificar sync-cerebro-health.sh |
| analise_erros (Seg-Sex 07h) | 1 | timeout | Revisar prompt |
| Follow-up semanal Zanella (Ter 08h50) | 1 | model_not_found | Haiku não existe — corrigir para MiniMax |
| Trinks booking (Dom 08h) | 1 | timeout | Aguarda TRINKS_PASSWORD |
| verifica_contratos (Seg-Sex 11h20) | timeout | timeout | Script precisa de revisão |

### Jobs desabilitados (manter assim por agora)

- Briefing Dominical (pausado 60d — reavalia 16/05)
- Harvester lessons/decisions (pausado 60d)
- MiniMax Health Check (unificado em outro job)
- Smart Email Scan (pausado — reavaliar)
- Scan Praças Weekly (pausado — reavaliar 16/05)
- Daily Briefing (pausado — reavaliar)
- Check-in Praças + Pulse Praças (manual por enquanto)

### Decisão operacional

**Manter jobs críticos ativos + pausar os restantes conforme planejado.**

### Status: ✅ AUDITADO — Pendente decisão estratégica de Diego
