# 03_OPERACAO_EXTERNA.md — Camada Externa de Operação
> **Diagnóstico:** Etapa 3 de 7
> **Auditor:** Morfeu
> **Base:** 01_inventario_sistema.md + 02_governanca_workstreams.md + sondagem real de integrações (gcalcli, Gmail, tl;dv, contratos, smart email scan)
> **Anti-alucinação:** Dados reais verificados via execução de scripts. Nenhuma afirmação sem evidência.

---

## 1. MAPA DA CAMADA EXTERNA

A camada externa é o conjunto de ferramentas fora do OpenClaw/workspace que deveriam sustentar a operação da Órulo. Abaixo, o mapa do que existe, o que está conectado e o que é caixa-preta.

| Ferramenta | Tipo | Conexão com Morfeu | Acesso real | Escrita | Estado |
|-----------|------|-------------------|-------------|---------|--------|
| **Google Calendar** | Agenda | ✅ Bidirecional (gcalcli) | Leitura de eventos real | Criação de eventos (script) | `ESTRUTURA VÁLIDA` |
| **Gmail (leitura)** | E-mail | ✅ OAuth configurado | Scan de inbox real | — | `ESTRUTURA VÁLIDA` |
| **Gmail (envio)** | E-mail | ✅ OAuth configurado | Envio via script | Sim (com OK Diego) | `EXISTE, MAS ESTÁ INSUFICIENTE` |
| **tl;dv** | Transcrição reuniões | ✅ Parcial (email-based) | Leitura via Gmail | — | `EXISTE, MAS ESTÁ INSUFICIENTE` |
| **Clicksign** | Assinatura contratos | ✅ Passivo (email-based) | Notificações via Gmail | — | `EXISTE, MAS ESTÁ INSUFICIENTE` |
| **Bitrix24** | CRM operacional | ❌ Zero integração técnica | Nenhum | Nenhum | `LACUNA CRÍTICA` |
| **Google Drive** | Documentos da Órulo | ❌ Zero integração técnica | Nenhum | Nenhum | `LACUNA CRÍTICA` |
| **Z2A (WhatsApp IA)** | Comunicação corretores | ❌ Zero integração técnica | Nenhum | Nenhum | `LACUNA` |
| **WhatsApp (time)** | Comunicação interna | ❌ Zero integração | Nenhum | Nenhum | `LACUNA` |
| **Vaultwarden** | Credenciais | ✅ Configurado | Cofre acessível | Sim | `ESTRUTURA VÁLIDA` |
| **Telegram** | Output principal | ✅ Nativo OpenClaw | Total | Sim | `ESTRUTURA VÁLIDA` |
| **Trinks** | Agendamento pessoal | ✅ Script ativo | Leitura de slots | Futuro | `EXISTE, MAS ESTÁ INSUFICIENTE` |
| **Backup (local)** | Snapshot workspace | ✅ Cron diário | Backup real | Sim | `ESTRUTURA VÁLIDA` |

---

## 2. ANÁLISE DETALHADA POR FERRAMENTA

---

### 2.1 Google Calendar
**Estado:** `ESTRUTURA VÁLIDA`

**Evidência real:** Script gcalcli funcional. Leitura de agenda real de Diego:
- **Amanhã (09/03 — segunda):**
  - 06:00 — Treinar
  - 07:30 — S.A.V.E.R.S + Visualização
  - 09:00 — Z2A & Orulo | Comercial
  - 10:00 — Semanal Comercial - CRI
  - 11:00 — CCR Corretores
  - 13:30 — Zanella - Montar parceiros expandir PR
  - 14:00 — Review Dev
  - 15:00 — Diretoria: Alinhamento Semanal
  - 17:45 — Análise

**Coerência com governança:** Parcial. Os rituais de WS (kickoffs, pulses) não aparecem na agenda — nenhum deles está agendado. A agenda mostra reuniões operacionais fixas (Semanal Comercial, Diretoria, CCR Corretores, Review Dev) mas nenhuma é um ritual formal de WS.

**Gap crítico:** Reunião "Zanella - Montar parceiros expandir PR" (13:30 de segunda) — é o sócio local de Curitiba. Existe reunião com o sócio na agenda, mas o sistema de governança de praças não sabe disso. Se o tl;dv não estiver ativo nessa reunião, o Morfeu não captura o conteúdo.

**Observação:** Existe uma reunião "Diego / Esdras" agendada para ter. 10 mar. (detectada via email). Esdras não aparece em nenhum documento do sistema. Reunião não mapeada.

