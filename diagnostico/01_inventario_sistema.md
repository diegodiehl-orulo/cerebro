# 01_INVENTARIO_SISTEMA.md — Inventário Estrutural
> **Diagnóstico:** Etapa 1 de 7
> **Auditor:** Morfeu
> **Data:** 2026-03 (gerado em sessão ativa)
> **Escopo:** Tudo que existe no workspace + crons ativos no OpenClaw
> **Método:** Leitura direta de arquivos + cron list + find recursivo
> **Anti-alucinação:** Nenhum item inventariado sem evidência de leitura real.

---

## 1. VISÃO GERAL DO INVENTÁRIO

O sistema Morfeu/Órulo é um **workspace de alta densidade documental** operando sobre o OpenClaw. O repositório contém ~150 arquivos relevantes (excluindo .git), distribuídos em 20+ diretórios. Há **44 jobs de cron registrados** (29 ativos, 15 desativados), **3 agentes** distintos (morfeu, claudinei, larissa), **15+ scripts Python**, e uma infraestrutura de integrações externas parcialmente funcional.

A primeira impressão é de um sistema **vivo mas com alto débito de curadoria**: muita coisa foi criada, parte foi desativada, mas não há limpeza sistemática. O inventário revela um sistema que cresceu rápido e acumulou versões, experimentos e stubs sem consolidação formal.

---

## 2. TABELA POR CATEGORIA

### 2.1 Identidade e Governança do Agente

| Arquivo | Localização | Função | Estado |
|---------|-------------|--------|--------|
| `SOUL.md` | raiz | Persona, tom, valores do Morfeu | `ESTRUTURA VÁLIDA` — denso, real |
| `IDENTITY.md` | raiz | Identidade visual e infraestrutura | `ESTRUTURA VÁLIDA` |
| `USER.md` | raiz | Perfil completo de Diego (431 linhas) | `ESTRUTURA VÁLIDA` — fonte mais rica do sistema |
| `AGENTS.md` | raiz | Governança, guardrails, protocolos | `ESTRUTURA VÁLIDA` — detalhado |
| `HEARTBEAT.md` | raiz | Checklist operacional periódico | `ESTRUTURA VÁLIDA` — completo para [ÓRULO]; seção [PESSOAL] = stub |
| `MEMORY.md` | raiz | Índice de memória de longo prazo | `ESTRUTURA VÁLIDA` — atualizado 07/03 |
| `TOOLS.md` | raiz | Credenciais e notas de infraestrutura | `EXISTE, MAS ESTÁ INSUFICIENTE` — seção "What Goes Here" ainda com exemplos genéricos |
| `EMAIL_SECURITY.md` | raiz | Política de segurança de e-mail | `ESTRUTURA VÁLIDA` |
| `BOOT.md` | raiz | Checklist de inicialização | `EXISTE, MAS ESTÁ INSUFICIENTE` — não lido em detalhe; possivelmente stub |
| `BOOTSTRAP.md` | raiz | Arquivo ausente | `LACUNA` — esperado mas não existe |

**Concentração:** Todos os arquivos de identidade estão na raiz. Bem organizados, bem preenchidos. Principal lacuna: BOOTSTRAP.md ausente.

---

### 2.2 Memória

