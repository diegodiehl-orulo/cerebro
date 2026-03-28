# MEMORY.md — Índice de Memória do Morfeu

*Atualizado: 2026-03-28*
*Atualização anterior: 2026-03-27 (pós-curso SUPER CÉREBRO V2)*

---

## 🏛️ SISTEMA OPERACIONAL COMERCIAL ÓRULO — HIERARQUIA DE VERDADE

> Consolidado em 11/03/2026. Seção soberana — sempre prevalece sobre frameworks anteriores.
> **Referência completa:** `memory/orulo_sistema_operacional.md`

**Unidade de resultado:** Praça → métrica soberana: MRR/ARR por praça.

**Workstreams oficiais (7):**
WS1 Comunicação Corretores | WS2 Jornada DL→Pago | WS3 Execução Territorial | WS4 Estrutura Comercial e CRM | WS5 Marketing Event Driven | WS6 Embaixadoras Drive Free | WS7 Modelo Econômico Praça

**Hierarquia de verdade:**
1. Google Drive → fonte oficial (governança, docs, templates, histórico)
   - **URL:** https://drive.google.com/drive/folders/1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM
   - **ID:** `1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM`
2. Planilha `WS_OPERATING_SYSTEM_H1_2026` → cockpit (backlog, decisões, ritos)
   - **ID:** `1pYmAUBEJQXvN1yxYZb1ybRVtr_UbM7ft`
3. OpenClaw → leitura, síntese, auditoria, apoio executivo

**Regra de conflito:** Drive > memória OpenClaw. Sempre.

**Backlog inicial:** 70 itens consolidados (Sprint 0 + Sprint 1, todos os 7 WS) — base oficial desde 11/03/2026.

**Modo auditor ativo:** rodar rotina leve | auditoria curta | auditar WSX | preparar reunião de WSX

**Restrições OpenClaw:** NÃO cria backlog oficial | NÃO substitui Drive | NÃO inventa governança | NÃO cria sistemas paralelos | NÃO corrige sem instrução explícita.

---

---

## 🧠 SISTEMA DE MEMÓRIA — CICLO COMPLETO

### CURTO PRAZO (Instantâneo)
| Recurso | Função |
|---------|--------|
| `memory_search` | Busca semântica instantânea (Gemini embeddings) |
| `memory_get` | Leitura de snippets específicos de arquivos |
| `memory/daily/YYYY-MM-DD.md` | Notas brutas da sessão (captura raw) |
| Transcript de sessão | Automático (preservado pelo OpenClaw) |

### MÉDIO PRAZO (1-30 dias)
| Recurso | Função |
|---------|--------|
| `memory/daily/*.md` | Contexto acumulado por dia |
| `memory/pending.md` | Aguardando input ou ação |
| `memory/projects.md` | Status de projetos ativos |
| `memory/people.md` | Diretório de pessoas — canal, permissão, contato |
| `memory/roles.md` | Mapa de papéis, responsabilidades e permissões do Morfeu |
| Follow-ups | Arquivos temáticos (`followups-*.md`) |

### LONGO PRAZO (Permanente)
| Recurso | Função |
|---------|--------|
| `MEMORY.md` | Este índice — mapa geral |
| `SOUL.md` | Persona e tom do Morfeu |
| `IDENTITY.md` | Identidade e infraestrutura |
| `USER.md` | Perfil completo do Diego |
| `HEARTBEAT.md` | Checklist operacional permanente |

---

## 📂 ESTRUTURA DE ARQUIVOS

```
/root/.openclaw/workspace/
├── SOUL.md              # Alma e personalidade
├── IDENTITY.md          # Identidade e infraestrutura
├── USER.md              # Contexto completo de Diego (431 linhas)
├── AGENTS.md            # Protocolos operacionais
├── HEARTBEAT.md         # Checklist de verificação periódica
├── MEMORY.md            # Este índice
├── TOOLS.md             # Notas locais (credenciais, URLs)
├── EMAIL_SECURITY.md    # Política de segurança de email
├── BOOT.md              # Checklist de inicialização
├── BOOTSTRAP.md         # [Pendente]
│
├── memory/
│   ├── daily/           # Notas brutas por dia
│   ├── decisions.md     # Decisões estratégicas
│   ├── lessons.md       # Aprendizados (🔒 estratégicos + ⏳ táticos)
│   ├── people.md        # Pessoas-chave
│   ├── pending.md       # Pendências em aberto
│   ├── projects.md      # Projetos ativos
│   └── feedback/        # Feedback loops (content, tasks, recommendations)
│
├── biblioteca/           # Biblioteca estratégica (12 docs)
├── biblioteca/orulo/    # Documentos da Órulo (16 docs)
├── automations/         # Mapa de crons e scripts
├── scripts/             # Scripts Python
├── governance/          # Políticas e regras operacionais por praça
│   └── pracas_sprint.md # Sistema unificado de governança (v2.0)
├── templates/           # Templates reutilizáveis
│   ├── sprint_onepager.md         # One-pager do sócio local
│   ├── sprint_meeting_minutes.md  # Ata + contrato de sprint
│   ├── email_onepager_request.md  # E-mail de solicitação (3 versões)
│   ├── email_sprint_feedback.md   # Retorno de Diego ao sócio
│   └── checkin_questions.md       # 4 perguntas + rascunho de check-in
├── jobs/                # Jobs e crons de governança
│   ├── cron_plan.yml    # Plano unificado (v2.0) — 8 jobs
│   └── prompts/         # Prompts por job (10 arquivos ativos)
└── archive/             # Versões anteriores (não deletar)
```

