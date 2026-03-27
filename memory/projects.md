# projects.md — Projetos Ativos

## Setup Morfeu / OpenClaw — CONCLUÍDO ✅
**Concluído em:** 2026-02-26
**O que foi entregue:**
- Servidor blindado (UFW, Fail2ban, SSH key-only)
- Telegram x2 bots (@Base_DD_bot + @larissa_personal_assistant_bot)
- Cloudflare Tunnel (openclaw.diegodiehl.com + cofre.diegodiehl.com)
- Vaultwarden self-hosted
- Identidade completa: SOUL.md, USER.md (431 linhas), AGENTS.md, IDENTITY.md, BOOT.md
- Estrutura de memória: MEMORY.md + memory/ (01–05 + daily/ + feedback/)
- Configuração de compactação: 160k tokens, 30k reserva, memoryFlush ativo

## Módulo 4 — Memória — CONCLUÍDO ✅
**Concluído em:** 2026-02-27
**O que foi entregue:**
- Estrutura de arquivos (pending, projects, decisions, lessons, people, daily/)
- PRE_COMPACT_CHECKLIST, HEARTBEAT.md, feedback/ ativos
- Tokens configurados: contextTokens=160k, reserveTokensFloor=30k, memoryFlush=ativo
- Embedding provider: Gemini (gemini-embedding-001) — índice rodado, busca semântica ativa

## Órulo — Sócio Diretor Comercial
**Status:** Ativo (principal)
**Foco Q1:** MRR, praças com stack completo, rituais de governança, 3 playbooks
**Próxima viagem de campo:** Vitória (ES) — 04/03/2026

## Módulo 5 — Integrações e Crons — CONCLUÍDO ✅
**Concluído em:** 2026-02-27
**O que foi entregue:**
- 3 crons ativos: Daily Briefing (seg-sex 08h45), Revisão Semanal (sex 16h), Lembrete Vitória ES (03/03 08h)
- Google Calendar integrado via gcalcli — conta diego.diehl@orulo.com.br
- Daily Briefing atualizado para incluir agenda do Calendar
- Docs do módulo salvos em /workspace/docs/ (cron-examples.md, integrations-setup.md)
**Próximas integrações (backlog):**
- LinkedIn métricas via RapidAPI → H2 2026 (aguarda rotina de conteúdo estável)
- Notion → sem prazo definido
- Embedding provider → pendente decisão Diego

## LLM Quota Policy v2.1 — FASES 1-4 CONCLUÍDAS ✅
**Iniciado em:** 2026-03-06 | **Última atualização:** 16/03/2026
**Status:** Fases 1 a 4 completas. Fase 5 aguarda dados reais (~27/03).
**Fases:**
- ✅ Fase 1 (06/03): 7 jobs duplicados desativados
- ✅ Fase 2 (06/03): 10 correções de metadata
- ✅ Fase 3 (~09/03): 3 novos jobs P2 + constraint checks em P1-A
- ✅ Fase 4 (16/03): Harvesters decisions+lessons (Dom 22h/22h30) + double-pass Revisão Semanal + scripts P3 (lockfile, endpoint_health, quota_estimator)
- ⏳ Fase 5 (~27/03): Calibração com dados reais de latência e remains
**Quota estimada:** 93/100 restantes (aferido 16/03 22h30)
**Revisão geral agendada:** 16/04/2026 (cron one-shot ativo)
**Docs:** `sistema/llm_policy_v2.1.md` | scripts P3 em `scripts/`

## Monitor tl;dv — RECRIAR DO ZERO ⚠️
**Status:** Job IDs `e309b1a4` e `f82115ff` completamente ausentes do jobs.json (foram deletados, não só desativados)
**Ação necessária:** Recriar via Fase 3 com nova frequência (1x/2h, 10–18h seg-sex) + gate `remains ≥ 40` no prompt + model `minimax/MiniMax-M2.5`
**Scripts ativos:** `/root/.openclaw/workspace/scripts/tldv_monitor.py` e `tldv_check.py`
**Tokens Gmail:** `/root/.config/morfeu/gmail_token.pkl`
**Flag files:** `/root/.config/morfeu/tldv_pending.json`, `tldv_processed.json`, `tldv_pause_until`

## Monitor tl;dv — OBSOLETO (ver "RECRIAR DO ZERO" acima)
**Configurado em:** 2026-02-27 — **job IDs deletados em 2026-03-06**

