# 02_GOVERNANCA_WORKSTREAMS.md — Auditoria Estrutural

> **Etapa:** 2/6 — Governança dos 7 Workstreams
> **Data:** 2026-03-08
> **Base:** 01_inventario_sistema.md

---

## 1. TABELA-RESUMO DOS 7 WORKSTREAMS

| WS | Nome | DRI | Sponsor | Status | Classificação |
|----|------|-----|---------|--------|--------------|
| WS1 | Comunicação com Corretores | Mayumi | Diego | Estruturado, não operado | **C** |
| WS2 | Jornada CX DL → Pago | Gustavo | Diego | Estruturado, não operado | **C** |
| WS3 | Fórmula Lançamento / Workshops / Praças | Mayumi + Sócios | Diego | Estruturado, não operado | **C** |
| WS4 | Estrutura Comercial & CRM | Gustavo | Diego | Estruturado, não operado | **C** |
| WS5 | Marketing e Conteúdo | Mayumi | Diego | Estruturado, não operado | **C** |
| WS6 | Embaixadoras + apoio CS | Mayumi | Diego | Estruturado, não operado | **C** |
| WS7 | Produtos Financeiros e Parcerias | Eduardo + Felipe | Diego | Estruturado, não operado | **C** |

---

## 2. LEITURA CRÍTICA POR WS

### 2.1 WS1 — Comunicação com Corretores

| Dimensão | Avaliação | Evidência |
|-----------|-----------|-----------|
| **Estrutura** | ✅ Completa | 6 arquivos (charter, backlog, plan, kickoff, onepage, pulse) |
| **Completude** | ❌ Templates vazios | C1/C2/C3 sem dados preenchidos (apenas [PREENCHER]) |
| **Operação** | ❌ Não operado | Pulse v0 = template vazio; sem evidência de ciclo executado |
| **Coerência** | ✅ Coerente | Escopo claro, fronteira com WS3/WS5 definida |
| **Utilidade** | ⚠️ Documental | Existe como artefato, não como sistema vivo |
| **Dependência sponsor** | 🔴 Alta | Todo ciclo precisa de Diego para validar |
| **Autonomia time** | ❌ Zero | Executor (Ester) não consegue operar sem DRI (Mayumi) + Sponsor (Diego) |

**Análise:** WS1 tem estrutura de governança completa MAS:
- Touch tracking vazio (last_live_touch = [PREENCHER])
- C1/C2/C3 são placeholders sem dados reais
- Não há evidência de que o kickoff aconteceu
- Não há evidência de que qualquer ciclo foi executado
- O DRI (Mayumi) acumula WS1 + WS3 + WS5 + WS6 (4 WS no Bloco A)

---

### 2.2 WS2 — Jornada CX DL → Pago

| Dimensão | Avaliação | Evidência |
|-----------|-----------|-----------|
| **Estrutura** | ✅ Completa | 6 arquivos |
| **Completude** | ❌ Parcial | Dados de DL existem (1268) mas sem indicadores operacionais preenchidos |
| **Operação** | ❌ Não operado | Pulse v0 = template vazio |
| **Coerência** | ✅ Coerente | Trilha definida, indicadores mencionados |
| **Utilidade** | ⚠️ Documental | Artefato, não sistema |
| **Dependência sponsor** | 🔴 Alta | BDRs (Jade, Mirla) executam mas precisam de Gustavo + Diego |
| **Autonomia time** | ❌ Zero | Sem playbook executado |

**Análise:** WS2 tem baseline de dados (1268 DLs) MAS:
- Indicadores operacionais não foram preenchidos no plan
- "Trilha mínima" não existe como documento operacional
- Não há evidência de rituais executados

---

### 2.3 WS3 — Fórmula Lançamento / Workshops / Praças

| Dimensão | Avaliação | Evidência |
|-----------|-----------|-----------|
| **Estrutura** | ✅ Completa | 6 arquivos |
| **Completude** | ⚠️ Parcial | C1-C4 definidos MAS sem dados reais |
| **Operação** | ⚠️ Parcial | Sistema de praças existe (pracas_sprint.md v2.0) mas WS3 genérico não opera |
| **Coerência** | ✅ Coerente | Integração com pracas_sprint clara |
| **Utilidade** | ⚠️ Híbrido | Artefato WS3 fraco MAS pracas_sprint.md forte |
| **Dependência sponsor** | 🔴 Alta | Sócios locais (Zanella, Kneip) precisam de Diego para validar sprints |
| **Autonomia time** | ⚠️ Parcial | Sócios enviam one-pager mas governança é centralizada |

**Análise:** WS3 conflui com o sistema de praças (pracas_sprint.md). Há 6 crons de governança de praças ativos. MAS:
- O WS3 em si é genérico e fraco
- A operação real está no sistema de praças, não no WS3
- Existe risco de duplicação ou confusão entre WS3 e pracas_sprint

---

### 2.4 WS4 — Estrutura Comercial & CRM

