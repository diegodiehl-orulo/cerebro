# Convenção de Nomenclatura do Acervo — Órulo

**Data:** 26 de Março de 2026

Este documento define as regras de nomenclatura para todos os arquivos e pastas do acervo da Diretoria Comercial Órulo, com o objetivo de garantir consistência, navegabilidade e otimização para leitura por IA.

---

## 1. Regras Gerais de Nomenclatura

| Regra | Exemplo Correto | Exemplo Incorreto |
|---|---|---|
| Usar snake_case (underscores, sem espaços) | `WS4_ONEPAGE_CHARTER.md` | `WS4 - One Page Charter.md` |
| Prefixo numérico para ordenação (pastas) | `01_GOVERNANCA_GERAL/` | `Governança Geral/` |
| Prefixo de workstream quando aplicável | `WS3_ONEPAGE_CHARTER.md` | `Charter_Execucao_Territorial.md` |
| Prefixo de KR quando aplicável | `KR1.md` (aceito por brevidade) | `Key_Result_1.md` |
| Versão explícita quando houver evolução | `ARQUITETURA_OFICIAL_V2.md` | `ARQUITETURA_OFICIAL_nova.md` |
| Sem palavras vagas: "final", "novo", "cópia" | `MODELO_SOCIO_LOCAL_V4.md` | `MODELO_SOCIO_LOCAL_final_final.md` |
| Sem caracteres especiais: `()[]—–` | `NUNI_Indicadores.md` | `[N.U.N.I] Indicadores.md` |
| Data no nome apenas para reports/snapshots | `REPORT_EXECUTIVO_2026_03.md` | `report março.md` |

## 2. Regra Obrigatória: Workstreams Sempre com Sigla + Nome

**Nunca usar apenas a sigla do workstream isoladamente.** Em qualquer documento, relatório, referência cruzada, tabela ou comunicação, sempre usar a sigla acompanhada do nome descritivo completo. Essa regra vale tanto para nomes de arquivo quanto para menções no corpo de documentos.

| Sigla | Nome Oficial Completo |
|---|---|
| WS1 | WS1 — Comunicação com Corretores |
| WS2 | WS2 — Jornada CX DL → Pago |
| WS3 | WS3 — Execução Territorial Praças |
| WS4 | WS4 — Estrutura Comercial e CRM |
| WS5 | WS5 — Marketing Event Driven |
| WS6 | WS6 — Embaixadoras Drive Free |
| WS7 | WS7 — Modelo Econômico Praça |

**Exemplos de aplicação:**

| Contexto | Correto | Incorreto |
|---|---|---|
| Corpo de documento | "...conforme definido no WS3 — Execução Territorial Praças..." | "...conforme definido no WS3..." |
| Tabela de dependências | "Depende de WS2 — Jornada CX DL → Pago" | "Depende de WS2" |
| Referência cruzada | "Ver charter do WS6 — Embaixadoras Drive Free" | "Ver charter do WS6" |
| Report executivo | "WS4 — Estrutura Comercial e CRM: em andamento" | "WS4: em andamento" |

A primeira menção em cada documento deve sempre usar o nome completo. Menções subsequentes no mesmo parágrafo podem usar apenas a sigla, desde que o contexto seja inequívoco.

## 3. Convenção de Versionamento

O versionamento segue o padrão `_V{N}` no final do nome, antes da extensão. A versão mais alta é sempre a canônica. Versões anteriores devem ser movidas para `07_ARQUIVO` ou `99_Arquivo`.

| Situação | Ação |
|---|---|
| Documento evolui de V1 para V2 | Renomear para `_V2.md`. Mover V1 para arquivo. |
| Documento é reescrito completamente | Manter o mesmo nome, incrementar versão. |
| Documento é absorvido por outro | Mover para arquivo com nota no Changelog. |

## 4. Convenção de Status no Nome

Documentos em desenvolvimento podem usar sufixo `_DRAFT` ou `_WIP` para sinalizar que não são canônicos. Ao serem finalizados, o sufixo deve ser removido.

## 5. Formato de Arquivo

| Tipo de Documento | Formato Recomendado | Justificativa |
|---|---|---|
| Charters, bases, notas, prompts, READMEs | `.md` (Markdown) | Otimizado para leitura por IA, versionamento e edição rápida. |
| Reports para diretoria, apresentações | `.docx` ou `.pdf` | Formato adequado para comunicação humana formal. |
| Planilhas operacionais | `.xlsx` | Formato adequado para dados tabulares e cálculos. |
| Backups e versões históricas | Qualquer formato original | Preservar formato original no arquivo. |

## 6. Avaliação de Nomes Atuais

A análise dos 90 arquivos do acervo revelou que a grande maioria já segue padrões adequados. Os únicos problemas identificados são menores:

| Arquivo | Problema | Decisão |
|---|---|---|
| `Dinamica_Reflexao_Final_Ano.md` | Contém "Final" (ambíguo) | Já arquivado em `99_ARQUIVO_GERAL`. Sem ação necessária. |
| `KR1.md` a `KR7.md` | Nomes curtos | **Manter como estão.** O prefixo `KR` + número é uma convenção clara e consistente dentro da pasta `03_KRs`. Renomear adicionaria verbosidade sem ganho real. |

**Conclusão:** O acervo já possui nomenclatura de alta qualidade. A principal melhoria é a aplicação consistente da regra de sigla + nome para workstreams em todo o corpo documental.
