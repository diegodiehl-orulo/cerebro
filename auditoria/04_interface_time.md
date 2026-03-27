# 04_INTERFACE_TIME.md — Auditoria Estrutural

> **Etapa:** 4/6 — Interface com o Time
> **Data:** 2026-03-08
> **Base:** 01_inventario_sistema.md + 02_governanca_workstreams.md + 03_operacao_externa.md

---

## 1. MAPA DOS RITUAIS

### 1.1 Rituais Definidos (Documentados)

| Ritual | Frequência | Dono | Output Esperado | Status |
|--------|-----------|------|-----------------|--------|
| Kickoff WS | Uma vez | DRI do WS | Charter + Plan + Backlog | ❌ Não executado (0/7) |
| Sprint Quinzenal | 14 dias | DRI do WS | One-Pager + C1/C2/C3 | ❌ Sem evidência |
| WS Pulse | Quinzenal | DRI do WS | Pulse com evidência | ❌ Template vazio (0/7) |
| Check-in Praças | 2x/sem | Morfeu → Diego | Telegram + rascunho | ✅ Ativo (6 crons) |
| Reunião Quinzenal | Quinzenal | Sponsor (Diego) | Ata + próximo ciclo | ❌ Não documentado |
| Revisão Semanal | Sex 16h | Morfeu | Telegram briefing | ✅ Ativo (cron) |
| Daily Briefing | Seg-Sex 08:45 | Morfeu | Telegram | ✅ Ativo (cron) |
| Auditoria pending | Sex 17h | Morfeu | Telegram alerta | ✅ Ativo (cron) |

### 1.2 Rituais Ativos (Crons)

| Cron | Frequência | Função | Evidência de Uso |
|------|-----------|--------|------------------|
| pracas-pulse-2xweek | Ter+Sex 09h | Pulse praças | ✅ 6 crons ativos |
| pracas-sprint-checkin | Qua+Sex 09h | Check-in | ✅ Ativo |
| pracas-sprint-reminder | Qui 09:30 | Lembrete | ✅ Ativo |
| pracas-weekly-scan | Seg 08:30 | Scan semanal | ✅ Ativo |
| Revisão Semanal | Sex 16h | Briefing | ✅ lastRunStatus: ok |
| Daily Briefing | Seg-Sex 08:45 | Dia | ✅ lastRunStatus: ok |
| Auditoria pending | Sex 17h | Limpeza | ✅ lastRunStatus: ok |

### 1.3 Rituais Não Operacionais

| Ritual | Status | Por que não opera |
|--------|--------|------------------|
| Kickoff WS | ❌ Não executado | Sem evidência em nenhum WS |
| WS Pulse | ❌ Template vazio | 0/7 populado |
| Reunião Quinzenal WS | ❌ Não documentado | Não há registro |
| Check-in WS (não praças) | ❌ Inexistente | Só praças têm crons |

---

## 2. AVALIAÇÃO DE UTILIDADE PRÁTICA

### 2.1 Rituais que FUNCIONAM

| Ritual | Avaliação | Por que funciona |
|--------|-----------|------------------|
| **Check-in Praças** | ✅ Útil | Crons ativos, output claro (Telegram + rascunho) |
| **Daily Briefing** | ✅ Útil | Rotina estabelecida, dados consolidados |
| **Revisão Semanal** | ✅ Útil | Estrutura clara, lastRunStatus ok |
| **Auditoria pending** | ✅ Útil | Verificação sistemática de pendências |

### 2.2 Rituais que NÃO FUNCIONAM

| Ritual | Avaliação | Por que não funciona |
|--------|-----------|---------------------|
| **Kickoff WS** | ❌ Não executado | Apenas estrutura documental |
| **WS Pulse** | ❌ Template vazio | Não há evidência de execução |
| **Sprint Quinzenal WS** | ❌ Inexistente | Só funciona para praças (via pracas_sprint) |
| **Reunião Quinzenal** | ❌ Não documentada | Não há registro de meetings |

### 2.3 Análise de Utilidade

| Métrica | Dado |
|---------|------|
| Rituais documentados | 8 |
| Rituais ativos (crons) | 6 |
| Rituais operacionais | 4 (apenas praças + revisão) |
| Rituais WS (não praças) | 0 (não operam) |

**Veredicto:** Apenas **praças** têm rituais operacionais. Os **7 WS** não têm rituais funcionando.

---

## 3. GARGALOS DE COORDENAÇÃO

### 3.1 Gargalo: Input Manual

| Problema | Evidência | Impacto |
|----------|-----------|---------|
| One-Pager received manually | Diego cola e-mail no Morfeu | Sem automação de receive |
| Dados de sprint | Diego alimenta projects_orulo.md manualmente | Sem sistema de input |
| Cobrança manual | Lara envia após OK de Diego | Sem autonomia |

### 3.2 Gargalo: Ausência de Ferramenta do Time

| Problema | Evidência | Impacto |
|----------|-----------|---------|
| Corretores sem sistema | WS1 não opera | Time sem ferramenta |
| DLs sem tracking | WS2 não opera | BDRs sem sistema |
| Bitrix "referência" | WS4 não opera |CRM não usado |
| Drive como fonte | WS6 quer替代MAS não implementada | Meta vaporware |

### 3.3 Gargalo: Sobrecarga de Decisão

| Problema | Evidência | Impacto |
|----------|-----------|---------|
| Sponsor único | Diego = 7/7 WS | Gargalo absoluto |
| Mayumi sobrecarregada | 4 WS (WS1,3,5,6) | Risco de burnout |
| DRI inativo | WS7 (Eduardo+Felipe) não aceitaram | WS7 parado |