| Dimensão | Avaliação | Evidência |
|-----------|-----------|-----------|
| **Estrutura** | ✅ Completa | 6 arquivos |
| **Completude** | ❌ Fraca | Escopo definido, sem operacionalização |
| **Operação** | ❌ Não operado | Pulse v0 = template vazio |
| **Coerência** | ✅ Coerente | Foco CRM (Bitrix) claro |
| **Utilidade** | ❌ Fraca | Artefato sem função prática |

**Análise:** WS4 é o mais fraco em completude. Não há evidência de:
- Hygiene de CRM executada
- Cadências SDR implementadas
- Qualquer迭代 operacional

---

### 2.5 WS5 — Marketing e Conteúdo

| Dimensão | Avaliação | Evidência |
|-----------|-----------|-----------|
| **Estrutura** | ✅ Completa | 6 arquivos |
| **Completude** | ❌ Fraca | Escopo event-driven MAS sem eventos mapeados |
| **Operação** | ❌ Não operado | Pulse v0 = template vazio |
| **Coerência** | ✅ Coerente | Fronteira com WS1 clara |

**Análise:** WS5 depende de social media contratar (Q1) — condição não resolvida. O WS está contingente a essa ação, que não está em pending.md.

---

### 2.6 WS6 — Embaixadoras + apoio CS

| Dimensão | Avaliação | Evidência |
|-----------|-----------|-----------|
| **Estrutura** | ✅ Completa | 9 arquivos (mais que outros WS) |
| **Completude** | ⚠️ Parcial | C1-C4 comtemplados, checkin_mensal, criterios_minimos |
| **Operação** | ⚠️ Evidência drive-free | Arquivo evidencia_drive_free_v0.md existe |
| **Coerência** | ✅ Coerente | Métrica soberana clara (% drive-free) |

**Análise:** WS6 é o mais completo operacionalmente (9 arquivos vs 6). MAS:
- drive-free é condição "a validar" não executada
- Métrica soberana existe mas não tem baseline

---

### 2.7 WS7 — Produtos Financeiros e Parcerias

| Dimensão | Avaliação | Evidência |
|-----------|-----------|-----------|
| **Estrutura** | ✅ Completa | 6 arquivos |
| **Completude** | ❌ Fraca | DRI = Eduardo + Felipe (não definidos como DRI operacional) |
| **Operação** | ❌ Não operado | Pulse v0 = template vazio |
| **Coerência** | ⚠️ Incompleto | Escopo claro MAS sem DRI ativo |

**Análise:** WS7 é o mais frágil em termos de ownership. DRI = Eduardo + Felipe, mas:
- Não há evidência de que eles assumiram o DRI
- "Planejamento (Q1) → Execução (Q2)" — está em modo wait
- Sem pedido ao sponsor ou cadência definida

---

## 3. PADRÕES DE CONSISTÊNCIA

### 3.1 Padrões Positivos

| Padrão | Evidência |
|--------|-----------|
| **Estrutura documental uniforme** | Todos WS têm charter, plan, backlog, kickoff, onepage, pulse |
| **Método de governança definido** | workstreams.md define DRI, sponsor, touch, cadência |
| **Sistema de praças maduro** | pracas_sprint.md v2.0 com 6 crons ativos |
| **Clareza de fronteiras** | workstreams.md define WS1 vs WS3 vs WS5 |

### 3.2 Padrões Negativos (Consistentes em Todos WS)

| Padrão | WS Afetados | Evidência |
|--------|-------------|-----------|
| **Touch tracking vazio** | WS1, WS2, WS4, WS7 = [PREENCHER]; WS3, WS5, WS6 = sem campo | 7/7 |
| **Pulse template vazio** | Todos | pulse_v0.md = estrutura sem dados |
| **C1/C2/C3 como placeholders** | Todos | plan_quinzenal_sprint01.md com dados genéricos |
| **Dependência exclusiva do sponsor** | Todos | Diego = sponsor de todos os 7 WS |
| **Sobrecarga de Mayumi** | WS1, WS3, WS5, WS6 | 4 WS com mesmo DRI |
| **Kickoff sem evidência** | Todos | Não há ata, registro ou output de kickoff |

---

## 4. LACUNAS DE GOVERNANÇA

### 4.1 Lacunas de Execução

| Lacuna | WS | Impacto |
|--------|-----|---------|
| **Kickoffs não executados** | WS1-WS7 | Sistema não saiu do papel |
| **Pulses não executados** | WS1-WS7 | Sem evidência de cadência |
| **C1/C2/C3 não populados** | WS1-WS7 | Contratos vazios |
| **Touch tracking ausente** | WS1-WS7 | Não há como medir Days Since Touch |

### 4.2 Lacunas Estruturais

