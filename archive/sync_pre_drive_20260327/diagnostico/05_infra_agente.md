# 05_INFRA_AGENTE.md — Infraestrutura do Agente
> **Diagnóstico:** Etapa 5 de 7
> **Auditor:** Morfeu
> **Base:** 01_inventario_sistema.md + 02_governanca_workstreams.md + 03_operacao_externa.md + 04_interface_time.md + execução direta de análise de runs (7 dias), memory stats, policy files
> **Anti-alucinação:** Dados de runs reais auditados via cron/runs/*.jsonl. Políticas lidas diretamente dos arquivos. Nenhuma capacidade afirmada sem evidência de implementação.

---

## 1. MAPA DA INFRAESTRUTURA DO AGENTE

### 1.1 Camadas do sistema

```
┌─────────────────────────────────────────────────────────┐
│  CAMADA DE INTERFACE                                    │
│  Telegram (output) · task-received hook (ack)          │
│  Único canal de input/output entre Diego e agente      │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│  CAMADA DE EXECUÇÃO (Agentes)                           │
│  main · morfeu · claudinei · larissa                   │
│  29 jobs ativos | 3 agentes operacionais               │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│  CAMADA DE COGNIÇÃO                                     │
│  Modelos: MiniMax-M2.5 (primário) · Claude (fallback   │
│  manual) · Gemini (embeddings)                         │
│  Quota: MiniMax Starter 100 prompts/5h (~64 uso real)  │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│  CAMADA DE MEMÓRIA                                      │
│  SQLite: morfeu.sqlite (21MB) · claudinei (22MB) ·     │
│  larissa (21MB) · main (16MB)                          │
│  Arquivos MD: pending · projects · decisions · lessons  │
│  · people · daily/ · feedback/                         │
│  Embeddings: Gemini gemini-embedding-001 (ativo)       │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│  CAMADA DE INTEGRAÇÕES                                  │
│  Gmail · gcalcli · tl;dv · Clicksign · Vaultwarden    │
│  Backup (rsync diário) · Trinks (parcial)              │
│  AUSENTE: Bitrix · Google Drive · Z2A · WhatsApp       │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Jobs ativos por função e agente

| Categoria | Jobs ativos | Agente(s) | Frequência |
|-----------|------------|-----------|-----------|
| **Monitoramento pessoal** | Daily Briefing, Revisão Semanal, Briefings Dom | main | Diário / semanal |
| **Saúde do sistema** | Watchdog, MiniMax Health, Diagnóstico, Relatório, Erros Cron | morfeu / claudinei | Diário |
| **Governança de praças (WS3)** | sprint-watcher, check-mon, check-tue, reminder-thu, check-in-qua, check-in-sex, pulse-2x, scan-weekly, email-watcher-seg/ter | claudinei | 2h a diário |
| **Monitoramento externo** | Smart Email Scan, Monitor tl;dv, Check Contratos | larissa / claudinei | 2h / horário |
| **Memória e consolidação** | Madrugada, Harvester Memória Dom | morfeu / claudinei | Diário / semanal |
| **Projetos pessoais** | Check Livro, Cuidados Pessoais, Trinks Cabelo | claudinei / main | Diário / semanal |
| **Infraestrutura** | Backup Diário | main | Diário |
| **One-shot lembretes** | Kickoff WS2 (16/03), Tom de Voz | claudinei / main | Pontual |

---

## 2. CAPACIDADES REAIS

### 2.1 O que o agente faz bem (comprovado)

**Monitoramento passivo de inbox**
Smart Email Scan (100% taxa de sucesso, 2ok/0err): detecta contratos, propostas, reuniões, urgências. Funcionando e entregando valor real — 33 emails importantes classificados nas últimas 48h.

**Processamento de tl;dv**
Monitor tl;dv novo (100%, 4ok/0err): detecta reuniões, processa via pipeline enriquecido, entrega resumo ao Telegram. Reuniões como "1:1 Diego-Gustavo" e "Funil CRI" já capturadas.

**Backup de workspace**
Backup Diário (100%, 4ok/0err): cron às 02h UTC (05h BRT). Workspace protegido com histórico.

**Consolidação de memória noturna**
Madrugada (100%, 2ok/0err): processamento diário às 02h BRT. Harvester Memória Dom (100%, 1ok): consolidação estratégica semanal. Arquivos de memória com modificações recentes (decisions.md atualizado hoje às 09:46).

**Vigilância de praças (WS3) — parcial**
pracas-sprint-watcher (100%, 7ok/0err): rodando a cada 2h nos dias úteis. Detectaria one-pager se chegasse por email. O problema não é o job — é que os dados de entrada (C1/C2/C3) estão zerados.

**Memória semântica**
4 bases SQLite ativas: morfeu (21MB), claudinei (22MB), larissa (21MB), main (16MB). Embeddings via Gemini. Busca semântica operacional.

### 2.2 O que o agente faz com qualidade variável

**Daily Briefing (P0)**
Taxa de sucesso: **50% (3ok/3err nos últimos 7 dias)**. Este é o job mais crítico do sistema — é classificado como P0-A, mas está falhando 1 de cada 2 vezes. As 3 falhas não têm diagnóstico público registrado.

**Watchdog de Crons**
Taxa de sucesso: **57% (4ok/3err)**. O job responsável por monitorar outros jobs tem taxa de falha de 43%. Paradoxo estrutural: quem monitora o monitor?

**Briefing Dominical Coleta (16h Dom)**
Taxa de sucesso: **0% (0ok/3err, consecutiveErrors=3)**. O job de coleta de dados para o Briefing Dominical está completamente quebrado. O job de análise (17h) roda sobre dados inconsistentes.

**Check Email Qui**
Taxa de sucesso: **0% (0ok/1err — timeout)**. Timeout de 120s. Confirmado como ponto fraco.

### 2.3 O que o agente não faz (ausência documentada)

| Capacidade | Por quê não faz | Impacto |
|-----------|----------------|---------|
| Rastrear itens de ação de reuniões | Sem pipeline item→pendência automático | Ações de tl;dv somem após o Telegram |
| Monitorar WS1, WS2, WS4, WS5, WS6, WS7 | Sem prompt, sem cron | 6 de 7 WS invisíveis |
| Cobrar DRIs (Gustavo, Mayumi, Eduardo) | Sem job de cobrança interna | Time opera sem accountability |
| Ler Bitrix | Sem integração | Pipeline comercial = caixa-preta |
| Verificar execução de e-mails via Lara | Sem job de confirmação | Envios não têm registro de conclusão |
| Aprendizado contínuo de padrões | Harvester existe, mas é semanal e silencioso | Aprendizados raramente chegam ao Diego |
| Detectar `days_since_touch` de WS | Sem dados de touch nos charters | Indicador-âncora inoperante |
| Alertar sobre reuniões sem tl;dv | Sem correlação Calendar ↔ tl;dv | Reuniões não cobertas são invisíveis |

---

## 3. LIMITAÇÕES REAIS

### Limitação 1: A política de quota existe mas não é enforcement
O `sistema/llm_policy_v2.1.md` e o `jobs/quota_policy.yml` são documentos sofisticados de arquitetura. Mas o próprio documento v2.1 declara explicitamente:

> *"Pools/circuit breaker/DLQ apresentados como nativos [na v2.0] eram NÃO CONFIRMADOS. O OpenClaw não tem suporte nativo a pools de concorrência, circuit breaker de endpoint, DLQ automática, overlap control ou quota tracking em tempo real."*

**O que isso significa na prática:**
- Os `pools` (P0/P1/P2/P3) são classificações conceituais — não há runtime que as enforça
- O `circuit_breaker` no quota_policy.yml é aspiracional — não existe como mecanismo real
- O `capacity_harvester` com `activation_conditions` não está implementado como job
- A `DLQ` (dead letter queue) não existe operacionalmente
- Os `thresholds` de quota (normal/cautious/restricted) são verificados manualmente pelos próprios prompts dos jobs (via `"if remains < X, NO_REPLY"`) — não há enforcement central

**Consequência:** O sistema depende de cada job individualmente respeitar as regras da política. Se um job não implementar o gate de remains corretamente, consome quota sem controle.

### Limitação 2: Memória viva mas não retroalimenta ação
Os arquivos de memória são atualizados regularmente (decisions.md hoje, lessons.md hoje, pending.md hoje). A busca semântica funciona. Mas:

- Os itens de ação capturados pelo tl;dv não entram automaticamente no `pending.md`
- Os `daily/*.md` são notas brutas de sessão, não índices de ação
- O `harvester` de memória (semanal) consolida mas não gera itens acionáveis
- A memória cresce, mas o pipeline memória → próxima ação → responsável → follow-up não existe

A memória é excelente como **repositório retrospectivo**. É fraca como **sistema de accountability prospectivo**.

### Limitação 3: Agentes sem separação clara de escopo
O sistema tem 4 agentes (main, morfeu, claudinei, larissa), mas a separação de responsabilidade é confusa:
- **main:** briefings, revisão semanal, watchdog, contratos — generalista
- **morfeu:** saúde do MiniMax, madrugada — infraestrutura
- **claudinei:** praças, tl;dv, livro, erros de cron — operacional
- **larissa:** smart email scan — quase inativo

O `claudinei` acumulou funções demais: governança de praças (10 jobs), tl;dv, livro, auditoria de crons, check-in de sócios. Se claudinei tiver problema, múltiplas funções críticas param.

A `larissa` tem o papel mais importante declarado (secretária executiva) mas o menor escopo real (1 job ativo). Inversão de papéis documentados vs. operacionais.

### Limitação 4: Proatividade condicional, não estrutural
O sistema é proativo apenas quando os dados de entrada existem. Sem dados:
- Jobs de praças rodam e não geram sinal útil (dados zerados)
- Heartbeat verifica pendências mas retorna HEARTBEAT_OK quando tudo está "PRONTO para kickoff"
- Madrugada processa "tudo que gerou nas últimas 24h" — mas se Diego não teve sessão, há pouco para processar

A proatividade real depende de Diego estar ativo e alimentando o sistema. Em períodos de viagem ou sobrecarga, o agente opera no vácuo.

### Limitação 5: Falhas silenciosas em jobs críticos
O Daily Briefing falhou 3 de 6 vezes nos últimos 7 dias. O Watchdog falhou 3 de 7 vezes. O Briefing Dom Coleta falhou 3 de 3 vezes. Essas falhas:
- Geram `consecutiveErrors` no sistema
- Watchdog deveria detectar — mas o próprio Watchdog está falhando 43%
- Não há DLQ ou escalation automático funcional para P0

---

## 4. SOBRECARGAS

### Sobrecarga 1: WS3 concentra 60% dos jobs
10+ jobs dedicados exclusivamente à governança de praças (WS3). Os outros 6 WS têm zero automação. O sistema está desequilibrado: hiperautomatizado para WS3 (que tem dados zerados) e completamente cego para WS1, WS2, WS4, WS5, WS6, WS7.

### Sobrecarga 2: Claudinei com 14 jobs ativos
O agente claudinei concentra: 10 jobs de praças + 1 de tl;dv + 1 de livro + 1 de auditoria + 1 de check-in sócios. É o agente mais carregado. Se falhar ou tiver problema de modelo, 14 funções param simultaneamente.

### Sobrecarga 3: Infraestrutura de governança de modelos mais complexa que o necessário
O sistema tem:
- `sistema/llm_policy_v2.1.md` (política operacional)
- `sistema/llm_policy_v2.md` (versão anterior — não deletada)
- `sistema/llm_policy.md` (versão v1 — não deletada)
- `jobs/quota_policy.yml` (documentação arquitetural)
- Regras de modelo hardcoded em cada prompt de job

Três versões de política convivendo. A versão real que governa o comportamento são as regras embutidas nos prompts — as políticas em MD/YML são documentos que **descrevem** intenção, não **enforcement**.

### Sobrecarga 4: Check Pós-Reunião (desativado) ainda aparece no histórico
O job `696a5c6b` (Check Pós-Reunião, desativado) tem 35 runs nos últimos 7 dias — 33 ok, 2 err. Wait — se foi desativado, por que tem 35 runs? Isso indica que foi desativado **durante a semana** e correu muito antes disso. Representa 35 prompts gastos em um job que foi classificado como "desperdício" (132 prompts/semana). A desativação foi correta e efetiva.

### Sobrecarga 5: Memória cresce sem política de expurgação
4 bases SQLite com 21–22MB cada. `memory/daily/` com 10 arquivos. Sem política documentada de limpeza ou arquivamento. O Harvester de Memória (Dom 09h) consolida — mas não tem critério claro de quando deletar/arquivar.

---

## 5. LACUNAS DE INFRAESTRUTURA

| # | Lacuna | Impacto | Complexidade de resolver |
|---|--------|---------|------------------------|
| 1 | **Sem pipeline automático tl;dv → pending.md** | 🔴 ALTO | Média — script de extração + cron |
| 2 | **Daily Briefing (P0) com 50% de falha** | 🔴 ALTO | Baixa — diagnosticar e corrigir causa raiz |
| 3 | **Briefing Dom Coleta com 0% de sucesso** | 🔴 ALTO | Baixa — cron quebrado, recriar |
| 4 | **Watchdog falhando 43%** | 🔴 ALTO | Baixa — diagnosticar causa raiz |
| 5 | **Sem jobs para WS1, WS2, WS4, WS5, WS6, WS7** | 🟡 MÉDIO | Média — criar prompts + jobs por WS |
| 6 | **Sem cobrança automática de DRIs internos** | 🟡 MÉDIO | Média — job de "days_since_touch" por WS |
| 7 | **Larissa com 1 job ativo vs. papel declarado** | 🟡 MÉDIO | Alta — requer definição de escopo + aprovação |
| 8 | **Política de quota como documento, não enforcement** | 🟡 MÉDIO | Alta — requer suporte nativo do OpenClaw |
| 9 | **Capacity harvester não implementado** | 🟢 BAIXO | Média — criar jobs P2 de análise |
| 10 | **Sem correlação Calendar ↔ tl;dv (reuniões sem cobertura)** | 🟢 BAIXO | Alta — requer comparação de eventos |
| 11 | **3 versões de llm_policy não consolidadas** | 🟢 BAIXO | Baixa — deletar v1 e v2, manter v2.1 |

---

## 6. DIAGNÓSTICO FINAL — AS 6 PERGUNTAS

**O agente é proativo?**
Parcialmente. É reativo-inteligente: detecta emails, processa tl;dv, gera alertas. Proatividade verdadeira (antecipar sem trigger) é limitada ao Briefing Dominical (quando funciona) e à Madrugada. Para WS e time: zero proatividade — não há trigger para gerar alertas sobre DRIs, `days_since_touch` ou bloqueios de WS.

**Registra aprendizado?**
Sim, mas de forma fragmentada. `lessons.md` existe e é atualizado. O Harvester consolida semanalmente. Mas os aprendizados raramente chegam a Diego como sugestão de mudança de comportamento. A memória registra — mas não age sobre o que registrou.

**Detecta lacunas?**
Detecta o que tem dados. Lacunas com dados (ex: contrato pendente, email importante) são detectadas e alertadas. Lacunas sem dados (ex: WS2 sem pulse, DRI sem touch) são invisíveis — porque o sistema não tem acesso aos dados que permitiriam detectá-las.

**Acompanha evolução dos WS?**
Não. O sistema acompanha apenas WS3 (praças), e mesmo assim com dados zerados. Para os outros 6 WS, não há job, prompt, verificação ou alerta. A evolução dos WS existe apenas no que Diego reporta manualmente.

**Ajuda melhoria contínua?**
Potencialmente sim. Tem arquitetura para isso (harvester, lessons, decisions). Na prática, o ciclo de melhoria está incompleto: aprende → registra → **não retroalimenta operação**. O sistema aprende, mas o time não recebe o aprendizado, e o agente não age sobre ele automaticamente.

**Está sendo usado como cérebro auxiliar ou repositório passivo?**
Oscila. É cérebro auxiliar para Diego pessoalmente (briefings, alertas, agenda, emails). É repositório passivo para a operação da Órulo (WS, time, DRIs, pipeline). A distinção é clara: onde Diego interage diretamente, o agente agrega valor. Onde o time opera sem Diego, o agente não existe.

---

## 7. INSUMOS PARA A ETAPA 6 — ARQUITETURA RECOMENDADA

A Etapa 5 revelou que o sistema tem **boa arquitetura de monitoramento pessoal** e **arquitetura fraca de governança operacional**. Para a Etapa 6 propor melhorias realistas, considerar:

1. **Correções imediatas (baixa complexidade, alto impacto):**
   - Diagnosticar e corrigir Daily Briefing (50% falha)
   - Recriar Briefing Dom Coleta (0% sucesso)
   - Diagnosticar Watchdog (43% falha)
   - Deletar llm_policy v1 e v2 (manter apenas v2.1)

2. **Automações novas de alto valor (média complexidade):**
   - Pipeline tl;dv → extração de itens de ação → pending.md automático
   - Job de `days_since_touch` por WS (alerta quando > 14 dias)
   - Job de cobrança de DRIs (Gustavo/WS2+WS4, Mayumi/WS1+WS5+WS6, Eduardo/WS3)

3. **Expansão estrutural que requer decisão de Diego:**
   - Escopo real de Lara (o que ela pode enviar sem OK? Para quem?)
   - Ativação dos kickoffs (quem convoca? Via Morfeu ou manual?)
   - Canal direto do time com o agente (ou continua tudo via Diego?)

4. **O que NÃO fazer agora (complexidade alta, ganho incerto):**
   - Integração Bitrix (depende de API key + mapeamento de objetos)
   - Integração Google Drive (depende de OAuth + estrutura de pastas)
   - Integração Z2A (depende de API da plataforma)

5. **A pergunta de arquitetura central:** O sistema deve ser expandido para dar ao time acesso direto (Lara como interface do time) ou manter Diego como único ponto de contato? A resposta determina toda a arquitetura futura.

---

*Etapa 5 concluída. Próxima: `06_arquitetura_recomendada.md`*
