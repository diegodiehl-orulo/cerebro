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
