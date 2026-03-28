# ⚠️ PRIORITÁRIO — P7: REVISÃO DA CADÊNCIA OPERACIONAL

**Versão:** 1.0
**Data de criação:** 26/03/2026
**Status:** PRONTO PARA RODAR
**Urgência:** ALTA — cadência muito pouco executada; rituais aspiracionais precisam ser ajustados para realidade

---

## CONTEXTO

A CADENCIA_OPERACIONAL define 4 ritmos oficiais (quinzenal, mensal, trimestral, eventual).

O diagnóstico atual é que **muito pouco está sendo executado de fato**.

Este prompt existe para transformar a cadência aspiracional em uma cadência aderente — baseada no que **realmente acontece** hoje e no que é **factível** dado o estágio do time.

---

## INSTRUÇÃO PARA A IA

Você está atuando como Sistema Integrado de Gestão de OKRs e Inteligência Documental da Órulo.

Leia o arquivo `CADENCIA_OPERACIONAL.md` antes de iniciar.

Seu objetivo é conduzir uma **revisão cirúrgica da cadência**, perguntando ao Diego ritual por ritual, e propor uma versão recalibrada que reflita a realidade de execução atual.

---

## ROTEIRO DE EXECUÇÃO

### ETAPA 1 — Diagnóstico de aderência

Pergunte ao Diego, ritual por ritual:

**Ritmo quinzenal — Pulse por workstream**

> Este rito acontece de verdade? Com qual frequência real?
> Quem participa? Tem registro posterior?
> Se não acontece: por quê? Falta de tempo, clareza, ferramenta ou hábito?

**Ritmo mensal — Revisão executiva**

> A revisão mensal com leitura consolidada de workstreams acontece?
> Existe saída formal (report, decisão, direcionamento) ou é conversa?

**Ritmo trimestral — Revisão de portfólio**

> Aconteceu alguma vez? Está agendada?

**Ritmo eventual — Readout D+14**

> Para WS3: existe readout 14 dias após cada evento/ação territorial?
> O aprendizado do evento está sendo registrado em algum lugar?

---

### ETAPA 2 — Mapeamento de realidade vs aspiração

Com base nas respostas, classifique cada ritual em uma das categorias:

| Ritual | Status real |
|---|---|
| Pulse quinzenal por WS | Acontece / Acontece parcialmente / Não acontece |
| Revisão mensal executiva | Acontece / Acontece parcialmente / Não acontece |
| Revisão trimestral portfólio | Acontece / Acontece parcialmente / Não acontece |
| Readout D+14 (WS3) | Acontece / Acontece parcialmente / Não acontece |

---

### ETAPA 3 — Proposta de cadência recalibrada

Com base no diagnóstico, proponha:

1. **Quais rituais manter** como estão (porque já acontecem ou são factíveis)
2. **Quais rituais simplificar** (reduzir frequência, duração ou complexidade do registro)
3. **Quais rituais pausar** temporariamente até o sistema ter mais maturidade
4. **Quais rituais criar do zero** que não existem mas fazem falta (ex: check-in rápido semanal, flash report por WS)

**Critério de decisão:**
- Ritual só deve constar na cadência se alguém vai de fato executá-lo
- Cadência aspiracional sem execução é ruído

---

### ETAPA 4 — Atualização da CADENCIA_OPERACIONAL

Após validação com Diego:

1. Reescreva os rituais da CADENCIA_OPERACIONAL com:
   - nome do ritual
   - frequência real
   - participantes
   - duração máxima
   - o que deve ser revisado
   - registro obrigatório mínimo (1 linha, não relatório)

2. Adicione uma seção **"RITUAIS PAUSADOS"** com os ritos que existem no papel mas não na prática, com justificativa e critério de reativação

3. Salve versão atualizada como `CADENCIA_OPERACIONAL_V2.md`

---

### ETAPA 5 — Registro

Registre na aba `RITUAIS` do `WS_OPERATING_SYSTEM_H1_2026.xlsx`:

- Nome de cada ritual recalibrado
- Frequência
- DRI
- Status (ativo / pausado)
- Próxima ocorrência prevista

---

## SAÍDA ESPERADA

- `CADENCIA_OPERACIONAL_V2.md` — versão recalibrada e aderente à realidade
- Aba `RITUAIS` atualizada na planilha
- Decisão clara: quais rituais sobrevivem, quais são pausados, quais são criados

**Decisão obrigatória no final:**
Qual é o único ritual que, se executado com consistência nas próximas 4 semanas, teria mais impacto no sistema?

---

*Prompt criado em 26/03/2026 — Urgência: ALTA*
