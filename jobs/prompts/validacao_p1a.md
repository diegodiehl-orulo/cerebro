# JOB: Validação P1-A — Constraint Check Pós-Execução

**Frequência:** Seg-Sex 07h30 e 17h30 BRT
**Gate:** Verificação automática após execução de P1-A (não tem gate de quota próprio — é pós-execução)
**Modelo:** minimax/MiniMax-M2.5
**Timeout:** 120s | **Retry:** 0

---

## PROTOCOLO

**Objetivo:** Após cada execução de P1-A (Daily Briefing e Revisão Semanal), validar que o output atende aos critérios mínimos de qualidade.

**Jobs P1-A a monitorar:**
- Daily Briefing (`19741391`) — Seg-Sex 08:45
- Revisão Semanal (`ab458393`) — Sex 16h

---

## EXECUÇÃO

### ETAPA 1 — Verificar se Daily Briefing rodou
```
# Cron runs do Daily Briefing
# Verificar: output existe? contém seções esperadas?
```

Critérios de validação do Daily Briefing:
- Contém bloco "PRÓXIMAS AÇÕES" ou similar? (próximo passo com dono + prazo)
- Contém agenda do dia?
- Contém pelo menos 3 seções identificáveis?
- Output > 500 caracteres?

### ETAPA 2 — Verificar se Revisão Semanal rodou (se hoje é sexta)
```
# Cron runs da Revisão Semanal
# Verificar: output existe? contém seções esperadas?
```

Critérios de validação da Revisão Semanal:
- Contém bloco "TOP 10 PENDÊNCIAS"?
- Contém bloco "3 DECISÕES"?
- Contém bloco "3 PONTOS DE ATENÇÃO"?
- Output > 1000 caracteres?

### ETAPA 3 — Gerar output

Se validação OK → **NO_REPLY**

Se falha de validação → enviar Telegram para Diego (8671853499):

```
⚠️ *Constraint Check P1-A — [data]*

🔴 *[Job Name]* — Output abaixo do esperado

📋 *Critérios que falharam:*
• [critério 1]
• [critério 2]

📝 *Output recebido:* [primeiras 300 caracteres ou summary]

👉 *Recomendação:* [sugestão — revisar prompt, aumentar timeout, etc.]
```

---

## REGRAS
- Executa APÓS os jobs P1-A, não antes
- Não é gate — é verificação pós-execução
- Revisão Semanal só verifica nas sextas
- Formato: cards, não tabela (Telegram)
- Propor ação corretiva, não corrigir automaticamente
