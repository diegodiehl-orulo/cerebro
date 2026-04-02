# VPS Info — Órulo

## Acesso SSH

- **Host:** 187.77.58.250
- **Porta:** 22 (padrão)
- **Usuário:** root
- **Chave:** `~/.ssh/id_ed25519_morfeu_vps`
- **Alias SSH:** `vps-orulo`

## Especificações

- **Hostname:** srv1429674
- **OS:** Ubuntu 24.04 (Noble)
- **Kernel:** 6.8.0-106-generic
- **CPU:** 2 vCPU AMD EPYC
- **RAM:** 7.8GB
- **Arquitetura:** x86_64

## Serviços ativos

| Serviço | Tipo | Status |
|---------|------|--------|
| Docker | Container runtime | ✅ |
| OpenClaw | Agent | ✅ |
| Vaultwarden | Password manager | ✅ |

## Volumes e paths importantes

- **Docker compose files:** `/docker/`
- **Vaultwarden data:** `/docker/vaultwarden/data/`
- **OpenClaw:** `systemd` (não docker)

## Credenciais

- **VPS root:** autenticação por chave SSH (sem senha)
- **Vaultwarden:** acesso via cofre.diegodiehl.com (mesma conta Morfeu)
- **Docker registry local:** nenhum (usa imagens públicas)

## Arquivos de configuração

- **SSH authorized_keys:** `/root/.ssh/authorized_keys`
- **Docker daemon:** `/etc/docker/daemon.json`

## rede

- **Firewall:** ufw ativo (ssh, 80, 443 liberados)
- **Cloudflare Tunnel:** rodando (openclaw + cofre expostos)
