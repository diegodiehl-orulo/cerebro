# Prompt de Especificação — Novas Abas Comerciais do Portal Órulo

**Versão:** 1.0 | **Data:** 27 de março de 2026

---

## Visão Geral

Adicionar uma nova seção principal **"Comercial"** ao portal Órulo, posicionada como a **segunda seção na sidebar** (logo após "Visão de Praças"), contendo três sub-abas internas que cobrem toda a gestão comercial da empresa. A seção deve funcionar como a **tela principal para reuniões comerciais** (daily, weekly, monthly e QBR).

---

## Aba 1: Painel Comercial (Visão Consolidada)

### Propósito
Cockpit executivo para o Diretor e gerência. Responde à pergunta: "A empresa está no ritmo certo para bater a meta?"

### Layout

**Barra superior — KPIs Macro com Farol RAG (6 cards)**

| Card | Valor Mock | Meta | Farol | Tendência |
|------|-----------|------|-------|-----------|
| MRR | R$ 617.000 | R$ 833.000 | Amarelo (74%) | Subindo |
| ARR | R$ 7.4M | R$ 10M | Amarelo (74%) | Subindo |
| Churn Rate | 2.8% | < 3% | Verde | Estável |
| Pipeline Coverage | 3.2x | 3.5x | Amarelo | Subindo |
| Win Rate | 27% | 25% | Verde | Subindo |
| Deals Abertos | 142 | — | Neutro | — |

Cada card deve ter: valor atual (grande), meta (pequeno), barra de progresso com cor RAG, ícone de tendência (seta para cima/baixo/estável), e sparkline dos últimos 6 meses.

**Bloco central esquerdo — Gráfico Acumulativo de Receita**

Gráfico de área com duas linhas:
- **Linha de meta:** Crescimento linear de R$ 0 a R$ 10M ao longo de 12 meses (eixo X: Jan-Dez 2026)
- **Linha de realizado:** Acumulado real mês a mês
- **Área entre as linhas:** Verde se realizado > meta, vermelho se realizado < meta
- **Ponto atual:** Marcador destacado com tooltip mostrando gap

Dados mock (acumulado):
- Jan: Meta R$ 833k / Real R$ 780k
- Fev: Meta R$ 1.67M / Real R$ 1.62M
- Mar: Meta R$ 2.5M / Real R$ 2.38M (ponto atual)
- Abr-Dez: Apenas linha de meta (projeção)

Abaixo do gráfico, um toggle para alternar entre: **Anual**, **Trimestral** (Q1 atual), **Mensal** (março).

**Bloco central direito — Funil Comercial**

Funil visual vertical com 6 etapas, cada uma mostrando:
- Nome da etapa
- Volume (quantidade de deals)
- Valor (R$)
- Taxa de conversão para a próxima etapa
- Cor RAG baseada na conversão vs. benchmark

Dados mock:

| Etapa | Deals | Valor | Conversão |
|-------|-------|-------|-----------|
| Lead/Prospect | 480 | R$ 4.8M | — |
| Qualificação | 210 | R$ 2.1M | 43.7% (verde) |
| Apresentação | 142 | R$ 1.42M | 67.6% (verde) |
| Proposta | 78 | R$ 780k | 54.9% (amarelo) |
| Negociação | 45 | R$ 450k | 57.7% (amarelo) |
| Fechamento | 12 | R$ 120k | 26.7% (verde) |

**Bloco inferior esquerdo — Forecast**

Três barras horizontais empilhadas:
- **Commit:** R$ 280k (deals com >80% probabilidade)
- **Best Case:** R$ 420k (commit + deals 50-80%)
- **Upside:** R$ 580k (best case + deals em estágio inicial)
- **Meta do mês:** R$ 833k (linha vertical de referência)

Abaixo, uma mini-tabela de acurácia do forecast:

| Mês | Forecast Commit | Realizado | Acurácia |
|-----|----------------|-----------|----------|
| Jan | R$ 750k | R$ 780k | 96% (verde) |
| Fev | R$ 820k | R$ 840k | 98% (verde) |
| Mar | R$ 800k | Em andamento | — |

**Bloco inferior direito — Ranking de Praças por Receita**

Tabela compacta com as top 10 praças:

| # | Praça | Receita Mês | Meta | % | Farol |
|---|-------|------------|------|---|-------|
| 1 | Curitiba | R$ 124k | R$ 100k | 124% | Azul |
| 2 | São Paulo | R$ 98k | R$ 120k | 82% | Amarelo |
| 3 | Recife | R$ 87k | R$ 80k | 109% | Verde |
| ... | ... | ... | ... | ... | ... |

---

## Aba 2: Performance Individual (Vendedor e Equipe)

### Propósito
Tela operacional para coordenadores e vendedores. Responde à pergunta: "Cada pessoa da equipe está no ritmo?"

### Layout

**Barra superior — Seletor de Contexto**

Três dropdowns:
1. **Praça:** Todas / João Pessoa / Curitiba / etc.
2. **Equipe:** Todas / Equipe Alpha / Equipe Beta / etc.
3. **Período:** Hoje / Esta Semana / Este Mês / Este Trimestre

**Bloco principal — Tabela de Performance Individual**

Tabela com farol RAG por KPI para cada vendedor:

