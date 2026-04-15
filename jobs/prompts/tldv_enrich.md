# JOB: TL;DV Enrich — Enriquecer Reuniões Coletadas
**Schedule:** 10 min após collect (10 */6 * * *)
**Timeout:** 150s
**Modelo:** minimax/MiniMax-M2.7

---

## O QUE FAZER

Para cada reunião nova em raw/ sem enrich correspondente, rodar enricher.

## EXECUÇÃO

```bash
cd /root/.openclaw/workspace

# Listar meetings raw sem enriquecimento
for f in $(ls memory/meetings/raw/ 2>/dev/null | tail -10); do
  mid=$(basename $f .json)
  if [ ! -f "memory/meetings/enriched/${mid}.json" ]; then
    echo "Enriching: $mid"
    python3 integrations/tldv/enricher.py --meeting-id $mid >> logs/tldv_enricher.log 2>&1
  fi
done

echo "ENRICH DONE: $(date)"
```

## DECISÃO

- Se executou sem erro → **NO_REPLY**
- Se erro → Telegram com erro简要