# 06_ARQUITETURA_RECOMENDADA.md — Auditoria Estrutural

> **Etapa:** 6/6 — Avaliação de Arquitetura Futura
> **Data:** 2026-03-08
> **Base:** 02_governanca_workstreams.md + 03_operacao_externa.md + 04_interface_time.md + 05_infra_agente.md

---

## 1. ESTADO REAL (Síntese das Etapas Anteriores)

Antes de comparar cenários, os fatos que fundamentam a decisão:

| Dimensão | Estado |
|----------|--------|
| 7 WS com estrutura documental | ✅ Existe |
| 7 WS com operação real | ❌ Não existe |
| Praças com governança funcional | ✅ 6 crons ativos |
| Tracking de evolução WS | ❌ Nenhum cron |
| Agente com 11 funções | ✅ Sobrecarregado |
| Diego como sponsor/gargalo | ✅ 7/7 WS + 80 alertas/sem |
| Mayumi como DRI sobrecarregada | ✅ 4/7 WS |
| Time com ferramenta própria | ❌ Não |
| Memória de estado de WS | ❌ Não existe |

---

## 2. COMPARAÇÃO DOS 4 CENÁRIOS

---

### CENÁRIO A — Manter Agente Único Centralizado

**Descrição:** Morfeu continua sendo o único agente, absorvendo tudo: praças, WS, operação pessoal, memória, briefings, saúde técnica, e-mails, tl;dv, livro, Trinks, etc.

| Aspecto | Avaliação |
|---------|-----------|
| **Vantagens** | Simplicidade operacional; um único ponto de configuração; contexto unificado; sem risco de dessincronia entre agentes |
| **Desvantagens** | 11 funções em 1 agente; sobrecarga de contexto; sem diferenciação entre urgência e importância; risco de colapso cognitivo na sessão |
| **Riscos** | Governo sem governança WS continua zero; Diego continua como gargalo absoluto; 80+ alertas/semana sem priorização |
| **Complexidade** | Baixa — não muda nada |
| **Clareza operacional** | Baixa — tudo misturado |
| **Sobrecarga cognitiva** | 🔴 Alta — Diego recebe tudo |
| **Dependência Diego** | 🔴 Não reduz |
| **Adoção pelo time** | ❌ Time não muda — continua sem ferramenta |
| **Quando faz sentido** | Se o problema for apenas falta de execução dos kickoffs (problema humano, não técnico) |
| **Quando não faz sentido** | Se o objetivo for reduzir dependência de Diego ou aumentar capacidade autônoma do time |

---

### CENÁRIO B — Criar Agente Dedicado de Governança / PMO Estratégico

**Descrição:** Criar um agente separado (ex: "Morfeu-PMO") dedicado exclusivamente à governança dos 7 WS: tracking de touch, alertas de cadência, consolidação de pulses, relatório de dias_since_touch, digest semanal de WS.

| Aspecto | Avaliação |
|---------|-----------|
| **Vantagens** | Separação clara entre operação pessoal (Morfeu) e governança estratégica (PMO); tracking de WS pode ser automatizado; foco cognitivo no agente PMO |
| **Desvantagens** | Necessita de sincronização de memória entre agentes; risco de duplicação de contexto; WS ainda sem execução (o problema não é falta de tracking, é falta de kickoffs) |
| **Riscos** | PMO só funciona se os WS estiverem operando — atualmente não operam; risco de criar complexidade sem resolver o problema raiz (falta de kickoff + execução) |
| **Complexidade** | Alta — novo agente, nova sessão, sincronização de memória |
| **Clareza operacional** | Média — mais clara para WS, mas fragmenta visão para Diego |
| **Sobrecarga cognitiva** | 🟡 Reduz para WS — mas cria novo canal |
| **Dependência Diego** | 🟡 Leve redução se PMO puder cobrar DRI diretamente |
| **Adoção pelo time** | ⚠️ Time ainda precisa operar os WS |
| **Quando faz sentido** | Quando WS estiverem operando (kickoffs feitos) e precisarem de tracking automatizado |
| **Quando não faz sentido** | Agora — os WS não operam, então trackear estado vazio não resolve nada |

---

### CENÁRIO C — Bot Operacional Telegram + Agente de Governança

**Descrição:** Criar um bot Telegram dedicado à operação do time (check-ins, updates de WS, registro de one-pagers, cobrança de evidências) com Morfeu como agente estratégico/cognitivo. O bot absorve interações rotineiras do time, liberando Morfeu para análise estratégica.

