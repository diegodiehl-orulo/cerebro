# 02_GOVERNANCA_WORKSTREAMS.md — Auditoria de Governança
> **Diagnóstico:** Etapa 2 de 7
> **Auditor:** Morfeu
> **Base:** 01_inventario_sistema.md + leitura direta de todos os 7 charters, backlogs, planos de sprint, kickoff_preps, pulses e HARMONIZACAO_FINAL.md
> **Anti-alucinação:** Nenhuma afirmação sem evidência de arquivo lido.
> **Classificação adotada:** A (Pronto e operacional) / B (Pronto mas não executado) / C (Estrutura parcial, execução zero) / D (Estrutura com inconsistência crítica) / E (Apenas nome — sem estrutura real)

---

## 1. TABELA-RESUMO DOS 7 WORKSTREAMS

| WS | Nome curto | DRI declarado | DRI real (decisions.md) | Estrutura doc. | Kickoff realizado | Pulse gerado | Touch tracking | Classificação |
|----|-----------|---------------|------------------------|---------------|-------------------|-------------|----------------|---------------|
| **WS1 CC** | Comunicação Corretores | Mayumi | Mayumi | ✅ Completa | ❌ Não | ❌ Vazio | ❌ `[PREENCHER]` | **B** |
| **WS2 CX** | Jornada DL → Pago | Gustavo | Gustavo | ✅ Completa | ❌ Não | ❌ Vazio | ❌ `[PREENCHER]` | **B** |
| **WS3 FL** | Fórmula Lançamento / Praças | Mayumi | **Eduardo** ⚠️ | ✅ Completa + extra | ❌ Não | ❌ Vazio | ❌ `[PREENCHER]` | **D** |
| **WS4 CRM** | Estrutura Comercial & CRM | Gustavo | Gustavo | ✅ Completa | ❌ Não | ❌ Vazio | ❌ `[PREENCHER]` | **B** |
| **WS5 MKT** | Marketing e Conteúdo | Mayumi | Mayumi | ✅ Completa | ❌ Não | ❌ Vazio | ❌ `[PREENCHER]` | **B** |
| **WS6 EMB** | Embaixadoras Drive-Free | Mayumi | Mayumi | ✅ Completa + extra | ❌ Não | ❌ Vazio | ❌ `[PREENCHER]` | **B** |
| **WS7 SL** | Modelo Econômico Sócio-Local | Eduardo + Felipe | **Diego** ⚠️ | ✅ Completa | ❌ Não | ❌ Vazio | ❌ `[PREENCHER]` | **D** |

> **Definição de cada nota:**
> - **A:** Pronto + executando + evidências vivas → não existe nenhum neste portfólio
> - **B:** Estrutura completa + não executado + sem inconsistência
> - **C:** Estrutura parcial + sem execução
> - **D:** Estrutura completa + inconsistência crítica não resolvida nos arquivos
> - **E:** Apenas nome — sem estrutura real

---

## 2. LEITURA POR WORKSTREAM

---

### WS1 CC — Comunicação com Corretores
**Nota: B**

**Estrutura documental:**
- `charter.md` ✅ — completo, com problema declarado, mecanismo de valor, DRI/Executor/Sponsor, fronteiras, rituais, evidência mínima, riscos
- `plan_quinzenal_sprint01.md` ✅ — C1/C2/C3 definidos com dono e prazo
- `backlog.md` ✅ — 10 itens com prioridade e sprint
- `kickoff_prep.md` ✅ — perguntas obrigatórias, pré-work, outputs
- `pulse_v0.md` ✅ — template pronto, mas **100% vazio** (zero dados)
- `onepage.md` ✅ — existência confirmada

**Touch tracking:** Todos os campos `[PREENCHER]` — `last_live_touch`, `last_pulse`, `days_since_touch`, `next_touch_due` sem data.

**Operacional:** Zero evidência de execução. Nenhuma comunicação realizada, nenhum envio Z2A registrado, WAU baseline não medido.

**Coerência interna:** Alta. Charter, plano e backlog estão alinhados entre si. Fronteiras com WS3 e WS5 definidas e sem sobreposição.