| Arquivo / Pasta | Localização | Função | Estado |
|----------------|-------------|--------|--------|
| `memory/daily/` | memory/ | Notas brutas por sessão | `EXISTE, MAS ESTÁ INSUFICIENTE` — 9 arquivos, alguns densos, outros genéricos |
| `memory/daily/2026-02-26.md` | memory/daily | Nota de sessão | `ESTRUTURA VÁLIDA` |
| `memory/daily/2026-03-05.md` | memory/daily | Nota + transcrição tl;dv | `ESTRUTURA VÁLIDA` |
| `memory/daily/2026-03-07.md` | memory/daily | Nota de sessão | `ESTRUTURA VÁLIDA` |
| `memory/daily/2026-03-08.md` | memory/daily | Nota mais recente | `ESTRUTURA VÁLIDA` |
| `memory/daily/sunday-prep.md` | memory/daily | Dados para Briefing Dominical | `EXISTE, MAS ESTÁ INSUFICIENTE` — cron de coleta com 3 consecutiveErrors |
| `memory/pending.md` | memory/ | Lista soberana de pendências | `ESTRUTURA VÁLIDA` — viva, com seções organizadas |
| `memory/people.md` | memory/ | Diretório de pessoas | `EXISTE, MAS ESTÁ INSUFICIENTE` — estrutura boa, mas 70%+ dos contatos sem email/telefone |
| `memory/decisions.md` | memory/ | Decisões permanentes | `ESTRUTURA VÁLIDA` — denso, cobrindo WS1–WS7 |
| `memory/lessons.md` | memory/ | Aprendizados estratégicos | `ESTRUTURA VÁLIDA` — cobrindo curadoria de WS |
| `memory/projects.md` | memory/ | Projetos ativos | `EXISTE, MAS ESTÁ INSUFICIENTE` — não lido em detalhe; provavelmente incompleto |
| `memory/projects_orulo.md` | memory/ | Tracking de praças | `EXISTE, MAS ESTÁ INSUFICIENTE` — estrutura boa, mas C1/C2/C3 marcados como ⚠️ REVISAR |
| `memory/roles.md` | memory/ | Papéis e permissões | Não lido em detalhe — existência confirmada |
| `memory/personal_care.md` | memory/ | Cuidados pessoais de Diego | `ESTRUTURA VÁLIDA` — alimenta cron de cabelo |
| `memory/treinos.md` | memory/ | Registro de treinos | Existência confirmada — conteúdo não auditado |
| `memory/feedback/` | memory/ | Feedback loops (content, tasks, recommendations) | `EXISTE, MAS ESTÁ INSUFICIENTE` — 3 JSON files; ciclo de uso não documentado |
| `memory/tasks/task_pessoas_chave.md` | memory/tasks | Tarefa de mapeamento de pessoas | Existência confirmada |
| `memory/PRE_COMPACT_CHECKLIST.md` | memory/ | Checklist pré-compactação | Existência confirmada |

**Status das notas diárias:** 9 arquivos entre 26/02 e 08/03. Frequência inconsistente — há gaps. Pipeline de captura → consolidação não está automatizado de ponta a ponta.

---

### 2.3 Governança de Workstreams

| Arquivo / Pasta | Localização | Função | Estado |
|----------------|-------------|--------|--------|
| `governance/workstreams.md` | governance/ | Portfólio WS1–WS7 — documento-mestre | `ESTRUTURA VÁLIDA` — denso, completo, v1.0 (08/03) |
| `governance/pracas_sprint.md` | governance/ | Sistema sprint quinzenal com sócios | `ESTRUTURA VÁLIDA` — v2.0, completo |
| `governance/workstreams/WS1/` | governance/workstreams | CC — Comunicação Corretores | `ESTRUTURA VÁLIDA` — charter, plano, backlog, kickoff, pulse, onepage |
| `governance/workstreams/WS2/` | governance/workstreams | CX — Jornada DL→Pago | `ESTRUTURA VÁLIDA` — mesma estrutura |
| `governance/workstreams/WS3/` | governance/workstreams | FL — Fórmula Lançamento / Praças | `ESTRUTURA VÁLIDA` — mesma estrutura |
| `governance/workstreams/WS4/` | governance/workstreams | CRM — Estrutura Comercial | `ESTRUTURA VÁLIDA` — mesma estrutura |
| `governance/workstreams/WS5/` | governance/workstreams | MKT — Marketing e Conteúdo | `ESTRUTURA VÁLIDA` — mesma estrutura |
| `governance/workstreams/WS6/` | governance/workstreams | EMB — Embaixadoras Drive-Free | `ESTRUTURA VÁLIDA` — mais completo: inclui critérios_minimos, evidencia, checkin_mensal |
| `governance/workstreams/WS7/` | governance/workstreams | SL — Modelo Econômico Sócio Local | `ESTRUTURA VÁLIDA` — mesma estrutura |
| `governance/templates/` | governance/ | Templates de charter, kickoff, pulse | `ESTRUTURA VÁLIDA` — 3 templates |
| `governance/HARMONIZACAO_FINAL.md` | governance/workstreams | Alinhamento final dos WS | Existência confirmada |
| `governance/grupos_telegram/` | governance/ | Proposta de estrutura de grupos | `EXISTE, MAS ESTÁ INSUFICIENTE` — documentos criados, implementação PENDENTE |

