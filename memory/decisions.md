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
- [Implementação Z2A na H Station com prazo de 7-10 dias úteis] @(Carlos Stoppa + H Station) — [6745b87129016500130d9262](/2024-11) [confirmed]
- [Treinamento em 2 dias após implementação] @(Carlos Stoppa + H Station) — [6745b87129016500130d9262](/2024-11) [confirmed]
- [H Station preencher planilha com usuários, hierarquia, dados cadastrais e telefone obrigatório] @(H Station (Carol + equipe)) — [6745b87129016500130d9262](/2024-11) [confirmed]
- [Campos dinâmicos de qualificação do corretor/parceiro definidos pela H Station] @(H Station) — [6745b87129016500130d9262](/2024-11) [confirmed]
- [Carol exportar lista de parceiros do WhatsApp para importação no sistema] @(Carol (H Station)) — [6745b87129016500130d9262](/2024-11) [confirmed]
- [Cadastrar telefones de Bruno e Sara como contatos do projeto] @(H Station) — [6745b87129016500130d9262](/2024-11) [confirmed]
- [Conectar WhatsApp, marcar treinamento e validar ferramenta] @(Carlos Stoppa + H Station) — [6745b87129016500130d9262](/2024-11) [confirmed]
- [Criar grupo WhatsApp para comunicação e alinhamento de próximos passos] @(Carlos Stoppa) — [6745b87129016500130d9262](/2024-11) [confirmed]
- [Criar e compartilhar video com prompt personalizado de ChatGPT para uso interno no time — focado em neutralidade e objetividade] @(Diego Diehl) — [688155a73ead900013f0436f](/2025-07) [confirmed]
- [Usar mesma configuração de ChatGPT para trabalho, incluindo histórico de trajetória pessoal no prompt] @(Diego Diehl) — [688155a73ead900013f0436f](/2025-07) [confirmed]
- [Criar área de parcerias dentro do Z2A para ampliar alcance e escala de comunicação com corretores] @(Diego Diehl) — [68c091be0972b500130a0529](/2025-09) [confirmed]
- [Desenvolver material de marketing pronto (cards, sugerido) para corretores usarem em suas divulgações] @(Diego Diehl) — [68c091be0972b500130a0529](/2025-09) [confirmed]
- [Implementar follow-up telefônico mais próximo com corretores que já geraram visita ou demostraram interesse (cauda longa)] @(Diego Diehl) — [68c091be0972b500130a0529](/2025-09) [likely]
- [Agendar apresentação do Troca Fácil em Google Meet para sanar dúvidas da equipe] @(Diego Diehl) — [68c091be0972b500130a0529](/2025-09) [confirmed]
- [Piloto Z2 com Lúcio (Faria Lima) approved pela diretoria — 30 dias de implementação, resultado positivo] @(Lúcio (cliente)) — [68d52426dd73370013fde50a](/2025-09) [confirmed]
- [Eduardo envia lista de 3 empreendimentos com grupos de concorrentes para Wallace — rodar teste de ativação metrificado] @(Eduardo Stringhini) — [68d52426dd73370013fde50a](/2025-09) [confirmed]
- [Transição para método de meta com custo por mensagem — novo modelo de precificação] @(Diego Diehl + Junior) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [Qualificação separada para Z2 e Órulo — diferentes perfis de acesso para cada produto] @(Eduardo Stringhini) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [Sigilo nas qualificações de corretores entre incorporadoras — dado competitivo não pode ser compartilhado] @(Eduardo Stringhini) — [68d52426dd73370013fde50a](/2025-09) [confirmed]
- [Desenvolver sistema de classificação de incorporadores em níveis de verificação (1, 2, 3)] @(Equipo técnica) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [Criar interface simples para consulta rápida de zona e status do corretor] @(Equipo técnica) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [Eduardo agenda reunião específica com Alejandro sobre score prototype] @(Eduardo Stringhini) — [68d52426dd73370013fde50a](/2025-09) [confirmed]
- [Habilitar monitoramento Z2 via plataforma Ouro para consolidar bases de dados] @(Alejandro Olchik) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [Separar na plataforma Z2 dados de eventos internos vs. dados de busca do mercado] @(Equipo técnica) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [Expansão Campinas — Diego propõe explorar mercado local (maior potencial que praça atual)] @(Diego Diehl) — [68d52426dd73370013fde50a](/2025-09) [confirmed]
- [Diego + Junior planejam podcast juntos] @(Diego Diehl + Junior) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [Estratégia de eventos + dinâmicas de premiação para corretores — fidelização] @(Junior Silva) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [Login unificado com potencial de antecipação de comissões para corretores] @(Alejandro Olchik) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [Incluir monitoramento de gestores no relatório mensal] @(Alejandro Olchik) — [68d52426dd73370013fde50a](/2025-09) [likely]
- [João assume formalmente como líder da célula de expansão de praças — ponte entre operação comercial e sócios locais] @(Diego Diehl + João Vitor) — [68efb4bd79b4280013204146](/2025-10) [confirmed]
- [Investimento de R$ 300 mil em Balneário Camboriú — evento de expansão com time todo (início de 2027)] @(Diego Diehl) — [68efb4bd79b4280013204146](/2025-10) [likely]
- [Diego aprova contratação de 2 S10s com Gustavo para apoiar expansão] @(Diego Diehl) — [68efb4bd79b4280013204146](/2025-10) [confirmed]
- [Métricas principais de expansão: (1) corretores ativos, (2) integrações concluídas, (3) faturamento por praça] @(Diego Diehl) — [68efb4bd79b4280013204146](/2025-10) [confirmed]
- [Praças prioritárias de expansão: João Pessoa, Goiânia, Campinas, Rio de Janeiro, Recife] @(Diego Diehl) — [68efb4bd79b4280013204146](/2025-10) [confirmed]
- [Modelo de gamificação: pontos por cadastro de novo corretor, resgatáveis em descontos ou ativações digitais] @(João Vitor + Diego) — [68efb4bd79b4280013204146](/2025-10) [confirmed]
- [João recebe autonomia para flexibilizar propostas comerciais em novas praças] @(Diego Diehl) — [68efb4bd79b4280013204146](/2025-10) [confirmed]
- [Foco de expansão de Diego: incorporadora em São Paulo (não presença pessoal)] @(Diego Diehl) — [68efb4bd79b4280013204146](/2025-10) [confirmed]
- [SDR inicia contato com corretores e usuários — modelo Buster (conversa em Volume para identificar incorporadora)] @(Diego Diehl) — [68efb4bd79b4280013204146](/2025-10) [likely]
- [Estruturar modelo variável de remuneração de João baseado em resultados de expansão] @(Diego Diehl) — [68efb4bd79b4280013204146](/2025-10) [likely]
- [Usar noticiários de Lula (amanhã) como gancho para follow-up em massa com contatos] @(Diego Diehl) — [6911e83237437f0013102674](/2025-11) [confirmed]
- [Desenvolver Iara (IA) treinada em CRI para responder dúvidas frequentes da equipe — redução de dependência de Diego] @(Diego Diehl) — [6911e83237437f0013102674](/2025-11) [confirmed]
- [Equipe NÃO usar a palavra 'CRI' ao se comunicar com incorporadores — usar nomenclatura mais atrativa (ex: 'recebíveis', 'solução de fundir')] @(Diego Diehl) — [6911e83237437f0013102674](/2025-11) [confirmed]
- [Gustavo registrar todas as incorporadoras no CRM para evitar conflitos de venda entre membros do time] @(Diego Diehl) — [6911e83237437f0013102674](/2025-11) [confirmed]
- [Time comercial regionalizado: Curitiba foca no Paraná, Vitória lidera Espírito Santo + contactos em outras regiões] @(Diego Diehl) — [6911e83237437f0013102674](/2025-11) [confirmed]
- [Criar grupo interno do time para absorver conteúdo de CRI, tirar dúvidas e aprender coletivamente] @(Diego Diehl) — [6911e83237437f0013102674](/2025-11) [confirmed]
- [Transformar próximo evento presencial em webinar para incorporadoras — ajustar convites] @(Diego Diehl) — [6911e83237437f0013102674](/2025-11) [confirmed]
- [Remover opção de visualizar lista de convidados nas reuniões — simplificação operacional] @(Diego Diehl) — [6911e83237437f0013102674](/2025-11) [confirmed]
- [Discussão de temas sensíveis deve ocorrer previamente em particular, não em reunião aberta] @(Diego Diehl) — [6911e83237437f0013102674](/2025-11) [confirmed]
- [Diego centralizará demandas comerciais e redistribuirá tarefas] @(Diego Diehl) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Diego contratar um ou dois closers para atender demanda de reuniões] @(Diego Diehl) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Diego conversar com João sobre potencial liderança e reposição de closer] @(Diego Diehl) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Diego substituir Melo e criar processos internos para melhorar desenvolvimento comercial] @(Diego Diehl) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Reunião de diretoria agendada para 26 a 29 de janeiro] @(Diego Diehl + diretoria) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Dois encontros presenciais de duas horas cada — reunião dia 19 das 16 às 18h] @(Diego Diehl + diretoria) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Meta 2026: R$8 milhões de receita com crescimento de 50%] @(Diego Diehl + diretoria) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Diego centralizar controle total de vendas no CRM] @(Diego Diehl) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Carolina preparar relatório consolidado de pronto atendimento de 2025] @(Carolina Campos) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Laís fará acompanhamento com contas de baixo retorno] @(Laís) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Diego propor parceria agnóstica com CV com negociação flexível] @(Diego Diehl) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Diego postar stories de contratos assinados para visibilidade no mercado] @(Diego Diehl) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Felipe criar grupo de trabalho nas associações de classe] @(Felipe Goettems) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Diego centralizar demandas comerciais que serão redistribuídas] @(Diego Diehl) — [695bfc1ee9b88d0013912e2b](/2026-01) [confirmed]
- [Piloto Embaixador em Goiânia com corretores mais ativos usando ferramenta] @(Diego Diehl) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [Ester fica responsável pela primeira rotina em Goiânia] @(Diego Diehl) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [João focar em Recife — Saraiva cadastrou 300+ corretores recentemente] @(João Vitor Portes da Silva) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [Gustavo propor reunião longer para traçar estratégia detalhada por praças] @(Gustavo Torres) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [Fazer mapa estratégico de Curitiba como modelo inicial] @(Diego Diehl) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [Ester e João se comunicam com corretores das praças-alvo] @(Ester + João Vitor Portes da Silva) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [João desbravando desafio estratégico de praças com pouca audiência] @(João Vitor Portes da Silva) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [Sprints planejados para eventos em Porto Alegre, Capão da Canoa e Vitória em abril] @(Diego Diehl) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [Webinar em janeiro com Filipe e João para divulgação] @(Diego Diehl) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [Testar estratégias antes de repassar para time júnior] @(Diego Diehl) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [Fazer mapa por praça: quem é quem, situação atual, crescimento] @(Gustavo Torres) — [695c285567410d0013fd37f1](/2026-01) [confirmed]
- [Treinamento comercial semanal às quartas-feiras às 9h estabelecido como prática padrão] @(Diego Diehl) — [695e4ac3e9b88d00139173a0](/2026-01) [confirmed]
- [Corretores devem divulgar link da Órula como fonte oficial de consulta para aumentar audiência] @(Diego Diehl) — [695e4ac3e9b88d00139173a0](/2026-01) [confirmed]
- [Integração e produtos para imobiliárias oferecidos gratuitamente por incorporadoras clientes] @(Diego Diehl) — [695e4ac3e9b88d00139173a0](/2026-01) [confirmed]
- [Plataforma atualiza mais de 70% dos dados imobiliários do Brasil com equipe de 40 pessoas] @(Diego Diehl) — [695e4ac3e9b88d00139173a0](/2026-01) [confirmed]
- [Mirla destaque: primeiro entender o problema do corretor antes de ajudar] @(Mirla Menezes + Diego Diehl) — [695e4ac3e9b88d00139173a0](/2026-01) [confirmed]
- [Treinar equipe para auxiliar corretores com dificuldades técnicas] @(Diego Diehl + Gustavo Torres) — [695e4ac3e9b88d00139173a0](/2026-01) [confirmed]
- [Incorporadoras pequenas podem se beneficiar de plataformas digitais para ganhar visibilidade] @(Diego Diehl) — [695e4ac3e9b88d00139173a0](/2026-01) [confirmed]
- [Diego será consultado sobre instabilidades do sistema e relatos de clientes] @(Diego Diehl) — [695f91a6828894001391e6e0](/2026-01) [confirmed]
- [Equipe em fase de validação de testes de volume para melhorar infraestrutura de mensageria do WhatsApp] @(Marcelo Tadeu) — [695f91a6828894001391e6e0](/2026-01) [confirmed]
- [Alinhar expectativa de tempo de resposta com clientes para integração gratuita (2 dias)] @(Diego Diehl) — [695f91a6828894001391e6e0](/2026-01) [confirmed]
- [Marcelão deverá levantar número de incidentes no Desk para análise] @(Marcelo Tadeu) — [695f91a6828894001391e6e0](/2026-01) [confirmed]
- [Modelo SP: focar em grandes lançamentos com contrato de 6-12 meses] @(Eduardo Stringhini) — [695f91a6828894001391e6e0](/2026-01) [likely]
- [Modelo híbrido: equipe interna em contas estratégicas + escalabilidade] @(Junior Silva) — [695f91a6828894001391e6e0](/2026-01) [confirmed]
- [Equipe é ferramenta para canal de parcerias — ganhando comissão com alinhamento estratégico] — [695f91a6828894001391e6e0](/2026-01) [confirmed]
- [Saída de Wallace requer realinhamento estratégico da equipe] @(Eduardo Stringhini) — [695f91a6828894001391e6e0](/2026-01) [confirmed]
- [Foco em expandir para capitais com empresas de receita transacional] @(Eduardo Stringhini) — [695f91a6828894001391e6e0](/2026-01) [confirmed]
- [Diego contratar um ou dois closers para atender 160 reuniões mensais] @(Diego Diehl) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [João responsável pelo onboarding e estruturação inicial das atividades da Ester] @(Diego Diehl + João Vitor Portes da Silva) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [Reunião na sexta às 9h para Ester apresentar progresso ao time] @(Diego Diehl + João Vitor Portes da Silva + Ester) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [Comissão de Recife definida em 150% da mensalidade] @(Diego Diehl + João Vitor Portes da Silva) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [João preparar visão estratégica macro e plano de ação para área de corretores] @(João Vitor Portes da Silva) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [Diego combinar com Mirla e Knight projeto de um mês para reduzir reuniões de João] @(Diego Diehl) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [Diego combinar horário fixo semanal com João para alinhamento] @(Diego Diehl + João Vitor Portes da Silva) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [Webinar dia 19 com Philip, Wagner e Diego] @(Diego Diehl) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [Mensagem de Ano Novo para embaixadores enviada na próxima semana] @(João Vitor Portes da Silva) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [João acionar SDRs para suportar eventos locais] @(João Vitor Portes da Silva) — [6960edbf427f08001307f913](/2026-01) [confirmed]
- [João criar grupo no WhatsApp com Ester, Gustavo e Diego para discutir ações de corretores] @(João Vitor Portes da Silva) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Gustavo meta de 30 reuniões agendadas] @(Gustavo Torres) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [João absorver 15 reuniões mais quentes das BDRs] @(João Vitor Portes da Silva) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Diego, Gustavo, Zanella e Knight dividem 15 reuniões restantes (3 cada)] @(Diego Diehl) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Diego abrir vaga para closer/executivo de contas — contratar 1-2 profissionais] @(Diego Diehl) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Objetivo trimestre: estabelecer CRM padrão com responsável claro e último contato atualizado] @(Diego Diehl) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [João limpar funil, descartar leads frios, alinhar com Gustavo estratégia de contato] @(João Vitor Portes da Silva) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [100% das contas devem ter dono atualizado e próximo passo claro] @(Time comercial) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Criar funil que qualquer pessoa nova entenda em 10 minutos] @(Gustavo Torres) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Diego quer acompanhar rotinas de cada membro na próxima sexta] @(Diego Diehl) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Diego планує reunião com Knight, Usernela e João sobre três principais negócios] @(Diego Diehl) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Próxima reunião semanal focará em estratégias para reuniões mais frias] @(Diego Diehl) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Foco em prospecção de clientes em São Paulo] @(Diego Diehl) — [6964f0693d76f900137fb719](/2026-01) [confirmed]
- [Usar pessoas físicas como cotistas para garantir isenção de imposto de renda] @(Paulo Deitos) — [696528960245ea00136ccc1d](/2026-01) [confirmed]
- [Cada empreendimento terá uma SPE específica com início, meio e fim definidos] @(Eduardo + Paulo Deitos) — [696528960245ea00136ccc1d](/2026-01) [confirmed]
- [Terreno comprado pela SPE diretamente] @(Eduardo + Paulo Deitos) — [696528960245ea00136ccc1d](/2026-01) [confirmed]
- [Custo máximo de R$ 2 mil para cada novo aporte no contrato] @(Paulo Deitos) — [696528960245ea00136ccc1d](/2026-01) [confirmed]
- [Eduardo propõe investimento inicial de R$ 1 milhão no empreendimento Onix] @(Eduardo) — [696528960245ea00136ccc1d](/2026-01) [confirmed]
- [Paulo sugere investir até R$ 500 mil na primeira parte do projeto para a SPE] @(Paulo Deitos) — [696528960245ea00136ccc1d](/2026-01) [confirmed]
- [CRI proposto com 80% de juros, independente do prazo de pagamento] @(Paulo Deitos) — [696528960245ea00136ccc1d](/2026-01) [confirmed]
- [Cotistas devem se reunir e assinar alteração do CRI conforme mudanças no planejamento] @(cotistas) — [696528960245ea00136ccc1d](/2026-01) [confirmed]
- [Jade precisa de volumão + checklist de 4 pontos por ligação + reunião de check todo dia 9h] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Gustavo vai triar 300+ currículos e agendar entrevistas para vaga de Closer] @(Gustavo Torres) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Faixa salarial Closer: CLT 3-6, PJ 4-8 + comissionamento (modelo atual mantido temporariamente)] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Modelo de incentivo: mensalidade de custo por colaborador + mínimo garantido para Closer] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Diego pode pedir apoio de Gustavo em reuniões com clientes enquanto contrata novos closers] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Gustavo distribui ~100 leads por pessoa na equipe] @(Gustavo Torres) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Entrevistas de emprego vão direto para Diego (não só para Gustavo)] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Praças prioritárias: Goiânia, São Paulo, Porto Alegre, Floripa, João Pessoa, Recife, Campinas] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Eventos: Porto Alegre 14/04 e Capão da Canoa 16/04 — 3 empresas já confirmadas] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Plano: 24 eventos em 12 cidades, 50 pessoas por evento, workshops de manhã] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Diego apresentar planejamento estratégico detalhado ao time nas próximas duas semanas] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Gustavo criar tutorial rápido sobre vinculação de agendamentos aos cards do CRM] @(Gustavo Torres) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Validação de contato comercial deve ocorrer 2 meses antes de cada evento] @(Diego Diehl) — [6966a43a99bea20013efccec](/2026-01) [confirmed]
- [Estrutura com empresa intermediária como tomadora do CRI aprovada por todas as partes] @(Paulo Deitos + VitaUrbana) — [6968f2f67ab7870013a596e4](/2026-01) [confirmed]
- [Sala enviar relação das SPEs e imóveis vinculados para documentação] @(Sala Av. Paulista (VitaUrbana)) — [6968f2f67ab7870013a596e4](/2026-01) [confirmed]
- [Sala registrar contrato social da VitaInvest junto ao comercial] @(Sala Av. Paulista (VitaUrbana)) — [6968f2f67ab7870013a596e4](/2026-01) [confirmed]
- [Sala enviar lista de documentos necessários para agilizar processo] @(Sala Av. Paulista (VitaUrbana)) — [6968f2f67ab7870013a596e4](/2026-01) [confirmed]
- [Paulo Deitos enviar contrato de serviço ainda hoje para assinatura] @(Paulo Deitos) — [6968f2f67ab7870013a596e4](/2026-01) [confirmed]
- [Documentação pode ser processada em paralelo com registro do contrato social] @(Paulo Deitos + Sala) — [6968f2f67ab7870013a596e4](/2026-01) [confirmed]
- [Paulo receber documentos e operação estar de pé em 10-15 dias] @(Paulo Deitos) — [6968f2f67ab7870013a596e4](/2026-01) [confirmed]
- [Primeira série CRI com ~R$4M, remuneração mensal, data específica e metros quadrados como garantia] @(Sala Av. Paulista (VitaUrbana)) — [6968f2f67ab7870013a596e4](/2026-01) [confirmed]
- [Diego enviar proposta comercial e minuta de contrato para Amanda assinar] @(Diego Diehl) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Amanda enviar informações de cadastro (CNPJ, nome, CPF, e-mail) para Diego processar proposta] @(Amanda Rocha) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Diego iniciar criação de conta Z2 em paralelo após aprovação] @(Diego Diehl) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Amanda passar retorno sobre ferramenta para supervisor Gustavo e equipe BH] @(Amanda Rocha) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Sem contrato de fidelidade — apenas implantação como garantia de uso efetivo] @(Diego Diehl) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Máximo uma mensagem a cada cinco minutos para verificados — evitar spam e banimento] @(Diego Diehl) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Disparos devem abrir relacionamento, não transformar comunicação em máquina] @(Diego Diehl) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Enviar material mastigado: três imagens, áudio e convite — não book completo] @(Diego Diehl) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Integração com Ouro em SP: mapeia produtos automaticamente. Em BH: base manual sem link Ouro] @(Diego Diehl) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Amanda possui entre 500 e 600 corretores cadastrados atualmente] @(Amanda Rocha) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Ouro registrou 2.000 visualizações com 800 corretores de outubro a janeiro] @(Amanda Rocha) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Proposta R$ 1.674/mês com implantação R$ 7.955 para dois produtos e dois mil corretores] @(Diego Diehl) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Cobrança por produto, licenças WhatsApp e quantidade de parceiros (R$ 50 por mil)] @(Diego Diehl) — [69691d10290b3e0013fc4c42](/2026-01) [confirmed]
- [Diego vai compartilhar prompt compilado de especialista em YAH com participantes interessados] @(Diego Diehl) — [696c11393259e40013346e82](/2026-01) [confirmed]
- [Diego criar projeto 'diretoria Órulo' no ChatGPT para centralizar conhecimento] @(Diego Diehl) — [696c11393259e40013346e82](/2026-01) [confirmed]
- [Diego vai recriar memória global do GPT do zero após migração de conta] @(Diego Diehl) — [696c11393259e40013346e82](/2026-01) [confirmed]
- [Bia verificar contratos Z2 com 11 clientes para analisar cláusulas pro rata] @(Bia) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [Novo modelo de cobrança pro rata não será aplicado a novos clientes] @(Diego Diehl + Eduardo Stringhini) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [Brasal aguarda assinatura há 2 meses — empresa burocrática de Goiânia] @(Diego Diehl) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [Contratar número telefônico para envio e recebimento via WhatsApp] @(Marcelo Rodrigues) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [Usar dívida como moeda de troca com Júnior (Z2)] @(Diego Diehl) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [Esperar retorno da advogada em 21 de janeiro antes de formalizar demissão] @(Diego Diehl + Marcelo Rodrigues) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [Contratar Douglas para negociar acordo trabalhista com advogada da funcionária] @(Marcelo Rodrigues) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [Proposta Marcelo Zen Maceió inclui percentual inicial alto com incentivo até atingir meta] @(Diego Diehl) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [Diego enviar proposta contrato Marcelo Zen Maceió para diretoria revisar] @(Diego Diehl) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [Diego aberto a feedbacks pontuais sobre comunicação e comportamento] @(Diego Diehl) — [696e712f500a210013c24a52](/2026-01) [confirmed]
- [CRI é 100% isento para pessoa física sobre ganho de capital e dividendos] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Investidor com ganho de capital de 3.5M paga 350k em SCP (10%) vs 0 em CRI] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Pessoa jurídica comprando CRI paga 15% — não justifica] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Custo total do CRI para 3 apartamentos: ~100k (64k constituição + 1k/mês manutenção)] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [CRI pode ser vinculado a apartamentos específicos (cota 1 = apt 21, cota 2 = apt 31, etc)] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Investidor pode comprar CRI parcelado ao longo do tempo (3 anos)] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [SCP clients podem economizar 10% em impostos migrando para CRI] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Grande maioria das vendas SCP conseguem ser convertidas para CRI] — [696f8356ee25fd0013b6ac94](/2026-01) [likely]
- [Benefício tributário pode ser embutido no preço para o cliente] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Paulo adicionar regras básicas de criação do CRI na planilha] @(Paulo Deitos) — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Paulo enviar ajustes na planilha e documentação básica de estruturação do CRI ainda hoje] @(Paulo Deitos) — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Luciano analisar aplicação prática do CRI em vendas de participação] @(Luciano) — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [CRI permite definir regras de distribuição diferenciadas entre sócios e herdeiros] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Pai pode comprar 70-80% das cotas enquanto filhos compram diferença] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Remuneração pode ser invertida: pai recebe menos, filhos recebem mais] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Duração da distribuição pode ser por período determinado ou vida inteira] — [696f8356ee25fd0013b6ac94](/2026-01) [confirmed]
- [Diego conectar José com sócios locais de Curitiba e Vitória para benchmarking de conversão] @(Diego Diehl) — [696fc2aba1068c0013a3116d](/2026-01) [confirmed]
- [José pesquisar taxa média de conversão de Curitiba e Vitória para benchmarking] @(José Antônio Freitas) — [696fc2aba1068c0013a3116d](/2026-01) [confirmed]
- [José e Diego alinhar com Gustavo sobre métricas: conversão, ticket médio e perfil de cliente] @(José Antônio Freitas + Diego Diehl + Gustavo Torres) — [696fc2aba1068c0013a3116d](/2026-01) [confirmed]
- [Segunda conversa segunda-feira com José com dados de conversão e faturamento da praça de Goiânia] @(José Antônio Freitas + Diego Diehl) — [696fc2aba1068c0013a3116d](/2026-01) [confirmed]
- [Proposta de fixo mínimo 10-12k para sócio local — baseline para negociação] @(Diego Diehl) — [696fc2aba1068c0013a3116d](/2026-01) [confirmed]
- [Mapear melhor nomenclaturas de mercado como 'coordenador de parcerias' para padronizar linguagem interna] @(Diego Diehl) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Diego criar webinar 'Como Vender Mais' para clientes incorporadoras sobre operação da plataforma] @(Diego Diehl) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Aba de desempenho com grupo de concorrentes liberada para todos clientes] @(Diego Diehl + João) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Closer vincular Incorporadora na aba desempenho dez minutos antes da reunião] @(Diego Diehl) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Distribuir leads da aba de desempenho para coordenadores via CRM conforme protocolo] @(Diego Diehl) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Luiz fornecer informações das reuniões com Elisângela e Jade antes dos encontros] @(Luiz Gustavo Zanella) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Alejandro adicionar coluna de Incorporadora na tabela de eventos] @(Alejandro Olchik) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Semana que vem substituto ministrará treinamento enquanto Diego participa planejamento estratégico POA] @(Diego Diehl) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Treinamentos mantêm frequência semanal toda quarta às 9h exceto feriados] @(Diego Diehl) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Validar configuração de WhatsApp direto para Karen em Curitiba] @(Diego Diehl) — [6970bfcbe50d0f0012494508](/2026-01) [confirmed]
- [Mayumi entregar relatório fechado do webinar até segunda-feira com alcance e retornos] @(Mayumi Takeda) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Mayumi marcar conversa com Wagner para alinhamento] @(Mayumi Takeda) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Mayumi desenvolver esboço de sincronização de movimentos para eventos em praças] @(Mayumi Takeda) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Diego enviar documentos sobre planejamento de canal de parcerias e diagnóstico de maturidade] @(Diego Diehl) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Mayumi enviar cronograma e pré-desenho dos painéis até esta semana] @(Mayumi Takeda) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Plantão de dúvidas semanal será testado em Curitiba com Zanella] @(Diego Diehl) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Webinar: usar dupla em vez de três pessoas — mais efetivo e menos cansativo] @(Diego Diehl) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Integração de catálogo com imobiliárias requer treinamento de onboarding] @(Diego Diehl) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Corrigir problemas técnicos antes do próximo webinar (fone para Felipe)] @(Diego Diehl) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Estratégia de cashback/comissão para corretores via integração com imobiliárias] @(Diego Diehl) — [6970d3346d38bb00139bbcb1](/2026-01) [confirmed]
- [Diego agendar semana de visitas em imobiliárias para 5 de fevereiro] @(Diego Diehl) — [6970fca1e50d0f00124950b1](/2026-01) [confirmed]
- [Diego enviar informações de precificação e material sobre destaque para Otimatec] @(Diego Diehl) — [6970fca1e50d0f00124950b1](/2026-01) [confirmed]
- [João Diego (especialista) entrar em contato com Otimatec para trocar ideias sobre estratégia] @(Diego Diehl) — [6970fca1e50d0f00124950b1](/2026-01) [confirmed]
- [Otimatec enviar material dos empreendimentos para cadastro rápido na plataforma] @(Elizangela Fernandes Borges) — [6970fca1e50d0f00124950b1](/2026-01) [confirmed]
- [Otimatec pagará valor mínimo de R$ 655 para dois empreendimentos conforme negociado] @(Elizangela Fernandes Borges) — [6970fca1e50d0f00124950b1](/2026-01) [confirmed]
- [Otimatec fornecer dados para faturamento: e-mail, data vencimento, forma pagamento, assinante e CNPJ] @(Elizangela Fernandes Borges) — [6970fca1e50d0f00124950b1](/2026-01) [confirmed]
- [Pedro assinar NBA de incorporação de 80 milhões VGV na quarta-feira] @(Pedro Monte) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Diego apresentar solução CRI/SCP ao incorporador e avaliar estruturação de crédito] @(Diego Diehl) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Pedro e Diego se reunirem na quarta-feira seguinte para definir estratégia de venda do projeto] @(Pedro Monte + Diego Diehl) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Diego enviar site de Claudio para Pedro avaliar captação de recursos] @(Diego Diehl) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Diego visitar projeto estudantil perto da USP numa quarta-feira à tarde] @(Diego Diehl) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Pedro conectar Diego com Leandro para conversa sobre metodologia de avaliação imobiliária] @(Pedro Monte) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [CRI é isento de imposto para pessoa física — usar como argumento de venda] @(Diego Diehl) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Empresa terá conselheiros dedicados ao negócio para estruturação melhor] @(Pedro Monte) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Pedro escalar com agentes autônomos no segundo semestre de 2026] @(Pedro Monte) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Diego estruturar modelo com sócio local que circula entre incorporadoras e imobiliárias] @(Diego Diehl) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [CRI com custo de 100 mil em três anos para operações de 5 milhões] @(Diego Diehl) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Projeto de 40 milhões VGV economizaria 1.5 milhão em impostos com dois CRIs] @(Diego Diehl) — [6971292de4d717001331d562](/2026-01) [confirmed]
- [Bruna desbloquear Mirla do disco conforme combinado] @(Bruna Soares) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Diego apresentar estratégia de integração Z2 e Ouro nos próximos dias] @(Diego Diehl) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Time de produto levar retorno para Ouro sobre downloads de tabelas via WhatsApp] @(Time de Produto) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Treinamento Z2A toda quarta às 9h com participação do Rodrigo Italiano] @(Diego Diehl) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Teste liberou Z2 gratuitamente por 2 meses para 15 clientes com boa adesão] @(Diego Diehl) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Metade das informações já sincronizadas entre Z2 e Ouro, outra metade em integração] — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Monitora Zé funciona como MVP com dados Z2 evoluindo para score integrado Ouro] @(Rodrigo Italiano) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Projeto futuro: levar Z2 para dentro da plataforma Ouro de forma integrada] — [697214b6e4d717001331f32f](/2026-01) [likely]
- [Z2A integra vendas do CV automaticamente — timeline completa do corretor] @(Rodrigo Italiano) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Plataforma homologada Meta permite criar templates com aprovação automática em até 24h] @(Rodrigo Italiano) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Dashboard diferencia crescimento de contatos vs engajamento para visão clara] @(Rodrigo Italiano) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [Relatório semanal traz indicadores operacionais com análise Z2 sobre crescimento e desempenho] @(Rodrigo Italiano) — [697214b6e4d717001331f32f](/2026-01) [confirmed]
- [João perguntar à Z2 se é possível responder contatos pelo número oficial da Meta] @(João Vitor Portes da Silva) — [69736636913cb900132bd0eb](/2026-01) [confirmed]
- [Gustavo criar processo inicial para acionamento das 26 incorporadoras do webinar antes de passar aos BDRs] @(Gustavo Torres) — [69736636913cb900132bd0eb](/2026-01) [confirmed]
- [João e Ester agendar reunião com dono da Jampa Life (17 corretores) para segunda-feira] @(João Vitor Portes da Silva + Ester Elisa de Souza Rodrigues) — [69736636913cb900132bd0eb](/2026-01) [confirmed]
- [Neno participar de reunião com dono da imobiliária Jampa Life para validar integração e coletar feedback] @(Neno) — [69736636913cb900132bd0eb](/2026-01) [confirmed]
- [Manter foco em João Pessoa durante janeiro — número banido precisa ser desbloqueado] @(Diego Diehl) — [69736636913cb900132bd0eb](/2026-01) [confirmed]
- [Próximo evento será em Capão da Canoa após manter foco em João Pessoa] @(Diego Diehl) — [69736636913cb900132bd0eb](/2026-01) [confirmed]
- [Ester e João executarem experimento de ativação com cadastros da semana em João Pessoa (50%)] @(Ester Elisa de Souza Rodrigues + João Vitor Portes da Silva) — [69736636913cb900132bd0eb](/2026-01) [likely]
- [Diego criar relatório processado com IA para planejamento estratégico] @(Diego Diehl) — [69736636913cb900132bd0eb](/2026-01) [confirmed]
- [Gustavo enriquecer documento com Bruna antes de compartilhar com time] @(Gustavo Torres) — [69736636913cb900132bd0eb](/2026-01) [confirmed]
- [Trocar 'ver contato' para 'quero falar com gerente de parcerias' — mais claro e alinhado com intenção] @(Marcelo Rodrigues) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Neno refinar fluxos e criar copy detalhada para intermediação de contatos] @(Neno Andrade) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Priorizar notificações via app/push sobre WhatsApp — reduzir custos] @(Alejandro Olchik) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Sistema detectar instalação de app e enviar push em vez de WhatsApp quando possível] @(Neno Andrade) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Botão de contato mais visível e destacado no portal] @(Neno Andrade) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [DL deve ter muito menos visibilidade de audiência que incorporadores regulares — criar percepção de valor] @(Alejandro Olchik) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Gustavo coordenar outreach com Laura em João Pessoa — 27 incorporadoras] @(Gustavo Torres + Laura) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Gustavo e Laura refinarem copy da Ester — pedir contato de gerente de parcerias, não número geral] @(Gustavo Torres + Laura) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Diego identificar contatos-chave de corretores em cada região] @(Diego Diehl) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Bruna compartilhar lista centralizada de contatos-chave com Diego] @(Bruna Soares) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Bruna alinhar cartilha de comunicação com Laura e Mayumi] @(Bruna Soares + Laura + Mayumi) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Mensagem deve enfatizar benefícios gratuitos da plataforma — evitar linguagem repetitiva de vendas] @(Diego Diehl) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Testar primeiro com 5-7 incorporadoras antes de масштабировать para todas 27] @(Gustavo Torres) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Epic focado em visibilidade e valor percebido — não só intermediação] @(Alejandro Olchik) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Epic pequeno e focado para entregar resultados concretos rapidamente] @(Alejandro Olchik) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [Template WhatsApp aprovado para continuar conversas após janela de 24h] @(Neno Andrade) — [697377d35355be00138a5614](/2026-01) [confirmed]
- [José desenvolverá projeto em Goiânia focado em corretores com acesso à diretora comercial Beatriz Gomes] @(José Antônio Freitas) — [6973b71e7f640c0013685039](/2026-01) [confirmed]
- [Estratégia local em Goiânia: visitas a imobiliárias, eventos e relacionamento próximo com corretores] @(José Antônio Freitas) — [6973b71e7f640c0013685039](/2026-01) [confirmed]
- [Integração da solução Órulo com CRM, portfólio e site das imobiliárias é fundamental] — [6973b71e7f640c0013685039](/2026-01) [confirmed]
- [Abordagem segmentada para incorporadoras via ADEMI e empresas grandes com diretores de inteligência] @(José Antônio Freitas) — [6973b71e7f640c0013685039](/2026-01) [likely]
- [José enviar mensagem para Diego informando sobre a conversa com Felipe] @(José Antônio Freitas) — [6973b71e7f640c0013685039](/2026-01) [confirmed]
- [Gustavo abrir card de agendamento no Skydes para rastreabilidade de negociacoes] @(Gustavo Torres) — [6979fa4507a27300130c12b7](/2026-01) [confirmed]
- [Luiz revisar WhatsApp conforme solicitado por Mirla após término da reunião] @(Luiz Gustavo Zanella) — [6979fa4507a27300130c12b7](/2026-01) [confirmed]
- [Ester abordar 24-26 corretores cadastrados entre 18-24 janeiro para aumentar retenção nas primeiras semanas] @(Ester Elisa de Souza Rodrigues) — [697ca3cb6216b200139caad4](/2026-01) [confirmed]
- [Usar abordagem pessoal com áudio e material educativo em vez de mensagens genéricas] @(Ester Elisa de Souza Rodrigues) — [697ca3cb6216b200139caad4](/2026-01) [confirmed]
- [Implementar sistema de pontuação 0-10 para incentivar atualização de anúncios de incorporadoras] @(time de produto) — [697ca3cb6216b200139caad4](/2026-01) [likely]
- [João contatar Wagner Felipe solicitando indicação de corretor da zona sul de João Pessoa] @(João Vitor Portes da Silva) — [697ca3cb6216b200139caad4](/2026-01) [confirmed]
- [Ester identificar corretor com forte atuação na zona sul de João Pessoa para ser ponte com incorporadoras] @(Ester Elisa de Souza Rodrigues) — [697ca3cb6216b200139caad4](/2026-01) [confirmed]
- [Gustavo definir cartilha de comunicação para processar indicações de incorporadoras não cadastradas] @(Gustavo Torres) — [697ca3cb6216b200139caad4](/2026-01) [likely]
- [Parceria com Creci Paraíba em projeto 'Índice Cresce'] @(Ester Elisa de Souza Rodrigues) — [697ca3cb6216b200139caad4](/2026-01) [likely]
- [Gustavo enviar contrato e termo de adesão para assinatura após Kaique coletar dados (CNPJ, assinante, dia preferido boleto, email financeiro)] @(Gustavo Torres) — [697cbcd6697b570013ec88f3](/2026-01) [confirmed]
- [Kaique apresentar proposta Orla à gerente comercial para aprovação] @(Kaique Carvalho) — [697cbcd6697b570013ec88f3](/2026-01) [confirmed]
- [Gustavo enviar template de proposta de duas páginas para Kaique apresentar à gerente] @(Gustavo Torres) — [697cbcd6697b570013ec88f3](/2026-01) [confirmed]
- [Kaique retornar dados assinados para Gustavo processar contratação] @(Kaique Carvalho) — [697cbcd6697b570013ec88f3](/2026-01) [confirmed]
- [Mune qualifica para preço reduzido de R$ 1.500 mensais por volume baixo de empreendimentos] @(Diego Diehl) — [697cbcd6697b570013ec88f3](/2026-01) [confirmed]
- [Contrato Orla é anual — período mínimo de 2 meses não é suficiente para avaliar] @(Diego Diehl) — [697cbcd6697b570013ec88f3](/2026-01) [confirmed]
- [Mune substituir Google Drive por link Orla para aumentar audiência e engajamento] @(Kaique Carvalho) — [697cbcd6697b570013ec88f3](/2026-01) [likely]
- [Diego enviar link de acesso a plataforma Orulo para Luigi via WhatsApp] @(Diego Diehl) — [6980adfcc547420013ede25e](/2026-02) [confirmed]
- [Luigi conversar com equipe interna para implementar uso da plataforma Orulo] @(Luigi Gubert) — [6980adfcc547420013ede25e](/2026-02) [likely]
- [Thales passar contato de Janela para Luigi conectar com suporte local em Curitiba] @(Thales Santos) — [6980adfcc547420013ede25e](/2026-02) [confirmed]
- [Treinamento prático será reformatado por Diego baseado no feedback da equipe para a próxima semana] @(Diego Diehl) — [698334ce7d83e400138dc05b](/2026-02) [confirmed]
- [Próximo treinamento será sobre planejamento estratégico de canal de parcerias com case real] @(Diego Diehl) — [698334ce7d83e400138dc05b](/2026-02) [confirmed]
- [Semana seguinte incluirá Lab Series com workshop prático, roleplay e reenactment] @(Diego Diehl) — [698334ce7d83e400138dc05b](/2026-02) [confirmed]
- [Diego enviará apresentação de evolução organizacional para o time] @(Diego Diehl) — [698334ce7d83e400138dc05b](/2026-02) [confirmed]
- [Time revisará apresentação de planejamento estratégico como lição de casa] @(time) — [698334ce7d83e400138dc05b](/2026-02) [confirmed]
- [Diego agendará treinamento de inteligência de mercado com Pedro para abril] @(Diego Diehl) — [698334ce7d83e400138dc05b](/2026-02) [confirmed]
- [Diego removerá nome de cliente da apresentação antes de compartilhar com o time] @(Diego Diehl) — [698334ce7d83e400138dc05b](/2026-02) [confirmed]
- [Zanella prefere manter duas reuniões semanais sem adicionar mais treinamentos] @(Luiz Gustavo Zanella) — [698334ce7d83e400138dc05b](/2026-02) [confirmed]
- [Desentendimentos devem ser resolvidos um a um sem envolver terceiros] — [698334ce7d83e400138dc05b](/2026-02) [confirmed]
- [Comissões varían por categoria: mercado 4%, premium 5%, super 6%] — [698334ce7d83e400138dc05b](/2026-02) [likely]
- [One page deve ser enviado até 17h do dia anterior à reunião] @(Diego Diehl) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Reunião de GTM para conectar marketing, CS e cadastro] @(Diego Diehl) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Evento de Curitiba 25/02 focado em incorporadoras — local confirmado pelo IBPQ] @(Luiz Gustavo Zanella) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Luiz trazer estimativa de custo do evento de 25/02 para orçamento] @(Luiz Gustavo Zanella) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Luiz abordar mínimo 100 incorporadores para convite do evento de março] @(Luiz Gustavo Zanella) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Comunicação com incorporadores deve começar até 10/02] @(Luiz Gustavo Zanella) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Meta de Luiz é atingir 30 incorporadoras no evento de 25/02] @(Luiz Gustavo Zanella) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Evento de março em Vitória será workshop com foco em incorporadoras] @(Pedro Ruza Kneip Navarro) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Pedro solicitar relatório de requisições do Espírito Santo dos últimos três meses] @(Pedro Ruza Kneip Navarro) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Diego agendar reunião com Mayumi para sexta às 11h30] @(Diego Diehl) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Pedro agendar cinco reuniões com incorporadoras até 20/02] @(Pedro Ruza Kneip Navarro) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Pedro enviar mensagem para 30 corretores pedindo produtos faltantes] @(Pedro Ruza Kneip Navarro) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Pedro treinar corretores para pressionar incorporadoras a entrarem na plataforma] @(Pedro Ruza Kneip Navarro) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Diego reforçar pauta de Portal Z2 em reunião com Z2 amanhã cedo] @(Diego Diehl) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Sprints devem ser semanais com foco em planejado, executado e resultados] @(Diego Diehl) — [69834628f89b5a0013ba42fd](/2026-02) [confirmed]
- [Felipe enviar apresentação para Micheline, Celina e Diego] @(Felipe Goettems) — [6984a262c8ca580013150c28](/2026-02) [confirmed]
- [Felipe reunir-se com Celina para discutir questões técnicas adicionais] @(Felipe Goettems) — [6984a262c8ca580013150c28](/2026-02) [confirmed]
- [CRI permite ciclo de reinvestimento com isenção em novos empreendimentos] @(Felipe Goettems) — [6984a262c8ca580013150c28](/2026-02) [confirmed]
- [Limite de 50 mil mensais por CNPJ aplica-se ao total, múltiplos CNPJs não evitam tributação] — [6984a262c8ca580013150c28](/2026-02) [confirmed]
- [Celina simular novo projeto e lançamento recente com estrutura CRI] @(Celina Villarim) — [6984a262c8ca580013150c28](/2026-02) [confirmed]
- [Reforma tributária aumentara carga — cautela com litígio administrativo após Instrução 227] — [6984a262c8ca580013150c28](/2026-02) [confirmed]
- [24 eventos programados para 2026 com a VMV, incluindo workshop sobre estruturação de canal] @(Diego Diehl + VMV Group) — [6984c57ba0c380001332dc21](/2026-02) [confirmed]
- [Priscila encaminhar demanda de enriquecimento de anúncios para assistente de marketing da Torreão] @(Priscila) — [6984c57ba0c380001332dc21](/2026-02) [confirmed]
- [Diego solicitar atenção especial do Cesar para reunião com equipe da Torreão] @(Diego Diehl) — [6984c57ba0c380001332dc21](/2026-02) [confirmed]
- [Agendar treinamento com time de CS da Órulo para Torreão Vilarinho] @(Diego Diehl) — [6984c57ba0c380001332dc21](/2026-02) [confirmed]
- [Bruna liberar link da gravação para acesso posterior dos participantes] @(Bruna Almeida) — [6984c57ba0c380001332dc21](/2026-02) [confirmed]
- [Incorporadoras abertas ao mercado têm melhor relacionamento com corretores] @(Diego Diehl) — [6984c57ba0c380001332dc21](/2026-02) [confirmed]
- [Criar método para canal de parcerias e padrão replicável] @(Diego Diehl) — [6984c57ba0c380001332dc21](/2026-02) [confirmed]
- [Vitacom usar corretores Órulo como divulgadores e promotores de CRI] @(Paulo Deitos + Samanta) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [White label criado para cada corretor acessar página exclusiva com oferta Vitacom] @(Paulo Deitos) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [Cliente final contrata e deposita diretamente na página white label do corretor] @(Paulo Deitos) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [Cadastro do cliente fica vinculado ao cadastro do corretor referenciador] @(Paulo Deitos) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [Corretores recebem comissão de 1% adicional — total 6% taxa de distribuição] @(Paulo Deitos) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [Comissão retida por Captable e paga após fechamento da série] @(Paulo Deitos) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [Oferta potencial inicial de R$5 milhões em primeira série de CRI] @(Paulo Deitos) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [Próximos R$5 milhõesColocados rapidamente se primeira série tiver sucesso (escassez)] @(Paulo Deitos) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [Paulo estruturar segunda série de CRI dentro de 1-2 dias quando aprovado] @(Paulo Deitos) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [André levar proposta de distribuição via corretores para comitê e retornar com resposta] @(André Franklin) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [Paulo validar mensagens dos corretores para garantir conformidade regulatória] @(Paulo Deitos) — [6989ef6383febd0013d31918](/2026-02) [confirmed]
- [Diego compartilhar documento com Gustavo como editor para sugestões conjuntas] @(Diego Diehl) — [698b7223486bad00134bacac](/2026-02) [confirmed]
- [Diego organizar e limpar arquivos do drive comercial com Gustavo] @(Diego Diehl + Gustavo Torres) — [698b7223486bad00134bacac](/2026-02) [confirmed]
- [Gustavo revisar playbooks antigos e organizar conhecimentos estruturados da equipe] @(Gustavo Torres) — [698b7223486bad00134bacac](/2026-02) [confirmed]
- [Gustavo mapear educação antes da venda e elementos-chave para incorporadoras] @(Gustavo Torres) — [698b7223486bad00134bacac](/2026-02) [confirmed]
- [Gustavo formalizar projeção salarial e mudança de função similar ao documento de Mila] @(Gustavo Torres) — [698b7223486bad00134bacac](/2026-02) [confirmed]
- [Diego compartilhar DOC com Gustavo como editor para sugestões] @(Diego Diehl) — [698b7223486bad00134bacac](/2026-02) [confirmed]
- [Playbooks devem ser revisados mensalmente com contribuições da equipe] @(Diego Diehl + Gustavo Torres) — [698b7223486bad00134bacac](/2026-02) [confirmed]
- [SDRs devem trazer cases de sucesso em reuniões para enriquecer conhecimento coletivo] @(Diego Diehl) — [698b7223486bad00134bacac](/2026-02) [confirmed]
- [Gustavo杭revisar playbooks antigos e organizar conhecimentos] @(Gustavo Torres) — [698b7223486bad00134bacac](/2026-02) [confirmed]
- [João reduzir carteira de negócios de 66 para 50 clientes nos próximos 10 dias] @(João Vitor Portes da Silva) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Diferenciar 'perdido' de 'não vai comprar agora' para melhor gestão de carteira] @(Diego Diehl) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Criar padrão de cadência de contatos antes de marcar cliente como perdido] @(Diego Diehl) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [João documentar perdidos em planilha com situação, chance de compra e prazo] @(João Vitor Portes da Silva) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [João preencher campo 'analisar falha' antes de marcar negócio como perdido] @(João Vitor Portes da Silva) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Negócios perdidos ficam em área separada com histórico completo] @(Diego Diehl) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Closer focado em atividade, reuniões e contratos fechados — não volume de CRM] @(Diego Diehl) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Reunião semanal de forecast na terça-feira] @(Diego Diehl) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Gustavo definir critérios claros para reuniões XL que vão para closer] @(Gustavo Torres) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Gustavo enviar feedback a João sobre qualidade e andamento das reuniões XL] @(Gustavo Torres) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Reunião XL com sócio ou decisor deve ter closer presente obrigatoriamente] @(Diego Diehl) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Validação de cargo e expectativa do cliente deve ser feita pelo BDR antes de reunião XL] @(Diego Diehl) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Implementar campo de observações para documentar motivo da perda de negócio] @(Gustavo Torres) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [João testar vídeos curtos personalizados para apresentar solução a decisores] @(João Vitor Portes da Silva) — [698b9011657ae90013b40ee1](/2026-02) [confirmed]
- [Laura do cadastro direcionada para suporte Bitrix ou Marcelo (novo dono do processo)] @(Diego Diehl) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Marcelo investigar e entender mais sobre Bitrix para suportar equipe comercial] @(Marcelo Rodrigues) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Luiz avançar para contratação se proposta de isenção tributária IGSA for aprovada] @(Luiz Gustavo Zanella) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Luiz atualizar CRM com informações sobre proposta de isenção tributária] @(Luiz Gustavo Zanella) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Diego criar infraestrutura automatizada para apoiar análises comerciais] @(Diego Diehl) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Diego testar abordagem estratégica com dados em follow-up com incorporadora hoje] @(Diego Diehl) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Marcelo adicionar data de entrega ao banco de dados de propostas comerciais] @(Marcelo Rodrigues) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Diego priorizar aprofundamento em conceitos-chave ao invés de cobertura superficial] @(Diego Diehl) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Conteúdo do treinamento será transcrito e consolidado para agente de IA futuro] @(Diego Diehl) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Diego refinará prompt de análise de velocidade de vendas com estratégias de abordagem diplomática] @(Diego Diehl) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Diego aprofundará em três vertentes: lançamentos, estoque acumulado e vendas] @(Diego Diehl) — [698c6f356979ef0013b83ce5](/2026-02) [confirmed]
- [Guilherme manter controle inicial da operação com aconselhamento dos parceiros] @(Guilherme) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Modelo de coordenador de plataforma como evolução do vendedor tradicional] @(Guilherme + Eduardo) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Coordenador recebe 30% da comissão, 5% distribuído entre equipe] @(Guilherme) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Variável do coordenador gira entre 0,3% e 0,5% do faturamento] @(Guilherme) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Pacote Plus inclui destaques, banners, e-mail marketing e push notifications] @(Guilherme) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Serviço inclui institucional, viabilidade financeira e mentoria de tabela] @(Guilherme) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Workshop em março em Curitiba para 50 pessoas sobre parcerias] @(Guilherme) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Eduardo compartilhar modelo financeiro detalhado com Guilherme para análise conjunta] @(Eduardo Stringhini) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Diego e Guilherme elaborar planilha com receitas, custos e esforços de cada lado] @(Diego Diehl + Guilherme) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Guilherme trazer gerente experiente após Carnaval para iniciar operações] @(Guilherme) — [698cb58fecdf0e001300edbc](/2026-02) [confirmed]
- [Diego revisar apresentação comercial e ajustar slides para reduzir espaços em branco e aumentar impacto visual] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Apresentação deve transmitir 14 anos de experiência — não parecer startup de 6 meses] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Incluir números grandes de corretores acessando para criar sensação de volume e escala] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Contrato de 12 meses sem fidelidade deve ser comunicado proativamente antes de perguntas] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Incluir passos do processo de implementação na apresentação] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Z2A como integração importante na apresentação para incorporadoras] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Digital activation oferecida como pacote adicional no momento da venda] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Bloqueio de tabela já foi desenvolvido — incluir na apresentação] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Diego consolidar versão final do material completo de embaixadores para segunda quinzena de fevereiro] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Comercial vende, CS toca, marketing apoia no programa de embaixadores] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Produtos financeiros mencionados como gancho para cliente perguntar detalhes] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Slides consolidados para menos slides com mais informação] @(Diego Diehl) — [698dcb4b834af3001393610e](/2026-02) [confirmed]
- [Serviço de consultoria de Gisele será opcional (não obrigatório) e cobrado Separado da integração] @(Diego Diehl + Bruno) — [698e071b1bcf5d0012a314f4](/2026-02) [confirmed]
- [Diego e Bruno indicam 5 a 7 clientes para Gisele testar serviço de consultoria (clientes médio porte, não plano mínimo)] @(Diego Diehl + Bruno) — [698e071b1bcf5d0012a314f4](/2026-02) [confirmed]
- [Bruno entrega apresentação comercial atualizada com novos valores e fluxo do delimitador pós-Carnaval] @(Bruno Zucchetti) — [698e071b1bcf5d0012a314f4](/2026-02) [confirmed]
- [Bruno agenda treinamento com Gisele sobre integrações, catálogo e exclusividades após apresentação pronta] @(Bruno Zucchetti) — [698e071b1bcf5d0012a314f4](/2026-02) [confirmed]
- [Gisele prepara documento detalhado com serviços oferecidos e valores para imobiliárias] @(Gisele Vilela) — [698e071b1bcf5d0012a314f4](/2026-02) [confirmed]
- [Gisele define preço do serviço de consultoria com base em feedback de Bruno e Diego] @(Gisele Vilela) — [698e071b1bcf5d0012a314f4](/2026-02) [confirmed]
- [Diego propõe rebate para Gisele ao trazer exclusividades imobiliárias para a plataforma] @(Diego Diehl) — [698e071b1bcf5d0012a314f4](/2026-02) [likely]
- [Login simplificado é PRIORIDADE 1 para reduzir atrito com Google Drive] @(Alexandre Rodrigues + Alejandro Olchik) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Página de empreendimentos com filtros e descrição simplificada na capa é PRIORIDADE 2] @(Alexandre Rodrigues + Alejandro Olchik) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Tabela digital geral para filtrar múltiplos empreendimentos é PRIORIDADE 3] @(Alexandre Rodrigues + Alejandro Olchik) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Analytics do Portal de Parcerias vem antes de Analytics dos Empreendimentos] @(Alexandre Olchik) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Acesso a dados parciais sem login para gerar engajamento antes de login completo] @(Alejandro Olchik) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Login via WhatsApp é a solução para problemas de login] @(Alexandre Rodrigues + Diego Diehl) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Lançamento André de Barros confirmado para 14 de abril com 1.500 corretores na Ópera de Arame] @(Alexandre Rodrigues) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Alejandro produzir vídeo explicativo sobre Portal e marca Hype para novos parceiros] @(Alejandro Olchik) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Alexandre enviar vídeos de tela quando surgirem demandas para Diego organizar] @(Alexandre Rodrigues) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Diego organizar demandas de ajustes rápidos e agenda de evolução do Portal] @(Diego Diehl) — [698f6d9bacd46d001342c98e](/2026-02) [confirmed]
- [Luiz enviar orçamentos dos locais para evento até hoje] @(Luiz Gustavo Zanella) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Z2A deve ser tratado como prioridade real, não acessório — meta de 12 contratos no período] @(Diego Diehl) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Eliminar etapa de formulário; enviar contrato após aprovação da proposta] @(Diego Diehl) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Definir ação em escala semanal com Zanella, Knight, Gustavo, Mirla e João] @(Diego Diehl) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Diego estruturar desdobramento de metas para conversa com Gustavo] @(Diego Diehl) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Diego apresentar desdobramento de metas na semana que vem] @(Diego Diehl) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Gustavo e time validar iniciativa de vídeo follow-up com decisores ausentes] @(Gustavo Torres + time) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [João enviar vídeo resumido da reunião ao grupo] @(João Vitor Portes da Silva) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Follow-up rápido é essencial; 'bom dia tudo bem' é amadorismo] @(Diego Diehl) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Prospectar grandes incorporadoras para trazer contratos de ticket maior] @(Diego Diehl) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Todos negócios devem ter próximo passo com data definida] @(Diego Diehl) — [699c4f44e344ac00135beff1](/2026-02) [confirmed]
- [Douglas agendar reunião com João Biasi quando Diego visitar Curitiba (semana de 16 de março)] @(Douglas Vilar) — [699de717fc507800135cebf6](/2026-02) [confirmed]
- [Diego enviar apresentação enxuta sobre CRI para Andressa] @(Diego Diehl) — [699de717fc507800135cebf6](/2026-02) [confirmed]
- [Diego enviar agenda detalhada para Douglas e Andressa organizarem reuniões em Curitiba] @(Diego Diehl) — [699de717fc507800135cebf6](/2026-02) [confirmed]
- [Andressa estudar proposta de Diego antes da próxima semana] @(Andressa Magalhães) — [699de717fc507800135cebf6](/2026-02) [confirmed]
- [Diego visitar Curitiba semana de 16 de março (segunda a sexta)] @(Diego Diehl) — [699de717fc507800135cebf6](/2026-02) [confirmed]
- [Diego participar de homenagem na ALESP em São Paulo dia 18 de março] @(Diego Diehl) — [699de717fc507800135cebf6](/2026-02) [confirmed]
- [Possível almoço entre Diego, Douglas e Andressa após podcast] @(Diego Diehl + Douglas Vilar + Andressa Magalhães) — [699de717fc507800135cebf6](/2026-02) [likely]
- [Rafael não é o contato certo — atua com tributação de dividendos e indústria, não imobiliário] — [699de717fc507800135cebf6](/2026-02) [confirmed]
- [Padronizar negociações quentes em etapa específica no CRM para visibilidade de previsão] @(Diego Diehl + Gustavo Torres) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [João já cria card na etapa após reunião com cliente se chance grande de fechar no mês] @(João Vitor) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Luiz adicionar Terral de Goiânia (1500) ao consolidado] @(Luiz Gustavo Zanella) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Luiz adicionar 2R ao consolidado com valor confirmado] @(Luiz Gustavo Zanella) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Luiz enviar proposta 2R com Hora hoje no contrato] @(Luiz Gustavo Zanella) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Gustavo remover clientes da época sem música do forecast] @(Gustavo Torres) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Diego enviar informações de contato do Senac para Felipe] @(Diego Diehl) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [João enviar mensagem diplomática para Alan da Arquiplan sobre uso] @(João Vitor) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [João reforçar com Evandro sobre lista atualizada de produtos com estoque] @(João Vitor) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Diego sugerir áudio personalizado para Senac sobre fechamento e assinatura] @(Diego Diehl) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Knight abordar novos usuários de Vitória para evento dia 4] @(Knight) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Convites centralizados — evitar sobrecarga e garantir qualidade] @(Diego Diehl) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Contato WhatsApp obrigatório na inscrição para follow-up] @(Diego Diehl) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Luiz adicionar implementação no resultado comercial no Bitrix para cobrança financeira] @(Luiz Gustavo Zanella) — [699df8a5fc507800135cef6d](/2026-02) [confirmed]
- [Patrocínio de R$80k por empresa com 50% de desconto já acordado] @(Diego Diehl + André Battú) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [Dia 15: Órulo palestra 30min focada em corretores + painel 50min com três empresas das 8h30-18h] @(Diego Diehl + Bruna Almeida + André Battú) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [Dia 16: workshop próprio usando apenas espaço e estrutura básica do local] @(Diego Diehl + Bruna Almeida) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [André passar Instagram da imobiliária e/ou fazer vídeo do espaço para equipe] @(André Battú) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [Bruna enviar logomarca, fotos dos palestrantes e materiais para André até dia 15] @(Bruna Almeida) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [André conversar com Cauã Machado no sábado sobre horário do evento dia 16] @(André Battú) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [Gustavo continuar procurando local em Curitiba e Luana adaptar orçamento para 150 pessoas] @(Gustavo Torres + Luana) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [Criar grupo separado para sincronizar comunicação e marketing do evento] @(Diego Diehl + Bruna Almeida) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [Diego ajustar passagem para ficar até sexta-feira em Capão] @(Diego Diehl) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [André apresentar espaço e condomínios locais para Diego conhecer mercado] @(André Battú) — [699f2aa210f9590013215cfc](/2026-02) [confirmed]
- [Sugestão André: evento à noite (18h30) em Capão para não tirar construtores da rotina] @(André Battú) — [699f2aa210f9590013215cfc](/2026-02) [likely]
- [Workshops confirmados em Vitória (4/3) e Curitiba (18/3) com dois dias antes em Porto Alegre] @(Diego Diehl + Mayumi Takeda) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Diego marcar reunião para apresentar cronograma de ações dos eventos na semana que vem] @(Diego Diehl) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Diego e Mayumi confirmar data 12 de março para reunião estendida sobre cronograma de eventos (1h30)] @(Diego Diehl + Mayumi Takeda) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Diego enviar apresentação para Carli revisar e atualizar para congresso] @(Diego Diehl) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Gustavo encabezar convites para eventos em Porto Alegre e Capão da Canoa] @(Gustavo Torres) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Diego revisar apresentação comercial com todo time e abrir para comentários antes da finalização] @(Diego Diehl + time comercial) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Diego criar documento de formalização do vídeo institucional até segunda quinquana de fevereiro] @(Diego Diehl) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Mayumi retornar calendário de eventos por praça revisado no início da semana] @(Mayumi Takeda) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Próxima reunião semana que vem no mesmo horário] @(Mayumi Takeda + Gustavo Torres + Diego Diehl) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Diego dar toque em Kowalski para intermediação com Vinícius sobre colaboração] @(Diego Diehl) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Testar estratégias manualmente em pequena escala antes de automatizar] @(Diego Diehl) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Gustavo rever planilha de prioridades e ações em próxima reunião] @(Gustavo Torres) — [69a0435446f1b600120eec2f](/2026-02) [confirmed]
- [Parceria Órulo + Apolar formally fechada — 14 empreendimentos novos entram na plataforma Apolar com 90 dias de carência gratuita] @(Diego Diehl + Felipe Steberl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Comissão Apolar: 5% nas negociações com construtoras (vs. 4% na plataforma padrão) — diferencial pelo volume] @(Felipe Steberl + Diego Diehl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Modelo de exclusividade total para pequenas e médias construtoras — argumento competitivo para captar novas incorporadoras] @(Felipe Steberl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Órulo usado como Pit comercial das exclusividades — argumentação: reach de 600 imobiliárias + 5 mil corretores] @(Diego Diehl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Imóveis não vendidos em 10-15 dias vão para Apolar Busca — ciclo virtuoso de distribuição] @(Felipe Steberl + Diego Diehl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Luiz (Apolar) faz treinamento personalizado para a equipe Órulo sobre rastreabilidade] @(Luiz Gustavo Zanella) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Diego manda proposta padrão em minuta para Werner — template padronizado de contrato] @(Diego Diehl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Luiz envia minuta padrão para Werner, removendo dados do último contratante] @(Luiz Gustavo Zanella) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Diego cria grupo para discussão exclusiva de lançamentos com Apolar] @(Diego Diehl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Felipe contata João para incluir Paraguai no pacote de expansão] @(Felipe Steberl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Workshop em Curitiba em 3 semanas — focado em 150 incorporadoras sobre parcerias] @(Felipe Steberl + Diego Diehl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Werner envia lista completa de incorporadoras e empreendimentos para Diego e Luiz] @(Werner Winter) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Paraguai incluído na plataforma — possível tradução do site + 5 lojas (1 própria de Felipe)] @(Felipe Steberl + Felipe Goettems) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Precificação padrão Apolar para incorporadoras — segue tabela Apolar (não Órulo)] @(Diego Diehl + Felipe Steberl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Portal Apolar exibe apenas lançamentos com gestão exclusiva de Órulo — curadoria] @(Felipe Steberl) — [69a07c1fe344ac00135c907e](/2026-02) [confirmed]
- [Mensagens incluem últimos 4 dígitos do contato do corretor para instigar] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Usuário sem permissão recebe mensagem informando restrição e opção de solicitar acesso] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Editor não consegue alterar responsável — replica permissões da web] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Imobiliárias com exclusividade configuradas como leitoras, não editoras] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [E-mails planejados semanalmente compilando dados de visibilidade] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Título alterado para 'Acessos Recentes' para direcionar comunicação ao recente] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Redirect para web requer login automático para melhor fluidez] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Quantidade de corretores acessando aparece em destaque sem minimizar nomes] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Consulta limitada a 90 dias sem permitir usuário editar período inicialmente] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [CTA para incentivar contratação de plano avançado na aba audiência] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Tabela digital destacada com botão primário em vez de secundário] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Tipologias e características reordenadas para posição superior na tela] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Campos sem dados exibem tracinho para indicar possibilidade de preenchimento] @(Talita Campos) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Corretores não pagantes aparecem no final da listagem com menos destaque] @(Alejandro Olchik) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Sinalização visual de credibilidade para diferenciar pagantes de não pagantes] @(Alejandro Olchik) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Suporte para até dois contatos com interface de rotação] @(Neno Andrade) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Última atualização aparece junto ao preço para facilitar visualização] @(Alejandro Olchik) — [69a19c4b7ac8c80013e360e1](/2026-02) [confirmed]
- [Luan Felipe de Souza Assume posição de Closer na equipe] @(Diego Diehl) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Time revisar documento sobre funil de closet e trazer perspectivas] @(Time comercial) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Objetivo aumentar conversão de reunião para contrato de 16% para 18%] @(Diego Diehl) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Meta médio prazo: atingir conversão entre 20 a 30%] @(Diego Diehl) — [69a589c5e344ac00135cecc6](/2026-03) [likely]
- [BDRs participar ativamente dos convites para eventos] @(Time BDR) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Luiz fazer convite para evento de Capão da Canoa durante reunião de hoje] @(Luiz Gustavo Zanella) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Diego enviar datas dos eventos no grupo (Vitória, Curitiba, Porto Alegre, Capão da Canoa)] @(Diego Diehl) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Pedro marcar reunião com Felipe amanhã cedo para revisar aplicativo] @(Pedro Ruza Kneip Navarro) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Pedro enviar link do aplicativo para Gustavo testar] @(Pedro Ruza Kneip Navarro) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Pedro entrar no tldv para buscar reuniões gravadas e enviar link para Gustavo] @(Pedro Ruza Kneip Navarro) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Mirla enviar link da ferramenta Tic Tic para Jade] @(Mirla Menezes) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [João continuar usando vídeos em follow-up — resultados bons] @(João Vitor Portes da Silva) — [69a589c5e344ac00135cecc6](/2026-03) [confirmed]
- [Eduardo organizar reunião com Quinto Andar esta semana] @(Eduardo Stringhini) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Cobrar entre R$ 10 a R$ 15 por integração ativa mensalmente] @(Felipe Goettems + Eduardo Stringhini) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Marcelo rodar relatórios de dimensionalidade com tabela de preços 2026] @(Marcelo Rodrigues) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Marcelo começar reajuste de preços pelos clientes baratos e locais] @(Marcelo Rodrigues) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Felipe conversar com equipe financeira sobre cobrança de integrações] @(Felipe Goettems) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Eduardo conversar com imobiliárias sobre valor mínimo de integração] @(Eduardo Stringhini) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Diego apresentar OKRs para todo time segunda-feira] @(Diego Diehl) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Alejandro fazer reunião com Mari sobre gestão de demandas] @(Alejandro Olchik) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Alejandro continuar campanha de integrações ativas para desabilitar ou reativar] @(Alejandro Olchik) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Eduardo sugerir contratar pessoa sênior para estruturar processos por 6 meses] @(Eduardo Stringhini) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Alejandro prefere terceirização a contratação full time de RH] @(Alejandro Olchik) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Marcelo pesquisar mais empresas terceirizadas de RH] @(Marcelo Rodrigues) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Eduardo responder Mateus da Universal com postura fria e reconstruir relação] @(Eduardo Stringhini) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Diego mandar mensagem para pessoas que falaram sobre integração Universal] @(Diego Diehl) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Diego fazer alinhamento com João em Vitória amanhã] @(Diego Diehl) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Estratégia: focar em lançamentos e fortalecer canal de distribuição com Quinto Andar] @(Diego Diehl) — [69a5d01885c6ba0013e91d47](/2026-03) [confirmed]
- [Evento Panorama Litoral confirmado para 14 de maio em formato similar ao de Porto Alegre] @(Felipe Goettems + Ramiro Laurent) — [69a8812d22b1f60013518707](/2026-03) [confirmed]
- [Felipe enviar informações de unidades e VGV de Xangri-lá e Capão para Tiago e Rafael] @(Felipe Goettems) — [69a8812d22b1f60013518707](/2026-03) [confirmed]
- [Ramiro enviar planilha com dados de 70 edifícios de Capão e Vertical para Felipe] @(Ramiro Laurent) — [69a8812d22b1f60013518707](/2026-03) [confirmed]
- [Rafael enviar modelo de sondagem do mercado imobiliário para Ramiro avaliar aplicabilidade no litoral] @(Rafael Garcia) — [69a8812d22b1f60013518707](/2026-03) [confirmed]
- [Felipe e Tiago elaborarem Panorama 2025 e primeiro trimestre 2026 consolidado para o litoral] @(Felipe Goettems + Tiago Jung) — [69a8812d22b1f60013518707](/2026-03) [confirmed]
- [Rafael coordenar apresentações e formato do evento de 14 de maio com equipe] @(Rafael Garcia) — [69a8812d22b1f60013518707](/2026-03) [confirmed]
- [Ramiro levantar patrocínio com fornecedores para cobrir custos do evento] @(Ramiro Laurent) — [69a8812d22b1f60013518707](/2026-03) [confirmed]
- [Prefeito e secretario serão convidados para entender tamanho do mercado imobiliário] @(Ramiro Laurent) — [69a8812d22b1f60013518707](/2026-03) [confirmed]
- [Ramiro validar base de dados de incorporadoras e empreendimentos do litoral] @(Ramiro Laurent + Felipe Goettems) — [69a8812d22b1f60013518707](/2026-03) [confirmed]
- [Diego marcar reunião mais concentrada com Luan para conversa rica (adiada por viagem de Diego)] @(Diego Diehl) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [Luan começa treinamentos de produto na próxima semana (Z2 + contextos específicos)] @(Gustavo Torres) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [Luan começa a atender com acompanhamento na terceira semana (acompanhamento antes de solo)] @(Gustavo Torres) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [João trazer números quinzenais de reuniões realizadas (quinta a quinta) —guardião do reporting] @(João Vitor Portes) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [Gustavo ser guardião do método de reunião do closer — criar modelo de cadência] @(Gustavo Torres) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [Processo: closer deve ligar para Gustavo após reunião para reportar resultado] @(Diego Diehl) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [João preencher planilha de consolidação de vendas de fevereiro] @(João Vitor Portes) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [SDR responsible por preencher planilha após reunião do closer] @(Diego Diehl) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [Gustavo passar planilha para Jade e SDRs preencherem também] @(Gustavo Torres) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [Remover etapa 'Seguir Cadência' do CRM — etapa desnecessária] @(Diego Diehl) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [João revisar negociações quentes e remover etapas desnecessárias do CRM] @(João Vitor Portes) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [Diego liga de aeroporto para fechamento final (caso não resolvido antes)] @(Diego Diehl) — [69a9d2aaf0f6080013cc814b](/2026-03) [likely]
- [Gustavo colocar SW a Construções no grupo comercial] @(Gustavo Torres) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [Reunião Bitrix amanhã para ajustar funil e revisar campos] @(Diego Diehl) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [João testar processo de pedir indicação na próxima semana] @(João Vitor Portes) — [69a9d2aaf0f6080013cc814b](/2026-03) [confirmed]
- [Usar Stories em vez de e-mail marketing para não sobrecarregar corretores] @(Diego Diehl) — [69a9d2aaf0f6080013cc814b](/2026-03) [likely]
- [Fornecedor geral de vídeo vai enviar materiais para qualquer lugar do Brasil] @(Mayumi Takeda) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Calendário interno Orlando atualizado com datas organizadas e cidades confirmadas] @(Mayumi Takeda) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Mayumi revisar apresentação comercial e validar estrutura com Diego] @(Mayumi Takeda + Diego Diehl) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Marketing deve ser específico nas demandas para execução mais rápida] @(Diego Diehl) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Estratégia deve focar em conteúdo específico por praça, não generalista] @(Mayumi Takeda) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Diego atualizar linhas do funil comercial com dados de clientes] @(Diego Diehl) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Diego trazer proposta de vídeo com Júnior para evento Curitiba] @(Diego Diehl) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Diego criar grupo para organizar conversas sobre eventos] @(Diego Diehl) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Mayumi enviar vídeo do evento Curitiba para compartilhar comercialmente] @(Mayumi Takeda) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Closers devem postar Stories com prints de reuniões com incorporadoras] @(Diego Diehl) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Diego definir tema de apresentação para corretores no congresso] @(Diego Diehl) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Gustavo apresentar alavancas e gatilhos para Mayumi construir conteúdo] @(Gustavo Torres) — [69aac1ccd537b40013ab1c27](/2026-03) [confirmed]
- [Gustavo agendar reuniões com Luan para formação e execução de apresentações de Closer] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Gustavo estabelecer meta de duas reuniões de Closer por semana] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Gustavo杭周二和周五上午处理CRM e atualizar CRM] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Trabalhar base de Porto Alegre a partir do dia 15 com validação de contatos] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Gustavo baixar base de usuários de Incorporadora em POA com último acesso em janeiro] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Gustavo fazer disparo via Meta para convidar diretores e donos ao evento em POA] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Gustavo ligar para prospects de POA e Capão da Canoa para qualificar participação] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Limitar duas pessoas por Incorporadora no evento com presença obrigatória de gestão] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Fazer disparo em grupo com ligações simultâneas para aumentar taxa de conversão] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Gustavo杭做ligações junto com time para demonstrar na prática] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Gustavo杭limpar base de contatos desativados e pedir validação ao João] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Gustavo杭garantir que gerente de parcerias participe das primeiras reuniões com incorporadoras] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [Gustavo杭posicionar projetos por dia da semana para melhor execução] @(Gustavo Torres) — [69ab191ceef3be0013324da1](/2026-03) [confirmed]
- [João gravar apresentação do zero para cronometrar duração e ajustar conteúdo] @(João Vitor Portes da Silva) — [69b0722b4519e900135b07f9](/2026-03) [confirmed]
- [Hotsite liberado via e-mail após corretor enviar comprovante de ação (5 indicações ou stories)] @(João Vitor Portes da Silva + Diego Diehl) — [69b0722b4519e900135b07f9](/2026-03) [confirmed]
- [João enviar apresentação atualizada para Diego revisar após finalizações] @(João Vitor Portes da Silva) — [69b0722b4519e900135b07f9](/2026-03) [confirmed]
- [Diego comprar passagem aérea de João para João Pessoa antecipadamente] @(Diego Diehl) — [69b0722b4519e900135b07f9](/2026-03) [confirmed]
- [João viajar para João Pessoa de 4 a 8 de maio para reuniões e fechamentos] @(João Vitor Portes da Silva) — [69b0722b4519e900135b07f9](/2026-03) [confirmed]
- [João registrar novo cliente Dantas e Lira no consolidado de vendas] @(João Vitor Portes da Silva) — [69b0722b4519e900135b07f9](/2026-03) [confirmed]
- [João enviar solicitação de pagamento de R$ 500 para café da manhã em Florianópolis para Mayumi com cópia para Diego] @(João Vitor Portes da Silva) — [69b0722b4519e900135b07f9](/2026-03) [confirmed]
- [Diego e João organizar café da manhã em João Pessoa com Ester] @(Diego Diehl + João Vitor Portes da Silva) — [69b0722b4519e900135b07f9](/2026-03) [confirmed]
- [João reconhecido como potencial sócio-local de Florianópolis para expansão regional] @(Diego Diehl) — [69b0722b4519e900135b07f9](/2026-03) [confirmed]
- [Diego enviar apresentação dos workstreams para o time via WhatsApp] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [Diego consolidar feedbacks da reunião e ajustar redação final de cada KR até meio-dia] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [Time enviar áudio ou mensagem com feedback sobre estratégia até meio-dia] @(Time comercial) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [Diego definir claramente o que é embaixador e outras definições de termos-chave] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [Diego fechar os donos de apoio por frente de trabalho] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [WS1: Comunicação com corretores — Ester responsável] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [WS3: Execução territorial com fórmula de lançamento — eventos e embaixadores] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [WS4: Estrutura comercial — amadurecer indicadores e automações] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [WS5: Marketing direcionado por eventos em ciclos conforme execução] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [WS2: Jornada DL pago — cadastro até compra para incorporadoras] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [WS6: Programa de embaixadores com incorporadoras como aposta para crescimento] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [WS7: Modelo econômico por praça — receita para sustentar operações locais] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [João responsável por sucesso estratégico e tracionamento de embaixadores] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [Time dedicar 10% do tempo a projetos fora da zona de atuação padrão] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [Cadência operacional quinzenal por praça para abordar novos usuários de incorporadoras] @(Diego Diehl) — [69b159356fac13001319c488](/2026-03) [confirmed]
- [Evento Porto Alegre 14/04 e Capão da Canoa 16/04 — 200 contatos de líderes de incorporadoras em POA] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Dois blocos de acionamento planejados: 1º de Abril (ou 6) e outro na semana seguinte] @(Gustavo Torres) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Anúncio deve direcionar para WhatsApp de BDR específico, não para link do Simba] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Centralizar acionamento em um BDR permite mensuração e evita variações] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Gustavo conectar WhatsApp do time de BDR à plataforma Z2] @(Gustavo Torres) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Time de BDR precisa ser treinado para usar funcionalidades da Z2 (automação, detecção de diálogos quentes, auditoria)] @(Gustavo Torres) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Funil BDR = 'Corp-BR-BDR', Funil Closer = 'Corp-BR-Closer'] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Nela terá acesso a ambos funis de BDR e Closer para gerenciar negócios] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Não criar funis separados para Z2A e CDA — usar filtros e nomenclatura em cards] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Após assinatura: enviar mensagem de parabenização → avisar CS → celebrar com coordenador e marketing → enviar para financeiro] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Etapas principais do funil: Descoberta realizada, Jornada em andamento, Negociação, Fechamento, Contrato assinado] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Diego criar funil para CRI seguindo modelo do Closer] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Diego cobrar Felipe para preencher RM a partir de reunião realizada] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Remover 'Obter dados' como etapa — transformar em tarefa automática] @(Gustavo Torres) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Acompanhamento semanal: rastrear pessoas acionadas, convites enviados, cadastros realizados] @(Gustavo Torres) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Proposta de escopo necessária para apresentar valores sem ser proposta comercial completa] @(Diego Diehl) — [69b1bd08c1e9ee0013779ffa](/2026-03) [confirmed]
- [Porto Camargo utiliza modelo SCP para todos empreendimentos — 100% dinheiro investidores] @(Porto Camargo) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [CRI pode ser emitido em 15 dias com documentos prontos (prazo comercial 30 dias)] @(Porto Camargo) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Setup CRI custa 60k (pode aumentar para 100k em breve)] @(Porto Camargo) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Securitizadora cobra 2-4% da economia gerada pelo CRI] @(Porto Camargo) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Custo total estimado em 100k ao longo de 3 anos (incluindo carry 1.2k-1.5k/mês)] @(Porto Camargo) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Porto Camargo tem bancarizador in-house e acordo de bancarização] @(Porto Camargo) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [CFG é securitizadora que emitiu 5a maior quantidade de CRIs no ano passado] @(Felipe Goettems) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [CRI pode ser estruturado para evitar que dívida apareça formalmente no balanço] @(Felipe Goettems) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [CRI isenta ganho de capital do terrenista — margem de 10% no terreno] @(Felipe Goettems) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Processo: análise de contrato, assinatura em 30 dias, emissão e captação] @(Porto Camargo + Felipe) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Porto Camargo agenda próxima reunião com contador e advogado da empresa] @(Porto Camargo (Rodrigo)) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Diego enviar convite do evento em Curitiba para Porto Camargo] @(Diego Diehl) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Diego e Felipe reunião presencial em Curitiba com advogado de Porto Camargo] @(Diego Diehl + Felipe Goettems) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Diego e Felipe enviam modelo de contrato para Porto Camargo analisar] @(Diego Diehl + Felipe Goettems) — [69b2f1112c298800128eafa1](/2026-03) [confirmed]
- [Meta de Ester: 20 solicitações de integração de CRM por mês] @(Ester Elisa de Souza Rodrigues) — [69b3ffb54270ef0013147a6a](/2026-03) [confirmed]
- [Priorizar imobiliárias estruturadas para gerar mais corretores na plataforma] @(Ester Elisa de Souza Rodrigues) — [69b3ffb54270ef0013147a6a](/2026-03) [confirmed]
- [Objetivo aumentar integrações ativas em 50% — totalizando 60 por mês] @(Ester Elisa de Souza Rodrigues + Diego Diehl) — [69b3ffb54270ef0013147a6a](/2026-03) [confirmed]
- [Ester contatar 40 integrações inativas em João Pessoa e documentar motivos] @(Ester Elisa de Souza Rodrigues) — [69b3ffb54270ef0013147a6a](/2026-03) [confirmed]
- [MVP: testar envolvimento de BDR com corretores em Capão da Canoa] @(Gustavo Torres + Diego Diehl) — [69b3ffb54270ef0013147a6a](/2026-03) [likely]
- [Ester mapear 5 a 10 integrações inativas para entender causas em escala] @(Ester Elisa de Souza Rodrigues) — [69b3ffb54270ef0013147a6a](/2026-03) [confirmed]
- [Diego enviar link da planilha de integrações inativas para Ester] @(Diego Diehl) — [69b3ffb54270ef0013147a6a](/2026-03) [confirmed]
- [Aproximar Bruno da Remax para conversa sobre integração] @(Ester Elisa de Souza Rodrigues) — [69b3ffb54270ef0013147a6a](/2026-03) [confirmed]
- [Knight fechou parceria — accelerating confirmed] @(Knight) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Próxima reunião deve incluir advogado imobiliário do cliente] @(Diego Diehl) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Evento interno em São Paulo com Paulo — estratégia para trazer donos] @(Diego Diehl + Paulo Deitos) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [GC Engenharia não avançou apesar de reunião presencial com dois consultores] @(GC Engenharia) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Constrói pode indicar advogados de outro escritório] @(Constrói) — [69b44bbf7314d6001379cf1c](/2026-03) [likely]
- [E-mail para base de incorporadoras pode gerar leads qualificados] @(Diego Diehl) — [69b44bbf7314d6001379cf1c](/2026-03) [likely]
- [RD Station foi referência de canal de parcerias bem-sucedidas] @(Diego Diehl) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Remuneração com Alessandra precisa ser discutida] @(Diego Diehl + Alessandra) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Funil avançou de 18 para 32 incorporadores em reunião realizada] @(Felipe Goettems) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Gustavo está aprendendo operação para desdobrar funil] @(Gustavo Torres) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Inicializados aumentaram de 20 para 27 incorporadores] @(Felipe Goettems) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Terracota está próximo de Laguna e pode fazer ponte] @(Diego Diehl) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Coral Zanella entrou recentemente na carteira] @(Felipe Goettems) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Boa Vista tem Daniel como dono e confirmou presença no evento] @(Daniel (Boa Vista)) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Quest tem coordenadores enrolados e Bruno não repassa informações] @(Bruno (Quest)) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Marco da R2 não responde — pode ser deixado de lado] @(Marco (R2)) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Luciano xingou e situação é difícil de resolver] @(Luciano) — [69b44bbf7314d6001379cf1c](/2026-03) [confirmed]
- [Equipe aprova liberação de duas posições para CS] @(Diego Diehl + diretoria) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Marcelo preparar documento de KRs ao longo dessa semana] @(Marcelo Rodrigues) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Alejandro propõe eliminar KR3 e focar em fluxo de pagamento e qualidade] @(Alejandro Olchik) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Felipe cobrar Z2 sobre implantações não faturadas] @(Felipe Goettems) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Eduardo questionar Bruno sobre preço mínimo de integração] @(Eduardo Stringhini) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Diego enviar página de captação de investidor para assinatura do Junior] @(Diego Diehl) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Felipe e Alejandro reunir com Mayumi e Nemo sobre estratégia de divulgação White Label] @(Felipe Goettems + Alejandro Olchik) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Necessário reunião específica sobre projeto de embaixadores e GD] @(Diego Diehl) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Eduardo enviou e-mail para Junior pedindo assinatura da lista de funcionalidades] @(Eduardo Stringhini) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Testar preço de integração com novos clientes primeiro, depois expandir para existentes] @(Felipe Goettems) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Meta é 15 embaixadores no ano, começando mais devagar] @(Diego Diehl) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Eduardo propõe pessoa dedicada para suportar embaixadores com foco em vendas] @(Eduardo Stringhini) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Indicadores devem focar em críticos: atualização, integrações e qualidade] @(Marcelo Rodrigues) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Marcelo adicionar tag 'atrito' nos KRs para rastrear resolução até fim do ano] @(Marcelo Rodrigues) — [69b845174ddb450012bb9140](/2026-03) [confirmed]
- [Diego encaminhar material sobre CVM 88 para Sergio estudar e aprofundar conhecimento] @(Diego Diehl) — [69bbe54c50d24b001394c612](/2026-03) [confirmed]
- [Paulo falar com Guto para avaliar possibilidade de estruturar operação de 25 milhões em equity (Campinas)] @(Paulo Deitos) — [69bbe54c50d24b001394c612](/2026-03) [confirmed]
- [Paulo enviar nome de estruturador para cliente de Campinas validar e iniciar processo] @(Paulo Deitos) — [69bbe54c50d24b001394c612](/2026-03) [confirmed]
- [Retomar conversa em abril sobre carteira de loteador do interior de São Paulo] @(Paulo Deitos + Diego Diehl) — [69bbe54c50d24b001394c612](/2026-03) [confirmed]
- [CVM 88 permite eliminar seis players do processo usando tecnologia — de seis meses para dez dias] @(Paulo Deitos) — [69bbe54c50d24b001394c612](/2026-03) [confirmed]
- [Limite atual de 15 milhões por estrutura aumentará para 75-100 milhões em 2027] @(Paulo Deitos) — [69bbe54c50d24b001394c612](/2026-03) [confirmed]
- [CRI resolve dor latente de incorporadores pequenos sem balanço para acessar financiamento bancário] @(Paulo Deitos) — [69bbe54c50d24b001394c612](/2026-03) [confirmed]
- [Somatos: zero para 2,7 vendas mensais após consultoria de agosto a novembro] @(Felipe Goettems + Rodrigo Capp) — [69bbe54c50d24b001394c612](/2026-03) [confirmed]
- [Ester ligar para 8 corretores de outubro que não responderam — fechar amostra de follow-up] @(Ester Elisa de Souza Rodrigues) — [69bd3dc6afb4b00013f63364](/2026-03) [confirmed]
- [Ester desenvolver e testar mensagem assertiva de reativação antes de programar disparo em massa] @(Ester Elisa de Souza Rodrigues) — [69bd3dc6afb4b00013f63364](/2026-03) [confirmed]
- [João configurar disparo de mensagem para segunda-feira com foco em lançamentos] @(João Vitor Portes da Silva) — [69bd3dc6afb4b00013f63364](/2026-03) [confirmed]
- [Diego e João testam disparos na terça e quinta para medir reativação de usuários — experimento controlado] @(Diego Diehl + João Vitor Portes) — [69bd3dc6afb4b00013f63364](/2026-03) [confirmed]
- [Continuar focando em integração de CRM para aumentar base em João Pessoa] @(Ester + João) — [69bd3dc6afb4b00013f63364](/2026-03) [confirmed]
- [Bruno verificar status da integração Vivalista com Órulo (dois casos pendentes)] @(Ester Elisa de Souza Rodrigues + Bruno) — [69bd3dc6afb4b00013f63364](/2026-03) [likely]
- [Imobmeet desenvolver funcionalidade de exportação PDF/Excel de tabela de vendas] @(Gleybiony Camargo) — [69bd9ef06a28e60013c3eb61](/2026-03) [confirmed]
- [Marcelo enviar documentação detalhada de integração por e-mail com links pré-direcionados] @(Marcelo Rodrigues) — [69bd9ef06a28e60013c3eb61](/2026-03) [confirmed]
- [Marcelo fornecer token de acesso e credenciais para testes da API] @(Marcelo Rodrigues) — [69bd9ef06a28e60013c3eb61](/2026-03) [confirmed]
- [Gleybiony adicionar campo de observações na criação de novas tabelas de vendas] @(Gleybiony Camargo) — [69bd9ef06a28e60013c3eb61](/2026-03) [confirmed]
- [Diego passar contato comercial de Gleybiony para primeiros clientes das capitais] @(Diego Diehl) — [69bd9ef06a28e60013c3eb61](/2026-03) [confirmed]
- [Integração via webhook (tempo real) ou rotinas diárias agendadas] @(Marcelo Rodrigues) — [69bd9ef06a28e60013c3eb61](/2026-03) [confirmed]
- [Incorporadoras podem selecionar quais status de unidades enviar para integração] @(Gleybiony Camargo) — [69bd9ef06a28e60013c3eb61](/2026-03) [confirmed]
- [Gleybiony compartilhar exemplos de layouts de tabelas de vendas com Marcelo] @(Gleybiony Camargo) — [69bd9ef06a28e60013c3eb61](/2026-03) [confirmed]
- [Felipe enviar cálculo detalhado sobre benefício tributário de locação via CRI para Daniel] @(Felipe Goettems) — [69be9d49c1f67b0013e5fa4c](/2026-03) [confirmed]
- [Felipe enviar desenho técnico da estrutura de CRI para Daniel] @(Felipe Goettems) — [69be9d49c1f67b0013e5fa4c](/2026-03) [confirmed]
- [Felipe realizar simulação de produtos com informações do Sublime e propriedade para locação] @(Felipe Goettems) — [69be9d49c1f67b0013e5fa4c](/2026-03) [confirmed]
- [Daniel fornecer informações de VGV médio e tabela de vendas para simulação] @(Daniel Ribas) — [69be9d49c1f67b0013e5fa4c](/2026-03) [confirmed]
- [CRI na regulação 88 para terrenista do Sublime pode reduzir ganho de capital em 600k] @(Felipe Goettems) — [69be9d49c1f67b0013e5fa4c](/2026-03) [confirmed]
- [Daniel explorar opção de 60 meses pós-obra com fundos (Finova/Faria Lima)] @(Daniel Ribas) — [69be9d49c1f67b0013e5fa4c](/2026-03) [confirmed]
- [Guilherme marcar reunião com Rafael e Décio (sócios) para discutir estrutura financeira e administrativa] @(Guilherme Mendes) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [Felipe simular cenários financeiros com VGB 350M e margem 20%] @(Felipe Goettems) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [Diego e Guilherme agendar próxima reunião para segunda-feira da semana seguinte] @(Diego Diehl + Guilherme Mendes) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [Guilherme falar com Nágila e Edésio sobre próximos passos da estruturação] @(Guilherme Mendes) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [CRI oferece vantagem fiscal comparado a SCP para retorno de investimento] @(Felipe Goettems) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [Incorporadora parceira tem 697 unidades entregues e 300M em entregas —validação de track record] @(Guilherme Mendes) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [Pesquisa Data Store + Prospecta validou localização, público-alvo e modelo de negócio] @(Guilherme Mendes) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [Empreendimento de 100M vendido em 2 dias — validação de demanda forte] @(Guilherme Mendes) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [Investidor PF é isento de IR sobre ganho de capital ao revender] @(Felipe Goettems) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [Empreendedor pode reduzir tributação em 10% usando PF em vez de PJ na obra] @(Felipe Goettems) — [69c3dc5fdbc75500136ae2e6](/2026-03) [confirmed]
- [Victor enviar apresentação em slides sobre implementações por departamento para Órulo] @(Victor Baggio) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Diego e Marcelo definir priorização de projetos com base em ROI estimado] @(Diego Diehl + Marcelo Rodrigues) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Projetos com retorno imediato e concreto têm prioridade sobre melhorias de longo prazo] @(Diego Diehl) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Processo vem antes da automação — primeiro validar na mão, depois automatizar] @(Diego Diehl + Victor Baggio) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Modelos SaaS de automação funcionam melhor quando processo já está validado] — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Playbook Lab opera com Squad dedicada de 3 pessoas alocadas junto ao cliente] @(Victor Baggio) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Pacotes de horas mensais variáveis — velocidade de entrega proporcional ao investimento] @(Victor Baggio) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Sem contrato de longo prazo — cancelamento possível a qualquer momento] @(Victor Baggio) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Victor enviar estimativas de tempo mínimo de implementação por projeto] @(Victor Baggio) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [N8N permite integração com sistemas internos da Órulo via webhooks e APIs] @(Victor Baggio) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Eficiência operacional: transformar 3 SDRs em 6 sem contratar novos funcionários] @(Diego Diehl) — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [WhatsApp oficial necessário para disparos em massa (~R$ 400 por número)] — [69c53bda89dd4d0013feab19](/2026-03) [confirmed]
- [Treinar BDRs em IA no dia a dia antes de investir em automação outbound] @(Diego Diehl) — [69c53bda89dd4d0013feab19](/2026-03) [likely]
- [Contratos workshop salvos com nomenclatura padrão 'combo workshop'] @(Diego Diehl) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Gustavo ajustar contrato MDI conforme modelo padrão definido] @(Gustavo Torres) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Modelo de cobrança Closer: pro rata do dia de assinatura até data de vencimento mensal] @(Diego Diehl) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Faturamento deve ser emitido no CNPJ da Incorporadora para evitar alterações] @(Diego Diehl) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Dividir por SPA apenas se cliente solicitar — não oferecer como padrão] @(Diego Diehl) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Estado deve aparecer no título do contrato e no card de visualização] @(João Vitor Portes da Silva) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Primeira cobrança será junto com primeira mensalidade no segundo mês] @(Diego Diehl) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Cláusula padrão para workshop: plataforma disponibilizada a partir da assinatura] @(Diego Diehl) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [João atualizar proposta e enviar para Salazar com novo valor acordado] @(João Vitor Portes da Silva) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [João integrar tldv no sistema de CRM e Beatles com contexto GPT] @(João Vitor Portes da Silva) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Diego validar cláusula de contrato com Bia e confirmar padrão para workshop] @(Diego Diehl) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Diego enviar proposta para Salazar com valor de R$ 1.897 até 31 de março] @(Diego Diehl) — [69c58224f2dd940013643f4d](/2026-03) [confirmed]
- [Vinícius chamar João hoje para configurar acesso à plataforma Salve para receber SMS] @(Vinícius + João Vitor Portes da Silva) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [João configurar número da Ester na Z2 hoje] @(João Vitor Portes da Silva) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [Diego e João revisar plugin Chrome para organização de contatos WhatsApp] @(Diego Diehl + João Vitor Portes da Silva) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [Ester continuar ligações para corretores de João Pessoa focando em integrações inativas] @(Ester Elisa de Souza Rodrigues) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [Acompanhar integrações inativas e fazer follow-up em abril conforme combinado] @(Ester Elisa de Souza Rodrigues) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [João Pessoa virar praça de DM para DL em maio com oferta de cliente pagante] @(Diego Diehl + João Vitor Portes da Silva) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [João comprar passagem para João Pessoa em maio para aproximação com incorporadoras] @(João Vitor Portes da Silva) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [Evento em Goiânia marcado para 27 de maio com foco em incorporadoras] @(Diego Diehl) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [Ester trazer planejamento de Goiânia segunda-feira com cronograma de ações para dois meses] @(Ester Elisa de Souza Rodrigues) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [Importar base de Goiânia na Z2 com segmentação por data de cadastro] @(Ester Elisa de Souza Rodrigues) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [Replicar estratégia bem-sucedida de João Pessoa em Goiânia] @(Diego Diehl + Ester Elisa de Souza Rodrigues) — [69c674b5602e260013bbd14c](/2026-03) [confirmed]
- [Três frentes de acionamento definidas: marketing por e-mail, ligações e mensagens S10] @(Diego Diehl + Gustavo Torres + Mayumi Takeda) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Mayumi enviar link do Sympla e materiais dos cards segunda-feira] @(Mayumi Takeda) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Tema da palestra será mantido para primeira rodada em todas as cidades] @(Diego Diehl + Mayumi Takeda) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Porto Alegre e Capão da Canoa são cidades prioritárias para eventos] @(Diego Diehl) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Gustavo centralizar base de acionamento em Excel com etapas e responsáveis] @(Gustavo Torres) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Diego revisar apresentação do Pit e enviar feedback até primeiro de abril] @(Diego Diehl) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Diego agendar reunião para gravar vídeo de sucesso do evento] @(Diego Diehl) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Diego gravará conteúdos no escritório de Alphaville terça e quinta presencialmente] @(Diego Diehl) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Mayumi organizar gravação de vídeo com Ellen sobre evento] @(Mayumi Takeda) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Duas linhas de materiais: educação/ativação e ferramentas para validação estratégica] @(Diego Diehl) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Gustavo finalizar documento de materiais com comentários do Diego até terça-feira] @(Gustavo Torres) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Jantar em Porto Alegre focado em Criptografia com incorporadores em abril] @(Diego Diehl) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Proposta de pré-proposta personalizada por incorporadora sem valores] @(Diego Diehl) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Processo de follow-up após um mês de contratação para abordar Criptografia] @(Diego Diehl) — [69c67bbe0da323001305d36e](/2026-03) [confirmed]
- [Patamar mínimo mensal é 20k com 2.5k por sócio local] @(Diego Diehl) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Meta anual aproximadamente 250k em receita] @(Diego Diehl) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Se meta atingida na sexta, time emenda segunda e terça de feriado] @(Diego Diehl) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Gustavo realizar migração de cards do CRM local para fundo de executivo de contas] @(Gustavo Torres) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Felipe transferir dados de PDR no CRM para melhor organização] @(Felipe) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [João ligar para Salazar sobre proposta de 50% até sexta-feira] @(João Vitor Portes da Silva) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Não closetizar vendas pequenas para não confundir — foco em S10 ou closers] @(Diego Diehl) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Diego marcar reunião de 15 minutos sobre disciplina comercial] @(Diego Diehl) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Vitória agendar reunião com Marcelo para revisar clientes e próximos passos] @(Luiz Gustavo Zanella + Marcelo) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Janela postar material sobre evento em Instagram e Stories] @(Luiz Gustavo Zanella) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Treinamento final de mês: quarta-feira às 10h56] @(Diego Diehl) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Sócios locais devem fazer contato pessoal com novas incorporadoras na praça] @(Luiz Gustavo Zanella + socios locais) — [69ca73c524b2440013ebe436](/2026-03) [confirmed]
- [Marcelo repor pessoa removida da atualização no início de abril] @(Marcelo Rodrigues) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Marcelo iniciar processo seletivo para contratar substituto em automações] @(Marcelo Rodrigues) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Diego apresentar proposta do playbook na próxima semana para decisão] @(Diego Diehl) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Diego atualizar planilha de faturamento quando virar o mês] @(Diego Diehl) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Marcelo rodar teste para relatório de reajuste sair automaticamente] @(Marcelo Rodrigues) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Diego conectar marketing e CS no projeto de embaixadores] @(Diego Diehl) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Eduardo pegar sala para reunião de diretoria no dia 13 às 14h] @(Eduardo Stringhini) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Relatório de causas de não fechamento de integrações pronto até segunda] @(Marcelo Rodrigues) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Diego se encontrar com Z2 na quarta para resolver pendências] @(Diego Diehl) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Diego trazer lista de atividades do programa de embaixadores para quarta] @(Diego Diehl) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Diego definir estratégia para receber 50 mil de implantações da Z2] @(Diego Diehl) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Diego negocia 20% adicional para pagar sócio local em novas praças] @(Diego Diehl) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Cobrança de valor simbólico em integrações está sendo encaminhada com Bruno] @(Felipe Goettems) — [69caba140da323001306119a](/2026-03) [confirmed]
- [Modelo GD Curitiba: 2.500 reais base para dois empreendimentos] @(Diego Diehl + Eduardo Stringhini + Guilherme) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Topo de funil fica com imobiliária, qualificação e visita com GD Curitiba] @(Guilherme) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Estudo de mercado na implantação diferencia proposta e reforça mística local] @(Guilherme) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Combo promocional: 2 empreendimentos por 2 mil reais até 10 de abril] @(Diego Diehl) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Eduardo revisar e finalizar apresentação, ajustando modelo de Porto Alegre e percentuais corretos] @(Eduardo Stringhini) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Tabela promocional de ativação para clientes novos] @(Eduardo Stringhini + Diego Diehl) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Eduardo e Diego alinharem justificativa dos 14% de faturamento ou negociar com Guilherme] @(Eduardo Stringhini + Diego Diehl) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Guilherme e Eduardo alinharem modelo de remuneração com Zanella para evitar conflitos] @(Guilherme + Eduardo Stringhini) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Eduardo e Diego estruturarem proposta de parceria contratual direta com incorporadoras] @(Eduardo Stringhini + Diego Diehl) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Guilherme plan