| Vendedor | Praça | Ligações | Reuniões | Propostas | Deals Fechados | Receita | Score |
|----------|-------|----------|----------|-----------|----------------|---------|-------|
| Ana Silva | Curitiba | 🟢 185/200 | 🟢 16/15 | 🟡 4/5 | 🟢 3/2 | 🟢 R$ 45k | 92 |
| Pedro Santos | São Paulo | 🟡 160/200 | 🔴 8/15 | 🔴 2/5 | 🟡 1/2 | 🟡 R$ 22k | 58 |
| Joana Lima | Recife | 🟢 210/200 | 🟢 18/15 | 🟢 6/5 | 🟢 4/2 | 🔵 R$ 68k | 98 |
| Carlos Mendes | JP | 🔴 120/200 | 🟡 12/15 | 🟡 3/5 | 🔴 0/2 | 🔴 R$ 8k | 35 |
| ... | ... | ... | ... | ... | ... | ... | ... |

Cada célula mostra: ícone de farol + realizado/meta. Clique na linha expande o detalhe do vendedor.

**Bloco expandido — Detalhe do Vendedor (ao clicar)**

Ao clicar em um vendedor, expande um painel com:

1. **Gráfico acumulativo semanal:** Ligações realizadas vs. meta (linha a linha, dia a dia)
2. **Gráfico acumulativo mensal:** Receita acumulada vs. meta
3. **Mini-funil individual:** Deals do vendedor por etapa
4. **Últimas atividades:** Lista das 5 últimas ações (ligação, reunião, proposta, fechamento)
5. **Alertas:** "Pedro está 47% abaixo da meta de reuniões. Sugestão: revisar lista de prospects e priorizar follow-ups."

**Bloco lateral — Ranking e Comparativo**

Ranking de vendedores por score (composição ponderada de todos os KPIs). Gráfico de barras horizontais mostrando cada vendedor vs. a média da equipe.

---

## Aba 3: Pipeline e Forecast

### Propósito
Visão analítica do funil para reuniões semanais e forecast. Responde à pergunta: "O pipeline é saudável e o forecast é confiável?"

### Layout

**Bloco superior — Pipeline Overview**

Quatro cards de resumo:

| Card | Valor | Status |
|------|-------|--------|
| Pipeline Total | R$ 4.8M | — |
| Pipeline Coverage | 3.2x (meta: 3.5x) | Amarelo |
| Cycle Time Médio | 32 dias (meta: < 45) | Verde |
| Deals Parados > 30 dias | 18 | Vermelho |

**Bloco central — Funil Detalhado com Waterfall**

Gráfico waterfall mostrando a perda em cada etapa do funil:
- Entrada: 480 leads (R$ 4.8M)
- Perda na qualificação: -270 (R$ 2.7M)
- Perda na apresentação: -68 (R$ 680k)
- Perda na proposta: -64 (R$ 640k)
- Perda na negociação: -33 (R$ 330k)
- Fechamento: 12 deals (R$ 120k)

Cada barra de perda é vermelha; cada barra de passagem é verde. A maior barra vermelha indica o principal gargalo.

**Bloco central — Aging de Deals**

Tabela de deals ordenados por tempo parado:

| Deal | Praça | Etapa | Valor | Dias Parado | Responsável | Ação |
|------|-------|-------|-------|-------------|-------------|------|
| Incorp. Cyrela SP | São Paulo | Negociação | R$ 85k | 45 dias | Pedro | 🔴 Escalar |
| Imob. Premium CWB | Curitiba | Proposta | R$ 42k | 38 dias | Ana | 🟡 Follow-up |
| Incorp. MRV REC | Recife | Apresentação | R$ 65k | 22 dias | Joana | 🟢 Normal |

Filtros: por praça, por etapa, por responsável, por aging (> 15, > 30, > 45 dias).

**Bloco inferior — Forecast Detalhado**

Tabela de forecast por cenário com drill-down:

| Cenário | Valor | Deals | Prob. Média | Confiança |
|---------|-------|-------|-------------|-----------|
| **Commit** | R$ 280k | 8 | 87% | Alta |
| **Best Case** | R$ 420k | 15 | 62% | Média |
| **Upside** | R$ 580k | 28 | 38% | Baixa |

Ao clicar em cada cenário, expande a lista de deals que compõem aquele cenário.

**Bloco inferior — Forecast Accuracy**

Gráfico de barras agrupadas mostrando, para cada mês: forecast commit, forecast best case, e realizado. Linha de acurácia (%) sobreposta.

---

## Regras de Design

1. **Farol RAG:** Usar dots pulsantes (como já existe no portal) para status. Azul = superação, Verde = no caminho, Amarelo = atenção, Vermelho = crítico.

2. **Gráficos acumulativos:** Usar Recharts (já instalado). Área preenchida entre meta e realizado com gradiente verde/vermelho.

3. **Tipografia:** Números grandes em JetBrains Mono. Labels em Open Sans. Manter consistência com o portal existente.

4. **Responsividade:** Desktop-first (uso em reuniões com projetor), mas funcional em tablet.

5. **Interatividade:** Tooltips em todos os gráficos. Clique para drill-down. Filtros persistentes na sessão.

6. **Cadência visual:** A aba deve ter um indicador de "última atualização" no topo, e um badge indicando para qual reunião a visão é otimizada (Daily / Weekly / Monthly / QBR).

---

## Dados Mock

Todos os dados devem ser mock mas **estruturalmente realistas** — com variações, tendências, e distribuições que simulem uma operação real. Os dados devem ser definidos no arquivo `data.ts` existente, com tipos TypeScript bem definidos, para facilitar a futura conexão com API/banco real.

---

## Navegação

A sidebar do portal deve ganhar um novo item "Comercial" com ícone de gráfico de barras (BarChart3 do Lucide), posicionado como segunda seção. As três sub-abas devem ser acessíveis via tabs internas dentro da seção, não como itens separados na sidebar.