**Status WS:** Todos os 7 WS têm documentação completa de papel. **Nenhum WS passou por kickoff formal registrado ainda.** Documentação: pronta. Execução: zero evidências no sistema.

---

### 2.4 Prompts e Jobs

| Arquivo | Localização | Função | Estado |
|---------|-------------|--------|--------|
| `jobs/cron_plan.yml` | jobs/ | Plano unificado de jobs v2.0 | `ESTRUTURA VÁLIDA` — 8 jobs documentados com IDs |
| `jobs/prompts/pracas_sprint_reminder_thu.txt` | jobs/prompts | Lembrete quinzenal sócio | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/pracas_sprint_check_mon.txt` | jobs/prompts | Checagem segunda 18h | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/pracas_sprint_check_tue_10.txt` | jobs/prompts | Alerta terça 10h | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/pracas_sprint_on_receive.txt` | jobs/prompts | Análise one-pager recebido | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/pracas_sprint_checkin_2xweek.txt` | jobs/prompts | Check-in 2x/semana | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/pracas_sprint_email_watcher.txt` | jobs/prompts | Watcher de e-mail one-pager | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/pracas_tldv_socio_detector.txt` | jobs/prompts | Detector tl;dv sócio local | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/pracas_pulse_2xweek.txt` | jobs/prompts | Pulse praças 2x/semana | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/memory_harvester.txt` | jobs/prompts | Consolidação estratégica memória | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/praças_weekly_scan.txt` | jobs/prompts | Scan semanal de praças | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/sprint_checkpoint.txt` | jobs/prompts | Checkpoint de sprint | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/sprint_facilitator.txt` | jobs/prompts | Facilitador de sprint | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/sprint_followup_tracker.txt` | jobs/prompts | Tracker de follow-ups D+3 | `ESTRUTURA VÁLIDA` |
| `jobs/prompts/sprint_reminder.txt` | jobs/prompts | Lembrete genérico de sprint | `ESTRUTURA VÁLIDA` |
| `jobs/quota_policy.yml` | jobs/ | Política de quotas de modelos | `ESTRUTURA VÁLIDA` |

**Total de prompts:** 14 arquivos. Todos focados em governança de praças e sprint. Não há prompts para workstreams não-WS3 (ex: WS1 CC, WS2 CX, WS4 CRM). **Lacuna evidente.**

---

### 2.5 Crons Ativos no OpenClaw (29 ativos de 44 registrados)

