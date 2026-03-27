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

## 🔑 Sessão: Diagnóstico Estrutural Órulo — Etapas 4 e 5
*Data: 2026-03-09 | Sessão: Auditoria cognitiva e operacional*

### 1. O AGENTE É PESSOAL, NÃO OPERACIONAL
- O agente é cérebro auxiliar para Diego individualmente (briefings, alertas, agenda, emails)
- O agente é repositório passivo para a operação da Órulo (WS, time, DRIs, pipeline)
- Distinção ativa: onde Diego interage diretamente, o sistema funciona. Onde o time opera sem Diego, o agente não existe.
- **Regra aprendida:** Qualquer melhoria que não resolve o gargalo "Diego como único ponto de contato" vai ter retorno limitado.

### 2. PIPELINE tl;dv → AÇÃO → RASTREAMENTO NÃO EXISTE
- Reunião ocorre → tl;dv captura → Morfeu processa → Telegram alerta Diego → **fim**
- Itens de ação gerados em reunião não entram automaticamente em `pending.md`
- Após 12 dias (1:1 Diego/Gustavo de 25/02 → 08/03): nenhum item verificado ou rastreado
- **Regra aprendida:** Captura sem accountability não gera resultado. O pipeline mais valioso do sistema está incompleto pela metade mais importante.

### 3. JOBS CRÍTICOS COM FALHAS SILENCIOSAS
- Daily Briefing (P0): 50% de falha nos últimos 7 dias (3ok/3err)
- Watchdog de Crons: 43% de falha (4ok/3err) — o monitor que deveria detectar isso também falha
- Briefing Dom Coleta: 0% de sucesso (completamente quebrado)
- **Regra aprendida:** Jobs críticos precisam de verificação ativa, não só logging. O Watchdog falhando é o pior cenário possível — quem audita o auditor?

### 4. POLÍTICA DE LLM É DOCUMENTAÇÃO, NÃO ENFORCEMENT
- LLM Policy v2.1 é sofisticada e bem redigida
- Mas pools/circuit breaker/DLQ/quota tracking não existem nativamente no OpenClaw
- O enforcement real são regras embutidas em cada prompt de cada job (`if remains < X, NO_REPLY`)
- **Regra aprendida:** Tratar a policy como "intenção documentada", não como "mecanismo ativo". Compliance depende de cada job individualmente.

### 5. DESEQUILÍBRIO ESTRUTURAL DE AUTOMAÇÃO
- WS3 (Praças) concentra 10+ jobs de automação — com dados zerados
- WS1, WS2, WS4, WS5, WS6, WS7 = zero automação — com kickoffs não realizados
- Lara: papel declarado de secretária executiva → 1 job ativo (Smart Email Scan)
- **Regra aprendida:** Automação sem dado de entrada útil é ruído. Vale mais 1 job por WS com dado real do que 10 jobs para um WS com campos `a definir`.

### 6. DIEGO COMO OPERADOR, NÃO SÓ SPONSOR (PADRÃO OBSERVADO EM REUNIÕES)
- No 1:1 com Gustavo: Diego instrui como limpar CRM, com quem falar, como estruturar funil
- No CCR Corretores: Diego diz a Ester o que criar, com quem falar, qual conteúdo
- **Consequência:** Time opera por instrução de Diego, não por método autônomo → não escala
- **Regra aprendida:** DRIs que recebem instrução de Diego não são DRIs — são executores. O papel de sponsor implica cobrar método, não ensinar operação.

### 7. SEMANAL COMERCIAL 09/03 — SINAIS ESTRATÉGICOS
- Z2 contribui **32,8% do MRR** — peso real, não periférico
- CRI está sendo visto como **caminho de crescimento acelerado** (nova lei tributária → oportunidade)
- Povo sul menos aberto a ligações que nordeste → estratégia de abordagem diferente
- Paraná lidera distribuição de agendamentos BDR por causa do calendário de eventos → eventos como motor de pipeline é dado, não teoria

---

## 🔑 Sessão: Curadoria WS1 + WS2 + WS3 (Workstreams H1)
*Data: 2026-03-07 | Sessão: Curadoria de Workstreams*

### 1. CURADORIA SIGUE PROTOCOLO RÍGIDO
- Não reinventar o WS — apenas consolidar e formalizar
- Fontes de verdade: charters + respostas de Diego
- Conflitos entre docs e charter = prevalecem decisões mais recentes de Diego

### 2. PRINCÍPIO DO MODO SUPERVISOR
- Larissa como "Supervisora de Curadoria" — não redesenha, apenas enriquece e revisa
- Cada WS curado segue: Resumo canônico → O que charter cobre bem → Lacunas → Conflitos → Perguntas → C1/C2/C3 → Backlog → Evidência → Baseline → Pré-work → Classificação

### 3. CLASSIFICAÇÃO FINAL
- **A)** Pronto para kickoff com pré-work padrão
- **B)** Precisa de decisões antes do kickoff
- **C)** Precisa de mais base documental antes do kickoff

