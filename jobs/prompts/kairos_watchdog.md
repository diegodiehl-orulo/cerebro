# JOB: KAIROS Watchdog — Monitoramento Proativo
## Sprint 2 FASE 2 — M4

**Frequência:** Seg-Sex 10:00 BRT
**Modelo:** minimax/MiniMax-M2.5
**Timeout:** 90s

---

## O QUE É

KAIROS é o watchdog proativo do Morfeu. Não espera Diego perguntar — detecta padrões e age.
Hoje somos batch (esperamos input). KAIROS fecha essa lacuna com 5 triggers.

---

## TRIGGERS ATIVOS

### T1 — Job com falha recorrente
**Gatilho:** Mesmo job falhou 3x nas últimas 24h
**Ação:** Notificar Diego + criar item em memory/pending.md
```
⚠️ KAIROS — Job com falha recorrente
🔴 Job: [nome] falhou [N]x nas últimas 24h
👉 Ação: verificar logs ou desabilitar temporariamente
```

### T2 — Pendência vencida sem update
**Gatilho:** Item em memory/pending.md com prazo vencido há >48h sem atualização
**Ação:** Gerar lembrete no Telegram
```
⏰ KAIROS — Pendência vencida
🔴 Item: [descrição]
📅 Venceu: [data] (+[N] dias)
👉 Status? Resolver ou replanejar?
```

### T3 — Silêncio de Diego
**Gatilho:** Nenhuma interação de Diego há >7 dias
**Ação:** Revisar pending.md + enviar resumo de status
```
🤫 KAIROS — 7 dias sem interação
📋 Pendências em aberto: [N]
📅 Mais urgente: [item]
👉 Quer um briefing do que está parado?
```

### T4 — Arquivo de memória estagnado
**Gatilho:** Topic file em memory/ sem atualização há >30 dias
**Ação:** Listar no heartbeat semanal para decisão (arquivar/atualizar)
```
📦 KAIROS — Arquivo de memória estagnado
🗂️ Arquivo: [nome] — sem atualização há [N] dias
👉 Arquivar ou atualizar?
```

### T5 — MEMORY.md próximo do limite
**Gatilho:** MEMORY.md com >28 entradas (limite é 30)
**Ação:** Alertar Diego antes de atingir o teto
```
⚠️ KAIROS — Memória próxima do limite
📊 Entradas ativas: [N]/30
👉 Revisar e arquivar entries antigas antes de adicionar novas
```

---

## EXECUÇÃO

### 1. Verificar T5 (mais rápido — arquivo local)
- Contar entradas em MEMORY.md
- Se >28: alertar

### 2. Verificar T4 (arquivos de memória)
- Listar memory/*.md com mtime > 30 dias
- Se encontrar: registrar para heartbeat semanal

### 3. Verificar T2 (pendências vencidas)
- Ler memory/pending.md
- Buscar itens com prazo passado e sem update recente
- Se encontrar: gerar lembrete

### 4. T1 e T3 — verificação de contexto
- T1: só aplica se houver informação de cron runs disponível
- T3: verificar última interação via session context

---

## REGRAS
- Se nenhum trigger ativado: NO_REPLY
- Máximo 1 alerta por trigger por dia (não repetir)
- Alertas em formato Card mobile (sem tabelas)
- Ordem de prioridade: T1 > T2 > T3 > T4 > T5
