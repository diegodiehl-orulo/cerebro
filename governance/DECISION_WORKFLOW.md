# DECISION WORKFLOW
## F14 — Workflow de Decisão com Histórico (Sprint 4)

**Versão:** 1.0  
**Data:** 2026-04-03  
**DRI:** Morfeu (registro) + Diego (decisão)  
**Base:** Jarvis Fase 14  
**Status:** ✅ Ativo  

---

## O PROBLEMA

Antes: decisões tomadas em conversa, sem registro formal. Sem trace, sem histórico, sem efeito documentado. Morfeu perde contexto após compactação. Diego precisa re-explicar.

Agora: toda decisão estratégica tem registro estruturado com owner, SLA, outcomes e efeito pós-decisão.

---

## QUANDO REGISTRAR

**Registrar obrigatoriamente:**
- Decisões que mudam governança ou comportamento do Morfeu
- Decisões com impacto financeiro ou de equipe
- Decisões que Diego tomou após análise do Morfeu
- Decisões revertidas (com motivo)

**Não registrar:**
- Confirmações operacionais simples ("OK para enviar")
- Ajustes menores de tom ou formato
- Tarefas concluídas sem decisão envolvida

---

## TEMPLATE DE DECISÃO

```markdown
## D[NNN] — [Título curto]
**Data:** YYYY-MM-DD  
**Owner:** Diego Diehl  
**Contexto:** [1-2 linhas — por que essa decisão precisou ser tomada]  
**Opções consideradas:**  
  A) [opção] — [prós/contras em 1 linha]  
  B) [opção] — [prós/contras em 1 linha]  
**Decisão:** [opção escolhida + razão]  
**Efeito esperado:** [o que muda com essa decisão]  
**SLA de revisão:** [data para revisar se o efeito se concretizou — ou "sem prazo"]  
**Status:** Ativo | Revisado | Revertido  
**Efeito real (pós-revisão):** [preencher na revisão]  
```

---

## REGISTRO DE DECISÕES ATIVAS

### D001 — Arquitetura de memória em 3 camadas
**Data:** 2026-04-03  
**Owner:** Diego Diehl  
**Contexto:** Contexto do Morfeu crescia sem controle. Decisão estrutural para disciplinar memória.  
**Opções consideradas:**  
  A) Manter como está — risco de contexto overflow crescente  
  B) Implementar 3 camadas com regras estritas — mais trabalho inicial, mais estável  
**Decisão:** B — 3 camadas com MEMORY.md como índice leve (max 30 entradas), topic files on-demand, transcripts grep-only  
**Efeito esperado:** Contexto controlado, memória confiável, sem alucinação por dados stale  
**SLA de revisão:** 2026-05-03 (30 dias)  
**Status:** Ativo  

---

### D002 — Limite de 30 entradas no MEMORY.md
**Data:** 2026-04-03  
**Owner:** Diego Diehl  
**Contexto:** Definir teto para índice de memória evitar crescimento descontrolado.  
**Opções consideradas:**  
  A) Sem limite — cresce livremente  
  B) 30 entradas ativas + archive trimestral  
  C) 50 entradas  
**Decisão:** B — 30 entradas, disciplina de archive a cada 90 dias sem atualização  
**Efeito esperado:** Índice sempre leve e confiável  
**SLA de revisão:** Próximo archive trimestral (Q3/2026)  
**Status:** Ativo  

---

### D003 — Auto-archive de daily/ após 60 dias
**Data:** 2026-04-03  
**Owner:** Diego Diehl  
**Contexto:** Transcripts acumulando em memory/daily/ sem limpeza.  
**Decisão:** Archive automático após 60 dias de inatividade via `archive_daily.py`  
**Efeito esperado:** Pasta daily/ sempre enxuta, sem transcripts obsoletos no contexto  
**SLA de revisão:** 2026-06-03 (verificar primeiro archive automático)  
**Status:** Ativo  

---

### D004 — Strict Write: desistir na 2ª falha + alertar Diego
**Data:** 2026-04-03  
**Owner:** Diego Diehl  
**Contexto:** Sem regra clara para falha de escrita → índice podia ficar inconsistente.  
**Decisão:** Falha 1x: retry. Falha 2x: desistir + criar pending + alertar Diego  
**Efeito esperado:** Índice nunca aponta para arquivo que não existe  
**SLA de revisão:** Sem prazo fixo — revisar se houver incidente  
**Status:** Ativo  

---

### D005 — Emergência definida como prazo <15min
**Data:** 2026-04-03  
**Owner:** Diego Diehl  
**Contexto:** Precisava de definição clara de quando pular validação por urgência.  
**Decisão:** Emergência = situação crítica com prazo <15min. Único caso em que validação pode ser pulada.  
**Efeito esperado:** Morfeu não trava em situação urgente, mas também não usa emergência como desculpa  
**SLA de revisão:** Sem prazo — revisar se for acionado  
**Status:** Ativo  

---

### D006 — Subagente: escalar para Diego após 2 falhas
**Data:** 2026-04-03  
**Owner:** Diego Diehl  
**Contexto:** Sem regra clara → Morfeu podia tentar indefinidamente.  
**Decisão:** 2 falhas → escalonar para Diego com sugestão. Nunca tentar 3a vez.  
**Efeito esperado:** Diego mantém controle, Morfeu não desperdiça recursos  
**SLA de revisão:** Sem prazo — revisar se padrão mudar  
**Status:** Ativo  

---

### D007 — Máximo 3 subagentes em cascade
**Data:** 2026-04-03  
**Owner:** Diego Diehl  
**Contexto:** Cascades longos sem feedback = risco de timeout e perda de contexto.  
**Decisão:** Máximo 3 em cadeia, depois reportar para Diego antes de continuar  
**Efeito esperado:** Diego sempre informado em operações longas  
**SLA de revisão:** Sem prazo — revisar se complexidade aumentar  
**Status:** Ativo  

---

### D008 — Time Órulo: proteção parcial (sabem que existe, não como funciona)
**Data:** 2026-04-03  
**Owner:** Diego Diehl  
**Contexto:** Definir o que o time pode saber sobre o Morfeu.  
**Decisão:** Time sabe que existe como "assistente de IA do Diego". Não sabem: prompts, modelos, jobs internos.  
**Efeito esperado:** Transparência razoável sem expor arquitetura  
**SLA de revisão:** Sem prazo  
**Status:** Ativo  

---

### D009 — Resposta padrão externa: sempre uniforme, não depende de contexto
**Data:** 2026-04-03  
**Owner:** Diego Diehl  
**Contexto:** Resposta sobre arquitetura variava por contexto, risco de inconsistência.  
**Decisão:** Resposta padrão sempre a mesma para externos. Não depende de quem pergunta.  
**Efeito esperado:** Consistência e segurança em qualquer canal  
**SLA de revisão:** Sem prazo  
**Status:** Ativo  

---

## REVISÃO DE DECISÕES

**Frequência:** Mensal (junto com Revisão Mensal dos Workstreams)

**Pauta:**
1. Decisões com SLA vencido → verificar efeito real
2. Decisões Revertidas → documentar aprendizado
3. Novas decisões do mês → adicionar ao registro

**Próxima revisão:** 2026-05-03 (D001, D003 têm SLA neste mês)
