# tl;dv — Pipeline de Enriquecimento

## Visão Geral

Pipeline de enriquecimento de reuniões: busca transcript + notes da API tl;dv para cada reunião em `memory/meetings/raw/` e gera um consolidado normalizado.

**Fluxo:**
```
raw/{id}.json  →  enricher.py  →  transcripts/{id}.json
                              →  notes/{id}.json
                              →  normalized/{id}.json
                              →  enriched_ledger.json
```

---

## Scripts

### Rotina principal — `enricher.py`
```bash
TLDV_API_KEY="${TLDV_API_KEY}" \
PYTHONPATH=/root/.openclaw/workspace/integrations \
python3 integrations/tldv/enricher.py
```

**Parâmetros:**
- `--limit N` — processar apenas N reuniões
- `--dry-run` — mostrar o que faria sem salvar
- `--meeting-id ID` — processar uma reunião específica

**Comportamento:**
- Apenas reuniões em `raw/` são processadas
- IDs já no ledger são pulados (idempotente)
- Lock file evita execuções concorrentes
- Transcript 204 (pendente) ≠ erro — registrado como `pending`
- Transcript vazio → `unavailable` (não é pending)
- Notes vazias → `unavailable`
- 401/403 → `error` (para e regista)

---

## Flags de Status

| Campo | Valores possíveis | Significado |
|-------|-------------------|-------------|
| `transcript_status` | `pending` / `available` / `unavailable` / `error` | Estado do transcript |
| `notes_status` | `available` / `unavailable` / `error` | Estado das notes |
| `analysis_status` | `not_started` / `ready` / `enriched` | Prontidão para análise IA |

**Lógica de `analysis_status`:**
- `available` em tx ou notes → `ready`
- ambos `unavailable` → `not_started`
- após enrich por IA → `enriched` (próxima fase)

**Lógica de `transcript_status`:**
- `pending` — API retornou 204 (transcript ainda processando)
- `available` — transcript com dados
- `unavailable` — reunião sem transcript ou sem dados
- `error` — erro de API (401/403/5xx)

---

## Estrutura de Arquivos Gerados

```
memory/meetings/
├── raw/                          # Dados brutos da coleta (meetings)
│   └── {meetingId}.json
├── transcripts/                  # Transcripts individuais
│   └── {meetingId}.json         # Resposta direta da API
├── notes/                        # Notes individuais
│   └── {meetingId}.json         # Resposta direta da API
├── normalized/                   # Consolidados por reunião
│   └── {meetingId}.json
└── ledger/
    ├── processed_meetings.json   # Ledger da coleta
    └── enriched_ledger.json      # Ledger do enrichment
```

---

## Modelo do JSON Normalizado

