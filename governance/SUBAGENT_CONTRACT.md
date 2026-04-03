# SUBAGENT CONTRACT
## Contrato Formal para sessions_spawn

**Versão:** 1.1  
**Data:** 2026-04-03  
**DRI:** Morfeu  
**Base:** Claude Code Leak (Coordinator/Swarm) + Jarvis Fase 5  
**Status:** ✅ Validado — decisões Q6 + Q7 aplicadas  

---

## O QUE É

Quando o Morfeu delega uma tarefa a um subagente (via `sessions_spawn`), existe um contrato:
- **Input:** o que o subagente recebe
- **Output:** o que o subagente deve retornar
- **Reconciliação:** como o Morfeu confere o resultado antes de seguir

**Por quê?**  
Sem contrato, o subagente pode devolver "feito" sem ter feito, ou fazer a coisa errada, ou fazer certo mas não conseguir provar. O Morfeu precisa de um formato validável.

---

## O MODELO DE CONTRATO

### Estrutura básica de cada spawn:

```python
sessions_spawn(
    task="""
    [TASK DESCRIPTION]
    
    CONTEXT:
    - [contexto necessário para a tarefa]
    - [arquivos para ler]
    - [constraints]
    
    OUTPUT FORMAT:
    Você DEVE retornar:
    1. [resultado concreto — o que foi produzido]
    2. [evidência — como validar que foi feito]
    3. [exceptions — o que deu errado se algo deu]
    
    DO NOT return: "feito", "completo", "ok" sem evidências.
    """,
    runtime="subagent"  # ou "acp" se for coding agent
)
```

---

## INPUT — O QUE O SUBAGENTE RECEBE

### Template de contexto para subagente:

```
## Tarefa: [nome]
## Dono original: Morfeu (para Diego Diehl)

### O que fazer:
[descrição clara da tarefa em 1-3 linhas]

### Contexto disponível:
- Arquivo: [path] — ler este arquivo
- Informação: [resumo do que precisa saber]

### Constraints:
- Formato de output: [descrição]
- Prazo: [se aplicável]
- O que NÃO fazer: [restrições]

### Output esperado:
[descrição de como o subagente deve retornar resultado]
```

---

## OUTPUT — O QUE O SUBAGENTE DEVE RETORNAR

### Formato obrigatório (4 campos):

```markdown
## Resultado

[O que foi produzido — concreto, não "feito"]

## Evidência

[Como validar — arquivo criado, link, screenshot, output de script]

## Exceções

[O que deu errado — se nada, escrever "Nenhuma"]

## Próximo passo

[O que o Morfeu deve fazer depois — se não houver, escrever "Nenhum"]
```

---

## RECONCILIAÇÃO — COMO O MORFEU CONFERE

### Checkpoints de validação:

```
1. RESULTADO EXISTE?
   → Se output não tem "Resultado" → REJEITAR
   → Se resultado é vago ("feito") → REJEITAR

2. EVIDÊNCIA VÁLIDA?
   → Verificar arquivo criado: ls [path]
   → Verificar conteúdo: head -5 [path]
   → Se não existe → REJEITAR

3. EXCEÇÕES DOCUMENTADAS?
   → Se silêncio absoluto → perguntar
   → Se exceções sérias → escalar para Diego

4. PRÓXIMO PASSO CLARO?
   → Se não há próximo passo → definir baseado no resultado
```

### Se rejeitar:
```
→ sessions_send para o subagente: "Output não atende ao contrato. 
   Por favor revise: [具体问题]. Tente novamente."
→ Não seguir adiante até validar
```

---

## EXEMPLO PRÁTICO

### Tarefa: Analisar pendências do CRM

**Input para subagente:**
```
## Tarefa: Analisar pendências CRM Bitrix
## Dono: Morfeu (para Diego Diehl)

### O que fazer:
Analisar deals parado há mais de 7 dias no pipeline "DL → Pago"

### Contexto:
- CRM: Bitrix (acesso via API — credenciais em TOOLS.md)
- Arquivo: memory/pending.md — pendências existentes

### Constraints:
- Formato: lista cards (não tabela) — formato Telegram
- Máximo: 10 deals mais antigos
- Ignorar: deals em etapa "Fechado" ou "Perdido"

### Output esperado:
4 cards: 🔴 +3, 🟡 +4, 🟢 +3 (por status de risco)
Cada card: deal name, dias parado, última ação, próximo passo
```

