# 03_LESSONS.md — Lições Aprendidas

> Erros, padrões e aprendizados do dia a dia com o Morfeu.
> 🔒 Estratégicas = permanentes | ⏳ Táticas = expiram em 30 dias

---

## 🔒 Estratégicas

### Docker bypassa UFW — sempre bindar em 127.0.0.1 (2026-02-26)
**Contexto:** Painel web estava exposto na internet mesmo com UFW ativo
**Regra:** Qualquer container Docker com porta exposta → `127.0.0.1:PORTA` no compose, nunca `0.0.0.0`

### allowFrom, não dmAllowlist (2026-02-26)
**Contexto:** Campo errado na config do Telegram — gateway rejeitou silenciosamente
**Regra:** O campo correto para allowlist do Telegram no OpenClaw é `allowFrom`

### Reiniciar gateway via systemctl, não openclaw CLI (2026-02-26)
**Contexto:** `openclaw gateway restart` dentro de sessão ativa derruba a própria sessão
**Regra:** Usar sempre `systemctl --user restart openclaw-gateway.service`

---

## ⏳ Táticas

### `openclaw memory index --all` não existe (2026-02-26) [expira: 2026-03-26]
Usar `--force` no lugar: `openclaw memory index --force`

### `agents.defaults.compaction.memoryFlush` é objeto, não boolean (2026-02-26) [expira: 2026-03-26]
Deve ser passado como JSON com `enabled`, `softThresholdTokens`, `systemPrompt`, `prompt`

### Busca semântica requer embedding provider (2026-02-26) [expira: 2026-03-26]
FTS-only mode não indexa arquivos. Precisa de Voyage AI ou Gemini para ativar `memory_search()` completo

---

*Revisão mensal: deletar táticas vencidas.*
