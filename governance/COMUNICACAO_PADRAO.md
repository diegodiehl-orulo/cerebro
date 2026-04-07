# COMUNICAÇÃO PADRÃO — Todos os Bots (Morfeu, Lara, Claudinei)

> **Versão:** v1 | **Atualizado:** 2026-04-06
> **Scope:** Todas as entregas de todos os bots da arquitetura (Morfeu, Larissa, Claudinei)
> **Regra:** Sem exceção — qualquer canal (Telegram, DM, grupo, cron, reply, subagente).

---

## 1. REGRA DE OURO — Tabelas com pipes/traços

**PROIBIDO** usar tabelas Markdown com pipes (`| ... |`) em qualquer entrega via Telegram.

Toda tabela com estrutura colunar **DEVE** ser:
1. Convertida em **texto descritivo** (blocos numerados ou bullets)
2. **Ou** exportada como arquivo `.csv` / `.txt` em anexo

**Por quê?** O Telegram não renderiza tabelas Markdown — elas aparecem como texto plano com barras e espaços, ilegíveis no mobile.

---

## 2. ESTRUTURA DE ENTREGA PADRÃO

### 2.1. Sempre abrir com: "Resumo em texto"

```
Resumo em texto:
```

### 2.2. Colunas — usar formato "Coluna X = ..."

Quando a informação tiver estrutura tabular, escrever cada coluna explicitamente:

```
Coluna 1 = Workstream
Coluna 2 = DRI
Coluna 3 = Status
Coluna 4 = Próximo passo
```

### 2.3. Itens — formato Card (sem tabela)

```
🟡 WS1 — Comunicação com Corretores
• Coluna 1 (Workstream) = WS1 — Comunicação com Corretores
• Coluna 2 (DRI) = Mayumi
• Coluna 3 (Status) = Kickoff pendente
• Coluna 4 (Próximo passo) = Confirmar data de kickoff
```

**Separador entre cards:** linha em branco (sem `---` ou `===`).

### 2.4. Fechamento padrão

Sempre terminar com:

```
Se quiser, posso mandar o arquivo completo como anexo.
```

---

## 3. REGRAS DE FORMATO MOBILE

**PROIBIDO:**
- Tabelas Markdown (`| col | col |`)
- Listas aninhadas com mais de 2 níveis
- Parágrafos com mais de 4 linhas sem quebra
- Blocos de código como substituto de lista

**OBRIGATÓRIO:**
- Bullets `•` para listas
- **Negrito** para destacar nome, prazo ou decisão
- Emojis como marcadores visuais de status: 🟢 🟡 🔴 ⚫ 👤 📊 ⚠️ 👉
- Linha em branco entre blocos temáticos
- Máximo 4 linhas por bloco antes de quebrar

---

## 4. ESCOPO DE APLICAÇÃO

| Bot | Username |应用规则 |
|-----|----------|---------|
| Morfeu | @Base_DD_bot | ✅ Regra absoluta |
| Larissa | @larissa_personal_assistant_bot | ✅ Regra absoluta |
| Claudinei | @Claudinei_Master_Bot | ✅ Regra absoluta |
| Subagentes | — | ✅ Regra absoluta |

**Canal:** Telegram (grupo + DM + threads).

---

## 5. COMO REFERENCIAR ESTA REGRA

Qualquer bot ou sessão deve abrir com:

> *"Li a política de comunicação padrão. Todas as entregas seguirão o formato textual com colunas descritas e arquivo em anexo quando necessário."*

Se a conversa envolver um pedido de tabela/lista, aplicar automaticamente sem precisar perguntar.

---

## 6. EXEMPLO COMPLETO DE ENTREGA

```
Resumo em texto:

🟡 WS1 — Comunicação com Corretores
• Coluna 1 (Workstream) = WS1 — Comunicação com Corretores
• Coluna 2 (DRI) = Mayumi
• Coluna 3 (Status) = Kickoff pendente de data
• Coluna 4 (Próximo passo) = Confirmar data na Terça (07/04)

🟢 WS2 — Jornada DL → Pago
• Coluna 1 (Workstream) = WS2 — Jornada DL → Pago
• Coluna 2 (DRI) = Gustavo Torres
• Coluna 3 (Status) = Kickoff realizado em 19/03
• Coluna 4 (Próximo passo) = Revisar e-mail de onboarding com Jade

🔴 WS6 — Embaixadoras Drive Free
• Coluna 1 (Workstream) = WS6 — Embaixadoras Drive Free
• Coluna 2 (DRI) = Diego (provisório)
• Coluna 3 (Status) = Sem início — DRI não confirmado
• Coluna 4 (Próximo passo) = Definir DRI até 10/04

Se quiser, posso mandar o arquivo completo como anexo.
```

---

*Regra criada em 2026-04-06 por Diego Diehl para padronizar entregas de todos os bots da arquitetura.*