```json
{
  "meeting_id": "69d3f49884d30500130092c2",
  "name": "Diretoria: Alinhamento Semanal",
  "happened_at": "2026-04-06T18:00:00.000Z",
  "duration_seconds": 6929.226,
  "duration_minutes": 115.5,
  "organizer": { "name": "Diego Diehl", "email": "diego.diehl@orulo.com.br" },
  "invitees": [
    { "name": "Alejandro Olchik", "email": "alejandro@orulo.com.br" }
  ],
  "url": "https://tldv.io/app/meetings/69d3f49884d30500130092c2",
  "template": { "id": "ai-topics", "label": "Smart topics" },
  "conference_id": "rra-szub-wdu",

  "transcript_status": "available",
  "notes_status": "available",
  "analysis_status": "ready",

  "transcript": {
    "id": "69d3f4bf2e1fc40013292b08",
    "meetingId": "69d3f49884d30500130092c2",
    "data": [
      {
        "startTime": 25,
        "endTime": 33,
        "speaker": "Eduardo Stringhini",
        "text": "Deixa eu ver um assunto rápido aí que eu preciso da Google sexta-feira"
      }
    ]
  },
  "transcript_summary": {
    "entry_count": 89,
    "speakers": ["Diego Diehl", "Felipe Goettems", "Eduardo Stringhini", "Alejandro Olchik", "Marcelo Rodrigues"],
    "total_words_estimate": 12400,
    "duration_start": 1,
    "duration_end": 6929
  },
  "transcript_unavailable_reason": null,

  "notes": {
    "structuredNotes": [
      {
        "segmentId": "...",
        "timestamp": 66,
        "text": "Gravação de eventos é importante para divulgação...",
        "topicId": "..."
      }
    ],
    "markdownContent": "## 1. Itens de Ação\n\n- [ ] Diego marcar reunião...",
    "topics": [
      { "id": "...", "order": 1, "title": "Itens de Ação", "summary": "" }
    ]
  },
  "notes_summary": {
    "note_count": 34,
    "topic_count": 16,
    "has_markdown": true
  },
  "notes_unavailable_reason": null,
  "topics": [
    { "id": "...", "order": 1, "title": "Itens de Ação", "summary": "" }
  ],

  "_schema_version": "1.0",
  "_enriched_at": "2026-04-06T23:45:00.000Z",
  "collected_at": "2026-04-06T23:45:00.000Z"
}
```

---

## Ledger de Enrichment (`enriched_ledger.json`)

```json
{
  "enriched": ["id1", "id2", ...],
  "failed": ["id3", "id4", ...],
  "pending": [],
  "last_run": "2026-04-06T23:45:00Z",
  "stats": {
    "total": 23,
    "enriched": 20,
    "failed": 3,
    "skipped": 0
  }
}
```

---

## Reprocessamento

### Reprocessar reuniões com erro
```bash
# Opção 1: matar o ledger de failed (remove só os failed)
python3 -c "
import json
with open('/root/.openclaw/workspace/memory/meetings/ledger/enriched_ledger.json') as f:
    d = json.load(f)
d['failed'] = []  # limpa failures para reprocessar
d['enriched'] = [x for x in d['enriched'] if x not in d.get('_retry_ids', [])]
with open('/root/.openclaw/workspace/memory/meetings/ledger/enriched_ledger.json', 'w') as f:
    json.dump(d, f, indent=2)
print('Ledger limpo. Rode enricher.py novamente.')
"
```

### Reprocessar reunião específica
```bash
TLDV_API_KEY="..." PYTHONPATH=/root/.openclaw/workspace/integrations \
python3 integrations/tldv/enricher.py --meeting-id 69d3f49884d30500130092c2
```

### Forçar reprocessamento completo (limpa tudo)
```bash
rm /root/.openclaw/workspace/memory/meetings/ledger/enriched_ledger.json
rm /root/.openclaw/workspace/memory/meetings/transcripts/*.json
rm /root/.openclaw/workspace/memory/meetings/notes/*.json
rm /root/.openclaw/workspace/memory/meetings/normalized/*.json
# depois: python3 enricher.py
```

---

## Execução Periódica (Cron)

Recomenda-se rodar a cada 6h para captar transcripts que ficaram pendentes (204):
```
# crontab -e
0 */6 * * * TLDV_API_KEY="${TLDV_API_KEY}" PYTHONPATH=/root/.openclaw/workspace/integrations /usr/bin/python3 /root/.openclaw/workspace/integrations/tldv/enricher.py >> /root/.openclaw/workspace/logs/tldv_enricher.log 2>&1
```

**Log:** `/root/.openclaw/workspace/logs/tldv_enricher.log`

---

## Limitações e Riscos

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| Transcript 204 (pendente) | Não disponível ainda | Rodar novamente em horas |
| Rate limit desconhecido | 429 se exceder | Retry com backoff (próxima fase) |
| Notes AI desabilitadas | meeting sem topics | `template: null` → sem enrich |
| Plan free expira em 2 dias | Perder histórico | Ingestão agora enquanto disponível |
