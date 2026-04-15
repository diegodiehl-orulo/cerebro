# JOB: Auditoria pending.md — Semanal (P2-A)

**Frequência:** Sexta 17h BRT
**Modelo:** minimax/MiniMax-M2.5
**Timeout:** 90s | **Retry:** 0

---

## PROTOCOLO

**Objetivo:** Verificar se `memory/pending.md` está limpo e relevante. Detectar itens obsoletos, duplicados, ou sem dono/prazo.

**Arquivo-fonte:** `/root/.openclaw/workspace/memory/pending.md`

---

## EXECUÇÃO

### ETAPA 1 — Ler pending.md
```
cat /root/.openclaw/workspace/memory/pending.md
```

### ETAPA 2 — Análise
Para cada item, verificar:
1. **Obsoleto?** → Concluído, cancelado, ou irrelevante para o contexto atual
2. **Duplicado?** → Mesmo assunto de outro item
3. **Sem dono?** → Item sem responsável atribuído
4. **Sem prazo?** → Item sem data limite
5. **Vencido?** → Data no passado sem resolução registrada
6. **Bloqueado >30 dias?** → Aguardando terceiros há mais de 30 dias sem follow-up

### ETAPA 3 — Classificar

| Status | Definição |
|--------|-----------|
| ✅ Válido | Tem dono + prazo + contexto claro |
| ⚠️ Arguido | Falta dono OU prazo (não vencidos) |
| 🔴 Obsoleto | Concluído / cancelado / duplicado / >30 dias parado |
| ❓ Indefinido | Não dá para classificar sem contexto adicional |

### ETAPA 4 — Gerar output

Se todos válidos → **NO_REPLY**

Se houver obsoletos ou arguidos → enviar Telegram para Diego (8671853499):

```
🔍 *Auditoria pending.md — [data]*

📊 *Resultado:* [N] válidos | [N] arguidos | [N] obsoletos

🔴 *Para arquivar/remover:*
• [item] — [razão: duplicado/concluído/bloqueado 30d+]

⚠️ *Para corrigir (sem dono ou prazo):*
• [item] — [o que falta]

👉 [1-2 ações concretas para limpar a lista]
```

---

## REGRAS
- Nunca alterar o arquivo pending.md diretamente
- Propor apenas — Diego aprova antes de qualquer mudança
- Se houver mais de 10 itens para arquivar → listar os 10 mais críticos e sinalizar o resto
- Formato: cards, não tabela (Telegram)
