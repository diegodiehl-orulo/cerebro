# tl;dv API — Integração Morfeu

## Visão Geral

Pipelines de ingestão de reuniões do tl;dv via API v1alpha1.
Dados são salvos em `memory/meetings/raw/` com ledger de controle de processados.

---

## Estrutura de Arquivos

```
integrations/tldv/
├── client.py           # Cliente Python da API (TldvClient)
├── collector.py        # Rotina de coleta (lista + busca detalhes + salva)
├── test_health.py      # Teste rápido de conectividade
├── list_meetings.py    # Lista reuniões com paginação (manual)
├── README.md           # Este arquivo
└── DIAGNOSTIC.md       # Formato real dos dados, gaps, riscos

memory/meetings/
├── raw/                # Um arquivo JSON por reunião ({meetingId}.json)
│   ├── 69d3f49884d30500130092c2.json  # Diretoria: Alinhamento Semanal
│   └── ...
└── ledger/
    └── processed_meetings.json         # Controle de já processados
```

---

## Configuração

**1. Variável de ambiente (obrigatória):**
```bash
export TLDV_API_KEY="YOUR_TLDV_API_KEY_HERE"
```

**2. Caminho do Python:**
```bash
export PYTHONPATH=/root/.openclaw/workspace/integrations
```

---

## Scripts Disponíveis

### Teste de saúde da API
```bash
PYTHONPATH=/root/.openclaw/workspace/integrations \
TLDV_API_KEY="sua_chave" \
python3 integrations/tldv/test_health.py
```
Retorna: `{"status":"ok"}` ou erro de autenticação.

---

### Listar reuniões (manual)
```bash
PYTHONPATH=/root/.openclaw/workspace/integrations \
TLDV_API_KEY="sua_chave" \
python3 integrations/tldv/list_meetings.py --page 1 --page-size 10
```

---

### Coleta de reuniões (principal)
```bash
PYTHONPATH=/root/.openclaw/workspace/integrations \
TLDV_API_KEY="sua_chave" \
python3 integrations/tldv/collector.py
```

**Parâmetros:**
- `--pages N` — limitar a N páginas (default: todas)
- `--dry-run` — listar o que faria sem salvar nada
- `--page-size N` — reuniões por página (default: 50)

**O que faz:**
1. Lista reuniões (paginação automática)
2. Compara com ledger de processados
3. Para cada reunião nova: busca detalhes e salva em `memory/meetings/raw/{id}.json`
4. Atualiza o ledger ao final

**Saída típica:**
```
INFO — === COLETA tl;dv INICIADA ===
INFO — Passo 1/3: Listando reuniões...
INFO —  → Total de reuniões listadas: 773
INFO — Passo 2/3: Identificando reuniões novas...
INFO —  → Já processadas: 0
INFO —  → Novas nesta execução: 773
INFO — Passo 3/3: Buscando detalhes e salvando...
INFO —   ★ Nova salva: 69d3f49884d30500130092c2
INFO —   ✗ Erro ao buscar detalhes de xxx: Recurso não encontrado (404)
...
INFO — === COLETA FINALIZADA | 478s | novas: 769 | erros: 4 ===
```

---

## Formato dos Dados (confirmado)

### meeting detail — campos principais
```json
{
  "id": "69d3f49884d30500130092c2",
  "name": "Diretoria: Alinhamento Semanal",
  "happenedAt": "2026-04-06T18:00:00.000Z",
  "duration": 6929.226,
  "organizer": { "name": "Diego Diehl", "email": "diego.diehl@orulo.com.br" },
  "invitees": [{ "name": "Eduardo Stringhini", "email": "eduardo@orulo.com.br" }],
  "url": "https://tldv.io/app/meetings/69d3f49884d30500130092c2",
  "template": { "id": "ai-topics", "label": "Smart topics" },
  "extraProperties": { "conferenceId": "rra-szub-wdu" }
}
```

### Ledger (processed_meetings.json)
```json
{
  "processed": ["id1", "id2", ...],
  "last_run": "2026-04-06T22:48:51",
  "stats": {
    "total": 849,
    "new": 769,
    "errors": 4
  }
}
```

---

## Execução Periódica (Cron)

### Recomendação: a cada 6 horas
```bash
# crontab -e
TLDV_API_KEY="YOUR_TLDV_API_KEY_HERE"
PYTHONPATH=/root/.openclaw/workspace/integrations

0 */6 * * * /usr/bin/python3 /root/.openclaw/workspace/integrations/tldv/collector.py >> /root/.openclaw/workspace/logs/tldv_collector.log 2>&1
```

Ou via cron job no OpenClaw (Larissa pode agendar).

---

## Notas Importantes

- **IDs com 404:** Alguns IDs listados pela API retornam 404 no detail — são reuniões deletadas ou inacessíveis. O collector trata isso gracefully e continua.
- **Lock file:** Se o collector travar, remova `/root/.openclaw/workspace/memory/meetings/ledger/.processing_lock`.
- **Ledger:** Não edite manualmente. O collector gerencia.
- **Erro 401/403:** API key inválida ou revogada.

---

## Enriquecimento (transcript + notes)

```bash
PYTHONPATH=/root/.openclaw/workspace/integrations \
TLDV_API_KEY="YOUR_TLDV_API_KEY_HERE" \
python3 integrations/tldv/enricher.py
```

**Parâmetros:** `--limit N` | `--dry-run` | `--meeting-id ID`

**Flags de status:**
- `transcript_status`: `pending` | `available` | `unavailable` | `error`
- `notes_status`: `available` | `unavailable` | `error`
- `analysis_status`: `not_started` | `ready` | `enriched`

**Estrutura gerada:**
```
memory/meetings/
├── transcripts/{id}.json
├── notes/{id}.json
├── normalized/{id}.json   ← consolidado com metadados + flags
└── ledger/enriched_ledger.json
```

Documentação completa: `ENRICHMENT_README.md`

---

## Próximas Etapas (enriquecimento)

1. `GET /meetings/{id}/transcript` — baixar transcript por reunião
2. `GET /meetings/{id}/notes` — baixar notes estruturadas
3. Enriquecer JSONs salvos com transcript + notes
4. Indexar por speaker, data, tema
5. Integrar com Drive (Google Sheets ou Docs)
