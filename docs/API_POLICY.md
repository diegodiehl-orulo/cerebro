# 🔐 Política de Uso de API — Morfeu

> **Versão:** 1.0  
> **Data:** 05/03/2026  
> **Objetivo:** Controlar custos, evitar rate limits e garantir disponibilidade

---

## 1. Endpoints e Provedores

| Provider | Endpoint | Região | Status |
|----------|----------|--------|--------|
| **MiniMax (primário)** | `https://api.minimaxi.chat/v1` | CN (China) | ✅ Ativo |
| **Groq (fallback)** | `https://api.groq.com/openai/v1` | US (EUA) | ✅ Configurado |
| **Anthropic** | — | — | ❌ Não configurado |

---

## 2. Modelos e Custos

| Modelo | Input ($/1M) | Output ($/1M) | Uso |
|--------|-------------|--------------|-----|
| **MiniMax-M2.5** | $0.30 | $1.20 | Tarefas complexas (briefing, análise) |
| **MiniMax-M2.5-Lightning** | $0.05 | $0.20 | Tarefas rápidas (health check, tl;dv) |
| **Groq Llama-3.3-70B** | $0 | $0 | Fallback de emergência |

---

## 3. Classificação de Tarefas

### 🔴 P0 — Crítico (escrita obrigatória + alta prioridade)

| Tarefa | Modelo | Timeout | Concorrência | Retry |
|--------|--------|---------|--------------|-------|
| Daily Briefing (08:45) | M2.5 | 180s | 1 | 2x |
| Check Pós-Reunião (input) | M2.5 | 180s | 1 | 2x |
| Watchdog de Crons (09h) | M2.5 | 120s | 1 | 2x |
| Madrugada Insight (02h) | M2.5 | 180s | 1 | 2x |

### 🟡 P1 — Importante (escrita condicionada)

| Tarefa | Modelo | Timeout | Gatilho |
|--------|--------|---------|---------|
| Contratos Pendentes (11h) | Lightning | 60s | Sempre (dias úteis) |
| Monitor tl;dv | Lightning | 90s | Se email novo detectado |
| Livro check (18h) | Lightning | 60s | Sempre (dias úteis) |
| MiniMax Health (09h) | Lightning | 60s | Sempre (dias úteis) |
| Briefing Dominical (14h) | M2.5 | 240s | Domingo |

### 🟢 P2 — Background (sem custo imediato)

| Tarefa | Modelo | Timeout | Frequência |
|--------|--------|---------|------------|
| Backup | N/A (shell) | 30s | Diário 05:00 UTC |
| Email Digest | N/A (script) | 60s | Sob demanda |

---

## 4. Budget por Tipo de Tarefa

### Estimativa Mensal

| Categoria | Execuções/mês | Tokens/exec | Custo estim. |
|-----------|---------------|-------------|--------------|
| **P0 (crítico)** | ~50 | 15k | $0.45 × 50 = **$22.50** |
| **P1 (importante)** | ~100 | 5k | $0.10 × 100 = **$10.00** |
| **P2 (background)** | ~30 | 1k | $0.02 × 30 = **$0.60** |

**Total estimado:** ~$33/mês

### Alertas de Budget

| Threshold | Ação |
|-----------|------|
| 50% do budget | Alerta interno (log) |
| 75% do budget | Notificar Diego |
| 100% do budget | Desativar P1, manter só P0 |

---

## 5. Retry, Breaker e Filas

### Retry Policy

```python
RETRY_CONFIG = {
    "max_attempts": 3,
    "backoff_multiplier": 2,  # 1s → 2s → 4s
    "max_backoff": 30,        # max 30s
    "retry_on": ["rate_limit", "timeout", "500", "502", "503"]
}
```

### Circuit Breaker

| Estado | Condição | Ação |
|--------|----------|------|
| **CLOSED** | Normal | Requisições normais |
| **OPEN** | 3 falhas consecutivas | Bloquear por 5 min |
| **HALF-OPEN** | After 5 min | 1 requisição teste |

### Timeout por Tipo

| Tipo | Timeout | Rationale |
|------|---------|-----------|
| Lightning | 60s | Processamento leve |
| M2.5 padrão | 120s | Análise moderada |
| Briefing/Complexo | 180-240s | Processamento heavy |

---

## 6. Rate Limit Handling

### MiniMax
- **Limite:** ~60 req/min (informado)
- **Estratégia:** 
  - 1 requisição por vez (sem paralelismo)
  - Se 429 → backoff 60s + pausar cron por 4h

### Groq (Fallback)
- **Limite:** ~30 req/min
- **Estratégia:** Única opção se MiniMax indisponível

---

## 7. Lista de Crons Ativos

| ID | Nome | Tipo | Modelo | Janela |
|----|------|------|--------|--------|
| 696a5c6b | Check Pós-Reunião | 30min | M2.5 | 9-20h |
| b534ff47 | Madrugada Insight | 2h | M2.5 | 02:00 |
| 19741391 | Daily Briefing | 1x | M2.5 | 08:45 |
| 0f03c740 | MiniMax Health | 1x | Lightning | 09:00 |
| 3a6caf28 | Contratos | 1x | Lightning | 11:00 |
| ab458393 | Revisão Semanal | 1x | M2.5 | 16:00 sex |
| 7e712ad8 | Livro | 1x | Lightning | 18:00 |
| e309b1a4 | tl;dv Monitor | 2h | Lightning | 10-18h |

---

## 8. Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│  DECISÃO RÁPIDA                                          │
├─────────────────────────────────────────────────────────────┤
│  •Task pesada?      → M2.5 (180s timeout)                 │
│  •Task leve?        → Lightning (60s timeout)              │
│  •Rate limit 429?   → Backoff 60s + Groq fallback          │
│  •3 falhas seguidas → Circuit breaker (5min pause)        │
│  •Budget >75%?      → Alert Diego, desativar P1            │
└─────────────────────────────────────────────────────────────┘
```

---

*Documento vivo — atualizar conformeusage real*
