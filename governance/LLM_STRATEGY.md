# LLM STRATEGY — Diego Diehl / Morfeu
**Atualizado:** 2026-04-08
**Versão:** v1.0

---

## Hierarquia de Uso (Hard Rule)

| Prioridade | Modelo | Quando usar | Fallback |
|---|---|---|---|
| **1 — DEFAULT** | `minimax/MiniMax-M2.7` | Todas as tarefas: chat, rotinas, crons, análises | groq |
| **2 — FALLBACK 1** | `groq/llama-3.3-70b-versatile` | Se MiniMax falhar (timeout, rate limit, erro) | haiku (sob demanda) |
| **3 — FALLBACK 2** | `anthropic/claude-haiku-3-5` | **SOMENTE** se MiniMax E Groq falharem — e APENAS para tarefas simples | nenhum |
| **4 — SOB DEMANDA** | `anthropic/claude-sonnet-4-6` ou `claude-opus-4-5-20251120` | **NUNCA automático.** Apenas quando Diego pedir explicitamente por "Claude" ou "Opus" | — |

---

## Regras de Ouro

1. **MiniMax é o default para TUDO.** Todas as tarefas — chat, crons, rotinas, análises, relatórios.
2. **Groq é o fallback automático #1.** Rate limit ou timeout do MiniMax → groq assume.
3. **Haiku é fallback de último recurso.** Não deve aparecer emChain de erro — o cron job deve falhar antes de chegar nele.
4. **Opus/Sonnet = sob demanda explícita.** Se Diego não pedir por nome, NÃO использовать. Nunca como fallback automático.
5. **Sem instruções redundantes nos prompts.** Não escrever "execute SOMENTE com MiniMax" — é o default.

---

## Stack Atual (OpenClaw)

```
Primary:   minimax/MiniMax-M2.7     (1M context, default)
Fallback:  groq/llama-3.3-70b-versatile (128k context, backup)
Fallback:  anthropic/claude-haiku-3-5 (last resort)
```

---

## Anti-patterns (Nunca fazer)

- ❌ Colocar `anthropic/claude-opus` como fallback automático
- ❌ Usar Haiku como fallback rotineiro — é para situação crítica
- ❌ Escrever "use apenas MiniMax" nos prompts — é o default
- ❌ Deixar cron rodando em agent diferente de `cron-mini`
- ❌ Manter `cron-haiku` ativo — está desativado

---

## Documentação Relacionada

- `performance/MODEL_GUIDE.md` — calibração e benchmarks
- `governance/SUBAGENT_CONTRACT.md` — contrato de subagentes