**Útil ou documental?** Documental. O artefato é de alta qualidade, mas não tem toque de realidade. A pergunta "qual foi o último envio para corretores?" não tem resposta no sistema.

**Risco específico:** Mayumi é DRI de WS1, WS3, WS5 e WS6 simultaneamente — 4 workstreams no Bloco A. Risco de sobrecarga aceito por Diego, mas não mitigado estruturalmente. Se Mayumi travar, 4 WS param.

---

### WS2 CX — Jornada DL → Pago
**Nota: B**

**Estrutura documental:**
- `charter.md` ✅ — completo, com separação clara WS2/WS4, indicadores operacionais definidos, trilha mínima declarada
- `plan_quinzenal_sprint01.md` ✅ — C1/C2/C3 claros: trilha mínima (Gustavo, dia 7), mapeamento de DLs (BDRs, dia 10), ritual quinzenal (Gustavo, dia 14)
- `backlog.md` ✅ — 10 itens
- `kickoff_prep.md` ✅
- `pulse_v0.md` ✅ — template pronto, 100% vazio
- `onepage.md` ✅

**Touch tracking:** Todos `[PREENCHER]`.

**Dado real disponível:** Baseline de 1268 DLs declarado no charter. Todo o resto (DLs em contato, com próximo passo, com valor entregue, avançados) marcado como `[levantamento]`.

**Operacional:** Zero evidência de execução. Trilha mínima DL→Pago não existe como playbook vivo — está declarada como meta do Sprint 01, mas Sprint 01 não rodou.

**Coerência interna:** Alta. Separação WS2 (jornada) vs WS4 (infraestrutura) é consistente e explícita.

**Útil ou documental?** Documental. O único dado concreto é o baseline de 1268 DLs. O kickoff WS2 CX com Gustavo está agendado para a semana de 16/03 (lembrete no sistema) — é o WS mais próximo de sair do papel.

**Risco específico:** WS2 depende de WS4 (CRM saudável). Se WS4 não fizer higiene do Bitrix primeiro, WS2 roda sobre dados ruins.

---

### WS3 FL — Fórmula de Lançamento / Praças
**Nota: D** ⚠️ INCONSISTÊNCIA CRÍTICA

**Estrutura documental:** A mais rica do portfólio.
- `charter.md` ✅
- `plan_quinzenal_sprint01.md` ✅
- `backlog.md` ✅
- `kickoff_prep.md` ✅
- `pulse_v0.md` ✅ — template pronto, 100% vazio
- `onepage.md` ✅
- `governance/pracas_sprint.md` ✅ — documento operacional complementar (v2.0)
- `memory/projects_orulo.md` ✅ — tracking por praça (incompleto)

**Inconsistência crítica — DRI:**
- `charter.md` declara DRI = **Mayumi**
- `decisions.md` (08/03/2026) registra decisão explícita: *"WS3 FL: Mayumi sai como DRI. Eduardo assume."*
- O charter **não foi atualizado**. O documento mais lido pelo time contradiz a decisão mais recente.

**Touch tracking:** Todos `[PREENCHER]`. Os jobs de governança de praças (pulse 2x/semana, check-in quarta/sexta) estão ativos nos crons, mas nunca rodaram com dados reais — `projects_orulo.md` tem todos os C1/C2/C3 como "a definir".

**Operacional:** É o único WS com infraestrutura de agente associada (10+ jobs, 14 prompts). Mas toda essa máquina está rodando em vazio: sem C1/C2/C3 reais, sem one-pager recebido, sem fase do sprint definida.

**Útil ou documental?** Híbrido — tem mais estrutura operacional que qualquer outro WS, mas a parte de dados (o que o sócio está executando) está zerada.

**Risco específico:** Máquina de governança (jobs) ligada, dados apagados. Toda cobrança automatizada está baseada em `[PREENCHER]`. O sistema cria ruído sem sinal.

---

### WS4 CRM — Estrutura Comercial & CRM
**Nota: B**

**Estrutura documental:**
- `charter.md` ✅ — completo, com indicadores operacionais, separação clara de escopo
- `plan_quinzenal_sprint01.md` ✅
- `backlog.md` ✅
- `kickoff_prep.md` ✅
- `pulse_v0.md` ✅ — 100% vazio
- `onepage.md` ✅

