# ARQUITETURA DE MEMÓRIA — 3 CAMADAS
## Base: Claude Code Leak (512k linhas) + Jarvis Fases 2-3

**Versão:** 1.1  
**Data:** 2026-04-03  
**DRI:** Morfeu (execução) + Diego (validação)  
**Status:** ✅ Validado — decisões de Diego aplicadas  

**Decisões Validadas (03/04/2026):**
- Q1: Archive separado (Índice Histórico via semantic search) ✅
- Q2: Limite 30 entradas ativas + archive trimestral ✅
- Q3: Auto-archive daily/ após 60 dias de inatividade ✅  

---

## O PROBLEMA QUE RESOLVEMOS

O Claude Code revelou uma arquitetura de memória que resolve o maior problema de agentes de longa duração: **context entropy** — a tendência do modelo perder o fio quando o histórico cresce.

Solução deles (e nossa agora): **3 camadas estritas com disciplina de acesso**.

---

## AS 3 CAMADAS

### CAMADA 1 — MEMORY.md (Índice Leve)

**O que é:**  
Arquivo único, sempre carregado no context. NÃO contém dados — contém ponteiros (pointers).

**Formato:**  
```
*Última atualização: [data]*

## Índice

| Arquivo | Conteúdo | Última revisão |
|---------|----------|----------------|
| memory/people.md | Mapa de pessoas e papéis | 2026-03-11 |
| memory/pending.md | Pendências em aberto | 2026-04-03 |
| memory/projects.md | Status de projetos ativos | 2026-04-01 |
```

**Regras:**
- Linhas curtas: máximo ~150 caracteres por entrada
- NUNCA colocar dados brutos (textos de reunião, transcrições)
- Atualizar APÓS escrita confirmada (strict write discipline)
- Revisado semanalmente — entradas velhas arquivadas, não deixadas lá

**O que NÃO entra:**
- Transcripts de reuniões
- Dados de CRM
- E-mails completos
- Outputs longos de scripts

---

### CAMADA 2 — Topic Files (Conhecimento por Domínio)

**O que é:**  
Arquivos por domínio, lidos on-demand quando o contexto exige.

**Estrutura atual:**
```
memory/
├── people.md          # Mapa de pessoas + canal + papel
├── pending.md         # Pendências com DRI + prazo + status
├── projects.md        # Projetos ativos + fase + próxima ação
├── decisions.md       # Decisões estratégicas com histórico
├── lessons.md         # Aprendizados (erros + correções)
├── roles.md           # Papéis e responsabilidades do Morfeu
└── daily/
    └── YYYY-MM-DD.md  # Notas brutas da sessão (raw, sem filtro)
```

**Regras:**
- Um arquivo por domínio — não fragmentar demais
- Atualizar via Strict Write Discipline (escrever → confirmar → indexar)
- Lidos via semantic search ou grep — nunca carregar full desnecessariamente
-有效期: arquivos > 90 dias sem acesso = verificar relevância

**Leitura:**
- `memory_search` → busca semântica (Gemini embeddings)
- `memory_get` → snippet específico (lê só o necessário)
- NÃO carregar arquivos full no context sem necessidade

---

### CAMADA 3 — Transcripts e Raw Data (Nunca no Context Principal)

**O que é:**  
Transcripts de sessões, logs brutos, outputs de scripts. Lidos APENAS via grep/semantic search.

**Regra de ouro:**  
> Transcripts are never fully read back into context — they are grep'd for specific identifiers.

**Na prática:**
- Sessão longa? Nunca carrego o transcript completo
- Preciso de algo do transcript? Semantic search ou grep por identificador
- daily/YYYY-MM-DD.md = raw capture, não leitura primária
- Se algo do daily é importante → extrair e mover para topic file relevante

**Formato daily/ para captura:**
```
# YYYY-MM-DD

## Resumo
[3-5 linhas do que importa do dia]

## Decisões
- [decisão 1]
- [decisão 2]

## Pendências novas
- [item] → [dono] → [prazo]

## Notas
[raw stuff — sem filtro, depois filtro]
```

