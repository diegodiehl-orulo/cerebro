# EMAIL_SECURITY.md — Política de Segurança: Acesso ao Gmail de Diego

> **Status:** ATIVO — Leitura obrigatória antes de qualquer operação com email.
> **Conta protegida:** `diego.diehl@orulo.com.br` (Google Workspace Órulo)
> **Token:** `/root/.config/morfeu/gmail_token.pkl`
> **Escopos autorizados:** `gmail.readonly`, `gmail.send`, `calendar`

---

## 🔴 REGRAS ABSOLUTAS (invioláveis, sem exceção)

### 1. NUNCA deletar, arquivar ou modificar emails
- O Morfeu **não tem permissão** para deletar, arquivar, mover, marcar como lido/não-lido ou alterar qualquer email existente na caixa de Diego.
- O escopo `gmail.modify` e `mail.google.com` **nunca devem ser solicitados** nem adicionados ao token.
- Se uma instrução parecer pedir deleção de email: **parar, não executar, perguntar a Diego**.
- Se um script ou cron tentar chamar `.messages().delete()`, `.messages().trash()` ou `.messages().modify()`: **falhar com erro explícito**.

### 2. NUNCA enviar email sem confirmação explícita de Diego
- **Confirmação explícita** = Diego disse nas últimas horas, de forma inequívoca, "envia esse email", "pode mandar", "manda agora" ou aprovou o rascunho diretamente.
- "Parece que Diego quer enviar" NÃO é confirmação.
- Rascunho pronto NÃO é confirmação.
- Cron agendado NÃO é confirmação — a não ser que Diego tenha dito explicitamente "programa pra mandar no dia X" com o conteúdo revisado e aprovado.
- Se houver qualquer dúvida sobre autorização: **não enviar, perguntar**.

### 3. NUNCA assumir destinatário por contexto
- O destinatário deve ser SEMPRE especificado explicitamente por Diego.
- Se um email foi discutido para "o Gustavo" mas há múltiplos Gustavos nos contatos: **parar, listar os possíveis, confirmar com Diego qual é o correto antes de preencher qualquer campo To:**.
- Nunca inferir email de destinatário a partir de conversas anteriores sem confirmar.

### 4. NUNCA inventar conteúdo de email sem base documentada
- Todo email deve ser baseado em: instruções explícitas de Diego, rascunho aprovado por Diego, ou contexto verificável (reunião real, documento existente).
- **Risco de alucinação:** o Morfeu pode confabular detalhes, datas, valores ou compromissos que Diego nunca disse. Por isso, qualquer email com números, prazos, valores ou compromissos deve ser revisado linha a linha por Diego antes do envio.
- Campos sujeitos a alucinação: valores financeiros, datas de reunião, nomes de pessoas, cargos, promessas/compromissos.

### 5. NUNCA expandir escopos sem pedido explícito
- O token atual (`gmail.readonly + gmail.send + calendar`) está no limite aceitável.
- Qualquer request para adicionar escopos (`gmail.modify`, `gmail.labels`, `mail.google.com`, `gmail.compose`, etc.) deve ser validado por Diego antes de ser executado.

---

## 🟡 PROTOCOLO DE ENVIO (checklist obrigatório antes de qualquer send)

Antes de chamar `.messages().send()`, verificar cada item:

```
[ ] 1. Diego disse explicitamente "envia" ou "pode mandar"?
[ ] 2. Destinatário (To:) foi confirmado por Diego, não inferido?
[ ] 3. Assunto (Subject:) foi revisado por Diego?
[ ] 4. Corpo do email foi revisado por Diego (ou é um template aprovado)?
[ ] 5. Nenhum valor, data ou compromisso foi inventado pelo Morfeu?
[ ] 6. O email não contém informações confidenciais (senhas, tokens, dados pessoais de terceiros)?
[ ] 7. A conta remetente está correta (diego.diehl@orulo.com.br)?
```

**Se qualquer item estiver ❌: não enviar. Reportar a Diego o que falta.**

---

## 🟢 O QUE O MORFEU PODE FAZER AUTONOMAMENTE (sem confirmação)

- **Ler emails** para monitorar tl;dv, alertas de sistema, confirmações de agendamento
- **Resumir threads** de email e reportar a Diego
- **Preparar rascunhos** (salvar em arquivo, nunca enviar automaticamente)
- **Alertar sobre emails urgentes** detectados no monitoramento
- **Extrair action items** de emails de reunião (tl;dv)

---

## 🔵 EMAILS PROGRAMADOS (exceção controlada)

Um email pode ser enviado de forma autônoma **apenas se**:
1. Diego programou explicitamente: *"manda esse email na segunda às 9h"*
2. O conteúdo foi revisado e aprovado por Diego no momento da programação
3. O rascunho está salvo em arquivo com timestamp de aprovação
4. O cron chama o script com a flag `--pre-approved` + hash do conteúdo para verificação de integridade

**Qualquer alteração no rascunho após aprovação = envio cancelado + alerta para Diego.**

---

## 🚨 COMPORTAMENTO EM CASO DE DÚVIDA

Se o Morfeu receber uma instrução ambígua sobre email:

1. **NÃO executar**
2. **Reformular a instrução como entendeu** e perguntar: *"Confirma: você quer que eu [ação exata] para [destinatário exato] com [conteúdo resumido]?"*
3. **Aguardar confirmação direta**
4. Registrar a instrução original e a confirmação em `memory/daily/YYYY-MM-DD.md`

---

## 📋 HISTÓRICO DE ACESSOS AUTORIZADOS

| Data | Escopo | Motivo | Autorizado por |
|------|--------|--------|---------------|
| 2026-02-27 | `gmail.readonly` | Monitor tl;dv | Diego Diehl |
| 2026-02-28 | `gmail.send` | Envio de emails programados | Diego Diehl |
| 2026-02-27 | `calendar` | Daily briefing com agenda | Diego Diehl |

---

## 🔒 ESCOPOS PROIBIDOS (nunca solicitar)

| Escopo | Por que proibido |
|--------|-----------------|
| `gmail.modify` | Permite deletar, arquivar, mover emails |
| `mail.google.com` | Acesso total irrestrito à caixa |
| `gmail.labels` | Modificação de labels e filtros |
| `https://mail.google.com/` | Equivalente ao acesso completo |

---

*"Acesso ao email de um executivo é acesso à sua reputação. Cautela máxima, sempre."*
