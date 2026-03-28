# ESTADO DO SISTEMA — MORFEU
> Versão: 1.0 | Data: 2026-03-28 | Autor: Onda 5 — Limpeza de Sistema
> Atualizar manualmente após cada mudança de jobs

---

## RESUMO EXECUTIVO

| Indicador | Valor |
|-----------|-------|
| Jobs ativos | 18 |
| Jobs disabled | 15 |
| Jobs removidos (total histórico) | 6 |
| Scripts testáveis | 29 ✅ |
| Scripts com WARN | 5 ⚠️ |
| Scripts com timeout OAuth | 8 ⏱️ |
| Skills ativas | 4 |
| Pendências em aberto | [VERIFICAR] |

---

## 🟢 JOBS ATIVOS (18)

### PESSOAL — Diego Diehl

| # | Nome | ID | Schedule | Proprietário | Propósito | SLA |
|---|------|----|----------|--------------|-----------|-----|
| 1 | 🌙 Overnight Thinking Mode | 7dd8f8d5 | Ter-Sáb 04:30 BRT | morfeu | Processar últimas 24h, gerar alertas e perguntas para Diego | — |
| 2 | 💈 Trinks — Sugestão Cabelo | 21647e7c | Dom 08h BRT | morfeu | Sugerir horário de cabelo baseado em janela de 21-28 dias | — |
| 3 | 💈 Cuidados Pessoais — Check Semanal | 0f529fd3 | Dom 14h BRT | morfeu | Check de cabelo + sugestão de agendamento | — |

### ÓRULO — Operações

| # | Nome | ID | Schedule | Proprietário | Propósito | SLA |
|---|------|----|----------|--------------|-----------|-----|
| 4 | 🧭 Briefing Dominical — Coleta (13h) | 02d749f4 | Dom 16h BRT | morfeu | Coletar dados para briefing das 17h | — |
| 5 | 🧭 Briefing Dominical — Análise (14h) | d12a4136 | Dom 17h BRT | morfeu | Briefing completo para Diego | Dom 17h BRT |
| 6 | 📊 Pulse Praças 2x/semana (Ter+Sex 09h) | b9726fbf | Ter+Sex 09h BRT | morfeu | Status das praças (Curitiba + Vitória) | Ter+Sex 09h |
| 7 | 📲 Check-in Praças — Quarta 09h | 57ec47fc | Quarta 09h BRT | morfeu | 4 perguntas + rascunho para sócio local | Quarta 09h |
| 8 | 🔬 MiniMax Health Unificado (09h) | 5edcf78f | Seg-Sex 09h BRT | morfeu | Health + quota + diagnóstico MiniMax | Seg-Sex 09h |
| 9 | 🧠 Harvester — decisions.md (Dom 22h) | 65cf1970 | Dom 22h BRT | morfeu | Auditar decisões, detectar inconsistências | Dom 22h |
| 10 | 🧠 Harvester — lessons.md (Dom 22h30) | 08f2a618 | Dom 22h30 BRT | morfeu | Auditar lições, detectar padrões recorrentes | Dom 22h30 |
| 11 | 🌙 Madrugada — Insight e Memória | b534ff47 | Seg-Sáb 02h BRT | morfeu | Processar reuniões + crons + pendências | Seg-Sáb 02h |

### TIME — Operações de Time

| # | Nome | ID | Schedule | Proprietário | Propósito | SLA |
|---|------|----|----------|--------------|-----------|-----|
| 12 | 📧 Smart Email Scan — 2h (9h-18h) | 1ba68cbe | Seg-Sex 09h,13h,17h | larissa | Triar emails importantes, enviar resumo | Seg-Sex 3xdia |
| 13 | 📧 Follow-up semanal: Zanella + V6 | 8a0a2fa6 | Ter 08:50 BRT | larissa | Lembrete para Zanella sobre reunião V6 | Ter 08:50 |
| 14 | 📋 Lembrete CRM CRI Semanal | dcf23d48 | Sex 08h BRT | larissa | Lembrete para time atualizar CRM de CRI | Sex 08h |

### INFRA — Sistema e Backups

| # | Nome | ID | Schedule | Proprietário | Propósito | SLA |
|---|------|----|----------|--------------|-----------|-----|
| 15 | ⚙️ P3 — Quota Estimator (2h) | 539b796f | 2h | claudinei | Atualizar quota_estimator a cada 2h | — |
| 16 | 💾 Backup Diário — Workspace → Drive | 9574d0b0 | Diariamente 05h UTC | main | Backup workspace para Google Drive | Diário 05h UTC |

