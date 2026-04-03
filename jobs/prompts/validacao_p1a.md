# JOB: Validação P1-A — Constraint Check Pós-Execução

**Frequência:** Seg-Sex 07h30 e 17h30 BRT
**Modelo:** minimax/MiniMax-M2.5
**Timeout:** 60s

---

## EXECUÇÃO SIMPLIFICADA

### Regra: Apenas verificar se rodou recentemente

1. Se rodou OK nas últimas 24h → **NO_REPLY**

2. Se NÃO rodou E hoje é dia útil (seg-sex) → alerta simples:

```
⚠️ *Constraint Check — [data]*
🔴 [Nome do job] não executou nas últimas 24h
👉 Verificar: job travado ou quota esgotada?
```

3. Revisão Semanal (ab458393): só verifica sextas. Se não rodou na sexta → alerta.

---

## REGRAS
- Simplicidade: 1 alerta = 1 job = 1 linha
- Não tentar ler outputs ou verificar conteúdo — só checar se executou
- Alerta limpo e direto — sem análise extensa
- Output máximo: 2 linhas