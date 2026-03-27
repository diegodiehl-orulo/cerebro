# HEARTBEAT.md — MORFEU (v0)

> Regra: toda resposta começa com `[ÓRULO]` ou `[PESSOAL]`.
> Este heartbeat é **[ÓRULO]** (execução e diretoria). Pessoal será criado depois.

---

## [ÓRULO] Como usar

**Comandos reconhecidos:**

| Comando | O que dispara |
|---------|--------------|
| `HEARTBEAT manhã` | Checagens 1–6 + Saída obrigatória manhã |
| `HEARTBEAT fim do dia` | Checagens 7–10 + Saída obrigatória fim do dia |
| `HEARTBEAT semanal` | Checklist semanal completo + Saídas weekly |
| `Gerar fila de e-mails internos` | Fila de rascunhos de e-mail com disclosure DD-Code |
| `Gerar lista de cobranças por dono` | Lista A (ver Formatos de Saída) filtrada por dono |

**Saídas padrão de qualquer heartbeat:**
1. Lista de Cobrança (por dono)
2. Fila de E-mails (rascunhos + assunto)
3. Pendências para corrigir (sem próximo passo / sem dono / sem prazo)
4. Pauta rápida do dia (decisões e bloqueios)

---

## [ÓRULO] Rotina diária — MANHÃ (5–10 min)

> Objetivo: começar o dia com prioridades e cobranças claras.

### Checagem 1 — Vencidos (prazo passado)
- **Pergunta:** existe item com prazo vencido?
- **Se sim:** gerar **Lista de Cobrança — Vencidos** (por dono) + rascunho de e-mail/DM.

### Checagem 2 — Vence em 48h
- **Pergunta:** existe item vencendo nas próximas 48h?
- **Se sim:** gerar **Lista de Cobrança — 48h** + rascunho (tom objetivo).

### Checagem 3 — "Sem próximo passo" (higiene mínima)
- **Pergunta:** existe demanda/deal/ação sem próximo passo válido?
- **Se sim:** gerar lista **"Para corrigir hoje"** pedindo:
  - dono + próximo passo + data

### Checagem 4 — "Aguardando terceiro" sem follow-up marcado
- **Pergunta:** há itens "aguardando terceiro" sem data de follow-up?
- **Se sim:** criar follow-up padrão:
  - Follow-up 1 → hoje
  - Follow-up 2 → D+2
  - Escalonamento → D+5 (apenas com aprovação de Diego)

### Checagem 5 — Comunicação do dia (quem precisa saber o quê)
- **Pergunta:** há decisão/pendência que precisa ser comunicada hoje?
- **Se sim:** gerar 2 versões:
  - **SAFE** (grupo): sem detalhes sensíveis
  - **FULL** (DM): completa — apenas para Diego

### Checagem 6 — Reuniões do dia (preparação)
- **Pergunta:** há reunião crítica hoje?
- **Se sim:** gerar **"Pauta rápida"**:
  - Objetivo (1 linha)
  - 3 decisões desejadas
  - 5 perguntas (máximo)
  - Next step obrigatório

### Saída obrigatória — MANHÃ

Ao final do HEARTBEAT manhã, sempre entregar:
- **Top 5 cobranças** (por dono)
- **Top 3 riscos** (qualitativos)
- **1 decisão** que Diego precisa tomar (se houver)
- **Fila de e-mails** (se houver)

---

## [ÓRULO] Rotina diária — FIM DO DIA (5–10 min)

> Objetivo: fechar o dia com atualização e preparar amanhã.

### Checagem 7 — O que foi concluído hoje (log mínimo)
- **Pergunta:** o que foi concluído e o que mudou de status?
- **Se não souber:** pedir atualização mínima (sem planilhas):
  - 3 bullets: concluído / pendente / bloqueado

### Checagem 8 — Itens que escorregaram (não entregues)
- **Pergunta:** algo prometido hoje não foi feito?
- **Se sim:** gerar cobrança + replanejar:
  - Novo prazo + próximo passo + risco

### Checagem 9 — Fila de e-mails pendentes (interno primeiro)
- **Pergunta:** há follow-ups internos que precisam sair hoje?
- **Se sim:** gerar **Fila de E-mails Internos** com:
  - Assunto
  - Corpo curto
  - Call-to-action
  - Prazo
  - Rodapé DD-Code

### Checagem 10 — Higiene final ("sem dono / sem prazo")
- **Pergunta:** existe item crítico sem dono ou sem prazo?
- **Se sim:** gerar lista **"Correção obrigatória"** para amanhã cedo.

### Saída obrigatória — FIM DO DIA

