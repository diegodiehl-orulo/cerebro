# 02_DECISIONS.md — Decisões Permanentes de Diego

> Formato: [DATA] | Decisão | Contexto | Impacto

## Como registrar uma decisão
Quando Diego tomar uma decisão importante, o Morfeu registra aqui:
```
[YYYY-MM-DD] | DECISÃO: [o que foi decidido]
CONTEXTO: [por que foi tomada]
IMPACTO: [o que muda a partir disso]
INVIOLÁVEL: [sim/não — se sim, nunca questionar]
```

---

## Decisões Registradas

[2026-02-26] | DECISÃO: Usar Vaultwarden self-hosted para cofre do Morfeu
CONTEXTO: Mais privacidade, cofre exclusivo para credenciais do agente
IMPACTO: Credenciais centralizadas em cofre.diegodiehl.com
INVIOLÁVEL: não

[2026-02-26] | DECISÃO: Nome do agente = Morfeu
CONTEXTO: Referência ao Matrix — quem mostra a realidade, não poupa a verdade
IMPACTO: Identidade permanente do agente
INVIOLÁVEL: sim

[2026-02-26] | DECISÃO: Email do agente = agente.morfeu.dd@gmail.com
CONTEXTO: Tratar o agente como entidade separada, com infraestrutura própria
IMPACTO: Credenciais e serviços do agente separados dos de Diego
INVIOLÁVEL: não

[2026-02-26] | DECISÃO: contextTokens = 160.000 | reserveTokensFloor = 30.000
CONTEXTO: Módulo 4 do curso — configuração de memória recomendada pelo PRD
IMPACTO: Garante que raciocínio nunca é cortado no meio; compactação controlada
INVIOLÁVEL: não

[2026-02-26] | DECISÃO: memoryFlush ativado com PRE_COMPACT_CHECKLIST
CONTEXTO: Antes de cada compactação, o Morfeu extrai decisões, lições, pendências e projetos
IMPACTO: Nunca perder contexto relevante em compactações automáticas
INVIOLÁVEL: sim

[2026-02-26] | DECISÃO: Feedback loops em feedback/approved.json e feedback/rejected.json
CONTEXTO: Módulo 4 — capturar o que Diego aprova/rejeita para não repetir erros
IMPACTO: Evolução real do agente ao longo do tempo
INVIOLÁVEL: não
