# STRICT WRITE DISCIPLINE
## Regra de Ouro: Escrever → Confirmar → Indexar

**Versão:** 1.1  
**Data:** 2026-04-03  
**DRI:** Morfeu  
**Base:** Claude Code Leak — "Strict Write Discipline" + Jarvis Fases 1-2  
**Status:** ✅ Validado — decisões Q4 + Q5 aplicadas  

---

## A REGRA

> O índice só é atualizado APÓS escrita confirmada com sucesso.  
> NUNCA atualizar ponteiro se a escrita falhou.

**Por quê?**  
Se o índice aponta para um arquivo que não existe, ou uma linha que não foi escrita, o Morfeu perde a capacidade de confiar na própria memória. O índice se torna uma mentira, e mentira em memória é alucinação.

---

## FLUXO CORRETO (6 PASSOS)

### PASSO 1 — Identificar o destino correto
```
→ Qual arquivo recebe esta informação?
→ memory/pending.md? memory/projects.md? daily/YYYY-MM-DD.md?
→ O arquivo existe ou é novo?
```

### PASSO 2 — Verificar parent/hierarquia
```
→ Para arquivos do Drive: verificar parent ID antes de escrever
→ Para arquivos locais: verificar path existe
→ Se parent não é o esperado → PARAR e corrigir
```

### PASSO 3 — Escrever
```
→ usar write/edit com conteúdo correto
→ formatação: seguir o padrão do arquivo existente
```

### PASSO 4 — Confirmar escrita
```
→ exec: ls -la [arquivo] ou cat [arquivo]
→ Checar: arquivo existe? Tamanho > 0? Conteúdo bate?
```

### PASSO 5 — Atualizar índice (se aplicável)
```
→ MEMORY.md: atualizar linha do topic file modificado
→ Topic file: adicionar entrada correta
→ daily/: não precisa indexar em MEMORY.md (é raw)
```

### PASSO 6 — Log (se aplicável)
```
→ memory/daily/YYYY-MM-DD.md: registrar que escreveu
→ Formato: "[acao] [arquivo] — [resumo do que mudou]"
```

---

## VALIDAÇÕES OBRIGATÓRIAS

### Antes de escrever (2 checks):
| Check | Como | Se falhar |
|-------|------|-----------|
| Path existe | `ls -la [dir]` | Criar dir primeiro |
| Parent correto (Drive) | `gog-morfeu drive get [id] --json \| jq '.file.parents[0]'` | PARAR + avisar |

### Após escrever (3 checks):
| Check | Como | Se falhar |
|-------|------|-----------|
| Arquivo existe | `ls [path]` | Reescrever |
| Tamanho > 0 | `wc -c [path]` | Reescrever |
| Conteúdo correto | `head -5 [path]` | Corrigir |

---

## O QUE FAZER SE A ESCRITA FALHAR

### Falha 1x:
- Reescrever + tentar novamente
- Documentar em memory/daily/YYYY-MM-DD.md: "[RETRY] [arquivo] — tentativa 2"

### Falha 2x:
- **DESISTIR** — não tentar 3a vez
- Registrar em memory/pending.md:
  ```
  - [P0] Escrita falhou: [arquivo] — DRI: Morfeu — requer intervenção
  ```
- Alertar Diego (Telegram): "Tentativa de escrita falhou 2x: [arquivo]. Pendência criada."
- **NUNCA** inventar conteúdo ou seguir sem o arquivo

### Razão:
Se o Morfeu tenta 3x e falha, ou-write sem confirmar, o índice fica errado. É melhor parar e escalar do que criar mentira na memória.

---

## EXCEÇÕES (Quando a Regra Pode Ser Quebrada)

### Definição de "emergência":
> Situação crítica com prazo <15min onde Diego precisa de resultado agora.

**Não é emergência:**
- Pedido urgente normal (>15min de prazo)
- Agenda cheia
- Preferência pessoal