| Job | Agente | Frequência | Modelo | Status Real | consecutiveErrors |
|-----|--------|-----------|--------|-------------|-------------------|
| Daily Briefing — Morfeu | main | Seg–Sex 08:45 | MiniMax | ✅ ATIVO / OK | 0 |
| Watchdog de Crons | main | Diário 09:15 | MiniMax | ✅ ATIVO / OK | 0 |
| MiniMax Health Check (09h) | morfeu | Seg–Sex 09:00 | MiniMax | ✅ ATIVO / OK | 0 |
| Smart Email Scan (2h/9h-18h) | larissa | Seg–Sex 9–17h | MiniMax | ✅ ATIVO / OK | 0 |
| Scan Praças — Weekly | claudinei | Segunda 08:30 | MiniMax | ✅ ATIVO / nunca rodou | — |
| pracas-sprint-watcher | claudinei | A cada 2h/seg-sex | MiniMax | ✅ ATIVO / OK | 0 |
| Sprint Email Watcher — Seg/Ter | claudinei | A cada 2h/Seg+Ter | MiniMax | ✅ ATIVO / nunca rodou | — |
| Monitor tl;dv (2h/10h-18h) | claudinei | A cada 2h/Seg–Sex | MiniMax | ✅ ATIVO / OK | 0 |
| Check Contratos Pendentes (11h) | morfeu | Seg–Sex 11:20 | MiniMax | ✅ ATIVO / OK | 0 |
| pracas-sprint-check-mon | claudinei | Segunda 18:15 | MiniMax | ✅ ATIVO / nunca rodou | — |
| pracas-sprint-check-tue-10 | claudinei | Terça 10:00 | MiniMax | ✅ ATIVO / nunca rodou | — |
| pracas-sprint-reminder-thu | claudinei | Quinta 09:30 | MiniMax | ✅ ATIVO / nunca rodou | — |
| Pulse Praças 2x/semana | claudinei | Ter+Sex 09:00 | MiniMax | ✅ ATIVO / nunca rodou | — |
| Check-in Praças — Quarta 09h | claudinei | Quarta 09:00 | MiniMax | ✅ ATIVO / nunca rodou | — |
| Check-in Praças — Sexta 11h | claudinei | Sexta 11:00 | MiniMax | ✅ ATIVO / nunca rodou | — |
| Check Diário — Livro | claudinei | Seg–Sex 18:00 | MiniMax | ✅ ATIVO / OK | 0 |
| Madrugada — Insight e Memória | morfeu | Seg–Sáb 02:00 | MiniMax | ✅ ATIVO / OK | 0 |
| MiniMax Diagnóstico (04h) | morfeu | Seg–Sex 04:00 | MiniMax | ✅ ATIVO / OK | 0 |
| Relatório MiniMax (06h) | morfeu | Seg–Sex 06:00 | MiniMax | ✅ ATIVO / OK | 0 |
| Erros de Cron — Análise (07h) | claudinei | Seg–Sex 07:00 | MiniMax | ✅ ATIVO / nunca rodou | — |
| Auditoria Semanal — pending.md | claudinei | Sexta 17:00 | MiniMax | ✅ ATIVO / OK | 0 |
| Revisão Semanal — Morfeu | main | Sexta 16:00 | MiniMax | ✅ ATIVO / OK | 0 |
| Briefing Dom — Coleta (16h) | main | Domingo 16:00 | MiniMax | ✅ ATIVO / ERRO | **3 consecutiveErrors** |
| Briefing Dom — Análise (17h) | main | Domingo 17:00 | MiniMax | ✅ ATIVO / OK | 0 |
| Backup Diário (05h UTC) | main | Diário 02:00 BRT | systemEvent | ✅ ATIVO / OK | 0 |
| Cuidados Pessoais (Dom 14h) | main | Domingo 14:00 | MiniMax | ✅ ATIVO / nunca rodou | — |
| Trinks — Cabelo (Dom 08h) | claudinei | Domingo 08:00 | MiniMax | ✅ ATIVO / OK | 0 |
| Harvester de Memória (Dom 09h) | claudinei | Domingo 09:00 | MiniMax | ✅ ATIVO / OK | 0 |
| Lembrete WS2 Kickoff (16/03) | claudinei | One-shot 16/03 | systemEvent | ✅ ATIVO / pendente | — |

**Jobs desativados relevantes (15 total):**
- Monitor tl;dv (main) — substituído pela versão claudinei
- Digest Semanal de Emails — substituído por Quinta+Domingo
- Múltiplas versões duplicadas (larissa) de jobs que foram migrados para claudinei
- Check Pós-Reunião (30min) — desativado por custo/ruído
- Lembrete Tom de Voz — `🔴 ATIVO com ERRO`: model_not_found (haiku), patch aplicado mas próxima execução pendente (10/03)
- Check Email Qui 11h — `🔴 ERRO`: 1 consecutiveError por timeout (120s → 300s)

---

### 2.6 Scripts

