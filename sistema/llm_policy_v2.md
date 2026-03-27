# LLM Policy v2 — OpenClaw Morfeu
# Política Operacional Elástica e Segura
# Versão: 2.0 | Data: 2026-03-06 | Status: ATIVO

---

## 1. PLANO DE QUOTA MINIMAX CODING PLAN

### Parâmetros fixos
- **Plano:** Starter
- **Quota:** 100 prompts / 5 horas (rolling window)
- **Modelos válidos:** MiniMax-M2.5, MiniMax-M2.1, MiniMax-M2
- **Lightning:** NÃO disponível no Starter — PROIBIDO
- **Endpoint primário:** https://api.minimaxi.chat/v1
- **Endpoint fallback CN:** https://api.minimaxi.com/v1

### Reservas de quota por classe
| Classe | Reserva | Uso máximo por janela 5h |
|--------|---------|--------------------------|
| P0 (crítico) | 20 prompts reservados | Sempre disponível |
| P1 (importante) | 40 prompts | Até remains > 40 |
| P2 (oportunista LLM) | 30 prompts | Apenas remains > 60 |
| P3 (local-only) | 0 (sem LLM) | Sem limite |

### Thresholds de estado
```
remains >= 80  → MODO NORMAL    (P0+P1+P2 disponíveis)
remains 60-79  → MODO CAUTELOSO (P0+P1 disponíveis; P2 pausado)
remains 40-59  → MODO RESTRITO  (P0+P1 apenas; P2 bloqueado)
remains 20-39  → MODO PROTEÇÃO  (P0 apenas; P1 em fila)
remains < 20   → QUOTA LOCK     (apenas P0 emergencial; resto aguarda)
```

---

## 2. CLASSES DE TRABALHO

### P0 — CRÍTICO
> Nunca bloquear. Sempre executa. Fallback para Claude se MiniMax indisponível.

**Jobs:**
- Daily Briefing (seg-sex 08:45)
- Madrugada — Insight e Memória (02h)
- Watchdog de Crons (09h)
- Incident response (on-demand)

**Regras:**
- Concorrência máxima: 2
- Timeout: 180s
- Retry: 1x após 30s
- Modelo: minimax/MiniMax-M2.5 → fallback: anthropic/claude-sonnet-4-6
- Gate: NUNCA bloqueado por quota
- Validação: schema check obrigatório após execução

---

### P1 — IMPORTANTE
> Executa quando remains > 40. Prioridade sobre P2.

**Jobs:**
- Revisão Semanal (sex 16h)
- Briefing Dominical Coleta (dom 13h)
- Briefing Dominical Análise (dom 14h)
- Check Email Quinta (qui 08h)
- Check Contratos Pendentes (seg-sex 11h)
- Check Pós-Reunião → RECLASSIFICADO P3 (ver abaixo)
- Scan Praças Weekly (seg 08:30)
- pracas-sprint-check-mon (seg 18h)
- pracas-sprint-check-tue-10 (ter 10h)
- pracas-sprint-reminder-thu (qui 09h)
- pracas-sprint-watcher (8h,10h,12h,14h,16h,18h,20h seg-sex)

**Regras:**
- Concorrência máxima: 3
- Timeout: 180s padrão
- Retry: 1x após 60s
- Modelo: minimax/MiniMax-M2.5
- Gate: remains > 40

---

### P2 — OPORTUNISTA COM LLM
> Executa apenas quando remains > 60. Interrompível. Jamais bloqueia P0/P1.

**Jobs elegíveis (a ativar gradualmente):**
- Análise de qualidade de cron runs (semanal)
- Auditoria de memory/pending.md (semanal)
- Refinamento de templates (quinzenal)
- Análise de logs de erros recentes (diária noturna)
- Check Pós-Reunião → migrar para P3 local primeiro
- Lembrete Tom de Voz (único, baixo custo)
- Check Diário Livro (18h)
- Cuidados Pessoais Check (dom 14h)
- Trinks Sugestão (dom 08h)
- MiniMax Health Check (09h seg-sex)
- MiniMax Diagnóstico (04h)
- MiniMax Relatório (06h)

**Regras:**
- Concorrência máxima: 1 (nunca paralelo)
- Timeout: 90s máximo
- Retry: 0 (não retentar — oportunista)
- Modelo: minimax/MiniMax-M2.5
- Gate: remains > 60 AND backlog P0 = zero AND horário permitido (08h-22h)

---

### P3 — LOCAL-ONLY (sem LLM)
> Executa livremente. CPU/RAM/IO local. Sem consumir quota.

