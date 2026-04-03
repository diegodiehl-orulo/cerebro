---
name: vendas-report
description: Comparar o report mensal enviado por Diego com a planilha Consolidado de Vendas. Identifica vendas que estão no report mas faltam na planilha (Gustavo precisa cadastrar) e vendas que estão na planilha mas não estão no report (verificar se foram fechadas depois ou se são inconsistências). Dispara quando Diego enviar "comparar report", "validar vendas", "comparar com planilha" ou enviar o texto do Placar Mensal.
---

# VENDAS REPORT — SKILL DE COMPARAÇÃO

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

## Quando usar

Diego envia o texto do **Placar Mensal** e pide "comparar com planilha".

O agente deve:
1. Extrair as vendas do report enviado (texto livre)
2. Comparar com a planilha do mês correspondente
3. Identificar gaps
4. Gerar lista de cobrança para Gustavo

## Estrutura do Report Padrão (para extração)

```
🏆 PLACAR DO MÊS – [MÊS] (ATUALIZADO)
🎯 Meta de Valor: R$ [valor]
📦 Meta de Contratos: [N] fechamentos
💰 R$ [valor vendido] — [%] da meta de valor
📄 [N] de [N] contratos fechados — [%] da meta de contratos
...
📈 Fechamentos de Março (Vendas Normais)
🔹 R$ [valor]
UF – Cidade – Incorporadora – SDR – Closer
```

**Formato de cada venda no report:**
```
UF – Cidade – Incorporadora – SDR – Closer
```
(Às vezes inclui valor ou não)

## Lógica de comparação

### Passo 1 — Extrair vendas do report de Diego

Para cada linha do report que contém `UF – Cidade – Incorporadora – SDR – Closer`:
- UF: extrair estado
- Cidade: extrair cidade
- Incorporadora: extrair nome (matched fuzzy — "Nazca" = "Nazca ES")
- SDR: extrair nome
- Closer: extrair nome
- Valor: se presente, extrair

### Passo 2 — Buscar na planilha

Filtrar planilha por:
- Mês de Assinatura = mês do report
- Ano = 2026

Para cada venda do report, buscar na planilha:
- Match por nome da incorporadora (case-insensitive, fuzzy)
- Verificar UF coincide
- Verificar SDR/Closer coincide (pelo menos 1)
- Verificar mensalidade bate (se presente no report)

### Passo 3 — Classificar

```
✅ MATCH: venda está no report e na planilha (verificado)

⚠️ MATCH COM DIVERGÊNCIA: venda está nos dois mas com dados diferentes
  - Valor diferente
  - SDR diferente
  - Closer diferente

🔴 FALTA NA PLANILHA: venda está no report mas NÃO está na planilha
  → Gustavo precisa cadastrar

🔵 FALTA NO REPORT: venda está na planilha mas NÃO está no report
  → Verificar se foi fechada depois do report ou se é inconsistência
```

### Passo 4 — Gerar output

**Output Telegram (máx 30 linhas):**

```
📋 COMPARAÇÃO — [Mês/2026]
Report: [N] vendas | Planilha: [N] vendas

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ MATCHES: [N]
  [lista curta se houver divergências]

⚠️ DIVERGÊNCIAS: [N]
  • [Incorporadora] — diferença: [o que]
  • [Incorporadora] — diferença: [o que]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 FALTAM NA PLANILHA ([N]) — Gustavo precisa cadastrar
  • [Incorporadora] ([UF]) — [SDR] / [Closer]
  • [...]

🔵 FALTAM NO REPORT ([N]) — Verificar
  • [Incorporadora] ([UF]) — [Closer]
  • [...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👉 PRÓXIMO PASSO: Cobrar Gustavo para cadastrar [N] vendas até [prazo]
🔗 https://bit.ly/orulo-consolidado-vendas
```

## Script de comparação

```bash
python3 skills/vendas-report/scripts/compare_report.py [MES] [ANO]
```

Exemplo:
```bash
python3 skills/vendas-report/scripts/compare_report.py 3 2026
```

## Regras de operação

- SOMENTE LEITURA da planilha
- Não alterar, não escrever
- Sempre comparar mês + ano juntos
- Se o report incluir deals de meses anteriores (ex: janeiro em report de março), incluir todos
- Em caso de dúvida de match, incluir como "⚠️ verificar" — nunca inventar
- Nome da incorporadora com fuzzy match: "Nazca" = "Nazca ES", "Gabbai" = "Gabbai  ", etc.
- Report enviado por Diego é a fonte de verdade para fins de comparação

## Input esperado

Diego envia o texto do Placar Mensal como mensagem no Telegram.

O agente identifica:
- Mês do report (pela primeira linha: "PLACAR DO MÊS – MARÇO")
- Lista de vendas (cada linha no formato UF – Cidade – Incorporadora – SDR – Closer)
- Valor total se presente
- Total de contratos se presente
