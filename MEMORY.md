# MEMORY.md — Índice de Memória do Morfeu

*Atualizado: 2026-02-26*

---

## 📂 Topic Files

| Arquivo | O que contém |
|---------|-------------|
| `memory/projects.md` | Projetos ativos, concluídos e backlog |
| `memory/decisions.md` | Decisões permanentes com contexto |
| `memory/lessons.md` | Lições aprendidas (🔒 estratégicas + ⏳ táticas) |
| `memory/people.md` | Equipe, parceiros, contatos |
| `memory/pending.md` | Aguardando input ou ação |
| `memory/daily/YYYY-MM-DD.md` | Notas diárias (raw capture) |

## 🔄 Ciclo de Memória

```
Sessão (conversa) → memory/daily/YYYY-MM-DD.md (raw)
                          ↓ consolidação periódica
                     Topic files (curado)
                          ↓ índice atualizado
                     MEMORY.md (sumário)
```

---

## Quem sou
Morfeu 🔵 — Estrategista-Chefe e Mentor de Alta Performance do DD.
Arquétipo: Arquiteto da Clareza. Tom: direto, provocador, sem conforto vazio.
Ver `SOUL.md` e `IDENTITY.md` para detalhe completo.

## Quem é DD
Diego G. Diehl. Sócio Diretor Comercial da Órulo (proptech B2B imobiliária).
Base: São Paulo, SP (Alphaville). Timezone: America/Sao_Paulo.
Professor-Guerreiro-Guia. Arquiteto de máquinas de receita.
Marca DD em construção (autoridade: IA + Vendas + Mercado Imobiliário).
Ver `USER.md` para contexto completo (431 linhas).

---

## 📸 Estado Atual

### Projetos Ativos
- **Módulo 4 (Memória)** — ~80% concluído. Bloqueio: embedding provider para busca semântica
- **Órulo** — operação contínua. Próxima viagem: Vitória (ES) em 04/03
- **Marca DD** — planejamento Q1, execução Q2

### Pendências
- Escolher embedding provider (Voyage AI ou Gemini) para ativar memory_search()
- Enviar Biblioteca Estratégica (12+ docs) para importação
- Responder pergunta 14 (como receber crítica do Morfeu)

---

## Configuração Técnica do Servidor
*Setup: 2026-02-26*
- OpenClaw: systemd ativo | Dashboard: https://openclaw.diegodiehl.com
- Telegram: `@Base_DD_bot` + `@larissa_personal_assistant_bot` | só ID `8671853499`
- Segurança: UFW ativo, Fail2ban ativo, SSH key-only
- Cloudflare Tunnel: ativo (gru18, SP)
- Vaultwarden: https://cofre.diegodiehl.com | conta: agente.morfeu.dd@gmail.com
- Tokens: contextTokens=160k | reserveTokensFloor=30k | memoryFlush=ativo

## Lembretes Agendados
- **02/03 às 12h** — Refinamento de tom de voz (analisar vídeo/palestra de Diego)

---

*Última atualização: 2026-02-26*
