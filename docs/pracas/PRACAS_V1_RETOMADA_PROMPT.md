Sua tarefa é atuar como arquiteto e implementador da frente "Pracas", continuando o trabalho a partir da v1 já consolidada.

**Contexto:**
A v1 da frente "Pracas" foi totalmente desenhada, documentada e materializada no workspace. Ela consiste em um sistema de análise de performance e geração de relatórios para os sprints das praças. Todos os artefatos (código, testes, schemas, workflow, documentação) estão salvos na estrutura de pastas `/pracas/`. O checkpoint final e o manifesto de arquivos estão em `docs/pracas/CHECKPOINT_PRACAS_V1_FINAL.md` e `docs/pracas/PRACAS_V1_FILE_MANIFEST.json`.

**O que já existe:**
- Um workflow (`wkf_review_sprint_readout`) que automatiza a geração de relatórios de sprint.
- 7 skills em Python que executam as tarefas de coleta, validação, análise e comunicação.
- Uma suíte de testes completa em Pytest.
- Todos os contratos de dados (JSON Schema) e templates necessários.
- Um runbook detalhado (`docs/pracas/RUNBOOK_PRACAS_V1.md`) explicando como executar e testar a v1.

**O que ficou fora da v1 (pendências para v2):**
- Integração com fontes de dados reais (atualmente consome um arquivo JSON).
- Cálculo de um "Score" de praça.
- Geração de alertas automáticos.

**Sua Próxima Missão:**
Revise o estado atual da v1 consultando o checkpoint e o runbook. Em seguida, proponha e implemente a próxima iteração (v1.1 ou v2), focando em uma das pendências listadas ou em outra melhoria de alto valor.
