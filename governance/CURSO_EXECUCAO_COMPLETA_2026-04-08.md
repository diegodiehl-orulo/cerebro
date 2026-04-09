# CURSO BRUNO OKAMOTO — PLANO DE EXECUÇÃO COMPLETA
## openclaw-BrunoOkamoto · Diego Diehl · 2026-04-08

**Objetivo:** Consumir e implementar TODO o curso do Bruno Okamoto, mapeando cada módulo contra o estado atual do Morfeu.
**Contexto:** Diego já tem sistema rodando (Morfeu v4, FASE 0 + Sprint 1–3 ✅). Curso tem 11 módulos + aulas extras.
**Formato:** Cards (bullets + emojis, sem pipes). Máximo 4 linhas por bloco.

---

## VISÃO GERAL — REPO COURSE

```
11 MÓDULOS + AULAS EXTRAS
├── pdfs/        — 11 módulos em PDF
├── prompts/      — prompts guiados por aula
├── templates/    — SOUL, USER, AGENTS, IDENTITY, MEMORY, HEARTBEAT
├── prds/        — immune-system, multi-agent-setup, vps-setup, memory-architecture
├── skills/       — deep-research, seguranca, skills-by-profile
├── configs/     — cron-examples, modelo-config
├── docs/        — troubleshooting, custos, 10-regras, checklist-final
├── use-cases/   — business, community, content, productivity, research, support
├── qa/          — runbooks de diagnóstico
├── diagramas/   — arquitetura visual Excalidraw
└── landing-pages/ — referência
```

---

## MAPA DE COBERTURA DO MORFEU ATUAL

