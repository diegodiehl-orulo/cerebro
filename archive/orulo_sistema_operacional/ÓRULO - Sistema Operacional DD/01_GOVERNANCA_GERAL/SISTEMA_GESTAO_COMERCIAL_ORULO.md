# Sistema de Gestão Comercial da Órulo — Documento Consultivo

**Versão:** 1.0 | **Data:** 27 de março de 2026 | **Autor:** Manus AI para Diretoria Comercial Órulo

---

## 1. Contexto e Problema

A Órulo opera um modelo de expansão territorial B2B no mercado imobiliário, com múltiplas praças geográficas, sócios-locais, GDDs (Gestores de Desenvolvimento), coordenadores e vendedores. A complexidade da operação exige um sistema de acompanhamento de metas que funcione em múltiplas camadas hierárquicas e temporais, com clareza suficiente para que cada nível da organização saiba, a qualquer momento, se está no caminho certo.

O problema central é a ausência de um **sistema unificado de gestão de indicadores comerciais** que permita:

- ao vendedor saber se atingiu a meta do dia e da semana;
- ao coordenador saber se a equipe está no ritmo da semana e do mês;
- ao gerente/GDD saber se a praça está convergindo para a meta mensal;
- ao diretor saber se a empresa está no ritmo do trimestre e do ano.

Este documento propõe a arquitetura completa desse sistema, fundamentada na **metodologia Falconi de Gerenciamento pelas Diretrizes (GPD)**, no framework de **OKRs**, e nas melhores práticas de **gestão comercial B2B com funil CRM, forecast e cadência de reuniões**.

---

## 2. Fundamentos Metodológicos

### 2.1 Falconi — Gerenciamento pelas Diretrizes (GPD)

O GPD, criado por Vicente Falconi, é uma metodologia de gestão que alinha objetivos estratégicos com atividades operacionais por meio do **desdobramento cascateado de metas** [1]. O princípio central é que cada colaborador deve saber qual é sua meta individual e como ela contribui para o objetivo macro da empresa.

O GPD se sustenta em três pilares: **dedicação e ação criativa**, **inovação** e **monitoramento**. O motor de execução é o ciclo **PDCA** (Plan-Do-Check-Act), onde a fase de **Check** — a verificação sistemática de resultados contra metas — é considerada por Falconi como o momento onde os resultados realmente acontecem [2].

> "O foco no acompanhamento dos resultados e na atuação nos desvios é o que garante o que mais se persegue nas organizações: resultado." — Merithu Consultoria [2]

A aplicação do GPD à Órulo significa que a meta anual de receita (MRR) deve ser desdobrada em metas trimestrais, mensais, semanais e diárias, com indicadores específicos para cada nível hierárquico. Cada meta deve ter um **dono**, um **indicador mensurável**, uma **frequência de medição** e um **farol de status**.

### 2.2 Farol de Indicadores (Sistema RAG)

O farol de indicadores é uma ferramenta de gestão visual que utiliza cores para comunicar instantaneamente o status de cada meta [3]. O sistema padrão utiliza quatro faixas:

| Cor | Significado | Faixa Típica | Ação Requerida |
|-----|-------------|--------------|----------------|
| **Azul** | Superação | > 120% da meta | Documentar e replicar |
| **Verde** | No caminho | 100% a 120% da meta | Manter ritmo |
| **Amarelo** | Atenção | 80% a 99% da meta | Plano de correção |
| **Vermelho** | Crítico | < 80% da meta | Ação imediata + escalação |

A definição das faixas deve ser calibrada por indicador. Para indicadores de atividade (ligações, visitas), a tolerância pode ser menor (vermelho abaixo de 85%), enquanto para indicadores de resultado (receita), a tolerância pode ser maior (vermelho abaixo de 70%) devido à variabilidade natural do ciclo de vendas.