### ONE-SHOT — Lembretes Programados

| # | Nome | ID | Schedule | Proprietário | Propósito | Status |
|---|------|----|----------|--------------|-----------|--------|
| 17 | Lembrete Validacao Pracas v1 | 647a5670 | 03/04/2026 13h | claudinei | Validação da frente Pracas v1 | ⏳ Pendente |
| 18 | 💬 Pergunta: Sinduscon RS - Felipe | 18c31f46 | 11/04/2026 10h | morfeu | Pergunta sobre evento Porto Alegre | ⏳ Pendente |

---

## ⚫ JOBS DISABLED (15)

| # | Nome | ID | Motivo |
|---|------|----|--------|
| D1 | 🔬 MiniMax Health Check (09h BRT) | 0f03c740 | Duplicado do job 8 (MiniMax Health Unificado) |
| D2 | Daily Briefing — Morfeu | 19741391 | Desativado por Diego (pausado 60 dias) |
| D3 | pracas-sprint-check-mon | 1a8a8f9a | **Removido** na Onda 5 — timeout crônico |
| D4 | 🏛️ Scan Praças — Weekly | 2688a54a | Substituído pelo Pulse 2x/semana (job 6) |
| D5 | 🔬 MiniMax Diagnóstico Completo (04h) | 26f3c8cb | Duplicado do job 8 |
| D6 | 🔍 Scanner WS — Semanal (Qua 10h) | 2a54db05 | Nunca utilizado / sem evidência de valor |
| D7 | 🧠 Harvester de Memória — Dom 09h | 38ef0eb4 | Redundante com jobs 9+10 |
| D8 | pracas-sprint-reminder-thu | 39e87458 | **Removido** na Onda 5 — timeout crônico |
| D9 | 📋 Check Contratos Pendentes — 11h | 3a6caf28 | Script com problemas (timeout) |
| D10 | 🔒 LLM Policy — Constraint Check P1 | 576c265f | Verificação manual desnecessária |
| D11 | 🗓️ Check Pós-Reunião — 30min | 696a5c6b | Nunca utilizado |
| D12 | 📋 Auditoria Semanal — pending.md | 70fe1174 | **Removido** na Onda 5 — timeout crônico |
| D13 | 🔍 Erros de Cron — Análise Diária (07h) | 73a3a579 | **Removido** na Onda 5 — timeout crônico |
| D14 | 📬 Sprint Email Watcher | 8480fd4c | **Removido** na Onda 5 — timeout crônico |
| D15 | 📲 Check-in Praças — Sexta 11h | bbb492e8 | **Removido** na Onda 5 — timeout crônico + delivery failure |

---

## 🔇 REMOVIDOS NA LIMPEZA (6)

| # | Nome | ID | Motivo da Remoção |
|---|------|----|-------------------|
| R1 | pracas-sprint-check-mon | 1a8a8f9a | Timeout crônico 180s |
| R2 | pracas-sprint-reminder-thu | 39e87458 | Timeout crônico 120s |
| R3 | Auditoria Semanal pending.md | 70fe1174 | Timeout crônico 120s |
| R4 | Erros de Cron — Análise 07h | 73a3a579 | Timeout crônico 90s |
| R5 | Sprint Email Watcher | 8480fd4c | Timeout crônico 90s |
| R6 | Check-in Praças Sexta 11h | bbb492e8 | Timeout + delivery failure |

---

## 📊 SCRIPTS — ESTADO DE SAÚDE

### ✅ FUNCIONANDO (29)

