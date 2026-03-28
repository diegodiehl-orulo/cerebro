# 01_INVENTARIO_SISTEMA.md — Auditoria Estrutural

> **Etapa:** 1/6 — Inventário do Sistema
> **Data:** 2026-03-08
> **Objetivo:** Mapear o que existe hoje no sistema Órulo dentro e ao redor do OpenClaw

---

## 1. VISÃO GERAL DO INVENTÁRIO

### 1.1 Estrutura de Diretórios

```
/root/.openclaw/workspace/
├── AGENTS.md              # Governança do Morfeu (DRI, Níveis 0-2)
├── SOUL.md                # Persona e tom
├── USER.md                # Perfil completo Diego (431 linhas)
├── IDENTITY.md            # Infraestrutura digital
├── HEARTBEAT.md           # Checklist operacional (10 checagens)
├── MEMORY.md              # Índice de memória
├── TOOLS.md               # Credenciais e notas locais
├── EMAIL_SECURITY.md      # Política de segurança
├── BOOT.md                # Checklist de inicialização
│
├── biblioteca/            # 12 documentos estratégicos (Diego)
│   └── orulo/             # Apenas README (pré-mapeamento)
├── crm/                   # Sistema de inteligência (INDEX, SISTEMA)
│   └── pessoas/           # Perfis (time, clientes, parceiros)
├── governance/            # Workstreams + Praças + Templates
│   ├── workstreams/       # WS1-WS7 (7 pastas)
│   ├── pracas_sprint.md   # Sistema de governança de praças
│   ├── grupos_telegram/   # Estrutura de agentes
│   └── templates/         # Templates de rituais
├── memory/                # Memória operacional
│   ├── daily/             # 8 arquivos de sessão
│   ├── pending.md          # Pendências abertas
│   ├── projects.md        # Status de projetos
│   ├── lessons.md         # Aprendizados
│   ├── people.md          # Diretório de pessoas
│   ├── roles.md           # Mapa de papéis
│   └── personal_care.md  # Cuidados pessoais
├── jobs/                  # Crons e automações
│   ├── cron_plan.yml      # 30 jobs ativos
│   └── prompts/           # 14 prompts de job
├── scripts/               # 25 scripts Python
├── templates/             # 8 templates + drafts
├── automations/           # Índice de automações
├── docs/                  # 5 documentos técnicos
└── archive/               # Histórico
```

### 1.2 Quantificação

| Categoria | Quantidade | Observação |
|-----------|------------|------------|
| Documentos markdown (raiz) | 10 | SOUL, USER, AGENTS, HEARTBEAT, MEMORY, IDENTITY, TOOLS, EMAIL_SECURITY, BOOT, WORKSTREAMS.md |
| Documentos biblioteca | 12 | Biblioteca estratégica completa |
| Workstreams | 7 | WS1-WS7 completos (charter, backlog, plan, kickoff, onepage, pulse) |
| Arquivos de memória | 15+ | daily (8), pending, projects, lessons, people, roles, tasks, personal_care |
| Crons ativos | 30 | Jobs configurados no OpenClaw |
| Prompts de job | 14 | Arquivos .txt em jobs/prompts/ |
| Scripts Python | 25 | Automação e integração |
| Templates | 8 | Comunicação e rituais |

---

## 2. TABELA POR CATEGORIA

### 2.1 Workstreams (WS1–WS7)

| WS | Pasta | Arquivos | Status | Classificação |
|----|-------|----------|--------|----------------|
| WS1 | workstreams/WS1/ | 6 (charter, backlog, plan, kickoff, onepage, pulse) | Pronto para kickoff | A |
| WS2 | workstreams/WS2/ | 6 | Pronto para kickoff | A |
| WS3 | workstreams/WS3/ | 6 | Consolidado | A- |
| WS4 | workstreams/WS4/ | 6 | Consolidado | A |
| WS5 | workstreams/WS5/ | 6 | Consolidado | A- |
| WS6 | workstreams/WS6/ | 9 (inclui checkin, criterios, evidencia) | Consolidado | A |
| WS7 | workstreams/WS7/ | 6 | Consolidado | A- |

### 2.2 Crons (Jobs)

| Tipo | Quantidade | Exemplos |
|------|------------|----------|
| Briefing/Daily | 2 | Daily Briefing (08:45), Briefing Dominical (14h/17h) |
| Governança Praças | 6 | Pulse 2x/sem, check-in Q/S, weekly scan, reminder |
| Monitoramento | 5 | tl;dv (2h), smart email (2h), watchdog crons, erros |
| Saúde/Manutenção | 4 | MiniMax health (09h), diagnóstico (04h), backup |
| Follow-up/Recorrente | 5 | Revisão semanal (16h), check contratos (11h), Auditoria pending |
| Check-ins | 4 | Praças Ter/Sex, checkin Q/S |
| Operacionais | 4 | Trinks (cabelo), cuidados pessoais, email digest, livro check |