| Lacuna | WS | Impacto |
|--------|-----|---------|
| **Sobrecarga DRI** | WS1, WS3, WS5, WS6 | Mayumi = 4 WS = risco operacional |
| **DRI inativo** | WS7 | Eduardo + Felipe não aceitaram formalmente |
| **Condicional não resolvida** | WS5 | Social media pendente |
| **Duplicação WS3 ↔ pracas_sprint** | WS3 | Governance fragmentada |

### 4.3 Lacunas de Sistema

| Lacuna | Impacto |
|--------|---------|
| **Sem evidência de loop de aprendizado** | Error/Ajuste em pulse não tem base real |
| **Sem baseline de métricas** | WAU, DLs, drive-free =sem mensuração |
| **Sem automação de tracking** | Crons de WS não existem — só crons de praças |

---

## 5. RISCOS PRINCIPAIS

### 5.1 Risco: Sistema de Governança É Dokumentação, Não Operação

| Indicador | Dado |
|-----------|------|
| 7 WS com charter completo | MAS 0 com touch real |
| 30 crons ativos | MAS 0专为 WS execution |
| Pulse templates = 7/7 vazios | Sem exceção |

**Veredicto:** O sistema de governança de workstreams é **documental**. Existe como estrutura, não como operação.

### 5.2 Risco: Concentração de Decisão

| Indicador | Dado |
|-----------|------|
| Sponsor de todos WS | Diego = 7/7 |
| DRI = Mayumi | WS1, WS3, WS5, WS6 = 4/7 |
| DRI inativos | WS7 (Eduardo + Felipe não aceitaram) |

**Veredicto:** Se Diego não actuar, o sistema não move. Se Mayumi saturar, 4 WS param.

### 5.3 Risco: Duplicação WS3 ↔ Praças

| Indicador | Dado |
|-----------|------|
| WS3 = "Fórmula Lançamento / Workshops / Praças" | Genérico e fraco |
| pracas_sprint.md = Sistema de Praças v2.0 | Específico e forte |
| 6 crons de praças ativos | Existente |
| 0 crons de WS3 | Inexistente |

**Veredicto:** WS3 é redundante. A operação real de praças está em pracas_sprint.md, não no WS3.

---

## 6. INSUMOS PARA ETAPA 3

### 6.1 O que avaliar na Etapa 3

A **Etapa 3 (Camada Externa de Operação)** deve verificar:

1. **Coerência entre governança interna e externa:**
   - Os WS (documental) têm correspondência em Google Drive, planilhas, documentos externos?
   - Há duplicação ou divergência entre OpenClaw e sistemas externos?

2. **Estrutura de suporte:**
   - Onde o time busca informação? Drive? OpenClaw? Bitrix?
   - Há ponto único de verdade ou múltiplas fontes?

3. **Naming e organização:**
   - O time consegue encontrar o que precisa?
   - A nomenclatura é clara ou confusa?

### 6.2 Arquivos de Referência

| Arquivo | Leitura |
|---------|---------|
| 01_inventario_sistema.md | Inventário completo |
| governance/pracas_sprint.md | Sistema de praças (força real) |
| memory/pending.md | Pendências transversais |
| docs/*.md | Documentação técnica |

### 6.3 Pergunta Chave para Etapa 3

- Onde está a "verdade" operacional: dentro do OpenClaw (documentos) ou fora (Drive, Bitrix, planilhas)?
- O time sabe onde buscar sem perguntar Diego?

---

## 7. ACHADOS PRINCIPAIS (Etapa 2)

### ✅ O que existe

- 7 WS com estrutura completa (charter, backlog, plan, kickoff, onepage, pulse)
- workstreams.md com método, DRI, sponsor, touch, cadência definidos
- pracas_sprint.md v2.0 com 6 crons de governança ativos
- Fronteiras entre WS relativamente claras

### ❌ O que falta

- Evidência de kickoffs executados (0/7)
- Evidência de pulses executados (0/7)
- Touch tracking populated (0/7)
- C1/C2/C3 com dados reais (0/7)
- Automação de tracking de WS (0 crons)

### ⚠️ O que é risco

- **Governança é documentação, não operação**
- **Dependência exclusiva de Diego (7/7 WS como sponsor)**
- **Sobrecarga de Mayumi (4/7 WS como DRI)**
- **WS3 redundante (pracas_sprint é a operação real)**
- **WS7 sem DRI ativo (Eduardo + Felipe não aceitaram)**
- **WS5 dependente de social media (pendente desde Q1)**

### 📊 Classificação Final

| Classificação | Quantidade | WS |
|---------------|------------|-----|
| **A — Operacional** | 0 | — |
| **B — Estruturado mas imaturo** | 0 | — |
| **C — Parcialmente estruturado** | 7 | WS1-WS7 |
| **D — Estruturalmente fraco** | 0 | — |
| **E — Inexistente** | 0 | — |

**Veredicto:** Todos os 7 WS são **Classificação C** — parcialmente estruturados, precisam de reforço operacional.

---

*Fim da Etapa 2. Próxima: Etapa 3 — Camada Externa de Operação.*