## Monitor tl;dv — ATIVO ✅
**Criado em:** 2026-02-27
**Status:** Operacional
**O que faz:** Monitora inbox do Gmail (`diego.diehl@orulo.com.br`) para emails do tl;dv (`no-reply@tldv.io`). A cada nova reunião detectada, processa o corpo do email e envia resumo estruturado no Telegram com: participantes, tópicos, itens de ação (Diego separado do time), perguntas de esclarecimento e próximas ações.
**Componentes:**
- Script: `/root/.openclaw/workspace/scripts/tldv_monitor.py`
- Token Gmail: `/root/.config/morfeu/gmail_token.pkl`
- Última saída: `/root/.config/morfeu/tldv_latest.json`
- Processados: `/root/.config/morfeu/tldv_processed.json`
- Cron: ID `e309b1a4` — toda hora (`:00`) em BRT
**Reuniões já processadas (27/02):**
- Órulo + Apolar (26/02) — parceria com Apolar, 6 ações geradas
- Mayumi <> Gustavo (26/02) — mkt + comercial, eventos Vitória e Curitiba

## Integração Trinks — Agendamento Automático Cabelo
**Status:** Script pronto, cron pendente aprovação
**Criado em:** 2026-03-02
**O que faz:** Consulta disponibilidade de Moisés na Trinks, cruza com janela de 21-28 dias após último corte, sugere horários via Telegram. Agenda apenas com confirmação explícita.
**Componentes:**
- Script: `/root/.openclaw/workspace/scripts/trinks_booking.py`
- Credenciais: diegodiehl0@gmail.com / TRINKS_PASSWORD env
- IDs: estab=18557, prof=676076, servico=1329815
- Endpoints documentados em `memory/personal_care.md`
**Próximo:** Diego confirmar → criar cron domingo 08h BRT chamando `--suggest`

## Livro — Palestras Inspiradoras ✅ CONCLUÍDO
**Status:** Concluído em 26/03/2026
**Iniciado em:** 04/03/2026
**O que foi entregue:** Livro finalizado por Diego.
**Cron de check diário:** desativado (7e712ad8) em 26/03/2026.

## Diagnóstico Estrutural Órulo (7 etapas)
**Status:** Em andamento | **Iniciado em:** 2026-03-09
**Saída:** Artefatos em `diagnostico/` (1 arquivo por etapa)

| Etapa | Arquivo | Status |
|-------|---------|--------|
| 1 — Inventário do Sistema | `01_inventario_sistema.md` | ✅ Concluído |
| 2 — Governança Workstreams | `02_governanca_workstreams.md` | ✅ Concluído |
| 3 — Operação Externa | `03_operacao_externa.md` | ✅ Concluído |
| 4 — Interface com o Time | `04_interface_time.md` | ✅ Concluído |
| 5 — Infraestrutura do Agente | `05_infra_agente.md` | ✅ Concluído |
| 6 — Arquitetura Recomendada | `06_arquitetura_recomendada.md` | ⏳ Aguardando prompt Diego |
| 7 — Plano de Ação | `07_plano_acao.md` | ⏳ Aguardando prompt Diego |

**Achados críticos até Etapa 5:**
- Daily Briefing (P0): 50% falha nos últimos 7 dias
- Watchdog: 57% / Briefing Dom Coleta: 0% (completamente quebrado)
- LLM Policy v2.1: documento, não enforcement (pools/CB/DLQ não existem nativo)
- WS3 concentra 100% da automação; WS1/2/4/5/6/7 = zero
- Agente é pessoal para Diego; repositório passivo para a Órulo
- Pipeline tl;dv → pending.md → rastreamento não existe

## Governança Workstreams H1 — Órulo
**Status:** Em curadoria (WS1-WS7 concluídos) | **Harmonização:** Concluída
**Iniciado em:** 2026-03-07

### WS1 — Comunicação com Corretores ✅ PRONTO
**DRI:** Mayumi | **Executor:** Ester | **Coordenação:** Gustavo
**Escopo:** Comunicação + ativação + reativação de corretores, canal WhatsApp (foco), evolução e-mail/push
**Meta H1:** WAU +40% geral / +80% praças não consolidadas
**Baseline:** Parte do zero
**Arquivos:** `governance/workstreams/WS1/charter.md`, `plan_quinzenal_sprint01.md`, `backlog.md`, `kickoff_prep.md`
**Classificação:** A) Pronto para kickoff

