---
name: vps-access-agente
description: "Habilita acesso SSH a uma VPS remota para outra IA (Codex, Claude Code, etc.). A IA guest gera sua própria chave SSH,送你 a public key para o operador instalar no servidor. Inclui playbooks de operacao. Trigger: configurar acesso SSH para IA, habilitar IA guest na VPS, IA externa acessar servidor."
---

# VPS Access — Agente Externo

Habilita outra IA (Codex, Claude Code, Pi, etc.) a acessar a VPS da Órulo via SSH.

## Fluxo de Setup (para esta IA)

### Passo 1 — Verificar se já tem chave SSH

```bash
ls ~/.ssh/id_ed25519* 2>/dev/null || echo "SEM_CHAVE"
```

Se já tem chave: pular para Passo 3.

### Passo 2 — Gerar chave própria

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_vps_guest -N "" -C "ia-guest-vps"
```

**Cada IA deve ter sua própria chave. Não compartilhar chaves entre agentes.**

### Passo 3 — Exibir public key

```bash
cat ~/.ssh/id_ed25519_vps_guest.pub
```

**Copiar esta public key e enviar ao operador (Diego) para instalar na VPS.**

---

## Instruções para o Operador (Diego)

Após receber a public key da IA guest, instalar na VPS:

```bash
ssh vps-orulo "echo 'COLAR_AQUI_A_PUBLIC_KEY' >> ~/.ssh/authorized_keys"
```

**Comando alternativo (se ainda não tem alias):**
```bash
ssh root@187.77.58.250 -i ~/.ssh/id_ed25519_vps_guest "echo 'COLAR_AQUI_A_PUBLIC_KEY' >> ~/.ssh/authorized_keys"
```

---

## Configuração SSH local (nesta IA)

Após instalar, adicionar ao `~/.ssh/config`:

```
Host vps-orulo
    HostName 187.77.58.250
    User root
    IdentityFile ~/.ssh/id_ed25519_vps_guest
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
```

Testar:
```bash
ssh vps-orulo "echo OK && uname -a"
```

---

## Playbooks Rápidos

### Ver status dos serviços
```bash
ssh vps-orulo "docker ps && echo '---' && systemctl list-units --type=service --state=running | grep -E 'openclaw|docker|vaultwarden'"
```

### Restart OpenClaw (se necessário)
```bash
ssh vps-orulo "docker restart openclaw-gjiw-openclaw-1"
```

### Ver logs do OpenClaw
```bash
ssh vps-orulo "docker logs --tail 100 openclaw-gjiw-openclaw-1"
```

### Ver logs do Vaultwarden
```bash
ssh vps-orulo "docker logs --tail 50 vaultwarden"
```

### Ver logs do Orulo Portal
```bash
ssh vps-orulo "docker logs --tail 50 orulo-portal-new"
```

### Health check rápido
```bash
ssh vps-orulo "echo '=== DOCKER ===' && docker ps --format 'table {{.Names}}\t{{.Status}}' && echo '=== UPTIME ===' && uptime && echo '=== DISK ===' && df -h | grep -v tmpfs"
```

### Acessar shell do container
```bash
ssh vps-orulo "docker exec -it NOME_DO_CONTAINER /bin/sh"
```

---

## Informação dos Containers

| Container | Imagem | Porta | Status |
|-----------|--------|-------|--------|
| openclaw-gjiw-openclaw-1 | openclaw-gjiw/openclaw | 18777 | Em execução |
| orulo-portal-new | orulo/portal | ? | Em execução |
| vaultwarden | vaultwarden/vaultwarden | 8222→80 | Em execução |

## Credenciais e Endpoints

| Serviço | URL | Observação |
|---------|-----|-----------|
| OpenClaw (host) | https://openclaw.diegodiehl.com | Via Cloudflare Tunnel |
| Vaultwarden | https://cofre.diegodiehl.com | Via Cloudflare Tunnel |
| SSH | 187.77.58.250:22 | Chave única |

---

## Regras de Operação

1. **Confirmar antes de destructive actions** (rm, stop de container crítico)
2. **Sempre verificar disco** (`df -h`) antes de ops grandes
3. **Não modificar `authorized_keys` sem approval** do operador
4. **Logar operações** em `/root/vps_ops_log.txt`

## Reference

- Endpoints e specs: `references/vps_info.md`
- Playbooks avançados: `references/playbooks.md`