| Módulo Course | Tema | Cobertura Morfeu | Status |
|---|---|---|---|
| M01 | Fundações (setup, identidade, governança) | ✅ AGENTS, IDENTITY, SOUL, TOOLS | Ja feito |
| M02 | Memória em 3 camadas | ✅ MEMORY.md + memory/*.md + ARCHITECTURE | Ja feito |
| M03 | Subagentes + Orquestração | ✅ SUBAGENT_CONTRACT + sessions_spawn | Ja feito |
| M04 | Self-healing + Runbooks | ✅ SELF_HEALING_RUNBOOKS.md | Ja feito |
| M05 | KAIROS watchdog + Proatividade | ✅ kairos_watchdog.md + autodream.md | Ja feito |
| M06 | Multi-agent setup | ⚠️ Parcial — 3 bots (Morfeu, Larissa, Claudinei) | Parcial |
| M07 | Skills authoring | ⚠️ Parcial — skill-creator existe | Parcial |
| M08 | Cron + Automations | ✅ Jobs + cron config | Ja feito |
| M09 | Immune system | ❌ Não tem documento dedicado | A fazer |
| M10 | Use cases (business, productivity, etc.) | ⚠️ Parcial — only Órulo use case | A expandir |
| M11 | VPS + Infra (Hostinger) | ✅ TOOLS.md (VPS info) + vps-access skill | Ja feito |
| Extra | Troubleshooting + custos | ⚠️ Parcial — SELF_HEALING, custos.md do course | A fazer |
| Extra | Deep research skill | ❌ Não instalado | A instalar |
| Extra | Seguranca skill | ❌ Não instalado | A instalar |
| Extra | Landing pages | ❌ N/A — não se aplica | Skip |

---

## PLANO DE EXECUÇÃO — ORDEM CORRETA

### BLOCO 1 — FUNDAÇÕES JÁ COBERTAS ✅
(Ordem do course: M01 + M02 + parcialmente M11)

---

**M01 — Fundações: SOUL, USER, AGENTS, IDENTITY, HEARTBEAT**
📂 `templates/` — arquivos base do course
👤 DRI: Morfeu | Esforço: N/A | Prioridade: P0

• **O que já existe:** SOUL.md ✅ · IDENTITY.md ✅ · AGENTS.md ✅ · USER.md ✅ · HEARTBEAT.md ✅
• **Ação:** Nenhuma — ja coberto pelo Morfeu v4
• **Status:** ✅ Feito — nenhuma ação necessária

---

**M02 — Memória em 3 Camadas**
📂 `prds/memory-architecture.md` + `memory/*.md`
👤 DRI: Morfeu | Esforço: N/A | Prioridade: P0

• **O que já existe:** MEMORY.md (índice) · memory/*.md (topic files) · 3 camadas documentadas
• **Ação:** Nenhuma — arquitetura implementada na FASE 1 Sprint 1
• **Status:** ✅ Feito — nenhuma ação necessária

---

**M11 — VPS Setup (Hostinger)**
📂 `prds/vps-setup-hostinger.md` + `skills/vps-access/`
👤 DRI: Claudinei | Esforço: N/A | Prioridade: P0

• **O que já existe:** TOOLS.md (IP, credenciais, alias SSH) · vps-access skill ✅ · Vaultwarden ✅
• **Ação:** Nenhuma — infraestrutura operacional
• **Status:** ✅ Feito — nenhuma ação necessária

---

### BLOCO 2 — SUBAGENTES + GOVERNANÇA ✅
(Ordem do course: M03 + parcialmente M06)

---

**M03 — Subagentes + Contract Formal**
📂 `governance/SUBAGENT_CONTRACT.md` + `prds/multi-agent-setup.md`
👤 DRI: Morfeu | Esforço: N/A | Prioridade: P0

• **O que já existe:** SUBAGENT_CONTRACT.md ✅ · contract de 4 campos ✅ · sessions_yield ✅
• **Ação:** Nenhuma — contract implementado
• **Status:** ✅ Feito — nenhuma ação necessária

---

**M06 — Multi-Agent Setup (parcial)**
📂 `prds/multi-agent-setup.md` + configs/
👤 DRI: Morfeu + Diego | Esforço: Médio | Prioridade: P1

• **O que existe:** 3 bots: Morfeu (default), Larissa (larissa bot), Claudinei (claudinei bot)
• **O que falta:** Documento `multi-agent-setup.md` do course — belum comparado
• **Ação concreta:** Baixar repo → ler `prds/multi-agent-setup.md` → comparar com setup atual
• **Dependência:** Nenhuma
• **Status:** ⚠️ Parcial — 3 bots funcionando, doc do course nao validado
• **Prazo sugerido:** 2026-04-15

---

### BLOCO 3 — SKILLS 📚
(Ordem do course: M07 + skills/ do repo)

---

**M07 — Skill Authoring**
📂 `skills/skill-creator/SKILL.md`
👤 DRI: Morfeu | Esforço: Baixo | Prioridade: P1

• **O que existe:** `skill-creator` skill ✅ — ja permite criar/editar skills
• **O que falta:** Validar se a metodologia do course添   é mais robusta que a atual
• **Ação concreta:** Baixar repo → ler `skills/skill-creator/SKILL.md` → propor melhorias se houver
• **Dependência:** M06 (repo clonado)
• **Status:** ⚠️ Parcial — skill existe mas pode ter gap vs course
• **Prazo sugerido:** 2026-04-15

---

**SKILL — Deep Research (não instalada)**
📂 `skills/deep-research/`
👤 DRI: Morfeu | Esforço: Médio | Prioridade: P2

• **O que é:** Skill de pesquisa profunda com web search + synthesis
• **O que existe:** `summarize` skill ✅ + web_search tool ✅
• **Ação concreta:** Instalar via clawhub ou adaptar `summarize` skill para cover research
• **Dependência:** M07 (skill-creator)
• **Status:** ❌ Não instalado — usar summarize como fallback
• **Prazo sugerido:** 2026-05-01

---

**SKILL — Segurança (não instalada)**
📂 `skills/seguranca/`
👤 DRI: Morfeu | Esforço: Médio | Prioridade: P2

• **O que é:** Hardening, auditoria de segurança, check de vulnerabilidades
• **O que existe:** `healthcheck` skill ✅ — ja cobre host security
• **Ação concreta:** Baixar repo → comparar healthcheck atual vs course → gaps?
• **Dependência:** M07 (repo clonado)
• **Status:** ❌ Não instalado — healthcheck cobre parcialmente
• **Prazo sugerido:** 2026-05-01

---

**SKILL — Skills by Profile (não instalada)**
📂 `skills/skills-by-profile.md`
👤 DRI: Morfeu | Esforço: Baixo | Prioridade: P2

• **O que é:** Guia de quais skills instalar por perfil de uso
• **Ação concreta:** Ler do repo → gerar documento de skills recomendadas para Diego (perfil: executivo comercial)
• **Dependência:** M07 (repo clonado)
• **Status:** ❌ Não instalado — criar baseado no course
• **Prazo sugerido:** 2026-05-01

---

### BLOCO 4 — USE CASES 📊
(Ordem do course: M10 + use-cases/)

---

**M10 — Use Cases (business, productivity, research, etc.)**
📂 `use-cases/business/` · `use-cases/productivity/` · `use-cases/research/`
👤 DRI: Morfeu | Esforço: Alto | Prioridade: P1

• **O que existe:** Only Órulo use case implementado (vendas-analytics, vendas-audit, etc.)
• **O que falta:** Validar cada pasta de use-cases do course vs o que ja existe
• **Ação concreta:** Baixar repo → listar todos os use-cases → mapear contra skills existentes
• **Sub-ação — business/:** Ja temos vendas-analytics + vendas-audit + vendas-report ✅
• **Sub-ação — productivity/:** Verificar se há use-cases que agregam ao Morfeu atual
• **Sub-ação — research/:** deep-research skill covers this (quando instalada)
• **Sub-ação — support/:** N/A — contexto Órulo não tem support external
• **Sub-ação — community/:** N/A — contexto Órulo não tem community management
• **Dependência:** M07 (repo clonado)
• **Status:** ⚠️ Parcial — Órulo coberto, outros use cases nao validados
• **Prazo sugerido:** 2026-05-15

---

### BLOCO 5 — SELF-HEALING + IMMUNE SYSTEM 🛡️
(Ordem do course: M04 + M09)

---

**M04 — Self-healing + Runbooks**
📂 `governance/SELF_HEALING_RUNBOOKS.md` + `qa/runbooks/`
👤 DRI: Morfeu | Esforço: N/A | Prioridade: P0

• **O que existe:** 5 runbooks formais (RB1–RB5) ✅ + matriz de incidentes ✅
• **Ação:** Baixar repo → ler `qa/runbooks/` → comparar com runbooks atuais → gaps?
• **Dependência:** Nenhuma
• **Status:** ✅ Feito — runbooks ativos, validar se course添   mais
• **Prazo sugerido:** 2026-04-15

---

**M09 — Immune System (não existe documento dedicado)**
📂 `prds/immune-system.md`
👤 DRI: Morfeu | Esforço: Médio | Prioridade: P1

• **O que é:** Sistema de proteção contra prompts injection, jailbreak, dados sensíveis
• **O que existe:** UNDERCOVER_LAYER.md ✅ + SELF_HEALING ✅
• **Ação concreta:** Baixar repo → ler `prds/immune-system.md` → adaptar para Morfeu
• **Dependência:** Nenhuma
• **Status:** ❌ Não tem — implementar baseado no course
• **Prazo sugerido:** 2026-04-20

---

### BLOCO 6 — CRON + AUTOMATIONS ⚙️
(Ordem do course: M08)

---

**M08 — Cron + Configurações**
📂 `configs/cron-examples.md` + `configs/modelo-config.md`
👤 DRI: Morfeu | Esforço: Baixo | Prioridade: P1

• **O que existe:** 38 cron jobs ativos + `cron-examples` no course
• **Ação concreta:** Baixar repo → ler `configs/cron-examples.md` → comparar com jobs atuais
• **Ação concreta:** Verificar se há jobs novos que facam sentido para Diego (ex: notary, notary-discovery)
• **Dependência:** M06 (repo clonado)
• **Status:** ⚠️ Parcial — jobs existem, course pode ter patterns novos
• **Prazo sugerido:** 2026-04-20

---

### BLOCO 7 — DOCUMENTAÇÃO + extras 📋
(Ordem do course: docs/ + troubleshooting + checklist + custos)

---

**DOCS — Troubleshooting + 10 Regras Invioláveis**
📂 `docs/troubleshooting.md` + `docs/10-regras-inviolaveis.md`
👤 DRI: Morfeu | Esforço: Baixo | Prioridade: P2

• **O que existe:** SELF_HEALING_RUNBOOKS.md ✅ cobre troubleshooting
• **Ação:** Baixar repo → ler docs → integrar regras relevantes ao SOUL/AGENTS
• **Dependência:** M06 (repo clonado)
• **Status:** ⚠️ Parcial — integrar se houver gap
• **Prazo sugerido:** 2026-05-01

---

**DOCS — Custos (OpenClaw + VPS)**
📂 `docs/custos.md`
👤 DRI: Morfeu | Esforço: Baixo | Prioridade: P2

• **O que é:** Planilha de custos operacionais (tokens, API, VPS)
• **Ação:** Baixar repo → adaptar para contexto Diego (já tem custo知道的)
• **Dependência:** M06 (repo clonado)
• **Status:** ❌ Não tem — criar para controle de custo operacional
• **Prazo sugerido:** 2026-05-15

---

**DOCS — Checklist Final**
📂 `docs/checklist-final.md`
👤 DRI: Morfeu | Esforço: Baixo | Prioridade: P2

• **O que é:** Checklist de implementação completa do sistema
• **Ação:** Baixar repo → adaptar para contexto Diego → rodar auto-checklist
• **Dependência:** M06 (repo clonado)
• **Status:** ❌ Não tem — adaptar do course
• **Prazo sugerido:** 2026-05-15

---

### BLOCO 8 — DIAGRAMAS + LANDING PAGES 🎨
(Não prioritário para contexto Órulo)

---

**DIAGRAMAS — Arquitetura Visual Excalidraw**
📂 `diagramas/`
👤 DRI: Morfeu | Esforço: Baixo | Prioridade: P3

• **O que é:** Visualização da arquitetura do sistema em Excalidraw
• **Ação:** Baixar repo → adaptar diagramas para o Morfeu → usar em presentaciones
• **Dependência:** M06 (repo clonado)
• **Status:** ❌ Não tem — nice to have
• **Prazo sugerido:** 2026-06-01

---

**LANDING PAGES — Referência**
📂 `landing-pages/`
👤 DRI: N/A | Esforço: N/A | Prioridade: P0 (Skip)

• **O que é:** Templates de landing page para vender serviços de IA/OpenClaw
• **Ação:** Nenhuma — não se aplica ao contexto Órulo
• **Status:** ⏭️ Skip — fora de escopo

---

## RESUMO — TABELA DE AÇÕES

| Bloco | Módulo/Aula | Ação | Prio | Esforço | Dependência | Status | Prazo |
|-------|-------------|------|------|---------|------------|--------|-------|
| 1 | M01 Fundações | Nenhuma | P0 | N/A | Nenhuma | ✅ Feito | — |
| 1 | M02 Memória 3 Camadas | Nenhuma | P0 | N/A | Nenhuma | ✅ Feito | — |
| 1 | M11 VPS Setup | Nenhuma | P0 | N/A | Nenhuma | ✅ Feito | — |
| 2 | M03 Subagentes | Nenhuma | P0 | N/A | Nenhuma | ✅ Feito | — |
| 2 | M06 Multi-Agent Setup | Comparar doc course vs atual | P1 | Médio | Repo | ⚠️ Parcial | 15/04 |
| 3 | M07 Skill Authoring | Validar vs skill-creator | P1 | Baixo | Repo | ⚠️ Parcial | 15/04 |
| 3 | Skill: Deep Research | Instalar/adaptar | P2 | Médio | M07 | ❌ | 01/05 |
| 3 | Skill: Segurança | Comparar vs healthcheck | P2 | Médio | Repo | ❌ | 01/05 |
| 3 | Skill: Skills by Profile | Gerar doc para Diego | P2 | Baixo | Repo | ❌ | 01/05 |
| 4 | M10 Use Cases | Mapear todos vs existentes | P1 | Alto | Repo | ⚠️ Parcial | 15/05 |
| 5 | M04 Self-healing | Comparar runbooks vs current | P0 | N/A | Nenhuma | ✅ Feito | 15/04 |
| 5 | M09 Immune System | Implementar immune-system | P1 | Médio | Nenhuma | ❌ | 20/04 |
| 6 | M08 Cron+Configs | Comparar cron-examples | P1 | Baixo | Repo | ⚠️ Parcial | 20/04 |
| 7 | Docs: Troubleshooting | Integrar se gap | P2 | Baixo | Repo | ⚠️ Parcial | 01/05 |
| 7 | Docs: Custos | Criar tracker de custos | P2 | Baixo | Repo | ❌ | 15/05 |
| 7 | Docs: Checklist Final | Adaptar para Diego | P2 | Baixo | Repo | ❌ | 15/05 |
| 8 | Diagramas | Adaptar Excalidraw | P3 | Baixo | Repo | ❌ | 01/06 |
| 8 | Landing Pages | Skip | P0 | N/A | N/A | ⏭️ Skip | — |

---

## PRÓXIMA AÇÃO CRÍTICA — Bloco 2 (M06)

**Ação:** Clonar o repo do Bruno Okamoto para validar conteúdo dos módulos.
```
git clone https://github.com/brunookamoto/openclaw-BrunoOkamoto.git /tmp/openclaw-course
```

**Se git falhar (sem credentials):**
→ Pedir a Diego para fazer clone manual e disponibilizar localmente
→ Ou usar clawhub para instalar skills individualmente

**Se repo inacessível:**
→ Gerar plano baseado na estrutura conhecida (11 módulos + extras listados)
→ Preencher colunas "Status" e "Ação" baseadas apenas no que o course descreve
→ Marcar itens como "⚠️ A validar quando repo disponivel"

---

## ROADMAP SIMPLIFICADO — ORDEM DE EXECUÇÃO

```
abril 2026
├── 08-14/04: M06 Multi-Agent (comparar docs) + M04 Runbooks (comparar)
├── 15-20/04: M09 Immune System (implementar) + M08 Cron (comparar)
└── 21-30/04: M07 Skill Authoring + skills faltantes (deep-research, seguranca)

maio 2026
├── 01-15/05: M10 Use Cases (mapear todos) + Docs custos/checklist
└── 15-31/05: M06 Multi-Agent (implementar gaps) + Diagramas (se tempo)

junho 2026
└── 01+/06: Extras + refinamentos + auditoria final
```

---

**Documento gerado:** 2026-04-08
**Próxima microação:** Clonar repo do Bruno Okamoto + comparar `prds/multi-agent-setup.md` com setup atual de 3 bots
**DRI:** Morfeu
**Validação Diego:** needed for M06, M09, M10 decisions