### WS2 — Jornada CX: DL → Pago ✅ PRONTO
**DRI:** Gustavo | **Executores:** Jade + Mirla (BDRs) | **Closer:** Participa quando necessário
**Escopo:** Trilha mínima DL→Pago, lista de DLs, valor entregue, indicadores operacionais
**Indicadores:** Total DLs (1268), DLs em contato, DLs com próximo passo, DLs com valor entregue, DLs que avançaram
**Meta 400:** Meta comercial ampla — não é KPI operacional do WS2
**Arquivos:** `governance/workstreams/WS2/charter.md`, `plan_quinzenal_sprint01.md`, `backlog.md`, `kickoff_prep.md`
**Classificação:** A) Pronto para kickoff

### WS3 — Fórmula de Lançamento / Workshops / Praças ✅ CONSOLIDADO
**DRI:** Mayumi + Sócios Locais | **Praças:** Curitiba (Zanella), Vitória (Kneip)
**Escopo:** Sprint quinzenal por praça, One-Pager, workshops e ativações
**Classificação:** A-) Pronto para kickoff com pré-work estruturado

### WS4 — Estrutura Comercial & CRM ✅ CONSOLIDADO
**DRI:** Gustavo
**Escopo:** CRM mínimo + hygiene + cadências SDR leves
**Classificação:** A) Pronto para kickoff

### WS5 — Marketing e Conteúdo ✅ CONSOLIDADO
**DRI:** Mayumi
**Escopo:** Eventos → ativos → evidência; event-driven
**Classificação:** A-) Pronto para kickoff com pré-work estruturado

### WS6 — Programa de Incorporadoras Embaixadoras ✅ CONSOLIDADO
**DRI:** Mayumi
**Escopo:** Substituir Drive por Órulo/Portal como canal oficial; drive-free
**Métrica soberana:** % drive-free por praça
**Classificação:** A) Pronto para kickoff

### WS7 — Remuneração e Incentivos do Sócio-Local ✅ CONSOLIDADO
**DRI:** Eduardo + Felipe
**Escopo:** Modelo econômico por praça; tipos Full/Híbrida/Remota; arquitetura: base + verba + variável operacional + variável receita + booster; métrica soberana: MRR/ARR por praça
**Classificação:** A-) Pronto para kickoff com pré-work estruturado
**DRI:** Eduardo + Felipe | **Status:** Pendente documentos
**DRI:** Eduardo + Felipe | **Status:** Pendente documentos
**Status:** Planejamento (Q1) → Execução (Q2)
**Foco Q1:** Contratar social media (até março), definir territórios de conteúdo

### Intenção registrada — LinkedIn (27/02/2026)
Diego quer se posicionar melhor no LinkedIn, mas reconhece que **precisa primeiro de estrutura e rotina de criação de conteúdo** para aparecer lá de forma consistente.
- Integração técnica (RapidAPI métricas / automações): **backlog para H2 2026**
- Pré-requisito: social media contratada (Q1) + cadência de publicação estável (Q2)
- Revisitar quando a máquina de conteúdo estiver rodando

---

## Sistema Operacional Comercial Órulo — EM OPERAÇÃO PARCIAL 🔄
**Estruturação concluída em:** 11/03/2026 | **Última atualização:** 16/03/2026
**Status:** WS3 em operação (Sprint 02 iniciando 18/03). WS1/2/4/5/6/7 sem kickoff.

**O que foi entregue:**
- Drive organizado: raiz oficial + 8 pastas + 7 WS + todos os arquivos como Google Docs
- 9 documentos canônicos consolidados no Drive
- 7 ONEPAGE_CHARTERS (WS1-WS7) confirmados
- Planilha WS_OPERATING_SYSTEM_H1_2026 no lugar correto (01_GOVERNANCA_GERAL)
- 70 itens de backlog (Sprint 0+1) para todos os 7 WS
- Auditor leve configurado no OpenClaw (4 modos)
- Memória estrutural gravada: memory/orulo_sistema_operacional.md
- SOUL.md e TOOLS.md atualizados com perfil operacional Órulo

**Próximos marcos:**
1. Corrigir DRI na planilha
2. Definir prazos do Sprint 0
3. Agendar kickoffs (WS2 e WS4 primeiro)
4. Primeira rotina leve / auditoria curta

**Referências-chave:**
- Raiz Drive: `1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM`
- Planilha: `1n9CUO8U6h6MUKCmKszXMtU_veAmSCo-q`
- Memória estrutural: `memory/orulo_sistema_operacional.md`
- Fechamento do dia: `memory/daily/2026-03-11.md`

