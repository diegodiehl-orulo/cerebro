# LESSONS ANTIGAS — 05/03 a 16/03

*Arquivado em: 2026-03-28 — Onda 1 da Otimização de Sistema*
*Motivo: sessões supersedadas pelo sistema atual (v2.0) — preservadas para referência*

---

## Sessão: Governança Praças
*Data: 2026-03-05*

### 1. FLUXO 100% ASSÍNCRONO
- Escolhemos fluxo 100% assíncrono (One-Pager por e-mail, check-ins por mensagem)
- Contato quinzenal (reunião/audio/call) é ponto de enrichment, não requisito
- tl;dv como fonte de dados para enriquecer o Sprint

### 2. FONTE ÚNICA DE VERDADE
- Dados do Sprint vêm de: Diego enviando aqui OU e-mail que Morfeu lê
- Sem dependência de Google Sheets/Bitrix para dados de Sprint

### 3. CONSOLIDAÇÃO COMO PRINCÍPIO
- Dois arquivos de governance → 1 (pracas_sprint.md)
- Dois cron plans → 1 (cron_plan.yml)
- **Regra aprendida:** duplicates geram confusion e version conflict

### 4. D4: QUINTA FIXA > D-2 VARIÁVEL
- Lembretes fixos (quinta 09:00) são mais previsíveis para o sócio

---

## Sessão: Implementação Fase 1 + Fase 2
*Data: 2026-03-06*

### 1. DUPLICATAS SÃO INVISÍVEIS SEM AUDITORIA
- 7 jobs duplicados existiam silenciosamente
- **Regra:** auditar jobs.json mensalmente para detectar duplicatas

### 2. CUSTO REAL É MUITO MENOR QUE ESTIMADO
- Custo real: ~57–62 prompts/semana (maioria tem early-exit ou NO_REPLY)

### 3. MiniMax Lightning NÃO funciona no Starter
- **Regra:** verificar plano antes de adicionar modelos

### 4. Jobs DELETADOS vs DISABLED são diferentes
- **Regra:** ao desativar jobs importante, usar `enabled: false` (não deletar)

### 5. `model=default` em systemEvent não é bug
- **Regra:** classificar jobs por tipo (LLM vs systemEvent) antes de auditoria

### 6. DOIS JOBS SEM TIMEOUT IDENTIFICADOS
- Backup Diário e Check Contratos não tinham timeout explícito

### 7. FALLBACK `anthropic/claude-haiku-3-5` É INVÁLIDO
- String correta: `anthropic/claude-sonnet-4-6`

---

## Sessão: Curadoria WS1 + WS2 + WS3
*Data: 2026-03-07*

### 1. CURADORIA SIGUE PROTOCOLO RÍGIDO
- Não reinventar o WS — apenas consolidar e formalizar
- Conflitos entre docs e charter = prevalecem decisões mais recentes de Diego

### 2. PRINCÍPIO DO MODO SUPERVISOR
- Larissa como "Supervisora de Curadoria" — não redesenha, apenas enriquece e revisa

### 3. DIFERENÇA ENTRE WS1 E WS3 (FRONTEIRA CRÍTICA)
- WS1 = base geral de corretores / comunicação digital / escala
- WS3 = ativação territorial e estratégica por praça (mais presencial)
- Regra: WS1 faz digital, WS3 faz territorial

### 4. WS2: TIME COMERCIAL EXECUTA, NÃO FUNCTION SEPARADA
- CX-DL NÃO é função separada — é responsabilidade do time comercial

---

## Sessão: WS4, WS5, WS6 — Consolidação Final
*Data: 2026-03-08*

### 1. PRINCÍPIO DA SIMPLICIDADE DELIBERADA
- H1 deve ser leve, simples, operacional
- Não sofisticar KPIs além do necessário

### 2. CLASSIFICAÇÃO COMUM: A-) OU A
- WS1, WS2, WS3, WS4, WS5, WS6 = todos prontos para kickoff

### 3. LIÇÕES DAS CONSOLIDAÇÕES
- WS4: CRM mínimo + hygiene + cadências SDR leves
- WS5: Event-driven > always-on em H1
- WS6: Drive-free como métrica soberana + critérios mínimos + evidência prática

### 4. REFINAMENTO WS6 — LEVE E EXECUTÁVEL
- Critérios mínimos: relevância + portfólio + disposição de substituir Drive

---

## Sessão: Diagnóstico Estrutural Órulo — Etapas 4 e 5
*Data: 2026-03-09*

### 1. O AGENTE É PESSOAL, NÃO OPERACIONAL
- O agente é cérebro auxiliar para Diego individualmente
- Onde o time opera sem Diego, o agente não existe

### 2. PIPELINE tl;dv → AÇÃO → RASTREAMENTO NÃO EXISTE
- Reunião ocorre → tl;dv captura → Morfeu processa → Telegram alerta → **fim**
- **Regra aprendida:** Captura sem accountability não gera resultado

### 3. JOBS CRÍTICOS COM FALHAS SILENCIOSAS
- Daily Briefing (P0): 50% de falha
- Watchdog de Crons: 43% de falha

### 4. POLÍTICA DE LLM É DOCUMENTAÇÃO, NÃO ENFORCEMENT
- **Regra aprendida:** Tratar a policy como "intenção documentada", não como "mecanismo ativo"

### 5. DESEQUILÍBRIO ESTRUTURAL DE AUTOMAÇÃO
- WS3 concentra 10+ jobs de automação — com dados zerados

### 6. DIEGO COMO OPERADOR, NÃO SÓ SPONSOR
- DRIs que recebem instrução de Diego não são DRIs — são executores

---

## Sessão: Estabilização de Rotinas + Sprint 02 das Praças
*Data: 2026-03-16*

### 1. ROTINA SEM FONTE DE DADOS CONFIÁVEL É RUÍDO, NÃO VALOR
- Daily Briefing com 50% de falha e pending.md inconsistente

### 2. ONE-PAGER DE SPRINT ≠ RELATÓRIO DE SPRINT
- Um olha para frente, o outro presta contas para trás

### 3. SPRINT 01 DE VITÓRIA — MODELO FUNCIONA (EVIDÊNCIA REAL)
- Kneip fechou R$ 4.195 de MRR no sprint (meta: R$ 1.311)

### 4. ESTRUTURA PRONTA NÃO É OPERAÇÃO INICIADA
- 5 dias depois de 11/03: 6 de 7 workstreams sem kickoff realizado

---

## Lições — Sistema Operacional Comercial Órulo (11/03/2026)

### ⏳ Tático — Drive

**L1: Verificar parent antes de qualquer upload**
→ Regra: sempre `gog-morfeu drive get <parent_id> --json | jq '.file.parents[0]'` antes de escrever.

**L2: Upload .md não cria Google Doc automaticamente**
Arquivos `.md` sobem como texto/markdown, não como Google Docs.

**L3: Search no Drive retorna resultados do Drive inteiro**
Sempre confirmar o parent do arquivo encontrado.

### ⏳ Tático — Planilha

**L4: Estrutura de colunas importa antes de inserir dados**
→ Regra: sempre baixar e inspecionar a planilha antes de qualquer inserção.

### 🔒 Estratégico

**L5: Planilha e Drive podem estar desalinhados em DRI**
Sistema bem documentado não garante consistência automática entre fontes.