### 4. DIFERENÇA ENTRE WS1 E WS3 (FRONTEIRA CRÍTICA)
- WS1 = base geral de corretores / comunicação digital / escala / cadência contínua
- WS3 = ativação territorial e estratégica por praça (mais presencial, mais específica)
- Regra: WS1 faz digital, WS3 faz territorial

### 5. WS2: TIME COMERCIAL EXECUTA, NÃO FUNCTION SEPARADA
- CX-DL NÃO é função separada — é responsabilidade do time comercial
- BDRs (Jade, Mirla) são operadores principais
- Closer participa quando necessário
- CS é ponte futura, não executor fixo

### 6. MICROPATCH FINAL
- Ajustes finos de precisão sem reabrir conceito
- Baseline conhecidos: WS1 (zero), WS2 (1268 DLs)
- Classificação pode ser mantida mesmo com ajustes

### 5. WS5 — Marketing e Conteúdo: Modo Leve H1
- WS5 em H1 deve ser leve: eventos → ativos → evidência
- Foco em event-driven, não always-on robusto
- Always-on forte fica como evolução futura
- WS1 = comunicação; WS5 = ativos e narrativa
- PR/influenciadores NÃO entram como obrigação

### 6. WS6 — Programa de Incorporadoras Embaixadoras: Foco Drive-Free
- WS6 ≠ Embaixadoras genérico
- Problema: Drive como fonte → Órulo não vira fonte de verdade
- Tese: fonte de verdade > visibilidade isolada
- Métrica soberana: % drive-free por Praça
- H1: mapear incorporadoras, status drive-free, critérios mínimos, evidência simples
- Sem score sofisticado, sem cashback como centro, sem níveis obrigatórios

## 🔑 Sessão: WS4, WS5, WS6 — Consolidação Final (Workstreams H1)
*Data: 2026-03-08 | Sessão: Refinamento e consolidação final*

### 1. PRINCÍPIO DA SIMPLICIDADE DELIBERADA
- H1 deve ser leve, simples, operacional
- Não sofisticar KPIs além do necessário
- Priorizar execução sobre instrumentação

### 2. CLASSIFICAÇÃO COMUM: A-) OU A
- WS1, WS2, WS3, WS4, WS5, WS6 = todos prontos para kickoff
- Diferença: A (pronto) vs A- (pronto com pré-work estruturado)

### 3. LIÇÕES DAS CONSOLIDAÇÕES
- WS4: CRM mínimo + hygiene + cadências SDR leves
- WS5: Event-driven > always-on em H1
- WS6: Drive-free como métrica soberana + critérios mínimos + evidência prática
- WS7: Modelo econômico por praça; tipos Full/Híbrida/Remota

### 4. REFINAMENTO WS6 — LEVE E EXECUTÁVEL
- Critérios mínimos: relevância + portfólio + disposição de substituir Drive
- Contrapartida mínima explícita
- Evidência prática definida
- Check-in mensal leve

---

## 🔑 Sessão: WS4, WS5, WS6 — Consolidação Final (Workstreams H1)
*Data: 2026-03-06 | Sessão: Implementação Fase 1 + Fase 2*

### 1. DUPLICATAS SÃO INVISÍVEIS SEM AUDITORIA
- 7 jobs duplicados existiam silenciosamente (todos com `agentId: "larissa"`)
- Desperdício de ~132 prompts/semana apenas no Check Pós-Reunião
- **Regra aprendida:** auditar jobs.json mensalmente para detectar duplicatas

### 2. CUSTO REAL É MUITO MENOR QUE ESTIMADO
- v2.0 assumia 400+ prompts/semana — errado
- Custo real: ~57–62 prompts/semana (maioria tem early-exit ou NO_REPLY)
- **Regra aprendida:** medir com runs reais antes de definir thresholds de política

### 3. MiniMax Lightning NÃO funciona no Starter
- Tentativas de usar `minimax/MiniMax-M2.5-Lightning` retornaram erro no Starter
- **Regra aprendida:** verificar plano antes de adicionar modelos; Lightning = Plano Superior

### 4. Jobs DELETADOS vs DISABLED são diferentes
- Os job IDs `e309b1a4` e `f82115ff` (Monitor tl;dv) estavam completamente **ausentes** do jobs.json
- Não bastava "reativar" — era necessário recriar do zero
- **Regra aprendida:** ao desativar jobs importante, usar `enabled: false` (não deletar)

### 5. `model=default` em systemEvent não é bug
- Job Backup Diário (`9574d0b0`) usa `session=main` + `systemEvent` — não passa por LLM
- `model=default` correto para esse tipo; não alterar por convenção
- **Regra aprendida:** classificar jobs por tipo (LLM vs systemEvent) antes de auditoria de modelos

### 6. DOIS JOBS SEM TIMEOUT IDENTIFICADOS
- Backup Diário e Check Contratos não tinham timeout explícito — risco de loop infinito
- Contratos corrigido para 120s | Backup é systemEvent (sem LLM, menos crítico)

### 7. FALLBACK `anthropic/claude-haiku-3-5` É INVÁLIDO
- Jobs antigos (Watchdog, tl;dv) usavam essa string — não é um model string válido no OpenClaw
- String correta: `anthropic/claude-haiku-3-5` não funciona; usar `anthropic/claude-sonnet-4-6`

