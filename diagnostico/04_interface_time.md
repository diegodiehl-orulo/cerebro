# 04_INTERFACE_TIME.md — Interface com o Time
> **Diagnóstico:** Etapa 4 de 7
> **Auditor:** Morfeu
> **Base:** 02_governanca_workstreams.md + 03_operacao_externa.md + leitura de tl;dv processados, daily notes, pending.md, follow-up templates, atas e email scan
> **Anti-alucinação:** Dados reais de reuniões capturadas (tl;dv), emails detectados e pendências registradas. Nenhuma inferência sem evidência.

---

## 1. MAPA DOS RITUAIS

### 1.1 Rituais que existem e têm evidência de execução

| Ritual | Frequência | Participantes | Captura | Output real | Estado |
|--------|-----------|---------------|---------|-------------|--------|
| **1:1 Diego/Gustavo** | Semanal (aprox.) | Diego + Gustavo | tl;dv ativo | Itens de ação capturados | ✅ Existe e ocorre |
| **Semanal Comercial** | Semanal (seg 10h) | Diego + time comercial | tl;dv (parcial) | Números, ações, próximos passos | ✅ Existe e ocorre |
| **Diretoria: Alinhamento Semanal** | Semanal (seg 15h) | Diego + C-level | tl;dv | Múltiplos itens por liderança | ✅ Existe e ocorre |
| **CCR Corretores** | Semanal (seg 11h) | Diego + Ester | tl;dv | Ações Ester: conteúdo, follow-ups | ✅ Existe e ocorre |
| **Treinamento Comercial** | Semanal (qua 9h) | Diego + time | tl;dv | Metodologia PDR, perguntas, estrutura | ✅ Existe e ocorre |
| **Órulo & 5A** | Periódico | Marcus, João, Bruna | tl;dv | Ações técnicas (CRM, parceria) | ✅ Ocorre (parceria externa) |
| **Review Dev** | Semanal (seg 14h) | Diego + Alejandro | tl;dv (presumido) | Não capturado neste audit | ⚠️ Existe, captura incerta |
| **Reunião Zappa** | Pontual (13/03) | Diego + externos | Convite detectado no Gmail | Não processado | ⚠️ Detectado, sem cobertura |
| **Diego / Esdras** | Pontual (10/03) | Diego + Esdras | Convite detectado no Gmail | Não mapeado | ⚠️ Esdras não existe no sistema |

### 1.2 Rituais declarados na governança que NÃO têm evidência de execução

| Ritual | WS | Declarado em | Estado real |
|--------|----|-----------|----|
| **Kickoff WS1 CC** | WS1 | kickoff_prep.md + pending.md | ❌ Nunca realizado |
| **Kickoff WS2 CX** | WS2 | kickoff_prep.md + pending.md | ❌ Agendado para semana de 16/03 |
| **Kickoff WS3 FL** | WS3 | kickoff_prep.md + pending.md | ❌ Nunca realizado |
| **Kickoff WS4 CRM** | WS4 | kickoff_prep.md + pending.md | ❌ Nunca realizado |
| **Kickoff WS5 MKT** | WS5 | kickoff_prep.md + pending.md | ❌ Nunca realizado |
| **Kickoff WS6 EMB** | WS6 | kickoff_prep.md + pending.md | ❌ Nunca realizado |
| **Kickoff WS7 SL** | WS7 | kickoff_prep.md + pending.md | ❌ Nunca realizado |
| **Pulse quinzenal (qualquer WS)** | Todos | pulse_v0.md | ❌ Nenhum pulse preenchido |
| **Check-in sócio local (qua/sex)** | WS3 | pracas_sprint.md + crons | ❌ Cron ativo mas dados zerados |
| **One-Pager sprint (Zanella/Kneip)** | WS3 | cron_plan.yml | ❌ Nunca recebido via email watcher |

---

## 2. AVALIAÇÃO DE UTILIDADE PRÁTICA

### 2.1 O que funciona — rituais com valor real comprovado

**1:1 Diego/Gustavo (25/02)** — o ritual mais rico capturado no sistema:

Da transcrição tl;dv, em ~1h de reunião, foram gerados:
- **10+ itens de ação para Gustavo** com timestamp (limpeza CRM, onboarding Luan, funil de reestruturação, documento estratégico, filtros CRM, motivos de perda, envolver Paloma, envolver Mayumi)
- **1 item de ação para Diego** (enviar calendário de eventos)
- **Dados reais de conversão:** 14% com 74 reuniões → ~10 vendas. Ticket médio R$655, meta R$700
- **Dados reais de BDRs:** 62 agendamentos, 56 reuniões, 16% conversão (meta 15%), Jade 24 agendamentos em 2 meses, João Vitor 30 reuniões como closer