### 3.4 Gargalo: Comunicação Fragmentada

| Problema | Evidência | Impacto |
|----------|-----------|---------|
| Múltiplos canais | Telegram, e-mail, Drive, Bitrix | Confusão |
| Sem canal único | Cada script/output usa canal diferente | Time não sabe onde olhar |
| output do Morfeu | 10+ crons enviam Telegram para Diego | Sobrecarga de notificação |

---

## 4. LACUNAS

### 4.1 Lacunas de Rituais

| Lacuna | Status | Impacto |
|--------|--------|---------|
| WS Pulse não executado | 0/7 populado | Sem evidência de cadência |
| Kickoff WS não executado | 0/7 evidência | Sistema não saiu do papel |
| Reunião quinzenal WS | Não documentada | Não há registro |
| Check-in WS (não praças) | Inexistente | Governança fragmentada |

### 4.2 Lacunas de Comunicação

| Lacuna | Status | Impacto |
|--------|--------|---------|
| Canal único para time | Inexistente | Fragmentação |
| Feedback loop | Inexistente | Time não sabe resultado |
| Visibilidade de progresso | Inexistente | WS não tem dashboard |

### 4.3 Lacunas de Execução

| Lacuna | Status | Impacto |
|--------|--------|---------|
| Ferramenta do time | Inexistente | Time depende de Diego/Morfeu |
| Automação de input | Inexistente | Manual only |
| Autonomia de envio | Inexistente | Tudo depende de OK |

---

## 5. RISCOS HUMANOS E OPERACIONAIS

### 5.1 Risco: Sobrecarga do Sponsor

| Indicador | Dado |
|-----------|------|
| WS como sponsor | Diego = 7/7 |
| Crons que alertam Diego | ~10+ (Telegram) |
| Pendências com Dono = Diego | Múltiplas em pending.md |

**Veredicto:** Se Diego parar, o sistema para. Não há distribuição de carga.

### 5.2 Risco: Burnout de DRI

| Indicador | Dado |
|-----------|------|
| Mayumi = DRI | WS1, WS3, WS5, WS6 (4 WS) |
| WS dependem dela | Comunicação, praças, marketing, embaixadoras |
| Sem suporte estrutural | Sem ferramenta, sem time dedicado |

**Veredicto:** Mayumi é ponto único de falha para 4 WS.

### 5.3 Risco: Time Sem Propriedade

| Indicador | Dado |
|-----------|------|
| Executor WS1 (Ester) | Não tem sistema para operar |
| BDRs WS2 (Jade, Mirla) | Sem sistema de tracking |
| WS7 (Eduardo+Felipe) | Não aceitaram DRI formalmente |

**Veredicto:** O time é executor sem ferramenta. Depende de Diego para tudo.

### 5.4 Risco: Burocracia Excessiva

| Indicador | Dado |
|-----------|------|
| "OK para executar" | Policy em AGENTS.md |
| Rascunho + OK + Lara | Múltiplos passos para enviar |
| Sem autonomia | Nada acontece sem Diego |

**Veredicto:** O sistema é seguro MAS lento. Aprovações em múltiplas camadas.

---

## 6. INSUMOS PARA ETAPA 5

### 6.1 O que avaliar na Etapa 5

A **Etapa 5 (Infraestrutura do Agente)** deve verificar:

1. **Capacidade do Morfeu:**
   - O agente consegue sustentar a governança atual?
   - Onde está sobrecarregado?

2. **Automação existente:**
   - Crons sustentam os rituais?
   - Onde há gap de automação?

3. **Proatividade:**
   - O Morfeu detecta lacunas proativamente?
   - Registra aprendizados?

### 6.2 Arquivos de Referência

| Arquivo | Leitura |
|---------|---------|
| 01_inventario_sistema.md | Inventário |
| 02_governanca_workstreams.md | WS evaluation |
| 03_operacao_externa.md | Camada externa |
| HEARTBEAT.md | Rotinas do Morfeu |
| jobs/cron_plan.yml | Crons |

### 6.3 Pergunta Chave para Etapa 5

- O Morfeu é sustentação ou sobrecarga?
- Os crons sustentam o sistema ou são complexidade adicional?

---

## 7. ACHADOS PRINCIPAIS (Etapa 4)

### ✅ O que funciona

- Check-in de praças (6 crons)
- Daily Briefing (cron ativo)
- Revisão Semanal (cron ativo)
- Auditoria pending (cron ativo)

### ❌ O que não funciona

- Kickoff WS (0/7 executado)
- WS Pulse (0/7 populado)
- Rituais WS (não operam — só praças operam)
- Reunião quinzenal (não documentada)

### ⚠️ Riscos identificados

- **Sobrecarga Diego:** 7/7 WS + 10+ crons alertando
- **Burnout Mayumi:** 4 WS como DRI
- **Time sem ferramenta:** Dependência absoluta de Diego/Morfeu
- **Burocracia:** Múltiplos níveis de aprovação
- **Comunicação fragmentada:** Múltiplos canais, sem ponto único

### 📊 Resumo

| Dimensão | Avaliação |
|----------|-----------|
| Rituais documentados | 8 |
| Rituais operacionais | 4 (apenas praças) |
| Rituais WS funcionando | 0 |
| Dependência do sponsor | 🔴 Alta |
| Capacidade operacional do time | ❌ Baixa |

---

*Fim da Etapa 4. Próxima: Etapa 5 — Infraestrutura do Agente.*