---

## DISCIPLINA DE ESCRITA (STRICT WRITE)

### Ciclo correto:

```
1. IDENTIFICAR necessidade de escrever
   → Nova pendência? Decisão tomada? Projeto atualizado?
   
2. ESCREVER no topic file correto
   → não em memory.md direto
   → não em daily/ se for sesuatu permanente
   
3. CONFIRMAR que arquivo foi criado/atualizado
   → ls ou cat para verificar
   
4. ATUALIZAR índice (MEMORY.md ou topic file pai)
   → APENAS após confirmação de sucesso
   → Sem isso, o índice não reflete realidade
```

### Validação:

Antes de qualquer write/edit:
- ✅ Destino existe? (checar parent)
- ✅ Parent está na pasta correta? (hierarquia do Drive)
- ✅ Espaço disponível?

Após write:
- ✅ Arquivo existe?
- ✅ Tamanho > 0?
- ✅ Conteúdo correto?

Só então atualizar índice.

---

## OVERLAY COM O CLAUDE CODE

| Conceito Claude | Implementação Morfeu |
|-----------------|----------------------|
| MEMORY.md como índice | ✅ MEMORY.md — ponteiros, ~150 chars/linha |
| Topic files on-demand | ✅ memory/*.md — domínio específico |
| Transcript grep'd | ✅ daily/ + semantic search — nunca full load |
| Strict Write Discipline | ⚠️ Implementar — ainda não há validação |
| autoDream | ⚠️ Heartbeat existe —需要在 idle fazer mais |

---

## QUANDO LER CADA CAMADA

| Situação | Camada | Como |
|----------|--------|------|
| Início de sessão | MEMORY.md | Sempre — índice carregado |
| Pergunta sobre pessoa | people.md | memory_search → memory_get |
| Status de projeto | projects.md | memory_search → memory_get |
| Pendência específica | pending.md | memory_search → memory_get |
| Decisão antiga | decisions.md | memory_search |
| Informação de sessão antiga | daily/YYYY-MM-DD.md | Semantic search only |
| Contexto de reunião | tl;dv summaries | Semantic search — não transcript full |

---

## ANTES E DEPOIS

### Antes (problema):
- memory/ growing sem controle
- MEMORY.md com dados velhos de meses
- Transcripts carregados no context = context explosion
- Escrita sem validação = índice diverge da realidade

### Depois (meta):
- MEMORY.md: índice leve, sempre atualizado (max 30 entradas)
- Topic files: domínio único, on-demand
- Transcripts: grep only, nunca full load
- Escrita: confirmar → indexar → pronto
- Archive: automático trimestral

---

## REGRAS DE AUTO-ARCHIVE

### daily/ — archive automático após 60 dias
- Arquivos em memory/daily/ com mais de 60 dias sem acesso → mover para memory/archive/daily_YYYY-QX/
- O sistema detecta via timestamp de acesso
- Semanalmente: job verifica e arquiva

### MEMORY.md — limite de 30 entradas ativas
- Quando atingir 30 entradas: triggers de archive
- Archive: entries sem atualização > 90 dias
- Arquivadas: movidas para ARCHIVE_INDEX.md
- Pesquisáveis via semantic search

### Topic files — validade
- memory/*.md > 90 dias sem atualização: alerta no heartbeat
- Decisão: archivar, atualizar ou manter

---

## PRÓXIMOS PASSOS

- [x] Validar esta arquitetura com Diego ✅ (03/04/2026)
- [x] Implementar Strict Write Discipline (M2) ✅
- [x] Criar script de verificação de consistência entre camadas — pendente (futuro)
- [ ] Testar: Morfeu consegue explicar sua memória sem olhar transcript

---

*Inspirado no Claude Code leak de 31/03/2026 — arquitetura validada por milhares de devs*