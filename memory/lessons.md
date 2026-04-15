# lessons.md — Aprendizados

---

## 🔑 Sessão: Formato Mobile + Participantes WS + One-Pager Vitória
*Data: 2026-03-17 a 20/03 | Sessão: Retorno de Curitiba*

### 1. MORFEU PODE QUEBRAR SUAS PRÓPRIAS REGRAS NA MESMA MENSAGEM
- A regra "sem tabelas Markdown no Telegram" foi estabelecida e explicada — na mesma mensagem, Morfeu usou uma tabela para resumir o que foi feito.
- Diego flagrou imediatamente.
- **Regra aprendida:** Após criar uma regra de formato, aplicar na mesma resposta. Nunca usar formato proibido para anunciar que o formato está proibido. Auto-verificar antes de enviar.

### 2. GOOGLE DOCS NÃO PODE SER SUBSTITUÍDO VIA gog CLI
- `gog drive upload --replace` não funciona para arquivos `application/vnd.google-apps.document`.
- Solução: `gog docs create --file markdown.txt --parent <folderID>` cria novo doc a partir de Markdown. Arquivar o antigo manualmente.
- **Regra aprendida:** Para atualizar Google Docs via CLI: criar V+1 e arquivar Vn. Nunca tentar `--replace` em Google Workspace files.

### 3. sessions_send EXIGE sessionKey ou label — agentId não basta
- Ao tentar rotear para Larissa via `sessions_send(agentId="larissa")`, retornou erro: "Either sessionKey or label is required".
- Solução: usar `gog-larissa` diretamente para executar ações externas (envio de e-mails) em nome de Larissa.
- **Regra aprendida:** Para acionar Larissa, usar `gog-larissa` diretamente. sessions_send só funciona com sessionKey ativo ou label configurado.

### 4. ONE-PAGER DE SPRINT TEM DUAS FUNÇÕES NO MESMO DOCUMENTO
- O One-Pager de Kneip (Vitória) condensou: (a) retrospectiva do Sprint 01 e (b) planejamento do Sprint 02.
- É o formato correto e eficiente — um único artefato fecha o sprint anterior e abre o próximo.
- **Regra aprendida:** Ao analisar One-Pager, sempre separar claramente a seção retrospectiva (passado) da seção de planejamento (próximo sprint). Atualizar projects_orulo.md com C1/C2/C3 do próximo sprint.

---

## 🔑 Sessão: Estabilização de Rotinas + Sprint 02 das Praças
*Data: 2026-03-16 | Sessão: Dia de viagem para Curitiba + operação*

### 1. ROTINA SEM FONTE DE DADOS CONFIÁVEL É RUÍDO, NÃO VALOR
- Daily Briefing com 50% de falha e pending.md inconsistente → briefing de baixa qualidade é pior que nenhum briefing
- Scan Praças Weekly alertando toda semana para o mesmo problema estrutural não resolvido → alerta constante = ruído
- **Regra aprendida:** Antes de ativar qualquer rotina automatizada, garantir que a fonte de dados que ela consome está estável e confiável. Rotina sem dado é automação de ruído.

### 2. ONE-PAGER DE SPRINT ≠ RELATÓRIO DE SPRINT
- Zanella enviou um excelente plano de execução para o evento de Curitiba
- Porém o que a governança exige é o **relatório do sprint encerrado** (resultados, evidências, aprendizados)
- São documentos distintos com propósitos opostos: um olha para frente, o outro presta contas para trás
- **Regra aprendida:** Clarificar explicitamente qual documento é esperado ao cobrar o One-Pager. O sócio-local pode estar entregando com boa intenção o documento errado.

### 3. SPRINT 01 DE VITÓRIA — MODELO FUNCIONA (EVIDÊNCIA REAL)
- Kneip fechou R$ 4.195 de MRR no sprint (meta: R$ 1.311 / 2 clientes → superou em 3x)
- Pipeline em assinatura: R$ 3.857 | Em validação: R$ 1.925 | Total movimentado: ~R$ 10k
- Evidências concretas: contratos assinados + Notion atualizado
- **Regra aprendida:** O modelo de Sprint Quinzenal + One-Pager + C1/C2/C3 funciona quando o sócio-local executa com disciplina. Vitória é o primeiro dado real de que o framework gera resultado.

### 4. ESTRUTURA PRONTA NÃO É OPERAÇÃO INICIADA
- Sistema Operacional Comercial concluído em 11/03 com 70 itens de backlog e 7 charters
- 5 dias depois (16/03): 6 de 7 workstreams sem nenhum kickoff realizado
- **Regra aprendida:** Estruturar é necessário, mas não suficiente. A operação só começa com o kickoff. Cada semana sem arrancar é uma semana de execução perdida no H1.

---

## 🔑 Sessão: Arquitetura de Bots Telegram + Grupos com Tópicos
*Data: 2026-04-03*

### 1. groupAllowFrom ≠ channels.telegram.groups
- Ao tentar autorizar grupo via `groupAllowFrom`, o OpenClaw ignorou todas as mensagens (log: "not-allowed").
- O campo correto é `channels.telegram.groups` com o chat_id negativo do grupo.
- **Regra aprendida:** Para autorizar grupo Telegram, sempre usar `channels.telegram.groups["-100xxx"]`. `groupAllowFrom` é exclusivo para IDs de usuários.

### 2. MODELO POR TÓPICO NÃO É NATIVO — BOT SEPARADO É DETERMINÍSTICO
- Não existe roteamento nativo de LLM por tópico no OpenClaw.
- Forma confiável: bot separado com agent separado, cada um com modelo definido no config.
- **Regra aprendida:** Quando Diego pedir LLM diferente por contexto, recomendar bot separado. Tópico separa assunto, não modelo.

### 3. GRUPO TELEGRAM: HUMANO CRIA, MORFEU CONFIGURA
- Bot não pode criar grupo nem ativar tópicos — exige ação humana.
- Fluxo correto: Diego cria grupo + ativa tópicos + adiciona bots como admin → passa o ID → Morfeu configura roteamento.
- **Regra aprendida:** Setup de grupo Telegram é sempre em 2 etapas: humano primeiro, Morfeu depois.

### 4. requireMention: true NECESSÁRIO EM GRUPOS COM MÚLTIPLOS BOTS
- Com 3 bots no mesmo grupo e `requireMention: false`, todos respondem a toda mensagem.
- Solução definitiva: threadBindings — cada tópico vinculado a um agent específico.
- **Regra aprendida:** Em grupos com múltiplos bots, configurar threadBindings antes de desativar requireMention. Evita resposta duplicada.

### 5. PROCESSO ANTIGO CAPTURAVA MENSAGENS DO TELEGRAM
- Havia 2 instâncias do openclaw-gateway rodando (user `node` em /data e user `root`).
- A instância antiga consumia os updates antes da nova.
- **Regra aprendida:** Se bots param de responder após restart, verificar `ps aux | grep openclaw-gateway` para confirmar que não há instância duplicada rodando.

---

*Arquivadas em 28/03/2026 (Onda 1 — Otimização de Sistema): sessões de 05/03 a 16/03. Ver: archive/lessons_antigas_0305-0316.md*
- Evitar: Sem documentação das técnicas, conhecimento fica preso no Diego e não escala para o time — [6690232be5ccd900129d3e25](/2024-07) | Tipo: operational
- Evitar: Reunião de diretoria sem registro — histórico institucional incompleto — [669563a15e431f001476e56d](/2024-07) | Tipo: operational

