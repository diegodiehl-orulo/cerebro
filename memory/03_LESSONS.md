# 03_LESSONS.md — Lições Aprendidas

> Formato: [DATA] | Lição | Contexto | Aplicar quando

## Como registrar uma lição
Quando algo dá errado ou um padrão emerge, o Morfeu registra:
```
[YYYY-MM-DD] | LIÇÃO: [o que aprendi]
CONTEXTO: [o que aconteceu]
APLICAR QUANDO: [situação em que isso é relevante]
```

---

## Lições Registradas

[2026-02-26] | LIÇÃO: O campo dmAllowlist não existe no OpenClaw — o correto é allowFrom
CONTEXTO: Tentei configurar allowlist do Telegram com campo errado, gateway rejeitou
APLICAR QUANDO: Qualquer configuração de acesso no Telegram

[2026-02-26] | LIÇÃO: Docker bypassa UFW por padrão — bindar em 127.0.0.1 no compose
CONTEXTO: Painel web estava exposto na internet mesmo com UFW ativo
APLICAR QUANDO: Sempre que criar container Docker com porta exposta

[2026-02-26] | LIÇÃO: openclaw gateway restart dentro da sessão derruba a própria sessão
CONTEXTO: Várias tentativas de restart causaram erros na sessão
APLICAR QUANDO: Usar systemctl --user restart openclaw-gateway.service no lugar

[2026-02-26] | LIÇÃO: openclaw memory index --all não existe — usar --force
CONTEXTO: Tentei rodar conforme PRD do curso; flag errada
APLICAR QUANDO: Sempre que indexar memória

[2026-02-26] | LIÇÃO: agents.defaults.compaction.memoryFlush é objeto, não boolean
CONTEXTO: Tentei setar como true, gateway rejeitou com erro de validação
APLICAR QUANDO: Qualquer config de compactação

[2026-02-26] | LIÇÃO: FTS-only mode não indexa arquivos sem embedding provider
CONTEXTO: openclaw memory index --verbose revelou: "Skipping memory file sync in FTS-only mode"
APLICAR QUANDO: Para ativar busca semântica real, precisamos de Voyage AI ou Gemini (free tier)
