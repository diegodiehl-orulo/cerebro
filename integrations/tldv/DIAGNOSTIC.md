# DIAGNOSTIC.md — tl;dv API v1alpha1

## Estado da Integração (06/04/2026)

| Item | Status | Observação |
|------|--------|-----------|
| Autenticação | ✅ Validada | Header `x-api-key` funciona |
| Health check | ✅ Validado | `{"status":"ok"}` |
| Listagem reuniões | ✅ Validado | 773 reuniões, paginação `page`/`pageSize` |
| Detalhe reunião | ✅ Validado | Retorna invitees, organizer, duration, url |
| Transcript | ✅ Validado | Array de turnos com speaker + text + timestamps |
| Notes | ✅ Validado | `structuredNotes` + `markdownContent` + `topics` |

---

## Formato Real dos Dados (confirmado via API)

### GET /health
```json
{ "status": "ok" }
```

### GET /meetings
```json
{
  "page": 1,
  "pageSize": 50,
  "pages": 16,
  "total": 773,
  "results": [
    {
      "id": "69d3f49884d30500130092c2",
      "name": "Diretoria: Alinhamento Semanal",
      "happenedAt": "Mon Apr 06 2026 18:00:00 GMT+0000 (Coordinated Universal Time)",
      "duration": 6929.226,
      "invitees": [{ "name": "Diego Diehl", "email": "diego.diehl@orulo.com.br" }],
      "organizer": { "email": "diego.diehl@orulo.com.br", "name": "Diego Diehl" },
      "url": "https://tldv.io/app/meetings/69d3f49884d30500130092c2",
      "extraProperties": { "conferenceId": "rra-szub-wdu" }
    }
  ]
}
```
**Paginação:** `page` (1-indexed) + `pageSize`.
**Campo de nome:** `name` — não `title`.
**Duração:** segundos (não minutos).
**Filtros disponíveis:** `meetingType` (`internal` | `external`).

### GET /meetings/{id}
```json
{
  "id": "69d3f49884d30500130092c2",
  "name": "Diretoria: Alinhamento Semanal",
  "happenedAt": "2026-04-06T18:00:00.000Z",
  "duration": 6929.226,
  "invitees": [...],
  "organizer": { "name": "Diego Diehl", "email": "diego.diehl@orulo.com.br" },
  "url": "https://tldv.io/app/meetings/69d3f49884d30500130092c2",
  "template": { "id": "ai-topics", "label": "Smart topics" },
  "extraProperties": { "conferenceId": "rra-szub-wdu" }
}
```
**Nota:** `happenedAt` neste endpoint vem em ISO 8601, diferente do `/meetings` (raw string).

### GET /meetings/{id}/transcript
```json
{
  "id": "69d3f4bf2e1fc40013292b08",
  "meetingId": "69d3f49884d30500130092c2",
  "data": [
    {
      "startTime": 25,
      "endTime": 33,
      "speaker": "Eduardo Stringhini",
      "text": "Deixa eu ver um assunto rápido aí que eu preciso da Google sexta-feira, eu"
    }
  ]
}
```
**Formato:** array de turnos cronológicos. `startTime`/`endTime` em segundos. Texto em UTF-8 com caracteres pt-BR. Transcrição crua (sem formatação).

### GET /meetings/{id}/notes
```json
{
  "structuredNotes": [
    {
      "segmentId": "69d4125bd920790012f0e688",
      "timestamp": 66,
      "text": "Gravação de eventos é importante para divulgação e replicação de modelo",
      "topicId": "69d4125bd920790012f0e668"
    }
  ],
  "markdownContent": "## 1. Itens de Ação\n\n- [ ] Diego marcar reunião com Lab Playbook...",
  "topics": [
    {
      "id": "69d4125bd920790012f0e666",
      "order": 1,
      "title": "Itens de Ação",
      "summary": ""
    }
  ]
}
```
**Estrutura rica:** topics ordenados + notas segmentadas com timestamp + markdown pronto para renderizar.

---

## Riscos e Limitações

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| `meetingType` inválido → 400 com errors array | Listagem quebra se filtro errado | Não usar filtros sem validar valores primeiro |
| `pageSize` máximo desconhecido | Pode truncnar em valor alto | Manter em 50 por enquanto |
| Transcrição pode ter texto cru com ruído | Análise pode ser impacted | Limpar texto antes de usar |
| Notes expiram em 2 dias (plano gratuito) | Perder histórico se plan free | Não depende de nós — risco do organizer's plan |
| `template: null` em reuniões sem IA | Falta `ai-topics` | Tratar null na Extrair/Agregar |

---

## Erros — Formato Confirmado

**400 Validation Error:**
```json
{
  "message": "Invalid query params, check 'errors' property for more info.",
  "errors": [{ "property": "meetingType", "constraints": { "isEnum": "meetingType must be one of the following values: internal, external" } }]
}
```

**401/403/404:**
```json
{ "name": "NotFoundError", "message": "Meeting not found" }
```

---

## O que NÃO fazer agora

- Webhooks
- Bulk export
- Análise de sentiment

---

## Próximos Passos Recomendados

1. Criar script `get_meeting_full.py` — busca meeting + transcript + notes em uma chamada
2. Testar filtro `meetingType=internal` vs `external` na listagem
3. Descobrir `pageSize` máximo (testar 100, 200)
4. Implementar retry com backoff para 429/5xx
5. Avaliar storage de transcripts/notes (Drive ou local)