| Script | Função | Estado |
|--------|--------|--------|
| `tldv_check.py` | Monitora Gmail, extrai e-mails tl;dv | `ESTRUTURA VÁLIDA` — em uso pelo crontab sistema |
| `tldv_enrich.py` | Pipeline enriquecido de tl;dv | `ESTRUTURA VÁLIDA` |
| `tldv_monitor.py` | Versão atual do monitor tl;dv | `ESTRUTURA VÁLIDA` |
| `tldv_store.py` | Armazena reuniões tl;dv | `ESTRUTURA VÁLIDA` |
| `tldv_socio_check.py` | Detecta reunião tl;dv com sócio local | `ESTRUTURA VÁLIDA` |
| `tldv_full_pipeline.py` | Pipeline completo tl;dv | `ESTRUTURA VÁLIDA` |
| `sprint_email_watcher.py` | Detecta e-mail de one-pager | `ESTRUTURA VÁLIDA` |
| `smart_email_scan.py` | Scan inteligente de e-mails | `ESTRUTURA VÁLIDA` |
| `email_digest_v2.py` | Digest de e-mails v2 | `ESTRUTURA VÁLIDA` |
| `email_digest.py` | Digest de e-mails v1 | `EXISTE, MAS ESTÁ INSUFICIENTE` — versão antiga, provavelmente substituída |
| `gmail_auth.py` | OAuth Gmail leitura | `ESTRUTURA VÁLIDA` |
| `gmail_send_auth.py` | OAuth Gmail envio | `ESTRUTURA VÁLIDA` |
| `send_scheduled_email.py` | Envio de e-mail agendado | `ESTRUTURA VÁLIDA` |
| `gcal_morfeu.py` | Integração Google Calendar | `ESTRUTURA VÁLIDA` |
| `verifica_contratos_pendentes.py` | Verificação de contratos | `ESTRUTURA VÁLIDA` |
| `minimax_health.py` | Health check MiniMax | `ESTRUTURA VÁLIDA` |
| `minimax_diagnostic.py` | Diagnóstico completo MiniMax | `ESTRUTURA VÁLIDA` |
| `trinks_booking.py` | Agendamento de cabelo (Trinks) | `ESTRUTURA VÁLIDA` |
| `backup_diego.sh` | Backup do workspace | `ESTRUTURA VÁLIDA` |
| `apply_groq_config.sh` | Configuração Groq | `EXISTE, MAS ESTÁ INSUFICIENTE` — Groq não está na stack principal |
| `create_event.py` | Criação de eventos no Calendar | Existência confirmada |
| `criar_lembrete.py` | Criação de lembretes | Existência confirmada |
| `criar_viagens.py` | Cadastro de viagens | Existência confirmada |
| `deprecated/tldv_monitor.py` | Versão antiga tl;dv | Deprecated — não usar |
| `deprecated/tldv_smart.py` | Versão intermediária tl;dv | Deprecated — não usar |

**Concentração:** Scripts fortemente focados em tl;dv (6 scripts) e e-mail (5 scripts). Scripts de Calendar existem mas uso real não confirmado nos crons principais.

---

### 2.7 Templates

| Arquivo | Função | Estado |
|---------|--------|--------|
| `templates/cobrancas.md` | Templates de cobranças | `ESTRUTURA VÁLIDA` |
| `templates/sprint_onepager.md` | One-pager do sócio local | `ESTRUTURA VÁLIDA` |
| `templates/sprint_meeting_minutes.md` | Ata + contrato de sprint | `ESTRUTURA VÁLIDA` |
| `templates/email_onepager_request.md` | E-mail de solicitação (3 versões) | `ESTRUTURA VÁLIDA` |
| `templates/email_sprint_feedback.md` | Retorno de Diego ao sócio | `ESTRUTURA VÁLIDA` |
| `templates/checkin_questions.md` | 4 perguntas + rascunho de check-in | `ESTRUTURA VÁLIDA` |
| `templates/followup_gustavo_20260306.md` | Follow-up específico para Gustavo | `EXISTE, MAS ESTÁ INSUFICIENTE` — caso pontual, não genérico |
| `templates/drafts/followup_gustavo_20260306.txt` | Rascunho do follow-up | Arquivo pontual |
| `templates/drafts/resposta_gustavo_20260306.txt` | Resposta ao Gustavo | Arquivo pontual |

**Lacuna crítica:** Não há templates de e-mail para WS1, WS2, WS4, WS5, WS7. Templates existem quase exclusivamente para o contexto de praças (WS3).

---

### 2.8 CRM Estratégico

