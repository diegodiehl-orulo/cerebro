# README - Frente Pracas v1

## 1. Objetivo da Frente

A frente "Pracas" é a camada de execução territorial do sistema operacional comercial. Seu objetivo principal é traduzir a estratégia definida nos workstreams em resultados de receita em geografias específicas, reduzindo a variância de performance entre territórios e garantindo consistência na execução local.

## 2. Escopo da v1

A v1 foca em estabelecer um processo de **análise de performance e geração de relatórios** para os sprints das praças. Ela automatiza a coleta de dados, a identificação de desvios e a criação de um "One-pager" padronizado para as reuniões de revisão de sprint (Readout).

**O que a v1 faz:**
- Coleta KPIs de performance de um arquivo de dados JSON.
- Valida e limpa esses dados.
- Compara a performance do período atual com o anterior.
- Identifica desvios significativos (>10%).
- Gera um relatório padronizado em Markdown.
- Salva o relatório no workspace.

**O que a v1 NÃO faz:**
- Não se integra diretamente com CRMs ou bancos de dados.
- Não calcula um "Score" de praça.
- Não gera alertas automáticos.
- Não executa ações proativas.

## 3. Estrutura de Pastas

A frente utiliza a seguinte estrutura no workspace:
- `/data/pracas/`: Arquivos JSON com dados brutos de KPI.
- `/memory/pracas/`: Arquivos JSON com metadados estáticos das praças.
- `/reports/pracas/`: Destino dos relatórios em Markdown gerados.
- `/schemas/pracas/`: Contratos de dados (JSON Schema) que definem a estrutura dos objetos.
- `/skills/pracas/`: Implementação em Python das capacidades atômicas.
- `/templates/pracas/`: Templates (Jinja2/Markdown) para geração de artefatos.
- `/tests/pracas/`: Testes (pytest) para garantir a qualidade do código.
- `/workflows/pracas/`: Manifestos YAML que orquestram a execução das skills.
- `/docs/pracas/`: Documentação de consolidação.

## 4. Skills da v1

- `skill_get_context_for_praca`: Carrega metadados de uma praça.
- `skill_collect_kpis_from_praca`: Coleta e agrega KPIs de um arquivo fonte.
- `skill_validate_kpi_data`: Limpa e valida os dados de KPI.
- `skill_identify_kpi_deviations`: Compara períodos e encontra desvios.
- `skill_build_sprint_results_for_praca`: Agrega todos os dados de um sprint.
- `skill_generate_onepager_for_sprint`: Gera o relatório Markdown a partir de um template.
- `skill_persist_artifact`: Salva um artefato no workspace.

## 5. Workflow da v1

- `wkf_review_sprint_readout`: Orquestra todas as skills acima para executar o processo completo de revisão de sprint, desde a coleta de dados até a persistência do relatório final.

## 6. Como Executar

Consulte o `RUNBOOK_PRACAS_V1.md` para instruções detalhadas sobre pré-requisitos e execução.

## 7. Como Testar

Consulte o `RUNBOOK_PRACAS_V1.md` para instruções sobre como executar a suíte de testes.