**Touch tracking:** Todos `[PREENCHER]`.

**Operacional:** Zero evidência de execução. O Bitrix24 não tem integração técnica com o Morfeu — é caixa-preta. Higiene do CRM, handoff BDR→Closer e cadências SDR são metas do Sprint 01, mas não existe registro de que Sprint 01 rodou.

**Coerência interna:** Alta. Fronteira WS2/WS4 bem definida e consistente nos dois charters.

**Útil ou documental?** Documental. O WS existe para garantir que o CRM funcione — mas o agente não lê o CRM. Qualquer relatório sobre pipeline é baseado em input manual de Diego.

**Risco específico:** Gustavo é DRI de WS2 e WS4 simultaneamente (Bloco B). Dois rituais quinzenais com time, preparação e evidência. Mesmo problema de Mayumi: se Gustavo travar, 2 WS param.

---

### WS5 MKT — Marketing e Conteúdo
**Nota: B**

**Estrutura documental:**
- `charter.md` ✅ — mais enxuto que os anteriores, mas coerente
- `plan_quinzenal_sprint01.md` ✅
- `backlog.md` ✅
- `kickoff_prep.md` ✅
- `pulse_v0.md` ✅ — 100% vazio
- `onepage.md` ✅

**Touch tracking:** Todos `[PREENCHER]`.

**Operacional:** Zero evidência de execução. Nenhum ativo gerado, nenhum evento documentado, nenhuma publicação registrada.

**Coerência interna:** Alta. Escopo é intencionalmente restrito para H1 (event-driven, sem always-on). Charter é honesto sobre limitações.

**Útil ou documental?** Documental. WS5 é o mais dependente de outros WS (depende de WS3 para ter eventos para transformar em ativos). Se WS3 não executa, WS5 não tem insumo.

**Observação:** O Projeto Autoridade Digital de Diego (marca pessoal, LinkedIn 3x/semana, Instagram 4x/semana) é mencionado no USER.md como objetivo pessoal — mas não aparece como workstream nem como iniciativa dentro do WS5. Há um gap entre o projeto pessoal de Diego e a governança do WS5.

---

### WS6 EMB — Programa de Incorporadoras Embaixadoras
**Nota: B**

**Estrutura documental:** A segunda mais rica, com artefatos extras.
- `charter.md` ✅
- `plan_quinzenal_sprint01.md` ✅
- `backlog.md` ✅
- `kickoff_prep.md` ✅
- `pulse_v0.md` ✅ — 100% vazio
- `onepage.md` ✅
- `criterios_minimos_v0.md` ✅ — critérios de entrada, contrapartida mínima
- `evidencia_drive_free_v0.md` ✅ — o que conta como drive-free
- `checkin_mensal_v0.md` ✅ — template de check-in mensal

**Touch tracking:** Todos `[PREENCHER]`.

**Operacional:** Zero evidência de execução. Nenhuma incorporadora mapeada no sistema, nenhum status drive-free registrado, nenhum caso piloto documentado.

**Coerência interna:** Alta. Métricas e critérios são os mais detalhados do portfólio. A métrica soberana ("% drive-free por praça") é clara e mensurável.

**Útil ou documental?** Documental. WS6 tem a estrutura mais madura de critérios e evidência — mas não há um único dado real sobre nenhuma incorporadora no sistema.

**Observação:** WS6 usa "praça" como unidade de gestão — igual a WS3. Ambos têm Mayumi como DRI. Risco de confusão operacional se não houver separação clara de rituais (WS3 = sprint quinzenal com sócio; WS6 = check-in mensal com incorporadoras).

---

### WS7 SL — Modelo Econômico do Sócio-Local
**Nota: D** ⚠️ INCONSISTÊNCIA CRÍTICA

**Estrutura documental:**
- `charter.md` ✅ — completo, com arquitetura de 4 blocos + booster
- `plan_quinzenal_sprint01.md` ✅
- `backlog.md` ✅ — mais enxuto (10 itens em 3 sprints)
- `kickoff_prep.md` ✅
- `pulse_v0.md` ✅ — 100% vazio
- `onepage.md` ✅