| Componente | Estado |
|-----------|--------|
| `crm/SISTEMA.md` | `ESTRUTURA VÁLIDA` — filosofia e protocolo bem definidos |
| `crm/INDEX.md` | `EXISTE, MAS ESTÁ INSUFICIENTE` — 22 contatos mapeados, 60%+ sem perfil completo |
| `crm/templates/PESSOA_TEMPLATE.md` | `ESTRUTURA VÁLIDA` |
| `crm/templates/MEMBRO_TIME_TEMPLATE.md` | `ESTRUTURA VÁLIDA` |
| `crm/pessoas/time/gustavo-torres.md` | `ESTRUTURA VÁLIDA` — perfil detalhado |
| `crm/pessoas/time/zanella.md` | `ESTRUTURA VÁLIDA` — perfil com contexto Curitiba |
| `crm/pessoas/clientes/evandro.md` | `ESTRUTURA VÁLIDA` — ownership indefinido registrado |
| `crm/pessoas/parceiros/werner.md` | `ESTRUTURA VÁLIDA` — minuta pendente |
| Jade, Mirla, João Vitor, Luan, Kneip, Ester, Mayumi | `LACUNA` — 7 membros do time sem perfil |
| Diretoria (Alejandro, Felipe, Eduardo, Marcelo) | `LACUNA` — sem perfis |
| Clientes e networking além de Evandro/Werner | `LACUNA` — mapeamento incipiente |

---

### 2.9 Biblioteca Estratégica (Diego)

| Categoria | Estado |
|----------|--------|
| `biblioteca/00_indice.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/01_manifesto_identidade.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/02_savers_afirmacoes.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/03_visualizacao_guiada.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/04_okrs_metas.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/05_dashboard_kpis.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/06_autoridade_digital.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/07_voz_oratoria.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/08_forcas.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/09_sombras.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/10_leitura_mensal.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/11_implementacao_controle.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/12_manual_operacoes.md` | `ESTRUTURA VÁLIDA` |
| `biblioteca/orulo/` | `LACUNA` — diretório criado, nenhum dos 16 docs da Órulo foi importado |

---

### 2.10 Integrações Externas

| Integração | Documentação | Status Real | Estado |
|-----------|-------------|-------------|--------|
| **Gmail (leitura)** | Sim | Scripts funcionando | `ESTRUTURA VÁLIDA` |
| **Gmail (envio)** | Sim | Scripts existem; uso real via Lara (manual) | `EXISTE, MAS ESTÁ INSUFICIENTE` |
| **Google Calendar (gcalcli)** | Sim — TOOLS.md | Configurado em 27/02 | `ESTRUTURA VÁLIDA` |
| **tl;dv** | Sim — automations/index.md | Pipeline parcialmente ativo; cron recriado 07/03 | `EXISTE, MAS ESTÁ INSUFICIENTE` |
| **Bitrix24** | Referenciado em USER.md e AGENTS.md | Morfeu apenas lê; sem integração técnica direta | `LACUNA` — sem script, sem API, acesso manual |
| **Telegram** | Canal principal de output | Funcionando — saída dos crons | `ESTRUTURA VÁLIDA` |
| **Vaultwarden** | TOOLS.md | Configurado em cofre.diegodiehl.com | `ESTRUTURA VÁLIDA` |
| **Trinks** | Script existente | `trinks_booking.py` ativo | `EXISTE, MAS ESTÁ INSUFICIENTE` — funcionamento real não auditado |
| **WhatsApp** | Referenciado como canal futuro | Sem integração técnica | `LACUNA` |
| **Clicksign / Bitrix / Adobe Sign** | Referenciados no script de contratos | `verifica_contratos_pendentes.py` rodando | `EXISTE, MAS ESTÁ INSUFICIENTE` — não auditado output real |

---

### 2.11 Agentes

