# BRAIN COMPARISON — Morfeu vs Bruno Okamoto
## Análise Comparativa + Plano de Ação
**Data:** 2026-04-08
**DRI:** Morfeu (subagente)
**Versão:** 1.0 — Rascunho para Diego validar

---

## 1. ESTADO GERAL

### ✅ O que Morfeu TEM que Bruno NÃO TEM

• **HEARTBEAT.md** — rotina de pulso diária/semanal operacional com comandos reconhecidos
• **buddy/** — sistema de achievements + streaks (gamificação)
• **performance/** — benchmarks Jarvis 15/15, Claude Code 11/12, MODEL_GUIDE
• **skills/vendas-*** — 3 skills especializadas em analytics de vendas (Órulo-only)
• **skills/pracas/** — skill de cobertura territorial
• **skills/clawhub/** — clawhub CLI skill
• **skills/nano-pdf/** — edição de PDFs
• **skills/video-frames/** — extração de frames
• **governance/DECISION_WORKFLOW.md** — workflow formal de decisões
• **governance/IMPROVEMENT_LOOP.md** — ciclo de melhoria com 5 etapas
• **governance/STRICT_WRITE_DISCIPLINE.md** — disciplina de escrita validada
• **scripts/** — 30+ scripts operacionais (drive, email, gcal, tldv, minimax, Trinks)
• **biblioteca/** — docs estratégicos (llm_policy, integrations-setup, cron-examples)
• **crm/** — sistema de People Intelligence com templates
• **templates/** — 8 templates operacionais (checkin, cobrancas, followup, sprint, weekly)

### ⚠️ O que Morfeu TEM de forma PARCIAL vs Bruno

• **MEMORY.md** — índice existe e funcional, mas sem formalização do ciclo de archive
• **memory/*.md** — topic files existem, mas sem padronização de nomenclatura entre sessões
• **governance/SELF_HEALING_RUNBOOKS.md** — 5 runbooks criados, mas nenhum ainda validado em produção
• **governance/SUBAGENT_CONTRACT.md** — contrato existe no papel, mas nunca foi testado em cascade real

---

## 2. GAPS REAIS — O que Bruno TEM que Morfeu NÃO TEM

### 🔴 Gap P0 — Crítico para operação

**G1: skills/skill-creator/** — SKILL.md não existe como framework de autoria
📌 Por que importa: skill de criação de skills não existe no workspace. A skill `skill-creator` vem do bundle global (`openclaw/skills/skill-creator/SKILL.md`) e é acessível via busca, mas não está no workspace — o que significa que Diego não pode editá-la, auditá-la ou evoluí-la localmente. Qualquer skill nova que Morfeu precise criar depende de uma skill global que ele não controla.
🔗 Referência: `skills/skills-by-profile.md` da análise do subagente já aponta que skills customizadas são gap.

---

### 🟡 Gap P1 — Relevante mas não bloqueante

**G2: templates/MEMORY-template.md** — não existe template formal para topic files
📌 Por que importa: topic files em `memory/*.md` não seguem estrutura padronizada. Toda vez que um novo topic file é criado, não há template para garantir consistência. O formato varia de sessão para sessão. Isso degrada a capacidade de busca semântica e a legibilidade para Diego.
💡 Alternativa: não é urgente porque MEMORY.md já tem índice funcional. Mas sem template, a qualidade dos topic files depende do diligence do momento.

**G3: skills/proactive-self-improving-agent/** — skill em mandarim, teorética
📌 Por que importa: skill copiada de yanhongxi, toda em mandarim, com filosofia de "captura automática de erros". A ideia é boa mas o contexto é incompatível com Morfeu (Diego é brasileiro, time é brasileiro). Além disso, não está integrada a nenhum workflow real — é decorativa.
💡 Ação: avaliar se vale migrar a filosofia para português ou remover.

**G4: governance/TRIGGERS.md** — não existe doc de triggers e automações
📌 Por que importa: existe `HEARTBEAT.md` com comandos reconhecidos, mas não existe um documento que mapeie: trigger → rotina → ação → output. O HEARTBEAT é o "o que fazer" mas não o "quando e por quê".
💡 Depende de G2.

**G5: docs/TROUBLESHOOTING.md** — não existe guia de troubleshooting
📌 Por que importa: quando algo quebra (script falha, job para, Drive não responde), não há protocolo de diagnóstico em documento. O Morfeu resolve via scripts (`testar_scripts.py`) mas não há doc de troubleshooting para Diego ou para o próprio Morfeu.
💡 Depende de SELF_HEALING_RUNBOOKS.md estar validado (runbooks são o troubleshooting interno).

**G6: docs/CUSTOS.md** — não existe análise de custos operacionais
📌 Por que importa: Diego mencionou custo de tokens como preocupação. Não existe documento que registre: custo por modelo, custo por job, otimizações já feitas, tradeoff de quality vs cost. Sem isso, qualquer discussão de custo é ad-hoc.
💡 Não é urgente.

**G7: docs/INTEGRATIONS.md** — docs/integrations-setup.md existe mas não cobre tudo
📌 Por que importa: integrations-setup.md cobre setups de API (Gmail, Drive, Calendar) mas não há um mapa completo de: qual ferramenta → qual skill → qual script → qual job. Quando algo muda (ex: trocar modelo), não fica claro o que precisa ser atualizado.
💡 Depende de TOOLS.md estar completo (já existe, mas não cobre skills).

---

### 🟢 Gap P2 — Nice to have / Evolução

**G8: prds/immune-system.md** — PRD de immune system não existe no workspace
📌 Por que importa: o conceito de "sistema imune" (autoproteção contra prompts injection, jailbreak, vazamento) existe em `governance/UNDERCOVER_LAYER.md` mas não existe um PRD formal que descreva: ataques conhecidos, defesas implementadas, métricas de eficácia.
💡 Risco real mas já mitigado parcialmente pelo Undercover Layer.

**G9: prds/multi-agent-setup.md** — PRD de arquitetura multiagente não existe
📌 Por que importa: já existem 3 bots (Morfeu, Larissa, Claudinei) com threadBindings definidos. Mas não existe PRD formal que descreva: divisão de responsabilidades, protocolos de handover, conflitos de ownership, como escalar para novo agente.
💡 Sistema funciona na prática — PRD formal seria útil para auditoria e新規agent onboarding.

**G10: skills-by-profile reference** — arquivo da análise não está no workspace
📌 Por que importa: o subagente leu `skills/skills-by-profile.md` mas esse arquivo não está em `/root/.openclaw/workspace/skills/`. Está em algum lugar do bundle global ou foi consumido na análise. Isso significa que a recomendação de skills por perfil está disponível só no contexto do subagente, não no workspace permanente.
💡 Baixo impacto.

---

## 3. PLANO DE AÇÃO PRIORIZADO

### 🟥 P0 — Fazer agora (semana atual)

**P0.1: Avaliar e resolver skill proactive-self-improving-agent**
• Prioridade: 🔴 P0
• Item: Decidir se a skill em mandarim é removida ou portada para português com workflow real
• Esforço: Baixo
• Justificativa: Skill decorativa com contexto errado polui o workspace e pode confundir Morfeu
• Dependência: Nenhuma

**P0.2: Criar framework local de skill-creator**
• Prioridade: 🔴 P0
• Item: Criar `skills/SKILL_BUILDER.md` com guia de como criar, documentar e versionar skills no workspace
• Esforço: Médio
• Justificativa: Sem framework, qualquer skill nova é copy-paste sem padronização. Já existe `skill-creator` global mas está fora do workspace — precisamos de versão local que Diego possa editar
• Dependência: Nenhuma

---

### 🟨 P1 — Fazer nas próximas 2 semanas

**P1.1: Template padronizado para topic files**
• Prioridade: 🟡 P1
• Item: Criar `templates/TOPIC_FILE_TEMPLATE.md` — estrutura padrão (header, seções obrigatórias, footer)
• Esforço: Baixo
• Justificativa: G2 — topic files sem padrão = degradação de qualidade de busca com o tempo
• Dependência: Nenhuma

**P1.2: Documentar mapa de skills → triggers → outputs**
• Prioridade: 🟡 P1
• Item: Criar `governance/SKILLS_INVENTORY.md` — inventário de todas as skills do workspace com: nome, trigger, o que faz, quem usa
• Esforço: Baixo
• Justificativa: G7 — Diego e Morfeu precisam saber claramente o que cada skill faz e quando acioná-la
• Dependência: P0.2 (skill builder dá o formato)

**P1.3: Testar SUBAGENT_CONTRACT em cascade real**
• Prioridade: 🟡 P1
• Item: Validar o contrato de subagente na prática — rodar uma tarefa em cascade e verificar se reconciliação ocorre
• Esforço: Baixo
• Justificativa: Contrato existe mas nunca foi testado. Se falhar em produção, não queremos descobrir em momento crítico
• Dependência: Nenhuma

**P1.4: Testar SELF_HEALING_RUNBOOKS em produção**
• Prioridade: 🟡 P1
• Item: Validar os 5 runbooks de self-healing com cenários reais (job travado, memória inconsistente)
• Esforço: Baixo
• Justificativa: Runbooks criados mas não validados. Precisamos saber se funcionam antes de precisar de verdade
• Dependência: Nenhuma

---

### 🟩 P2 — Fazer no próximo mês

**P2.1: Criar docs/TROUBLESHOOTING.md**
• Prioridade: 🟢 P2
• Item: Guia de diagnóstico para os 5 problemas mais comuns (script falha, job não roda, Drive auth expira, email não envia, gcal não responde)
• Esforço: Médio
• Justificativa: G5 — quando algo quebra de madrugada, não há protocolo para Diego tentar antes de escalar
• Dependência: P1.4 (validar que runbooks funcionam antes de documentar)

**P2.2: Criar docs/CUSTOS.md**
• Prioridade: 🟢 P2
• Item: Planilha/texto com custo por modelo, por job, otimizações applied, tradeoff quality vs cost
• Esforço: Baixo
• Justificativa: G6 — Diego mencionou custo como preocupação; sem documento, qualquer análise é ad-hoc
• Dependência: P1.1

**P2.3: PRD formal multiagente (3 bots)**
• Prioridade: 🟢 P2
• Item: Criar `prds/MULTI_AGENT_SETUP.md` — arquitetura, division of labor, handover protocols, conflict resolution
• Esforço: Médio
• Justificativa: G9 — sistema de 3 bots funciona na prática mas não está documentado; novo agente ou auditoria depende de contexto oral
• Dependência: Nenhuma

**P2.4: PRD immune system**
• Prioridade: 🟢 P2
• Item: Criar `prds/IMMUNE_SYSTEM.md` — mapeamento de riscos, defesas existentes, métricas de eficácia
• Esforço: Médio
• Justificativa: G8 — Undercover Layer mitiga parcialmente; PRD formal permite auditoria e evolução controlada
• Dependência: P0.2

---

## 4. SÍNTESE — PRIORIDADES REAIS

**Foco da semana:**
• P0.1 — Remover/portar skill em mandarim
• P0.2 — Criar SKILL_BUILDER no workspace

**Foco das próximas 2 semanas:**
• P1.1 + P1.2 + P1.3 + P1.4

**Foco do próximo mês:**
• P2.1 + P2.2 + P2.3 + P2.4

---

## 5. O QUE NÃO PRECISAMOS (e por quê)

• **skills-by-profile.md no workspace** — arquivo de análise, não operacional. A recomendação de skills já está internalizada pelo Morfeu via análise do subagente.
• **Bruno's MEMORY-template.md** — Morfeu já tem MEMORY.md funcional com 3 camadas. Template seria redundante.
• **Bruno's HEARTBEAT-template.md** — Morfeu tem HEARTBEAT.md mais operacional que o template de Bruno (com comandos reconhecidos, não só estrutura).
• **Bruno's complete prompt library** — o workspace da Órulo tem contexto proprietary que não se aplica a Bruno. Não vale copiar por copiar.

---

*Documento gerado por subagente Morfeu — 2026-04-08.*
*Formato: card + bullets + emojis. Sem tabelas pipes.*
*Próximo passo: Diego valida prioridades → Morfeu executa P0.*
