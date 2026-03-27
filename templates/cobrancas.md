# templates/cobrancas.md — Cobranças e Follow-ups (v0)

> **Criado:** 2026-03-05
> **Objetivo:** Gerar cobranças consistentes em 3 níveis (N1 → N2 → N3). Suportar execução via Lara com segurança.
> **Prioridade:** E-mail. DM como alternativa rápida. WhatsApp para grupos (versão SAFE + aprovação).

**Regras:**
- Preencher todos os placeholders antes de enviar.
- Interno: mais direto. Externo: mais conservador.
- Grupo: somente versão SAFE e somente com autorização de Diego.

---

## Campos padrão (placeholders)

| Placeholder | Descrição |
|-------------|-----------|
| `[ASSUNTO]` | Assunto do e-mail |
| `[DESTINATÁRIO_NOME]` | Nome do destinatário |
| `[DESTINATÁRIO_EMAIL]` | E-mail do destinatário |
| `[ITEM]` | O que precisa acontecer |
| `[CONTEXTO]` | 1 linha de contexto |
| `[DONO]` | Responsável pela entrega |
| `[PRAZO]` | Data/hora |
| `[PRÓXIMO_PASSO]` | Ação concreta esperada |
| `[LINK]` | Bitrix / doc / referência — opcional |
| `[SEVERIDADE]` | baixa / média / alta — opcional |

---

## NÍVEL 1 (N1) — Lembrete objetivo (gentil)

> **Uso:** Primeira cobrança ou follow-up inicial. SLA padrão: 1 dia após o prazo combinado.

### N1 — DM (interno)

```
Oi, [DESTINATÁRIO_NOME]. Só reforçando: [ITEM].
Próximo passo: [PRÓXIMO_PASSO] até [PRAZO].
Se tiver bloqueio, me sinaliza com o que falta.
```

---

### N1 — E-mail (interno)

**Assunto:** [ASSUNTO]

```
Olá, [DESTINATÁRIO_NOME],

Só reforçando o ponto abaixo para mantermos o ritmo:

- Item: [ITEM]
- Próximo passo: [PRÓXIMO_PASSO]
- Prazo: [PRAZO]
- Referência: [LINK]

Se houver algum bloqueio, me sinalize com o que falta para destravar.

Obrigado,
Diego

```

---

### N1 — E-mail (externo — conservador)

**Assunto:** [ASSUNTO]

```
Olá, [DESTINATÁRIO_NOME],

Retomando rapidamente nosso combinado:

- Item: [ITEM]
- Próximo passo: [PRÓXIMO_PASSO]
- Prazo sugerido: [PRAZO]

Caso precise ajustar prazos, por favor me avise e proponha uma alternativa.

Atenciosamente,
Diego

```

---

### INSTRUÇÕES PARA LARA — N1

```
📋 LARA — Cobrança N1

1. Verificar se é INTERNO ou EXTERNO.
2. Preencher placeholders: [DESTINATÁRIO_NOME], [ITEM], [PRÓXIMO_PASSO], [PRAZO], [LINK].
3. Usar template correspondente (interno ou externo).
4. Aguardar aprovação: "OK para enviar N1".
5. Após envio: registrar em memory/pending.md:
   - status = AGUARDANDO
   - Follow-up agendado: D+2 se não houver resposta.
```

---

## NÍVEL 2 (N2) — Cobrança direta (prazo + consequência operacional)

> **Uso:** Sem resposta/execução após N1, ou prazo já passou.

### N2 — DM (interno)

> Curto. Usar somente se não houver resposta ao N1.

```
Precisamos fechar [ITEM] hoje para não travar o fluxo.
Confirma entrega até [PRAZO] e qual é o próximo passo: [PRÓXIMO_PASSO]?
Se não der, me manda agora o novo prazo e o bloqueio.
```

---

### N2 — E-mail (interno)

**Assunto:** [ASSUNTO] — prazo e confirmação

```
Olá, [DESTINATÁRIO_NOME],

Estou retomando porque o prazo está crítico para não travarmos o fluxo.

- Item: [ITEM]
- Próximo passo esperado: [PRÓXIMO_PASSO]
- Prazo: [PRAZO]
- Referência: [LINK]

Por favor, responda confirmando:
(i) entrega até [PRAZO], ou
(ii) qual bloqueio existe e qual novo prazo você assume.

Obrigado,
Diego

```

---