Expandir para outras praças se modelo validar em seis meses] @(Guilherme) — [69cc20acddea5b00135fdc45](/2026-03) [likely]
- [Incorporadora paga mensalidade de DA separadamente do percentual de faturamento] — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Rafael da RR descartado por tentar negociar preço e comportamento problemático] @(Guilherme) — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Zanella é sócio local, visita imobiliárias e vende exclusividade com remuneração por faturamento] — [69cc20acddea5b00135fdc45](/2026-03) [confirmed]
- [Funil PDR = conscientização para incorporadoras que não conhecem plataforma. Funil AE = incorporadoras que já conhecem e têm consciência] @(Gustavo Torres + Diego Diehl) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Pré-proposta deve explicar lógica de funcionamento sem valores monetários] @(Gustavo Torres + Diego Diehl) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Proposta oficial com valores enviada apenas quando cliente valida estrategicamente] @(Diego Diehl) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Vendedor deve conduzir processo e não deixar cliente pedir proposta prematuramente] @(Diego Diehl) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Feedback do closer após reunião deve ser registrado no card do BDR e do closer] @(Diego Diehl) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Diego conversar com Luiz após treinamento para definir processo de sócio local] @(Diego Diehl + Luiz Gustavo Zanella) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Gustavo preparar modelo de pré-proposta sem valores com Mayumi para validação estratégica] @(Gustavo Torres + Mayumi Takeda) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Time de Marcelo terá duas pessoas dedicadas exclusivamente a automações] @(Marcelo Rodrigues) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Luiz operar novo modelo de funil BDR por duas a três semanas antes de decisões finais] @(Luiz Gustavo Zanella) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Transferência de cards entre funis é possível sem criar novo card] @(Gustavo Torres) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Proposta deve demonstrar ROI esperado em vendas geradas versus investimento] @(Diego Diehl) — [69cd08ba5339450013b8fd72](/2026-04) [confirmed]
- [Raphael e Américo vão testar caso concreto com incorporador que precisa de R$ 2-3 milhões para estruturar via CRI] @(Raphael Bueno + Américo) — [69ce765eddea5b001360288d](/2026-04) [confirmed]
- [Raphael conversar com incorporador sobre alternativas de custo para equalizar estrutura] @(Raphael Bueno) — [69ce765eddea5b001360288d](/2026-04) [confirmed]
- [Raphael apresentar proposta alternativa ao incorporador e desenhar solução flexível] @(Raphael Bueno) — [69ce765eddea5b001360288d](/2026-04) [confirmed]
- [Paulo oferece flexibilidade nas regras de CRI conforme necessidade do negócio] @(Paulo Deitos) — [69ce765eddea5b001360288d](/2026-04) [confirmed]
- [Paulo pode distribuir fundos imobiliários no próximo ano via plataforma própria] @(Paulo Deitos) — [69ce765eddea5b001360288d](/2026-04) [likely]
- [CRI simples é melhor quando já existe cheque dentro de casa] — [69ce765eddea5b001360288d](/2026-04) [confirmed]
- [CRI revolvente é mais apropriado para operações pequenas e recorrentes] — [69ce765eddea5b001360288d](/2026-04) [confirmed]
- [Fundo imobiliário vale a pena apenas com atração significativa de originação] — [69ce765eddea5b001360288d](/2026-04) [confirmed]
- [CRI pode ser estruturado com fluxos de pagamento vinculados a vendas do empreendimento] @(Paulo Deitos) — [69ce765eddea5b001360288d](/2026-04) [confirmed]
- [Unitas e Orion formam parceria de originação com Paulo Deitos] @(Raphael Bueno + Diego Diehl + Felipe Goettems + Paulo Deitos) — [69ce765eddea5b001360288d](/2026-04) [confirmed]
- [Closers sendo renomeados para executivos de contas formalmente] @(Diego Diehl) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [Gustavo responsável por prospectação para preencher funil dos executivos] @(Diego Diehl) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [Luan treinar envio de contratos com João para dominar o processo] @(Luan Felipe de Souza + João Vitor Portes da Silva) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [Luan marcar reunião com João para explicar programa de embaixadores] @(Luan Felipe de Souza) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [Diego estruturar programa de embaixadores com Marcelo e enviar email] @(Diego Diehl + Marcelo Rodrigues) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [João preencher campos de estado e empresa antes de enviar contratos] @(João Vitor Portes da Silva) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [Roni organizar acesso Stories e contato com marketing para Floripa] @(Roni) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [João mudou narrativa com cliente Z2 focando em prática não teoria] @(João Vitor Portes da Silva) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [Diego dedicar uma semana desenvolvendo dashboards e corrigindo problemas de dados] @(Diego Diehl) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [Luan praticar digitação diariamente usando ferramenta de treinamento] @(Luan Felipe de Souza) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [Modelo de sócio local proposto para Recife com embaixador indicando clientes] @(Diego Diehl) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [João viajar para João Pessoa evento dias 5 ou 6 de maio] @(João Vitor Portes da Silva) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
- [Diego viajar domingo ou segunda para aproveitar semana inteira] @(Diego Diehl) — [69cebf017c8d0800136e9e57](/2026-04) [confirmed]