| Aspecto | Avaliação |
|---------|-----------|
| **Vantagens** | Equipe pode interagir com o sistema sem passar por Diego; reduz notificações no canal de Diego; permite input direto do DRI (Mayumi, Gustavo) sem mediação |
| **Desvantagens** | Requer desenvolvimento de bot dedicado; necessita de separação de permissões; risk of fragmentação; dois sistemas para Diego gerenciar; time precisa de onboarding |
| **Riscos** | Bot sem adoção = custo sem retorno; DRIs precisam engajar; Mayumi sobrecarregada pode não usar |
| **Complexidade** | 🔴 Muito alta — novo bot, integração, onboarding do time |
| **Clareza operacional** | Alta — canal separado para time |
| **Sobrecarga cognitiva** | 🟢 Reduz para Diego — se time usar |
| **Dependência Diego** | 🟢 Reduz significativamente — se time adotar |
| **Adoção pelo time** | ⚠️ Depende de motivação e treinamento |
| **Quando faz sentido** | Quando WS estiverem operando e time estiver engajado com o método |
| **Quando não faz sentido** | Agora — WS não operam, time não tem ferramenta básica, Mayumi sobrecarregada |

---

### CENÁRIO D — Separar Depois, Mas Não Agora

**Descrição:** Manter agente único, mas executar os kickoffs dos 7 WS, popular o tracking, gerar os primeiros pulses, e só então avaliar se separação faz sentido. Consolidar o que existe antes de criar nova complexidade.

| Aspecto | Avaliação |
|---------|-----------|
| **Vantagens** | Não cria complexidade nova antes de resolver o problema raiz; foca no que importa agora (kickoffs + execução); barato; risco zero de dessincronia |
| **Desvantagens** | Não resolve a sobrecarga de funções do agente; Diego continua como gargalo; Mayumi continua sobrecarregada |
| **Riscos** | Sem separação, WS podem continuar como documentação; problema de governança pode persistir indefinidamente |
| **Complexidade** | 🟢 Baixa — não muda arquitetura |
| **Clareza operacional** | 🟡 Não piora, mas não melhora estruturalmente |
| **Sobrecarga cognitiva** | 🟡 Não piora, pode melhorar com melhor priorização de alertas |
| **Dependência Diego** | 🟡 Não reduz automaticamente — depende de execução de kickoffs |
| **Adoção pelo time** | ⚠️ Depende dos kickoffs serem executados |
| **Quando faz sentido** | Agora — o problema real é falta de execução, não falta de arquitetura |
| **Quando não faz sentido** | Se os kickoffs forem feitos e o volume crescer — aí separação faz sentido |

---

## 3. TRADE-OFFS

### 3.1 Trade-off Central

| Opção | Resolve o problema? | Cria nova complexidade? |
|-------|---------------------|------------------------|
| A — Manter igual | ❌ Não | ❌ Não |
| B — PMO dedicado | ⚠️ Parcialmente | 🔴 Sim |
| C — Bot + Agente | ✅ Potencialmente | 🔴 Muito |
| D — Separar depois | ✅ Potencialmente | ❌ Não |

### 3.2 Trade-off de Timing

**O problema real não é arquitetura — é execução.**

- 7 WS têm estrutura documental completa mas **zero ciclos rodados**
- Criar um PMO ou bot para trackear WS que não operam é **criar overhead sem valor**
- O problema raiz é: **kickoffs não foram executados**
- Solução primária: **executar os kickoffs** — não mudar a arquitetura

### 3.3 Trade-off de Complexidade

| Dimensão | Cenário A/D | Cenário B | Cenário C |
|----------|-------------|-----------|-----------|
| Configuração | Baixa | Alta | Muito Alta |
| Manutenção | Baixa | Média | Alta |
| Risco de falha | Baixo | Médio | Alto |
| Valor gerado agora | Médio | Baixo | Baixo |
| Valor potencial | Médio | Alto | Alto |

---

## 4. RECOMENDAÇÃO FINAL

**RECOMENDAÇÃO: CENÁRIO D — Separar Depois, Mas Não Agora**

### 4.1 Fundamentação

A decisão é baseada no estado real encontrado, não em preferência arquitetural:

1. **O problema raiz é execução, não arquitetura.** Os 7 WS têm estrutura. Não foram kickoffados. Criar agente PMO para trackear WS que não operam é burocracia.

2. **A sobrecarga do agente é real, mas o remédio errado é pior que a doença.** Adicionar um segundo agente (PMO ou bot) antes de resolver o problema de execução cria sincronização, manutenção e cognitive load sem retorno imediato.

3. **O sistema de praças funciona e é o modelo.** Praças têm 6 crons, praças_sprint.md v2.0, e evidência de operação (lastRunStatus: ok). Isso mostra que o agente único consegue sustentar quando o processo está definido. A questão é replicar isso para os WS.

