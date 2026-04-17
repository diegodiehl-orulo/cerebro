# tl;dv — Integração Completa Morfeu

## Arquitetura

```
tl;dv API
    ↓
collector.py          → raw/{id}.json
    ↓
enricher.py          → transcripts/{id}.json + notes/{id}.json + normalized/{id}.json
    ↓
analyzer.py          → analysis/{id}.json + analysis/{id}.md
    ↓
persister.py         → memory/decisions.md | lessons.md | risks.md | commercial_context.md
                    → docs/meeting-derived-updates/{date}_{cat}.md (patches)
    ↓
pipeline.py          → orchestrates all above + digest
    ↓
webhook_server.js    → queue/{event}.json (event-driven trigger)
    ↓
queue_processor.py   → consume queue → pipeline por reunião
```

---

## Scripts

| Script | Responsabilidade |
|--------|----------------|
| `collector.py` | Lista reuniões da API, busca detalhes, salva em `raw/` |
| `enricher.py` | Para cada raw: transcript + notes → `transcripts/` + `notes/` + `normalized/` |
| `analyzer.py` | LLM analysis → `analysis/{id}.json` + `.md` |
| `persister.py` | Extrai decisões/lições/riscos → memória + patches |
| `pipeline.py` | Orquestra estágios 1-5 em sequência |
| `queue_processor.py` | Consome fila webhook → processa reunião |
| `webhook_server.js` | Endpoint receptor de webhooks tl;dv (porta 18788) |

---

## Endpoints do Webhook

```
POST http://localhost:18788/webhook/tldv
GET  http://localhost:18788/health
GET  http://localhost:18788/queue/status
```

**Registrar no tl;v:**
```
https://seu-servidor:18788/webhook/tldv
```
(tl;dv exige HTTPS em produção — ngrok ou Cloudflare Tunnel para expor)

---

## Como Rodar

### Pipeline completo (manual)
```bash
export TLDV_API_KEY="YOUR_TLDV_API_KEY_HERE"
export PYTHONPATH=$WORKSPACE/integrations

# Tudo
python3 integrations/tldv/pipeline.py

# Só coleta
python3 integrations/tldv/pipeline.py --stage collect

# Coleta + enrich
python3 integrations/tldv/pipeline.py --stage collect,enrich

# Digest do dia
python3 integrations/tldv/pipeline.py --stage digest --since 2026-04-06
```

### Dry-run (não escreve nada)
```bash
python3 integrations/tldv/pipeline.py --dry-run --stage collect,enrich
```

### Reprocessar reunião específica
```bash
python3 integrations/tldv/queue_processor.py --meeting-id 69d3f49884d30500130092c2
```

---

## Modos de Execução

| Modo | Comando | Quando |
|------|---------|--------|
| Webhook-driven | `queue_processor.py` a cada 1h | Para meetings que tiveram TranscriptReady/MeetingReady |
| Polling híbrido | `pipeline.py` a cada 6h | Garante que nada fica para trás |
| Digest diário | `pipeline.py --stage digest` | Relatório consolidado 1x/dia |
| Manual | qualquer script com `--dry-run` | Testar sem efeito |

---

## Estratégia Híbrida Webhook + Polling

### Por que os dois?
- **Webhook** = rápido, responde em minutos
- **Polling** = seguro, não perde nada mesmo se webhook falhar

### Fluxo
```
Nova reunião agendada
    ↓
tl;dv genera TranscriptReady (pode levar horas após a reunião)
    ↓
Webhook → /webhook/tldv → queue/{event}.json
    ↓
queue_processor (a cada 1h) → enrich + analyze
    ↓
pipeline (a cada 6h) → collect + enrich + analyze (polling fallback)
```

---

## Deduplicação

- **Webhook:** SHA256(eventType + meetingId + timestamp) em `.dedup_hashes.txt`
- **Enrich:** ledger em `enriched_ledger.json` (nunca reenriquece)
- **Analyze:** ledger em `analyzed_ledger.json` (nunca reanálise)
- **Persister:** SHA256 do texto normalizado em `persister_hashes.txt`

---

## Falhas e Recuperação

| Problema | Sintoma | Solução |
|----------|---------|---------|
| LLM timeout | rc=124 no log | 自动 retry — está no loop do runner |
| 5 erros seguidos | runner para e registra | Rodar novamente: `queue_processor.py --limit 20` |
| Webhook não chega | fila vazia | Verificar se ngrok/tunnel está ativo |
| Análise incompleta | normalized existe, analysis não | `pipeline.py --meeting-id ID` |
| Persister wrote wrong | pending.md sobrecrito | Reverter do git + rodar persister novamente |

### Reverter pending.md
```bash
git -C $WORKSPACE checkout -- memory/pending.md
```

---

## Registos

| Log | Conteúdo |
|-----|----------|
| `logs/tldv_pipeline.log` | Pipeline completo (estágios) |
| `logs/tldv_analyzer_2026.log` | Runner sequencial (batch 2026) |
| `logs/tldv_queue_processor.log` | Processamento de fila webhook |
| `logs/tldv_webhook.log` | Eventos recebidos |
| `logs/tldv_digest_*.md` | Digest consolidado |

---

## Configurar Webhook URL no tl;dl

1. Expor porta 18788 para internet (via Cloudflare Tunnel ou ngrok):
   ```bash
   cloudflared tunnel --url http://localhost:18788
   # Output: https://xxxx.trycloudflare.com/webhook/tldv
   ```
2. Registrar no dashboard tl;dv: `https://xxxx.trycloudflare.com/webhook/tldv`
3. Selecionar eventos: `MeetingReady`, `TranscriptReady`

---

## Pastas e Arquivos

```
memory/meetings/
├── raw/                    # Dados brutos (collect)
│   └── {meetingId}.json
├── transcripts/             # Transcripts (enrich)
│   └── {meetingId}.json
├── notes/                   # Notes (enrich)
│   └── {meetingId}.json
├── normalized/             # Consolidados (enrich)
│   └── {meetingId}.json
├── analysis/                # Análises executivas (analyze)
│   ├── {meetingId}.json
│   └── {meetingId}.md
├── queue/                   # Fila de webhooks
│   └── {timestamp}_{meetingId}_{eventType}.json
├── ledger/
│   ├── processed_meetings.json    # Collect
│   ├── enriched_ledger.json       # Enrich
│   ├── analyzed_ledger.json       # Analyze
│   ├── persisted_ledger.json       # Persister
│   └── persister_hashes.txt       # Dedup
└── docs/meeting-derived-updates/  # Patches sugeridos

logs/
├── tldv_pipeline.log
├── tldv_analyzer_2026.log
├── tldv_queue_processor.log
├── tldv_webhook.log
└── tldv_digest_YYYYMMDD_HHMMSS.md
```
