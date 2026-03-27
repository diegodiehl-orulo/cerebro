# DIAGNÓSTICO TÉCNICO — GOOGLE DRIVE NO OPENCLAW

**Data:** 08/03/2026  
**Objetivo:** Avaliar capacidade do ambiente OpenClaw para automação de criação de estrutura de pastas no Google Drive  

---

## 1. DIAGNÓSTICO DO AMBIENTE

### 1.1. O que já existe

| Recurso | Status | Detalhe |
|---------|--------|---------|
| **Skill gog** | ⚠️ Instalada, mas binário não disponível | Skill existe em `/usr/lib/node_modules/openclaw/skills/gog/SKILL.md` |
| **Google APIs Python** | ✅ Instalado | `google-api-python-client`, `google-auth`, `google-auth-oauthlib` |
| **Gmail OAuth** | ✅ Configurado | Token em `/root/.config/morfeu/gmail_token.pkl` |
| **Google Calendar** | ✅ Configurado | gcalcli com OAuth |
| **rclone** | ✅ Instalado | `/usr/bin/rclone` (potencial alternativa) |
| **Python 3.12** | ✅ Disponível | Para scripts customizados |
| **Node.js 22** | ✅ Disponível | Para wrappers NPM |

### 1.2. O que falta

| Item | Status | Ação necessária |
|------|--------|----------------|
| **Binário gog** | ❌ Não instalado | Precisa Go para compilar (não disponível no ambiente) |
| **Drive API OAuth** | ❌ Não configurado | Criar credentials + autorizar |
| **Credentials Google Cloud** | ❌ Não existe | Criar OAuth client ID |
| **Permissão Drive** | ❌ Não concedida | Escopo `drive` precisa ser autorizado |

### 1.3. O que está bloqueado

- **gog:** Binário não existe porque Go compiler não está instalado no ambiente
- **Drive API:** Sem credentials OAuth, não é possível autenticar

---

## 2. VALIDAÇÃO DE CAPACIDADE REAL

### O que este OpenClaw consegue fazer:

| Capacidade | Status | Detalhe |
|------------|--------|---------|
| Autenticar conta Google | ⚠️ Parcial | Gmail/Cal já autenticados, Drive não |
| Listar pastas Drive | ❌ Não | Sem API configurada |
| Criar pasta | ❌ Não | Sem API configurada |
| Criar subpasta | ❌ Não | Sem API configurada |

### Integração/credencial faltante:

**Google Drive API OAuth** — precisa ser criado e autorizado.

---

## 3. ESTRATÉGIA RECOMENDADA

### Caminho A) gog (Google Workspace CLI)

| Aspecto | Detalhe |
|---------|---------|
| **Pré-requisitos** | Instalar Go compiler + compilar gog + criar OAuth credentials |
| **Vantagens** | CLI nativa, sintaxe simples, já tenho skill documentada |
| **Riscos** | Go não está disponível no ambiente; manutenção de binário customizado |
| **Robustez** | Alta para produção (oficial) |
| **Recomendação** | ❌ Não viável agora (Go não instala fácil) |

### Caminho B) Script Python com Google Drive API

| Aspecto | Detalhe |
|---------|---------|
| **Pré-requisitos** | Criar OAuth credentials no Google Cloud, autorizar 1x, salvar token |
| **Vantagens** | Bibliotecas Python já instaladas, controle total, idempotente |
| **Riscos** | Token expira (refresh token resolve) |
| **Robustez** | Alta para produção |
| **Recomendação** | ✅ **ESCOLHIDO** — viável agora |

---

## 4. SEGURANÇA E GOVERNANÇA

### Regras operacionais (para o script):

