# Mapa de Lacunas Estruturais e Pendências

**Data de Atualização:** 26 de Março de 2026
**Responsável:** Agente Executivo de Curadoria (IA)

Este documento rastreia os "gaps" no acervo: documentos ausentes, informações incompletas, processos não documentados e ambiguidades que afetam a execução comercial.

## 1. Lacunas Críticas (Impacto Direto na Execução e Medição)

| Lacuna | Descrição | Impacto | Ação Recomendada |
|---|---|---|---|
| **Falta do KR4** | O arquivo `KR4.md` não existe no diretório `03_KRs`. | Quebra na sequência e possível perda de rastreabilidade de um objetivo chave. | Verificar com o DRI se o KR4 foi descontinuado, absorvido ou se o arquivo foi perdido. Se descontinuado, registrar no `00_KR_INDEX.md`. |
| **MRR Total Não Consolidado (KR7 — MRR Mensalidades)** | Conforme apontado no `KR7.md`, falta a consolidação do MRR total. | Impossibilidade de acompanhar a meta de receita de forma precisa. | Priorizar a extração e consolidação do dado de MRR líquido de mensalidades. |
| **Fonte de Dados do KR5 — Integrações Ativas Não Confirmada** | O `KR5.md` relata que a fonte para medir integrações ativas não está validada. | O KR5 não pode ser acompanhado confiavelmente. | Definir e instrumentar a fonte de dados definitiva para o KR5 nos próximos 7-14 dias. |
| **DRIs Indefinidos para WS3 — Execução Territorial Praças, WS6 — Embaixadoras Drive Free e WS7 — Modelo Econômico Praça** | O `MAPA_DE_RESPONSAVEIS_V1.1.md` aponta falta de definição de DRIs para estes workstreams. | Risco de paralisia na execução territorial e programa de embaixadoras por falta de dono. | Pautar na próxima reunião de diretoria a alocação formal dos DRIs. |

## 2. Lacunas Documentais e de Processo (Impacto na Padronização)

| Lacuna | Descrição | Impacto | Ação Recomendada |
|---|---|---|---|
| **Consolidação do Sócio-Local (P11)** | Existem múltiplos documentos sobre Sócio-Local com sobreposição na pasta `04_Expansao_Territorial/SOCIO_LOCAL`. | Confusão sobre qual é o modelo vigente e dificuldade de onboarding. | Executar o prompt `P11_CONSOLIDACAO_PASTA_SOCIO_LOCAL.md` para unificar a tese. |
| **Processo de Vendas BDR (P10) — vinculado ao WS4 — Estrutura Comercial e CRM** | O processo "as is" dos BDRs não está documentado de forma canônica. | Dificuldade em treinar novos BDRs e diagnosticar gargalos no funil. | Executar o prompt `P10_PROCESSO_BDR_VENDAS.md` com o especialista da área. |
| **Playbook de Evento Territorial (P9) — vinculado ao WS5 — Marketing Event Driven** | Eventos locais estão sendo executados sem um método replicável documentado. | Inconsistência nos resultados de geração de pipeline via eventos. | Executar o prompt `P9_MARKETING_TERRITORIAL_EVENTOS.md` para gerar o playbook. |
| **Revisão do Modelo Econômico por Praça (P8) — vinculado ao WS7 — Modelo Econômico Praça** | O modelo atual precisa ser refinado e formalizado para a expansão 2026. | Decisões de alocação de capital em novas praças baseadas em premissas desatualizadas. | Executar o prompt `P8_PRIORITARIO_MODELO_ECONOMICO_PRACA_WS7.md`. |
| **Charter WS4 — Estrutura Comercial e CRM** | O charter original continha três versões repetitivas. | Ambiguidade no escopo da operação BDR/Vendas. | **Resolvido:** charter consolidado em versão única durante esta curadoria. |

## 3. Lacunas de Governança do Acervo

| Lacuna | Descrição | Impacto | Ação Recomendada |
|---|---|---|---|
| **Registro de Decisões Vazio** | A pasta `07_DECISOES` recém-criada não possui histórico retroativo. | Perda do racional por trás de mudanças de rota anteriores. | Passar a registrar toda decisão executiva em formato de "Decision Record" nesta pasta. |
| **Documento GTM Disperso** | A estratégia de Go-to-Market está fragmentada entre Visão, Expansão e Produtos. | Dificuldade de apresentar a estratégia de forma coesa para o board ou novos líderes. | Criar um documento síntese de GTM consolidando as frentes. |
| **README das Bases Consolidadas** | A pasta `Bases CONSOLIDADAS de Documentos` não possui um `00_README` claro na raiz. | Navegação prejudicada para novos usuários. | Criar `00_README_BASES_CONSOLIDADAS.md` mapeando a arquitetura da base de conhecimento. |

---
**Protocolo de Manutenção:** Este mapa deve ser revisado mensalmente. Quando uma lacuna for resolvida, ela deve ser removida desta lista e a ação correspondente deve ser registrada no `00_CHANGELOG_CURADORIA.md`.
