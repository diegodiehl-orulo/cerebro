---
name: vendas-audit
description: Auditoria de preenchimento da planilha Consolidado de Vendas Órulo. Use para: (1) gerar ranking de preenchimento por SDR e Closer; (2) gerar mensagens personalizadas de cobrança para cada pessoa; (3) comparar dados da planilha com report de Diego; (4) identificar gaps de preenchimento estratégico. Sempre focado em 2026. Executar quando Diego pedir "auditar preenchimento", "ranking de preenchimento", "cobrar equipe" ou "mensagem para [nome]".
---

# VENDAS AUDIT — SKILL

## Fonte de dados

| Campo | Valor |
|-------|-------|
| Spreadsheet ID | `1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ` |
| Aba | `Vendas` |
| Link | `https://bit.ly/orulo-consolidado-vendas` |

## Acesso

```bash
gog-morfeu sheets get "1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ" "Vendas!A1:X201" --plain
```

## Estrutura de colunas

| Coluna | Dono | Campos |
|--------|------|--------|
| N | SDR | `Nome do SDR que agendou` |
| O | Closer | `Pessoa responsável` |
| Q | SDR | `O que levou o contato a aceitar a reunião com a Órulo?` |
| R | SDR | `Qual foi o contexto atual da incorporadora?` |
| S | Closer | `Principal gargalo identificado` |
| T | Closer | `O que mais chamou atenção do cliente?` |
| U | Closer | `Entrega de valor que mais se conectou` |
| V | Closer | `O que levou a decidir contratar?` |
| W | Closer | `Por que não tinha contratado antes?` |
| X | Closer | `Outras frentes/soluções abordadas?` |

## Output 1 — Ranking (Tabela 2 colunas)

```
📊 AUDITORIA — Preenchimento Estratégico 2026
🔗 https://bit.ly/orulo-consolidado-vendas
[N] vendas | Semana [DD/MM]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SDR — Colunas Q + R
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 [Pessoa]    [N] vendas pendentes  [N] campos vazios
🟡 [Pessoa]    [N] vendas pendentes  [N] campos vazios
🟢 [Pessoa]    [N] vendas pendentes  [N] campos vazios

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLOSER — Colunas S+T+U+V+W+X
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 [Pessoa]    [N] vendas pendentes  [N] campos vazios
🟡 [Pessoa]    [N] vendas pendentes  [N] campos vazios
🟢 [Pessoa]    [N] vendas pendentes  [N] campos vazios
```

**Regras de ordenação:**
- SDR: por total de campos vazios (Q+R) — maior primeiro
- Closer: por total de campos vazios (S+T+U+V+W+X) — maior primeiro
- Cor: 🔴 >5 campos = vermelho | 🟡 1-5 = amarelo | 🟢 0 = verde
- Excluir pessoas com 0 pendências da tabela principal

## Output 2 — Mensagens Personalizadas

### Template de mensagem:

```
[Pessoa], tudo bem?

Temos [N] vendas suas de 2026 sem os campos [Q,R / S,T,U,V,W,X] preenchidos na planilha:

🔗 https://bit.ly/orulo-consolidado-vendas

🔴 [N] vendas pendentes — [N] campos vazios

Vendas:
• [Nome] ([UF]) — Mês [N]
• [...]

Campos a preencher:
• [letras]: [pergunta curta]
• [letras]: [pergunta curta]

Consegue preencher até sexta 17h?

abs
Diego
```

### Detalhamento por pessoa (sempre incluir lista exata):

**SDR (Q e R):**
- Q: "O que levou o contato a aceitar a reunião?"
- R: "Qual foi o contexto atual da incorporadora?"

**CLOSER (S a X):**
- S: "Principal gargalo identificado"
- T: "O que mais chamou atenção?"
- U: "Entrega de valor que mais conectou"
- V: "O que levou a decidir contratar?"
- W: "Por que não tinha contratado antes?"
- X: "Outras frentes/soluções abordadas?"

## Script de análise

Executar via:

```bash
python3 skills/vendas-audit/scripts/audit_vendas.py
```

O script gera:
- Ranking SDR + Closer
- Lista de vendas pendentes por pessoa
- Quantidade de campos vazios por coluna

## Regras de operação

- SOMENTE LEITURA da planilha
- Gerar mensagens com tom direto, cordial, sem agressividade
- Sempre incluir o link da planilha
- Sempre listar as vendas pendentes com nome + UF + mês
- Sempre pedir prazo: "sexta 17h"
- Não enviar mensagens automaticamente — entregar para Diego/Lara validarem

## Formato de saída Telegram (máx 25 linhas/bloco)

```
📊 AUDITORIA — Preenchimento 2026

[tabela ranking]

━━━━━━━━━━━━━━━━━━━━━━━━
MENSAGENS PERSONALIZADAS
━━━━━━━━━━━━━━━━━━━━━━━━

[Pessoa 1 — texto completo]

[Pessoa 2 — texto completo]
```
