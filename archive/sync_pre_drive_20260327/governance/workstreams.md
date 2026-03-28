# governance/workstreams.md — Portfólio de Workstreams (WS1–WS7) — H1/2026

> **Última atualização:** 2026-03-08
> **Autor:** Diego Diehl
> **Status:** v1.0 — Fonte de verdade

---

## 1. Objetivo

Este documento define como os 7 workstreams da Órulo serão governados em H1/2026.

Objetivos do sistema:
- garantir cadência mínima de avanço em todos os WS
- definir donos claros (DRI), sponsor e participantes
- padronizar método de acompanhamento
- transformar erro em aprendizado e ajuste
- evitar dispersão e comitês implícitos
- preparar kickoffs oficiais com método e outputs consistentes

**Sponsor de todos os WS: Diego Diehl**

---

## 2. Princípios do portfólio

1. Cada WS existe para resolver um problema relevante do negócio.
2. Cada WS precisa ter um dono claro.
3. Cada WS precisa ter touch a cada 14 dias.
4. Cada WS precisa produzir evidência mínima por ciclo.
5. Erro é aceitável; erro sem aprendizado não é.
6. H1/2026 é fase de instalação de método e ritual — não de sofisticação excessiva.

---

## 3. Definições

### DRI
Directly Responsible Individual. É a pessoa diretamente responsável por garantir que o WS avance, rode o ritual, produza artefatos e traga evidências.

### Sponsor
É quem garante prioridade, remove bloqueios, arbitra trade-offs e cobra cadência. Neste portfólio, o sponsor de todos os WS é Diego.

### Touch
Touch válido é o mais recente entre:
1. reunião ao vivo com output registrado
2. artefato robusto publicado (WS Pulse com evidência)

### Days Since Touch
Quantidade de dias desde o último touch válido.

### Artefato robusto
Documento curto, objetivo e publicável, que mostre:
- avanço
- bloqueio
- próximos passos
- evidência
- pedido de decisão, se houver

---

## 4. Indicador-âncora

### Days Since Touch

Indicador principal transversal do portfólio em H1.

**Regra:** cada WS deve ter Days Since Touch <= 14 dias

Campos que cada WS deve manter:
- `last_live_touch`
- `last_pulse`
- `days_since_touch`
- `next_touch_due`

---

## 5. Definition of Ready para Kickoff de um WS

Um WS só entra em kickoff oficial quando tiver, no mínimo:
- DRI definido
- sponsor definido
- participantes fixos definidos
- objetivo do WS em 1–2 linhas
- "feito é" definido
- escopo entra / não entra definido
- draft inicial de C1/C2/C3
- evidência mínima do ciclo definida
- proposta de data do próximo touch

Sem isso, o kickoff vira alinhamento genérico e não contrato de execução.

---

## 6. Contrato do DRI

O DRI de cada WS é responsável por:
- garantir touch a cada 14 dias
- preparar e publicar o WS Pulse no ciclo
- manter backlog top 10 vivo
- trazer bloqueios com clareza
- registrar pelo menos 1 evidência por ciclo
- registrar 1 erro/aprendizado + 1 ajuste aplicado
- pedir ajuda ao sponsor antes de perder cadência

O DRI não precisa executar tudo, mas precisa garantir que o WS exista na prática.

---

## 7. Direitos de decisão

### DRI decide:
- organização do trabalho
- rotina operacional do ciclo
- priorização fina dentro do escopo do WS
- formato das evidências, desde que respeite o padrão mínimo

### Sponsor decide:
- prioridade relativa entre WS
- trade-offs e conflitos entre times
- desbloqueios estratégicos
- mudança de escopo
- temas que exigem patrocínio executivo

### Participantes contribuem:
- com execução
- com informação
- com validação pontual

**Regra:** evitar aprovação coletiva implícita.

---

## 8. Política de erro, aprendizado e ajuste

Erro é permitido quando:
- é rapidamente reportado
- gera aprendizado claro
- gera ajuste concreto no método, rotina ou play

Todo WS Pulse deve conter:
- Erro/Aprendizado
- Ajuste aplicado

Erro repetido sem aprendizado vira item de governança e entra no backlog com prioridade alta.

---

## 9. Artefatos obrigatórios por WS

Cada WS deve ter:
1. `charter.md`
2. `plan_quinzenal.md`
3. `backlog.md`
4. `pulses/`

### 9.1. Charter
Documento fixo do WS:
- por que existe
- objetivo H1
- "feito é"
- entra / não entra
- DRI / sponsor / participantes
- evidência mínima
- riscos