---

### 2.2 Gmail
**Estado:** `ESTRUTURA VÁLIDA` para leitura passiva. `EXISTE, MAS ESTÁ INSUFICIENTE` para uso ativo.

**Evidência real (smart_email_scan — últimas 48h):**
- **86 emails scaneados | 33 classificados como importantes**
- **Contratos (4):** Clicksign — "Termo de DA V.2026 - Cobra Engenharia" (pendente assinatura cliente), "Contrato Canal Órulo/z2" (minuta)
- **Propostas (6):** Z2A & EBS Engenharia (thread ativa — Tayna Teodoro / z2app.com.br), propostas de lorena e Wellyngton via Órulo
- **Reuniões (4):** "Reunião Zappa - sex. 13 mar." (convite), "Diego / Esdras - ter. 10 mar.", notas tl;dv de "1:1 Diego-Gustavo" e "Funil CRI"
- **Time (19):** Emails de Diego para ele mesmo (auto-envios) predominam — 19 de 86 são do próprio diego.diehl@orulo.com.br

**Achado crítico — "Sistema Operacional Órulo":** Um documento foi compartilhado via Google Docs com Diego (remetente: `drive-shares-dm-n`) com título **"Sistema Operacional Órulo — Base do Projeto"**. Este é provavelmente um dos 16 documentos estratégicos da Órulo que deveriam estar em `biblioteca/orulo/` — mas o Morfeu não tem acesso. Chegou via email, não foi importado.

**Achado — Proposta Z2A & EBS Engenharia:** Thread ativa com Tayna Teodoro (z2app.com.br) sobre proposta. Aparece no email scan como importante. Nenhum rastro desta negociação no sistema do Morfeu (CRM, pending, projects).

**Gap crítico:** O email scan identifica sinais, mas não os converte em ação estruturada. Não há pipeline de "email capturado → pendência criada → responsável notificado".

---

### 2.3 tl;dv
**Estado:** `EXISTE, MAS ESTÁ INSUFICIENTE`

**Evidência real:**
- **25 IDs de reuniões no `tldv_processed.json`** — mas o arquivo contém apenas IDs (hashes), não títulos ou conteúdo
- **tldv_latest.json:** Última reunião processada = "Gustavo / Diego" (25/02/2026) — há 12 dias
- **Emails recentes com tl;dv:** "1:1 - Diego - Gustavo" e "Funil CRI" (detectados no smart_email_scan) — não foram processados ainda
- **tldv_pending.json:** Zerado em 07/03 (arquivo de 49KB foi arquivado — backlog acumulado que causava lentidão)
- **tldv_store/:** Diretório criado em 06/03, com subpasta "2026-03-06" — aparentemente reunião do Mkt + Comercial

**O que funciona:** Detecção de emails tl;dv via Gmail → flag para processamento. Pipeline `tldv_enrich.py` rodando.

**O que não funciona:**
- Reuniões recentes ("1:1 Diego-Gustavo", "Funil CRI") detectadas no email mas não processadas (pending foi zerado em 07/03)
- O pipe email → pending → processamento tem latência e gaps
- Reunião "Zanella - Montar parceiros" (agenda de amanhã) — se não tiver tl;dv ativo, sumirá

**Lacuna fundamental:** tl;dv só funciona se estiver ativo na reunião. Reuniões por WhatsApp, telefone ou presenciais são invisíveis ao sistema.

---

### 2.4 Clicksign / Contratos
**Estado:** `EXISTE, MAS ESTÁ INSUFICIENTE`

**Evidência real:**
- **1 contrato pendente (06/03):** "ÓRULO SISTEMAS DE INFORMAÇÃO.pdf" — aguardando assinatura do cliente (prazo: 18/03/2026)
- **`contratos_pendentes.json` (40KB):** Arquivo maior com histórico mais extenso (gerado em 06/03)
- **Script `verifica_contratos_pendentes.py` rodando** diariamente às 11:20

**Coerência com governança:** Zero. O WS4 (Estrutura Comercial & CRM) deveria tratar contratos — mas o script de contratos é um processo independente sem conexão com rituais de WS.

**Gap:** O script detecta contratos mas não há pipeline de cobrança estruturada a partir dele. O dado chega ao Morfeu, mas a ação depende de Diego agir sobre ele manualmente.

---

### 2.5 Bitrix24
**Estado:** `LACUNA CRÍTICA`