O farol não é apenas decorativo. Cada indicador vermelho deve disparar automaticamente uma **análise de causa raiz** (usando 5 Porquês ou Ishikawa) e um **plano de ação corretivo** com dono e prazo [3].

### 2.3 OKRs Aplicados à Área Comercial

Os OKRs (Objectives and Key Results) complementam o GPD ao definir **objetivos ambiciosos** com **resultados-chave mensuráveis** em ciclos trimestrais [4]. A diferença fundamental entre OKRs e KPIs é que os KPIs monitoram a saúde contínua da operação, enquanto os OKRs direcionam mudanças específicas e ambiciosas.

Na Órulo, a coexistência de ambos é recomendada:

| Instrumento | Função | Exemplo Órulo | Cadência |
|-------------|--------|---------------|----------|
| **KPI** | Monitorar saúde operacional | Taxa de conversão lead → cliente | Contínuo |
| **OKR** | Direcionar mudança ambiciosa | Aumentar MRR de R$ 600k para R$ 800k no Q2 | Trimestral |

O desdobramento de OKRs para a área comercial segue uma cascata lógica [5]:

**Nível Empresa:** O: Atingir R$ 10M de ARR em 2026 → KR1: MRR de R$ 833k/mês; KR2: Churn < 3%; KR3: 12 praças com faturamento > R$ 50k/mês.

**Nível Diretoria Comercial:** O: Maximizar conversão e expansão territorial → KR1: Pipeline coverage de 3.5x; KR2: Win rate > 25%; KR3: 4 novas praças ativadas no trimestre.

**Nível Coordenador/GDD:** O: Consolidar praça X como madura → KR1: 300 corretores ativos; KR2: 15 imobiliárias integradas; KR3: Receita mensal > R$ 80k.

**Nível Vendedor/BDR:** O: Bater meta individual de ativação → KR1: 40 ligações/dia; KR2: 15 reuniões/semana; KR3: 5 propostas enviadas/semana.

### 2.4 Gráficos Acumulativos — A Ferramenta Central de Tracking

O gráfico acumulativo (ou burn-up chart adaptado para vendas) é a ferramenta visual mais poderosa para acompanhamento de metas porque responde instantaneamente à pergunta: **"Estou no ritmo certo?"** [6].

O princípio é simples: o eixo X representa o tempo (dias úteis do período), e duas linhas são plotadas: a **linha de meta** (crescimento linear do zero até a meta) e a **linha de realizado** (acumulado real dia a dia). Se a linha de realizado está acima da meta, o indicador é verde; se está abaixo, é vermelho. O gap visual é imediato e não requer interpretação.

A aplicação por camada hierárquica na Órulo seria:

| Camada | Período do Gráfico | Meta Acumulada | Atualização |
|--------|---------------------|----------------|-------------|
| **Vendedor** | Semana (5 dias úteis) | Atividades + resultado semanal | Diária |
| **Coordenador** | Mês (22 dias úteis) | Meta da equipe mensal | Diária |
| **GDD/Gerente** | Mês + Trimestre | Meta da praça/região | Semanal |
| **Diretor** | Trimestre + Ano | Meta da empresa | Semanal |

Além do gráfico acumulativo principal, outros tipos de visualização complementam a análise:

**Waterfall chart:** Mostra a contribuição de cada etapa do funil para o resultado final, evidenciando onde há perda de conversão.

**Gauge/Velocímetro:** Percentual de atingimento com faixas RAG, ideal para KPIs pontuais em dashboards de gestão à vista.

**Sparklines:** Mini-gráficos de tendência embutidos em tabelas, permitindo ver a direção de cada indicador sem ocupar espaço.

---

## 3. Funil Comercial da Órulo — Modelo Proposto

### 3.1 Estrutura do Funil

O funil comercial da Órulo opera em dois eixos simultâneos: o **funil de aquisição de praças** (expansão territorial) e o **funil de ativação dentro da praça** (corretores, imobiliárias, incorporadoras). Para o dashboard comercial, propomos um funil unificado com as seguintes etapas:

| Etapa | Descrição | Métrica Principal | Conversão Alvo |
|-------|-----------|-------------------|----------------|
| **Lead/Prospect** | Corretor ou imobiliária identificada | Volume de leads | — |
| **Qualificação** | Contato realizado, interesse validado | Taxa de qualificação | 40-50% |
| **Apresentação** | Demo/reunião realizada | Taxa de apresentação | 60-70% |
| **Proposta** | Proposta comercial enviada | Taxa de proposta | 50-60% |
| **Negociação** | Em discussão de termos/preço | Taxa de negociação | 60-70% |
| **Fechamento** | Contrato assinado | Win rate | 25-35% |
| **Ativação** | Usando o produto efetivamente | Taxa de ativação | 80-90% |

### 3.2 Métricas do Pipeline

Cinco métricas fundamentais devem ser monitoradas no pipeline [7]:

**Pipeline Coverage:** A razão entre o valor total do pipeline aberto e a quota do período. O benchmark para B2B SaaS é de 3x a 4x. Se a Órulo tem uma meta mensal de R$ 617k, o pipeline aberto deve ser de R$ 1.8M a R$ 2.5M.

**Stage Conversion Rate:** A taxa de conversão entre cada etapa do funil. Quedas abruptas em uma etapa específica indicam um gargalo que precisa de intervenção (treinamento, material de vendas, ajuste de pricing).

**Cycle Time:** O tempo médio entre a abertura de uma oportunidade e seu fechamento. A tendência deve ser de redução. Aumento no cycle time pode indicar deals "zumbis" no pipeline.

**Win Rate:** A proporção de oportunidades ganhas sobre o total de oportunidades trabalhadas. É o indicador mais direto de eficácia comercial.

**Average Deal Size:** O ticket médio por fechamento. Combinado com o volume, determina a receita total.

### 3.3 Forecast de Vendas

O forecast combina dados do pipeline com probabilidades por etapa para projetar a receita esperada. Três cenários devem ser mantidos simultaneamente [7]:

**Commit:** Deals com alta probabilidade de fechamento no período (>80%). É o número que o diretor pode "prometer" ao board.

**Best Case:** Commit + deals com probabilidade moderada (50-80%). É o cenário otimista realista.

**Upside:** Best case + deals em estágio inicial com potencial. É o teto teórico.

A acurácia do forecast (forecast vs. realizado) deve ser monitorada mês a mês. Um forecast consistentemente otimista indica que as probabilidades por etapa estão infladas; um forecast pessimista indica conservadorismo excessivo ou pipeline mal qualificado.

---

## 4. Cadência de Reuniões Comerciais

A cadência de reuniões é o "batimento cardíaco" da operação comercial. Cada camada temporal tem um propósito específico e não deve ser confundida com as demais [8].

### 4.1 Daily — Execução Imediata

| Aspecto | Definição |
|---------|-----------|
| **Quem** | Vendedor + Coordenador |
| **Duração** | 15 minutos |
| **Frequência** | Diária (início do expediente) |
| **Formato** | Stand-up (em pé, sem slides) |

**Agenda fixa:**
1. O que fiz ontem? (2 min por pessoa)
2. O que vou fazer hoje? (2 min por pessoa)
3. Algum blocker? (5 min coletivo)

**Indicadores na tela:** Gráfico acumulativo semanal de atividades (ligações, reuniões, propostas) vs. meta. Farol RAG individual.

**Regra de ouro:** Não é reunião de coaching. Não é reunião de estratégia. É alinhamento de execução.

### 4.2 Weekly — Correção de Rota (Reunião Semanal Comercial)

| Aspecto | Definição |
|---------|-----------|
| **Quem** | Coordenador + GDD + Gerente |
| **Duração** | 45-60 minutos |
| **Frequência** | Semanal (segunda-feira) |
| **Formato** | Sala com dashboard na tela |

