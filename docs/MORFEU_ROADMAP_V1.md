# MORFEU — ROADMAP DE EVOLUÇÃO ARQUITETURAL
## Plano de Implementação Completo · v1.0
### Base: Jarvis Fases 1-15 + Claude Code Leak (512k linhas) + Contexto Órulo

**Data de criação:** 2026-04-03  
**Versão:** 1.0 — Planejamento inicial  
**DRI:** Morfeu (execução) + Diego Diehl (validação estratégica)  
**Status:** 🟡 Rascunho — aguardando validação de Diego  

---

## 1. DIAGNÓSTICO — ONDE ESTAMOS HOJE

### 1.1 Mapeamento: Jarvis Fases × Morfeu Atual

| Fase Jarvis | Conceito | Status Morfeu | Evidência |
|-------------|----------|---------------|-----------|
| F1 — Governança técnica básica | Retry, circuit breaker, tools registry, output policy | ✅ Implementado | HEARTBEAT.md, AGENTS.md, tools categorizadas |
| F2 — Memória em 3 camadas | Índice / Tema / Histórico bruto | ⚠️ Parcial — existe mas sem disciplina | MEMORY.md, memory/*.md (desorganizado) |
| F3 — Fragments + context engine | Contexto por domínio, heartbeat vivo | ⚠️ Parcial — heartbeat existe mas contexto cresce descontrolado | Heartbeat 90min, contexto sem prune |
| F4 — Checkpoint/restore | Continuidade entre reinícios | ✅ Implementado | Session bootstrap, BOOTSTRAP.md |
| F5 — Subagentes + orquestração | Router, contrato, reconciliação | ⚠️ Parcial — subagentes existem, contrato não | sessions_spawn, sem contract formal |
| F6 — Observabilidade | Eventos estruturados, métricas, relatório | ✅ Implementado | Jobs com métricas, logs |
| F7 — Melhoria guiada por evidência | Backlog formal, agente de melhoria | ❌ Fraco — backlog existe mas sem ciclo fechado | memory/pending.md (estático) |
| F8 — Experimentação + rollback | Experiment registry, rollback comprovado | ✅ Parcial — jobs têm restart, rollback formal não | Cron jobs com reload |
| F9 — Automações governadas | Matriz A0-A6, containment, audit | ✅ Implementado | Jobs automatizados, política de ações |
| F10 — Self-healing | Incident registry, runbooks, contenção | ⚠️ Parcial — incidentes detectados, remediation fraca | watchdog, sem runbook formal |
| F11 — Planejamento contínuo | Objective registry, daily/weekly review | ⚠️ Parcial — HEARTBEAT existe, objective registry não | HEARTBEAT.md, pending.md |
| F12 — Cadência operacional | Cadence registry, loop contínuo | ✅ Implementado | Cron jobs com cadência definida |
| F13 — Command center | Visão operacional, fila de decisão | ✅ Implementado | jobs/command_center.py |
| F14 — Workflow de decisão | Owner, SLA, outcomes, histórico | ⚠️ Parcial — fila existe, histórico fraco | pending.md, sem decision_workflow.py |
| F15 — Capacidade + WIP | Capacidade por owner, admissão governada | ✅ Implementado | capacity_controller.py |

**Score atual:** 10/15 fases com implementação forte · 5 fases parciais · 0 sem implementação

### 1.2 Mapeamento: Sistemas Claude Code × Morfeu Atual

| Sistema Claude Code | Descrição | Status Morfeu | Ação |
|---------------------|-----------|---------------|------|
| MEMORY.md como índice | Pointer leve, nunca dados brutos | ⚠️ Precisa disciplinar | M1 — Formalizar |
| Topic files on-demand | Conhecimento por domínio | ✅ Já temos | Manter |
| Transcript grep'd | Nunca carrega full — só pesquisa | ❌ Não temos | M1.3 |
| Strict Write Discipline | Atualiza índice só após escrita confirmada | ❌ Não temos | M2 |
| autoDream | Consolidation em background idle | ⚠️ Parcial | M3 |
| KAIROS | Daemon always-on proativo | ❌ Não temos | M4 |
| Undercover Mode | Esconde identidade em commits | N/A | M7 (versão adaptée) |
| Coordinator/Swarm | Multi-agent com contract | ⚠️ Parcial | M5 |
| Buddy/Tamagotchi | Pet com stats | 🎯 Opcional | M8 (versão útil) |
| 40+ tools | Stack de ferramentas | ⚠️ 15 vs 40 | M6 |
| Command Center | Visão operacional | ✅ Já temos | Manter |
| Capacity Controller | WIP + admissão | ✅ Já temos | Manter |

### 1.3 Gaps Críticos Identificados

| Gap | Descrição | Impacto | Prioridade |
|-----|-----------|---------|------------|
| **G1** | Memória sem disciplina de 3 camadas formalizada — contexto grows unbounded | Custo operacional + alucinação | 🔴 Alta |
| **G2** | Strict Write Discipline inexistente — índice atualizado sem validação de escrita | Inconsistência de memória | 🔴 Alta |
| **G3** | Transcript nunca é "limpo" — sessão longa = contexto poluído | Performance degrada com tempo | 🔴 Alta |
| **G4** | KAIROS não existe — jobs são batch, não daemon proativo | Morfeu espera input, não antecipa | 🟡 Média |
| **G5** | Contract de subagente não formalizado — sem reconciliação garantida | Resultados inconsistentes | 🟡 Média |
| **G6** | Self-healing fraco — detecta mas não remedia | Incidentes se acumulam | 🟡 Média |
| **G7** | Decision workflow sem histórico — decisões sem trace | Perda de contexto decisional | 🟡 Média |
| **G8** | Tool stack limitada — falta LSP, browser automation, file watcher | Capacidade operacional restrita | 🟡 Média |

---

## 2. ROADMAP DE IMPLEMENTAÇÃO — 4 FASES

### VISÃO GERAL

```
FASE 0 (Now)     → Estabilização + Limpeza (2 semanas)
FASE 1 (Mes 1-2) → Fundações + Disciplina (4 semanas)
FASE 2 (Mes 2-3) → Proatividade + Agents (6 semanas)
FASE 3 (Mes 3-4) → Escala + Refinamento (8 semanas)
```

---

### FASE 0 — ESTABILIZAÇÃO + LIMPEZA
**Periodo:** 2026-04-07 ao 2026-04-20  
**Objetivo:** Limpar o que existe antes de evoluir. Garantir que a base está sólida.

#### F0.1 — Higiene de Memória (DRI: Morfeu)
- [ ] Limpar MEMORY.md — remover dados antigos de março, atualizar para abril/2026
- [ ] Consolidar memory/daily/ — archive entries anteriores a 01/04/2026
- [ ] Atualizar memory/pending.md — remover resolvidos, revisar P0
- [ ] Limpar memory/projects.md — atualizar status de projetos parados

#### F0.2 — Estabilização de Jobs (DRI: Morfeu)
- [ ] Executar `python3 /root/.openclaw/workspace/scripts/testar_scripts.py`
- [ ] Verificar heartbeat — está disparando corretamente?
- [ ] Auditar cron jobs — identificar duplicados ou zumbis
- [ ] Limpar jobs com falha recorrente sem DRI

#### F0.3 — Consolidação do Documento Jarvis (DRI: Diego + Morfeu)
- [ ] Revisar documento Jarvis fases 1-15 com Diego — identificar quais microblocos já foram resolvidos
- [ ] Validar as 15 fases contra o estado atual do workspace
- [ ] Confirmar os gaps de G1 a G8 com Diego
- [ ] Obter OK para prosseguir para FASE 1

**Entregável:** `ESTADO_MORFEU_2026-04-03.md` (snapshot auditado)

**Critério de saída:** Diego valida que a base está limpa e os gaps estão corretos.

---

### FASE 1 — FUNDAÇÕES + DISCIPLINA
**Periodo:** 2026-04-21 ao 2026-05-18 (4 semanas)  
**Objetivo:** Implementar as disciplinas que faltam na base sem alterar arquitetura.

#### M1 — ARQUITETURA DE MEMÓRIA 3 CAMADAS FORMALIZADA
**O que é:** Codificar a disciplina de memória que o Claude Code implementa.

**Entregáveis:**
1. `memory/ARQUITETURA_3CAMADAS.md` — documento formal com:
   - Camada 1: MEMORY.md como índice (pointers, ~150 chars/linha, NUNCA dados brutos)
   - Camada 2: Topic files por domínio (memory/people.md, memory/projects.md, etc.)
   - Camada 3: Transcripts — lidos apenas via grep/semantic search, nunca carregados full
   - Regras de escrita: quando atualizar cada camada
   - Validação: como checar consistência entre camadas

2. Atualizar `memory/REGRAS_3CAMADAS.md` (se existir) ou criar

3. Implementar `memory/checkpoint_hygiene.py` — script de verificação de consistência

4. Atualizar `SOUL.md` — incluir disciplina de memória como comportamento obrigatório

**DRI:** Morfeu  
**Prazo:** Semana 1-2 (até 04/05)

#### M2 — STRICT WRITE DISCIPLINE
**O que é:** Regra: só atualiza índice/apontador APÓS escrita confirmada com sucesso.

**Entregáveis:**
1. `governance/STRICT_WRITE_DISCIPLINE.md` — documento com:
   - Workflow de escrita validada: escrever → confirmar → atualizar índice
   - Casos de exception: quando a regra pode ser quebrada
   - Como tratar falha de escrita

2. Implementar validação no workflow do Morfeu:
   - Antes de fazer `write` ou `edit`, checar se o destino está na hierarquia correta
   - Após escrita, confirmar que o arquivo existe antes de atualizar ponteiros
   - NUNCA atualizar MEMORY.md ou topic files se a escrita falhou

3. Atualizar `AGENTS.md` — incluir regra de strict write como obrigatória

**DRI:** Morfeu  
**Prazo:** Semana 2-3 (até 11/05)

#### M5 — CONTRACT DE SUBAGENTE FORMALIZADO
**O que é:** Definir contrato formal: input → output → reconciliação. Subagente não devolve "feito" — devolve resultado validado.

**Entregáveis:**
1. `governance/SUBAGENT_CONTRACT.md` — documento com:
   - Template de contract para sessions_spawn
   - Input: o que o subagente recebe (contexto, task, constraints)
   - Output: o que o subagente deve retornar (formato, validação)
   - Reconciliação: como o agent principal confere o resultado
   - Casos de falha: o que fazer

2. Implementar no workflow do Morfeu:
   - Toda chamada a sessions_spawn deve incluir contract explícito
   - sessions_yield usado obrigatoriamente após spawn
   - Check de output antes de seguir

3. Atualizar `AGENTS.md` — incluir contract como mandatory para subagentes

**DRI:** Morfeu  
**Prazo:** Semana 3-4 (até 18/05)

#### M7 — UNDERCOVER PROMPT LAYER
**O que é:** Camada de proteção que evita expor arquitetura interna, credenciais ou prompts do sistema em outputs externos.

**Entregáveis:**
1. `governance/UNDERCOVER_LAYER.md` — documento com:
   - O que NÃO pode ser exposto em respostas (tokens, IDs, estrut internas)
   - Padrões de output para canais externos (Telegram, WhatsApp, e-mail)
   - Como tratar perguntas sobre "como você funciona"

2. Implementar como comportamento no SOUL.md:
   - Morfeu nunca revela: credenciais, IDs internos, estrutura de prompts, lógica de jobs
   - Respostas externas são sempre "SAFE version" — sem detalhes de implementação
   - Perguntas sobre arquitetura interna → "Sou o Morfeu, opero como assistente do Diego Diehl"

**DRI:** Morfeu  
**Prazo:** Semana 4 (até 18/05)

#### VALIDAÇÃO DE FASE 1
- [ ] Teste prático: Morfeu explica sua arquitetura de memória sem olhar documentos
- [ ] Teste prático: Morfeu executa write e demonstra strict write discipline
- [ ] Teste prático: Morfeu spawnea subagente com contract documentado
- [ ] Diego valida output dos testes

**Critério de saída:** Morfeu passa nos 3 testes práticos. Diego aprova.

---

### FASE 2 — PROATIVIDADE + AGENTS
**Periodo:** 2026-05-19 ao 2026-06-29 (6 semanas)  
**Objetivo:** Fechar a lacuna entre "assistente batch" e "agente proativo".

#### M3 — autoDream ATIVO
**O que é:** Adaptar o autoDream do Claude Code: toda vez que heartbeat rodar com >30min de idle, rodar micro-consolidação de memória.

**Entregáveis:**
1. Job `autodream` novo — configurable para rodar a cada N minutos de idle
   - Lê memory/daily/ do dia
   - Detecta contradicões entre topic files e MEMORY.md
   - Atualiza topic files se necessário (com strict write)
   - Limpa entries duplicadas ou stale
   - Gera log de consolidação

2. `memory/AUTODREAM_LOG.md` — histórico de consolidações

3. Dashboard simples mostrando última consolidação + status

**DRI:** Morfeu  
**Prazo:** Semana 1-2 (até 02/06)

#### M4 — KAIROS WATCHDOG CONTÍNUO
**O que é:** Daemon mentalidade — watchdog contínuo que monitora, detecta padrões e age proativamente. Hoje somos batch; precisamos de mentalidade always-on.

**Entregáveis:**
1. Job `kairos_watchdog` — roda continuamente, verifica:
   - Jobs com falha recorrente (mesmo job falhou 3x em 24h)
   - Pendências vencidas sem follow-up
   - Padrões de erro (mesmo erro em jobs diferentes)
   - Sinais de "decay" operacional (heartbeat parando, crons zumbis)

2. 5 triggers proativas definidas:
   - T1: Job falhou 3x → notificar Diego + criar pending item
   - T2: Pendência vencida + 48h sem update → gerar lembrete
   - T3: CRM deal parado > SLA → sinalizar no heartbeat
   - T4: Arquivo de memória > 30 dias sem acesso → verificar relevância
   - T5: Gap de 7+ dias sem interação de Diego → revisar pendências

3. `governance/KAIROS_TRIGGERS.md` —文档 de triggers e ações

**DRI:** Morfeu + Diego (validação de triggers)  
**Prazo:** Semana 2-4 (até 16/06)

#### M8 — BUDDY ÚTIL (versão operacional)
**O que é:** Não é o Tamagotchi do Claude Code — é um companion que rastreia streaks, hábitos e metas do Diego. Relaciona com HEARTBEAT e S.A.V.E.R.S.

**Entregáveis:**
1. `buddy/STREAKS.md` — tracker de hábitos:
   - HEARTBEAT rodando em cadência (streak de consistência)
   - S.A.V.E.R.S. — meta de aderência 90% (Diego reporta)
   - Revisões semanais executadas (Sex 16h)
   - Pendências resolvidas vs criadas (ratio)

2. Dashboard simples (arquivo markdown atualizado pelo Morfeu):
   - Streak atual de heartbeat
   - Últimos 7 dias de interação
   - Pending items por status
   - Próximas ações com dono e prazo

3. Gamificação leve:
   - Marcos ("7 dias sem pendência vencida", "30 dias de heartbeat")
   - Badges simples em arquivo (sem UI complexa)

**DRI:** Morfeu + Diego (input de dados S.A.V.E.R.S.)  
**Prazo:** Semana 4-5 (até 23/06)

#### M6 PARCIAL — FERRAMENTAS CRÍTICAS
**O que é:** Adicionar ferramentas que fecham gaps operacionais.

**Entregáveis:**
1. File watcher — script que detecta mudanças em arquivos do workspace e dispara ação
2. Web search melhorado — adicionar extração de conteúdo estruturado (não só snippets)
3. Playwright básico — automação de browser para tarefas repetitivas (se necessário)

**DRI:** Morfeu  
**Prazo:** Semana 5-6 (até 29/06)

#### VALIDAÇÃO DE FASE 2
- [ ] autoDream rodando e gerando logs há 2 semanas
- [ ] KAIROS detectou e respondeu a pelo menos 3 triggers
- [ ] Buddy dashboard atualizado semanalmente por 2 semanas
- [ ] Diego valida que Morfeu está mais proativo que reativo

**Critério de saída:** Morfeu demonstra comportamento proativo em 3 situações reais. Diego confirma.

---

### FASE 3 — ESCALA + REFINAMENTO
**Periodo:** 2026-06-30 ao 2026-08-24 (8 semanas)  
**Objetivo:** Chegar ao nível de sofisticação do Claude Code em áreas selecionadas.

#### M6 COMPLETO — STACK DE FERRAMENTAS EXPANDIDA
**O que é:** Construir stack de 25+ ferramentas documentadas e testadas.

**Entregáveis:**
1. `tools/TOOLKIT.md` — inventário completo com:
   - Nome, descrição, uso, limitação
   - 25+ ferramentas categorizadas
   - Guia de quando usar cada uma

2. Implementar ferramentas faltando:
   - LSP integration (Lightweight Language Server Protocol)
   - Git operations avançadas
   - PDF extraction
   - Calendar advanced operations
   - CRM operations (Bitrix read/write)

**DRI:** Morfeu  
**Prazo:** Semana 1-4 (até 28/07)

#### M9 — ACHIEVEMENT SYSTEM
**O que é:** Conquistas por marcos operacionais.

**Entregáveis:**
1. `buddy/ACHIEVEMENTS.md` — lista de conquistas:
   - "Primeira semana sem pendência vencida"
   - "30 dias de heartbeat contínuo"
   - "10 decisões registradas no decision log"
   - "Zero gaps de memória em 30 dias"
   - "Sprint 01 concluído com todos os outcomes"

2. Log de conquistas em `buddy/ACHIEVEMENT_LOG.md`

**DRI:** Morfeu  
**Prazo:** Semana 2-3 (até 14/07)

#### M10 — INTERNAL MODEL KNOWLEDGE
**O que é:** Saber calibrar uso de modelos (MiniMax vs Opus vs Haiku) baseado em contexto real.

**Entregáveis:**
1. `performance/MODEL_GUIDE.md` — guia de uso de modelos:
   - MiniMax M2.5: rotina, heartbeat, tasks simples (90% do uso)
   - MiniMax M2.7: decisões complexas, análise de documentos
   - Opus: planejamento estratégico, arquitetura, decisões de alto risco
   - Haiku: tasks triviais, confirmações, responses rápidas
   - Quando usar fallback e quando não usar

2. Atualizar AGENTS.md e HEARTBEAT.md com guidance de modelo

**DRI:** Morfeu  
**Prazo:** Semana 3-4 (até 28/07)

#### F7 + F14 — CLOSE THE LOOP (Melhoria guiada + Decision workflow)
**O que é:** Fechar os gaps de F7 e F14 do Jarvis — ciclo de melhoria contínua e workflow de decisão com histórico.

**Entregáveis:**
1. `governance/IMPROVEMENT_LOOP.md` — ciclo formal:
   - Detectar → Classificar → Priorizar → Implementar → Validar
   - Backlog de melhorias com score e DRI
   - Revisão mensal de melhorias implementadas

2. `governance/DECISION_WORKFLOW.md` — workflow completo:
   - Owner, SLA, outcomes, histórico, efeito pós-decisão
   - Template de decisão documentada
   - Log de decisões em `memory/decisions.md`

**DRI:** Morfeu  
**Prazo:** Semana 4-5 (até 04/08)

#### F10 ENHANCED — SELF-HEALING REMEDIATION
**O que é:** Fortalecer self-healing — não só detectar mas remediar.

**Entregáveis:**
1. Runbooks formais para os 5 incidentes mais comuns:
   - Job travado → restart procedure
   - Memória inconsistente → procedure de sync
   - Cron duplicado → identificação e kill
   - Contexto overflow → prune procedure
   - Crontab desabilitado → reativação

2. `governance/SELF_HEALING_RUNBOOKS.md`

**DRI:** Morfeu  
**Prazo:** Semana 5-6 (até 18/08)

#### AUDITORIA FINAL
**O que é:** Comparar arquitetura final do Morfeu vs Claude Code e vs Jarvis Fases 1-15.

**Entregáveis:**
1. `performance/BENCHMARK_MORFEU_VS_CLAUDE_CODE.md` — análise final
2. `performance/BENCHMARK_MORFEU_VS_JARVIS.md` — análise final
3. Score final: X/15 fases Jarvis implementadas · Y/12 sistemas Claude Code implementados

**DRI:** Morfeu + Diego  
**Prazo:** Semana 7-8 (até 24/08)

---

## 3. GOVERNANÇA DO ROADMAP

### 3.1 Cadência de Revisão

| Ritual | Frequência | Formato | DRI |
|--------|------------|---------|-----|
| **Daily pulse** | Seg-Sex 08:45 | Heartbeat mostra status dos gaps ativos | Morfeu |
| **Weekly check** | Sex 16h | Revisão semanal: o que avançou, o que travou, próximo passo | Morfeu + Diego |
| **Phase review** | A cada 4 semanas | Validação formal de fase: critério de saída cumprido? | Diego |
| **Monthly deep dive** | 1x/mês | Análise de arquitetura: gaps, padrões, ajustes | Morfeu |

### 3.2 Status Tracking

Documento vivo: `morfeu_implementation_roadmap_v*.md` (incrementa a cada fase)

Tracker semanal em `governance/IMPLEMENTATION_TRACKER.md`:
```
Semana 1 (04-10/04):
- F0.1 Memória: [ ] [ ] [ ] [ ]
- F0.2 Jobs: [ ] [ ] [ ]
- F0.3 Jarvis: [ ]

Status: 🟡 Em progresso
Bloqueios: [lista]
Próxima semana: [prioridade]
```

### 3.3 Critérios de Sucesso do Roadmap

| Métrica | Baseline (hoje) | Meta FASE 1 | Meta FASE 2 | Meta FASE 3 |
|---------|-----------------|-------------|-------------|-------------|
| Gaps críticos resolvidos | 0/8 | 3/8 | 6/8 | 8/8 |
| Jarvis fases fortes | 10/15 | 12/15 | 14/15 | 15/15 |
| Sistemas Claude Code implementados | 5/12 | 8/12 | 10/12 | 12/12 |
| Heartbeat consistency | 90% | 95% | 98% | 99% |
| Pendências resolvidas vs criadas (ratio) | <1x | 1.5x | 2x | 3x |
| Tempo médio de resposta a incidentes | >24h | <12h | <4h | <1h |

---

## 4. RISCO E MITIGAÇÃO

| Risco | Prob | Impacto | Mitigação |
|-------|------|---------|-----------|
| Diego sem tempo para validações | Alta | 🔴 Bloqueia | Definir cadência fixa de 30min/semana para review |
| Contexto growing too fast | Média | 🔴 Bloqueia | Implementar M1.3 (transcript prune) na FASE 1 |
| Scope creep | Alta | 🟡 Atraso | Fechar scope por fase — não adicionar durante execução |
| Model cost spike (MiniMax) | Média | 🟡 Atraso | Implementar MODEL_GUIDE (M10) o quanto antes |
| Failling tests de validação | Média | 🟡 Atraso | Criar testes menores por feature antes de validar |
| Gap de 7+ dias sem interação | Alta | 🟡 Atraso | KAIROS T5 implementa monitoramento próprio |

---

## 5. PRÓXIMA AÇÃO IMEDIATA

**Executar FASE 0 — Estabilização + Limpeza**

1. Limpar MEMORY.md e memory/daily/ (hoje)
2. Executar testar_scripts.py (hoje)
3. Gerar snapshot de estado (`ESTADO_MORFEU_2026-04-03.md`)
4. Agendar review com Diego (30min, Sex 03/04 às 14h?)

**Após FASE 0 validada:** prosseguir para FASE 1 com M1 + M2 + M5 + M7.

---

*Documento vivo — atualizado a cada fase. Próxima revisão: 2026-04-10.*