**Evidência:** Zero integração técnica. Nenhum script, nenhuma API key, nenhuma conexão. O Bitrix é o CRM operacional da Órulo — onde estão todos os deals, DLs, histórico comercial, pipeline de closers.

**O que o Morfeu sabe sobre o Bitrix:**
- Que ele existe (mencionado em AGENTS.md, USER.md, WS4 charter)
- Que a regra é "Morfeu lê e reporta. Não edita." (AGENTS.md)
- Que o WS4 depende de higiene do Bitrix para funcionar

**O que o Morfeu NÃO sabe:**
- Quantos deals existem no funil
- Quais deals estão sem próxima ação
- Quais DLs estão em que estágio (o WS2 precisa disso)
- Se houve handoff BDR → Closer essa semana
- Qualquer coisa sobre o pipeline real

**Impacto na governança:** WS2 (Jornada DL→Pago) e WS4 (Estrutura Comercial & CRM) dependem do Bitrix para existir. Sem leitura do Bitrix, o Morfeu não pode gerar relatório de pipeline, cobrar higiene de CRM ou validar se o WS4 está cumprindo seu "feito é".

**Risco:** O único sinal que chega sobre deals é via email (ex: propostas via Clicksign, notificações da plataforma Órulo). Isso é ruído, não dado estruturado.

---

### 2.6 Google Drive
**Estado:** `LACUNA CRÍTICA`

**Evidência:** Zero integração técnica. A pasta `docs/integrations-setup.md` menciona `gog drive ls` como possibilidade futura — não implementado.

**O que existe no Drive (inferido dos emails):**
- **"Sistema Operacional Órulo — Base do Projeto"** — compartilhado com Diego recentemente. Provavelmente a base dos 16 documentos estratégicos que deveriam estar em `biblioteca/orulo/`.
- Documentos de incorporadoras (implicados pelo WS6 — problema central é o Google Drive como fonte de verdade)
- Materiais de apresentação, planilhas de controle (inferidos de reuniões e contexto do WS4)

**Impacto na governança:**
- WS6 (Embaixadoras) tem como **problema central** o fato de incorporadoras usarem Google Drive em vez da Órulo/Portal. O Morfeu não enxerga esse Drive. Não pode validar se incorporadoras estão ou não drive-free.
- Os 16 documentos estratégicos da Órulo (playbooks, SDR, kits) estão no Drive — mas o Morfeu opera sem eles.

---

### 2.7 Z2A (WhatsApp IA Comercial)
**Estado:** `LACUNA`

**Evidência:** Mencionado extensamente em USER.md (produto da Órulo), no WS1 charter (métrica de impactos + respostas Z2A), e em uma proposta de negócios ativa (Z2A & EBS Engenharia). O Morfeu não lê nem escreve no Z2A.

**Impacto:** WS1 (Comunicação Corretores) tem como métrica soberana "impactados + respostas via Z2A". O Morfeu não tem como verificar essa métrica. Todo o "feito é" do WS1 depende de Ester ou Mayumi reportarem manualmente.

---

### 2.8 WhatsApp (Time)
**Estado:** `LACUNA`

**Evidência:** Canal de comunicação do time listado como "a definir" em AGENTS.md. Na prática, o time provavelmente se comunica via WhatsApp (grupos internos). O Morfeu tem zero acesso.

**Impacto:** Decisões, bloqueios, updates e follow-ups do time provavelmente acontecem no WhatsApp e são invisíveis ao sistema. O Morfeu captura via tl;dv (reuniões) e Gmail (e-mails formais), mas perde toda a comunicação informal.

---

## 3. COERÊNCIAS E INCOERÊNCIAS

### Coerências encontradas

✅ **Google Calendar ↔ Daily Briefing:** O cron de Daily Briefing (08:45, seg-sex) usa gcalcli para ler a agenda de Diego e entregar o contexto do dia. A integração funciona e entrega valor real.

✅ **Gmail ↔ Smart Email Scan:** O cron de Smart Email Scan (9h-17h, 2h, seg-sex) lê Gmail e classifica emails por tipo (contratos, propostas, reuniões). Funcionando e entregando alertas.

✅ **Gmail ↔ Clicksign:** O script `verifica_contratos_pendentes.py` detecta notificações de contratos via Gmail e gera relatório. Pipeline real e ativo.

✅ **tl;dv ↔ Morfeu (parcial):** Pipeline de detecção de reuniões via email tl;dv existe e processa. Últimas 25 reuniões foram capturadas (mesmo que parcialmente).