**Agenda fixa:**
1. **Resultado da semana anterior** (10 min): Gráfico acumulativo mensal. Farol por vendedor. Desvios críticos.
2. **Pipeline review** (20 min): Deals que avançaram, deals parados, deals perdidos. Pipeline coverage atualizado.
3. **Forecast update** (10 min): Atualização de commit/best case. Deals que entram ou saem do forecast.
4. **Ações da semana** (10 min): Plano de ação para desvios. Donos e prazos.

**Indicadores na tela:** Gráfico acumulativo mensal (meta vs. realizado). Funil com conversões por etapa. Pipeline coverage. Ranking de vendedores. Alertas vermelhos.

**Regra de ouro:** Pré-leitura obrigatória. Ninguém apresenta status na reunião — os dados já estão no dashboard. A reunião é para **decidir**, não para informar.

### 4.3 Monthly — Tendências e Prioridades (MBR)

| Aspecto | Definição |
|---------|-----------|
| **Quem** | GDD + Diretoria + RevOps |
| **Duração** | 60-90 minutos |
| **Frequência** | Mensal (primeira semana) |
| **Formato** | Apresentação estruturada |

**Agenda fixa:**
1. **Resultado do mês** (15 min): Receita vs. meta. Gráfico acumulativo trimestral. Farol por praça.
2. **Análise de funil** (25 min): Conversões por etapa. Gargalos identificados. Cycle time. Win rate por segmento.
3. **Forecast do próximo mês** (15 min): Commit/best case/upside. Acurácia do forecast anterior.
4. **Prioridades e recursos** (15 min): Praças que precisam de reforço. Contratações. Investimentos.

**Indicadores na tela:** Gráfico acumulativo trimestral e anual. Waterfall do funil. Heatmap de praças (score vs. receita). Forecast accuracy.

### 4.4 Quarterly — Reset Estratégico (QBR)

| Aspecto | Definição |
|---------|-----------|
| **Quem** | Diretoria + C-Level |
| **Duração** | 2-3 horas |
| **Frequência** | Trimestral |
| **Formato** | Sessão estratégica |

**Agenda fixa:**
1. **Resultado do trimestre** (30 min): OKRs — atingimento por KR. Receita vs. meta anual (gráfico acumulativo anual).
2. **Análise de portfolio** (45 min): Praças por fase estratégica. ROI por praça. Decisões de investimento/desinvestimento.
3. **OKRs do próximo trimestre** (30 min): Definição de novos objetivos e key results.
4. **Riscos e oportunidades** (15 min): Cenários. Contingências.

---

## 5. Desdobramento de Indicadores para a Órulo

### 5.1 Árvore de Indicadores

O desdobramento segue a lógica Falconi de cascata, onde cada indicador de nível superior é composto por indicadores de nível inferior:

**Nível 1 — Empresa (Diretor):**

| Indicador | Meta Anual | Frequência | Farol |
|-----------|-----------|------------|-------|
| ARR (Receita Recorrente Anual) | R$ 10M | Mensal | RAG |
| MRR (Receita Recorrente Mensal) | R$ 833k | Mensal | RAG |
| Churn Rate | < 3% | Mensal | RAG |
| Net Revenue Retention | > 110% | Trimestral | RAG |
| Praças Maduras (Score > 80) | 8 | Trimestral | RAG |
| Pipeline Coverage | 3.5x | Semanal | RAG |

**Nível 2 — Praça/Região (GDD/Gerente):**

| Indicador | Meta Mensal | Frequência | Farol |
|-----------|-----------|------------|-------|
| Receita da Praça | Varia por praça | Mensal | RAG |
| Corretores Ativos | Varia por praça | Semanal | RAG |
| Imobiliárias Integradas | Varia por praça | Mensal | RAG |
| Incorporadoras com DA | Varia por praça | Mensal | RAG |
| Score da Praça | > 75 | Semanal | RAG |
| Win Rate da Praça | > 25% | Mensal | RAG |

