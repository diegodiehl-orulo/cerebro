# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Identidade do Morfeu

- **Email:** agente.morfeu.dd@gmail.com
- **Cofre:** https://cofre.diegodiehl.com

---

## OpenClaw Dashboard

- **URL pública:** https://openclaw.diegodiehl.com
- **Token:** `Dbn8uL74ZN7pUNEPz3gojh8puPbVPe73`

## Domínio e Infraestrutura

- **Domínio:** diegodiehl.com
- **Registrador:** Cloudflare, Inc. (registrado em 26/02/2026)
- **DNS:** Cloudflare (etta.ns + fattouche.ns)
- **Subdomínios ativos:** openclaw.diegodiehl.com + cofre.diegodiehl.com (via Cloudflare Tunnel)
- **VPS Provider:** ⚠️ a confirmar com Diego (2 vCPU AMD EPYC, 7.8GB RAM)

---

## Vaultwarden (Cofre do Morfeu)

- **URL pública:** https://cofre.diegodiehl.com
- **URL local:** http://127.0.0.1:8222
- **Docker:** `/docker/vaultwarden/docker-compose.yml`
- **Dados:** `/docker/vaultwarden/data/`
- **Signup:** Desabilitado após criação da conta do Morfeu

---

## Google Drive (gog)

- **Binário:** `/usr/local/bin/gog` (v0.12.0, gogcli)
- **Wrapper:** `/usr/local/bin/gog-morfeu` (já inclui account + client + keyring)
- **Account:** diego.diehl@orulo.com.br
- **Client:** drive-client
- **Credentials:** `/root/.config/gogcli/credentials-drive-client.json`
- **Keyring password:** `/root/.config/morfeu/secrets/gog_keyring_password`
- **Scopes:** drive (full), gmail.readonly, gmail.send, calendar, userinfo.email
- **Configurado em:** 2026-03-09
- **Wrapper Larissa:** `/usr/local/bin/gog-larissa` (mesma conta, mesmo client)
- **Política de governança:** `governance/DRIVE_POLICY.md` — **leitura obrigatória antes de qualquer operação**
- **Log de operações:** `logs/drive_operations.log`
- **Uso nos scripts:**
  ```bash
  gog-morfeu drive search "query" --max 10 -p
  gog-morfeu drive mkdir "Nome da Pasta"
  gog-morfeu drive ls [folder-id]
  ```
- **⚠️ PASTA RAIZ OFICIAL — ÚNICA AUTORIZADA:**
  - **ID:** `1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM`
  - **Nome:** `ÓRULO - Sistema Operacional DD`
  - **URL:** https://drive.google.com/drive/folders/1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM
  - **Regra ABSOLUTA:** Toda criação, upload, move e edição **DEVE** ocorrer dentro desta pasta ou de suas subpastas diretas. Nada fora.

- **🔴 CHECKLIST OBRIGATÓRIO antes de qualquer operação de escrita no Drive:**
  1. Verificar o `parent` do destino via `gog-morfeu drive get <id> --json | jq '.file.parents[0]'`
  2. Confirmar que o parent está dentro de `1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM` (raiz ou subpasta)
  3. **Se o parent for diferente → PARAR e corrigir antes de escrever**
  4. Nunca usar como parent um ID sem verificar a qual pasta pertence

