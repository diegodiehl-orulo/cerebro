# JOB: KAIROS T2 — Pendências Vencidas
**Schedule:** Seg-Sex 10h10 BRT
**Timeout:** 60s
**Modelo:** minimax/MiniMax-M2.5
**Gate:** remains ≥ 30

---

## O QUE FAZER

Ler pending.md e encontrar itens com prazo vencido há mais de 48h sem atualização.

## EXECUÇÃO

```bash
cat /root/.openclaw/workspace/memory/pending.md
```

Procurar:
- Linhas com datas no passado (vencido)
- Items sem menção de "resolvido" ou "arquivado" desde a data do prazo

## DECISÃO

Se encontrar item vencido >48h:
```
⏰ KAIROS — Pendência vencida
🔴 Item: [descrição]
📅 Venceu: [data] (+[N] dias)
👉 Status? Resolver ou replanejar?
```

Se não encontrar: **NO_REPLY**