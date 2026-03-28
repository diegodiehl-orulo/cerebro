# DRIVE_POLICY.md — Política de Governança do Google Drive
> **Versão:** 1.0
> **Criado:** 2026-03-09
> **Dono:** Diego Diehl
> **Aplicável a:** Morfeu, Larissa, Claudinei — qualquer agente ou script com acesso ao Drive

---

## 1. PRINCÍPIO FUNDAMENTAL

O Google Drive é território de Diego e da Órulo. O agente opera como **hóspede com permissão restrita**, não como dono. Qualquer dúvida sobre escopo de uma ação → **não executa e pergunta**.

---

## 2. OPERAÇÕES PERMITIDAS (sem aprovação prévia)

| Operação | Condição |
|----------|----------|
| **Listar** arquivos e pastas | Apenas nas pastas autorizadas (Seção 4) |
| **Ler** conteúdo de arquivos | Apenas nas pastas autorizadas (Seção 4) |
| **Criar** pastas novas | Apenas dentro das pastas autorizadas (Seção 4) |
| **Criar** arquivos novos (upload) | Apenas dentro das pastas autorizadas (Seção 4) |
| **Renomear** arquivo ou pasta criado pelo agente | Apenas se o agente foi o criador original |
| **Buscar** (`drive search`) | Em toda a conta — apenas leitura |

---

## 3. OPERAÇÕES PROIBIDAS — CLASSIFICAÇÃO

### 🔴 PROIBIÇÃO ABSOLUTA (nunca, sob nenhuma circunstância)

| Operação | Motivo |
|----------|--------|
| **Excluir / mover para lixeira** qualquer arquivo ou pasta de **terceiros** | Irreversível. Pode destruir trabalho de outra pessoa. Proibido sem exceção. |
| **Excluir / mover para lixeira** qualquer arquivo cujo criador não seja o agente | Idem |
| **Modificar conteúdo** de arquivos que o agente não criou | Risco de sobrescrever trabalho alheio |
| **Revogar permissões** de compartilhamento | Impacto imprevisível na operação |
| **Mover** arquivos que o agente não criou para outra pasta | Altera estrutura que não pertence ao agente |
| **Operar fora das pastas autorizadas** (Seção 4) — exceto `drive search` (read-only) | Sem autorização explícita |

### 🟡 REQUER APROVAÇÃO EXPLÍCITA DE DIEGO ("OK para executar")

| Operação | O que o agente deve fazer antes |
|----------|--------------------------------|
| **Excluir** arquivo ou pasta **criado pelo agente** | Mostrar nome + ID + impacto. Aguardar "OK para excluir [nome]". |
| **Renomear** arquivo ou pasta **não criado pelo agente** | Mostrar o antes/depois. Aguardar OK explícito. |
| **Criar pasta na raiz** (fora de pastas autorizadas) | Justificar + mostrar estrutura proposta. Aguardar OK. |
| **Compartilhar** arquivo com terceiros | Mostrar quem receberá acesso + nível de permissão. Aguardar OK. |
| **Qualquer ação em massa** (bulk create, bulk move, bulk rename) | Sempre mostrar prévia completa + rollback possível. Aguardar OK. |

---

## 4. PASTAS AUTORIZADAS

**Regra de escopo:** O agente só pode criar, renomear ou fazer upload **dentro da pasta raiz autorizada e suas subpastas**. Operações fora desse escopo = bloqueadas.

---

### 🟢 PASTA RAIZ AUTORIZADA

| Campo | Valor |
|-------|-------|
| **Nome** | Morfeu — Central de Comando (ou equivalente) |
| **ID Drive** | `1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM` |
| **Link** | https://drive.google.com/drive/folders/1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM |
| **Operações** | Listar ✅ \| Ler ✅ \| Criar pasta ✅ \| Upload ✅ \| Renomear (próprios) ✅ \| Excluir ❌ (requer OK) |

### Estrutura atual da pasta raiz

