---
name: vps-access
description: Acessar e operar a VPS da Órulo via SSH com chave privada. Usar quando: (1) precisar executar comandos remotos na VPS, (2) fazer deploy, restart de serviços, (3) verificar logs, (4) instalar/configurar algo no servidor. Trigger: "acessar VPS", "conectar na VPS", "executar comando no servidor", "restart docker", "verificar logs do servidor", "acesso SSH".
---

# VPS Access Skill

Acessa a VPS da Órulo via SSH usando chave privada. A chave está em `~/.ssh/id_ed25519_morfeu_vps`.

## Configuração SSH

A chave já está configurada. SSH config está em `~/.ssh/config`:

```
Host vps-orulo
    HostName 187.77.58.250
    User root
    IdentityFile ~/.ssh/id_ed25519_morfeu_vps
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
```

## Como usar

### Acesso rápido
```bash
ssh vps-orulo
```

### Executar comando único
```bash
ssh vps-orulo "comando"
```

### Transferir arquivo (local → VPS)
```bash
scp arquivo.txt vps-orulo:/caminho/remoto/
```

### Transferir arquivo (VPS → local)
```bash
scp vps-orulo:/caminho/remoto/arquivo.txt ./
```

### Voltar arquivo (VPS → local)
```bash
scp vps-orulo:/root/.ssh/authorized_keys ./authorized_keys_bkp
```

## Serviços comuns na VPS

| Serviço | Comando restart | Porta |
|---------|----------------|-------|
| OpenClaw | `systemctl restart openclaw` | 18777 |
| Docker geral | `systemctl restart docker` | - |
| Vaultwarden | `docker-compose -f /docker/vaultwarden/docker-compose.yml restart` | 8222 |
| Nginx | `systemctl restart nginx` | 80, 443 |

## Verificar status de serviço
```bash
ssh vps-orulo "systemctl status nome-do-servico"
```

## Ver logs
```bash
ssh vps-orulo "journalctl -u nome-do-servico --since '1 hour ago'"
```

## Informações da VPS (sempre verificar antes de operar)
```bash
ssh vps-orulo "uname -a && df -h && free -m"
```

## ⚠️ Regras de operação

1. **Confirmar antes de destructive actions** — restart de serviço é OK; deletar arquivos ou configurações requer approval explícita
2. **Sempre verificar disco antes de operações grandes** — `df -h`
3. **Backup antes de alterar config** — fazer copy do arquivo antes de editar
4. **Log de todas as operações** — registrar o que foi feito em `/root/.openclaw/logs/vps_operations.log`

## Referências

- Credenciais e detalhes: `references/vps_info.md`
- Playbooks de operação: `references/playbooks.md`
