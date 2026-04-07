# DECISÕES ESTRATÉGICAS — H1 2026

*Atualizado: 20/03/2026*

---

## Formato Mobile — Regra Absoluta (17/03/2026)

**Decisão:** Nenhuma tabela Markdown (`| col |`) em qualquer output via Telegram. Canal principal de Diego é mobile.

**Regra:** Usar formato Card (emoji + bullets) em toda entrega — manual, cron, overnight, briefing. Sem exceção.

**Onde foi gravado:** SOUL.md (seção ⚠️ FORMATO MOBILE), AGENTS.md (seção 8), 8 prompts de cron atualizados.

---

## Participantes dos Workstreams (17/03/2026)

**Decisão:** Registro oficial de participantes por WS (além dos DRIs).

- WS1 — DRI: Mayumi | Participante: Ester
- WS2 — DRI: Gustavo Torres | Participantes: a definir
- WS3 — DRI: Eduardo (a confirmar) | Participantes: Gustavo Torres, Zanella, Pedro Kneip
- WS4 — DRI: Gustavo Torres | Participante: Zanella
- WS5 — DRI: Mayumi | Participantes: a definir
- WS6 — DRI: Diego (provisório) | Participante: Jade
- WS7 — DRI: Diego (provisório) | Participantes: a definir

**Onde foi gravado:** governance/workstream_index.md, AGENTS.md (tabela time), SOUL.md (participantes por WS), Drive: MAPA_DE_RESPONSAVEIS_V1.1

---

## MAPA_DE_RESPONSAVEIS atualizado no Drive (17/03/2026)

**Decisão:** Criar V1.1 com participantes registrados. Arquivar V1 em 07_ARQUIVO.

- **V1.1 (ativo):** ID `1X3EgdU0gf5uoGfgkzOYkpnWEsEnYxQU7ocuemvPq-u0`
- **V1 (arquivado):** movido para 07_ARQUIVO
- **Pasta:** 04_PESSOAS_E_RESPONSAVEIS (ID: `1ZF1SZjAipyEJkFfv2Qu5IbppLVjPtzUz`)

---

## Sprint Reminder — One-Pager enviado via gog-larissa (19/03/2026)

**Decisão:** Diego autorizou envio dos dois e-mails de lembrete de One-Pager de sprint.

- Zanella (Curitiba): enviado 09:33 BRT | msg_id `19d07a146ed5d37b`
- Kneip (Vitória): enviado 09:33 BRT | msg_id `19d07a15bb9ee5c8`
- CC: gustavo.torres@orulo.com.br em ambos

---

---

## Arquitetura de Canais e Agentes — v2 (03/04/2026)

**Decisão:** Reorganização completa dos 3 bots com modelos e papéis definitivos.

| Bot | Username | Agent | Modelo Primary | Fallbacks | Papel |
|-----|----------|-------|---------------|-----------|-------|
| @Base_DD_bot | morfeu | MiniMax M2.7 | Sonnet → Opus | Estratégico + Órulo + Pessoal |
| @larissa_personal_assistant_bot | larissa | MiniMax M2.7 | M2.5 | Rotinas, agenda, crons, e-mails |
| @Claudinei_Master_Bot | claudinei | Claude Haiku | Sonnet → M2.7 | Técnico: scripts, VPS, infra, deploys |

**Grupo Central Diego Diehl:**
• Chat ID: `-1003883137889`
• 8 tópicos criados (topics 9–16)
• topics 9-13 → Morfeu | topics 14-15 → Larissa | topic 16 → Claudinei
• threadBindings: pendente de configuração

**Regra operacional:** Claudinei não é mais exclusivo de config OpenClaw — opera como técnico geral com Haiku (tarefas simples) e Sonnet (análise complexa). MiniMax como fallback em todos.

---

## Portfólio H1 — Workstreams Consolidados

### Versão Final do Portfólio

Sete Workstreams (WS) organizados em dois Blocos operacionais:

| Bloco | Workstreams | DRI Principal |
|-------|-------------|---------------|
| **Bloco A** | WS1, WS3, WS5, WS6 | Mayumi |
| **Bloco B** | WS2, WS4, WS7 | Gustavo (WS2/WS4), Eduardo+Felipe (WS7) |

### Nome e Função Final de Cada WS

| WS | Nome | Função | DRI |
|----|------|--------|-----|
| WS1 | Comunicação com Corretores | Comunicação estruturada + ativação via Z2A | Mayumi |
| WS2 | Jornada CX: DL → Pago | Trilha mínima + cadências + valor entregue | Gustavo |
| WS3 | Fórmula de Lançamento / Praças | Sprint quinzenal + One-Pager + Score simplificado | ~~Mayumi~~ → **Eduardo** *(decisão 08/03)* |
| WS4 | Estrutura Comercial & CRM | Hygiene + handoff + cadências SDR | Gustavo |
| WS5 | Marketing e Conteúdo | Eventos → ativos → narrativa | Mayumi |
| WS6 | Incorporadoras Embaixadoras | Drive-free como meta | Mayumi |
| WS7 | Remuneração Sócio-Local | Modelo econômico por praça | ~~Eduardo + Felipe~~ → **Diego Diehl** *(decisão 08/03)* |

---

## Harmonização Final — Conflitos Resolvidos

### Conflitos Identificados
- **Nenhum conflito estrutural de escopo** encontrado entre os WS.
- **Atenção:** WS3 e WS6 usam "praça" como unidade de gestão — coordenação necessária via Mayumi (DRI de ambos).

### Ajustes Recomendados
- WS1: Validar canal principal (WhatsApp) no kickoff.
- WS2: Definir momento exato de handoff Closer (João Vitor).
- WS6: Clarificar coordenação com WS3.
- WS7: Aprovar arquitetura com Eduardo+Felipe no kickoff.

### Dependências Críticas
- WS2 depende de WS4 (CRM saudável).
- WS1 depende de WS5 (conteúdo) e WS3 (coordenação).
- WS5 depende de WS3 (eventos/workshops).

---

## Prontidão para Kickoffs

| WS | Prontidão |
|----|------------|
| WS1 | A- |
| WS2 | A- |
| WS3 | A |
| WS4 | A- |
| WS5 | A- |
| WS6 | A- |
| WS7 | A- |

> **Legenda:** A = Pronto. A- = Pronto com atenção. B = Ajustar antes.

---

## Ordem Sugerida dos Kickoffs

1. WS3 (base territorial)
2. WS4 (infraestrutura)
3. WS2 (jornada DL)
4. WS1 (comunicação)
5. WS5 (marketing)
6. WS6 (embaixadoras)
7. WS7 (remuneração)

---

## Pontos de Atenção para Kickoffs

1. **Sobrecarga Mayumi:** 4 WS simultâneos no Bloco A. Risco aceito, monitorar via pulses.
2. **Dependência WS2→WS4:** WS4 precisa entregar hygiene mínima para WS2 ter visibilidade.
3. **WS7:** Depende de aprovação de Eduardo+Felipe. Garantir alinhamento no kickoff.

---

## Próximos Marcos

- **Kickoffs:** Executar na ordem sugerida.
- **Revisão:** Pós-Sprint 02 (D+30).
- **Responsável atualização:** Morfeu.

---

---

## Revisões de DRI — Pós-Auditoria (09/03/2026)

| WS | DRI original | DRI atual | Data decisão | Fonte |
|----|-------------|-----------|--------------|-------|
| WS3 FL | Mayumi | **Eduardo** | 08/03/2026 | Diego (sessão de curadoria) |
| WS7 SL | Eduardo + Felipe | **Diego Diehl** | 08/03/2026 | Diego (sessão de curadoria) |

⚠️ **Status de atualização de charters:**
- WS3 charter: ainda registra Mayumi como DRI → **DIVERGENTE** (precisa de atualização)
- WS7 charter: ainda registra Eduardo+Felipe como DRI → **DIVERGENTE** (precisa de atualização)

---

## Achados Estratégicos — Semanal Comercial 09/03/2026

