# JOB: TL;DV Collect — Coleta de Reuniões
**Schedule:** A cada 6h (0 */6 * * *)
**Timeout:** 120s
**Modelo:** minimax/MiniMax-M2.7

---

## O QUE FAZER

Rodar o collector tl;dv para buscar reuniões novas.

## EXECUÇÃO

```bash
cd /root/.openclaw/workspace
python3 integrations/tldv/collector.py --pages 2 >> logs/tldv_collector.log 2>&1
echo "COLLECTOR OK: $(date)"
```

## VERIFICAR OUTPUT

```bash
ls -t /root/.openclaw/workspace/memory/meetings/raw/*.json 2>/dev/null | head -5
```

## DECISÃO

- Se novos arquivos encontrados → **NO_REPLY** (próximo job enrich vai processar)
- Se nenhum novo arquivo → **NO_REPLY**
- Se erro no collector → envie Telegram:
```
🔴 TL;DV Collector quebrou
[erro]
👉 Verificar collector.py
```