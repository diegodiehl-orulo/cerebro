# LLM Policy v2.1 — OpenClaw Morfeu
# Política Operacional Elástica — Revisão Crítica
# Versão: 2.1 | Data: 2026-03-06 | Substitui: v2.0
# Revisão motivada por: viés excessivo de economia, NÃO CONFIRMADOs não documentados,
# e análise incorreta de custo real dos jobs.

---

## CORREÇÕES CRÍTICAS DA V2.0

### 1. O custo real é muito menor do que estimado
A v2.0 assumiu que todos os disparos = prompts consumidos.
A realidade: a maioria dos jobs tem lógica NO_REPLY ou early exit.

| Métrica | V2.0 (errado) | V2.1 (real) |
|---------|--------------|-------------|
| Prompts estimados/semana | ~400+ | ~64 |
| Prompts/dia (média) | ~57 | ~9 |
| Margem na janela de 5h | pequena | enorme (~80-90 prompts) |
| Principal gargalo | quota | nenhum — folga abundante |

**Consequência: os thresholds conservadores da v2.0 eram desnecessariamente restritivos.**

### 2. O fallback para Claude estava errado
Os próprios prompts dos jobs dizem explicitamente:
> "Execute SOMENTE com MiniMax. Se diferente → NO_REPLY e encerre. NÃO use fallback."

A v2.0 propunha fallback automático para Claude em P0 — isso **viola as regras existentes dos jobs**.
A v2.1 não propõe fallback automático. Fallback é manual e explícito, job a job.

### 3. Pools, circuit breaker e queues são NÃO CONFIRMADOS
O OpenClaw não tem suporte nativo a:
- pools de concorrência por classe
- circuit breaker de endpoint
- DLQ automática
- overlap control / mutex entre jobs
- quota tracking em tempo real

Tudo isso precisa ser implementado via design de jobs e scripts externos (P3 local).

---

## A) PROBLEMAS DA POLÍTICA ATUAL (v2.0)

| # | Problema | Severidade | Impacto |
|---|---------|------------|---------|
| 1 | P0 "ignorava remains" — semanticamente errado | Alto | P0 pode consumir quota em regime imprevisto |
| 2 | Fallback automático para Claude viola prompts dos jobs | Crítico | Jobs terminariam em NO_REPLY de qualquer forma; fallback invisível cria ilusão de execução |
| 3 | Thresholds muito conservadores (P2 bloqueado em <60) | Médio | Impede uso da folga real (~80-90 prompts disponíveis/5h) |
| 4 | Custo de quota superestimado em 6x | Alto | Toda a política era baseada em premissa falsa |
| 5 | Pools/circuit breaker apresentados como nativos | Crítico | Arquitetura proposta era parcialmente irreal |
| 6 | P1 sem diferenciação de modelo | Médio | Todos os P1 usam M2.5 mesmo quando M2.1 basta |
| 7 | P2 não expandido — oportunidade desperdiçada | Médio | Folga real de ~36 prompts/semana não aproveitada |
| 8 | P1 e P2 "sem nenhuma validação" | Médio | Qualidade não monitorada |
| 9 | Check Pós-Reunião classificado errado | Baixo | Tem lógica inteligente de detecção; não é desperdício |
| 10 | Concorrência inicial de 2/3 sem justificativa de risco | Médio | Pode criar race condition em jobs de memória compartilhada |

---

## B) POLÍTICA V2.1 CORRIGIDA

### Princípio-guia revisado
> A folga real é enorme. O objetivo não é economizar — é usar com inteligência.
> P0 protegido por reserva mínima. P1/P2 podem operar liberalmente.
> Qualidade é variável monitorada, não sacrificada.

---

### P0 — CRÍTICO (com subníveis)

#### P0-A: Missão crítica MiniMax-only
**Sem fallback.** Sem exceção. Se MiniMax indisponível: requeue em 15min, max 2x. Sem Claude.

| Job | Razão P0-A |
|-----|-----------|
| Daily Briefing (seg-sex 08:45) | Contexto do dia — base de tudo |
| Madrugada (seg-sáb 02h) | Consolidação de memória — crítico para continuidade |

