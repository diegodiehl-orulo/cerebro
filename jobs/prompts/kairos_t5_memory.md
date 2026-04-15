# JOB: KAIROS T5 — Memory Check
**Schedule:** Seg-Sex 10h20 BRT
**Timeout:** 60s
**Modelo:** minimax/MiniMax-M2.5
**Gate:** remains ≥ 30

---

## O QUE FAZER

Verificar se MEMORY.md está próximo do limite (30 entradas ativas).

## EXECUÇÃO

```bash
grep -c "^|" /root/.openclaw/workspace/MEMORY.md 2>/dev/null || grep -c "^- \[" /root/.openclaw/workspace/MEMORY.md 2>/dev/null
```

## DECISÃO

Se entradas ativas > 28:
```
⚠️ KAIROS — Memória próxima do limite
📊 Entradas ativas: [N]/30
👉 Revisar e arquivar entries antigas antes de atingir o teto.
```

Se não: **NO_REPLY**