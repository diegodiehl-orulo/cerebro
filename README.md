# Cerebro — Segundo Cérebro Diego Diehl

Pasta raiz do workspace do Morfeu (OpenClaw agent).

## Estrutura

```
cerebro/
├── SOUL.md          # Persona e alma do Morfeu
├── USER.md          # Perfil completo do Diego
├── AGENTS.md        # Governança e protocolos
├── HEARTBEAT.md     # Checklist operacional
├── MEMORY.md        # Índice de memória
├── TOOLS.md         # Infraestrutura e credenciais
├── IDENTITY.md      # Identidade do Morfeu
│
├── memory/          # Memória de longo prazo
│   ├── decisions.md
│   ├── lessons.md
│   ├── people.md
│   ├── pending.md
│   ├── projects.md
│   ├── roles.md
│   ├── daily/       # Notas por sessão
│   └── krs/         # Status de OKRs
│
├── biblioteca/      # Biblioteca estratégica (12 docs)
├── templates/        # Templates reutilizáveis
├── scripts/         # Scripts Python/Shell
├── jobs/            # Definições de cron jobs
├── automations/     # Mapas de automação
└── crm/             # Sistema de people intelligence
```

## Regras

- **GitHub (este repo):** arquivos versionados, privados, acesso via SSH
- **Google Drive:** arquivos oficiais compartilhados com o time (WS charters, planilhas)
- **Drive > memória OpenClaw** em caso de conflito

## Sync

Git pull automático via cron (a cada 1h). Não commitar segredos ou credenciais.