**Nível 3 — Equipe (Coordenador):**

| Indicador | Meta Semanal | Frequência | Farol |
|-----------|-------------|------------|-------|
| Reuniões realizadas (equipe) | 30 | Semanal | RAG |
| Propostas enviadas (equipe) | 15 | Semanal | RAG |
| Deals avançados no funil | 10 | Semanal | RAG |
| Novos leads qualificados | 20 | Semanal | RAG |
| Receita fechada (equipe) | R$ X | Semanal | RAG |

**Nível 4 — Individual (Vendedor/BDR):**

| Indicador | Meta Diária | Meta Semanal | Frequência | Farol |
|-----------|-----------|-------------|------------|-------|
| Ligações realizadas | 40 | 200 | Diária | RAG |
| Reuniões agendadas | 3 | 15 | Diária | RAG |
| Propostas enviadas | 1 | 5 | Diária | RAG |
| Follow-ups realizados | 10 | 50 | Diária | RAG |
| Deals fechados | — | 2 | Semanal | RAG |

### 5.2 Regras de Farol por Tipo de Indicador

As faixas do farol devem ser calibradas de acordo com o tipo de indicador:

| Tipo | Verde | Amarelo | Vermelho | Lógica |
|------|-------|---------|----------|--------|
| **Atividade** (ligações, reuniões) | ≥ 95% | 80-94% | < 80% | Tolerância baixa: atividade é controlável |
| **Resultado** (receita, deals) | ≥ 100% | 75-99% | < 75% | Tolerância moderada: resultado tem variabilidade |
| **Qualidade** (win rate, NPS) | ≥ meta | meta ± 10% | < meta - 10% | Tolerância média: depende de múltiplos fatores |
| **Pipeline** (coverage, volume) | ≥ 3.5x | 2.5-3.4x | < 2.5x | Faixas absolutas baseadas em benchmark |

---

## 6. Aplicação Prática — Como Funciona no Dia a Dia

### 6.1 O Vendedor às 8h da Manhã

O vendedor abre o portal e vê imediatamente seu **gráfico acumulativo semanal**: uma linha de meta (ex: 200 ligações na semana, crescendo linearmente de 0 a 200 em 5 dias) e uma linha de realizado. Se é quarta-feira e ele fez 100 ligações (meta acumulada: 120), o gráfico mostra que está 20 ligações atrás — farol amarelo. Ele sabe exatamente quantas ligações precisa fazer hoje para voltar ao verde.

Abaixo do gráfico, um **scorecard individual** mostra todos os seus KPIs com farol RAG: ligações (amarelo), reuniões (verde), propostas (vermelho). O vermelho em propostas dispara um alerta: "Você está 40% abaixo da meta de propostas. Revise seu pipeline e priorize deals em estágio de apresentação."

### 6.2 O Coordenador na Segunda-Feira

O coordenador abre a **visão de equipe** e vê o gráfico acumulativo mensal da equipe. Estamos no dia 15 e a equipe fechou R$ 45k (meta acumulada: R$ 50k) — farol amarelo, gap de R$ 5k. Abaixo, um **ranking de vendedores** mostra quem está verde, amarelo e vermelho. Dois vendedores estão vermelhos em atividade — ele agenda 1:1 com eles.

Na reunião semanal, ele apresenta o **pipeline da equipe**: 15 deals em negociação totalizando R$ 120k (coverage de 2.4x — vermelho). Decisão: intensificar prospecção para aumentar o topo do funil.

### 6.3 O Diretor no Início do Trimestre

O diretor abre a **visão consolidada** e vê o gráfico acumulativo anual: meta de R$ 10M, realizado acumulado de R$ 2.3M no final do Q1 (meta acumulada: R$ 2.5M) — farol amarelo, gap de R$ 200k. O waterfall do funil mostra que a conversão de "Proposta → Negociação" caiu 15% no último mês — gargalo identificado.