### N2 — E-mail (externo — firme, mas educado)

**Assunto:** [ASSUNTO] — confirmação de prazo

```
Olá, [DESTINATÁRIO_NOME],

Para mantermos o andamento, preciso confirmar o próximo passo:

- Item: [ITEM]
- Próximo passo: [PRÓXIMO_PASSO]
- Prazo: [PRAZO]

Você consegue confirmar esse prazo? Se não, por favor indique a melhor alternativa.

Atenciosamente,
Diego

```

---

### INSTRUÇÕES PARA LARA — N2

```
📋 LARA — Cobrança N2

1. Só usar quando: (a) prazo passou, ou (b) N1 sem resposta em D+2.
2. Preencher "consequência operacional" apenas se for interno e factual (sem ameaça).
3. Aguardar aprovação: "OK para enviar N2".
4. Após envio: registrar em memory/pending.md:
   - status = VENCIDO ou 48H
   - Follow-up agendado: D+1.
```

---

## NÍVEL 3 (N3) — Escalonamento (visibilidade e decisão)

> **Uso:** Repetição do atraso, bloqueio recorrente, risco alto ou necessidade de decisão de liderança.
> ⚠️ **Regra:** N3 só com autorização explícita de Diego.

### N3 — DM (interno)

```
Vou escalar porque está impactando execução.
Status atual: [ITEM] (prazo: [PRAZO]) — bloqueio: [BLOQUEIO].
Preciso de uma decisão: [DECISÃO] até [PRAZO_DECISÃO].
```

---

### N3 — E-mail (interno — com CC sugerido)

**Assunto:** [ASSUNTO] — escalonamento e decisão

```
Olá, [DESTINATÁRIO_NOME],

Estou escalando para resolver e destravar execução.

- Item: [ITEM]
- Prazo original: [PRAZO]
- Status atual: [STATUS]
- Bloqueio: [BLOQUEIO]
- Próximo passo proposto: [PRÓXIMO_PASSO]
- Decisão necessária: [DECISÃO] até [PRAZO_DECISÃO]
- Referência: [LINK]

Peço confirmação do encaminhamento ou ajuste do plano com novo prazo assumido.

Obrigado,
Diego

```

---

### N3 — Grupo SAFE (somente com autorização)

```
Pessoal, para destravar execução, precisamos definir hoje: [DECISÃO].
Item: [ITEM] — Dono: [DONO] — Prazo: [PRAZO_DECISÃO].
Se houver bloqueio, sinalizar até [PRAZO_DECISÃO].
```

---

### INSTRUÇÕES PARA LARA — N3

```
📋 LARA — Escalonamento N3

⚠️ Nível máximo. NUNCA enviar sem "OK para enviar N3" de Diego.

1. Confirmar autorização explícita antes de qualquer ação.
2. Se for e-mail com CC — sugerir conforme o tema:
   - Comercial → Gustavo Torres (Coord. Comercial)
   - Operação / processo → Eduardo (COO)
   - CS / execução → Marcelo Rodrigues (Dir. Operações/CS)
   - Diego decide o CC final.
3. Produzir 2 versões:
   - FULL (e-mail com contexto completo)
   - SAFE (grupo WhatsApp, se solicitado — sem dados sensíveis)
4. Após envio: registrar em memory/pending.md:
   - status = BLOQUEADO
   - Criar item "decisão pendente": [DECISÃO] — dono — [PRAZO_DECISÃO]
```

---

## Fluxo Resumido

```
Prazo combinado
      ↓ +1 dia
   N1 — Lembrete gentil
        (interno: DM ou e-mail | externo: e-mail conservador)
      ↓ sem resposta
   N2 — Cobrança direta + confirmação de prazo ou bloqueio
      ↓ sem resposta
   N3 — Escalonamento + decisão ← SEMPRE aprovação de Diego
```

---

## Rodapés e Observações

- Todo e-mail gerado deve conter o rodapé DD-Code.
- Foco em: item, prazo, próximo passo, confirmação — sem excesso de texto.
- Sem ameaças — apenas consequência operacional factual.
  - ✅ *"para não travar agenda/pipeline"*
  - ❌ *"se não fizer, vou tomar uma decisão"*
- SLAs de N2 e N3: cadência a detalhar por tipo de demanda (comercial, operacional, financeiro).
- Integração futura com WhatsApp individual: quando Telegram Userbot estiver ativo.
