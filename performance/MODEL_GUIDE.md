# MODEL GUIDE — Calibração de Modelos
## M10 — Internal Model Knowledge (Sprint 5 FASE 3)

**Versão:** 1.0  
**Data:** 2026-04-03  
**DRI:** Morfeu  
**Status:** ✅ Ativo  

---

## PRINCÍPIO

> Modelo errado = custo desnecessário ou resposta fraca.
> MiniMax para rotina. Sonnet para análise. Opus apenas quando o risco justifica.

---

## GUIA DE MODELOS

### MiniMax M2.5 — `minimax` (90% do uso)
**Custo:** Baixo | **Velocidade:** Alta | **Qualidade:** Boa para tarefas estruturadas

✅ Usar para:
- Heartbeat diário e semanal
- Jobs cron (autoDream, KAIROS, daily briefing)
- Leitura e síntese de arquivos
- Cobranças e follow-ups simples
- Respostas a perguntas diretas com contexto disponível

❌ Não usar para:
- Análise estratégica complexa
- Documentos muito longos sem estrutura clara
- Decisões com alto risco operacional

---

### MiniMax M2.7 — `minimax-27` (análise intermediária)
**Custo:** Médio-baixo | **Velocidade:** Média | **Qualidade:** Alta para análise

✅ Usar para:
- Análise de documentos longos (charters, planilhas, reports)
- Decisões táticas dos workstreams
- Síntese de múltiplas fontes
- Rascunhos de comunicação importante

❌ Não usar para:
- Rotinas simples (desnecessário)
- Decisões estratégicas de alto risco (usar Opus)

---

### Claude Haiku — `haiku` (tarefas triviais)
**Custo:** Muito baixo | **Velocidade:** Muito alta

✅ Usar para:
- Confirmações simples ("OK para enviar?")
- Classificação rápida (sim/não)
- Formatação de dados simples
- Testes rápidos de prompt

❌ Não usar para:
- Análise de qualidade, raciocínio complexo, documentação

---

### Claude Sonnet — `sonnet` (qualidade de redação)
**Custo:** Médio | **Velocidade:** Média

✅ Usar para:
- E-mails e comunicações externas que exigem qualidade
- Redação de documentos formais
- Análise de código
- Quando M2.7 não está capturando nuances

❌ Não usar para:
- Rotinas, heartbeat, tasks simples

---

### Claude Opus — `opus` (decisões estratégicas)
**Custo:** Alto | **Velocidade:** Baixa

✅ Usar para:
- Planejamento estratégico (como hoje — Claude Code Leak + Jarvis)
- Arquitetura de novos sistemas
- Decisões de alto risco irreversível
- Revisão crítica de documentos de governança

❌ Usar só quando Diego solicita explicitamente ou quando o risco justifica

---

### Gemini Flash 2.5 — `flash-25` (pesquisa e multi-step)
**Custo:** Baixo | **Velocidade:** Alta | **Contexto:** 1M tokens

✅ Usar para:
- Pesquisa web multi-step
- Análise de documentos muito longos (>100k tokens)
- Tarefas com muito contexto

---

## FALLBACK

**Se modelo principal falhar (timeout/quota):**
1. MiniMax M2.5 falha → tentar MiniMax M2.7
2. MiniMax M2.7 falha → tentar Claude Haiku
3. Haiku falha → alertar Diego (não tentar Opus por custo)

**Regra anti-custo:** Nunca escalar para Opus automaticamente em fallback. Sempre perguntar Diego primeiro.

---

## QUOTA AWARENESS

- Jobs cron: sempre MiniMax M2.5 (custo mínimo)
- Timeout cron: máximo 90s (jobs simples), 180s (jobs complexos)
- Se quota MiniMax esgotada: notificar Diego + pausar jobs até recarregar
- Script de verificação: `python3 scripts/minimax_health.py`

---

## DECISÕES REGISTRADAS

| Data | Decisão |
|------|---------|
| 2026-04-03 | M2.5 como default para todos os crons. Opus apenas sob solicitação explícita. |