```
📁 Raiz (1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM)
├── 📁 01_GOVERNANCA_GERAL  (1hx7pJ62kMmk-YlMX3VzQ2nZe8YPATWRl)
├── 📁 02_WORKSTREAMS        (18X6LnY0epWKnblk7pr1nyvvdmEO4CfbL)
│   ├── 📁 WS1_Comunicacao_Corretores
│   ├── 📁 WS2_Jornada_DL_Pago
│   ├── 📁 WS3_Execucao_Territorial_Pracas
│   ├── 📁 WS4_Estrutura_Comercial_CRM
│   ├── 📁 WS5_Marketing_Event_Driven
│   ├── 📁 WS6_Embaixadoras_Drive_Free
│   └── 📁 WS7_Modelo_Economico_Praca
├── 📁 03_PRACAS             (1wJz8DFd_J5zRUY7IX9dfY6VRe0mxjh93)
├── 📁 04_PESSOAS_E_RESPONSAVEIS (1lfHEWH6p0LXVGb07_UmAqQz3YhiWo0Z6)
├── 📁 05_TEMPLATES          (1y-X29d-B0czGm_b_B1P7Zw_XsJ-BpD14)
├── 📁 06_REPORTS            (1SfTaSNrhvzYfHNNvLWOJt45upPfx7meM)
└── 📁 07_ARQUIVO            (1jCH8YPa-G2ORLLzRNA_YjE5W9lItVYqs)
```

### Fora do escopo (requer aprovação explícita de Diego para expandir)

- Qualquer pasta fora da raiz `1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM`
- Drives compartilhados de terceiros
- Pastas pessoais de outros usuários da Órulo

---

## 5. RASTREABILIDADE OBRIGATÓRIA

Toda operação de escrita (criar, renomear, mover) deve ser registrada:

```
[DRIVE LOG] 2026-03-09 13:55 | Agente: morfeu | Operação: mkdir
  Nome: "Sprint-WS3-Curitiba-Sprint01"
  Pasta pai: [ID]
  ID criado: [ID]
  Aprovação: Diego (sessão Telegram 2026-03-09)
```

Log salvo em: `/root/.openclaw/workspace/logs/drive_operations.log`

---

## 6. FLUXO DE APROVAÇÃO PARA EXCLUSÃO

```
Agente identifica necessidade de excluir
          ↓
Gera prévia:
  • Nome exato do arquivo/pasta
  • ID Drive
  • Criador original
  • Data de criação
  • Conteúdo (se possível resumir)
  • Motivo da exclusão
          ↓
Envia para Diego via Telegram
          ↓
Diego responde: "OK para excluir [nome]"
          ↓
Agente executa + registra no log
          ↓
Agente confirma: "Excluído: [nome] | ID: [id] | [timestamp]"
```

**Resposta parcial não vale.** "OK" genérico sem mencionar o nome do arquivo = **não executa**.

---

## 7. ARQUIVOS DE TERCEIROS — REGRA ZERO

Qualquer arquivo cujo campo `owners` na API do Drive **não seja** `diego.diehl@orulo.com.br`:

- **Leitura:** permitida (se estiver em pasta autorizada)
- **Escrita:** **PROIBIDA**
- **Exclusão:** **PROIBIDA** — sem exceção, sem aprovação, sem discussão

Se o agente receber instrução de excluir arquivo de terceiro:
→ Recusar, explicar o motivo, oferecer alternativa (ex: notificar o dono).

---

## 8. CONFIGURAÇÃO TÉCNICA

| Item | Valor |
|------|-------|
| Binário | `/usr/local/bin/gog` (v0.12.0) |
| Wrapper Morfeu | `/usr/local/bin/gog-morfeu` |
| Wrapper Larissa | `/usr/local/bin/gog-larissa` |
| Account | `diego.diehl@orulo.com.br` |
| Client | `drive-client` |
| Keyring password | `/root/.config/morfeu/secrets/gog_keyring_password` (chmod 600) |
| Log de operações | `/root/.openclaw/workspace/logs/drive_operations.log` |
| Credenciais OAuth | `/root/.config/gogcli/credentials-drive-client.json` |
| Escopos autorizados | `drive` (full), `gmail.readonly`, `gmail.send`, `calendar` |

---

## 9. REVISÃO DA POLÍTICA

- **Revisão inicial:** quando Diego definir as pastas autorizadas (Seção 4)
- **Revisão periódica:** trimestral ou quando houver incidente
- **Responsável:** Diego Diehl
- **Dono técnico:** Morfeu

---

*"Acesso não é propriedade. O agente opera no território de Diego como executor, não como dono."*
