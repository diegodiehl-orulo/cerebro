# Playbooks — srv1429674

## Restart de serviço

```bash
# OpenClaw (docker)
ssh vps-orulo "docker restart openclaw-gjiw-openclaw-1"

# Vaultwarden
ssh vps-orulo "docker restart vaultwarden"

# Orulo Portal
ssh vps-orulo "docker restart orulo-portal-new"
```

## Ver logs

```bash
ssh vps-orulo "docker logs --tail 100 openclaw-gjiw-openclaw-1"
ssh vps-orulo "docker logs --tail 50 vaultwarden"
ssh vps-orulo "docker logs --tail 50 orulo-portal-new"
```

## Ver uso

```bash
ssh vps-orulo "df -h && echo '---' && free -m && echo '---' && docker stats --no-stream"
```

## Entrar no container

```bash
ssh vps-orulo "docker exec -it openclaw-gjiw-openclaw-1 /bin/sh"
```

## Rebuild de container

```bash
# Exemplo: rebuild vaultwarden
ssh vps-orulo "cd /docker/vaultwarden && docker-compose pull && docker-compose up -d"
```

## Health check completo

```bash
ssh vps-orulo "docker ps --format 'table {{.Names}}\t{{.Status}}' && uptime && df -h | grep -v tmpfs && free -m"
```
