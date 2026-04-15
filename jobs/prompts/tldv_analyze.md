# JOB: TL;DV Analyze — Analisar Reuniões Enriquecidas
**Schedule:** 20 min após enrich (20 */6 * * *)
**Timeout:** 180s
**Modelo:** minimax/MiniMax-M2.7

---

## O QUE FAZER

Para cada reunião enriquecida sem análise, rodar analyzer.

## EXECUÇÃO

```bash
cd /root/.openclaw/workspace

for f in $(ls memory/meetings/enriched/ 2>/dev/null | tail -10); do
  mid=$(basename $f .json)
  if [ ! -f "memory/meetings/analysis/${mid}.md" ]; then
    echo "Analyzing: $mid"
    python3 integrations/tldv/analyzer.py --meeting-id $mid >> logs/tldv_analyzer.log 2>&1
  fi
done

echo "ANALYZE DONE: $(date)"
```

## DECISÃO

- Se executou sem erro → **NO_REPLY**
- Se novas análises geradas → **NO_REPLY** (digest job trata do resumo)
- Se erro → Telegram com erro简要