### 2.3 Scripts (Automação)

| Categoria | Scripts | Função |
|-----------|---------|--------|
| Google | 4 | gcal_morfeu, create_event, gmail_auth, gmail_send_auth |
| Email | 3 | email_digest, email_digest_v2, smart_email_scan |
| tl;dv | 5 | tldv_monitor, tldv_check, tldv_enrich, tldv_full_pipeline, tldv_store |
| Sprint/Praças | 2 | sprint_email_watcher, tldv_socio_check |
| Contratos | 1 | verifica_contratos_pendentes |
| Trinks | 1 | trinks_booking |
| Utilitários | 6 | minimax_health, minimax_diagnostic, send_scheduled_email, criar_lembrete, criar_viagens, backup_diego |
| Legado | 3 | apply_groq_config, test_gcal, deprecated/ |

### 2.4 Memória

| Arquivo | Conteúdo | Uso |
|---------|----------|-----|
| daily/*.md (8) | Notas de sessão | Contexto imediato |
| pending.md | Pendências abertas | Execução transversal |
| projects.md | Status de projetos | Visão de progresso |
| lessons.md | Aprendizados | Conhecimento acumulado |
| people.md | Diretório de pessoas | Contextualização |
| roles.md | Mapa de papéis | Permissões e responsabilidades |
| personal_care.md | Cuidados pessoais | Rotina de saúde |

---

## 3. PRINCIPAIS CONCENTRAÇÕES

### 3.1 Concentração de Artefatos
- **Governança de Workstreams:** 7 WS × 6-9 arquivos cada = ~50 arquivos de governança
- **Scripts de Automação:** 25 scripts cobrem email, calendário, tl;dv, sprint, contratos, Trinks
- **Crons:** 30 jobs com frequência definida, cobrindo operação completa

### 3.2 Concentração de Conhecimento
- **USER.md (431 linhas):** Perfil completo de Diego, incluindo rotina, valores, team, stack
- **workstreams.md:** Portfólio completo com método, cadência, DRI, sponsor
- **pracas_sprint.md:** Sistema unificado de governança de praças (v2.0)

### 3.3 Concentração de Automação
- **Jobs de Praças:** 6 crons dedicados (pulse, check-in, reminder, weekly scan, watcher)
- **Monitoramento:** 5 crons (tl;dv, email, watchdog, erros)
- **Governança:** 4 crons (revisão semanal, auditoria pending, check contratos)

---

## 4. PRINCIPAIS DISPERSÕES

### 4.1 Dispersão Documental
- **Biblioteca orulo/:** Apenas README (700 bytes). Sem documentos estratégicos operacionais.
- **Templates drafts/:** 2 rascunhos soltos (sem contexto de quando usar)
- **Docs/:** 5 arquivos técnicos soltos (API_POLICY, integrations-setup, etc)

### 4.2 Dispersão de Scripts
- **deprecated/:** 3 scripts marcados como obsoletos mas não removidos
- **Duplicação funcional:** email_digest e email_digest_v2 coexistem (qual está ativo?)

### 4.3 Dispersão de Memória
- **memory/tasks/:** 1 arquivo (task_pessoas_chave) — pasta subutilizada
- **memory/feedback/:** Referenciado em MEMORY.md mas não existe fisicamente

### 4.4 Dispersão de Governança
- **Grupos Telegram:** 3 agentes documentados (morfeu, larissa, claudinei) mas estrutura deallowlist分散
- **Sessões:** 30 jobs usam sessionKeys diferentes (main, morfeu, claudinei, larissa) — complexidade

---

## 5. LACUNAS

### 5.1 LACUNAS ESTRUTURAIS

| Lacuna | Localização | Impacto |
|--------|-------------|---------|
| **Biblioteca Órulo vazia** | biblioteca/orulo/ | Não existe estratégia documentada além do README |
| **projects_orulo.md** | memory/ | Precisa ser populado com C1/C2/C3 por praça |
| **memory/feedback/** | memory/ | Pasta referenciada mas não existe |
| **deprecated scripts** | scripts/deprecated/ | 3 scripts obsoletos sem cleanup |

### 5.2 LACUNAS OPERACIONAIS

| Lacuna | Evidência | Impacto |
|--------|-----------|---------|
| **WS touch tracking** | WS1-WS7 charters | Campos `last_live_touch`, `days_since_touch` = [PREENCHER] |
| **Baseline de WAU** | WS1 charter | "Iniciar do zero" — sem baseline |
| **SLAs por praça** | pracas_sprint.md | Estágios definidos mas sem métricas量化 |
| **Bitrix integração** | Jobs/Gov | "Integração a definir" em múltiplos pontos |

### 5.3 LACUNAS DE GOVERNANÇA

| Lacuna | Onde | status |
|--------|------|--------|
| **7 WS sem kickoff.realizado** | workstreams/ | Classificação A mas sem evidência de kickoff executado |
| **C1/C2/C3 populados?** | WS1-WS7 plans | Cada WS tem plan_quinzenal_sprint01.md mas não validado se populado |
| **Pulse executado?** | WS1-WS7 pulse_v0 | Arquivos existem mas não há evidência de uso real |

---

## 6. RISCOS DO INVENTÁRIO ATUAL

### 6.1 Risco: Documentação ≠ Operação

| Indicador | Evidência |
|-----------|-----------|
| 7 WS com charter completo | MAS touch tracking vazio |
| 30 crons ativos | MAS 3 jobs com consecutiveErrors > 0 |
| 14 prompts de job | MAS alguns referenciam scripts que podem estar obsoletos |

**Análise:** O sistema tem aparência de maturidade (arquivos existem) mas não há evidência de operação real.

### 6.2 Risco: Sobrecarga do Sponsor

| Indicador | Dado |
|-----------|------|
| WS1 DRI = Mayumi | Mayumi também é DRI de WS3, WS5, WS6 (4 WS) |
| Sponsor de todos WS = Diego | 7 workstreams para oversight único |
| Crons que alertam Diego | ~10+ crons enviam Telegram para Diego |

**Análise:** Concentração de decisão e oversight no sponsor (Diego) e DRI (Mayumi) é extrema.

### 6.3 Risco: Complexidade Técnica

| Indicador | Dado |
|-----------|------|
| 30 jobs ativos | Múltiplas sessões (main, morfeu, claudinei, larissa) |
| 25 scripts | Alguns duplicados ou obsoletos |
| Integrações parciais | Gmail, gcal, Trinks, tl;dv — cada uma com token/credencial |

**Análise:**many moving parts com baixa evidência de consolidação ou cleanup.

---

## 7. INSUMOS PARA ETAPA 2

### 7.1 O que avaliar na Etapa 2

A partir deste inventário, a **Etapa 2 (Governança dos Workstreams)** deve verificar:

1. **Complitude real dos WS:**
   - Os 6-9 arquivos por WS estão populados ou são templates vazios?
   - Os campos [PREENCHER] foram preenchidos?

2. **Operação real vs. documentação:**
   - Há evidência de que os pulses foram executados?
   - Há evidência de que os kickoffs ocorreram?
   - Os C1/C2/C3 têm dono + prazo + evidência?

3. **Governança ativa:**
   - Os rituais (quinzenal, pulse, check-in) estão rodando na prática?
   - Os crons de governança estão funcionando?

4. **Dependência do sponsor:**
   - Qual WS consegue operar sem Diego?
   - Qual WS precisa de Diego para cada ciclo?

### 7.2 Arquivos de Referência

| Arquivo | Leitura Obrigatória |
|---------|---------------------|
| governance/workstreams.md | Portfólio completo |
| governance/pracas_sprint.md | Sistema de praças |
| governance/workstreams/WS{1-7}/charter.md | Um por WS |
| governance/workstreams/WS{1-7}/plan_quinzenal_sprint01.md | Um por WS |
| memory/pending.md | Pendências em aberto |

### 7.3 Perguntas Chave para Etapa 2

1. Os 7 WS estão operacionais (A) ou apenas estruturados (B/C)?
2. Os rituais de governança estão rodando ou são documentação?
3. O sistema reduz dependência do sponsor ou apenas formaliza?
4. Onde há mais lacuna: estrutura documental ou execução real?

---

## 8. ACHADOS PRINCIPAIS (Etapa 1)

### ✅ O que existe

- 7 workstreams com estrutura completa (charter, backlog, plan, kickoff, onepage, pulse)
- Sistema de governança de praças documentado (v2.0)
- 30 crons cobrindo operação, governança, monitoramento
- 25 scripts de automação
- Memória operacional estruturada (daily, pending, projects, lessons)
- Biblioteca estratégica (12 documentos)
- HEARTBEAT.md com 10 checagens operacionais
- AGENTS.md com Níveis 0-2 definidos

### ❌ O que falta

- Biblioteca Órulo vazia (apenas README)
- Campos [PREENCHER] em todos os charters (touch tracking)
- Evidência de kickoffs executados
- Evidência de pulses executados
- projects_orulo.md populado com C1/C2/C3 por praça
- memory/feedback/ (pasta não existe)
- Cleanup de scripts obsoletos

### ⚠️ O que é risco

- Documentação ≠ Operação real
- Sobrecarga de Mayumi (4 WS) e Diego (7 WS como sponsor)
- 30 jobs + 4 sessões = complexidade técnica alta
- Duplicação (email_digest v1/v2, scripts deprecated)
- 3 jobs com consecutiveErrors (Watchdog, Briefing Dominical, Email Qui)

---

*Fim da Etapa 1. Próxima: Etapa 2 — Governança dos 7 Workstreams.*