**Inconsistência crítica — DRI:**
- `charter.md` declara DRI = **Eduardo + Felipe**
- `decisions.md` (08/03/2026) registra: *"WS7 SL: DRI = Diego Diehl. Não Eduardo + Felipe como previsto. Diego assume diretamente."*
- O charter **não foi atualizado**. Se Eduardo ou Felipe lerem o charter, acreditam que são DRI. Diego assumiu mas não está documentado no artefato principal.

**Touch tracking:** Todos `[PREENCHER]`.

**Operacional:** Zero evidência de execução. Modelo econômico não aprovado, praças não classificadas (Full/Híbrida/Remota), painel não criado.

**Impacto da inconsistência:** WS7 é estrategicamente crítico — define como sócios locais são remunerados. Diego assumiu o DRI pessoalmente. Mas o charter diz Eduardo + Felipe. Quem está monitorando o WS7 na prática?

**Útil ou documental?** Documental. Nem o modelo existe nem há governança ativa.

---

## 3. PADRÕES DE CONSISTÊNCIA

### 3.1. O que é consistente em todos os 7 WS

✅ **Formato padronizado:** Todos os WS têm charter, plano, backlog, kickoff_prep, pulse e onepage. Padrão de documentação é uniforme.

✅ **Sponsor único:** Diego em todos os WS — sem ambiguidade de patrocínio.

✅ **Cadência declarada:** Quinzenal em todos os WS — sem conflito de ritmo.

✅ **Fronteiras declaradas:** Todos os charters têm seção "entra / não entra" e referência aos WS adjacentes. Sobreposição de escopo foi minimizada na documentação.

✅ **H1 leve:** Todos os WS têm escopo intencionalmente limitado para H1. Sem promessas de RevOps, scoring complexo ou automações pesadas.

✅ **Evidência mínima definida:** Todos os WS têm critério de "feito é" e lista de evidências válidas vs. não válidas.

### 3.2. O que é inconsistente

❌ **DRI real vs. DRI documentado (WS3 e WS7):** Duas decisões de DRI registradas no `decisions.md` (08/03) não foram propagadas para os charters. Os charters — que são o documento de referência do time — estão desatualizados.

❌ **Touch tracking zerado em todos os WS:** 28 campos `[PREENCHER]` nos 7 charters (4 campos por WS). Nenhum WS tem data de último toque registrada.

❌ **Pulse universalmente vazio:** 7 pulses template sem um único dado real. O sistema declarou estar "pronto para kickoffs" (HARMONIZACAO_FINAL, 08/03) — mas não há evidência de que nenhum kickoff ocorreu.

❌ **Planos com datas em branco:** Os planos quinzenais de todos os WS têm `[DATA]` como campos de início e fim do sprint. Nenhum Sprint 01 tem data real associada.

❌ **Backlogs todos com status ⏳:** Em todos os WS, 100% dos itens do backlog estão como "pendentes". Nenhum item moveu.

---

## 4. LACUNAS DE GOVERNANÇA

| # | Lacuna | WS afetado | Impacto |
|---|--------|-----------|---------|
| 1 | **DRI desatualizado no charter** | WS3, WS7 | Time opera com informação errada sobre quem é responsável |
| 2 | **Nenhum kickoff formal realizado** | Todos (1–7) | Sprint 01 não existe em nenhum WS — há plano sem ciclo ativo |
| 3 | **Touch tracking zerado** | Todos (1–7) | Indicador-âncora do portfólio (`days_since_touch`) não é calculável |
| 4 | **Pulses todos vazios** | Todos (1–7) | Nenhum WS tem evidência de execução registrada |
| 5 | **Dados reais ausentes** | WS2, WS3, WS4 | Baseline incompleto: DLs por status (WS2), praças por estágio (WS3), Bitrix (WS4) |
| 6 | **Projeto Autoridade Digital fora do portfólio** | WS5 | Iniciativa pessoal crítica de Diego sem WS ou ritual formal |
| 7 | **Modelo econômico do sócio inexistente** | WS7 | Praças ativas (Curitiba, Vitória) operam sem modelo de remuneração aprovado |
| 8 | **WS6 sem dado de nenhuma incorporadora** | WS6 | Métrica soberana (% drive-free) não tem denominador |
| 9 | **Sobrecarga Mayumi não mitigada** | WS1, WS3, WS5, WS6 | 4 WS com DRI único; risco de gargalo humano no Bloco A |
| 10 | **Lara não tem papel nos rituais de WS** | Todos | Não há menção a Lara em nenhum ritual de WS — follow-ups pós-reunião não têm executor definido |
| 11 | **Morfeu não monitora WS1, WS2, WS4, WS5, WS6, WS7** | 6 de 7 WS | Não existe prompt, cron ou script para nenhum desses WS. Só WS3 tem automação. |