1. **Pasta raiz fixa:** Toda criação acontece dentro de uma pasta `ORULO_Automation_Root` (ID fixo)
2. **Nunca criar fora da raiz:** Qualquer.tree precisa validar que o parent está dentro da raiz
3. **Evitar duplicidade:** Antes de criar, verificar se pasta já existe (por nome + parent)
4. **Nunca renomear/apagar:** Apenas criar, por padrão. Ações destrutivas apenas com instrução explícita.
5. **Retornar IDs:** Sempre retornar Google Drive File ID de cada pasta criada
6. **Log de execução:** Registrar data, usuário, estrutura criada, IDs gerados

---

## 5. PROPOSTA TÉCNICA — create_drive_structure

### Parâmetros de entrada

```python
{
  "root_folder_id": "1ABC123...",  # ID da pasta raiz (fixo, configurado)
  "structure": [
    {"name": "2026", "type": "folder"},
    {"name": "H1_2026", "parent": "2026", "type": "folder"},
    {"name": "03_Marco", "parent": "H1_2026", "type": "folder"},
    {"name": "WS1_Comunicação", "parent": "03_Marco", "type": "folder"},
    ...
  ]
}
```

### Validações

1. Verificar se `root_folder_id` é válido e acessível
2. Validar que todas as pastas pais existem
3. Sanitizar nomes (remover caracteres inválidos)
4. Verificar duplicidade antes de criar

### Formato da árvore

 Estrutura em JSON declarativa, onde cada item especifica:
- `name`: nome da pasta
- `parent`: (opcional) ID ou nome do pai. Se omitido, cria na raiz.
- `type`: sempre "folder"

### Comportamento idempotente

- Se pasta já existe (mesmo nome + mesmo pai), retorna ID existente e **não** cria novamente
- Log registra "já exists" vs "criado"

### Saída esperada

```json
{
  "success": true,
  "created": [
    {"name": "2026", "id": "1ABC...", "status": "created"},
    {"name": "H1_2026", "id": "1DEF...", "status": "created"}
  ],
  "skipped": [
    {"name": "WS1_Comunicação", "id": "1GHI...", "status": "already_exists"}
  ],
  "execution_log": "2026-03-08 10:00:00 | user: diego.diehl@orulo.com.br | 2 created, 1 skipped"
}
```

### Tratamento de erro

- Erro de autenticação → raise com instrução de re-autenticar
- Pasta pai não existe → raise com nome da pasta faltante
- Erro de API → retry 3x com backoff, depois falha explícita
- Token expirado → detectar e pedir re-autenticação

---

## 6. ENTREGÁVEL FINAL

### Checklist do que você precisa configurar manualmente

| # | Item | Ação | Tempo |
|---|------|------|-------|
| 1 | **Criar OAuth Client ID** | Ir em Google Cloud Console → APIs → Credentials → Create OAuth Client ID | 5 min |
| 2 | **Baixar client_secret.json** | Salvar em `/root/.config/morfeu/drive_client_secret.json` | 1 min |
| 3 | **Autorizar acesso Drive** | Rodar comando de OAuth flow (vou criar script) | 2 min |
| 4 | **Testar criação de pasta** | Criar pasta de teste na raiz | 1 min |

### Plano de implementação recomendado

1. **Agora:** Você cria o OAuth Client ID no Google Cloud Console
2. **Depois:** Me passa o `client_secret.json`
3. **Eu crio:** Script `create_drive_structure.py` com toda lógica de segurança
4. **Testamos:** Criar uma estrutura de pastas de exemplo
5. **Produção:** Integrar aos crons de workstreams

### Comandos/arquivos que serão criados

| Arquivo | Função |
|---------|--------|
| `/root/.openclaw/workspace/scripts/drive_manager.py` | Script principal de automação |
| `/root/.config/morfeu/drive_token.pkl` | Token OAuth do Drive (após autorização) |
| `/root/.config/morfeu/drive_client_secret.json` | Credentials (você cria) |

---

## PRÓXIMO PASSO

Me passe o `client_secret.json` do OAuth Client ID que você criar no Google Cloud Console, ou me oriente para criar um projeto Google Cloud se preferir que eu faça tudo.

**Precisa de ajuda para criar o OAuth Client ID?** Posso gerar o passo a passo.
