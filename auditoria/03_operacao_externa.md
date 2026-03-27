# 03_OPERACAO_EXTERNA.md — Auditoria Estrutural

> **Etapa:** 3/6 — Camada Externa de Operação
> **Data:** 2026-03-08
> **Base:** 01_inventario_sistema.md + 02_governanca_workstreams.md

---

## 1. MAPA DA CAMADA EXTERNA

### 1.1 Sistemas Externos Identificados

| Sistema | Função | Referência no OpenClaw | Status |
|---------|--------|----------------------|--------|
| **Bitrix24** | CRM operacional | WS4, pracas_sprint.md | "Somente referência" — sem edição |
| **Google Drive** | Armazenamento atual | WS6 (Drive-free como meta) | Sistema a substituir |
| **Google Calendar** | Agenda | scripts/gcal_morfeu.py | Integrado |
| **Gmail** | E-mail | scripts/email_*.py | Integrado |
| **tl;dv** | Transcrição reuniões | scripts/tldv_*.py | Integrado |
| **Trinks** | Agendamento cabelo/barbear | scripts/trinks_booking.py | Integrado |
| **Notion** | GTD digital | memory/daily/*.md | Bloqueado (sem API key) |
| **Google Sheets** | Planilhas | Referenciado em WS1, WS2, WS6 | Pouco usado |

### 1.2 Estrutura de Arquivos Externos (OpenClaw-only)

O sistema atual opera **exclusivamente dentro do OpenClaw**:

| Categoria | Localização | Observação |
|-----------|-------------|-----------|
| Governança | /workspace/governance/ | WS1-WS7 + pracas_sprint.md |
| Memória | /workspace/memory/ | pending, projects, lessons, daily |
| Scripts | /workspace/scripts/ | 25 Python scripts |
| Crons | OpenClaw DB | 30 jobs |
| Biblioteca | /workspace/biblioteca/ | 12 docs estratégicos |
| CRM | /workspace/crm/ | Sistema de inteligência (sem Bitrix) |

### 1.3 Ausência de Camada Externa Estruturada

| O que seria esperado | Realidade |
|----------------------|-----------|
| Google Drive com estrutura de WS | Drive = sistema a substituir (WS6), não fonte |
| Planilhas de controle | Mencionadas em WS1/WS2 mas não existem estruturadas |
| Notion como Wiki | Bloqueado — sem API key |
| Base de dados unificada | Não existe — cada script gera JSON local |

---

## 2. COERÊNCIAS E INCOERÊNCIAS

### 2.1 Coerências Positivas

| Ponto | Análise |
|-------|---------|
| **OpenClaw como fonte única** | O sistema não tenta usar Drive como verdade — intencionalmente evita |
| **Scripts autossuficientes** | Cada script gera output local (JSON), não depende de sistema externo |
| **Pracas_sprint.md claro** | Fonte de governança de praças definida e consistente |
| **Memória estruturada** | pending, projects, lessons cobrem contexto operacional |

### 2.2 Incoerências Críticas

| Ponto | Incoerência | Impacto |
|-------|-------------|---------|
| **WS6 (Drive-free) vs. Realidade** | WS6 quer substituir Drive MAS não há替代 implementada | Meta sem mecanismo |
| **Bitrix como referência** | "Somente referência" em pracas_sprint.md MAS WS4 depende de hygiene Bitrix | Sem execução |
| **Google Sheets mencionada** | WS1/WS2 citam planilha MAS não existe | Contrato vazio |
| **Notion bloqueada** | GTD digital pendente MAS sem API key | Pendência antiga |

### 2.3 Duplicação WS3 ↔ Pracas_sprint

| Aspecto | WS3 | pracas_sprint.md |
|---------|-----|------------------|
| Escopo | "Fórmula Lançamento / Workshops / Praças" | Sprint quinzenal por praça |
| Maturidade | Genérico, fraco | Específico, forte (v2.0) |
| Crons | 0 | 6 |
| Evidência | Template vazio | 6 crons ativos |

**Conclusão:** WS3 é redundante. A operação real de praças está em pracas_sprint.md.

---

## 3. PRINCIPAIS CONFUSÕES ESTRUTURAIS

### 3.1 Confusão: Fonte de Verdade

| Tipo de Dado | Onde deveria estar | Onde está realmente |
|--------------|-------------------|-------------------|
| Dados de sprint | pracas_sprint.md + memory/projects_orulo.md | Diego colando e-mail manualmente |
| Pipeline CRM | Bitrix | "Somente referência" |
| Métricas WS | WS pulse (vazio) | Não existe |
| Base de corretores | WS1 | Não existe (planilha mencionada mas não criada) |
| Base de DLs | WS2 | 1268 mencionado, sem sistema |

### 3.2 Confusão: Nomeclatura

| Termo | Uso | Confusão |
|-------|-----|----------|
| **Touch** | workstreams.md | Campo days_since_touch existe mas nunca populado |
| **Pulse** | WS1-WS7 | Arquivo pulse_v0 existe mas vazio em todos WS |
| **Drive-free** | WS6 | Meta clara MAS sem mecanismo de medição |
| **One-Pager** | pracas_sprint.md | Template definido MAS sem evidência de recebimento |

### 3.3 Confusão: Responsabilidade

| Responsável | Referência | Realidade |
|-------------|-----------|----------|
| **Ester (WS1)** | "Executor com autonomia" | Não consegue executar — sem ferramenta |
| **Jade + Mirla (WS2)** | BDRs para mapear DLs | Sem sistema de tracking |
| **Eduardo + Felipe (WS7)** | DRI | Não aceitaram formalmente |
| **Mayumi (4 WS)** | DRI de WS1, WS3, WS5, WS6 | Sobrecarga, sem suporte |

---

## 4. LACUNAS

### 4.1 Lacunas de Ferramenta

| Lacuna | Evidência | Impacto |
|--------|-----------|---------|
| **Sistema de base de corretores** | WS1 menciona "mapear base" MAS não existe | WS1 não opera |
| **Sistema de DLs** | WS2 menciona 1268 MAS sem sistema de tracking | WS2 não opera |
| **Drive-free tracking** | WS6 quer substituir MAS não há替代 | Meta sem mecanismo |
| **GTD digital** | Notion pendente desde 27/02 | pending.md manual |

### 4.2 Lacunas de Integração

| Lacuna | Evidência | Impacto |
|--------|-----------|---------|
| **Bitrix read/write** | "Não editar nesta fase" + "Somente referência" | WS4 não opera |
| **E-mail automático** | Policy: "nunca automático" + "rascunho + OK" | Cobrança depende de Diego |
| **Google Sheets** | Mencionada em WS1/WS2 MAS não existe | Contrato vazio |
| **One-Pager receive** | Manual: Diego cola e-mail | Sem automação |

### 4.3 Lacunas de Dados

| Lacuna | Evidência | Impacto |
|--------|-----------|---------|
| **Baseline WAU** | WS1: "Iniciar do zero" | Sem meta mensurável |
| **Indicadores DL** | WS2: "1268" MAS sem breakdown | Sem tracking |
| **Score de Praça** | pracas_sprint.md menciona MAS não calculado | Sem métrica |
| **Drive-free %** | WS6: "% drive-free" MAS sem baseline | Meta vaporware |

---

## 5. RISCOS OPERACIONAIS

### 5.1 Risco: Sistema Dependente de Input Manual

| Indicador | Dado |
|-----------|------|
| One-Pager de sprint | Diego cola e-mail manualmente |
| Dados de praças | Diego alimenta memory/projects_orulo.md |
| Cobrança | Morfeu gera rascunho MAS Lara envia manualmente |
| follow-ups | Pendentes em memory/pending.md sem automação |

**Veredicto:** O sistema reduz carga de trabalho manual MAS não elimina dependência de Diego para input.

### 5.2 Risco: Time Sem Ferramenta

| Indicador | Dado |
|-----------|------|
| Corretores | Sem base estruturada — WS1 não opera |
| DLs | Sem sistema de tracking — WS2 não opera |
| Bitrix | "Somente referência" — WS4 não opera |
| Drive | Meta Drive-free MAS sem替代 implementada |

**Veredicto:** O time não tem ferramenta própria. Tudo passa por Diego ou Morfeu.

### 5.3 Risco: Duplicação e Fragmentação

| Indicador | Dado |
|-----------|------|
| WS3 vs pracas_sprint | WS3 fraco, pracas_sprint forte — confusão |
| memory/projects vs memory/pending | Overlap potencial |
| Scripts vs crons | 25 scripts, 30 crons — complexidade |
| Biblioteca vs crm/ | Diferença não clara |

**Veredicto:** Sistema fragmentado com múltiplos pontos de verdade potenciais.

---

## 6. INSUMOS PARA ETAPA 4

### 6.1 O que avaliar na Etapa 4

A **Etapa 4 (Interface com o Time)** deve verificar:

1. **Rituais e cadência:**
   - Os rituais definidos (quinzenal, pulse, check-in) estão funcionando?
   - O time sabe o que fazer após cada ritual?

2. **Comunicação:**
   - Como o time recebe informação? Telegram? E-mail? Drive?
   - Há ponto claro de comunicação ou fragmentação?

3. **Execução:**
   - O time consegue operar sem Diego para cada WS?
   - Onde está o gargalo: ferramenta, método, ou pessoa?

### 6.2 Arquivos de Referência

| Arquivo | Leitura |
|---------|---------|
| 01_inventario_sistema.md | Inventário |
| 02_governanca_workstreams.md | Avaliação WS |
| memory/pending.md | Pendências transversais |
| jobs/cron_plan.yml | Crons de governança |

### 6.3 Pergunta Chave para Etapa 4

- O time sabe o que fazer em cada WS? Ou depende de reunião com Diego?
- Onde está o gargalo: falta ferramenta, falta método, ou falta pessoa?

---

## 7. ACHADOS PRINCIPAIS (Etapa 3)

### ✅ O que existe

- Scripts autossuficientes (output JSON local)
- Pracas_sprint.md como fonte forte de governança
- Memória operacional estruturada (pending, projects, lessons)
- Integrações funcionais (gcal, gmail, tl;dv, Trinks)

### ❌ O que falta

- Sistema de base de corretores (WS1)
- Sistema de tracking de DLs (WS2)
- Bitrix integrado (WS4)
-替代ao Drive (WS6)
- Notion API key (GTD digital)
- Planilhas estruturadas (citadas em WS1/WS2 mas inexistentes)

### ⚠️ O que é risco

- **Sistema dependente de input manual** (Diego cola e-mail, alimenta dados)
- **Time sem ferramenta própria** (opera via Morfeu/Diego)
- **Duplicação WS3 ↔ pracas_sprint** (fragmentação)
- **Meta Drive-free sem mecanismo** (vaporware)
- **Contratos vazios** (C1/C2/C3 placeholders, planilhas inexistentes)

---

*Fim da Etapa 3. Próxima: Etapa 4 — Interface com o Time.*
