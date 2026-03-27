# Plano de Ação, Decisões e Rituais — Pós-Curadoria

**Data:** 26 de Março de 2026
**Responsável:** Agente Executivo de Curadoria (IA)
**Contexto:** Resultado da operação de curadoria sobre o acervo da Diretoria Comercial Órulo.

---

## 1. Decisões Executivas Registradas

As decisões a seguir foram tomadas durante a curadoria com base na análise documental. Devem ser registradas na pasta `07_DECISOES` do Sistema Operacional DD.

| ID | Decisão | Racional | Data |
|---|---|---|---|
| D-001 | **Absorver o SUPER CÉREBRO no Sistema Operacional DD e nas Bases Consolidadas.** | O SUPER CÉREBRO duplicava conteúdo estratégico já presente nos outros dois blocos. Manter 3 blocos ativos gerava ambiguidade sobre qual era a fonte da verdade. A cópia integral foi preservada em `99_ARQUIVO_GERAL`. | 2026-03-26 |
| D-002 | **Consolidar o charter do WS4 — Estrutura Comercial e CRM em uma única versão.** | O arquivo original continha 3 versões repetitivas do mesmo charter, gerando confusão sobre escopo e responsabilidades. A versão consolidada unifica o conteúdo sem perda de informação. | 2026-03-26 |
| D-003 | **Arquivar templates de reunião e notas vazios por workstream.** | 5 arquivos (reuniões de WS2 — Jornada CX DL → Pago, WS3 — Execução Territorial Praças e WS4 — Estrutura Comercial e CRM; notas de WS6 — Embaixadoras Drive Free e WS7 — Modelo Econômico Praça) eram cópias vazias do template oficial `TEMPLATE_WS_REUNIAO.md`. Mantê-los gerava falsa impressão de conteúdo e ruído no acervo. | 2026-03-26 |
| D-004 | **Arquivar ARQUITETURA_OFICIAL_V1.** | A V2 é a versão canônica vigente. Manter a V1 ativa gerava risco de referência a uma estrutura desatualizada. | 2026-03-26 |
| D-005 | **Criar 3 artefatos de governança do acervo.** | O acervo não possuía mecanismo de rastreabilidade de mudanças, registro de fontes canônicas ou mapa de lacunas. Foram criados: `00_REGISTRO_CANONICO_DO_ACERVO.md`, `00_CHANGELOG_CURADORIA.md` e `00_MAPA_DE_LACUNAS_ESTRUTURAIS.md`. | 2026-03-26 |

---

## 2. Plano de Ação — Próximos 14 Dias

As ações abaixo derivam diretamente das lacunas e pendências identificadas na curadoria. Estão ordenadas por impacto em receita e previsibilidade operacional.

| Prioridade | Ação | Responsável Sugerido | Prazo | Dependência |
|---|---|---|---|---|
| **P0 (Crítica)** | Consolidar o dado de MRR líquido de mensalidades (KR7 — MRR Mensalidades). | Diego (Sponsor) | 7 dias | Acesso ao financeiro/BI |
| **P0 (Crítica)** | Definir DRIs para WS3 — Execução Territorial Praças, WS6 — Embaixadoras Drive Free e WS7 — Modelo Econômico Praça. | Diego (Sponsor) | 7 dias | Reunião de diretoria |
| **P1 (Alta)** | Validar e instrumentar a fonte de dados do KR5 — Integrações Ativas. | DRI do WS1 — Comunicação com Corretores | 14 dias | Acesso ao sistema de integrações |
| **P1 (Alta)** | Investigar e resolver a ausência do KR4. | Diego | 7 dias | Nenhuma |
| **P2 (Média)** | Executar o prompt P11 (Consolidação Sócio-Local). | Diego + IA | 14 dias | Nenhuma |
| **P2 (Média)** | Executar o prompt P10 (Processo BDR/Vendas) — vinculado ao WS4 — Estrutura Comercial e CRM. | Gustavo (DRI do WS4) + IA | 14 dias | Disponibilidade do DRI |
| **P2 (Média)** | Executar o prompt P9 (Playbook Evento Territorial) — vinculado ao WS5 — Marketing Event Driven. | DRI do WS5 + IA | 14 dias | Nenhuma |
| **P3 (Baixa)** | Criar README para Bases Consolidadas. | IA | 7 dias | Nenhuma |
| **P3 (Baixa)** | Após validação, deletar a pasta SUPER CÉREBRO original da raiz. | Diego | 14 dias | Validação da migração |

---

## 3. Rituais e Cadências Recomendadas

Com base na análise do acervo, os seguintes rituais são recomendados para manter a saúde do sistema:

| Ritual | Frequência | Responsável | Artefato |
|---|---|---|---|
| **Coleta de dados dos KRs** (Prompt P1) | Mensal | Diego + IA | Atualização dos arquivos KR*.md e 00_KR_INDEX.md |
| **Revisão do Plano Estratégico** (Prompt P2) | Trimestral | Diego + IA | Atualização do Plano Ativo e Versão Executiva |
| **Curadoria do Acervo** | Mensal | IA | Atualização do Changelog, Registro Canônico e Mapa de Lacunas |
| **Revisão de Cadência Operacional** (Prompt P7) | Trimestral | Diego | Atualização do documento de cadência |
| **Report Executivo Mensal** | Mensal | Diego | Geração usando template `REPORT_EXECUTIVO_MENSAL_MODELO.md` |
| **Revisão de Visão e Modelo** (Prompt P4) | Semestral | Diego + IA | Atualização dos documentos fundacionais |

---

## 4. Itens Sem Dono (Lacunas de Responsabilidade)

Os seguintes itens foram identificados como ativos sem responsável definido, o que representa risco direto de paralisia na execução:

| Item | Tipo | Impacto |
|---|---|---|
| WS3 — Execução Territorial Praças | Workstream sem DRI | Ações territoriais sem coordenação formal |
| WS6 — Embaixadoras Drive Free | Workstream sem DRI | Programa de embaixadoras sem dono operacional |
| WS7 — Modelo Econômico Praça | Workstream sem DRI | Decisões de investimento territorial sem responsável |
| KR3 — Eventos Locais | KR com atraso (2/6 em março) | Ritmo 43% abaixo do necessário, sem plano de recuperação definido |
| KR6 — Corretores Ativos | KR com ritmo insuficiente | Crescimento 43% abaixo do necessário |
