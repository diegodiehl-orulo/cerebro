# 🔴 SECURITY NOTICE — Rotação de Credenciais

> **Data do alerta:** 2026-04-17 (sessão de diagnóstico)
> **Escopo:** Credenciais encontradas em texto aberto no histórico do repo `cerebro`.

---

## Credenciais expostas no git history

Durante auditoria profunda foram encontradas credenciais em plaintext commitadas ao repo. Mesmo após remoção do working tree, **elas permanecem acessíveis via `git log`** até rotação.

### Tokens comprometidos

| # | Credencial | Localização histórica | Ação obrigatória |
|---|-----------|----------------------|------------------|
| 1 | **Telegram bot token** `7812376878:AAEQ4d1SoGQ...` | `scripts/sync-cerebro-health-light.sh` | 🔴 **REVOGAR no BotFather imediatamente** → `/revoke` do bot → gerar novo → salvar em Vaultwarden como `morfeu-telegram-token` |
| 2 | **tl;dv API master key** `69f9a821-7286-46e8-...` | 17 locais (scripts, docs, integrations) | 🔴 **REVOGAR em tldv.io/app/settings** → regenerar → salvar em Vaultwarden como `tldv-api-key` |
| 3 | **OpenClaw Dashboard token** `Dbn8uL74ZN7pUNEPz...` | `TOOLS.md:15` | 🔴 **REVOGAR no painel OpenClaw** → regenerar → salvar em Vaultwarden como `openclaw-dashboard-token` |

---

## Playbook de rotação (executar na ordem)

### 1. Revogar e gerar novos tokens

```bash
# Telegram bot token:
#   - Telegram app → @BotFather → /mybots → selecionar bot
#   - "API Token" → "Revoke current token" → copiar novo token

# tl;dv API key:
#   - https://tldv.io/app/settings → API
#   - "Revoke" no token atual → "Generate new" → copiar

# OpenClaw Dashboard:
#   - https://openclaw.diegodiehl.com → Settings → API
#   - Revogar atual → gerar novo
```

### 2. Atualizar Vaultwarden

Salvar cada token como item separado em `cofre.diegodiehl.com`:
- `morfeu-telegram-token`
- `tldv-api-key`
- `openclaw-dashboard-token`

### 3. Atualizar `.env` no VPS

```bash
ssh vps-orulo
sudo -i
cp /root/.openclaw/workspace/.env.example /root/.config/morfeu/morfeu.env
chmod 600 /root/.config/morfeu/morfeu.env
# Editar e preencher com os novos tokens do Vaultwarden
nano /root/.config/morfeu/morfeu.env
```

### 4. Validar cron jobs carregando o env

Confirmar que todos os crons em `jobs/cron_plan.yml` + crontab do VPS carregam `/root/.config/morfeu/morfeu.env` antes de rodar. Exemplo:

```
0 */1 * * * . /root/.config/morfeu/morfeu.env && python3 /root/.openclaw/workspace/integrations/tldv/queue_processor.py >> /root/.openclaw/workspace/logs/tldv_queue_processor.log 2>&1
```

### 5. Limpeza opcional do git history

Apenas se a exposição for considerada crítica (tokens já revogados são inofensivos, mas ficam como histórico de segurança):

```bash
# Opção A (recomendado): aceitar que tokens revogados não são mais sensíveis
# Opção B (nuclear): git-filter-repo para remover completamente
#   pip install git-filter-repo
#   git filter-repo --invert-paths --path scripts/sync-cerebro-health-light.sh
#   git push --force origin master   # ⚠️ reescreve história pública
```

---

## Checklist de confirmação

- [ ] Telegram bot token revogado e substituído
- [ ] tl;dv API key revogada e substituída
- [ ] OpenClaw token revogado e substituído
- [ ] `.env` atualizado no VPS com novos tokens
- [ ] Teste manual: `. /root/.config/morfeu/morfeu.env && python3 scripts/sync-cerebro-health.py`
- [ ] 24h de observação: nenhum cron falha por env ausente
- [ ] Registrar decisão em `memory/decisions.md`

---

## Prevenção — lições aplicadas neste fix

1. `.gitignore` agora inclui `__pycache__/`, `*.pyc`, `.env`
2. Scripts agora exigem env vars via `${TLDV_API_KEY:?...}` (bash) ou `raise RuntimeError` (Python)
3. `.env.example` documenta TODAS as vars necessárias (commitável)
4. Docs não exibem tokens reais — usam placeholder `${TLDV_API_KEY}`

*Documento gerado em 2026-04-17 durante sessão de diagnóstico completo do cérebro. Atualizar checklist à medida que cada item for concluído.*