**Regra de remains:**
- remains ≥ 15 → executa normalmente
- remains < 15 → requeue em 15min, tenta mais 2x, depois alerta Diego e encerra sem executar
- **Nunca executa quando remains = 0**

**Modelo:** `minimax/MiniMax-M2.5` — sem exceção. Sem fallback.
**Timeout:** 180s
**Retry:** 2x com requeue de 15min (não retry imediato)
**Validação:** constraint check (verificar se saída tem pelo menos 100 chars e contém nome de seção esperada)

---

#### P0-B: Operacional crítico (fallback permitido, controlado)
**Fallback possível** para `anthropic/claude-sonnet-4-6` apenas se job tem flag explícita `allow_fallback: true` no prompt. Nenhum job atual tem essa flag — portanto, nenhum job atual está em P0-B.

**Como entrar em P0-B:** Diego adiciona `## FALLBACK: PERMITIDO` explicitamente no prompt do job.

**Uso futuro:** incident response manual, alertas de emergência ad-hoc.

---

### P1 — IMPORTANTE (com subníveis de modelo)

#### P1-A: Exige M2.5 (raciocínio e síntese complexa)

| Job | Razão M2.5 obrigatório |
|-----|------------------------|
| Revisão Semanal (sex 16h) | Síntese de múltiplos documentos + recomendações estratégicas |
| Briefing Dom Coleta (dom 13h) | Executa scripts + consolida dados heterogêneos |
| Briefing Dom Análise (dom 14h) | Análise e narrativa do briefing semanal completo |
| Scan Praças Weekly (seg 08:30) | Governança + análise de múltiplas praças simultâneas |
| pracas-sprint-check-mon (seg 18h) | Avaliação de entregável + geração de rascunho |
| pracas-sprint-check-tue (ter 10h) | Análise de D+1 + follow-up condicional |

**Modelo:** `minimax/MiniMax-M2.5`
**Gate:** remains ≥ 25
**Timeout:** 180s
**Retry:** 1x após 5min
**Validação:** constraint check (output contém seções esperadas?)

#### P1-B: M2.1 suficiente (extração estruturada, lembrete, resumo simples)

| Job | Razão M2.1 suficiente |
|-----|-----------------------|
| Check Email Thu (qui 08h) | Scan + triagem de emails — tarefa estruturada |
| Check Contratos (seg-sex 11h) | Lê output de script → formata resumo — simples |
| pracas-sprint-reminder-thu (qui 09h) | Lembrete padronizado — baixa complexidade |
| Check Pós-Reunião (*/30 9-20h) | Detecção binária + NO_REPLY padrão |

**Modelo:** `minimax/MiniMax-M2.1` — **[NÃO CONFIRMADO se M2.1 está no plano Starter]**
**Fallback se M2.1 indisponível:** usar M2.5 (mais caro, mas correto)
**Gate:** remains ≥ 25
**Timeout:** 120s
**Retry:** 1x após 5min
**Validação:** schema check simples (output JSON válido ou lista estruturada)

---

### P2 — OPORTUNISTA COM LLM (3 subgrupos)

#### P2-A: Qualidade / Regressão
**O que são:** jobs que verificam, auditam e melhoram resultados de outros jobs.
**Gate:** remains ≥ 40 AND horário 08h-22h

| Job | Frequência proposta | Descrição |
|-----|--------------------|-----------| 
| Auditoria quality de cron runs (novo) | Semanal, domingo 20h | LLM revisa últimos 7 dias de outputs de P0/P1 e aponta degradações |
| Double-pass em Revisão Semanal | Quando remains ≥ 65 | Após gerar revisão, passa pelo mesmo LLM com prompt de auto-crítica |
| Validação de pendências vs realidade (novo) | Semanal, sexta 17h | Compara pending.md com o que realmente foi feito — detecta itens obsoletos |
| Regressão de templates (novo) | Quinzenal | Verifica se templates de cobrança/email ainda fazem sentido dado o contexto atual |

