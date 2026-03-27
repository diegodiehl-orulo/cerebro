# MiniMax Health Checklist

## Teste de Regressão (5 casos)

| # | Caso | Comando | Esperado |
|---|------|---------|----------|
| 1 | Request simples | `curl ... "ok"` | 200 OK |
| 2 | Contexto médio | `curl ... "liste 3 prioridades"` | 200 OK |
| 3 | Contexto grande | `curl ... "resuma em 3 linhas..."` | 200 OK |
| 4 | 3 requests rápidos | 3x sequencial | 3x 200 OK |
| 5 | Latência p95 | tempo médio | < 15s |

## Monitoramento

- **Health check:** `python3 scripts/minimax_health.py`
- **Log:** `/root/.config/morfeu/minimax_health.log`
- **Frequência:** Diária 09:00 BRT

## Alertas

| Condição | Ação |
|----------|------|
| 2+ falhas em 3 requests | Alertar |
| p95 > 15s | Alertar |
| consecutiveErrors >= 3 | Alertar |

## Histórico

- **05/03/2026:** Configuração inicial
  - API: MiniMax M2.5
  - Latência avg: ~5s
  - p95: ~7.5s
