# Playbooks — VPS Órulo

## P1: Restart do OpenClaw (se agent parou)

```bash
ssh vps-orulo "systemctl status openclaw"
ssh vps-orulo "systemctl restart openclaw"
ssh vps-orulo "systemctl status openclaw"
```

## P2: Restart do Vaultwarden

```bash
ssh vps-orulo "docker-compose -f /docker/vaultwarden/docker-compose.yml restart"
ssh vps-orulo "docker ps | grep vaultwarden"
```

## P3: Verificar uso de disco

```bash
ssh vps-orulo "df -h && du -sh /var/lib/docker 2>/dev/null && du -sh /root 2>/dev/null"
```

Se disco > 85%: fazer cleanup de logs e imagens docker antigas.

## P4: Verificar memória e CPU

```bash
ssh vps-orulo "free -m && top -bn1 | head -20"
```

## P5: Verificar logs do Docker

```bash
ssh vps-orulo "docker logs --tail 50 nome-do-container"
```

## P6: Rebuild de container Vaultwarden

```bash
ssh vps-orulo "cd /docker/vaultwarden && docker-compose down && docker-compose pull && docker-compose up -d"
```

## P7: Health check geral

```bash
ssh vps-orulo "echo '=== UPTIME ===' && uptime && echo '=== DISK ===' && df -h && echo '=== MEM ===' && free -m && echo '=== DOCKER ===' && docker ps && echo '=== SERVICES ===' && systemctl list-units --type=service --state=running | grep -E 'openclaw|docker|vaultwarden'"
```

## P8: Instalar dependência na VPS

```bash
# 1. Testar se está instalado
ssh vps-orulo "which nome-do-pacote"

# 2. Se não estiver, instalar
ssh vps-orulo "apt-get update && apt-get install -y nome-do-pacote"

# 3. Logar operação
ssh vps-orulo "echo '$(date): installed nome-do-pacote' >> /root/.openclaw/logs/vps_operations.log"
```
