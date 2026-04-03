# Vendas Analytics — Configuração

*Criado: 2026-04-01*

## Fonte de dados
- **Planilha:** Consolidado de Vendas Órulo 2025/26
- **Spreadsheet ID:** `1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ`
- **Aba:** `Vendas`
- **Acesso:** gog-morfeu (diego.diehl@orulo.com.br) — SOMENTE LEITURA

## Skill
- **Path:** `skills/vendas-analytics/`
- **Script:** `scripts/parse_vendas.py`
- **Reference:** `references/report_padraoDiego.md`

## Estrutura de colunas (24 detectadas)
| # | Nome |
|---|------|
| A | Nome |
| B | UF |
| C | RM |
| D | SUB-RM |
| E | Tipo de Contrato |
| F | Mensalidade Total |
| G | Valor de Implantação |
| H | Data de Assinatura do Contrato |
| I | Mês de Assinatura do Contrato |
| J | Ano de Assinatura do Contrato |
| K | Fonte do Lead |
| L | Sub-categoria da Fonte |
| M | Detalhes exato sobre a Fonte |
| N | Nome do SDR que agendou |
| O | Pessoa responsável |
| P | Times |
| Q | (SDR) O que levou o contato a aceitar a reunião com a Órulo? |
| R | (SDR) Qual foi o contexto atual da incorporadora? |
| S | (CLOSER) Principal gargalo identificado |
| T | (CLOSER) O que mais chamou atenção do cliente? |
| U | (CLOSER) Entrega de valor que mais se conectou |
| V | (CLOSER) O que levou a decidir contratar? |
| W | (CLOSER) Por que não tinha contratado antes? |
| X | (CLOSER) Outras frentes/soluções abordadas |

## Volume de dados (2026-04-01)
- Total deals: 200
- Deals 2026: 15 (12 jan + 3 fev)
- Deals 2025: 185

## Gaps identificados (2026-04-01)
1. **MARÇO NÃO CADASTRADO** — report Diego mostra 28 contratos em março; planilha só tem até fevereiro
2. **Coluna X (OUTRAS FRENTES)** — 0% preenchimento para deals 2026
3. **Colunas SDR Q+R** — 86.7% (13/15)
4. **Colunas CLOSER S-V+W** — 80% (12/15)
5. **Falta de padronização** — Joal Teitelbaum com mensalidade R$ 0 (Dação?)

## Regras
- Operar SOMENTE em leitura
- Não alterar, não escrever, não append
- Reportar gaps para Diego via Telegram
- Antes de comparar: sempre pedir o report de Diego