---

## 🔑 Sessão: 10 Regras Invioláveis — ratificação e integração
*Data: 2026-04-08 | Sessão: Nova sessão + msg direta*

Diego reelaborou as 10 regras fundamentais do sistema. Todas ratificadas — nenhuma contradiz o que já estava em SOUL.md/AGENTS.md/TOOLS.md. Status de integração:

| # | Regra | Status | Onde está |
|---|-------|--------|-----------|
| 1 | isolated + agentTurn em crons | ✅ já em TOOLS.md + cron skill | — |
| 2 | Credenciais em .env | ✅ política existente | DRIVE_POLICY.md |
| 3 | dmPolicy allowlist | ✅ já configurado | IDENTITY.md |
| 4 | Extrair lessons antes de compactação | ✅ já em SOUL.md (Strict Write) | lessons.md |
| 5 | Agente novo = L1 observer | ✅ já em AGENTS.md | Subagent Contract |
| 6 | Split de modelos por tarefa | ✅ já em TOOLS.md | MODEL_GUIDE.md |
| 7 | Backup antes de mudança estrutural | ✅ já em AGENTS.md | SELF_HEALING_RUNBOOKS.md |
| 8 | Sub-agent retry 2x → alerta | ✅ já em AGENTS.md | Subagent Contract |
| 9 | SOUL.md genérico = agente genérico | ✅ centro do SOUL.md v4 | SOUL.md |
| 10 | Creators = skills dentro do agente, não agentes separados | ✅ já em AGENTS.md (skills) | SKILL.md |

**Ação tomada:** Adicionado entry em lessons.md.

*Revisado: 2026-04-08*

---

## 🔑 Bônus: 3 Regras Operacionais — ratificação
*Data: 2026-04-08 | Sessão: msg direta*

| # | Regra | Status | Onde está |
|---|-------|--------|-----------|
| B1 | Espaçar crons 15-30 min (colisão = rate limit) | ✅ já em TOOLS.md + cron skill | — |
| B2 | config.patch em horário sem crons | ✅ já em TOOLS.md | — |
| B3 | systemEvent não notifica no Telegram — usar agentTurn + message send | ✅ já em TOOLS.md + cron skill | — |

**Ação tomada:** Adicionado entry em lessons.md.

*Revisado: 2026-04-08*

**B4** | Jobs Cron isolated sessions falham com timeout (60-90s) + groq 401 | 2026-04-11 | — |
**Causa:** groq/llama-3.3-70b-versatile retorna HTTP 401 em todas as isolated sessions agentTurn. Timeout adicional de ~90s.
**Fix aplicado (Fase 1):** Trocar groq → minimax/MiniMax-M2.7 em todos os 10 jobs.
**Fix aplicado (Fase 2):** Aumentar timeout para 120-300s conforme complexidade.
**Jobs afetados:** polling, summarizer, tldv-digest, sync-cerebro-health, sync-cerebro system, validacao_p1a, auditoria_pending, self_improving_review, KAIROS watchdog, autoDream.
**Verificado:** sync-cerebro health check OK (exit 0).

