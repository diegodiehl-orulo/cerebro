# VPS Info — srv1429674

## Acesso

- **Host:** 187.77.58.250
- **Porta:** 22
- **Usuário:** root
- **Autenticação:** SSH key (nenhuma senha)

## Hardware

- **Hostname:** srv1429674
- **OS:** Ubuntu 24.04 Noble
- **Kernel:** 6.8.0-106-generic
- **CPU:** 2 vCPU AMD EPYC
- **RAM:** 7.8GB

## Containers Docker

| Container | Imagem | Porta | Descrição |
|-----------|--------|-------|-----------|
| openclaw-gjiw-openclaw-1 | ghcr.io/hostinger/hvps-openclaw:latest | - | Agent Morfeu (este) |
| orulo-portal | orulo-portal-new-portal | 8080→80 | Portal diegodiehl.com — Bitrix → Supabase → Portal |
| vaultwarden | vaultwarden/server:latest | 8222→80 | Cofre de senhas |

## Orulo Portal (projeto)

- **Stack:** Bitrix (fonte) → Supabase (consolidação) → portal.diegodiehl.com (front)
- **Stack técnica:** [a definir com Diego]
- **Porta interna:** 8080 (exposto na 80)

## Volumes

- `/docker/` — compose files e dados
- `/var/lib/docker/volumes/` — volumes persistentes

## Redes

- Cloudflare Tunnel expõe: openclaw.diegodiehl.com + cofre.diegodiehl.com
- Firewall: ufw (ssh, 80, 443 liberados)