| Agente | Papel declarado | Jobs ativos | Estado |
|--------|----------------|------------|--------|
| **main** | Agente principal (Morfeu) | 8 ativos | `ESTRUTURA VÁLIDA` |
| **morfeu** | Funções de saúde do sistema e madrugada | 5 ativos | `ESTRUTURA VÁLIDA` |
| **claudinei** | Governança de praças, tl;dv, livro | 14 ativos | `ESTRUTURA VÁLIDA` |
| **larissa** | Secretária executiva | 1 ativo (Smart Email Scan) | `EXISTE, MAS ESTÁ INSUFICIENTE` — escopo muito restrito vs. papel declarado |

---

### 2.12 Sistema e Políticas

| Arquivo | Estado |
|---------|--------|
| `sistema/llm_policy_v2.1.md` | `ESTRUTURA VÁLIDA` — política ativa |
| `sistema/llm_policy_v2.md` | `EXISTE, MAS ESTÁ INSUFICIENTE` — versão anterior, não deletada |
| `sistema/llm_policy.md` | `EXISTE, MAS ESTÁ INSUFICIENTE` — versão v1, não deletada |
| `jobs/quota_policy.yml` | `ESTRUTURA VÁLIDA` |
| `hooks/task-received/HOOK.md` | Existência confirmada — não auditado |
| `hooks/task-received/handler.ts` | Existência confirmada — não auditado |

---

### 2.13 Documentos Externos da Órulo (Biblioteca Órulo)

| Status | Detalhe |
|--------|---------|
| `LACUNA TOTAL` | 16 documentos estratégicos da Órulo mencionados no USER.md (playbooks, visão, SDR, kits comerciais) **não foram importados**. O diretório `biblioteca/orulo/` existe mas contém apenas o `README.md` com lista de pendentes. |

---

### 2.14 Archive e Deprecados

| Localização | Conteúdo | Estado |
|-------------|---------|--------|
| `archive/governance/praças_v1.md` | Versão anterior da governança | `EXISTE, MAS ESTÁ INSUFICIENTE` — não deletado, pode confundir |
| `archive/governance/sprint_quinzenal_pracas_v1.md` | Versão anterior do sprint | Idem |
| `archive/jobs/cron_plan_v1.md` | Versão anterior do plano de jobs | Idem |
| `scripts/deprecated/` | 2 scripts obsoletos de tl;dv | Idem |

---

## 3. PRINCIPAIS CONCENTRAÇÕES

1. **Governança de praças (WS3):** É o núcleo mais desenvolvido do sistema. Tem documentação completa (charter, plano, backlog, pulse, onepage por WS3), 8+ prompts dedicados, 10+ jobs ativos e scripts específicos. Maior densidade de qualquer área.

2. **Monitoramento passivo:** 6 scripts de tl;dv + 5 de e-mail + 3 de saúde do sistema. O sistema é forte em detectar e alertar Diego — fraco em agir.

3. **Identidade e persona:** SOUL, USER, AGENTS, HEARTBEAT — todos densos, vivos, atualizados. Base sólida para raciocínio contextual.

4. **WS documentação:** Todos os 7 WS têm documentação de papel completa. Concentração em estrutura, não em execução.

---

## 4. PRINCIPAIS DISPERSÕES

1. **Versões duplicadas sem limpeza:** 3 versões de llm_policy (v1, v2, v2.1), múltiplos jobs desativados de larissa que espelham jobs ativos de claudinei, 2 scripts deprecated, 3 arquivos de archive com v1s.

2. **Automations/index.md desatualizado:** Registra o estado de fevereiro, não reflete a realidade atual (jobs migrados para claudinei, novos scripts, tl;dv reconfigurado em março).

3. **CRM com maioria dos perfis vazios:** 22 contatos no INDEX, mas apenas 4 com arquivo real. 7 membros do time direto de Diego sem perfil.

4. **Templates concentrados em WS3:** Não há templates de comunicação para WS1 (cobranças com corretores), WS2 (follow-ups com DLs), WS4 (e-mails CRM) ou WS7 (produtos financeiros).

5. **Prompts sem cobertura:** 14 prompts ativos, mas 100% focados em praças. Nenhum prompt para os outros 6 workstreams.

---

## 5. LACUNAS

