# Pendências em Aberto — Morfeu

*Última atualização: 2026-03-27 (revisão pós-curso)*

---

## 🔴 URGENTE — Requer Decisão

- [ ] **[P0 — KR7 MRR]** Consolidar MRR total de todas as incorporadoras pagantes. Sem esse número, KR7 não tem diagnóstico. DRI: Diego + Felipe (financeiro) | Prazo: urgente.

- [ ] **[P0 — KR5 Instrumento]** Definir como medir "integrações ativas +40%" — qual é a base, o que entra, a frequência. DRI: Gustavo | Prazo: urgente.

- [ ] **[P0 — KR6 Baseline]** Definir baseline de "corretores ativos" — quantos existiam antes para medir +40%. DRI: Gustavo | Prazo: urgente.

- [ ] **[WS3 — DRI Eduardo]** Eduardo não confirmou se é DRI oficial do WS3. Sem confirmação, não há accountability. DRI: Diego | Prazo: esta semana.

- [ ] **[WS2 — Kickoff pendente]** Kickoff com Gustavo — >10 dias parado desde data combinada. DRI: Diego | Prazo: urgente.

- [ ] **[WS4 — Kickoff pendente]** WS4 (CRM) precisa de kickoff antes de WS2 andar. DRI: Diego | Prazo: esta semana.

---

## 🟡 ESTABILIZAÇÃO DO SISTEMA (prazo: 16/05/2026)

> Pré-requisitos para reativar Daily Briefing e Scan Praças Weekly.

- [ ] **[PROCESSO — CRM Bitrix]** Método único de marcar conta/deal como "DL" — tag, estágio ou pipeline. Sem isso, DL é falho. DRI: Diego + Gustavo | Prazo: a definir.

- [ ] **[PROCESSO — Praças]** Ciclo C1/C2/C3 por sprint — precisa fluir sem input manual toda vez. DRI: Diego | Prazo: Sprint 03.

- [ ] **[DADOS — CRM]** Campo `praça` como dropdown obrigatório no Bitrix. DRI: Diego + Gustavo | Prazo: a definir.

- [ ] **[DADOS — CRM]** JSON de SLA por estágio do funil — input para skill de deals parados. DRI: Diego + Gustavo | Prazo: a definir.

- [ ] **[SISTEMA — Briefing Dominical]** Verificar se está gerando output útil. DRI: Diego | Prazo: 16/05.

- [ ] **[SISTEMA — Scan Praças Weekly]** Reativar quando C1/C2/C3 fluir + projects_orulo atualizado por sprint. DRI: Morfeu + Diego | Prazo: ~16/05.

---

## 🟢 OPERACIONAL — CURSANDO

- [ ] **[SPRINT 02 — Curitiba (Zanella)]** 18/03–01/04. C1: 4 vendas em 7 dias. Evento foi 18/03. One-Pager Sprint 01 recebido? Registro em CRM? DRI: Zanella.

- [ ] **[SPRINT 02 — Vitória (Kneip)]** 18/03–01/04. C1: GS (minuta) + Canal (assinatura). Evento Apê Holding: 25/03. DRI: Kneip.

- [ ] **[WS6 — Embaixadoras]** Jade como participante. Programa estruturado? Embaixadoras ativas em cada praça? DRI: Diego.

- [ ] **[WS5 — Marketing Event Driven]** Calendário ativo. Método a definir. Depende de WS3 (eventos territoriais). DRI: Mayumi.

- [ ] **[PODCAST — Curitiba]** Material do podcast (4,5h de terça) — ativo do Projeto Autoridade Digital? DRI: Diego | Status: pendente definição.

- [ ] **[CURSO PNL — Módulo faltante]** Verificar módulos pendentes. DRI: Diego | Prazo: antes da próxima viagem.

- [ ] **[VPS Provider]** Provedor de cloud do VPS (diegodiehl.com) não confirmado. DRI: Diego | Prazo: a definir.

---

## ✅ RESOLVIDOS RECENTEMENTE

- [x] **threadBindings** — topics 9-13 → Morfeu | 14-15 → Larissa | 16 → Claudinei (05/04/2026)
- [x] **VPS Provider** — Hostinger confirmado (05/04/2026)
- [x] **GitHub sync** — master = default branch, sync-cerebro.sh corrigido (06/04/2026)
- [x] **6 jobs com erro** — modelo atualizado para M2.7 (LiveSessionModelSwitchError resolvido) (06/04/2026)

---

## 🛠 Scripts e Infra — Pendentes

- [ ] **[SCRIPT — generate_refresh_token.py]** Executar localmente com `client_secret.json` para gerar refresh token Google OAuth. DRI: Diego (ambiente local)
- [ ] **[SCRIPT — trinks_booking.py]** Definir `TRINKS_PASSWORD` na VPS para ativar agendamento automático de cabelo. DRI: Diego

---

*Revisado em 06/04/2026*

- [ ] **[TLDV — Cron Polling 6h]** Cron criado (e1ab5bf1) ✅ — vigiando se coleta roda a cada 6h
- [ ] **[TLDV — Webhook Server]** Servidor parou em 08/04 00:43. Precisa restart ou migrar para polling. DRI: Claudinei | Prazo: 10/04.