- **Z2 contribui 32,8% do MRR** — dado de receita confirmado em reunião
- **CRI = oportunidade de crescimento acelerado** — nova lei tributária de dezembro/2025 abre mercado (incorporadoras buscam isenção tributária para altas rendas)
- **Estratégia de abordagem por região:** Sul requer estratégia diferente do Nordeste para ligações
- **Eventos como motor de pipeline:** Paraná lidera BDR agendamentos — padrão causal entre calendário de eventos e resultado comercial confirmado

*Decisões registradas por Morfeu em 09/03/2026.*

---

## Estabilização do Sistema de Rotinas (16/03/2026)

**Decisão:** Pausar rotinas instáveis por 60 dias e reduzir escopo do Overnight.

| Rotina | Decisão | Prazo de revisão |
|--------|---------|-----------------|
| Daily Briefing | 🔴 Desligado | ~16/05/2026 |
| Scan Praças Weekly | 🔴 Desligado | ~16/05/2026 |
| Overnight Thinking Mode | 🟡 Reduzido (versão light) | ~16/05/2026 |

**Motivo:** Rotinas gerando ruído por falta de fonte de dados confiável (pending.md inconsistente, C1/C2/C3 não fluindo). Melhor sem do que com qualidade ruim.

**Condições de reativação:**
- Daily Briefing: pending.md consistente + Briefing Dominical gerando output útil por 2 semanas.
- Scan Praças Weekly: ciclo C1/C2/C3 fluindo + projects_orulo.md atualizado automaticamente a cada sprint.

**Revisão profunda agendada:** 16/04/2026 às 12h (cron ativo).

---

## LLM Policy v2.1 — Fases 1 a 4 Concluídas (16/03/2026)

**Status:** Fases 1, 2, 3 e 4 completas.

| Fase | O que foi feito | Data |
|------|----------------|------|
| Fase 1 | 7 jobs duplicados desativados | 06/03 |
| Fase 2 | 10 correções de metadata | 06/03 |
| Fase 3 | 3 novos jobs P2 + constraint checks | ~09/03 |
| Fase 4 | Harvesters decisions+lessons + double-pass Revisão Semanal + 3 scripts P3 | 16/03 |

**Novos componentes da Fase 4:**
- 🧠 Harvester decisions.md — Dom 22h (job `65cf1970`)
- 📚 Harvester lessons.md — Dom 22h30 (job `08f2a618`)
- ⚡ Double-pass na Revisão Semanal — ativo quando remains ≥ 65
- Scripts P3: `job_lockfile.sh`, `endpoint_health.py`, `quota_estimator.py`
- Quota estimada em execução: 93/100 (API OK em 16/03 22h30)

**Fase 5 (calibração):** aguarda dados reais de ~27/03.

---

## C1/C2/C3 Sprint 02 — Curitiba (Zanella) — 18/03–01/04/2026

**Definidos em:** 16/03/2026 por Diego.

- **C1 (Meta):** Fechar 4 vendas em 7 dias / 10 vendas em 30 dias / 20 vendas em 60 dias — originadas do evento de 18/03.
- **C2 (Ação Volumosa):** Executar o evento presencial com CTA final e comunicar em escala com todos os inscritos (presentes e ausentes), com follow-up pós-evento.
- **C3 (Ação Estrutural):** Registrar todos os contatos do evento no CRM com controle de follow-up estruturado.

---

## C1/C2/C3 Sprint 02 — Vitória (Kneip) — 18/03–01/04/2026

**Confirmados em:** 16/03/2026 via One-Pager de Kneip.

- **C1 (Meta):** Fechar Canal, Empar e +1 novo cliente.
- **C2 (Ação Volumosa):** Prospecção ativa de 10+ novos leads.
- **C3 (Ação Estrutural):** Organizar o avanço dos onboardings para manter ritmo compatível entre comercial e implantação (apoio CS solicitado à Matriz).

---

## Sistema Operacional Comercial Órulo — Consolidação Estrutural (11/03/2026)

### Decisão: Arquitetura oficial do sistema definida e gravada