**Jobs e tarefas:**
- Backup Diário Workspace → Google Drive (script local)
- Check Pós-Reunião → converter para verificação local de calendário/arquivos
- Health check de processos (ps, ports, disk)
- Validação de checksums do workspace
- Lint/typecheck de scripts Python
- Análise de logs de erros (grep, awk, sem LLM)
- Geração de relatórios estruturais (contagem, diffs, stats)
- Verificação de conectividade de endpoints (curl health check)
- Indexação local de arquivos memory/
- Limpeza de runs antigos em cron/runs/

---

## 3. CAPACITY HARVESTER

### Definição
Mecanismo que aproveita remaining quota + CPU ociosa de forma segura.

### Condições de ativação
```
remains >= 70
AND backlog P0 = 0
AND hora atual in [22h-07h] OR [12h-14h]
AND nenhum job P0/P1 nos próximos 30 min
```

### Jobs candidatos ao harvester
1. Auditoria semanal de memory/decisions.md vs projetos ativos
2. Geração de resumo semanal de cron runs (qualidade, erros, latência)
3. Revisão de memory/lessons.md para insights pendentes
4. Análise de consistência entre people.md e projetos ativos
5. Sugestão de novos P3 locais baseado em padrão de uso

### Regras do harvester
- Todos os jobs são **read-only** por padrão
- Nenhum job escreve sem approval gate
- Idempotente: re-executar produz mesmo resultado
- Interrompível a qualquer momento sem perda
- Máximo 5 prompts por ciclo de harvester

---

## 4. QUALIDADE ADAPTATIVA

### Por nível de folga
| Remains | Estratégia | Validação |
|---------|-----------|-----------|
| >= 80 | double-pass (gera + valida) | schema check + reprompt |
| 60-79 | single-pass + schema check | schema check |
| 40-59 | single-pass | nenhuma |
| 20-39 | single-pass mínimo | nenhuma |
| < 20 | não executa (exceto P0) | — |

### Double-pass: quando usar
- Rascunhos de e-mail externo
- Templates de comunicação
- Análises críticas de pipeline/deals
- Nunca para: health checks, watchdogs, tl;dv summaries

---

## 5. SEGURANÇA OPERACIONAL

### Read-only default
- Todos os jobs de análise/auditoria: read-only por design
- Writes exigem: approval gate + idempotency key + log de auditoria

### Circuit Breaker
```
Estado CLOSED (normal):    erros < 3 em 10 min → aceita requests
Estado OPEN (bloqueado):   erros >= 3 em 10 min → rejeita por 15 min
Estado HALF-OPEN (teste):  após 15 min → tenta 1 request
```

### Endpoint Failover
```
Tentativa 1: https://api.minimaxi.chat/v1 (primário)
Tentativa 2 (após 5s timeout): https://api.minimaxi.com/v1 (CN fallback)
Tentativa 3 (P0 only): anthropic/claude-sonnet-4-6
```

### DLQ (Dead Letter Queue)
- Jobs P1 que falham 2x → mover para DLQ em `jobs/dlq/`
- Jobs P2 que falham 1x → descartar (oportunista)
- Jobs P0 que falham → escalate imediato + fallback Claude

### Trilha de auditoria
- Todo job registra: início, fim, remains_before, remains_after, modelo usado, schema_pass
- Formato: `logs/audit/YYYY-MM-DD.jsonl`
- Retenção: 30 dias

---

## 6. OBSERVABILIDADE MÍNIMA

### Métricas obrigatórias por job run
```json
{
  "job_id": "...",
  "job_name": "...",
  "class": "P0|P1|P2|P3",
  "model": "...",
  "endpoint": "primário|fallback",
  "remains_before": 0,
  "remains_after": 0,
  "prompt_consumed": 0,
  "latency_ms": 0,
  "retries": 0,
  "schema_pass": true,
  "circuit_state": "CLOSED|OPEN|HALF-OPEN",
  "result": "ok|error|timeout|dlq",
  "ts": "ISO-8601"
}
```

### Alertas ativos
- remains < 25: alerta imediato para Diego via Telegram
- 3 falhas consecutivas de P0: alerta crítico
- Circuit breaker OPEN: alerta + pausa de P2
- Quota lock atingido: notificação + log

---

## 7. ANTI-PATTERNS PROIBIDOS

- ❌ Usar MiniMax-M2.5-Lightning (não disponível no Starter)
- ❌ Permitir P2 concorrer com P0 na mesma janela
- ❌ Retry automático em P2 (oportunista não justifica retry)
- ❌ Watchdog contínuo com LLM (usar health checks locais primeiro)
- ❌ Jobs sem timeout explícito (default é infinito = risco)
- ❌ Jobs duplicados (desperdiça quota 2x)
- ❌ Check Pós-Reunião com LLM a cada 30min (deve ser local/P3)

---

*Última revisão: 2026-03-06 | Próxima calibração: após 7 dias de dados*