- **🗂️ Subpastas oficiais e seus IDs:**
  | Pasta | ID |
  |-------|----|
  | `00_README_GERAL` | (verificar) |
  | `01_GOVERNANCA_GERAL` | `1VQDXQS6otxWsHKRuAZAXks0ps8Q9JJ5d` |
  | `02_WORKSTREAMS` | `1xR4m19rCOYViok7LlVG-IJhKuP-4N3Ru` |
  | `03_PRACAS` | (verificar) |
  | `04_PESSOAS_E_RESPONSAVEIS` | `1ZF1SZjAipyEJkFfv2Qu5IbppLVjPtzUz` |
  | `05_TEMPLATES` | (verificar) |
  | `06_REPORTS` | (verificar) |
  | `07_ARQUIVO` | (verificar) |
  | WS1 | `1vVV2LIw3CHQUex7LKksTFpaCkejYnSnz` |
  | WS2 | `1wmYccT0lNGi7eFl4IBwJuoLDFb9fcqm3` |
  | WS3 | `1eepLrEvY5uMTa3iLtPhcMGWiZVU0xmTY` |
  | WS4 | `1jNUrGrd5bQAvSVM7j_tK2jVNiPlzb02N` |
  | WS5 | `128Yj68QzpHtYvag2LsD4BUVXo0Pr0jdb` |
  | WS6 | `19WCVYDj2cEZtpJ2g8b1vcW6XDGJSj-ZH` |
  | WS7 | `1InY1hmco0luZIhR29dSQzeAG3ZK7Xuza` |

- **📋 Planilha operacional:**
  - **Nome:** `WS_OPERATING_SYSTEM_H1_2026`
  - **ID:** `1pYmAUBEJQXvN1yxYZb1ybRVtr_UbM7ft` *(atualizado 12/03/2026)*
  - **Localização:** `01_GOVERNANCA_GERAL` → dentro da raiz oficial

- **⚠️ REGRA OBRIGATÓRIA — edição da planilha (nunca criar arquivo novo):**
  ```bash
  # 1. Baixar versão atual
  gog-morfeu drive download 1pYmAUBEJQXvN1yxYZb1ybRVtr_UbM7ft > /dev/null
  cp '/root/.config/gogcli/drive-downloads/1pYmAUBEJQXvN1yxYZb1ybRVtr_UbM7ft_WS_OPERATING_SYSTEM_H1_2026' /tmp/WS_OS.xlsx

  # 2. Editar com Python/openpyxl

  # 3. Re-upload substituindo o arquivo existente (preserva ID, link e permissões)
  gog-morfeu drive upload /tmp/WS_OS.xlsx --replace 1pYmAUBEJQXvN1yxYZb1ybRVtr_UbM7ft
  ```
  **NUNCA usar `--parent` para reuploads da planilha. Sempre `--replace <ID>`.**

- **⚠️ REGRA OBRIGATÓRIA — inserção de novas linhas no backlog:**
  NUNCA usar `ws.append()` — joga na última linha da aba, que pode ser a linha 900+.
  Padrão correto:
  ```python
  # 1. Ler todos os dados como lista
  all_rows = [list(r[:12]) for r in ws.iter_rows(values_only=True)]
  data = [r for r in all_rows[1:] if any(v is not None for v in r)]

  # 2. Encontrar posição correta (ex: após último WS2)
  last_ws2_idx = max(i for i, r in enumerate(data) if r[0] == 'WS2')

  # 3. Inserir na posição certa
  data.insert(last_ws2_idx + 1, nova_linha)

  # 4. Reescrever aba do zero (limpa linhas fantasma)
  ws.delete_rows(1, ws.max_row)
  ws.append(header)
  for r in data:
      ws.append(r)
  ```
  Resultado: planilha sempre compacta, sem linhas fantasma, itens na sequência correta.

- **⚠️ Exclusão:** NUNCA sem aprovação explícita de Diego ("OK para excluir [nome]"). Ver `governance/DRIVE_POLICY.md`.

---

## Google Calendar (gcalcli)

- **Conta:** diego.diehl@orulo.com.br (Google Workspace Órulo)
- **Binário:** `/root/.local/bin/gcalcli`
- **Credenciais OAuth:** `~/.config/gcalcli/` (client_secret.json + oauth pickle)
- **Comando básico:** `gcalcli --client-secret ~/.config/gcalcli/client_secret.json agenda`
- **Scope:** `https://www.googleapis.com/auth/calendar` (leitura e escrita)
- **Configurado em:** 2026-02-27

---

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