---

## 🔑 Sessão: Governança Praças
*Data: 2026-03-05 | Sessão: Configuração Sprint Quinzenal*

---

## 🔑 DECISÕES CHAVE DO DESIGN

### 1. FLUXO 100% ASSÍNCRONO
- Escolhemos fluxo 100% assíncrono (One-Pager por e-mail, check-ins por mensagem)
- Contato quinzenal (reunião/audio/call) é ponto de enrichment, não requisito
- tl;dv como fonte de dados para enriquecer o Sprint

### 2. FONTE ÚNICA DE VERDADE
- Dados do Sprint vêm de: Diego enviando aqui OU e-mail que Morfeu lê
- Sem dependência de Google Sheets/Bitrix para dados de Sprint
- Evita duplicidade de fonte e inconsistency

### 3. CONSOLIDAÇÃO COMO PRINCÍPIO
- Dois arquivos de governance → 1 (pracas_sprint.md)
- Dois cron plans → 1 (cron_plan.yml)
- Dois watchers → 1 cron combinado (pracas-sprint-watcher)
- **Regra aprendida:** duplicates geram confusion e version conflict

### 4. D4: QUINTA FIXA > D-2 VARIÁVEL
- Lembretes fixos (quinta 09:00) são mais previsíveis para o sócio
- Não depende de injetar datas em cada cron

---

## 🛠 COMPONENTES CRIADOS

| Componente | Função |
|------------|--------|
| scripts/sprint_email_watcher.py | Monitora Gmail por One-Pager de Zanella/Kneip |
| scripts/tldv_socio_check.py | Detecta reuniões tl;dv com Sócios Locais |
| jobs/prompts/pracas_sprint_email_watcher.txt | Prompt para processar e-mail |
| jobs/prompts/pracas_tldv_socio_detector.txt | Prompt para processar reunião |
| pracas-sprint-watcher (cron) | Roda a cada 2h, seg-sex 08h-20h |

---

## 📊 LIÇÕES OPERACIONAIS

### Regra de Segurança Implementada
- Nenhum job envia e-mail automaticamente
- Sempre: rascunho + INSTRUÇÕES PARA LARA + "OK para enviar?"
- Alertas Telegram: automáticos (internos)

### Dados Confirmados
- E-mail Gustavo: gustavo.torres@orulo.com.br
- Bot Lara: @larissa_personal_assistant_bot
- Nome padronizado: "Gustavo Torres" (não "Gustavo Rodrigues")

---

## ⚠️ PENDÊNCIAS EM ABERTO

- memory/projects_orulo.md precisa de dados reais (estágio + sprint por praça)
- Primeiro Sprint ainda não validado → check-ins 2x/semana não ativados

---

## 🔄 REVISÃO FUTURA

Revisar governança após 3 sprints (aprox. 6 semanas):
- Verificar se o fluxo assíncrono está funcionando
- Avaliar necessidade de reunião quinzenal
- Consolidar aprendizados em novo arquivo de lessons

---

## Lições — Sistema Operacional Comercial Órulo (11/03/2026)

### ⏳ Tático — Drive

**L1: Verificar parent antes de qualquer upload**
Morfeu fez upload de arquivo em pasta homônima dentro de área de backup. A pasta `01_GOVERNANCA_GERAL` existia em dois lugares — área oficial e área de backup. Sem verificar o parent, o arquivo foi para o lugar errado.
→ Regra: sempre `gog-morfeu drive get <parent_id> --json | jq '.file.parents[0]'` antes de escrever.

**L2: Upload .md não cria Google Doc automaticamente**
Arquivos `.md` sobem como texto/markdown, não como Google Docs. O Google só converte quando o usuário abre o arquivo no navegador. Fluxo correto: upload → usuário abre uma vez → Google cria versão editável → deletar a versão .md original.

**L3: Search no Drive retorna resultados do Drive inteiro**
`gog-morfeu drive search` busca em todo o Drive, não apenas na pasta raiz oficial. Pastas com nomes iguais em locais diferentes aparecem nos resultados. Sempre confirmar o parent do arquivo encontrado.

### ⏳ Tático — Planilha

**L4: Estrutura de colunas importa antes de inserir dados**
Na primeira inserção de backlog do WS2, a coluna `Frente` foi ignorada. Diego formalizou depois que Frente e Evidência esperada são obrigatórias. Inserir dados sem verificar a estrutura completa gera retrabalho.
→ Regra: sempre baixar e inspecionar a planilha antes de qualquer inserção.

### 🔒 Estratégico

**L5: Planilha e Drive podem estar desalinhados em DRI**
A auditoria do dia revelou que PORTFOLIO e DRIS_E_RESPONSAVEIS da planilha contradizem o MAPA_DE_RESPONSAVEIS_V1 em WS3, WS6 e WS7. O MAPA é a fonte oficial, mas a planilha estava com dados antigos. Sistema bem documentado não garante consistência automática entre fontes.