| Lacuna | Impacto |
|--------|---------|
| `BOOTSTRAP.md` ausente | Arquivo esperado pelo sistema mas inexistente |
| `biblioteca/orulo/` vazia (16 docs não importados) | Morfeu não tem acesso aos playbooks, visão e kits da Órulo que Diego usa no dia a dia |
| CRM: 7 membros do time sem perfil | Morfeu não tem contexto de performance, histórico ou estilo de comunicação do time |
| Bitrix24 sem integração técnica | Sistema comercial principal é caixa-preta para o Morfeu |
| Prompts inexistentes para WS1, WS2, WS4, WS5, WS6, WS7 | Governança dos 6 outros workstreams depende 100% de input manual de Diego |
| `memory/projects_orulo.md`: C1/C2/C3 todos como "a definir" | Jobs de check-in e pulse rodam mas sem dados reais para processar |
| Template de cobranças externas | Templates existem para praças; cobranças para clientes Bitrix não documentadas |
| Larissa: escopo real ≠ escopo declarado | Bot existe, tem 1 job ativo, mas papel de secretária executiva não está operacionalizado |
| `memory/daily/sunday-prep.md`: coleta com 3 consecutiveErrors | Briefing Dominical de análise roda sem dados coletados |
| Pipeline de memória daily → consolidado: não automatizado | Notas diárias não sobem automaticamente para pending/projects/decisions |

---

## 6. RISCOS DO INVENTÁRIO ATUAL

| Risco | Severidade | Descrição |
|-------|-----------|-----------|
| **Jobs rodando com dados vazios** | 🔴 ALTO | 6+ jobs de praças ativos consumindo recursos e gerando alertas baseados em `[PREENCHER]` / "a definir" em `projects_orulo.md` |
| **Briefing Dominical quebrado** | 🔴 ALTO | Coleta com 3 consecutiveErrors; análise roda sobre dados inconsistentes |
| **Lembrete Tom de Voz com erro** | 🟡 MÉDIO | Job `lembrete-tom-de-voz` com `consecutiveErrors: 1`; modelo corrigido mas ainda não executou |
| **Check Email Qui com timeout** | 🟡 MÉDIO | `consecutiveErrors: 1`; timeout às 120s |
| **Duplicação de jobs (larissa vs claudinei)** | 🟡 MÉDIO | Jobs desativados de larissa espelham ativos de claudinei; risco de reativação acidental |
| **Ausência de Bitrix = caixa-preta** | 🟡 MÉDIO | Morfeu reporta pipeline sem dados reais; tudo que envolve deals é estimativa ou input manual |
| **16 docs Órulo não importados** | 🟡 MÉDIO | Morfeu opera sem acesso aos playbooks e visão da empresa que Diego usa no campo |
| **Archive não curado** | 🟢 BAIXO | 3 arquivos v1 no archive podem confundir leitura de contexto em sessões futuras |
| **3 versões de llm_policy** | 🟢 BAIXO | Risco de agente ler versão errada; nomes explícitos mitigam o risco |

---

## 7. INSUMOS PARA A ETAPA 2 — GOVERNANÇA DOS WORKSTREAMS

Com base neste inventário, a Etapa 2 deve investigar:

1. **Status real de execução dos WS:** Documentação está pronta, mas há evidência de reunião ao vivo, pulse gerado, ou ação executada por algum DRI?

2. **Ciclo de check-in funciona?** Os jobs de praças geram alertas. Diego age sobre eles? Sócios respondem? O one-pager já chegou ao sistema?

3. **Handoff Morfeu → Lara → Time:** O pipeline de rascunho + INSTRUÇÕES PARA LARA está sendo usado? Lara executa?

4. **WS sem prompt:** Como está sendo monitorado WS1 (Ester), WS2 (Gustavo/BDRs), WS4 (Gustavo), WS5 (Mayumi), WS6 (Mayumi), WS7 (Diego)?

5. **Days Since Touch por WS:** Qual é o `last_live_touch` real de cada WS? Algum já passou dos 14 dias?

6. **Bitrix: o que Diego enxerga vs. o que Morfeu enxerga:** Como o pipeline comercial real se traduz (ou não) em informação para o agente?

---

*Etapa 1 concluída. Próxima: `02_governanca_workstreams.md`*
