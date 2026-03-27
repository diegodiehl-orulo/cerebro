# DECISIONS - Frente Pracas v1

Este documento registra as decisões arquiteturais e de escopo tomadas durante o design da v1.

## 1. Decisões Arquiteturais Finais

- **Arquitetura em Camadas:** Foi adotado o modelo `Coleta -> Validação -> Análise -> Comunicação`.
  - **Motivo:** Modularidade, testabilidade e baixo acoplamento.
- **Desacoplamento da Fonte de Dados:** A v1 não se integra a sistemas externos. Ela consome um arquivo JSON padronizado.
  - **Motivo:** Simplificar a implementação da v1, focar na lógica do agente e criar um contrato de dados claro antes de lidar com a complexidade de integrações.
- **Workflows Decompostos:** O conceito monolítico de "Sprint de Praça" foi decomposto no workflow focado `wkf_review_sprint_readout`.
  - **Motivo:** Clareza, implementação faseada e simplicidade.

## 2. Simplificações de Escopo

- **Análise Focada em Desvios:** A análise de negócio da v1 se concentra exclusivamente na identificação de desvios percentuais em relação a um período anterior.
  - **Motivo:** Entrega o maior valor com a menor complexidade. Análises mais sofisticadas (correlação, predição) foram adiadas.
- **Sistema de Suporte (Não Autônomo):** A v1 atua como um sistema de suporte à decisão. Ela gera relatórios para revisão humana, mas não executa ações (ex: criar tarefas, enviar alertas).
  - **Motivo:** Reduzir o risco e a complexidade, garantindo primeiro a confiabilidade da camada de análise.

## 3. O que foi Adiado para v2

- **Integração com Fontes de Dados Reais:** A conexão direta com CRMs ou bancos de dados.
- **Cálculo do Score da Praça:** A lógica de negócio para um score consolidado precisa ser amadurecida.
- **Alertas e Ações Proativas:** A capacidade de monitorar dados e disparar ações automaticamente.
- **Interface de Usuário ou API:** A v1 opera via workflows internos; uma camada de interação externa não faz parte do escopo.

## 4. Riscos Assumidos

- **Dependência do Processo de Extração de Dados:** A qualidade da v1 depende diretamente da disciplina de popular corretamente o arquivo `[praca_id]_kpis.json`. O risco de "garbage in, garbage out" foi mitigado pela skill de validação, mas não eliminado.
- **Lógica de Agregação Simplificada:** As regras de agregação de KPIs (ex: "último valor do período") são uma simplificação. Elas podem precisar de refinamento em versões futuras para casos de uso mais complexos.