4. **O gargalo é humano, não técnico.** Diego é sponsor de 7/7 WS. Mayumi é DRI de 4/7. Os kickoffs não aconteceram. Mudar arquitetura não resolve isso.

### 4.2 O Que Deve Ser Feito Antes de Separar

| Ação | Prazo | Dono |
|------|-------|------|
| Executar kickoff WS1 | Sprint 01 | Diego + Mayumi |
| Executar kickoff WS2 | Sprint 01 | Diego + Gustavo |
| Executar kickoff WS4 | Sprint 01 | Diego + Gustavo |
| Popular touch tracking (WS1-WS7) | Após kickoffs | Cada DRI |
| Popular projects_orulo.md | Imediato | Diego |
| Criar cron de alerta days_since_touch | Após kickoffs | Morfeu |
| Gerar primeiro pulse real (qualquer WS) | Ciclo 1 | DRI do WS |
| Resolver sobrecarga Mayumi (4 WS) | Imediato | Diego |
| Definir se Eduardo+Felipe assumem WS7 | Imediato | Diego |

---

## 5. CONDIÇÕES PARA IMPLANTAÇÃO FUTURA (B ou C)

### 5.1 Quando o Cenário B (PMO dedicado) faz sentido

- [ ] WS1-WS4 com pelo menos 2 ciclos executados
- [ ] Touch tracking populado em 5+/7 WS
- [ ] Pelo menos 3 pulses reais gerados
- [ ] Diego precisando de separação explícita (sobrecarga comprovada)
- [ ] Mayumi com DRI redistribuída (WS1, WS3, WS5 → 3 DRIs diferentes)

### 5.2 Quando o Cenário C (Bot + Agente) faz sentido

- [ ] WS1-WS7 operacionais por pelo menos 1 trimestre
- [ ] Mayumi e Gustavo engajados com o sistema
- [ ] Time pedindo acesso direto ao sistema (demanda real)
- [ ] Volume de interações superando capacidade de Diego como mediador
- [ ] Estrutura de permissões por DRI resolvida

---

## 6. PENDÊNCIAS CRÍTICAS PARA CONSOLIDAÇÃO MANUAL POSTERIOR

Estas são as pendências que devem ser resolvidas **antes** de qualquer consolidação ou decisão estratégica:

### 6.1 Pendências de Execução (Urgente)

| Pendência | Dono | Impacto |
|-----------|------|---------|
| Kickoffs WS1-WS7 não executados | Diego + DRIs | Sistema não saiu do papel |
| projects_orulo.md incompleto | Diego | Crons de praças operam sem dado real |
| Touch tracking vazio (7/7) | DRIs | Indicador-âncora inútil |
| WS7 sem DRI ativo | Diego | Eduardo+Felipe não aceitaram |

### 6.2 Pendências de Governança (Importante)

| Pendência | Dono | Impacto |
|-----------|------|---------|
| Sobrecarga Mayumi (4 WS) | Diego | Risco de colapso operacional |
| WS5 dependente de social media | Diego | WS parado |
| WS3 vs pracas_sprint (duplicação) | Diego | Confusão de escopo |
| Bitrix "somente referência" (WS4) | Diego | WS4 sem execução |

### 6.3 Pendências Técnicas (Correção)

| Pendência | Dono | Impacto |
|-----------|------|---------|
| 3 crons com erros | Morfeu | Watchdog, Briefing Dom, Email Qui |
| 4 prompts orphaned | Morfeu | sprint_checkpoint, facilitator, followup_tracker, reminder |
| memory/feedback/ inexistente | Morfeu | Referenciado no MEMORY.md |
| Heartbeat [PESSOAL] ausente | Diego + Morfeu | Stub sem conteúdo |

---

## 7. RESUMO FINAL

### Estado do Sistema

| Dimensão | Avaliação |
|----------|-----------|
| **Como sistema de execução estratégica** | ❌ Não opera — WS sem kickoff |
| **Como sistema de governança dos 7 WS** | ❌ Documentação, não operação |
| **Como sistema de memória organizacional** | ✅ Parcialmente — pessoal/praças sim, WS não |
| **Como sistema de aprendizado contínuo** | ⚠️ Parcial — madrugada + harvester, não WS |
| **Como sistema de melhoria incremental** | ⚠️ Parcial — para Diego, não para time |
| **Como sistema de coordenação** | ❌ Diego é gargalo — time sem ferramenta |

### Recomendação

> **SEPARAR DEPOIS, MAS NÃO AGORA.**
>
> O problema não é arquitetura. É execução.
> Antes de criar complexidade nova, executar os kickoffs.
> Quando WS1-WS4 estiverem com 2+ ciclos rodados, reavaliar Cenário B.

---

*Fim da Etapa 6. Diagnóstico completo.*