### 9.2. Plano Quinzenal
Contrato do ciclo:
- C1
- C2
- C3
- dono
- prazo
- evidência
- bloqueio/pedido ao sponsor

### 9.3. Backlog
Top 10 contínuo:
- prioridades
- próximos ciclos
- itens de método
- itens bloqueados

### 9.4. Pulse
1 página:
- status do ciclo anterior
- gargalo #1
- pedido ao sponsor
- próximos passos
- evidência
- erro/aprendizado
- ajuste aplicado

---

## 10. Cadência

Tudo começa quinzenal.

### Bloco A — Quinzenal
- WS1 — Comunicação com Corretores
- WS3 — Fórmula de Lançamento / Workshops / Praças
- WS5 — Marketing e Conteúdo
- WS6 — Embaixadoras + apoio CS

### Bloco B — Quinzenal
- WS2 — Jornada CX DL→Pago
- WS4 — Estrutura Comercial & CRM
- WS7 — Produtos Financeiros e Parcerias Estratégicas

### Regra
Se não houver reunião ao vivo no ciclo, o DRI precisa "pagar a cadência" com:
- Pulse robusto
- evidência
- backlog atualizado
- próximo touch agendado

---

## 11. Dependências entre WS

Os WS não são independentes. Dependências relevantes:
- WS1 pode depender de insumos de WS5
- WS3 conversa com WS1, WS4 e WS5
- WS6 pode depender de WS5 e do contexto comercial
- WS7 pode depender de WS3/WS4 para origem e priorização de oportunidades

**Regra:** dependência bloqueante deve aparecer explicitamente no Pulse como "bloqueio externo".

---

## 12. Kickoff (Sprint 0) — padrão

O kickoff de um WS existe para fechar método e primeira quinzena.

### Pré-work do DRI (24h antes)
- objetivo do WS em 1–2 linhas
- "feito é"
- entra / não entra
- proposta inicial de C1/C2/C3
- evidência mínima do ciclo
- principais bloqueios percebidos

### Agenda do kickoff (30 min)
1. confirmar escopo e "feito é"
2. confirmar método do WS
3. fechar C1/C2/C3 da primeira quinzena
4. definir evidência
5. definir data do próximo touch

### Output obrigatório
- Charter v1.0 publicado
- Plano Quinzenal Sprint 01 publicado
- Backlog inicial criado
- `last_live_touch` atualizado
- próximo touch agendado

---

## 13. Ordem de implantação

### Fase 1
Fechar método do portfólio.

### Fase 2
Deixar os 7 WS prontos para kickoff.

### Fase 3
Rodar kickoffs por bloco.

### Fase 4
Rodar pulses quinzenais e backlog contínuo.

### Fase 5
Automatizar alertas e cadência no OpenClaw.

---

## 14. Mapa dos Workstreams

### WS1 — Comunicação com Corretores
- **Sponsor:** Diego
- **DRI:** Mayumi
- **Executor com autonomia:** Ester
- **Bloco:** A
- **Feito é:** 1 comunicação relevante por quinzena com evidência

### WS2 — Jornada CX: DL → Pago
- **Sponsor:** Diego
- **DRI:** Gustavo (Gustavo Rodrigues Torres)
- **Bloco:** B
- **Feito é:** lista de DLs com próximo passo, data e evidência de valor entregue por ciclo

### WS3 — Fórmula de Lançamento / Workshops / Praças
- **Sponsor:** Diego
- **DRI:** Mayumi + sócios locais
- **Bloco:** A
- **Feito é:** sprint territorial quinzenal rodando com one-pager e evidência

### WS4 — Estrutura Comercial & CRM
- **Sponsor:** Diego
- **DRI:** Gustavo (Gustavo Rodrigues Torres)
- **Bloco:** B
- **Feito é:** deals do funil ativo com próximo passo e data no CRM, com evidência quinzenal

### WS5 — Marketing e Conteúdo
- **Sponsor:** Diego
- **DRI:** Mayumi
- **Bloco:** A
- **Feito é:** pauta quinzenal + pelo menos 1 publicação com evidência

### WS6 — Embaixadoras + apoio CS
- **Sponsor:** Diego
- **DRI:** Mayumi
- **Apoio:** CS
- **Bloco:** A
- **Feito é:** programa rodando com evidência mínima por ciclo

### WS7 — Produtos Financeiros e Parcerias Estratégicas
- **Sponsor:** Diego
- **DRI:** Eduardo + Felipe
- **Bloco:** B
- **Feito é:** status do funil por produto + next action por ciclo
