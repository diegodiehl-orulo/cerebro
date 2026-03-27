# sistema/llm_policy.md — Política de Uso de LLMs

> **Versão:** v2.1
> **Definida em:** 2026-02-28
> **Princípio central:** Claude carrega o peso. Codex é backup de emergência conversacional. Crons param se Claude travar — sem Codex em automações.

---

## Stack de Modelos Ativos

| Modelo | Alias | Provider | Auth | Papel |
|--------|-------|----------|------|-------|
| `anthropic/claude-sonnet-4-6` | `sonnet` | Anthropic (API key) | ✅ | Principal — conversas e crons estratégicos |
| `anthropic/claude-haiku-3-5` | `haiku` | Anthropic (API key) | ✅ | Operacional — crons simples e heartbeat |
| `openai-codex/gpt-5.3-codex-spark` | `codex` | OpenAI (OAuth Plus) | ✅ | Fallback conversacional — só se Claude travar |

---

## Lógica de Fallback

```
Conversa com Diego
    → Sonnet (sempre tenta primeiro)
        ✅ OK → responde normalmente
        ❌ Rate limit → Codex Spark assume automaticamente
            → Diego é notificado: "Claude travou. Operando via Codex."

Cron automático
    → Sonnet ou Haiku (conforme job)
        ✅ OK → executa normalmente
        ❌ Rate limit → encerra silenciosamente
        → Codex NUNCA é usado em crons
```

---

## Classificação de Tarefas

| Nível | Tipo | Modelo |
|-------|------|--------|
| 1 | Estratégica / Arquitetural | **Sonnet** |
| 2 | Técnica Estrutural (código, infra, config, segurança) | **Sonnet** |
| 3 | Analítica Complexa (planejamento, trade-offs, decisões) | **Sonnet** |
| 4 | Operacional Estruturada (briefings, resumos com síntese) | **Sonnet** |
| 5 | Operacional Simples (formatação, extração, monitoramento) | **Haiku** |
| 6 | Fallback conversacional quando Claude indisponível | **Codex Spark** |

**Regra de desempate:** Na dúvida entre Haiku e Sonnet → Sonnet.

---

## Crons — Configuração Atual

| Cron | Modelo | Se travar |
|------|--------|-----------|
| Monitor tl;dv | **Sonnet** | Encerra silenciosamente |
| Daily Briefing | **Sonnet** | Encerra silenciosamente |
| Revisão Semanal | **Sonnet** | Encerra silenciosamente |
| Digest de Emails | **Haiku** | Encerra silenciosamente |
| Lembretes (at) | **Haiku** | Encerra silenciosamente |
| Heartbeat | **Haiku** | Encerra silenciosamente |

---

## Limites de Segurança do Codex

- ✅ Fallback automático apenas para conversas manuais com Diego
- ✅ Máximo 3-5 sessões/dia em modo fallback (uso conservador)
- ❌ Nunca ativado por crons ou automações
- ❌ Nunca para dados sensíveis da Órulo via OpenAI
- ❌ Nunca como modelo primário

**Motivo:** Conta OpenAI de Diego contém documentos importantes. OAuth via Plus pode violar ToS da OpenAI se usado em automações. Uso manual esporádico = risco baixo.

---

## Regras de Implementação

1. Ao criar novo cron: classificar primeiro, definir modelo antes de salvar.
2. Config, arquitetura e segurança: Sonnet sem exceção.
3. Não aplicar Haiku em tarefas que envolvam síntese, planejamento ou decisão.
4. Classificação feita no design do job — sem escalação automática em runtime.
5. Relatório de modelo: apenas quando Diego solicitar.
