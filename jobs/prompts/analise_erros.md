# JOB: Análise de Erros de Cron Runs — Diária (P2-B)

**Frequência:** Seg-Sex 07h BRT
**Gate:** remains ≥ 40
**Modelo:** minimax/MiniMax-M2.5
**Timeout:** 90s | **Retry:** 0

---

## PROTOCOLO

**Objetivo:** Detectar padrões de erro em jobs que falharam nas últimas 24h. Identificar se há degradação sistêmica ou falha isolada.

**Arquivo-fonte:** `/root/.openclaw/logs/cron_runs_*.log` ou saída de `cron runs` (últimas 24h)

---

## EXECUÇÃO

### ETAPA 1 — Coletar falhas
```
# Listar jobs com erro nas últimas 24h
# Verificar logs em /root/.openclaw/logs/
ls -lt /root/.openclaw/logs/*.log 2>/dev/null | head -10
```

### ETAPA 2 — Analisar padrões
Para cada falha, classificar:
1. **Timeout** → Job muito longo para o timeout configurado
2. **Erro de script** → Bug ou exceção no código
3. **Erro de API/externo** → Integração com Gmail, Drive, Bitrix falhou
4. **Erro de credencial** → Token expirado, auth failure
5. **Sobrou em NO_REPLY** → Agendado mas não executou (gate falhou)

### ETAPA 3 — Classificar severidade

| Severidade | Critério |
|------------|----------|
| 🔴 Alta | 3+ falhas do mesmo tipo em 7 dias OU job P0/P1 com erro |
| 🟡 Média | 1-2 falhas recentes do mesmo tipo |
| 🟢 Baixa | Falha isolada, já corrigida ou não-repetitiva |

### ETAPA 4 — Gerar output

Se nenhuma falha → **NO_REPLY**

Se houver falha de severidade média ou alta → enviar Telegram para Diego (8671853499):

```
🔧 *Análise de Erros — [data]*

🔴 *[se aplicável]* ALERTA: [pattern critico]
🟡 *[se aplicável]* Padrão: [pattern médio]

📋 *Detalhes:*
• [Job Name] — [erro específico] — [última tentativa]
• [Job Name] — [erro específico] — [última tentativa]

💡 *Causa raiz suspeita:* [análise]
👉 *Recomendação:* [ação sugerida — não executar, apenas propor]
```

---

## REGRAS
- Apenas reportar. Não corrigir automaticamente.
- Se timeout recorrente → sugerir aumento de timeout no job (comando exato)
- Se erro de API → verificar se já foi reportado recentemente (evitar spam)
- Formato: cards, não tabela (Telegram)