**Validação:** double-pass obrigatório (gera output → valida output com segundo prompt curto)
**Modelo:** M2.5
**Timeout:** 120s | **Retry:** 0

#### P2-B: Refinamento / Config / Logs
**O que são:** jobs que melhoram configurações, leem logs e propõem ajustes.
**Gate:** remains ≥ 40

| Job | Frequência proposta | Descrição |
|-----|--------------------|-----------| 
| MiniMax Health Check (09h, seg-sex) | atual | Script → interpreta → alerta se necessário |
| MiniMax Diagnóstico (04h, seg-sex) | atual | Diagnóstico completo overnight |
| MiniMax Relatório (06h, seg-sex) | atual | Lê relatório de diagnóstico |
| Análise de erros de cron runs (novo) | Diária 07h | Lê logs de falhas da última 24h, resume padrões |
| Watchdog de Crons | atual (reclassificar de P0 → P2-B) | Checa erros operacionais — importante mas não missão crítica |
| Livro Check (seg-sex 18h) | atual | Pergunta rotativa sobre o livro |

**Watchdog reclassificado:** O Watchdog verifica saúde operacional dos crons — importante mas não bloqueia o dia de Diego se falhar. Não é P0. Mover para P2-B mantém slot P0 protegido.
**Validação:** schema check (output tem seção de "status" identificável)
**Modelo:** M2.5 | **Timeout:** 90s | **Retry:** 0

#### P2-C: Documentação / Memória / Aprendizado
**O que são:** jobs que enriquecem a memória do sistema, documentam e geram insights.
**Gate:** remains ≥ 40 AND janela prioritária: 22h-07h ou fds

| Job | Frequência proposta | Descrição |
|-----|--------------------|-----------| 
| Harvester — Auditoria decisions.md (novo) | Semanal, dom 22h | Verifica se decisões tomadas estão refletidas nos projetos |
| Harvester — Insights de lessons.md (novo) | Quinzenal, dom 22h | Extrai padrões de lições aprendidas, sugere melhorias de processo |
| Harvester — Consistência people+projects (novo) | Mensal | Verifica alinhamento entre pessoas-chave e projetos ativos |
| Trinks Dom (08h domingo) | atual | Checa janela e sugere agendamento |
| Cuidados Pessoais Dom (14h domingo) | atual | Check de saúde/rotina pessoal |
| Lembrete Tom de Voz (one-shot 10/03) | atual | Aguarda expirar, depois arquivar |

**Validação:** nenhuma obrigatória — output é informacional/documental
**Modelo:** M2.5 | **Timeout:** 120s | **Retry:** 0

---

### P3 — LOCAL-ONLY (sem LLM)
**Sem quota. Sem MiniMax. CPU/IO local.**

| Tarefa | Implementação |
|--------|---------------|
| Backup Diário Workspace | `bash backup_diego.sh` — já é session=main/systemEvent (não consome quota) |
| Health check endpoints (novo) | `curl` + python script — 15min |
| Checksums workspace (novo) | `sha256sum -c` — diário 06h |
| Limpeza cron runs antigos (novo) | `find + rm` — semanal |
| Lint scripts Python (novo) | `flake8` — semanal |
| Disk/memory report (novo) | `df + free` — diário |
| SQLite integrity check (novo) | `sqlite3 PRAGMA` — semanal |

---

## C) TABELA COMPLETA DE JOBS