Este ritual **gera sinal real** e seria o insumo perfeito para o WS2 (DLs, conversão) e WS4 (CRM hygiene). Mas os itens de ação vão para uma mensagem no Telegram — e depois?

**Semanal Comercial** — também captura dados reais:
- BDRs com métricas
- Resultados de fevereiro
- Ações do time (Pedro, Luiz, Mirla)
- Decisões (envio de datas de eventos)

**CCR Corretores** — Ester recebe direção clara:
- Criar conteúdo educativo vídeo sobre CRM
- Follow-up corretores outubro
- Criar playlist YouTube treinamentos CRM
- Conversar com Bruno sobre CRM autônomos JP

### 2.2 O que não funciona — o gap entre ritual e accountability

**O problema central:** Os rituais acontecem, o tl;dv captura, o Morfeu processa e entrega via Telegram. **Mas não há rastreamento do que aconteceu com os itens de ação.**

Evidência concreta:
- O 1:1 de 25/02 gerou 10+ ações para Gustavo
- O Morfeu gerou um follow-up template (06/03) perguntando o status de: limpeza do CRM, estruturação do funil, plano B10, follow-up Mayumi, decisões pendentes
- O follow-up está em `memory/pending.md` como "AGUARDANDO TERCEIRO"
- **Não há evidência de que o email foi enviado nem de resposta de Gustavo**
- **Não há evidência de que o CRM foi limpo** (mencionado na reunião de 25/02 como pendência Gustavo)
- **Não há evidência de que a trilha de onboarding de Luan foi compartilhada** (item gerado em 25/02)

**Em 12 dias (25/02 → 08/03):** Nenhuma dessas ações foi verificada pelo sistema.

### 2.3 Os rituais são úteis ou burocráticos?

**Rituais existentes (1:1, Semanal, Diretoria, CCR):** `ÚTEIS` — geram dados reais, decisões reais, direções reais. O problema não é o ritual, é o pós-ritual.

**Rituais propostos nos WS (kickoffs, pulses):** `BUROCRÁTICOS` — ainda não existem na prática. São templates de documentos. Nenhum DRI os realizou.

**Conclusão crítica:** O sistema tem bons rituais operacionais (que acontecem). Tem maus rituais de governança (que não acontecem). E nenhum dos rituais operacionais alimenta os rituais de governança.

---

## 3. GARGALOS DE COORDENAÇÃO

### Gargalo 1: Diego como único conversor de sinal em ação
**O mais crítico do sistema.**

```
Reunião ocorre
    ↓ tl;dv captura
    ↓ Morfeu processa
    ↓ Telegram alerta Diego
    ↓ Diego precisa lembrar / agir / delegar
    ↓ Se Diego não agir → o item desaparece
```

Não há mecanismo automático de follow-up. Não há cobrança de DRI por item de ação. O Morfeu gera rascunhos, mas a execução depende integralmente de Diego decidir usar o rascunho.

**Exemplo real:** Follow-up do 1:1 Gustavo (06/03) está em `templates/drafts/` e `pending.md` como "AGUARDANDO TERCEIRO". Sem evidência de envio.

### Gargalo 2: Lara existe mas não opera
**Papel declarado:** Secretária executiva — executa envios, follow-ups, e-mails sob instrução de Diego.
**Papel real:** 1 job ativo (Smart Email Scan às 9h-17h). Não há e-mail enviado via Lara documentado no sistema. Não há "INSTRUÇÕES PARA LARA" gerada e executada com evidência de conclusão.

O pipeline declarado no AGENTS.md é:
```
Morfeu gera rascunho + INSTRUÇÕES PARA LARA
    → Diego diz "OK para enviar"
    → Lara executa via @larissa_personal_assistant_bot
```

Não há evidência desse pipeline em operação real. Os rascunhos existem. O "OK" não foi documentado. O envio não está registrado.

### Gargalo 3: Time sem canal com o sistema
Gustavo, Jade, Mirla, João Vitor, Luan, Ester, Mayumi, Kneip, Zanella — **nenhum deles tem canal com o Morfeu ou Lara**. Eles:
- Recebem direção nas reuniões (ao vivo, com Diego)
- Potencialmente receberão e-mails via Lara (não operacional ainda)
- **Não têm como reportar status, bloqueios ou atualizações ao sistema**

A única forma do sistema saber o que o time fez é:
1. Diego reportar manualmente
2. tl;dv capturar em reunião
3. Email chegar ao inbox de Diego

### Gargalo 4: Sócios locais fora do circuito
Zanella (Curitiba) e Kneip (Vitória) são tratados como executores do sprint — mas o circuito de comunicação é:
```
Morfeu gera check-in → Diego lê → Diego envia ao sócio → Sócio responde a Diego → Diego repassa ao Morfeu
```

