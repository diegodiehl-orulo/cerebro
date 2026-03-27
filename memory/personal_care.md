# personal_care.md — Cuidados Pessoais de Diego

> Gerenciado pelo Morfeu. Atualizado automaticamente após cada serviço realizado.

---

## 💈 Cabelo — Moisés

| Campo | Valor |
|---|---|
| **Cabeleireiro** | Moisés |
| **ID Profissional** | `676076` |
| **Frequência** | A cada 21–28 dias |
| **Requisito** | Diego deve estar em São Paulo |
| **Plataforma** | Trinks |
| **URL booking** | https://www.trinks.com/barbearia-retrogol/framebusca |
| **Login** | diegodiehl0@gmail.com |
| **Estabelecimento ID** | `18557` |
| **Serviço** | Corte de Cabelo — ID `1329815` — 40min — R$137 |
| **Último corte** | 2026-03-02 |
| **Próxima janela** | 2026-03-23 a 2026-03-30 |

### Histórico
| Data | Observação |
|---|---|
| 2026-03-02 | Corte registrado (PACOTE CABELO 90 DIAS, 11:30) |
| 2026-03-02 | ⚠️ Morfeu fez booking acidental às 14:00 durante teste da API (cancelar manualmente) |

### API Trinks — Endpoints Mapeados
```
# Disponibilidade (auth via cookie TokenApiTrinks)
GET /api/v2/servicos/1329815/profissionais
    ?IdProfissionalEstabelecimento=676076&data=YYYY-MM-DD

# Agendamento (POST autenticado)
POST /api/v2/agendamentos
Body: {
  "idServicoEstabelecimento": "1329815",
  "idProfissional": "676076",
  "idEstabelecimento": 18557,
  "dataHora": "YYYY-MM-DD HH:MM",
  "comentarios": "",
  "origem": 4
}
# Retorna: {"idAgendamento": <id>, "descricao": "Seu pedido está confirmado"}
```

### Script
- **Arquivo:** `/root/.openclaw/workspace/scripts/trinks_booking.py`
- **Modo padrão:** `--dry-run` (sem `--confirm`, nunca agenda de verdade)

### Preferências de Horário
- **Horário preferido:** Segunda-feira às 11:30
- **Formato de sugestão:** sempre 4 opções de horário (não mais, não menos)
- **Prioridade na sugestão:** segundas-feiras 11:00–12:00 primeiro, depois outros dias/horários compatíveis

### Integração
- [x] Plataforma identificada: Trinks
- [x] API mapeada (disponibilidade + booking + auth via Playwright)
- [x] Script criado com dry-run obrigatório
- [ ] Cron de domingo para sugerir horários (aguarda aprovação de Diego)
- [ ] Endpoint de cancelamento (não encontrado via API — apenas via UI)

---

## 🦷 Dentista

| Campo | Valor |
|---|---|
| **Status** | Pendente — Diego adia sistematicamente |
| **Nota** | Lembrete periódico ativo (Sombra 4 detectada) |

---

## 🏋️ Treino

| Campo | Valor |
|---|---|
| **Frequência** | 5x/semana |
| **Horário** | 06:00–07:30 |
| **Status** | Ativo — pilar inegociável |

---

## 📋 Outros (backlog)

> Adicionar aqui quando Diego mencionar novos cuidados a rastrear.
