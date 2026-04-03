# IMPROVEMENT LOOP
## F7 — Ciclo de Melhoria Guiada por Evidência (Sprint 4)

**Versão:** 1.0  
**Data:** 2026-04-03  
**DRI:** Morfeu  
**Base:** Jarvis Fase 7  
**Status:** ✅ Ativo  

---

## O PROBLEMA

Antes deste documento: melhorias surgiam de conversas ad-hoc, sem priorização formal, sem score, sem loop fechado. Resultado: boas ideias perdidas, melhorias sem validação, backlog informal.

Agora: ciclo formal com 5 etapas e backlog priorizado.

---

## O CICLO (5 ETAPAS)

```
DETECTAR → CLASSIFICAR → PRIORIZAR → IMPLEMENTAR → VALIDAR
    ↑                                                    |
    └────────────────── APRENDIZADO ←───────────────────┘
```

### Etapa 1 — DETECTAR
**Fontes de detecção:**
- Morfeu detecta padrão de erro repetido → cria item
- Diego reporta fricção ou necessidade → Morfeu registra
- autoDream detecta inconsistência → cria item
- KAIROS ativa trigger → cria item
- Heartbeat semanal identifica gap → cria item

**Ação:** Adicionar ao backlog de melhorias abaixo com status `🔵 Detectado`.

### Etapa 2 — CLASSIFICAR
**Dimensões de classificação:**
- **Tipo:** Governança | Memória | Job/Automação | UX | Integração | Segurança
- **Origem:** Morfeu | Diego | autoDream | KAIROS | Heartbeat
- **Urgência:** Crítico (bloqueia operação) | Alto | Médio | Baixo

### Etapa 3 — PRIORIZAR
**Score de prioridade (1-10):**
```
Score = (Impacto × 0.5) + (Urgência × 0.3) + (Facilidade × 0.2)
```
- Impacto: 1=mínimo, 10=transforma operação
- Urgência: 1=pode esperar, 10=bloqueia agora
- Facilidade: 1=semanas de trabalho, 10=30 minutos

**Teto de WIP:** Máximo 3 itens em andamento simultaneamente.

### Etapa 4 — IMPLEMENTAR
- Criar branch de implementação (para mudanças em arquivos de governança)
- Documentar o que vai mudar + por quê
- Implementar com Strict Write Discipline
- Testar: dry-run quando possível

### Etapa 5 — VALIDAR
**Critérios mínimos de conclusão:**
- [ ] Mudança implementada e confirmada (arquivo existe, tamanho > 0)
- [ ] Efeito mensurável descrito ("antes X, depois Y")
- [ ] MEMORY.md atualizado se for novo arquivo
- [ ] Item marcado como `✅ Validado` no backlog

---

## BACKLOG DE MELHORIAS

> Status: 🔵 Detectado | 🟡 Em análise | 🟠 Em implementação | ✅ Validado | ❌ Descartado

| # | Melhoria | Tipo | Score | Status | DRI | Prazo |
|---|----------|------|-------|--------|-----|-------|
| M01 | Arquitetura de Memória 3 Camadas | Memória | 9.5 | ✅ Validado | Morfeu | 03/04 |
| M02 | Strict Write Discipline | Governança | 9.0 | ✅ Validado | Morfeu | 03/04 |
| M03 | autoDream — consolidação semanal | Automação | 8.5 | ✅ Validado | Morfeu | 03/04 |
| M04 | KAIROS Watchdog — 5 triggers | Automação | 8.5 | ✅ Validado | Morfeu | 03/04 |
| M05 | Subagent Contract formalizado | Governança | 8.0 | ✅ Validado | Morfeu | 03/04 |
| M06 | Undercover Layer | Segurança | 7.5 | ✅ Validado | Morfeu | 03/04 |
| M07 | Self-Healing Runbooks (5 RBs) | Governança | 8.0 | ✅ Validado | Morfeu | 03/04 |
| M08 | Tool Stack Inventário (26 tools) | UX | 7.0 | ✅ Validado | Morfeu | 03/04 |
| M09 | Improvement Loop (este doc) | Governança | 7.5 | 🟠 Em implementação | Morfeu | 03/04 |
| M10 | Decision Workflow com trace | Governança | 7.5 | 🟠 Em implementação | Morfeu | 03/04 |
| M11 | G3 Transcript Pruning script | Memória | 8.0 | ✅ Validado | Morfeu | 03/04 |
| M12 | Tool stack G8 (LSP, Bitrix, watcher) | Integração | 6.5 | 🔵 Detectado | a definir | FASE 3 |
| M13 | Buddy/Streaks tracker | UX | 5.0 | 🔵 Detectado | a definir | FASE 3 |
| M14 | Model cost optimization (quota) | Automação | 6.0 | 🔵 Detectado | a definir | FASE 3 |

---

## REVISÃO MENSAL DO BACKLOG

**Frequência:** 1x/mês, junto com Revisão Mensal Executiva dos Workstreams

**Pauta:**
1. Itens validados no mês → comemorar + documentar aprendizado
2. Itens em andamento há >30 dias → avaliar bloqueio
3. Novos detectados → classificar e priorizar
4. Itens Detectado há >60 dias sem movimento → descartar ou replanejar

---

## APRENDIZADOS DO CICLO

> Registrar aqui o que foi aprendido após cada validação.

- **M01-M11 (03/04/2026):** Implementar em sprints curtos com aprovação de Diego a cada sprint é mais eficiente do que planejar tudo antes. Decisões estratégicas (Q1-Q9) em formato de pergunta direta aceleram execução.
