# Cron — tl;dv Pipeline

## Webhook Server (sempre rodando)

```bash
# Iniciar como systemd service
nohup node $WORKSPACE/integrations/tldv/webhook_server.js \
  >> $WORKSPACE/logs/tldv_webhook.log 2>&1 &
# Reiniciar se morrer
```

Ou via cron `@reboot`:
```
@reboot root /usr/bin/node $WORKSPACE/integrations/tldv/webhook_server.js >> $WORKSPACE/logs/tldv_webhook.log 2>&1
```

---

## Pipeline — Execução Periódica

### A cada 1h (WEBHOOK + POLLING FALLBACK)
**Objetivo:** Processar eventos webhook + verificar reuniões pendentes de enrichment.

```
0 */1 * * * TLDV_API_KEY="YOUR_TLDV_API_KEY_HERE" PYTHONPATH=$WORKSPACE/integrations /usr/bin/python3 $WORKSPACE/integrations/tldv/queue_processor.py >> $WORKSPACE/logs/tldv_queue_processor.log 2>&1
```

### A cada 6h (COLLECT + ENRICH + ANALYZE + PERSIST)
**Objetivo:** Garantir que reuniões novas sejam coletadas e enriquecidas mesmo sem webhook.

```
0 */6 * * * TLDV_API_KEY="YOUR_TLDV_API_KEY_HERE" PYTHONPATH=$WORKSPACE/integrations /usr/bin/python3 $WORKSPACE/integrations/tldv/pipeline.py --stage collect,enrich,analyze,persist >> $WORKSPACE/logs/tldv_pipeline.log 2>&1
```

### 1x ao dia às 08h — DIGEST
**Objetivo:** Relatório consolidado diário de reuniões.

```
0 8 * * * PYTHONPATH=$WORKSPACE/integrations /usr/bin/python3 $WORKSPACE/integrations/tldv/pipeline.py --stage digest --since $(date -d '1 day ago' +\%Y-\%m-\%d) >> $WORKSPACE/logs/tldv_digest.log 2>&1
```

---

## Verificação de Status

```bash
# Ver se webhook está rodando
ps aux | grep webhook_server | grep -v grep

# Ver fila de eventos
curl -s http://127.0.0.1:18788/queue/status

# Ver último digest
ls -t $WORKSPACE/logs/tldv_digest*.md | head -1 | xargs cat

# Ver logs recentes
tail -20 $WORKSPACE/logs/tldv_pipeline.log
tail -20 $WORKSPACE/logs/tldv_queue_processor.log

# Ver quantas análises temos
ls $WORKSPACE/memory/meetings/analysis/*.json | wc -l
ls $WORKSPACE/memory/meetings/normalized/*.json | wc -l
```

---

## Reprocessamento Manual

### Reprocessar reunião específica (webhook processor)
```bash
PYTHONPATH=$WORKSPACE/integrations \
TLDV_API_KEY="YOUR_TLDV_API_KEY_HERE" \
python3 $WORKSPACE/integrations/tldv/queue_processor.py \
  --meeting-id 69d3f49884d30500130092c2
```

### Reprocessar via pipeline direto
```bash
PYTHONPATH=$WORKSPACE/integrations \
python3 $WORKSPACE/integrations/tldv/pipeline.py \
  --meeting-id 69d3f49884d30500130092c2 --verbose
```

### Limpar e reprocessar fila de eventos
```bash
# Mover eventos para reprocessar
mv $WORKSPACE/memory/meetings/queue/failed/*.json \
   $WORKSPACE/memory/meetings/queue/ 2>/dev/null || true

# Reprocessar fila
python3 $WORKSPACE/integrations/tldv/queue_processor.py --limit 20
```