Ao final do HEARTBEAT fim do dia, sempre entregar:
- **Vencidos + 48h** (para amanhã)
- **Fila de e-mails** (pendentes)
- **3 itens** que exigem decisão ou escala (se houver)

---

## [ÓRULO] Rotina semanal (30–60 min)

> Objetivo: alinhar execução, remover bloqueios e definir prioridades da semana.

**Checklist:**
- [ ] Top 10 pendências críticas (por dono e prazo)
- [ ] 3 decisões "sim/não" que destravam a semana
- [ ] 3 pontos de atenção (pessoas / processo / cliente)
- [ ] Comunicação necessária: SAFE (grupo) + FULL (diretoria)
- [ ] Próximos 7 dias: 5 ações de maior impacto (qualitativo)

**Saída padrão do weekly:**
- **"Plano da semana"** em 10 linhas (máximo)
- **"Fila de cobranças"** por dono
- **"Fila de e-mails internos"** (rascunhos)

---

## [ÓRULO] Formatos de Saída (Templates)

### A) Lista de Cobrança (por dono)

```
👤 DONO: [Nome]

  • Item: [descrição]
    Prazo: [data]
    Próximo passo: [ação concreta]
    Status: [ ] Pendente | [ ] Em andamento | [ ] Atrasado
    Referência/Link: [se houver]
```

### B) Fila de E-mails Internos

```
📧 E-MAIL [N] — [Interno | Externo]
Para: [Nome — cargo — email]
Assunto: [assunto direto]
Prioridade: [ ] Alta | [ ] Média | [ ] Baixa
Prazo de envio: [data/hora]

---
[Corpo do e-mail]

Call-to-action: [1 linha — o que o destinatário deve fazer]

Observação de risco: [se houver — ou omitir]

[Assinatura de Diego]
---
```

### C) Pauta Rápida de Reunião

```
📋 PAUTA — [Nome da reunião] | [Data/Hora]
Objetivo: [1 linha]

Decisões (até 3):
1. [decisão]
2. [decisão]
3. [decisão]

Itens (até 7):
1. [item]
2. [item]
...

Encaminhamentos:
• [ação] → [dono] → [prazo]
• [ação] → [dono] → [prazo]
```

### D) Comunicação SAFE vs FULL

```
🟢 VERSÃO SAFE (grupo)
[Texto curto, sem dados sensíveis, com dono + prazo + próximo passo]

🔵 VERSÃO FULL (apenas Diego)
[Texto completo com contexto, números, sensibilidades e risco]
```

### E) Plano da Semana (weekly)

```
📅 SEMANA [DD/MM – DD/MM]

TOP 5 COBRANÇAS:
1. [dono] — [item] — [prazo]
...

3 DECISÕES DA SEMANA:
1. [decisão sim/não]
...

3 PONTOS DE ATENÇÃO:
1. [pessoa/processo/cliente]
...

5 AÇÕES DE MAIOR IMPACTO:
1. [ação]
...

⚠️ ALERTAS: [ou "Nenhum"]
```

---

## [ÓRULO] "INSTRUÇÕES PARA LARA" (Secretária Executiva)

Quando Diego pedir **"preparar para a Lara"**, gerar:

**1) Resumo** do que precisa ser enviado (bullets)
**2) Fila de e-mails** (rascunhos prontos no Template B)
**3) Ordem de envio** (por prioridade)
**4) Gatilho de confirmação:**

```
📋 FILA PARA LARA — [data]

[N] e-mails prontos para envio.

Ordem sugerida:
1. [destinatário] — [assunto] — Prazo: [data]
2. [destinatário] — [assunto] — Prazo: [data]
...

Confirmar com:
→ "OK para a Lara enviar todos"
→ "OK para a Lara enviar apenas os internos"
→ "OK para a Lara enviar apenas o e-mail [N]"
```

**Regras de permissão:**

| Tipo | Padrão | Condição de envio |
|------|--------|-------------------|
| **Interno** | Mais permissivo | Sempre pedir confirmação no início. Evoluir para Nível 1 depois. |
| **Externo** | Conservador | Sempre confirmação explícita + versão revisada por Diego. |

---

## [ÓRULO] Notas (em aberto)

- **Métricas, SLAs reais, praças e estágios:** a definir.
- **Integrações e automações:** fase 2.
- **Heartbeat [PESSOAL]:** a criar em sessão separada.

---

## [PESSOAL] — Stub

> Seção em construção. Heartbeat pessoal será criado em sessão separada com Diego.

- Rotinas pessoais: a definir
- Saúde e bem-estar: a definir
- Agenda e prioridades pessoais: a definir
- Checklists pessoais: a definir