---

## 5. RISCOS PRINCIPAIS

| Risco | Severidade | Descrição |
|-------|-----------|-----------|
| **Portfólio inteiro sem sprint ativo** | 🔴 CRÍTICO | Nenhum dos 7 WS tem Sprint 01 em execução. HARMONIZACAO_FINAL declarou prontidão em 08/03, mas a máquina não foi ligada. |
| **WS3 com DRI errado no charter** | 🔴 ALTO | Eduardo é DRI por decisão de Diego (08/03), mas o charter diz Mayumi. Jobs de praças rodam sem que o DRI real saiba que é responsável. |
| **WS7 com DRI errado no charter** | 🔴 ALTO | Diego é DRI, mas charter aponta Eduardo + Felipe. Modelo econômico do sócio — a peça que viabiliza a expansão territorial — está sem dono real documentado. |
| **Mayumi com 4 WS no Bloco A** | 🟡 MÉDIO | Risco aceito. Mas sem sprint ativo, sem evidência de reunião com time, não há como validar se essa carga é real ou teórica. |
| **WS2 depende de WS4 que não rodou** | 🟡 MÉDIO | O kickoff WS2 CX foi agendado para 16/03. Se o CRM não tiver higiene mínima antes, o WS2 roda sobre dados ruins. |
| **Projeto Autoridade Digital de Diego sem governança** | 🟡 MÉDIO | Está nos OKRs de Diego para 2026. Não tem WS, não tem DRI, não tem cadência formal. |
| **Morfeu monitorando 1 de 7 WS** | 🟡 MÉDIO | O agente tem visibilidade quase zero de WS1, WS2, WS4, WS5, WS6. Qualquer alerta ou cobrança nesses WS depende de Diego reportar manualmente. |
| **`days_since_touch` > 14 em todos os WS** | 🟡 MÉDIO | A regra definida em `governance/workstreams.md` é: "cada WS deve ter Days Since Touch ≤ 14 dias". Nenhum WS tem data de início — portanto todos estão tecnicamente vencidos. |

---

## 6. INSUMOS PARA A ETAPA 3 — CAMADA EXTERNA DE OPERAÇÃO

A Etapa 2 revelou que a governança está inteiramente no papel. Para entender por que não saiu do papel, a Etapa 3 deve investigar as ferramentas externas que deveriam dar vida a esse portfólio:

1. **Bitrix24:** O CRM é a fonte de verdade operacional da Órulo. WS2 e WS4 dependem dele inteiramente. Como o time acessa? O que está lá? Por que o Morfeu não lê?

2. **Google Calendar:** Nenhum ritual de WS tem data. Os kickoffs existem como intenção. O Calendar de Diego reflete algum desses rituais?

3. **tl;dv:** Reuniões com o time deveriam gerar transcrições. Algum WS ritual já foi capturado pelo tl;dv?

4. **Gmail:** Follow-ups pós-reunião deveriam estar circulando. O smart email scan está captando sinais de algum WS?

5. **Telegram (time):** O canal de comunicação do time está definido como "a definir". Como o Morfeu entrega cobranças ao time sem canal oficial?

6. **Lara:** A secretária executiva tem 1 job ativo. Qual é a rotina real de output da Lara para o time? Algum e-mail de follow-up foi enviado?

---

*Etapa 2 concluída. Próxima: `03_operacao_externa.md`*
