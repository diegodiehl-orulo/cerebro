# governance/sprint_quinzenal_pracas.md
# Sistema: Sprint Quinzenal de Praças — Sócios Locais
*Versão: 1.0 | Criado: 2026-03 | Dono: Diego Diehl (Morfeu)*

---

## 1. OBJETIVO DO SISTEMA

Implementar governança leve e previsível para praças operadas por sócios locais.
Foco: disciplina de execução, comunicação estruturada, follow-up sem burocracia.

Praças ativas (fase inicial):
| Praça | Sócio Local | E-mail |
|-------|-------------|--------|
| Curitiba | Luiz Zanella | luiz.zanella@orulo.com.br |
| Vitória | Pedro Kneip | pkneip@orulo.com.br |

---

## 2. ESTRUTURA DO CICLO QUINZENAL

```
[QUI -7] → Lembrete: prazo do One-Pager é SEG EOD
[SEG 18:00] → Checagem: recebido? Se não → pré-alerta preparado
[TER 10:00] → Se ainda ausente → ALERTA no Telegram para Diego cobrar
[RECEBIMENTO] → Morfeu analisa → Telegram para Diego com análise completa
[VALIDAÇÃO] → Diego valida sprint → Morfeu agenda check-ins 2x/semana
[CHECK-IN TER + SEX 09:00] → Lembretes e rascunhos para Diego
[FINAL DO SPRINT] → Novo ciclo começa
```

**Timezone:** America/Sao_Paulo (BRT)

---

## 3. ONE-PAGER DO SPRINT (PADRÃO OBRIGATÓRIO)

### Assunto padrão do e-mail do sócio local:
```
ÓRULO | Sprint Quinzenal | Praça: {PRAÇA} | Período: {DD/MM–DD/MM} | One-Pager
```

Exemplos:
- `ÓRULO | Sprint Quinzenal | Praça: Curitiba | Período: 10/03–24/03 | One-Pager`
- `ÓRULO | Sprint Quinzenal | Praça: Vitória | Período: 10/03–24/03 | One-Pager`

### Blocos obrigatórios do One-Pager (e-mail escrito):
1. **Sprint (período) | Praça | Sócio local**
2. **Indicador norte** (1) — texto curto
3. **Planejado** (sprint anterior) — bullets
4. **Executado** (volume) — bullets + números se tiver
5. **Resultados** (3–5 números) — opcional, "a definir"
6. **Problemas/Oportunidades** (3 bullets + causa provável)
7. **Próximo sprint** — 3 compromissos:
   - C1 Meta (leading) — [número + prazo] ou [PREENCHER]
   - C2 Ação volumosa — [o quê + volume mínimo + lista-alvo]
   - C3 Ação estrutural — [o que muda no sistema]
8. **Riscos principais** (1–2)
9. **Pedido de ajuda à Matriz** (1 só)
10. **Evidências combinadas** — prints/links/listas/agenda/Bitrix

> Template de solicitação: `templates/email_onepager_request.md`

---

## 4. PAPÉIS E RESPONSABILIDADES

| Papel | Quem | Responsabilidade no sistema |
|-------|------|-----------------------------|
| Sócio Local | Zanella / Kneip | Enviar One-Pager até SEG EOD; responder check-ins |
| Diretor Comercial | Diego Diehl | Validar sprint; cobrar quando necessário; aprovar envios |
| Coordenação | Gustavo Torres | CC em e-mails; suporte operacional à praça |
| Secretária Executiva | Larissa (Lara) | Enviar e-mails aprovados por Diego |
| Facilitador | Morfeu | Analisar, alertar, gerar rascunhos |
| Comms Corretores | Ester | Acionar quando praça pede apoio de comunicação |
| Marketing | Mayumi | Acionar quando praça pede apoio de conteúdo/comunidade |

---

## 5. CANAIS DE COMUNICAÇÃO

| Tipo | Canal | Regra |
|------|-------|-------|
| Cobrança operacional | E-mail | Principal — sempre via Lara após aprovação |
| Alertas para Diego | Telegram | Pode ser gerado automaticamente (interno) |
| CRM | Bitrix | Somente referência. Sem edição nesta fase |
| Agenda | Google Calendar | Integração a definir |

**Rodapé obrigatório em todo e-mail:**
> *E-mail enriquecido com a IA DD-Code de Diego Diehl.*

---

## 6. POLÍTICA DE SEGURANÇA (INVIOLÁVEL)

1. **Nenhum job envia e-mail automaticamente.** Sempre: rascunho + INSTRUÇÕES PARA LARA + "OK para enviar?"
2. **Alertas via Telegram para Diego** podem ser gerados sem aprovação prévia (são internos).
3. **Não inventar números ou métricas.** Usar `[PREENCHER]` ou "a definir" onde faltar.
4. **Leitura de inbox** — integração a definir. Enquanto não integrado: Morfeu roda análise manual quando Diego cola o e-mail.
5. **Não editar Bitrix** nesta fase.

---

## 7. CHECK-INS DURANTE O SPRINT (2x por semana)

Após validação do sprint por Diego:
- **Terça 09:00** — Morfeu envia Telegram para Diego com:
  - "Pedir status do sprint da Praça X"
  - 4 perguntas padrão de check-in
  - Rascunho curto de mensagem para o sócio local
- **Sexta 09:00** — Mesmo formato

> Perguntas padrão: `templates/checkin_questions.md`
> Rascunho: Diego envia (ou pede para Lara). Nunca automático.

---

## 8. ATUALIZAÇÃO DE MEMÓRIA (após cada sprint fechado)

Morfeu atualiza automaticamente:
- `memory/projects_orulo.md` — sprint fechado, C1/C2/C3, gargalo
- `memory/pending.md` — follow-ups abertos
- `memory/lessons.md` — aprendizados extraídos (se relevante)

---

## 9. EVIDÊNCIAS ACEITAS

| Tipo | Exemplo |
|------|---------|
| Print Bitrix | Pipeline atualizado, registro de atividade |
| Print de conversa | WhatsApp, e-mail enviado |
| Link de agenda | Google Calendar com evento |
| Lista exportada | CSV ou print da lista abordada |
| Ata/Documento | Arquivo com data e assinatura do sócio |

> Sem evidência combinada = compromisso não conta como executado.

---

## 10. LOGS E RASTREABILIDADE

Cada sprint fechado gera entrada em `memory/projects_orulo.md`:
```
Sprint [nº] | [PRAÇA] | [período]
C1: [meta] → [resultado]
C2: [ação] → [executado]
C3: [estrutural] → [executado]
Gargalo: [identificado]
Aprendizado: [...]
```

---

*Política de revisão: a cada ciclo de 3 sprints (aprox. 6 semanas).*
*Atualizar este arquivo quando regras mudarem.*
