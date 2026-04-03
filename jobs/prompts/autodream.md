# JOB: autoDream — Consolidação de Memória
## Sprint 2 FASE 2 — M3

**Frequência:** Toda segunda-feira 09:00 BRT + quando solicitado manualmente
**Modelo:** minimax/MiniMax-M2.5
**Timeout:** 90s

---

## EXECUÇÃO

### 1. Rodar script de diagnóstico
```bash
python3 /root/.openclaw/workspace/scripts/autodream.py
```

### 2. Rodar script de archive
```bash
python3 /root/.openclaw/workspace/scripts/archive_daily.py --execute
```

### 3. Interpretar resultado

**Se OK (sem alertas):** NO_REPLY

**Se alertas encontrados:**
```
🌙 autoDream — [data]

⚠️ [N] inconsistência(s) detectada(s):
• [alerta 1]
• [alerta 2]

👉 Ação necessária: [o que Diego deve fazer ou aprovar]
```

---

## REGRAS
- Nunca logar se resultado for OK — silêncio é sinal de saúde
- Máximo 3 linhas por alerta
- Se MEMORY.md atingir >28 entradas → alertar antes de atingir o limite
- Se arquivo atingir >90 dias sem atualização → sugerir archive ou update