| Job | ID (8 chars) | Classe | Modelo | Frequência | Impacto se falhar | Retry | Timeout | Validação | Fallback? | Local sem LLM? |
|-----|-------------|--------|--------|-----------|-------------------|-------|---------|-----------|-----------|----------------|
| Daily Briefing | 19741391 | **P0-A** | M2.5 | Seg-Sex 08:45 | Alto — Diego sem contexto do dia | 2x/15min | 180s | constraint | ❌ Nunca | ❌ |
| Madrugada | b534ff47 | **P0-A** | M2.5 | Seg-Sáb 02h | Alto — memória não consolidada | 2x/15min | 180s | constraint | ❌ Nunca | ❌ |
| Revisão Semanal | ab458393 | **P1-A** | M2.5 | Sex 16h | Médio — revisão adiada 1 semana | 1x/5min | 180s | constraint | ❌ | ❌ |
| Briefing Dom Coleta | 02d749f4 | **P1-A** | M2.5 | Dom 13h | Médio — análise do dom sem dados | 1x/5min | 300s | constraint | ❌ | Parcial (scripts) |
| Briefing Dom Análise | d12a4136 | **P1-A** | M2.5 | Dom 14h | Médio — briefing não enviado | 1x/5min | 240s | constraint | ❌ | ❌ |
| Scan Praças Weekly | 2688a54a | **P1-A** | M2.5 | Seg 08:30 | Médio — sem relatório semanal praças | 1x/5min | 120s | constraint | ❌ | ❌ |
| sprint-check-mon | 1a8a8f9a | **P1-A** | M2.5 | Seg 18h | Médio — cobrança não gerada | 1x/5min | 120s | constraint | ❌ | ❌ |
| sprint-check-tue | 3a13d632 | **P1-A** | M2.5 | Ter 10h | Baixo — D+1 check pode atrasar | 1x/5min | 120s | constraint | ❌ | ❌ |
| Check Email Thu | 89f8af36 | **P1-B** | M2.5* | Qui 08h | Baixo — check adiado 1 semana | 1x/5min | 180s | schema | ❌ | Parcial |
| Check Contratos | 3a6caf28 | **P1-B** | M2.5* | Seg-Sex 11h | Baixo — lembrete adiado 1 dia | 1x/5min | 120s | schema | ❌ | Parcial |
| sprint-reminder-thu | 39e87458 | **P1-B** | M2.5* | Qui 09h | Baixo — lembrete quinzenal | 1x/5min | 120s | schema | ❌ | ❌ |
| Check Pós-Reunião | 696a5c6b | **P1-B** | M2.5* | */30 9-20h M-Sa | Mínimo — maioria NO_REPLY | 0 | 120s | nenhuma | ❌ | Potencial |
| Watchdog Crons | 359bb580 | **P2-B** | M2.5 | Diário 09h | Baixo — diagnóstico atrasado | 0 | 120s | schema | ❌ | ❌ |
| MiniMax Health | 0f03c740 | **P2-B** | M2.5 | Seg-Sex 09h | Mínimo — script faz o check | 0 | 60s | schema | ❌ | Sim (script) |
| MiniMax Diagnóstico | 26f3c8cb | **P2-B** | M2.5 | Seg-Sex 04h | Mínimo — log apenas | 0 | 180s | schema | ❌ | Sim (script) |
| MiniMax Relatório | acb8caaa | **P2-B** | M2.5 | Seg-Sex 06h | Mínimo — lê report | 0 | 30s | nenhuma | ❌ | Sim |
| Livro Check | 7e712ad8 | **P2-B** | M2.5 | Seg-Sex 18h | Mínimo — 1 dia sem ping | 0 | 60s | nenhuma | ❌ | ❌ |
| Trinks Dom | 21647e7c | **P2-C** | M2.5 | Dom 08h | Mínimo — aviso de cabelo | 0 | 120s | nenhuma | ❌ | Potencial |
| Cuidados Pessoais | 0f529fd3 | **P2-C** | M2.5 | Dom 14h | Mínimo — check pessoal | 0 | 180s | nenhuma | ❌ | ❌ |
| Lembrete Tom Voz | 7e9cef0f | **P2-C** | M2.5 | One-shot 10/03 | Mínimo — lembrete | 0 | 60s | nenhuma | ❌ | ❌ |
| Backup Diário | 9574d0b0 | **P3** | nenhum | Diário 05h | Médio — sem backup | 3x | — | n/a | n/a | ✅ (systemEvent) |
| Regra Claudinei | ec00b872 | — | M2.5 | One-shot 06/03 | — | 0 | 30s | nenhuma | ❌ | — |

*M2.1 preferencial quando disponível no plano. Fallback: M2.5.

**Duplicatas a desabilitar (dry run confirmado):**