- **Data:** 11/03/2026
- **Contexto:** Dia inteiro de estruturação do Sistema Operacional Comercial da Órulo
- **Decisões fechadas:**
  1. Pasta raiz oficial: `1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM` — única autorizada para operações
  2. Planilha `WS_OPERATING_SYSTEM_H1_2026` (ID: `1n9CUO8U6h6MUKCmKszXMtU_veAmSCo-q`) em `01_GOVERNANCA_GERAL` = cockpit oficial
  3. Backlog inicial de 70 itens (Sprint 0+1, todos os 7 WS) = base oficial
  4. Estrutura oficial do BACKLOG_GERAL: 12 colunas com Frente e Evidência esperada obrigatórias
  5. Morfeu opera como auditor leve + copiloto executivo — sem correção automática
  6. Hierarquia: Drive > Planilha > OpenClaw — imutável
  7. Pastas 98_BASES_DIEGO e 99_BACKUP = auxiliares, não oficiais
  8. Todos os arquivos WSX_REUNIOES e WSX_NOTAS = Google Docs (não markdown)
  9. MAPA_DE_RESPONSAVEIS_V1 = árbitro oficial de DRI em caso de conflito
  10. DRI oficial: WS1=Mayumi, WS2=Gustavo Torres, WS3=Eduardo(a confirmar), WS4=Gustavo Torres, WS5=Mayumi, WS6=Diego(provisório), WS7=Diego(provisório)
- **Não reabrir sem instrução explícita de Diego**


---

## Curadoria SUPER CÉREBRO V2 (27/03/2026)

**Decisão:** Absorver orientações do curso SUPER CÉREBRO V2 no sistema Morfeu. Estrutura de 3 pastas do Drive oficializada. Modo Cowork + Chat ativado.

**Modificações aplicadas:**
- `memory/kr_status.md` criado (KR1-KR7 + gaps)
- `memory/orulo_sistema_operacional.md` criado (arquitetura consolidada)
- `memory/pending.md` atualizado (P0s identificados + P7-P11 não executados)
- `memory/projects_orulo.md` atualizado (Sprint 02 sem update — 9 dias)
- Biblioteca orulo instalada: `biblioteca/orulo/00_SUMARIO_ESTRATEGICO.md` + `PLANO_DE_ACAO_E_DECISOES.md`
- Prds instalados: `prds/security-hardening.md`, `prds/memory-architecture.md`, `prds/integrations-setup.md`

**Gap crítico identificado:**
- P0s do plano de curadoria (26/03): nenhum executado
- KR7: MRR total desconhecido
- KR5/KR6: sem instrumento de medição
- Sprint 02 (9 dias sem update documentado)

**Ação:** Diego precisa endereçar P0s. Sem dado consolidado, KR7 não tem diagnóstico.

---

## KR4 — NÃO EXISTE (27/03/2026)

**Decisão:** KR4 não existe no sistema. Pular de KR3 para KR5. Confirmado pelo plano de curadoria V2.

**Regra:** Não criar KR fantasma. Aguardar instrução de Diego se quiser defini-lo.
- [Usar linguagem específica do setor do cliente (ex: 'vidas' em vez de 'funcionários' para planos de saúde)] @(Diego Diehl) — [6690232be5ccd900129d3e25](/2024-07) [confirmed]
- [Trabalhar o viés da familiaridade criando rapport antes de apresentar solução] @(Diego Diehl) — [6690232be5ccd900129d3e25](/2024-07) [confirmed]
- [Usar técnica de loss aversion (medo de perder oportunidade) para cualificar interés do cliente] @(Diego Diehl) — [6690232be5ccd900129d3e25](/2024-07) [confirmed]
- [Fazer amizade com a secretária como parte do processo de compra] @(Diego Diehl) — [6690232be5ccd900129d3e25](/2024-07) [confirmed]
- [Vendedor deve fazer o cliente trabalhar para ele (entregar valor antes de fechar)] @(Diego Diehl) — [6690232be5ccd900129d3e25](/2024-07) [confirmed]