- Evitar: H Station não usa CRM para incorporadora — processo de vendas é manual (contrato na mão, controle em planilha). Implementação do Z2A pode encontrar resistência de processo. — [6745b87129016500130d9262](/2024-11) | Tipo: operational
- Evitar: Telefone obrigatório no Z2A é para autenticação — sem telefone válido, usuário não acessa. Risco de onboarding bloqueado. — [6745b87129016500130d9262](/2024-11) | Tipo: operational
- Evitar: Reunião de novembro 2024 — 17 meses de décalage. Status real completamente desconhecido. — [6745b87129016500130d9262](/2024-11) | Tipo: strategic
- Evitar: João Pessoa é mercado de corretores externos — diferente de outras praças. Estratégia de venda e treinamento precisa ser adaptada para esse perfil. — [6745b87129016500130d9262](/2024-11) | Tipo: operational
- Evitar: Video de julho 2025 pode não ter sido formalmente distribuído — risco de conhecimento não chegar ao time — [688155a73ead900013f0436f](/2025-07) | Tipo: operational
- Evitar: Equipe não está fazendo follow-up em massa com corretores —gap entre discurso e execução — [68c091be0972b500130a0529](/2025-09) | Tipo: operational
- Evitar: Corretores estão conduzindo visitas com qualidade desigual — impacto na conversão — [68c091be0972b500130a0529](/2025-09) | Tipo: operational
- Evitar: Produto Z2A ainda não tem capacidade de ver quem são os 232 corretores que acessaram — visibilidade limitada — [68c091be0972b500130a0529](/2025-09) | Tipo: operational
- Evitar: 63% do VGV (R$ 56k de R$ 89k) ainda está pendente — risco de recebimento — [68d52426dd73370013fde50a](/2025-09) | Tipo: financial
- Evitar: Corretores de grupo de concorrência representam 50% dos ativos — dependência de canal único de captação — [68d52426dd73370013fde50a](/2025-09) | Tipo: operational
- Evitar: Baixa conversão de corretores — base de dados tem volume mas qualificação é fraca — [68d52426dd73370013fde50a](/2025-09) | Tipo: operational
- Evitar: CRM CV tem muitos problemas internos — Junior mencionou que 'tem muitos problemas para resolver' — [68d52426dd73370013fde50a](/2025-09) | Tipo: operational
- Evitar: Desbalanceamento e impressão negativa entre equipes (Eduardo levantou) — risco culture — [68d52426dd73370013fde50a](/2025-09) | Tipo: relationship
- Evitar: João manifestou desejo de otimizar tempo — especificamente sobre reuniões sem resultado e projeto ISO tomando 2h/semana. Pode indicar insatisfação ou sinyal de burnout — [68efb4bd79b4280013204146](/2025-10) | Tipo: operational
- Evitar: Expansão sem dono formal — Diego identificou que estava 'muito comigo e gargalo em mim'. Se João não foi empowered corretamente, o gargalo persiste — [68efb4bd79b4280013204146](/2025-10) | Tipo: operational
- Evitar: Praças prioritárias definidas (João Pessoa, Goiânia, Campinas, Rio, Recife) —semfollow-up sobre priorização. Pode ter havido diluição de foco — [68efb4bd79b4280013204146](/2025-10) | Tipo: strategic
- Evitar: João vê potencial como futuro diretor regional de expansão — sem plano de desenvolvimento formalizado, pode ser perda de talento — [68efb4bd79b4280013204146](/2025-10) | Tipo: relationship
- Evitar: Prazo de distribuição de lucros para PF era 31/12/2025 — oportunidadede tax planning pode ter sido perdida se não structurada a tempo — [6911e83237437f0013102674](/2025-11) | Tipo: financial
- Evitar: Iara (IA) treinada em CRI — se não foi implemented, equipe continua dependente de Diego para dúvidas técnicas — [6911e83237437f0013102674](/2025-11) | Tipo: operational
- Evitar: Modelo de CRI 88 é pouco diffundido no mercado — time pode enfrentar objeções de incorporadores que já receberam proposta cara anterior — [6911e83237437f0013102674](/2025-11) | Tipo: operational
- Evitar: Reunião de planning anual sem nenhum dado gravado — risco de decisões estratégicas perdidas — [695657252ab9160013645599](/2026-01) | Tipo: strategic
- Evitar: Se reunião foi em 01/01/2026, possibilidade alta de ter sido cancelada ou remarcada — [695657252ab9160013645599](/2026-01) | Tipo: operational
- Evitar: Três cancelamentos de contas em dezembro por falta de retorno — processo de follow-up fraco — [695bfc1ee9b88d0013912e2b](/2026-01) | Tipo: operational
- Evitar: Pisano pediu demissão 22/12 mas comunicação só confirmada 02/01 — 10 dias sem comunicação — [695bfc1ee9b88d0013912e2b](/2026-01) | Tipo: operational
- Evitar: Laís grávida (previsão junho/julho) — licença maternidade vai impactar time — [695bfc1ee9b88d0013912e2b](/2026-01) | Tipo: operational
- Evitar: Diego sem processo claro de coordenação — risco de ser gargalo — [695bfc1ee9b88d0013912e2b](/2026-01) | Tipo: operational
- Evitar: Sem Embaixador, audiência não cresce — é um loop que precisa ser quebrado — [695c285567410d0013fd37f1](/2026-01) | Tipo: operational
- Evitar: Time spreads too thin — fazendo várias praças ao mesmo tempo sem foco — [695c285567410d0013fd37f1](/2026-01) | Tipo: operational
- Evitar: Expansão sem estratégia documentada resulta em ação sem direção — [695c285567410d0013fd37f1](/2026-01) | Tipo: operational
- Evitar: Recife pode não tracionar se não houver follow-up consistente — [695c285567410d0013fd37f1](/2026-01) | Tipo: operational
- Evitar: Corretor pode não entender valor da plataforma vs portal genérico — [695e4ac3e9b88d00139173a0](/2026-01) | Tipo: operational
- Evitar: Mascam cancelou possivelmente por saída de SDR e falta de visibilidade — risco de efeito dominó — [695f91a6828894001391e6e0](/2026-01) | Tipo: operational
- Evitar: Saída de Wallace requer realinhamento estratégico — conhecimento pode ser perdido — [695f91a6828894001391e6e0](/2026-01) | Tipo: operational
- Evitar: Construtoras em SP não são fieis a um único escritório — exige modelo diferenciado — [695f91a6828894001391e6e0](/2026-01) | Tipo: relationship
- Evitar: João com ansiedade de gestão de múltiplos projetos — risco de burnout — [6960edbf427f08001307f913](/2026-01) | Tipo: operational
- Evitar: Incorporadoras não entendem processo de cadastro da Órula — objeção recorrente — [6960edbf427f08001307f913](/2026-01) | Tipo: operational
- Evitar: João se isola no remoto — Diego não consegue passar na cadeira — [6960edbf427f08001307f913](/2026-01) | Tipo: operational
- Evitar: João sobrecarregado — 15 reuniões + atualizar cards + treinar Ester + limpar funil — [6964f0693d76f900137fb719](/2026-01) | Tipo: operational
- Evitar: CRM desorganizado — cards desatualizados, leads frios sem limpeza — [6964f0693d76f900137fb719](/2026-01) | Tipo: operational
- Evitar: Processo CXDL não está claro — 'receita do bolo' ainda precisa ser descoberta — [6964f0693d76f900137fb719](/2026-01) | Tipo: strategic
- Evitar: Complexidade de gerenciar múltiplos cotistas com valores e prazos diferentes — [696528960245ea00136ccc1d](/2026-01) | Tipo: operational
- Evitar: Mudanças na legislação tributária após sanção presidencial em dezembro — incerteza — [696528960245ea00136ccc1d](/2026-01) | Tipo: compliance
- Evitar: Alíquota 10% flat aplica-se apenas acima de R$ 1,2M — risco de tributação se investimento abaixo — [696528960245ea00136ccc1d](/2026-01) | Tipo: financial
- Evitar: Proprietário de terreno pode não aceitar receber em CRI em vez de dinheiro — [696528960245ea00136ccc1d](/2026-01) | Tipo: relationship
- Evitar: Jade está 'relaxada' e 'crua' — não sabe ler playbook. Risco de pipeline lento se não melhorar rápido — [6966a43a99bea20013efccec](/2026-01) | Tipo: operational
- Evitar: 300+ currículos para triar — Gustavo vai perder muito tempo se fizer manualmente — [6966a43a99bea20013efccec](/2026-01) | Tipo: operational
- Evitar: Closer ainda não contratado — time está 'gargalado' — [6966a43a99bea20013efccec](/2026-01) | Tipo: operational
- Evitar: Volume de leads está baixo (Mila precisa expandir) — [6966a43a99bea20013efccec](/2026-01) | Tipo: operational
- Evitar: Reunião sem transcript, notas ou tópicos — 100% dos dados de conteúdo hilang. Impossível analisar, rastrear ou documentar. — [6968cc27290b3e0013fc3d86](/2026-01) | Tipo: operational
- Evitar: Se esta reunião foi relevante para decisões de janeiro/2026, esas decisões não estão documentadas em nenhum lugar acessível ao Morfeu. — [6968cc27290b3e0013fc3d86](/2026-01) | Tipo: strategic
- Evitar: Banco pode questionar estrutura se parecer engenharia para fugir de dívida — [6968f2f67ab7870013a596e4](/2026-01) | Tipo: financial
- Evitar: Rodrigo Italiano pode não estar usando a ferramenta em BH — pode indicar problemas de adoção — [69691d10290b3e0013fc4c42](/2026-01) | Tipo: operational
- Evitar: Sem contrato de fidelidade — cliente pode cancelar fácil se não ver resultado rápido — [69691d10290b3e0013fc4c42](/2026-01) | Tipo: financial
- Evitar: BH não tem integração com Ouro — base de corretores precisa ser preenchida manualmente — [69691d10290b3e0013fc4c42](/2026-01) | Tipo: operational
- Evitar: R$ 13k em dívidas Z2 (R$ 9k de 1 cliente) — contrato 30 dias impede cobrança — [696e712f500a210013c24a52](/2026-01) | Tipo: financial
- Evitar: Funcionária abandonou emprego há 14 dias — risco de processo trabalhista — [696e712f500a210013c24a52](/2026-01) | Tipo: compliance
- Evitar: Brasal com contrato parado há 2 meses — empresa burocrática de Goiânia — [696e712f500a210013c24a52](/2026-01) | Tipo: operational
- Evitar: Felipe tem reputação de difícil — afasta pessoas e cria medo na equipe — [696e712f500a210013c24a52](/2026-01) | Tipo: relationship
- Evitar: Relógio de ponto: lei exige acima de 20 funcionários desde 2022 — [696e712f500a210013c24a52](/2026-01) | Tipo: compliance
- Evitar: Empresa sem transparência — comunicação indireta prevalece — [696e712f500a210013c24a52](/2026-01) | Tipo: operational
- Evitar: Valor do apartamento está em discussão (4.5M vs 6M) — sem acordo, não há como fechar estrutura — [696f8356ee25fd0013b6ac94](/2026-01) | Tipo: financial
- Evitar: Imposto sobre aluguel vai aumentar de 6.73% para 10-16% em 2026 — [696f8356ee25fd0013b6ac94](/2026-01) | Tipo: financial
- Evitar: IBS e CBS vão aumentar de 6% para 10% sobre receita de aluguel — [696f8356ee25fd0013b6ac94](/2026-01) | Tipo: financial
- Evitar: José perdeu CPFL por falta de firmeza em acompanhamento de retornos — verificar se não é padrão — [696fc2aba1068c0013a3116d](/2026-01) | Tipo: relationship
- Evitar: Candidato não conhece detalhes do modelo (percentual, projeções) — sem dados pode não decidir — [696fc2aba1068c0013a3116d](/2026-01) | Tipo: operational
- Evitar: Produto em menos de 1.000 imobiliários = receita perdida enorme — [6970bfcbe50d0f0012494508](/2026-01) | Tipo: financial
- Evitar: 70% das 3.600 integrações inativas (mencionado em reunião prévia) — mesma dinâmica pode estar em treinamentos — [6970bfcbe50d0f0012494508](/2026-01) | Tipo: operational
- Evitar: Curitiba superou Porto Alegre em uso — mas sem dados de receita correlatos — [6970bfcbe50d0f0012494508](/2026-01) | Tipo: operational
- Evitar: Falta de CTA claro para corretores — baixo clique e conversão — [6970d3346d38bb00139bbcb1](/2026-01) | Tipo: operational
- Evitar: Integração com imobiliárias sem treinamento de onboarding — baixa ativação — [6970d3346d38bb00139bbcb1](/2026-01) | Tipo: operational
- Evitar: Sem sincronização de movimentos por praça, ações ficam isoladas e marca não acumula força — [6970d3346d38bb00139bbcb1](/2026-01) | Tipo: strategic
- Evitar: Problemas técnicos do webinar (fone) prejudicaram apresentação do Felipe — [6970d3346d38bb00139bbcb1](/2026-01) | Tipo: operational
- Evitar: Diego acumulando gestão interna + 25 viagens este ano — risco de overload — [6970d3346d38bb00139bbcb1](/2026-01) | Tipo: operational
- Evitar: Lançamento dez/2025 com apenas 6 vendas e zero visitas — Otimatec pode não ver ROI se visitas não começarem — [6970fca1e50d0f00124950b1](/2026-01) | Tipo: operational
- Evitar: Contrato ainda não formalizado — Otimatec precisa enviar dados de faturamento — [6970fca1e50d0f00124950b1](/2026-01) | Tipo: financial
- Evitar: Pedro busca renda passiva com mínimo trabalho operacional — se não conseguir, pode perder engagement — [6971292de4d717001331d562](/2026-01) | Tipo: operational
- Evitar: Custo de crédito CDI+10 a CDI+12 é alto — pode afastar clientes — [6971292de4d717001331d562](/2026-01) | Tipo: financial
- Evitar: Exclusividade em mercado secundário gera baixo volume — modelo pode não escalar — [6971292de4d717001331d562](/2026-01) | Tipo: operational
- Evitar: Integração Z2+Ouro 50% incompleta — clientes podem ficar confusos — [697214b6e4d717001331f32f](/2026-01) | Tipo: operational
- Evitar: Teste free sem follow-up pode não mostrar ROI real — [697214b6e4d717001331f32f](/2026-01) | Tipo: operational
- Evitar: Cadência de treino pode perder momentum se não houver prática — [697214b6e4d717001331f32f](/2026-01) | Tipo: operational
- Evitar: Número WhatsApp banido impediu contato com alguns potenciais clientes — risco de perda de pipeline — [69736636913cb900132bd0eb](/2026-01) | Tipo: operational
- Evitar: Bug na solicitação de integração não abre formulário no navegador para alguns CRMs — atrito no funil — [69736636913cb900132bd0eb](/2026-01) | Tipo: operational
- Evitar: Nova leva de inscritos no final de segunda-feira não foi importada na Meta a tempo dos disparos — [69736636913cb900132bd0eb](/2026-01) | Tipo: operational
- Evitar: Retenção em João Pessoa é 23-24% em 5 meses — abaixo do ideal — [69736636913cb900132bd0eb](/2026-01) | Tipo: operational
- Evitar: Impossibilidade de responder via número oficial da Meta sem template — limita interação em tempo real — [69736636913cb900132bd0eb](/2026-01) | Tipo: operational
- Evitar: DL recebe menos informações que incorporadores regulares — pode gerar percepção de injustiça — [697377d35355be00138a5614](/2026-01) | Tipo: relationship
- Evitar: WhatsApp gera custos altos — se não migrar para app, Margens sofrem — [697377d35355be00138a5614](/2026-01) | Tipo: financial
- Evitar: Fluxo de intermediação complexo demais afasta corretores — [697377d35355be00138a5614](/2026-01) | Tipo: operational
- Evitar: Mercado de Goiânia pode ser diferente de SP/Porto Alegre — comportamento e culture local unknown — [6973b71e7f640c0013685039](/2026-01) | Tipo: operational
- Evitar: José não tem histórico em mercado imobiliário — curva de aprendizado pode ser longa — [6973b71e7f640c0013685039](/2026-01) | Tipo: operational
- Evitar: Sem acesso direto a Beatriz Gomes, José pode perder tempo esperando alinhamento interno — [6973b71e7f640c0013685039](/2026-01) | Tipo: operational
- Evitar: Corretor pode abandonar producto se tabela estiver desatualizada - gera frustração no cliente final — [6979fa4507a27300130c12b7](/2026-01) | Tipo: operational
- Evitar: Se corretor não gosta do coordenador de plataforma, ele não oferece o producto - impacto direto em vendas — [6979fa4507a27300130c12b7](/2026-01) | Tipo: relationship
- Evitar: Rastreabilidade de negociacoes ainda está precária - necessidade de usar Skydes para tracking — [6979fa4507a27300130c12b7](/2026-01) | Tipo: operational
- Evitar: Reunião sem registro estruturado — histórico perdido. Apenas 4 palavras de transcript. — [697b41262238f70013485bfe](/2026-01) | Tipo: operational
- Evitar: Zona sul de João Pessoa tem demanda grande sem cobertura atual — oportunidade sendo perdida — [697ca3cb6216b200139caad4](/2026-01) | Tipo: operational
- Evitar: Corretores não encontram filtros disponíveis na plataforma — frustração por desconhecimento do produto — [697ca3cb6216b200139caad4](/2026-01) | Tipo: operational
- Evitar: Tabelas de preço desatualizadas causam frustração quando imóvel custa mais que informado — [697ca3cb6216b200139caad4](/2026-01) | Tipo: operational
- Evitar: Usuários ativos desconhecem filtros e funcionalidades — produto subutilizado — [697ca3cb6216b200139caad4](/2026-01) | Tipo: operational
- Evitar: Kaique precisa aprovar gerente — decisão fora do alcance direto da Orla. Risco de travamento. — [697cbcd6697b570013ec88f3](/2026-01) | Tipo: operational
- Evitar: Contrato anual pode ser barreira para primeira contratação — manager pode hesitAR em comprometer 12 meses — [697cbcd6697b570013ec88f3](/2026-01) | Tipo: operational
- Evitar: Mune descobriu Orla via ChatGPT — cliente ainda está validando. Pode estar em paralelo com outros fornecedores. — [697cbcd6697b570013ec88f3](/2026-01) | Tipo: operational
- Evitar: Luigi sente-se refem de parceiro unico e busca diversificar - risco de lock-in atual e perda de controle comercial — [6980adfcc547420013ede25e](/2026-02) | Tipo: strategic
- Evitar: Time de coordenadores foi perdido - necessidade de reforms estrutural antes de cualquier aktivacao — [6980adfcc547420013ede25e](/2026-02) | Tipo: operational
- Evitar: Bloqueio de parcerias esta impedindo corretores de vender quando ha interessados - impacto direto em receita — [6980adfcc547420013ede25e](/2026-02) | Tipo: operational
- Evitar: Desalinhamento de incentivos entre corretores internos e externos prejudica abertura de mercado — [6980adfcc547420013ede25e](/2026-02) | Tipo: operational
- Evitar: Automove: Revenda apos entrega deprimiu precos - recuperacao iniciando — [6980adfcc547420013ede25e](/2026-02) | Tipo: financial
- Evitar: Déficit de 7k em vendas mencionado como tema recorrente sem plano de ação definido — [698334ce7d83e400138dc05b](/2026-02) | Tipo: operational
- Evitar: 119 tarefas sem dono no CRM (dado externo) sinalizam falta de accountability estrutural no time — [698334ce7d83e400138dc05b](/2026-02) | Tipo: operational
- Evitar: Treinamentos podem perder effectiveness se formato não mudar (time pediu menos slides, mais cases) — [698334ce7d83e400138dc05b](/2026-02) | Tipo: operational
- Evitar: Arcplan integra apenas com 50 CRM de imobiliárias em vez dos 1050 esperados — frustração potencial em clientes — [698334ce7d83e400138dc05b](/2026-02) | Tipo: operational
- Evitar: Portal Z2 está canibalizando audiência da plataforma — pode prejudar conversão — [69834628f89b5a0013ba42fd](/2026-02) | Tipo: operational
- Evitar: Pedro executou apenas 25-30% das requisições de integração do ES — [69834628f89b5a0013ba42fd](/2026-02) | Tipo: operational
- Evitar: Problema sistêmico de Vitória: baixo número de incorporadoras cadastradas — [69834628f89b5a0013ba42fd](/2026-02) | Tipo: operational
- Evitar: Dispersão de audiência em diferentes aplicativos prejudica conversão em Vitória — [69834628f89b5a0013ba42fd](/2026-02) | Tipo: operational
- Evitar: Reforma tributária aumenta carga — cautela com litígio após Instrução 227 — [6984a262c8ca580013150c28](/2026-02) | Tipo: financial
- Evitar: Limite 50k mensais por CNPJ aplica-se ao total — planejamento tributário precisa ser cuidadoso — [6984a262c8ca580013150c28](/2026-02) | Tipo: compliance
- Evitar: Torreão nunca captou via CRI — pode haver resistência institucional — [6984a262c8ca580013150c28](/2026-02) | Tipo: operational
- Evitar: Incorporadoras ainda tratam canal de parcerias como mal necessário, não como ativo estratégico — [6984c57ba0c380001332dc21](/2026-02) | Tipo: strategic
- Evitar: Falta de rastreabilidade e continuidade no trabalho de parcerias — [6984c57ba0c380001332dc21](/2026-02) | Tipo: operational
- Evitar: Treinamentos presenciais não escalam — corretores trocam frequentemente — [6984c57ba0c380001332dc21](/2026-02) | Tipo: operational
- Evitar: Reunião sem transcript, notas ou tópicos — risco de perda de conhecimento institucional — [6984f6b56de6d60013aef6ba](/2026-02) | Tipo: operational
- Evitar: Não há controle total sobre mensagem de cada corretor — [6989ef6383febd0013d31918](/2026-02) | Tipo: compliance
- Evitar: Potencial canibalização com base de clientes diretos da Vitacom — [6989ef6383febd0013d31918](/2026-02) | Tipo: operational
- Evitar: Samanta só 2 semanas no projeto — pode ter gaps de informação — [6989ef6383febd0013d31918](/2026-02) | Tipo: operational
- Evitar: Volume de reuniões cresceu mas vendas não acompanharam — incongruência — [698b7223486bad00134bacac](/2026-02) | Tipo: operational
- Evitar: Não existe métrica de qualidade ou assertividade ainda — [698b7223486bad00134bacac](/2026-02) | Tipo: operational
- Evitar: Carteira de João com 66 clientes está grande demais — não consegue dar atenção adequada — [698b9011657ae90013b40ee1](/2026-02) | Tipo: operational
- Evitar: Sem padrão de perdido, negócios ficam em limbo — nem ativos nem cerrados — [698b9011657ae90013b40ee1](/2026-02) | Tipo: operational
- Evitar: Histórico de atividades do João não aparece — dados de CRM incompletos — [698b9011657ae90013b40ee1](/2026-02) | Tipo: operational
- Evitar: BDRs não validam cargo e expectativa antes de reuniões XL — resulta em meetings ineficazes — [698b9011657ae90013b40ee1](/2026-02) | Tipo: operational
- Evitar: Boulevard Zanella: 4 unidades em 12 anos — caso extrema de VSO baixo — [698c6f356979ef0013b83ce5](/2026-02) | Tipo: operational
- Evitar: IGSA: dois terrenistas podem não aprovar proposta de isenção — [698c6f356979ef0013b83ce5](/2026-02) | Tipo: financial
- Evitar: Laguna Curitiba: 11 unidades em estoque de 48 — vendas lentas mesmo com 77% vendido — [698c6f356979ef0013b83ce5](/2026-02) | Tipo: operational
- Evitar: Mercado aponta possível queda nas vendas para próximos meses — [698cb58fecdf0e001300edbc](/2026-02) | Tipo: financial
- Evitar: Difícil convencer incorporadores a usar plataforma em vez de Google Drive — [698cb58fecdf0e001300edbc](/2026-02) | Tipo: operational
- Evitar: WhatsApp enfrenta riscos regulatórios que afetam estratégia de mensageria — [698cb58fecdf0e001300edbc](/2026-02) | Tipo: compliance
- Evitar: Rafael possui produto com problemas de precificação e posicionamento — [698cb58fecdf0e001300edbc](/2026-02) | Tipo: operational
- Evitar: Guilherme precisa de abertura com incorporadoras — competência difícil de desenvolver rápido — [698cb58fecdf0e001300edbc](/2026-02) | Tipo: relationship
- Evitar: Apresentação parece startup de 6 meses — não transmite 14 anos de experiência — [698dcb4b834af3001393610e](/2026-02) | Tipo: strategic
- Evitar: Muitos espaços em branco na apresentação — não passa sensação de volume e escala — [698dcb4b834af3001393610e](/2026-02) | Tipo: operational
- Evitar: Vídeos muito calmos — não geram engajamento — [698dcb4b834af3001393610e](/2026-02) | Tipo: marketing
- Evitar: Processo seletivo sem registro — se Luan foi contratado, sua integração não está documentada — [698ddce91bcf5d0012a30d2c](/2026-02) | Tipo: operational
- Evitar: Se decisão foi contrária (Luan não aprovado), essa informação também está perdida — [698ddce91bcf5d0012a30d2c](/2026-02) | Tipo: operational
- Evitar: Imobiliárias resistem a pagar custo adicional por consultoria — response foi unânime. Positioning do serviço opcional pode não converter — [698e071b1bcf5d0012a314f4](/2026-02) | Tipo: financial
- Evitar: Equipe técnica com apenas 4 pessoas atende 11 estados — clientes de catálogo gratuito podem demorar >1 dia. Prioridade para pagos cria atrito — [698e071b1bcf5d0012a314f4](/2026-02) | Tipo: operational
- Evitar: ~40 CRMs com regras variáveis — sem monitoramento ativo, regras mudam sem notificação (ex: Mobi Brasil começou a cobrar pacote extra) — [698e071b1bcf5d0012a314f4](/2026-02) | Tipo: operational
- Evitar: CRM subscendo edições feitas pela equipe — trabalho de curadoria da Gisele pode ser apagado na próxima atualização automática — [698e071b1bcf5d0012a314f4](/2026-02) | Tipo: operational
- Evitar: Integração com plantas de unidades às vezes puxa apenas uma planta, causando inconsistência com preço — Dado técnico que afeta qualidade do catálogo — [698e071b1bcf5d0012a314f4](/2026-02) | Tipo: operational
- Evitar: REUNIÃO NÃO OCORREU — 0.1min de duração. Possível cancelamento ou erro de registro. Necessária confirmação. — [698e3137ecdf0e00130126b6](/2026-02) | Tipo: operational
- Evitar: Tela de login completa com muitos campos causa atrito significativo — corretor abandona — [698f6d9bacd46d001342c98e](/2026-02) | Tipo: operational
- Evitar: Usuários mais velhos (50+) preferem PDF e não usam portal — população crescente — [698f6d9bacd46d001342c98e](/2026-02) | Tipo: operational
- Evitar: Formatação CMS não corresponde ao publicado — frustra gestor de conteúdo — [698f6d9bacd46d001342c98e](/2026-02) | Tipo: operational
- Evitar: Mês em 82% do tempo com menos de 50% da meta atingida — ritmo insuficiente — [699c4f44e344ac00135beff1](/2026-02) | Tipo: operational
- Evitar: Follow-up com 'bom dia tudo bem' sem conteúdo é amadorismo eafasta cliente — [699c4f44e344ac00135beff1](/2026-02) | Tipo: operational
- Evitar: Etapa de formulário entre aprovação e contrato atrasa fechamento — [699c4f44e344ac00135beff1](/2026-02) | Tipo: operational
- Evitar: Incorporadoras em Curitiba estão demorando para se mexerem após lei de altas rendas — urgência não é clara para eles — [699de717fc507800135cebf6](/2026-02) | Tipo: operational
- Evitar: Curitiba evita palavra 'permuta' — linguagem precisa ser adaptada para 'parcelamento' — [699de717fc507800135cebf6](/2026-02) | Tipo: operational
- Evitar: Luiz não atualizou cards há duas semanas — visibilidade de pipeline comprometida — [699df8a5fc507800135cef6d](/2026-02) | Tipo: operational
- Evitar: Marcos enrolando há 3 dias para assinar Lagon — pode perder deal — [699df8a5fc507800135cef6d](/2026-02) | Tipo: operational
- Evitar: Divergência 180 no consolidado — planejamento financeiro pode ser afetado — [699df8a5fc507800135cef6d](/2026-02) | Tipo: financial
- Evitar: Anton não está no Bitrix — falta visibilidade de Curitiba — [699df8a5fc507800135cef6d](/2026-02) | Tipo: operational
- Evitar: Programação do painel dia 15 ainda não definida — compromete marketing e comunicação — [699f2aa210f9590013215cfc](/2026-02) | Tipo: operational
- Evitar: Evento no condomínio Murano é plantão de vendas adaptado — pode ter limitações de estrutura — [699f2aa210f9590013215cfc](/2026-02) | Tipo: operational
- Evitar: Horário de evento pode conflitar com rotina de construtores se for de manhã — [699f2aa210f9590013215cfc](/2026-02) | Tipo: operational
- Evitar: Kowalski não aceitou colaboração via business — apenas Facebook e Instagram — [69a0435446f1b600120eec2f](/2026-02) | Tipo: operational
- Evitar: Diego perdeu robô corretor ao migrar conta para business — [69a0435446f1b600120eec2f](/2026-02) | Tipo: operational
- Evitar: 90 dias de carência gratuita terminam ~final de maio 2026 — se não houver processo de conversão, empreendimentos podem sair sem收费 — [69a07c1fe344ac00135c907e](/2026-02) | Tipo: financial
- Evitar: Precificação segue tabela Apolar — se a tabela Apolar for mais baixa que a Órulo, há risco de subprecificação — [69a07c1fe344ac00135c907e](/2026-02) | Tipo: financial
- Evitar: Imóveis não vendidos em 10-15 dias vão automaticamente para Apolar Busca — podem criar conflito de exclusividade com outros canais — [69a07c1fe344ac00135c907e](/2026-02) | Tipo: operational
- Evitar: Apolar atualiza 70% dos lançamentos do Brasil — poder de dados grande mas dependencia de partner único — [69a07c1fe344ac00135c907e](/2026-02) | Tipo: strategic
- Evitar: Muitos clientes não possuem administrador definido — risco operacional alto — [69a19c4b7ac8c80013e360e1](/2026-02) | Tipo: operational
- Evitar: Percepção de baixa atualização pode gerar desconfiança no produto — [69a19c4b7ac8c80013e360e1](/2026-02) | Tipo: operational
- Evitar: Editor pode tentar roubar corretor de outro gerente se tiver permissões — [69a19c4b7ac8c80013e360e1](/2026-02) | Tipo: operational
- Evitar: Fevereiro foi mês desafiador (chuvas) — equipe manteve foco mas resultados podem ter sido impactados — [69a589c5e344ac00135cecc6](/2026-03) | Tipo: operational
- Evitar: Luan novo — curva de aprendizado pode impactar resultados de março — [69a589c5e344ac00135cecc6](/2026-03) | Tipo: operational
- Evitar: Follow-up sem valor contextualizado não gera impacto — time tende a fazer follow-up mecânico — [69a589c5e344ac00135cecc6](/2026-03) | Tipo: operational
- Evitar: Feb venda R$ 3.800 vs meta R$ 15k — 75% abaixo da meta — [69a5d01885c6ba0013e91d47](/2026-03) | Tipo: financial
- Evitar: 2 mil integrações inativas sem resolução — receita estagnada — [69a5d01885c6ba0013e91d47](/2026-03) | Tipo: operational
- Evitar: Bruno não demonstrando urgência e falta objetividade — risco para time — [69a5d01885c6ba0013e91d47](/2026-03) | Tipo: relationship
- Evitar: Universal: PH com histórico de não responder e não colaborar — [69a5d01885c6ba0013e91d47](/2026-03) | Tipo: operational
- Evitar: Knight não colaborou com BDRs — atrapalha performance do time — [69a5d01885c6ba0013e91d47](/2026-03) | Tipo: operational
- Evitar: Tentativa anterior de levar Panorama para litoral não evoluiu em 2024 — [69a8812d22b1f60013518707](/2026-03) | Tipo: strategic
- Evitar: João fez 8 reuniões na semana — abaixo do número 'bom' de 20. Performando abaixo do target. — [69a9d2aaf0f6080013cc814b](/2026-03) | Tipo: operational
- Evitar: Tenda 'sempre escorrega' — padrão de perda reiterada. Sem intervenção, histórico vai se repetir. — [69a9d2aaf0f6080013cc814b](/2026-03) | Tipo: operational
- Evitar: Processo de reporte entre closer e Gustavo não estava acontecendo antes — 'fechar ciclo' era necessário — [69a9d2aaf0f6080013cc814b](/2026-03) | Tipo: operational
- Evitar: João fechou 5-7 vendas — mas qual o ticket médio? A meta de R$ 15mil depende de mix de produtos — [69a9d2aaf0f6080013cc814b](/2026-03) | Tipo: financial
- Evitar: Qualidade de vídeo em Vitória foi fraca — sem profissionalismo não escala — [69aac1ccd537b40013ab1c27](/2026-03) | Tipo: operational
- Evitar: Compartilhamento Instagram com usuários não-hora é complicado — [69aac1ccd537b40013ab1c27](/2026-03) | Tipo: operational
- Evitar: Evento Vitória focou em redes sociais sem anúncio — alcance pode ter sido baixo — [69aac1ccd537b40013ab1c27](/2026-03) | Tipo: operational
- Evitar: Gustavo estava muito focado no topo do funil e pouco no fundo — [69ab191ceef3be0013324da1](/2026-03) | Tipo: operational
- Evitar: CRM precisa melhorar preenchimento de etapa do funil e dados de temperatura — [69ab191ceef3be0013324da1](/2026-03) | Tipo: operational
- Evitar: João é novo como apresentador — risco de perder público ou não cobrir conteúdo no tempo — [69b0722b4519e900135b07f9](/2026-03) | Tipo: operational
- Evitar: Ativar rede de audiência qualificada é a maior lacuna de recursos — [69b159356fac13001319c488](/2026-03) | Tipo: operational
- Evitar: Comunicação com corretores é um dos pontos mais frágeis da estratégia atual — [69b159356fac13001319c488](/2026-03) | Tipo: operational
- Evitar: Falta visualização de quais ações geraram aumento de corretores ativos em Curitiba — [69b159356fac13001319c488](/2026-03) | Tipo: operational
- Evitar: Time de BDR não está usando Z2 corretamente — não sabe usar automação, detecção de diálogos quentes ou auditoria — [69b1bd08c1e9ee0013779ffa](/2026-03) | Tipo: operational
- Evitar: Bloqueio por spam se exceder 2 mensagens por hora — pode afectar comunicação do evento — [69b1bd08c1e9ee0013779ffa](/2026-03) | Tipo: operational
- Evitar: Felipe está focado em Vitória (fechando 4 contratos grandes) — pode não ter bandwidth para Capão — [69b1bd08c1e9ee0013779ffa](/2026-03) | Tipo: relationship
- Evitar: Segmentação de blocos pode não atingir público certo — 200 contatos podem não responder — [69b1bd08c1e9ee0013779ffa](/2026-03) | Tipo: operational
- Evitar: Mercado imobiliário Curitiba é mais tradicional e lento na adoção de CRI — [69b2f1112c298800128eafa1](/2026-03) | Tipo: relationship
- Evitar: Advogados e contadores ainda não dominam CRI — pode gerar resistência — [69b2f1112c298800128eafa1](/2026-03) | Tipo: compliance
- Evitar: WhatsApp de Ester restrito por 24h devido a fluxo de mensagens — [69b3ffb54270ef0013147a6a](/2026-03) | Tipo: operational
- Evitar: Maioria dos corretores não conhece CRM ou integração — educação de mercado necessária — [69b3ffb54270ef0013147a6a](/2026-03) | Tipo: operational
- Evitar: Apenas 1.278 de 3.611 integrações têm fluxo de dados — baixa utilização — [69b3ffb54270ef0013147a6a](/2026-03) | Tipo: operational
- Evitar: Reuniao de 63 minutos sem registro — histórico completamente perdido. Impossível auditar. — [69b406bf6fac1300131a22fb](/2026-03) | Tipo: operational
- Evitar: GC Engenharia não avançou despite reunião presencial — pode ser desinteresse real — [69b44bbf7314d6001379cf1c](/2026-03) | Tipo: operational
- Evitar: Marco da R2 não responde — pode ser perdido — [69b44bbf7314d6001379cf1c](/2026-03) | Tipo: operational
- Evitar: Luciano situation is difficult — relacionamento comprometido — [69b44bbf7314d6001379cf1c](/2026-03) | Tipo: relationship
- Evitar: Quest: Bruno não repassa informações — coordadores enrolados — [69b44bbf7314d6001379cf1c](/2026-03) | Tipo: operational
- Evitar: Desafio principal: avançar de reunião realizada para negociação ativa — [69b44bbf7314d6001379cf1c](/2026-03) | Tipo: operational
- Evitar: Reunião de 119.8 minutos sem nenhum dado — impossibilidade total de análise — [69b47ac2e108b900136ad1fd](/2026-03) | Tipo: operational
- Evitar: Se reunião aconteceu e continha decisões estratégicas, essas decisões não estão documentadas em nenhum lugar — [69b47ac2e108b900136ad1fd](/2026-03) | Tipo: strategic
- Evitar: Z2 tem implantações não faturadas — risco de receita não reconhecida — [69b845174ddb450012bb9140](/2026-03) | Tipo: financial
- Evitar: Clientes do ano passado ainda têm discussões abertas sobre pagamento — [69b845174ddb450012bb9140](/2026-03) | Tipo: financial
- Evitar: Super Lógica não responde há dois meses sobre categorização — [69b845174ddb450012bb9140](/2026-03) | Tipo: operational
- Evitar: Internacionalização (Paraguai) não suportada pelo sistema — [69b845174ddb450012bb9140](/2026-03) | Tipo: operational
- Evitar: Levantar 25M em equity para Campinas não é trivial no mercado atual — [69bbe54c50d24b001394c612](/2026-03) | Tipo: financial
- Evitar: Limite de 15M por estrutura pode ser insuficiente para operações maiores — [69bbe54c50d24b001394c612](/2026-03) | Tipo: financial
- Evitar: Loteador do interior quer capitalizar para comprar concorrentes — uso de capital pode não gerar retorno esperado — [69bbe54c50d24b001394c612](/2026-03) | Tipo: financial
- Evitar: Limite de imóveis no plano CRM causa retrabalho e desistência — barreira de produto que empurra corretores para uso direto do Ouro — [69bd3dc6afb4b00013f63364](/2026-03) | Tipo: operational
- Evitar: Mensagem anterior com hotsite/inteligência de mercado teve 35-40% de resposta — mas pode estar saturando. Testar mensagem nova com abordagem diferente. — [69bd3dc6afb4b00013f63364](/2026-03) | Tipo: operational
- Evitar: Corretores preferem plataforma gratuita — custo do CRM é barreira real. Se não houver argumento de valor forte, perdem para alternativas gratuitas. — [69bd3dc6afb4b00013f63364](/2026-03) | Tipo: financial
- Evitar: De 19 inativos contactados, apenas 1 quer reativar — taxa de sucesso de 5%. Esforço alto para resultado baixo se não segmentar melhor. — [69bd3dc6afb4b00013f63364](/2026-03) | Tipo: operational
- Evitar: Se Imobmeet não tiver tabela de vendas estruturada, integração não funciona — [69bd9ef06a28e60013c3eb61](/2026-03) | Tipo: operational
- Evitar: Incorporadoras podem resistir à integração por medo de expor dados — [69bd9ef06a28e60013c3eb61](/2026-03) | Tipo: relationship
- Evitar: Expansão para capitais depende de Gleybiony resolver problemas técnicos — [69bd9ef06a28e60013c3eb61](/2026-03) | Tipo: operational
- Evitar: 4 empreendimentos simultâneos exigem capital próprio significativo — risco de concentração de risco — [69be9d49c1f67b0013e5fa4c](/2026-03) | Tipo: financial
- Evitar: Daniel não financia pós-obra — dependência de capital próprio limita escala — [69be9d49c1f67b0013e5fa4c](/2026-03) | Tipo: financial
- Evitar: Terrenista do Sublime Batel declinou permuta antes — pode resistir novamente — [69be9d49c1f67b0013e5fa4c](/2026-03) | Tipo: relationship
- Evitar: Locação tem carga tributária de ~30% vs 4% em compra e venda — sem CRI, penaliza investidor — [69be9d49c1f67b0013e5fa4c](/2026-03) | Tipo: financial
- Evitar: Greca: 9.892m², 24 pavimentos, 95% capital próprio — obra de alto risco se mercado esfriar — [69be9d49c1f67b0013e5fa4c](/2026-03) | Tipo: financial
- Evitar: Incorporação imobiliária em Sinop é negocio de alto risco — não aceita amador — [69c3dc5fdbc75500136ae2e6](/2026-03) | Tipo: operational
- Evitar: Mato-grossenses patrimonialistas — 80% não querem revender, difere do perfil SP — [69c3dc5fdbc75500136ae2e6](/2026-03) | Tipo: strategic
- Evitar: Sem definição de estrutura (CRI vs SCP), economia de 5M não acontece — [69c3dc5fdbc75500136ae2e6](/2026-03) | Tipo: financial
- Evitar: Gustavo em tratamento de saúde desde fim de 2024 — projeto pode atrasar — [69c53bda89dd4d0013feab19](/2026-03) | Tipo: operational
- Evitar: Automação de outbound sem processo validado primeiro pode desperdiçar investimento — [69c53bda89dd4d0013feab19](/2026-03) | Tipo: operational
- Evitar: BDRs não sabem usar IA no dia a dia — automação avançada inútil sem treinamento básico — [69c53bda89dd4d0013feab19](/2026-03) | Tipo: operational
- Evitar: Cada SDR/BDR usa WhatsApp web individual — sem centralização não há controle — [69c53bda89dd4d0013feab19](/2026-03) | Tipo: operational
- Evitar: Negociação Luli Goiânia travada na diretoria — risco de perder três contratos — [69c58224f2dd940013643f4d](/2026-03) | Tipo: operational
- Evitar: W3 Rio aguardando assinatura — faturamento por SPA pode travar novamente — [69c58224f2dd940013643f4d](/2026-03) | Tipo: operational
- Evitar: 430 imobiliárias aguardando ativação — botão não habilitado — [69c58224f2dd940013643f4d](/2026-03) | Tipo: operational
- Evitar: Denise SP aguardando aprovação da diretoria de parcerias — [69c58224f2dd940013643f4d](/2026-03) | Tipo: operational
- Evitar: Velocidade de 10% da meta mensal insuficiente — 90% do caminho falta — [69c674b5602e260013bbd14c](/2026-03) | Tipo: operational
- Evitar: Z2 não suporta áudios — comunicação pode ser perdida — [69c674b5602e260013bbd14c](/2026-03) | Tipo: operational
- Evitar: João Pessoa uma das piores cidades para integração de corretores — [69c674b5602e260013bbd14c](/2026-03) | Tipo: operational
- Evitar: Video maker não retornou ajustes solicitados para material de evento — [69c67bbe0da323001305d36e](/2026-03) | Tipo: operational
- Evitar: Capão da Canoa pode não ter lotação suficiente para evento — [69c67bbe0da323001305d36e](/2026-03) | Tipo: operational
- Evitar: Realiza em Curitiba não sabia sobre planos de aceleração — informação não está chegando aos clientes — [69ca73c524b2440013ebe436](/2026-03) | Tipo: operational
- Evitar: Sócios locais podem sobrecarregar se não tiver automações/processos — [69ca73c524b2440013ebe436](/2026-03) | Tipo: operational
- Evitar: Paisagem Corporal pediu remoção de empreendimentos — perdemos conta? — [69ca73c524b2440013ebe436](/2026-03) | Tipo: operational
- Evitar: Volume de reuniões precisa aumentar para bater meta anual de 250k — [69ca73c524b2440013ebe436](/2026-03) | Tipo: operational
- Evitar: Z2 deve R$ 50 mil de implantações e não paga há um ano — [69caba140da323001306119a](/2026-03) | Tipo: financial
- Evitar: Modelo de sociedade com Z2 não funciona operacionalmente — [69caba140da323001306119a](/2026-03) | Tipo: operational
- Evitar: Passivos jurídicos e financeiros pendentes bloqueiam novas pautas — [69caba140da323001306119a](/2026-03) | Tipo: compliance
- Evitar: Corretores reclamam que não existe book para empreendimento — [69caba140da323001306119a](/2026-03) | Tipo: operational
- Evitar: Cyrela tem problema com comissão que diminui quando vende bem — [69caba140da323001306119a](/2026-03) | Tipo: financial
- Evitar: Guilherme ainda não fechou nenhum contrato assinado — só GFR contratando e Antônio pending — [69cc20acddea5b00135fdc45](/2026-03) | Tipo: operational
- Evitar: Conflito potencial entre remuneração de Zanella e Guilherme (ambos querem % do faturamento) — [69cc20acddea5b00135fdc45](/2026-03) | Tipo: relationship
- Evitar: Mercado Curitiba é fechado por corretores — requer presença física e mística local — [69cc20acddea5b00135fdc45](/2026-03) | Tipo: operational
- Evitar: Incorporadoras conversam entre si sobre preços — criam pressão para padronização — [69cc20acddea5b00135fdc45](/2026-03) | Tipo: financial
- Evitar: Rafael descartado por comportamento problemático — pode spread negative word-of-mouth — [69cc20acddea5b00135fdc45](/2026-03) | Tipo: relationship
- Evitar: CRM em avaliação sem decisão — processo pode estar parado — [69cd08ba5339450013b8fd72](/2026-04) | Tipo: operational
- Evitar: Bianca 80% estoque vendido sem lançamento este ano — não tem momento crítico = não converte agora — [69cd08ba5339450013b8fd72](/2026-04) | Tipo: operational
- Evitar: Mateus (Sobral) ainda em investigação — sem card robusto não avança — [69cd08ba5339450013b8fd72](/2026-04) | Tipo: operational
- Evitar: Unitas tem capacidade de distribuição via Samba Office e investidores conhecidos — pode não precisar do Paulo se conseguir deals grandes — [69ce765eddea5b001360288d](/2026-04) | Tipo: operational
- Evitar: Parceria ainda não está selada — Raphael vai testar com um caso — [69ce765eddea5b001360288d](/2026-04) | Tipo: relationship
- Evitar: Fundo imobiliário só vale a pena com originação significativa — Unitas pode não ter volume suficiente — [69ce765eddea5b001360288d](/2026-04) | Tipo: financial
- Evitar: Maristela (Floripa) parou de responder — contrato de 6 meses pode ser perdido — [69cebf017c8d0800136e9e57](/2026-04) | Tipo: operational
- Evitar: Cumaru recusou taxa de implementação — pode perder Implementation fee — [69cebf017c8d0800136e9e57](/2026-04) | Tipo: financial
- Evitar: Dados CRM em caos — campo estado não usado, duplicações, campos conflitantes — [69cebf017c8d0800136e9e57](/2026-04) | Tipo: operational
- Evitar: João tem 89% da carteira com Luan — concentração de risco — [69cebf017c8d0800136e9e57](/2026-04) | Tipo: operational
- Evitar: Salazar com 50% desconto — margem comprometida se aceitar — [69cebf017c8d0800136e9e57](/2026-04) | Tipo: financial