| Script | Tempo | Propósito |
|--------|-------|-----------|
| create_event.py | 0.9s | Criar evento no Google Calendar |
| create_event_from_email.py | OK | Criar evento a partir de e-mail |
| criar_viagens.py | OK | Gerar roteiros de viagem |
| drive_audit.py | OK | Auditar estrutura do Drive |
| drive_auth.py | OK | Autenticar Google Drive |
| drive_auth_v2.py | OK | Autenticação v2 |
| drive_list_structure.py | 6.3s | Listar estrutura do Drive |
| drive_oauth_manual.py | OK | OAuth manual Drive |
| drive_reorg.py | OK | Reorganizar Drive |
| email_digest_v2.py | OK | Digest de e-mails |
| endpoint_health.py | 0.7s | Health de endpoints |
| gcal_morfeu.py | OK | Google Calendar |
| gmail_auth.py | OK | Gmail auth |
| gmail_send_auth.py | OK | Enviar gmail auth |
| minimax_diagnostic.py | OK | Diagnóstico MiniMax |
| minimax_health.py | OK | Health MiniMax |
| quota_estimator.py | 0.0s | Estimar quota MiniMax |
| smart_email_scan.py | OK | Scan inteligente de emails |
| sprint_email_watcher.py | 0.9s | Detectar One-Pagers de sprint |
| test_gcal.py | 0.8s | Testar gcalcli |
| testar_scripts.py | OK | Auditoria completa de scripts |
| tldv_check.py | 0.0s | Checar transcrições tl;dv |
| tldv_enrich.py | 0.9s | Enriquecer transcrições |
| tldv_full_pipeline.py | 0.9s | Pipeline completo tl;dv |
| tldv_monitor.py | 1.2s | Monitorar reuniões |
| tldv_socio_check.py | 0.0s | Checar status de sócio |
| tldv_store.py | 0.0s | Armazenar transcrições |
| trinks_booking.py | 0.0s | Booking de cabelo (requer TRINKS_PASSWORD) |

### ⚠️ PRECISAM ARGUMENTO OU CONFIG (5)

| Script | Problema | Ação Necessária |
|--------|----------|-----------------|
| create_drive_structure.py | Requer --tree ou --file | Definir escopo |
| drive_auth.py | Precisa auth manual | Manual setup |
| drive_auth_v2.py | Precisa auth manual | Manual setup |
| drive_oauth_manual.py | Precisa auth manual | Manual setup |
| trinks_booking.py | TRINKS_PASSWORD não definido | Configurar variável |

### ⏱️ TIMEOUT — OAuth Interativo (8)

| Script | Causa |
|--------|-------|
| criar_viagens.py | OAuth Gmail interativo |
| drive_audit.py | OAuth Drive interativo |
| drive_reorg.py | OAuth Drive interativo |
| email_digest_v2.py | OAuth Gmail interativo |
| gmail_auth.py | OAuth interativo |
| gmail_send_auth.py | OAuth interativo |
| smart_email_scan.py | OAuth interativo |
| testar_scripts.py | Auto-referência (normal) |

---

## 🎯 SLAs DOS JOBS CRÍTICOS

| Job | SLA | Criticidade | Action se falhar |
|-----|-----|-------------|------------------|
| Backup Diário (05h UTC) | 06h BRT | 🔴 Alta | Alertar Diego manualmente |
| Briefing Dominical (17h BRT) | 17h05 BRT | 🟡 Média | Gerar manualmente na segunda |
| Pulse Praças (Ter+Sex 09h) | 09h30 BRT | 🟡 Média | Gerar manualmente |
| MiniMax Health (09h) | 09h30 BRT | 🟡 Média | Verificar manualmente |
| Check-in Praças Quarta (09h) | 09h30 BRT | 🟡 Média | Gerar manualmente |
| Smart Email Scan (3x dia) | +15min do schedule | 🟢 Baixa | Ignorar (retry no próximo ciclo) |

---

## 📝 REGISTRO DO QUE FOI CORTADO — ONDAS 1-5

### Jobs Removidos (6)
**Por quê:** Timeout crônico — script não completava dentro do limite de 180s imposto pelo plano MiniMax Starter.

**Decisão:** Remover em vez de corrigir porque:
- Os scripts dependiam de OAuth interativo
- O tempo de execução excedia consistentemente o SLA
- Função era coberta por outros jobs ativos

### Jobs Desativados (18)
**Por quê:** Pausados por Diego ou identificados como duplicados/redundantes.

**Critérios:**
- Funcionalidade coberta por outro job ativo
- Nunca gerou output útil documentado
- Diego pausou explicitamente (Daily Briefing)

### Pendências Arquivadas (P1-P11)
**Por quê:** Nunca executadas. Eram planos ambitious demais para o momento.

### Lições Antigas (sessões 03/05-03/16)
**Por quê:** Supersedadas por sessões mais recentes com informação mais relevante.

---

## 🔄 PRÓXIMAS MUDANÇAS ESPERADAS

| O quê | Quando | Condição |
|-------|--------|----------|
| Reativar Daily Briefing | Após validação de Diego | depends on Diego |
| Reativar Scanner WS | Quando WS ficarem mais maduros | depends on WS maturity |
| Consolidar Pracas jobs | Quando segunda praça ativar | depends on praça expansion |
| Reativar Harvester Memória | Se memória começar a degradar | depends on memory quality |

---

*Documento gerado na Onda 5 (2026-03-28). Atualizar após cada adição/remoção de job.*