O sócio nunca fala com o sistema. O one-pager deveria chegar por email (detectado pelo `sprint_email_watcher.py`), mas nunca chegou. O pipeline existe na teoria; na prática, a comunicação é informal (WhatsApp, ligação).

### Gargalo 5: Reunião "Zanella - Montar parceiros expandir PR" (09/03)
Agenda de amanhã mostra reunião com o sócio de Curitiba às 13:30. É uma reunião de trabalho real, mas:
- Não está no protocolo de sprint (não é check-in formal)
- Não está vinculada a nenhum C1/C2/C3
- Se o tl;dv não estiver ativo, o sistema não saberá o que foi discutido
- O Morfeu gerará check-in de Quarta às 09h — sem saber que já houve reunião às 13:30 de segunda

---

## 4. LACUNAS

| # | Lacuna | Impacto | WS / Ritual afetado |
|---|--------|---------|---------------------|
| 1 | **Nenhum sistema de rastreamento de itens de ação pós-reunião** | 🔴 CRÍTICO | Todos os rituais existentes |
| 2 | **Lara não opera o pipeline de envio de e-mails** | 🔴 ALTO | WS3 (cobranças sócio), Follow-ups |
| 3 | **Time sem canal de reporte ao sistema** | 🔴 ALTO | WS1–WS7 (pulses nunca preenchidos) |
| 4 | **Reunião Zanella (09/03) fora do protocolo** | 🟡 MÉDIO | WS3 FL |
| 5 | **Esdras não existe no sistema** | 🟡 MÉDIO | Contexto desconhecido |
| 6 | **Itens de ação de Gustavo (25/02) sem follow-up verificado** | 🟡 MÉDIO | WS2, WS4 (CRM limpeza) |
| 7 | **Eduardo não foi comunicado sobre DRI WS3** | 🟡 MÉDIO | WS3 FL |
| 8 | **Nenhum kickoff aconteceu** | 🟡 MÉDIO | Todos os WS |
| 9 | **Sócios locais nunca enviaram one-pager** | 🟡 MÉDIO | WS3, governança de praças |
| 10 | **"Reunião Zappa" (13/03) sem contexto** | 🟢 BAIXO | Não mapeado |
| 11 | **Proposta Z2A & EBS Engenharia sem rastreio** | 🟢 BAIXO | Oportunidade comercial em andamento |

---

## 5. RISCOS HUMANOS E OPERACIONAIS

### Risco 1 — Diego como gargalo de execução (CRÍTICO)
Diego é o único ponto de contato entre sistema e time. Ele:
- É o único que recebe alertas do Morfeu (Telegram)
- É o único que pode aprovar envios (Lara)
- É o único que repassa informações do time ao sistema
- É o único que pode iniciar qualquer ritual de WS

**Se Diego estiver em viagem, sobrecarregado ou simplesmente não agir sobre um alerta → o item morre.** Isso não é hipótese — é o padrão observado nos últimos 12 dias (itens de ação do 1:1 de 25/02 sem follow-up documentado).

### Risco 2 — Diego atuando como operador, não como sponsor (ALTO)
A análise das reuniões capturadas revela um padrão:
- **1:1 com Gustavo:** Diego é quem conduz, cobra, orienta o CRM, diz como limpar, define quem envolver (Paloma, Mayumi), decide sobre o funil. **Gustavo recebe direção, não a gera.**
- **CCR Corretores:** Diego diz a Ester o que criar, com quem falar, qual conteúdo fazer. **Ester executa por instrução, não por iniciativa própria com método.**
- **Treinamento Comercial:** Diego estrutura a metodologia, define os eixos do produto, cria o framework PDR. O time consome.

O papel de sponsor (prioridade, desbloqueio, arbitragem) está sendo exercido, mas o papel de **executivo operacional** também — gerando dependência estrutural do time em Diego para quase toda decisão de como fazer.

**Critério de avaliação (da própria governança, `workstreams.md`):** O DRI deve "garantir touch a cada 14 dias, preparar e publicar o WS Pulse no ciclo, manter backlog top 10 vivo, trazer bloqueios com clareza." Nenhum DRI está fazendo isso — e possivelmente porque Diego não pediu/cobrou formalmente.

### Risco 3 — Mayumi sobrecarregada de forma invisível (MÉDIO)
Mayumi é DRI de 4 WS simultâneos (WS1, WS3*, WS5, WS6). Mas:
- Não há nenhuma reunião com Mayumi capturada nas notas
- Não há nenhum item de ação de Mayumi registrado fora das CCR Corretores (onde Ester aparece mais)
- Não há evidência de que Mayumi foi comunicada sobre ser DRI de 4 WS

*WS3: na prática, agora é Eduardo — mas Mayumi não foi formalmente liberada.