### Incoerências críticas

❌ **WS2 + WS4 precisam do Bitrix. Bitrix não existe para o Morfeu.**
Os dois workstreams com maior dependência de dados de CRM (WS2 = 1268 DLs, WS4 = higiene) são completamente opacos. Os planos de sprint dessas WSs listam "levantamento no Bitrix" como C1 — mas quem fará esse levantamento não é o agente, é o humano (Gustavo/BDRs). O Morfeu receberá um relatório manual, se e quando vier.

❌ **WS1 usa Z2A como métrica. Z2A não existe para o Morfeu.**
O "feito é" do WS1 é medido por impactados + respostas via Z2A. O Morfeu não lê Z2A. Qualquer evidência de execução do WS1 depende de Ester/Mayumi reportar no pulse — que ainda é um template vazio.

❌ **WS6 combate o Google Drive. O Morfeu não vê o Google Drive.**
O problema central do WS6 é que incorporadoras usam Drive em vez da Órulo. A métrica soberana é "% drive-free por praça". O Morfeu não pode auditar isso — não tem acesso ao Drive de nenhuma incorporadora.

❌ **Reunião com Zanella amanhã (09/03) sem cobertura.**
O calendário mostra "Zanella - Montar parceiros expandir PR" (13:30, segunda). É o sócio de Curitiba. O sistema de governança de praças tem 10+ jobs ativos para monitorar Curitiba — mas se o tl;dv não estiver ativo nessa reunião, o conteúdo se perde completamente.

❌ **"Sistema Operacional Órulo" compartilhado mas não importado.**
Um documento estratégico da Órulo foi compartilhado com Diego via Google Docs. O Morfeu detectou via email mas não tem acesso ao conteúdo. Os 16 docs da Órulo continuam inacessíveis.

---

## 4. PRINCIPAIS CONFUSÕES ESTRUTURAIS

**Confusão 1: O que é fonte da verdade?**
A Órulo tem múltiplas fontes de verdade potenciais, sem hierarquia clara:
- Bitrix (CRM operacional — mais completo, inacessível ao Morfeu)
- Google Sheets / Drive (planilhas de controle — inacessíveis ao Morfeu)
- Emails (sinais passivos — capturados parcialmente)
- Workspace do Morfeu (documentação — sem dado real)
- Memória verbal de Diego (mais completo de todos — mas mortal e inconsistente)

Nenhuma dessas fontes é canônica para o agente. O Morfeu opera sobre o que Diego decide falar.

**Confusão 2: tl;dv como pipeline estratégico**
O tl;dv captura reuniões e as entrega como notas via email. O pipeline existe e funciona. Mas:
- A reunião precisa ter tl;dv ativo (não é garantido)
- Reuniões presenciais/WhatsApp/informais são perdidas
- O conteúdo processado vai para Telegram mas não alimenta nenhum artefato de WS

O tl;dv é tratado como broadcast, não como input para governança.

**Confusão 3: Contratos sem dono**
O script de contratos detecta pendências. O Morfeu gera relatório. Mas não há pipeline: quem age sobre um contrato pendente? Não há DRI de contratos. WS7 é sobre modelo econômico, não sobre execução de contratos. WS4 é sobre CRM, não sobre contratos. Os contratos detectados ficam em um JSON sem downstream definido.

**Confusão 4: O time existe fora do sistema**
Gustavo, Jade, Mirla, João Vitor, Luan, Ester, Mayumi, Kneip, Zanella — todos estão listados nos documentos do Morfeu, mas nenhum tem canal com o agente. O time opera em seus próprios canais (WhatsApp, Bitrix, Google Meet) e o Morfeu não enxerga isso. A única janela é tl;dv + Gmail — ambas passivas.

---

## 5. LACUNAS OPERACIONAIS