---

## 🔄 CICLO DE VIDA DA MEMÓRIA

```
Sessão (conversa)
       ↓
memory/daily/YYYY-MM-DD.md (raw capture)
       ↓ heartbeat (a cada 90min)
Verificar pendências, projetos, viagens
       ↓ consolidação periódica
Topic files (pending, projects, decisions, lessons)
       ↓ atualização
MEMORY.md (índice atualizado)
```

---

## ⚙️ PROCESSOS AUTOMATIZADOS

| Processo | Frequência | Função |
|----------|------------|--------|
| **Heartbeat** | 90min | Verificar pendências, notas diárias, projetos, viagens |
| **Daily Briefing** | Seg-Sex 08:45 | Resumo do dia + agenda |
| **Smart Email Scan** | 2h (09h–18h, seg-sex) | Triagem de emails importantes |
| **Monitor tl;dv** | 2h (10h–18h, seg-sex) | Consolidar transcrições de reuniões |
| **Check Contratos** | Seg-Sex 11:20 | Pendências de assinatura |
| **Watchdog Crons** | Diário 09:15 | Verificar saúde dos crons |
| **Revisão Semanal** | Sex 16h | Análise e planejamento semanal |
| **Auditoria pending.md** | Sex 17h | Limpeza e relevância de pendências |
| **Briefing Dominical** | Dom 16h + 17h | Coleta + análise semanal |
| **Harvester de Memória** | Dom 09h | Consolidação estratégica da memória |
| **Madrugada** | Seg-Sáb 02h | Insight e consolidação da memória diária |

---

## 🛠️ SKILLS ATIVAS

| Skill | Função |
|-------|--------|
| `weather` | Clima e previsões (wttr.in / Open-Meteo) |
| `healthcheck` | Segurança e hardening do servidor |
| `skill-creator` | Criar/editar skills customizadas |
| `tmux` | Controlar sessões tmux remoto |
| `clawhub` | Buscar/instalar skills do hub |

*Skills unavailable: brainstorming, google-calendar, marketing, qmd-local-search, openai-image-gen, openai-whisper-api (não instaladas)*

---

## 📸 ESTADO ATUAL

### Mudanças Estruturais (11/03/2026)
- **SOUL.md v3:** Morfeu reposicionado como Gestor de Projetos dos Workstreams + estrategista. Novo caráter: rastreia DRI, prazo, evidência, cadência. Sempre termina com próxima ação com dono e prazo.
- **AGENTS.md v3:** Papel atualizado — gestor de projetos como camada principal. Cobra DRI vencido, evidência ausente, rito pendente.
- **CONSOLIDACAO_11032026:** Documento de fechamento do dia salvo localmente em `memory/orulo/` e no Drive (`01_GOVERNANCA_GERAL`, ID: `1BTXufJ2g7dD2VrgCd0IkoC9WGqz2Zdc13cirDKFUzj8`)

### Projetos Ativos
- **Crons/Jobs** — 22+ jobs ativos (LLM Policy v2.1 aplicada) | Snapshot: `/root/backups/openclaw_snapshot_20260306_101436/`
- **MiniMax** — Coding Plan Key configurada ✅ (05/03) | Lightning PROIBIDO no Starter
- **Livro "Palavras que Vendem"** — ✅ CONCLUÍDO em 26/03
- **Órulo** — Operação contínua | Governança de Praças v2.0 ✅ | Curitiba (Zanella) + Vitória (Kneip)
- **LLM Policy v2.1** — Fases 1+2 concluídas | Fase 3 aguarda `"OK Fase 3"` de Diego

### Pendências em Aberto
- `memory/projects_orulo.md` — estágio e sprint por praça (aguarda Diego)
- LLM Policy Fase 3 — aguarda OK Diego
- Heartbeat [PESSOAL] — stub a construir

---

## 🔑 CONFIGURAÇÃO TÉCNICA

- **Heartbeat:** 90min (model: minimax/MiniMax-M2.5)
- **Context tokens:** 160k | **Reserve:** 30k | **Memory flush:** ativo
- **Busca semântica:** Gemini gemini-embedding-001
- **Modelo principal:** MiniMax M2.5 | **Fallback automático:** desativado (LLM Policy v2.1)
- **Jobs ativos:** 22+ | **Política:** `sistema/llm_policy_v2.1.md`

---

*Próxima revisão automática: dom 23/03/2026 às 09h (Harvester de Memória)*
