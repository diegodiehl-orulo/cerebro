# SELF-HEALING RUNBOOKS
## Morfeu — F10 Enhanced (Sprint 3 FASE 2)

**Versão:** 1.0  
**Data:** 2026-04-03  
**DRI:** Morfeu  
**Base:** Jarvis Fase 10 + operação real do Morfeu  
**Status:** ✅ Validado — 5 runbooks ativos  

---

## O PROBLEMA

Até o Sprint 2, o Morfeu detectava incidentes mas não tinha procedimento formal de remediação.
Resultado: incidentes acumulavam, exigindo intervenção manual de Diego.

Agora: cada tipo de incidente tem um runbook — quem faz o quê, em que ordem, como confirmar resolução.

---

## RUNBOOK 1 — JOB TRAVADO

**Sintoma:** Job não roda há >24h em dia útil, sem disable manual.

**Diagnóstico:**
```bash
# Verificar status do job via cron tool
# cron action=list → checar lastRunAt + consecutiveErrors
```

**Remediação:**
1. Verificar se o job está enabled (`cron list`)
2. Se enabled mas não rodou: verificar payload (model existe? prompt file existe?)
3. Se payload OK: fazer `cron run` manual para forçar execução
4. Se falhar manualmente: desabilitar + criar pending item + alertar Diego

**Confirmação:** Job executa sem erro → `consecutiveErrors` = 0

**Escalada:** Se após `cron run` manual ainda falhar → escalar para Diego com log do erro.

---

## RUNBOOK 2 — MEMÓRIA INCONSISTENTE

**Sintoma:** autoDream detecta stale entries ou orphan files (>2 no mesmo ciclo).

**Diagnóstico:**
```bash
python3 /root/.openclaw/workspace/scripts/autodream.py
```

**Remediação:**
1. Stale entries (índice aponta para arquivo inexistente):
   - Verificar se o arquivo foi renomeado ou movido
   - Se movido: corrigir entrada no MEMORY.md
   - Se deletado: remover entrada do MEMORY.md
2. Orphan files (topic file sem entrada no índice):
   - Avaliar relevância do arquivo (data de criação, conteúdo)
   - Se relevante: adicionar entrada no MEMORY.md
   - Se obsoleto: mover para `memory/archive/memory_files_YYYY-QX/`
3. Após correções: rodar autoDream de novo para confirmar 0 inconsistências

**Confirmação:** `python3 autodream.py` retorna "Nenhuma inconsistência detectada."

**Escalada:** Se autoDream detectar >5 inconsistências → escalar para Diego (sinal de problema sistêmico).

---

## RUNBOOK 3 — CRON DUPLICADO

**Sintoma:** Dois jobs com nome similar rodando na mesma frequência.

**Diagnóstico:**
```
cron list → ordenar por nome → detectar duplicatas por nome/schedule
```

**Remediação:**
1. Identificar qual é o job oficial (verificar cron_plan.yml ou jobs/)
2. Listar ambos os jobs com `cron list` e comparar payloads
3. Desabilitar o duplicado (nunca deletar sem confirmar qual é o oficial)
4. Registrar em memory/pending.md: "Cron duplicado desabilitado: [nome] (id: X) — era duplicata de (id: Y)"
5. Alertar Diego com resumo

**Confirmação:** `cron list` mostra apenas 1 job por função.

**Escalada:** Se houver dúvida de qual é o oficial → perguntar Diego antes de desabilitar.

---

## RUNBOOK 4 — CONTEXT OVERFLOW

**Sintoma:** Sessão muito longa, context >80% do limite (120k+ tokens), respostas começam a perder coerência.

**Diagnóstico:**
- Checar `/status` ou `session_status` para ver uso de contexto

**Remediação:**
1. **Imediato:** Parar de adicionar contexto. Não ler arquivos grandes.
2. Salvar estado em `memory/daily/YYYY-MM-DD.md`:
   - O que estava sendo feito
   - Próximo passo concreto
   - Arquivos modificados na sessão
3. Informar Diego: "Contexto próximo do limite. Preciso de uma nova sessão para continuar."
4. Diego inicia nova sessão → Morfeu lê `memory/daily/` para retomar

**Confirmação:** Nova sessão iniciada com contexto <20%.

**Escalada:** Nunca tentar "comprimir" sozinho — sempre salvar estado e pedir nova sessão.

---

## RUNBOOK 5 — CRONTAB DESABILITADO INESPERADAMENTE

**Sintoma:** Job que estava ativo aparece como disabled sem intervenção de Diego.

**Diagnóstico:**
```
cron list → verificar enabled=false + updatedAt recente
```

**Remediação:**
1. Verificar log de runs do job (`cron runs <jobId>`) para entender último estado
2. Verificar se foi desabilitado por consecutiveErrors alto
3. Se foi por erros: seguir Runbook 1 primeiro (corrigir a causa)
4. Se foi desabilitado sem causa aparente: documentar + alertar Diego antes de reativar
5. Nunca reativar sem entender por que foi desabilitado

**Confirmação:** Job está enabled=true e roda sem erro no próximo ciclo.

**Escalada:** Se o padrão se repetir (mesmo job desabilitado 2x sem causa clara) → escalar para Diego como possível bug de plataforma.

---

## MATRIZ DE INCIDENTES

| Incidente | Runbook | Tempo estimado | Autonomia Morfeu |
|-----------|---------|---------------|-----------------|
| Job travado | RB1 | 5 min | Alta — tenta remediar, escalada se falhar |
| Memória inconsistente | RB2 | 10 min | Alta — corrige orphans/stale direto |
| Cron duplicado | RB3 | 3 min | Alta — desabilita duplicata, registra |
| Context overflow | RB4 | 2 min | Total — salva estado e pede nova sessão |
| Crontab desabilitado | RB5 | 5 min | Baixa — só reativa após entender causa |

---

## REGISTRO DE INCIDENTES

Quando um runbook for executado, registrar em `memory/daily/YYYY-MM-DD.md`:
```
## Incidente [RBX] — [HH:MM]
- Sintoma: [descrição]
- Remediação: [o que foi feito]
- Confirmação: [como confirmou resolução]
- Escalou para Diego: sim/não
```

Incidentes críticos (escalados) também vão para `memory/pending.md`.