| ID (8 chars) | Nome | Ação |
|-------------|------|------|
| aff6ad79 | Livro (dupe) | DISABLE |
| 18e71a89 | Trinks (dupe) | DISABLE |
| 3d6cf969 | Scan Praças (dupe) | DISABLE |
| 4ff7a234 | sprint-reminder-thu (dupe) | DISABLE |
| 972f07d4 | sprint-check-mon (dupe) | DISABLE |
| eb5e7cdb | sprint-check-tue (dupe) | DISABLE |
| 4d10d354 | sprint-watcher (dupe) | DISABLE |

---

## D) THRESHOLDS REVISADOS

```
quota_window: 5h
quota_max: 100

reserve_p0:      15   # P0-A aguarda requeue se abaixo disso
                       # (antes era 20 — muito conservador)

p0a_min:         15   # P0-A executa normalmente acima disso
p0a_requeue:     5    # Requeue interno após 15min (max 2x)

p1_min:          25   # P1 executa normalmente acima disso
                       # (antes era 40 — desperdiçava ~36 prompts de folga)

p2_min:          40   # P2 ativo acima disso
                       # (antes era 60 — excessivamente restritivo)

harvester_min:   55   # Harvester overnight ativo acima disso

double_pass_min: 65   # Double-pass de qualidade quando há folga real
```

### Justificativa dos números

| Threshold | V2.0 | V2.1 | Razão da mudança |
|-----------|------|------|-----------------|
| reserve_p0 | 20 | 15 | Custo real é ~9/dia. 15 cobre ~8h de P0 |
| p1_min | 40 | 25 | Com 25, ainda sobram 10 para P0 em qualquer janela |
| p2_min | 60 | 40 | Com 40, sobram 25 para P0+P1 — confortável |
| harvester_min | 70 | 55 | Harvester tem 5 prompts/ciclo. 55-5=50, ainda seguro |
| double_pass_min | 80 | 65 | Com 65, double-pass de 2 prompts deixa 63 — seguro |

---

## E) CONCORRÊNCIA INICIAL vs ALVO

### Por que via schedule design e não pools nativos
O OpenClaw **não tem suporte nativo a pools de concorrência** [NÃO CONFIRMADO como nativo].
Portanto: concorrência é controlada via **design de schedule** (espaçamento de crons) e **lockfiles locais** (P3 script).

### Fase Inicial (agora → D+14)
```
Regra: máximo 1 job LLM simultâneo por design de schedule
Como: verificar que nenhum P1-A sobrepõe outro no mesmo slot
Exceção: sprint-watcher e outro job podem coexistir se watcher tiver
         NO_REPLY rápido (< 10s via script)
```

