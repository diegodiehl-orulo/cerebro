# P10: DOCUMENTAÇÃO DO PROCESSO DE VENDAS — BDRs E CICLO COMERCIAL

**Versão:** 1.0
**Data de criação:** 26/03/2026
**Status:** PRONTO PARA RODAR
**DRI:** Gustavo Torres (WS4)
**WS associado:** WS4 — Estrutura Comercial e CRM
**Urgência:** BAIXA — rodar quando WS4 estiver mais estruturado

---

## CONTEXTO

A Órulo tem 2 BDRs ativos (modelo B2B).

O processo de venda existe na prática, mas **não está documentado de forma oficial**.

A ausência de documentação gera:
- inconsistência entre BDRs
- dificuldade de onboarding de novos vendedores
- impossibilidade de identificar onde o funil perde mais

O objetivo deste prompt é capturar e documentar o processo de venda **como ele é hoje** — não como deveria ser.

---

## INSTRUÇÃO PARA A IA

Você está atuando como Sistema Integrado de Gestão de OKRs e Inteligência Documental da Órulo.

Leia os documentos do WS4 antes de iniciar (Charter, Rituais Comerciais, CSDL).

Seu objetivo é conduzir uma sessão de extração do processo comercial atual com Diego e Gustavo Torres.

---

## ROTEIRO DE EXECUÇÃO

### ETAPA 1 — Mapeamento do funil atual

Pergunte sobre cada etapa do funil:

**Topo: Prospecção**
> Como os BDRs identificam e selecionam prospects hoje?
> Há lista fria, indicação, evento, ou múltiplos canais?
> Qual é a taxa de aproveitamento de lista (contato → interesse)?

**Abordagem inicial**
> Qual é o canal de primeiro contato: telefone, WhatsApp, e-mail, LinkedIn?
> Existe um script de abordagem padrão?
> Como é feita a qualificação inicial (ICP — perfil ideal)?

**Agendamento de reunião**
> Qual é a taxa de abordagem → reunião agendada?
> Quem faz a reunião: o próprio BDR, Diego, ou Gustavo?
> Há um deck ou material enviado antes da reunião?

**Reunião de descoberta / demo**
> Quanto tempo dura uma reunião típica?
> Existe roteiro de perguntas de qualificação?
> Quando a Órulo decide propor?

**Proposta e follow-up**
> Existe modelo de proposta?
> Qual o tempo médio de follow-up após proposta?
> Quantos contatos são feitos antes de considerar perdido?

**Fechamento**
> Quais as objeções mais comuns e como são tratadas?
> O que define um "sim"? Assinatura? Ativação? Primeiro pagamento?

**Pós-venda (handoff para CS)**
> Existe um processo formal de passagem do cliente para CS?
> O BDR acompanha os primeiros dias do cliente?

---

### ETAPA 2 — Dados do funil

> Qual é o ciclo de venda médio (primeiro contato → fechamento)?
> Qual é a taxa de conversão de reunião → proposta?
> Qual é a taxa de proposta → fechamento?
> Qual é o ticket médio de uma venda nova?

---

### ETAPA 3 — Diagnóstico de gargalos

> Onde o funil perde mais hoje: prospecção, abordagem, reunião, proposta ou follow-up?
> O que o BDR mais reclama que falta para vender mais?
> Existe diferença de performance entre os 2 BDRs? O que explica?

---

### ETAPA 4 — Documentação

Com base nas respostas, produza:

1. `WS4_PROCESSO_VENDAS_BDR_V1.md` com:
   - Funil de vendas Órulo (etapas, responsáveis, duração esperada)
   - Métricas-alvo por etapa
   - Scripts básicos (abordagem + qualificação)
   - Objeções comuns + respostas sugeridas
   - Checklist de handoff para CS

2. Atualize o Charter do WS4 com referência a este documento

---

## SAÍDA ESPERADA

- `WS4_PROCESSO_VENDAS_BDR_V1.md` — processo documentado
- Diagnóstico dos principais gargalos do funil atual
- Métricas de linha de base para acompanhar melhoria

**Decisão obrigatória no final:**
Qual é a etapa do funil com maior oportunidade de melhoria nos próximos 30 dias?

---

*Prompt criado em 26/03/2026 — Urgência: BAIXA — WS4 — DRI: Gustavo Torres*
