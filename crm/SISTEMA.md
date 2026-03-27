# CRM Estratégico — Sistema de Inteligência de Pessoas
> **Morfeu v0 | Criado: 2026-03-05**
> **Propósito:** Registro vivo de pessoas com quem Diego se envolve — time, parceiros, clientes, networking. Não é um pipeline de deals. É uma base de inteligência relacional que cresce com cada interação.

---

## 🧠 Filosofia do Sistema

**Pessoas são ativos.** Cada contato tem contexto, conexões, timing e potencial. A maioria dos sistemas armazena quem a pessoa é. Este sistema armazena *o que fazer com essa pessoa e quando.*

**Princípios:**
1. **Contexto > Dados:** Mais útil saber "ela está em momento de expansão" do que só o cargo.
2. **Ação > Registro:** Cada entrada deve ter uma próxima ação ou sinal de que não há nenhuma necessária.
3. **Enriquecimento contínuo:** Toda nova informação absorvida deve ser avaliada como candidata a campo permanente.
4. **Separação de camadas:** Time interno (demandas/performance) ≠ Parceiros (negócios/timing) ≠ Networking (relacionamento/oportunidade).

---

## 📂 Estrutura de Arquivos

```
crm/
├── SISTEMA.md              # Este arquivo — meta e protocolos
├── INDEX.md                # Tabela mestre de todos os contatos
│
├── templates/
│   ├── PESSOA_TEMPLATE.md      # Template padrão (parceiros, clientes, networking)
│   └── MEMBRO_TIME_TEMPLATE.md # Template específico para time interno
│
└── pessoas/
    ├── time/               # Membros do time direto de Diego
    ├── parceiros/          # Parceiros estratégicos e comerciais
    ├── clientes/           # Clientes ativos e prospects quentes
    └── networking/         # Contatos de networking e autoridade
```

---

## 🔄 Protocolo de Melhoria Contínua (CAMPO VIVO)

**Toda vez que uma nova memória for absorvida sobre uma pessoa, o Morfeu deve:**

### Passo 1 — Atualizar o arquivo da pessoa
Adicionar o dado na seção `📓 Histórico de Interações` com data e fonte.

### Passo 2 — Reflexão de campo (obrigatória)
Perguntar internamente:
> *"Este dado é recorrente, crítico ou diferenciador o suficiente para virar um campo permanente no perfil desta pessoa?"*

**Critérios para propor novo campo:**
- Aparece em 2+ interações (padrão)
- Impacta a forma de se comunicar com a pessoa
- Relevante para timing de contato ou oportunidade
- Útil para personalizar cobranças, rascunhos ou abordagens

**Se sim:** propor ao Diego antes de adicionar.
> Exemplo: *"Notei que o Werner sempre responde à noite. Quero adicionar o campo `Melhor horário de contato` no perfil dele — faz sentido?"*

### Passo 3 — Verificar networking_queue
Se a última interação foi há mais tempo que a `Frequência ideal de contato`, adicionar à `networking_queue` do `INDEX.md`.

---

## 📡 Integração Futura (WhatsApp)

Quando a leitura de WhatsApp estiver ativa, o sistema deve:
1. Identificar a pessoa pelo número
2. Extrair o contexto da última conversa
3. Atualizar `Última interação` automaticamente
4. Propor enriquecimento de campos com base no conteúdo

**Campos preparados para WhatsApp:** `whatsapp`, `última_mensagem_whatsapp`, `sentimento_ultima_conversa`

---

## 🏷️ Tipos de Relação

| Tipo | Descrição | Template |
|------|-----------|----------|
| `time` | Membro direto do time de Diego | `MEMBRO_TIME_TEMPLATE.md` |
| `sócio-local` | Operador regional da Órulo | `PESSOA_TEMPLATE.md` |
| `parceiro` | Parceiro estratégico externo | `PESSOA_TEMPLATE.md` |
| `cliente` | Cliente ativo ou prospect quente | `PESSOA_TEMPLATE.md` |
| `networking` | Contato de mercado, autoridade, influenciador | `PESSOA_TEMPLATE.md` |
| `pessoal` | Família, amigos próximos | `PESSOA_TEMPLATE.md` (campos reduzidos) |

---

## ⚡ Comandos Rápidos (para Diego)

| Comando | O que o Morfeu faz |
|---------|-------------------|
| `"Atualiza [Nome]"` | Abre o perfil e pergunta o que foi absorvido |
| `"Quem precisa de atenção?"` | Lista pessoas na networking_queue com atraso |
| `"Situação do time"` | Lista demandas abertas + status de cada membro |
| `"Próximos toques de networking"` | Lista contatos com frequência ideal vencida |
| `"Novo contato: [Nome]"` | Cria perfil a partir do template |
| `"O que sei sobre [Nome]?"` | Consolida tudo que está no perfil |