**Por que 1 simultâneo no início:**
- Jobs de memória compartilhada (escrevem em memory/*.md) podem criar race condition
- Sem mutex nativo, dois jobs escrevendo no mesmo arquivo = corrupção
- Sem métricas de latência, não sabemos se 2 jobs simultâneos causam timeout em cascata

### Fase Alvo (D+14 → D+30, após métricas)
```
Regra: máximo 2 jobs LLM simultâneos, desde que:
  - Nenhum dos dois escreve nos mesmos arquivos
  - Um deles é "read-only" por design
  - Nenhum é P0-A
```

**Por que 2 e não 3:**
- VPS aguenta 3+ sem problema de recurso
- O risco não é VPS: é race condition em memória + imprevisibilidade de ordem de escrita
- 2 é o mínimo para ganhar velocidade sem abrir risco de corrupção

### Implementação de sobreposição por schedule design
```
Slots problemáticos detectados (segunda-feira):
  08:30 → Scan Praças Weekly
  08:45 → Daily Briefing     ← COLISÃO (15min de gap)
  09:00 → Watchdog + MiniMax Health ← COLISÃO DUPLA

Correção proposta:
  08:30 → Scan Praças (P1-A, 120s max)
  08:50 → Daily Briefing (P0-A — só dispara após Scan terminar)
  09:15 → Watchdog (P2-B)
  09:30 → MiniMax Health (P2-B)
```

---

## F) ESTRATÉGIA DE USO MAIOR DA QUOTA SEM PERDER QUALIDADE

### A realidade: sobram ~36 prompts/semana úteis para expandir

```
Consumo atual real (após dedup):   ~55 prompts/semana
Quota disponível (100/5h × ~9h úteis/dia × 5 dias): >> 100 disponíveis
Headroom real:                      enorme
```

### 6 formas de usar melhor, por ordem de impacto

**1. Ativar P2-A: double-pass oportunista na Revisão Semanal**
- Quando: sexta + remains ≥ 65
- Custo: +1 prompt (segundo pass curto de 30s)
- Benefício: qualidade da revisão semanal aumenta mensuravelmente

**2. Ativar P2-C: Harvester nocturno de memória (2 jobs novos)**
- Quando: domingo 22h, remains ≥ 55
- Custo: 3-5 prompts/semana
- Benefício: memory/decisions.md e lessons.md sempre em dia sem esforço manual

**3. Ativar P2-A: Auditoria semanal de pending.md**
- Quando: sexta 17h, remains ≥ 40
- Custo: 1 prompt/semana
- Benefício: lista de pendências limpa e relevante toda semana

**4. Adicionar validação P1-A**
- O que: constraint check de 30s após cada P1-A
- Custo: +1 prompt por P1-A executado
- Benefício: outputs degradados detectados antes de chegar ao Diego

**5. Ativar P2-B: Análise diária de erros de logs**
- Quando: seg-sex 07h, remains ≥ 40
- Custo: 1 prompt/dia = 5 prompts/semana
- Benefício: erros silenciosos de scripts detectados proativamente

**6. Reativar Monitor tl;dv (agora desabilitado)**
- Schedule atual: `0 10-18/2 * * 1-5` (6x/dia em dias úteis)
- Custo se reativado: ~6 disparos × 50% NO_REPLY = ~3 prompts/dia reais
- Benefício: reuniões processadas automaticamente
- Gate: remains ≥ 40 → reativar com segurança

---

## G) ITENS NÃO CONFIRMADOS

| Item | Status | Workaround proposto |
|------|--------|---------------------|
| **Pools de concorrência nativos** | ❌ NÃO CONFIRMADO | Schedule design (espaçar crons) + lockfile P3 |
| **Circuit breaker de endpoint** | ❌ NÃO CONFIRMADO | Health check P3 local (curl) + alerta Telegram |
| **DLQ automática** | ❌ NÃO CONFIRMADO | Script local monitora runs.json → escreve dlq/ quando detecta falha |
| **Quota tracking em tempo real** | ❌ NÃO CONFIRMADO | Script P3 que estima remains por sliding window das runs |
| **Overlap control / mutex** | ❌ NÃO CONFIRMADO | Lockfile `/tmp/morfeu-<job-id>.lock` em P3 scripts |
| **Prioridade de fila entre classes** | ❌ NÃO CONFIRMADO | Schedule espaçado + P0 com maior delay de retry |
| **Cancelamento de job em execução** | ❌ NÃO CONFIRMADO | Timeout por job (já configurável) é o mecanismo disponível |
| **Failover automático de endpoint** | ❌ NÃO CONFIRMADO | Configurar baseUrl alternativo no provider do job manualmente |
| **M2.1 disponível no Starter** | ⚠️ NÃO VERIFICADO | Assumir M2.5 como padrão até confirmar |
| **Heartbeat consome quota** | ⚠️ NÃO VERIFICADO | Se HEARTBEAT_OK não aciona LLM, custo = 0; verificar |

### Workarounds implementáveis como P3 local

```bash
# 1. Lockfile de overlap (P3 script)
LOCKFILE="/tmp/morfeu-job-${JOB_ID}.lock"
if [ -f "$LOCKFILE" ]; then
  echo "Job already running. Skipping." && exit 0
fi
touch "$LOCKFILE"
trap "rm -f $LOCKFILE" EXIT

# 2. Circuit breaker local (P3 health check a cada 15min)
# scripts/endpoint_health.py
# → curl https://api.minimaxi.chat/v1/models (sem autenticação real)
# → se falha 3x em 10min → escreve /tmp/minimax_circuit_open
# → jobs verificam arquivo antes de disparar

# 3. Quota estimator (P3, baseado em cron/runs/)
# scripts/quota_estimator.py
# → lê timestamps dos últimos runs em cron/runs/*.jsonl
# → calcula quantos rodaram nos últimos 5h
# → escreve /tmp/morfeu_remains_estimate
# → jobs leem esse arquivo para auto-gate
```

---

## H) PLANO DE APLICAÇÃO REVISADO

### Fase 1 — Zero risco (HOJE)
**Ação única: desabilitar 7 duplicatas**
```
Custo: 0 risco
Ganho: ~35 prompts/semana economizados (headroom P2)
Método: cron update nos 7 IDs confirmados no dry run
```
> Diego: `"OK Fase 1"` → Morfeu aplica via ferramenta cron.

---

### Fase 2 — Fixes de qualidade (D+1, após Fase 1 estável)
**Ações:**
- Adicionar `timeout=120s` em Contratos (faltando)
- Explicitar `model=minimax/MiniMax-M2.5` nos 5 jobs com `model=default` de praças
- Ajustar schedule para eliminar colisões de 08:30-09:00 na segunda
- Adicionar `timeout` no Backup Diário (hoje: N/A)

**Custo:** baixo. Nenhuma lógica muda. Só metadados dos jobs.

---

### Fase 3 — Ativar P2 expandido (D+3, após Fase 2 estável)
**Ações:**
- Criar job P2-A: Auditoria de pending.md (sex 17h, 1 prompt)
- Criar job P2-B: Análise de erros de logs (seg-sex 07h, 1 prompt)
- Reativar Monitor tl;dv com gate de remains ≥ 40
- Adicionar constraint check leve pós-execução em P1-A (Revisão Semanal + Daily Briefing)

**Custo:** +8-10 prompts/semana de jobs úteis. Sobra enorme.

---

### Fase 4 — Harvester + double-pass (D+10, após métricas de 7 dias)
**Ações:**
- Criar job P2-C: Harvester decisions.md (dom 22h)
- Criar job P2-C: Harvester lessons.md (dom 22h, 30min após decisions)
- Ativar double-pass na Revisão Semanal quando remains ≥ 65
- Criar scripts P3: lockfile, health check endpoint, quota estimator

**Pré-condição:** ter dados de latência e remains real dos 7 dias anteriores.

---

### Fase 5 — Calibração e P3 local (D+21)
**Ações:**
- Revisar thresholds com dados reais (manter, ajustar ou afrouxar)
- Implementar 3 scripts P3 locais (health check, disk report, SQLite integrity)
- Avaliar se Monitor tl;dv reativado justifica frequência maior
- Documentar baseline de qualidade por classe

---

## RESUMO EXECUTIVO V2.1

| Dimensão | V2.0 | V2.1 |
|----------|------|------|
| Custo real/semana | Estimado em 400+ (errado) | Real: ~55-64 |
| Headroom disponível | Parecia pequeno | Enorme (~36 prompts/semana livres) |
| Fallback Claude | Automático e amplo | Nunca (exceto P0-B explícito futuro) |
| P0 | "Ignora remains" | Reserva 15; P0-A sem fallback; P0-B com flag explícita |
| P1 | Um único nível | P1-A (M2.5 obrigatório) + P1-B (M2.1 preferencial) |
| P2 | Bloqueado em <60 (muito conservador) | 3 subgrupos ativos a partir de 40 |
| Concorrência | Proposta como pool nativo | Schedule design + lockfile P3 |
| NÃO CONFIRMADOs | Não documentados (erro grave) | 10 itens explícitos com workaround |
| Validação P1/P2 | "Nenhuma" | Constraint check P1-A, schema P1-B, double-pass P2-A |
| Estratégia geral | Economizar quota | Usar com inteligência — folga é ativo |

---

*Próxima ação: Diego confirma `"OK Fase 1"` para dedup imediato.*
*Próxima revisão desta política: D+21 com dados reais.*