### Risco 4 — Luan em onboarding sem sistema (MÉDIO)
Luan é closer novo, onboarding ativo. A reunião de 25/02 gerou: "Gustavo compartilhar trilha de onboarding para Luan até final do dia." Não há evidência de que a trilha foi compartilhada. Não há registro do onboarding no sistema do Morfeu. O closer está sendo integrado ao time comercial de forma completamente off-system.

### Risco 5 — Decisões estratégicas tomadas verbalmente (MÉDIO)
A reunião de Diretoria (Alinhamento Semanal, 02/03) gerou:
- Marcelo → iniciar reajuste de preços de clientes baratos
- Eduardo → organizar reunião com Quinto Andar
- Felipe/Eduardo → conversar com times sobre OKRs
- Diego → apresentar OKRs pro time na segunda

Nenhuma dessas decisões estratégicas tem registro no sistema do Morfeu além do resumo do tl;dv. Não está em `decisions.md`. Não está em `pending.md`. Se Diego não reportou, o Morfeu não sabe.

### Risco 6 — Conversão de reunião em ação sem fechamento (MÉDIO)
Padrão detectado em todos os rituais capturados:
```
Reunião → itens de ação gerados → tl;dv email → Morfeu processa → Telegram
         ↕
         Sem: prazo, dono formal, critério de "feito", próximo check-in
```

Os itens de ação do tl;dv não têm estrutura de accountability (dono + prazo + critério). São listas informais. Nenhum DRI os incorpora ao pulse do WS.

---

## 6. DIAGNÓSTICO FINAL — AS 5 PERGUNTAS

**O sistema gera próxima ação clara?**
Parcialmente. O tl;dv gera itens de ação capturados. O Morfeu os processa e entrega via Telegram. Mas "próxima ação clara" pressupõe dono + prazo + verificação — e nenhum desses três elementos é sistemático.

**Os rituais são úteis ou burocráticos?**
Os rituais existentes (1:1, Semanal, Diretoria, CCR) são úteis e geram dados reais. Os rituais propostos nos WS (kickoffs, pulses) são burocráticos — existem no papel e nunca foram realizados.

**O time sabe o que fazer após cada ritual?**
Sim, verbalmente. As reuniões geram direção clara. Mas não há sistema de rastreamento. O que foi definido em reunião não aparece em nenhum artefato de WS. O time sabe o que fazer na semana seguinte à reunião — e provavelmente esquece na semana seguinte.

**Há dependência excessiva de alinhamento verbal?**
Sim. A Órulo opera predominantemente por alinhamento verbal (reuniões + WhatsApp), com tl;dv como único registro. Documentação é esparsa e não retroalimenta nenhum ritual de governança. O Morfeu captura o verbal mas não o converte em sistema.

**O diretor está atuando como sponsor/controller ou caindo em microgestão?**
Oscila entre os dois, com tendência para o segundo. Em reuniões de 1:1 e CCR, Diego instrui operação (como limpar CRM, o que criar, com quem falar) em vez de cobrar de DRIs que tragam bloqueios e decisões. A consequência estrutural é que o time opera por instrução de Diego, não por método autônomo.

---

## 7. INSUMOS PARA A ETAPA 5 — INFRAESTRUTURA DO AGENTE

Com base nos gargalos identificados, a Etapa 5 deve avaliar se a infraestrutura do agente (jobs, prompts, memória, modelos) está calibrada para resolver — ou está amplificando — os problemas detectados:

1. **Jobs de praças estão ativos mas sem dados.** Estão consumindo recursos e gerando alertas baseados em `[PREENCHER]`. Qual o custo real de manter 10+ jobs de governança rodando sobre dados vazios?

2. **O pipeline tl;dv → ação é o mais valioso do sistema.** Mas tem gaps. Os jobs de tl;dv estão calibrados para capturar as reuniões certas (1:1, Semanal Comercial, CCR)?

3. **A memória captura itens de ação de reuniões?** O `tldv_actions/` tem 4 arquivos de 06/03. O `daily/` captura sínteses. Mas os itens de ação não viram pendências estruturadas automaticamente.

4. **Lara tem 1 job ativo (Smart Email Scan).** Se o papel dela é executar envios, por que o único job ativo é de leitura?

5. **A cobrança automática de DRIs é possível com a infra atual?** O sistema tem jobs para cobrar sócios locais. Mas não tem jobs para cobrar Gustavo (WS2/WS4 DRI), Mayumi (WS1/WS5/WS6 DRI), ou Eduardo (WS3 novo DRI). Por quê?

6. **O heartbeat de 90 min está gerando valor?** Ele verifica pendências e projetos. Mas com projetos/WS todos em estado "PRONTO — realizar kickoff", o que o heartbeat entrega?

---

*Etapa 4 concluída. Próxima: `05_infra_agente.md`*