Na QBR, ele apresenta: OKRs do Q1 (2 de 3 KRs atingidos), forecast do Q2 (commit: R$ 2.4M, best case: R$ 2.8M), e propõe investimento em treinamento de negociação para atacar o gargalo de conversão.

---

## 7. Estrutura de Abas Proposta para o Portal

Com base em toda a fundamentação acima, a nova seção "Comercial" do portal Órulo deve conter as seguintes sub-abas:

### 7.1 Aba "Painel Comercial" (Visão Consolidada)

Visão de cockpit para o diretor e gerência. Contém: KPIs macro com farol (MRR, ARR, Churn, Pipeline Coverage, Win Rate), gráfico acumulativo anual e trimestral de receita, funil comercial com conversões por etapa, forecast (commit/best case/upside), e ranking de praças por receita.

### 7.2 Aba "Performance Individual" (Vendedor e Equipe)

Visão operacional para coordenadores e vendedores. Contém: seletor de vendedor/equipe, gráfico acumulativo semanal e mensal de atividades e resultado, scorecard individual com farol RAG por KPI, ranking de vendedores, e alertas de desvio.

### 7.3 Aba "Pipeline e Forecast"

Visão analítica do funil. Contém: funil visual com volume e valor por etapa, pipeline coverage por período, aging de deals (deals parados há mais de X dias), forecast por cenário (commit/best/upside), e acurácia histórica do forecast.

### 7.4 Integração com Abas Existentes

As abas existentes de "Visão de Praças" e "Praça Específica" devem ser enriquecidas com os indicadores comerciais (receita, funil, forecast por praça), criando uma ponte entre a visão territorial e a visão comercial.

---

## 8. Recomendações de Implementação

A implementação deve seguir uma abordagem incremental, priorizando o que gera valor imediato:

**Fase 1 (Semana 1-2):** Implementar o Painel Comercial com dados mock estruturados. Definir as faixas de farol para cada indicador. Criar os gráficos acumulativos.

**Fase 2 (Semana 3-4):** Implementar Performance Individual e Pipeline/Forecast. Conectar com fonte de dados real (CRM, planilhas).

**Fase 3 (Mês 2):** Calibrar faixas de farol com dados reais. Implementar alertas automáticos. Treinar a equipe na cadência de reuniões.

**Fase 4 (Mês 3):** Medir acurácia do forecast. Ajustar metas e faixas. Iterar com feedback da operação.

---

## Referências

[1]: https://actiosoftware.com/metodo-falconi-gerenciamento-pelas-diretrizes-gpd/ "Método Falconi: Gerenciamento pelas Diretrizes (GPD) — Actio"
[2]: https://merithu.com.br/2021/03/25/o-poder-do-check-onde-os-resultados-realmente-acontecem/ "O poder do Check: onde os resultados realmente acontecem — Merithu"
[3]: https://www.siteware.com.br/blog/indicadores/farol-de-indicadores/ "Farol de indicadores: o que é e como fazer? — Siteware"
[4]: https://asana.com/pt/resources/okr-vs-kpi "OKR ou KPI: qual dessas estruturas é melhor? — Asana"
[5]: https://c-suite.com.br/definicao-de-metas-metodologia-de-desdobramento-de-okrs-para-a-area-comercial/ "Metodologia de Desdobramento de OKRs para a Área Comercial — C-Suite"
[6]: https://www.atlassian.com/agile/project-management/burn-up-chart "What is a burn up chart and how to create one — Atlassian"
[7]: https://www.pedowitzgroup.com/best-cadence-for-business-reviews-weekly-monthly-quarterly "Best cadence for business reviews — Pedowitz Group"
[8]: https://www.tableau.com/dashboard/sales-dashboard-examples-and-templates "7 Great Examples & Templates Of Sales Dashboards — Tableau"