| # | Lacuna | Ferramentas afetadas | WS afetado | Impacto |
|---|--------|---------------------|-----------|---------|
| 1 | **Bitrix24 sem integração** | Bitrix24 | WS2, WS4 | Pipeline comercial invisível. Qualquer dado de CRM é estimativa. |
| 2 | **Google Drive sem integração** | Google Drive | WS6, biblioteca/orulo | 16 docs da Órulo inacessíveis. Drive de incorporadoras inaudível. |
| 3 | **Z2A sem leitura** | Z2A / WhatsApp | WS1 | Métrica soberana de WS1 não verificável pelo agente. |
| 4 | **WhatsApp do time inacessível** | WhatsApp | Todos | Comunicação informal do time = caixa-preta. |
| 5 | **tl;dv não cobre reuniões informais/presenciais** | tl;dv | WS3 (praças) | Interações com sócios locais fora do Meet são perdidas. |
| 6 | **Email scan sem downstream para WS** | Gmail | Todos | Sinais capturados não alimentam rituais de WS nem pendências automaticamente. |
| 7 | **Contratos sem DRI de ação** | Clicksign | WS7 (indireto) | Contrato detectado não tem pipeline de encaminhamento. |
| 8 | **Dashboards externos inexistentes** | Google Sheets / Data Studio | WS2, WS4 | Nenhum painel de MRR, DLs, funil ou pipeline existe no sistema. |
| 9 | **Playbooks externos não importados** | Google Drive | Todos | Morfeu sem acesso a playbooks de SDR, kits comerciais, visão da Órulo. |
| 10 | **Agenda sem rituais de WS** | Google Calendar | Todos | Nenhum kickoff, pulse ou reunião de WS está agendado. |

---

## 6. RISCOS OPERACIONAIS

| Risco | Severidade | Descrição |
|-------|-----------|-----------|
| **Pipeline comercial invisível** | 🔴 CRÍTICO | WS2 e WS4 dependem do Bitrix para existir. Sem integração, qualquer relatório de pipeline é estimativa baseada em input manual. |
| **Reunião com Zanella amanhã sem cobertura** | 🔴 ALTO | Sócio local de Curitiba tem reunião na agenda (09/03 13:30). Se tl;dv não estiver ativo, o conteúdo se perde. Os jobs de praças não saberão o que foi discutido. |
| **16 docs da Órulo inacessíveis** | 🟡 MÉDIO | O "Sistema Operacional Órulo" e outros docs estratégicos estão no Drive. O Morfeu opera sem o playbook da empresa que representa. |
| **Proposta Z2A & EBS Engenharia sem rastreio** | 🟡 MÉDIO | Thread ativa no Gmail (Tayna Teodoro / z2app.com.br). Negociação B2B em andamento, sem rastro no sistema do Morfeu. |
| **Contrato pendente (Cobra Engenharia)** | 🟡 MÉDIO | Termo de DA vence 18/03/2026. Detectado pelo script. Nenhuma cobrança formal ativa para o signatário. |
| **Morfeu como gargalo único de interface** | 🟡 MÉDIO | Diego é o único ponto de contato entre o time e o agente. Qualquer dado que Diego não reportar, o Morfeu não saberá. Risco de gargalo humano crítico. |
| **tl;dv pendente zerado (07/03)** | 🟡 MÉDIO | Backlog acumulado foi arquivado. Reuniões novas ("1:1 Diego-Gustavo", "Funil CRI") detectadas no Gmail mas não processadas ainda. |
| **WhatsApp como canal real do time** | 🟢 BAIXO | Provavelmente o principal canal de comunicação interna da Órulo. Zero visibilidade para o Morfeu — mas baixo porque é esperado dada a ausência de integração declarada. |

---

## 7. INSUMOS PARA A ETAPA 4 — INTERFACE COM O TIME

A Etapa 3 confirmou que a camada externa é fortemente passiva e Diego-centrada. Para entender como o time se relaciona com o sistema, a Etapa 4 deve investigar:

1. **O que o time recebe hoje do Morfeu (direta ou indiretamente)?**
   Há e-mails enviados via Lara? Follow-ups que chegaram ao Gustavo, Zanella, Kneip?

2. **O que o time sabe sobre o sistema de agentes?**
   Mayumi, Ester, Gustavo, BDRs — sabem que o Morfeu existe? Interagem com outputs do agente?

3. **O pipeline Morfeu → Diego → Time funciona?**
   Quando Morfeu gera rascunho + INSTRUÇÕES PARA LARA, isso chega ao time? Há evidência de e-mail enviado?

4. **A reunião "Zanella - Montar parceiros expandir PR" (09/03) é gerida como sprint?**
   Ou é uma reunião ad-hoc fora do protocolo de governança de praças?

5. **O tl;dv está ativo nas reuniões corretas?**
   Quem ativa o tl;dv? É sistemático ou depende de Diego lembrar?

6. **O que o time usa como fonte da verdade para tomar decisões?**
   Bitrix? WhatsApp? Reunião semanal? E-mail? Planilha? O Morfeu espelha isso?

---

*Etapa 3 concluída. Próxima: `04_interface_time.md`*
