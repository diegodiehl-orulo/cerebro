# TOOLKIT.md — Inventário de Ferramentas do Morfeu
## M6 — Stack de Ferramentas (Sprint 3 FASE 2)

**Versão:** 1.0  
**Data:** 2026-04-03  
**DRI:** Morfeu  
**Status:** ✅ Inventário inicial — 26 ferramentas catalogadas  

---

## FILOSOFIA DE USO

> Use a ferramenta certa para cada contexto. Não invente quando a ferramenta existe.
> Antes de "não consigo fazer X", consultar este toolkit.

**Regra de economia:**
- Ferramentas rápidas (exec, read) → usar direto
- Ferramentas pesadas (browser, pdf, subagente) → só quando necessário
- Modelos mais caros (Opus, Pro) → só para decisões estratégicas

---

## CATEGORIA 1 — ARQUIVOS E SISTEMA

| Ferramenta | Uso principal | Quando NÃO usar |
|------------|---------------|-----------------|
| `Read` | Ler conteúdo de arquivo local | Arquivos >2000 linhas sem offset |
| `Write` | Criar/sobrescrever arquivo | Edição pontual (use Edit) |
| `Edit` | Edição precisa por trecho | Substituições grandes (use Write) |
| `exec` | Rodar comandos shell | Comandos destrutivos sem `--dry-run` |
| `process` | Gerenciar processos em background | Tarefas rápidas (<10s) |

**Scripts disponíveis em `scripts/`:**
- `autodream.py` — diagnóstico de memória (M3)
- `archive_daily.py` — archive de daily/ (G3)
- `testar_scripts.py` — health check de scripts
- `gcal_morfeu.py` — agenda Google Calendar
- `smart_email_scan.py` — scan inteligente de emails
- `email_digest_v2.py` — digest de emails
- `backup_diego.sh` — backup para Google Drive
- `drive_audit.py` — auditoria de Drive
- `minimax_health.py` — health check MiniMax
- `quota_estimator.py` — estimativa de quota

---

## CATEGORIA 2 — WEB E PESQUISA

| Ferramenta | Uso principal | Custo relativo |
|------------|---------------|----------------|
| `web_search` | Pesquisa DuckDuckGo (título + snippet) | Baixo |
| `web_fetch` | Extrair conteúdo de URL específica | Médio |
| `browser` | Automação de browser (login, forms, cliques) | Alto |

**Regra:** `web_search` → se snippet resolve → fim. Só usar `web_fetch` se precisar do conteúdo completo. `browser` → último recurso (sessão com login).

---

## CATEGORIA 3 — MEMÓRIA E CONTEXTO

| Ferramenta | Uso principal | Regra de uso |
|------------|---------------|--------------|
| `memory_search` | Busca semântica em MEMORY.md + topic files | SEMPRE antes de responder sobre histórico |
| `memory_get` | Leitura de snippet específico (from/lines) | Após memory_search — não carregar full |
| `session_status` | Status + uso de contexto atual | Quando contexto próximo do limite |
| `sessions_history` | Histórico de outra sessão | Somente via grep/semantic — não full load |

**Hierarquia de memória:**
1. Arquivo de workspace (read) → verdade local
2. memory_search → verdade histórica
3. Pergunta para Diego → quando esgotei fontes

---

## CATEGORIA 4 — COMUNICAÇÃO

| Ferramenta | Uso principal | Quando usar |
|------------|---------------|-------------|
| `message` (send) | Enviar mensagem proativa | Relatórios, alertas, follow-ups |
| `message` (react) | Reagir a mensagem | Confirmação leve (sem resposta) |
| `tts` | Texto para voz | Quando Diego pedir áudio |
| `cron` | Criar/gerenciar jobs agendados | Tarefas recorrentes |

---

## CATEGORIA 5 — ANÁLISE DE CONTEÚDO

| Ferramenta | Uso principal | Modelo recomendado |
|------------|---------------|-------------------|
| `image` | Analisar imagem ou screenshot | flash (rápido) / sonnet (detalhado) |
| `pdf` | Analisar documento PDF | pro (nativo Anthropic/Google) |
| `canvas` | Visualizar UI / snapshot de página | — |

---

## CATEGORIA 6 — GOOGLE WORKSPACE (via gog-morfeu)

| Comando | Uso |
|---------|-----|
| `gog-morfeu drive search "query" --max 10 -p` | Buscar no Drive |
| `gog-morfeu drive ls [folder-id]` | Listar pasta |
| `gog-morfeu drive get [id] --json` | Metadados de arquivo |
| `gog-morfeu drive download [id]` | Download de arquivo |
| `gog-morfeu drive upload [file] --replace [id]` | Re-upload preservando ID |
| `gcalcli agenda` | Ver agenda Google Calendar |
| `python3 scripts/gcal_morfeu.py` | Agenda formatada |
| `python3 scripts/smart_email_scan.py` | Scan de emails |

**⚠️ Drive:** Sempre verificar parent antes de criar/mover. Ver `governance/DRIVE_POLICY.md`.

---

## CATEGORIA 7 — SUBAGENTES E ORQUESTRAÇÃO

| Ferramenta | Uso |
|------------|-----|
| `sessions_spawn` | Criar subagente (runtime=subagent ou acp) |
| `sessions_yield` | Aguardar resultado de subagente |
| `subagents` | Listar, matar ou direcionar subagentes |
| `sessions_send` | Enviar mensagem para outra sessão |

**Regra:** Todo spawn requer contract (ver `governance/SUBAGENT_CONTRACT.md`).

---

## MODELOS — GUIA DE USO

| Modelo | Alias | Quando usar |
|--------|-------|-------------|
| MiniMax M2.5 | `minimax` | 90% das tarefas: heartbeat, rotinas, análise simples |
| MiniMax M2.7 | `minimax-27` | Análise de documentos longos, decisões táticas |
| Haiku | `haiku` | Confirmações rápidas, respostas triviais |
| Sonnet | `sonnet` | Análise complexa, redação de qualidade |
| Opus | `opus` | Decisões estratégicas de alto risco, arquitetura |
| Flash 2.5 | `flash-25` | Pesquisa web, tarefas multi-step rápidas |

**Padrão:** MiniMax M2.5 para jobs cron. Opus apenas quando Diego solicita explicitamente.

---

## FERRAMENTAS NÃO DISPONÍVEIS (gaps G8 a fechar)

| Ferramenta | Status | Plano |
|------------|--------|-------|
| LSP (Language Server) | ❌ Não integrado | FASE 3 |
| File watcher | ❌ Sem daemon próprio | FASE 3 |
| Bitrix24 API | ❌ Sem integração direta | FASE 3 |
| WhatsApp send | ❌ Bloqueado por política | Aguardar Nível 1 |
| tl;dv API | ✅ Registrada | Manter — key: `69f9a...01576`, base: `https://pasta.tldv.io/v1alpha1`, var: `TLDV_API_KEY`, locals: `/etc/environment` + `integrations/tldv/.env` |

---

## REGRA GERAL

Antes de usar qualquer ferramenta:
1. É a ferramenta mais simples para a tarefa? Se não → usar a mais simples.
2. A ferramenta gera efeito externo (send, write, cron)? Se sim → confirmar com Diego.
3. O resultado pode ser validado? Se não → usar dry-run primeiro.
