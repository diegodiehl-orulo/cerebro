# JOB: Revisão Self-Improving — Sex 18h

**Frequência:** Sexta 18h BRT
**Gate:** remains ≥ 40
**Modelo:** minimax/MiniMax-M2.5
**Timeout:** 120s | **Retry:** 0

---

## PROTOCOLO

**Objetivo:** Revisar o ciclo de aprendizados da semana, identificar padrões e reportar Diego.

---

## EXECUÇÃO

### ETAPA 1 — Ler .learnings/
```
cat /root/.openclaw/workspace/.learnings/LEARNINGS.md
cat /root/.openclaw/workspace/.learnings/ERRORS.md
cat /root/.openclaw/workspace/.learnings/FEATURE_REQUESTS.md
```

### ETAPA 2 — Analisar
- Itens novos da semana
- Padrões recorrentes
- Erros não resolvidos
- Requests pendentes

### ETAPA 3 — Gerar output

Se nada relevante → NO_REPLY

Se houver aprendizados ou alertas → Telegram para Diego (8671853499):

```
🔄 *Revisão Semanal — .learnings*

📚 *Esta semana:*
• [N] aprendizados novos
• [N] erros registrados
• [N] feature requests

🔁 *Padrões identificados:*
• [padrão 1]
• [padrão 2]

⚠️ *Pendências:*
• [erro não resolvido]
• [feature request pendente]

💡 *Sugestão:*
• [1 evolução do sistema se aplicar]
```

---

## REGRAS
- Formato: cards, não tabela
- Máx 15 linhas
- Apenas reportar, não modificar arquivos