**Output retornado pelo subagente:**
```
## Resultado
Analisados 47 deals no pipeline. 10 em estado de risco.

🔴 Crítico (3):
1. Construtora Alpha — 23 dias | Última ação: 15/03 | Próximo:reter contato
...

## Evidência
Leitura via API Bitrix — query: stage.id = "QUALIFICATION" AND updated < DATE_SUB(NOW(), INTERVAL 7 DAY)
10 deals identificados, ordenados por dias sem atualização.

## Exceções
- 2 deals não têm campo "última ação" (legacy) — marcado como "sem dado"
- API rate limit atingiu 80% — reduziu query batch

## Próximo passo
Diego precisa validar: 3 deals 🔴 exigem decisão sua sobre reter ou arquivar.
```

**Reconciliação do Morfeu:**
```
✅ Resultado concreto: 10 deals, separados por risco
✅ Evidência: API query documentada, número faz sentido
✅ Exceções: documentadas (legacy, rate limit)
✅ Próximo passo: claro — Diego precisa decidir sobre 3 deals

→ Passar para Diego em formato Telegram
```

---

## TIPOS DE SUBAGENTE E CONTRATO

### Tipo 1 — Subagente de Análise (runtime=subagent)
- Input: dados para analisar
- Output: síntese + recomendações
- Validação: conferir lógica + existência de recomendações

### Tipo 2 — Coding Agent (runtime=acp)
- Input: tarefa de código + arquivos de referência
- Output: código escrito + testes
- Validação: rodar testes + verificar que compila

### Tipo 3 — Research Agent (runtime=subagent)
- Input: query + fontes
- Output: fatos encontrados + fontes
- Validação: fontes reais + sem alucinação

---

## REGRAS DE LIMITE E ESCALADA

### Limite de cascade (spike em sequência):
> Máximo 3 subagentes em cadeia antes de reportar a Diego.

**Por quê:** Cada subagente pode demorar ~2min. 10 em cadeia = 20min sem feedback, risco de timeout e perda de contexto.

**Regra:**
- 1-2 subagentes: seguir normalmente
- 3+ subagentes: pausar + reportar a Diego: "Processando [N] tarefas em paralelo. Continuo quando terminar?"
- Se Diego confirmar: seguir. Se não responder em 5min: assumir OK e seguir.

### Falha de subagente — regra de escalação:
> Se subagente retorna resultado inválido 2x → escalar para Diego.

**Workflow:**
1. Failure 1x: retornar para subagente com instrução mais específica
2. Failure 2x: **ESCALAR** — enviar para Diego:
   ```
   ⚠️ Subagente falhou 2x: [tarefa]
   Detalhe: [o que deu errado]
   Sugestão: [o que fazer — fazer manualmente, pular, resolver de outra forma]
   ```
3. Aguardar decisão de Diego antes de prosseguir
4. **NUNCA** fazer 3a tentativa sem consultar Diego

### Quando desistir do subagente:
- Se subagente retorna "não consegui" com exceção razoável (API down, rate limit)
- Se subagente retorna dados mas claramente incompletos ou errados
- Escalonar com contexto do que foi tentado e por quê

---

## SESSIONS_YIELD — USO CORRETO

Após `sessions_spawn`, o Morfeu DEVE usar `sessions_yield` para receber o resultado.

**Regra:**
```
1. sessions_spawn(task=...) → submete tarefa
2. sessions_yield() → espera resultado
3. Processar resultado → reconciliação
4. Se válido → seguir | Se inválido → rejeitar + pedir retry
```

**Nunca:**
- Fazer spawn e não fazer yield (resultado perdido)
- Fazer yield e não processar (ignorar output)
- Seguir adiante sem reconciliação (aceitar output não validado)

---

## INTEGRADO AO AGENTS.md

Adicionar em AGENTS.md:

```
### Subagentes — Contrato Obrigatório

Todo sessions_spawn DEVE incluir:
- Contexto claro (arquivos + constraints)
- Formato de output definido (4 campos)
- sessions_yield após spawn
- Reconciliação antes de seguir

Output inválido = rejeitar + pedir retry.
Output válido = passar para Diego ou seguir execução.
```

---

## RESUMO: CHECKLIST POR TASK

- [ ] Task description clara (1-3 linhas)
- [ ] Contexto + arquivos necessários
- [ ] Constraints definidos
- [ ] Output format especificado (4 campos)
- [ ] sessions_spawn feito
- [ ] sessions_yield aguardado
- [ ] Reconciliação: resultado + evidência + exceções + próximo passo
- [ ] Se inválido → rejeitar + retry
- [ ] Se válido → seguir

---

*Criado como parte da FASE 1 — M5 (Contract de Subagente)*  
*Baseado em: Claude Code Leak (Coordinator/Swarm) + Jarvis Fase 5*