# 05_INFRA_AGENTE.md — Auditoria Estrutural

> **Etapa:** 5/6 — Infraestrutura do Agente
> **Data:** 2026-03-08
> **Base:** 01_inventario_sistema.md + 02_governanca_workstreams.md + 03_operacao_externa.md + 04_interface_time.md

---

## 1. MAPA DA INFRAESTRUTURA DO AGENTE

### 1.1 Camadas de Memória

| Camada | Arquivo / Mecanismo | Função | Status |
|--------|---------------------|--------|--------|
| **Contexto de sessão** | Transcript OpenClaw | Contexto imediato | ✅ Automático |
| **Memória de curto prazo** | memory/daily/*.md | Notas brutas por sessão | ✅ 8 arquivos |
| **Memória operacional** | memory/pending.md | Pendências abertas | ✅ Ativo |
| **Memória de projetos** | memory/projects.md | Status de projetos | ✅ Ativo |
| **Memória de aprendizado** | memory/lessons.md | Aprendizados | ✅ Ativo |
| **Memória de pessoas** | memory/people.md | Diretório | ✅ Ativo |
| **Memória de papéis** | memory/roles.md | Papéis e permissões | ✅ Ativo |
| **Busca semântica** | Gemini gemini-embedding-001 | Recuperação por similaridade | ✅ Ativo |
| **Consolidação estratégica** | memory_harvester.txt | Consolidação semanal | ⚠️ Ativo, sem execução comprovada |

### 1.2 Automações (Crons Ativos)

Total de crons: **30 ativos**

| Categoria | Crons | Frequência | Status |
|-----------|-------|-----------|--------|
| **Pessoal/Saúde** | 3 (Trinks, Personal Care, Livro) | Dom 08h / Dom 14h / Seg-Sex 18h | ✅ Ativo |
| **Praças/Sprint** | 6 | 2x/sem + Mon + Tue + Wed + Thu | ✅ Ativo |
| **Email/Tl;dv** | 5 | Cada 2h (9h-18h) | ✅ Ativo |
| **MiniMax Health** | 4 | 04h, 06h, 09h diário | ✅ Ativo |
| **Briefings** | 4 (Daily, Dominical 13h/14h, Semanal) | Seg-Sex + Dom | ✅ Ativo |
| **Governança** | 4 (Watchdog, Contratos, Auditoria pending, Madrugada) | Diário/Semanal | ⚠️ 2 com erros |
| **Backup** | 1 | Diário 05h UTC | ✅ Ativo |
| **Memória** | 2 (Harvester Dom 09h, Madrugada Seg-Sáb 02h) | Semanal/Diário | ✅ Ativo |
| **Diagnóstico** | 1 (Lembrete Tom de Voz) | One-shot | ⚠️ Erro em 10/03 |

### 1.3 Prompts Persistidos

| Arquivo | Função | Vinculado a cron? |
|---------|--------|------------------|
| memory_harvester.txt | Consolidação semântica de memória | ✅ Dom 09h |
| pracas_pulse_2xweek.txt | Pulse de praças | ✅ Ter+Sex 09h |
| pracas_sprint_check_mon.txt | Check segunda | ✅ Seg 18:15 |
| pracas_sprint_check_tue_10.txt | Check terça | ✅ Ter 10h |
| pracas_sprint_checkin_2xweek.txt | Check-in Qua+Sex | ✅ Qua/Sex 09h |
| pracas_sprint_email_watcher.txt | Monitor e-mail | ✅ Watcher |
| pracas_sprint_on_receive.txt | On receive | ⚠️ Manual (Diego cola) |
| pracas_sprint_reminder_thu.txt | Lembrete qui | ✅ Qui 09:30 |
| praças_weekly_scan.txt | Scan semanal | ✅ Seg 08:30 |
| sprint_checkpoint.txt | Checkpoint | ⚠️ Não linkado a cron ativo |
| sprint_facilitator.txt | Facilitador | ⚠️ Não linkado a cron ativo |
| sprint_followup_tracker.txt | Follow-up | ⚠️ Não linkado a cron ativo |
| sprint_reminder.txt | Reminder | ⚠️ Não linkado a cron ativo |
| pracas_tldv_socio_detector.txt | Detector tl;dv | ✅ Watcher |

---

## 2. CAPACIDADES REAIS

### 2.1 O agente é proativo?

**Resposta: SIM, mas seletivamente.**

| Proatividade | Evidência | Contexto |
|--------------|-----------|---------|
| ✅ **Alertas de praças** | 6 crons enviam alertas | Quando one-pager chega ou sprint está atrasado |
| ✅ **Briefings diários** | Cron Seg-Sex 08:45 | Agenda + pendências + OKRs |
| ✅ **Auditoria pending** | Cron Sex 17h | Verifica e classifica pendências |
| ✅ **Monitor email** | 5x/dia (9h-18h) | Triagem de e-mails importantes |
| ✅ **Monitor tl;dv** | 2h (10h-18h) | Processa reuniões |
| ❌ **Alertas de WS** | Nenhum | Sem cron para governança de WS |
| ❌ **Alertas de touch** | Nenhum | Days Since Touch nunca calculado |
| ❌ **Alertas de cadência WS** | Nenhum | Sem verificação de 14 dias |

**Veredicto:** Proativo para praças e operação pessoal. **Inativo para governança de WS.**

### 2.2 Registra aprendizado?

**Resposta: SIM, estruturalmente. Mas raramente em prática.**

| Capacidade | Evidência |
|-----------|-----------|
| ✅ memory/lessons.md | Estrutura ativa com 6+ aprendizados registrados |
| ✅ memory/daily/*.md | Notas por sessão (8 arquivos) |
| ✅ memory_harvester | Dom 09h consolida memória |
| ❌ Pulse WS | Pulses vazios — sem loop de aprendizado |
| ❌ Erro/ajuste WS | Sem evidência de erro+ajuste por WS |

**Veredicto:** Registra aprendizados estratégicos (lições) mas **não registra aprendizados operacionais dos WS** (erro/ajuste por ciclo).

### 2.3 Detecta lacunas?

**Resposta: PARCIALMENTE.**

| Capacidade | Evidência |
|-----------|-----------|
| ✅ Pendências sem dono/prazo | HEARTBEAT.md — checagem 3 e 10 |
| ✅ Auditoria pending (Sex 17h) | Cron ativo |
| ✅ Watch de erros de cron (07h) | Cron ativo |
| ❌ WS sem touch | Sem cron para verificar days_since_touch |
| ❌ WS sem pulse | Sem cron de verificação |
| ❌ Kickoffs não executados | Sem alerta |

**Veredicto:** Detecta lacunas operacionais (pending, emails) mas **não detecta lacunas de governança de WS**.

### 2.4 Acompanha evolução dos WS?

**Resposta: NÃO.**

| Capacidade | Evidência |
|-----------|-----------|
| ❌ Tracking de touch | days_since_touch = [PREENCHER] em todos WS |
| ❌ Cron de evolução WS | Nenhum cron verifica WS |
| ❌ Pulse automatizado | Sem geração de pulse |
| ❌ Dashboard de WS | Não existe |

**Veredicto: O agente não monitora a evolução dos WS. Zero.**

### 2.5 Ajuda melhoria contínua?

**Resposta: PARA OPERAÇÃO PESSOAL SIM; PARA WS NÃO.**

| Capacidade | Evidência |
|-----------|-----------|
| ✅ Madrugada (02h) | Processa insights das últimas 24h |
| ✅ Harvester (Dom 09h) | Consolida memória estratégica |
| ✅ Revisão semanal (Sex 16h) | Análise e planejamento |
| ❌ Loop de aprendizado WS | Sem execução de erro/ajuste |
| ❌ Melhoria de playbooks | Sem mecanismo |

**Veredicto:** Melhoria contínua existe para Diego pessoalmente. **Inexistente para WS.**

---

## 3. LIMITAÇÕES REAIS

### 3.1 Limitação: Sem Memória de Estado dos WS

| Problema | Evidência |
|----------|-----------|
| touch tracking vazio | 7/7 WS com [PREENCHER] |
| Pulses vazios | 7/7 WS sem dados |
| Sem estado de sprint | projects_orulo.md com defaults |
| Sem cron de check WS | Nenhum |

**Impacto:** O agente não sabe o estado real dos WS. Cada sessão começa do zero para governança.

### 3.2 Limitação: Agente Como Gargalo

| Problema | Evidência |
|----------|-----------|
| 10+ crons alertam Diego | Tudo passa pelo agente |
| Rascunhos dependem de OK | Policy de Nível 0 |
| Nada acontece sem Diego | Autonomia = 0 |
| One-pager: Diego cola | Manual always |

**Impacto:** O agente centraliza as operações em vez de descentralizá-las.

### 3.3 Limitação: Contexto de Sessão

| Problema | Evidência |
|----------|-----------|
| Memória de sessão zerada | Cada sessão inicia do zero |
| Depende de memory/ | Apenas o que está nos arquivos |
| Prompts truncados | Daily Briefing: "..." truncado no payload |
| Arquivos não lidos | Sem cron que garante leitura de todos |

**Impacto:** Risco de lacuna entre o que está documentado e o que está na sessão.

---

## 4. SOBRECARGAS

### 4.1 Sobrecarga de Funções

| Função | Evidência |
|--------|-----------|
| Chief of Staff | SOUL.md, AGENTS.md |
| PMO de 7 WS | governance/workstreams.md |
| Governança de Praças | pracas_sprint.md |
| Monitor de Email | 5 crons |
| Monitor tl;dv | 5 scripts |
| Gestor de Saúde Técnica | MiniMax health + diagnóstico |
| Cuidados Pessoais | Trinks, personal_care |
| Projeto Livro | Cron diário |
| Backup | Diário |
| Harvester de Memória | Semanal |
| Secretária Executiva (suporte a Lara) | AGENTS.md |

**Total:** 11 funções distintas para um único agente.

### 4.2 Sobrecarga de Crons

| Dimensão | Dado |
|----------|------|
| Total de crons | 30 |
| Crons com erros | 3 (Watchdog, Briefing Dom, Email Qui) |
| Sessões diferentes | 4 (main, morfeu, claudinei, larissa) |
| Crons que alertam Diego | ~15 |

**Veredicto:** 30 crons em 4 sessões diferentes é complexidade alta para um único operador (Diego).

### 4.3 Sobrecarga Cognitiva (Diego)

| Fonte | Alertas por semana |
|-------|-------------------|
| Praças (check-in Qua+Sex) | 2 |
| Praças (pulse Ter+Sex) | 2 |
| Daily Briefing (Seg-Sex) | 5 |
| Revisão Semanal | 1 |
| Email Monitor (9h-18h 5 dias) | até 25 |
| tl;dv (2h 10-18h 5 dias) | até 25 |
| Contratos (Seg-Sex 11:20) | 5 |
| MiniMax + Watchdog | ~3 |
| Livro (Seg-Sex 18h) | 5 |
| Madrugada (insights) | 6 |

**Total estimado:** ~80+ alertas/notificações por semana para Diego.

---

## 5. LACUNAS

### 5.1 LACUNAS DE GOVERNANÇA (Críticas)

| Lacuna | Impacto |
|--------|---------|
| **Sem cron de tracking WS** | O agente nunca sabe o estado dos 7 WS |
| **Sem alerta de days_since_touch** | Nenhum WS é cobrado por cadência |
| **Sem pulse automatizado** | Memória de WS nunca construída |
| **projects_orulo.md incompleto** | Dados de sprint não existem |

### 5.2 LACUNAS DE MEMÓRIA

| Lacuna | Impacto |
|--------|---------|
| **memory/feedback/ não existe** | Referenciado mas ausente |
| **Loop de aprendizado WS ausente** | Sem erro+ajuste por ciclo |
| **Estado de WS não persistido** | Sessão inicia sem contexto de WS |

### 5.3 LACUNAS DE AUTOMAÇÃO

| Lacuna | Impacto |
|--------|---------|
| **4 prompts não linkados a crons** | Artefatos mortos |
| **One-pager receive manual** | Dependência de Diego |
| **WS tracking manual** | Sem cron |

---

## 6. INSUMOS PARA ETAPA 6

### 6.1 Questão Central para Etapa 6

Com base em todos os achados das Etapas 1–5, a Etapa 6 (Arquitetura Recomendada) deve responder:

> **O agente único atual consegue sustentar os 7 WS + praças + operação pessoal + memória + melhoria contínua? Ou é necessário separar funções?**

### 6.2 Fatos para a Decisão

| Fato | Dado |
|------|------|
| 11 funções distintas | 1 agente |
| 30 crons | 4 sessões |
| 7 WS sem tracking | 0 crons de WS |
| Praças com 6 crons | Operação funcional |
| Diego = sponsor 7/7 + 80 alertas/semana | Sobrecarga |
| Time sem ferramenta | Dependência absoluta |

### 6.3 Cenários a Avaliar (Etapa 6)

1. **Manter agente único:** Tudo em Morfeu. Simplificação vs. sobrecarga.
2. **Criar agente PMO:** Separar governança de WS em agente dedicado.
3. **Bot + Agente:** Bot Telegram operacional + Morfeu estratégico.
4. **Separar depois:** Consolidar o que existe antes de separar.

---

## 7. ACHADOS PRINCIPAIS (Etapa 5)

### ✅ Capacidades Reais

- Proativo para praças (6 crons funcionando)
- Monitor de email e tl;dv (10 crons)
- Daily briefing e revisão semanal (entregues)
- Memória estruturada (lessons, pending, projects, daily)
- Harvester de memória (Dom 09h)
- Auditoria de pending (Sex 17h)
- Busca semântica (Gemini embedding)

### ❌ Capacidades Ausentes

- Tracking de evolução dos 7 WS (zero)
- Alerta de days_since_touch (zero)
- Pulse automatizado (zero)
- Loop de aprendizado por WS (zero)
- Estado persistido de WS (zero)

### ⚠️ Riscos

- **Sobrecarga de funções:** 11 funções no mesmo agente
- **Diego como gargalo:** 80+ alertas/semana + sponsor de tudo
- **Memória de WS = zero:** Cada sessão inicia sem estado
- **3 crons com erros:** Watchdog, Briefing Dom, Email Qui
- **4 prompts orphaned:** sprint_checkpoint, facilitator, followup_tracker, reminder

### 📊 Classificação das Capacidades

| Capacidade | Status |
|------------|--------|
| Proatividade para praças | ✅ Funciona |
| Proatividade para WS | ❌ Não existe |
| Registro de aprendizado pessoal | ✅ Funciona |
| Registro de aprendizado WS | ❌ Não existe |
| Detecção de lacunas operacionais | ✅ Parcial |
| Detecção de lacunas de governança WS | ❌ Não existe |
| Auditoria recorrente | ✅ Parcial (pending, email, tl;dv) |
| Auditoria de WS | ❌ Não existe |
| Melhoria contínua operacional | ✅ Madrugada + Harvester |
| Melhoria contínua WS | ❌ Não existe |

**Veredicto geral:** O agente sustenta bem a **operação pessoal e de praças**. Não sustenta a **governança estratégica dos 7 WS**.

---

*Fim da Etapa 5. Próxima: Etapa 6 — Avaliação de Arquitetura Futura.*
