---
name: vendas-analytics
description: Análise de vendas da Órulo via Google Sheets (somente leitura). Use para: (1) comparar dados da planilha Consolidado de Vendas com o report padrão enviado por Diego; (2) auditar preenchimento das colunas estratégicas (SDR/CLOSER); (3) gerar reportes de performance por UF, SDR, Closer e tier de valor; (4) identificar gaps de preenchimento; (5) alertas de deals sem atualização. ATENÇÃO: esta skill opera exclusivamente em modo SOMENTE LEITURA — nunca escrever, editar ou alterar a planilha.
---

# VENDAS ANALYTICS — SKILL (SOMENTE LEITURA)

## Fonte de dados

| Campo | Valor |
|-------|-------|
| Spreadsheet ID | `1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ` |
| Aba principal | `Vendas` |
| Colunas | A–XFD (máx 24 cols detectadas) |
| Linhas | ~200 deals |

## Acesso (gogcli)

```bash
# Ler intervalo inteiro
gog-morfeu sheets get "1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ" "Vendas!A1:AA200" --plain

# Ler só colunas básicas (A-O)
gog-morfeu sheets get "1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ" "Vendas!A1:O200" --plain

# Ler colunas estratégicas (P-AA)
gog-morfeu sheets get "1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ" "Vendas!P1:AA200" --plain
```

## Estrutura das colunas

### Colunas básicas (A-O)
| # | Coluna | Descrição |
|---|--------|-----------|
| A | Nome | Razão social da incorporadora |
| B | UF | Estado |
| C | RM | Região Metropolitana |
| D | SUB-RM | Sub-região |
| E | Tipo de Contrato | DA / Z2A / DA-Embaixador / Dação |
| F | Mensalidade Total | Valor mensal R$ |
| G | Valor de Implantação | Fee de implantação R$ |
| H | Data de Assinatura | DD/MM/AAAA |
| I | Mês de Assinatura | Número (1-12) |
| J | Ano de Assinatura | Número (2025/2026) |
| K | Fonte do Lead | Inbound / Outbound |
| L | Sub-categoria da Fonte | Digisac, Site, Sócio Local, etc. |
| M | Detalhes Fonte | Texto livre |
| N | Nome do SDR | Quem agendou |
| O | Pessoa responsável | Closer / dono do deal |
| P | Times | Dono do deal |

### Colunas estratégicas (Q-AA) — Meta: 100% preenchimento 2026+
| # | Coluna | Dono |
|---|--------|------|
| Q | (SDR) O que levou o contato a aceitar a reunião? | SDR |
| R | (SDR) Qual foi o contexto atual da incorporadora? | SDR |
| S | (CLOSER) Principal gargalo identificado | Closer |
| T | (CLOSER) O que mais chamou atenção do cliente? | Closer |
| U | (CLOSER) Entrega de valor que mais se conectou | Closer |
| V | (CLOSER) O que levou a decidir contratar? | Closer |
| W | (CLOSER) Por que não tinha contratado antes? | Closer |
| X | (CLOSER) Outras frentes/soluções abordadas | Closer |

## Workflows

### Workflow 1 — Comparar Planilha vs Report Diego

Quando Diego enviar o report padrão (placar mensal):

1. Ler a aba Vendas completa (A:O)
2. Filtrar por Mês = mês do report E Ano = 2026
3. Comparar deals do report vs. deals da planilha
4. Identificar:
   - Deals que estão no report mas faltam na planilha
   - Deals na planilha que não estão no report
   - Divergências de valor (mensalidade diferente)
   - Divergências de SDR/Closer
5. Gerar output:
   - ✅ Matches (confirmados)
   - ⚠️ Divergências (valor, SDR, Closer)
   - 🔴 Faltam na planilha (Gustavo precisa cadastrar)
   - 🔴 Faltam no report (deal fechou mas não foi adicionado)

### Workflow 2 — Auditoria de Preenchimento Estratégico

Executar toda segunda-feira:

1. Contar total de deals comAno = 2026
2. Para cada coluna Q–X, contar % preenchido
3. Gerar alerta se < 100% para deals de 2026
4. Lista por Closer/SDR do que falta preencher

**Output Telegram (máx 20 linhas):**
```
📋 Auditoria Preenchimento — [Mês/Ano]
Deals 2026: [N] total

✅ [Coluna]: [N]/[Total] ([%] — [status])
⚠️ [Coluna]: [N]/[Total] ([%] — ATRASADO)
🔴 [Coluna]: [N]/[Total] ([%] — CRÍTICO)

Donos com pendência:
• [SDR/Closer]: [N] colunas incompletas
```

### Workflow 3 — Report de Performance (Diário/Terceiro)

Gerar para Diego via Telegram (horário: 09h ou 14h — configurable):

**Por UF:**
```
📊 Vendas por UF — [mês/ano]
SP: [N] contratos | R$ [valor]
ES: [N] contratos | R$ [valor]
PR: [N] contratos | R$ [valor]
...
Total: [N] contratos | R$ [valor]
```

**Por Closer:**
```
👤 Performance Closers — [mês/ano]
João: [N] deals | R$ [valor]
Zanella: [N] deals | R$ [valor]
Kneip: [N] deals | R$ [valor]
```

**Por tier de valor:**
```
💰 Variação de Ticket
R$ 0–300: [N] deals
R$ 300–600: [N] deals
R$ 600–900: [N] deals
R$ 900+: [N] deals
```

### Workflow 4 — Alerta de Deals Abertos sem Evolução

Semanal (quinta):
1. Identificar deals com data de assinatura vazia E战略 cols todas vazias E ano 2026
2. Ordenar por UF/responsável
3. Alerta Diego sobre risco de deal parado

## Regras de operação (invioláveis)

- **SOMENTE LEITURA** — nunca usar `sheets update`, `append`, `insert`, `clear`
- Sempre confirmar com Diego antes de qualquer ação external
- Reportes para Diego via Telegram (target: 8671853499)
- Não enviar para time sem autorização explícita
- Dados de 2025 = referência histórica; foco em 2026+
- Verificar `recent_minutes` de 30 antes de enviar alerta группale

## Configuração local

Salvar em `memory/vendas_config.md`:
- Spreadsheet ID
- Aba ativa
-Horário de report preferencial (hora)
- UF prioritárias
- DRIs (SDR + Closer)

## Output padrão Telegram (máx 25 linhas por mensagem)

```
🔵 [TÍTULO] — [data]

[conteúdo em bullets]

[pendências ou próximos passos se houver]
```
