# CHANGELOG - Frente Pracas v1

**Versão: 1.0.0 (Consolidação Inicial)**
**Data:** 2026-03-13

Este changelog registra as ações de materialização e correção realizadas durante a consolidação final da v1.

## Arquivos Criados

Um total de **34 arquivos** foram criados nas seguintes pastas:
- `data/pracas` (1)
- `docs/pracas` (6)
- `memory/pracas` (1)
- `schemas/pracas` (6)
- `skills/pracas` (8)
- `templates/pracas` (1)
- `tests/pracas` (9)
- `workflows/pracas` (1)

## Correções e Refinamentos Aplicados

- **[corrigido]** Nomenclatura de todos os artefatos foi padronizada para `ASCII`, `snake_case`, `minúscula`.
- **[simplificado]** `skill_calculate_score_for_praca` foi removida do núcleo v1 para adiar a dependência de uma lógica de negócio pendente.
- **[adicionado]** `skill_build_sprint_results_for_praca` foi introduzida para criar explicitamente o objeto `sprint_results`, melhorando a modularidade.
- **[adicionado]** `skill_persist_artifact` foi introduzida para formalizar o salvamento dos relatórios.
- **[corrigido]** O schema de dados de KPI foi dividido em `schema_kpi_source_file.json` e `schema_kpi_data_raw.json` para maior clareza de contrato.
- **[corrigido]** O objeto `sprint_results` foi atualizado para incluir `sprint_period`, garantindo que o template tenha acesso ao intervalo de datas.
- **[implementado]** A regra de agregação de KPIs (último valor para métricas de estoque, soma para métricas de fluxo) foi implementada em `skill_collect_kpis_from_praca`.
- **[implementado]** A regra de cálculo de desvio percentual, incluindo o tratamento para `previous_value = 0`, foi implementada em `skill_identify_kpi_deviations`.
- **[atualizado]** O arquivo de dados de amostra `CWB_kpis.json` foi expandido para suportar testes de múltiplos períodos.
- **[adicionado]** A documentação completa da v1 foi criada em `docs/pracas/` para garantir a rastreabilidade e manutenibilidade.
- **[adicionado]** A suíte de testes completa foi materializada em `tests/pracas/`, incluindo um teste de integração ponta a ponta.