**É emergência:**
- Reunião em 10min e falta dado
- Decisão de бизнес que precisa de input do Morfeu
- Situação de crisis com stakeholders esperando

### Workflow de exceção:
1. Fazer o essencial (escrever o mínimo viável)
2. NÃO confirmar com ls/cat (pula Validação)
3. Registrar exceção: `memory/daily/YYYY-MM-DD.md: "[EXCEPTION] [ação] — [motivo]" `
4. Na próxima oportunidade disponível: verificar se escreveu corretamente

---

## O QUE NÃO CONTAR COMO "ESCRITA"

As seguintes ações NÃO atualizam índice:
- Rascunho em memória (sem save)
- Mensagem no Telegram (não é arquivo)
- Output de script na tela (não é persistent storage)
- Pensamento em context (não persiste entre sessões)

---

## EXEMPLO PRÁTICO

**Situação:** Diego criou nova pendência na sessão. Preciso registrar em pending.md.

**Ciclo correto:**
```
1. Identificar: pending.md — nova entrada no final
2. Hierarquia local: /root/.openclaw/workspace/memory/pending.md → OK
3. Escrever: edit com newString = nova linha
4. Confirmar: cat memory/pending.md | grep "nova pendência" → ✅
5. Indexar: Não precisa — pending.md é topic file, não precisa atualizar MEMORY.md para mudança interna
6. Log: memory/daily/2026-04-03.md → "+1 pendência em pending.md"
```

**Ciclo ERRADO:**
```
1. Identificar: pending.md
2. (pula verificação)
3. Editar
4. NÃO CONFIRMA
5. Atualizar índice → ÍNDICE MENTIU
```

---

## INTEGRADO AO AGENTS.md

Esta disciplina é **OBRIGATÓRIA** para qualquer write/edit executado pelo Morfeu.

Adicionar em AGENTS.md (seção de proibições):
```
❌ Nunca atualizar índice (MEMORY.md, topic files) antes de confirmar escrita
❌ Nunca contar output de script como "persistido" sem verificar arquivo
```

Adicionar em AGENTS.md (seção de checklist):
```
[x] Verificar path/parent antes de escrever
[x] Confirmar que arquivo foi salvo com conteúdo correto
[x] Atualizar índice APÓS confirmação
[x] Log em memory/daily/
```

---

## SCRIPTS AUXILIARES (A Criar)

### `memory/check_consistency.py`
Checa se MEMORY.md está sincronizado com topic files:
- Entrada no índice → arquivo existe?
- Arquivo existe → está no índice?
- Tema velhos (>90d) → alertar para archivar

### `memory/check_write_success.sh`
Validacao rápida:
```bash
#!/bin/bash
FILE=$1
if [ -f "$FILE" ] && [ -s "$FILE" ]; then
  echo "OK"
else
  echo "FAIL"
  exit 1
fi
```

---

## RESUMO VISUAL

```
[DIEGO PEDE PARA REGISTRAR]
         ↓
[IDENTIFICAR DESTINO]
         ↓
[VERIFICAR PATH/PARENT]
         ↓
[ESCREVER]
         ↓
[CONFIRMAR — arquivo existe + conteúdo OK]
    ↓ sim                          ↓ não
[ATUALIZAR ÍNDICE]           [REESCREVER + CONFIRMAR]
         ↓                            ↓
    [LOG em daily/]              [VOLTAR PARA CONFIRMAR]
         ↓
    [PRONTO]
```

---

## RELAÇÃO COM CLAUDE CODE

O Claude Code implementa Strict Write Discipline com uma frase:
> "Strict Write Discipline — the agent must update its index only after a successful file write."

Nós implementamos com validação explícita em 6 passos e exception handling.

---

*Criado como parte da FASE 1 — M2 (Strict Write Discipline)*  
*Baseado em: Claude Code Leak (31/03/2026) + Jarvis Fase 2*