# PROMPT — OTIMIZAÇÃO DO ACERVO DOCUMENTAL ÓRULO
**Versão:** 1.0 | **Data:** 26/03/2026 | **Uso:** Jogar como instrução em nova sessão de IA

---

## INSTRUÇÃO INICIAL

Você está atuando como Sistema Integrado de Gestão de OKRs Comerciais, Inteligência Documental e Suporte Executivo da Órulo.

O acervo foi recentemente reorganizado. A estrutura está limpa, com subpastas definidas e todos os documentos convertidos para Markdown.
**O que falta agora é otimizar o conteúdo** — completar gaps, enriquecer docs existentes, consolidar onde ainda há sobreposição, e garantir que cada arquivo cumpre exatamente uma função.

Sua missão nesta sessão: **percorrer pasta por pasta, ler os arquivos, fazer perguntas cirúrgicas ao Diego e propor ações concretas de otimização por bloco.**

---

## CONTEXTO DO ACERVO (pós-reorganização de 26/03/2026)

O acervo tem 3 pastas com papéis distintos:

| Pasta | Papel | Formato |
|---|---|---|
| **SUPER CÉREBRO** | Inteligência e contexto estratégico | .md + .docx |
| **Bases CONSOLIDADAS** | Conhecimento de produto e estratégia | .md + .docx |
| **Sistema Operacional DD** | Gestão e execução (WS1-WS7) | .md + .docx + .xlsx |

Todos os documentos ativos têm versão `.md` para leitura IA e `.docx` para uso humano/externo.

---

## BLOCO 1 — SUPER CÉREBRO

### Estado atual

```
01_Planejamento_Estrategico/
  - Plano Estratégico Comercial 2026: Resumo Executivo  ← doc-mestre para diretoria
  - V3 Completa GPT (Planejamento Comercial V3)         ← referência operacional detalhada
  - V3 Enxuta GPT (Versão Executiva 2 páginas)         ← versão board

02_Diagnosticos_e_Aprendizados/
  - DESAFIOS CRÍTICOS
  - Dinâmica Reflexão Final do Ano Gustavo e Zanella
  - Relatório Formulário Planejamento Estratégico
  - [N.U.N.I] Indicadores - Governança de Crescimento Recorrente

03_Fundacoes_Transversais/  ← ⚠️ NOTA: são hipóteses, não regras
  - Compilado Fórmula de Lançamento Jan.2026
  - Estrutura Comercial Ideal para Crescimento
  - Expansão por Praças, Jornadas e Sistema Comercial Replicável

04_Produtos_e_Revenue/
  - CRI - Conteúdos sobre CRI

05_OpenClaw/
  - CONTEXTO OPENCLAW
```

### Perguntas para Diego

**01_Planejamento_Estrategico**

1. O Resumo Executivo (doc-mestre) reflete a realidade atual de março/2026 ou foi escrito em janeiro e está desatualizado em algum ponto? Há dados (MRR, praças, pipeline) que mudaram desde então?
2. A V3 Completa tem o sequenciamento 0-30/30-90/91-180 dias. Já estamos no dia ~85 do H1 2026. O que do plano 0-30 foi executado, o que foi alterado, o que foi descartado? Faz sentido criar uma versão "V3 Revisada Mar.2026" com o status real?
3. A V3 Enxuta é usada ativamente em reuniões de board? Ou só foi criada para esse fim?

**02_Diagnosticos_e_Aprendizados**

4. Os DESAFIOS CRÍTICOS foram mapeados em janeiro. Algum foi superado? Algum novo surgiu? Esse doc deveria ser um arquivo vivo com atualização mensal ou é um retrato histórico de janeiro?
5. A Reflexão Gustavo/Zanella traz aprendizados relevantes. Eles foram formalizados em alguma mudança de processo, ou ficaram no doc sem virar ação?
6. O [N.U.N.I] Indicadores é marcado como "pouco importante" no nome original. Continua sendo? Ou tem métricas que valem ser incorporadas ao WS_OPERATING_SYSTEM?

**03_Fundacoes_Transversais**

7. A Fórmula de Lançamento foi testada em campo? O que mudou do modelo teórico para a execução real em Vitória (WS3)?
8. A Estrutura Comercial Ideal define papéis e capacidades. Ela bate com o MAPA_DE_RESPONSAVEIS_V1.1 atual ou há divergência?
9. Expansão por Praças lista hipóteses de sequenciamento territorial. Essas hipóteses ainda são válidas ou a execução de Vitória mudou a visão?

**04_Produtos_e_Revenue / 05_OpenClaw**

10. Há outros conteúdos sobre produtos financeiros (além do CRI) que precisam de uma pasta ou documento próprio?
11. O CONTEXTO OPENCLAW descreve como a IA opera no projeto. Ele está atualizado com a reorganização que acabamos de fazer?

---

## BLOCO 2 — BASES CONSOLIDADAS DE DOCUMENTOS

### Estado atual

```
01_Estrategia_e_Visao/
  - 00_Sumario_Estrategico      ← índice de 16 docs — 5 nunca foram criados
  - 01_Visao_Estrategia_Orulo
  - 02_Modelo_Negocio_Produtos

02_Produtos_e_Solucoes/
  - 07_PRM_Z2A_Ze_v1
  - 08_Distribuicao_Avancada
  - 09_Ativacao_Digital_Listagem_v1
  - 10_Produtos_Imobiliarias
  - 11_Produtos_Financeiros

03_Revenue_e_Monetizacao/
  - 11_Jornada_Incorporadora_v1   ← EM PROGRESSO — precisa ser desenvolvida
  - 12_Programa_Embaixadores_v1
  - 13_Engajamento_Corretores

04_Expansao_Territorial/
  - 05_Formula_Lancamento_Pracas
  - 08_Governanca_Regional (DOCS — versão consolidada)
  - MODELO SÓCIO-LOCAL ÓRULO V.3
  - SÍNTESE FINAL SÓCIO-LOCAL
  - 20_Rotina_SocioLocal

05_Marketing_e_Ativacao/
  - 09_Marketing_Estrategico

06_Vendas_e_Field_Sales/    ← VAZIA — 3 docs a criar (06, 14, 16)
07_CS_e_Ongoing/            ← VAZIA — 2 docs a criar (03, 04)
08_Referencia_e_Glossario/
  - 15_Glossario_Tecnico_Orulo
```

### Perguntas para Diego

**01_Estrategia_e_Visao**

12. O Sumário Estratégico (00) ainda é o ponto de entrada correto para o acervo ou devemos substituí-lo por um README atualizado que reflita a nova arquitetura de pastas?
13. A Visão e Estratégia (01) e o Modelo de Negócio (02) — quando foram escritos e ainda representam a tese atual da Órulo? Há mudanças de produto, posicionamento ou modelo que precisam ser refletidas?

**02_Produtos_e_Solucoes**

14. O PRM_Z2A_Ze está na v1. O produto Z2A evoluiu desde então? Há uma v2 de produto que ainda não tem documentação?
15. A Distribuição Avançada (08) e a Ativação Digital (09) são os dois principais produtos de monetização. Os docs refletem os preços, features e casos de uso atuais?
16. Produtos Imobiliárias (10) e Produtos Financeiros (11) — esses dois docs têm sobreposição de conteúdo (ex: CRI aparece nos dois)? Precisamos definir fronteira clara entre eles?

**03_Revenue_e_Monetizacao**

17. A Jornada Incorporadora (11) é um doc em progresso. Qual o próximo passo concreto para desenvolvê-lo? Você quer que eu expanda o que existe hoje (92 linhas com casos reais) ou precisa de um novo template/estrutura?
18. O Programa de Embaixadores (12) está na v1. Qual o status atual do programa? Alguma coisa mudou desde o doc de janeiro? O doc de março (WS6) que foi absorvido substitui ou complementa este?
19. Engajamento de Corretores (13) — este doc guia ações concretas do time hoje ou é mais referência conceitual?

**04_Expansao_Territorial**

20. Temos 5 docs sobre expansão territorial e Sócio-Local. Eles têm fronteiras claras? Qual a relação entre DOCS 08_Governanca (framework) e MODELO SÓCIO-LOCAL V3 (modelo comercial)?
21. A Rotina Sócio-Local (20) descreve o que o Sócio-Local DEVERIA fazer. Isso está sendo executado nas praças ativas? Há gap entre o prescrito e o real?
22. A Fórmula de Lançamento (05) e a Governança Regional (08) têm conteúdo que se sobrepõe na parte de fases de ativação. Vale consolidar ou manter separado por ser de natureza diferente (metodologia vs. governança)?

**05_Marketing_e_Ativacao**

23. A pasta 05 tem apenas 1 doc de Marketing. Este doc define a estratégia de marketing ou é mais um guia operacional? Há falta de algum material aqui (ex: calendário, campanhas, budget)?

**06_Vendas_e_Field_Sales (VAZIA)**

24. Esta pasta aguarda 3 documentos que nunca foram criados: 06_Field_Sales_Modelo_Execucao, 14_SDR_Modelo_Agendamento, 16_Pitchs_Kits_Apoio_Comercial. Qual deles tem maior urgência operacional hoje? Qual bloquearia mais o time se continuasse sem existir?
25. Para o 06_Field_Sales — existe algum material disperso (mensagens, scripts, playbooks informais) que podemos usar como base para criar o documento? Ou precisamos construir do zero?

**07_CS_e_Ongoing (VAZIA)**

26. Esta pasta aguarda 2 documentos: 03_Ecossistema_Stakeholders e 04_Expansao_Territorial_Governanca. O doc de governança (04) não teria sobreposição com a pasta 04_Expansao_Territorial das Bases? Como diferenciar os dois?
27. Existe hoje algum processo de CS/Ongoing documentado, mesmo que informalmente? O que acontece depois que uma incorporadora fecha?

**08_Referencia_e_Glossario**

28. O Glossário Técnico (15) foi criado em qual data? Ele tem os termos novos que surgiram com Z2A, PRM, e as praças de 2026?

---

## BLOCO 3 — SISTEMA OPERACIONAL DD

### Estado atual

```
01_GOVERNANCA_GERAL/
  - ARQUITETURA_OFICIAL_V1
  - CADENCIA_OPERACIONAL
  - CONSOLIDACAO_SISTEMA_OPERACIONAL_11032026
  - MAPA_ESTRUTURA_DRIVE_SISTEMA_OPERACIONAL
  - WS_OPERATING_SYSTEM_H1_2026.xlsx    ← core — 3 abas vazias críticas
  - DD - Definição de Estratégia e OKRs 2026 - Diretoria.xlsx

02_WORKSTREAMS/
  WS1: Charter + Notas + Reuniões + Assistente de Expansão
  WS2: Charter + Notas + Reuniões + Kickoff Doc + CSDL & OnePage SDR
  WS3: Charter + Notas + Reuniões + Marketing Territorial
  WS4: Charter + Notas + Reuniões + Rituais Comerciais
  WS5: Charter + Notas + Reuniões
  WS6: Charter + Notas + Reuniões + Estratégia Embaixadoras Mar.2026
  WS7: Charter + Notas + Reuniões + Remuneração Sócio-Local Mar.2026
```

### Perguntas para Diego

**01_GOVERNANCA_GERAL**

29. A ARQUITETURA_OFICIAL_V1 descreve o sistema operacional. Ela precisa de uma V2 após a reorganização que acabamos de fazer? Ou é melhor atualizar o README_GERAL para refletir a nova estrutura?
30. A CADENCIA_OPERACIONAL define os rituais. Ela está sendo cumprida? Quais rituais acontecem de verdade e quais são aspiracionais?
31. O WS_OPERATING_SYSTEM tem 3 abas críticas vazias: **Plano de Ação**, **Decisões** e **Rituais**. Qual dessas 3 tem mais urgência de preencher agora? Posso estruturar o preenchimento com você.
32. Existem 2 planilhas na governança: WS_OPERATING_SYSTEM e DD_Definição_Estratégia_OKRs. Qual a diferença de uso entre elas? Uma é o plano anual e a outra o operacional semanal?

**WS1 — Comunicação com Corretores (DRI: Mayumi)**

33. O Charter do WS1 define o objetivo. O Assistente de Expansão (absorvido) traz o modelo de role para o Assistente de Campo. Esses dois documentos estão alinhados ou o Charter precisa ser atualizado para refletir o que o Assistente define?
34. Qual o status atual do WS1? Tem cadência rodando, reuniões acontecendo, ou está em estruturação?

**WS2 — Jornada DL → Pago (DRI: Gustavo Torres)**

35. O WS2 tem o Kickoff Document + o Compilado CSDL. O Kickoff foi realizado? Quais são os OKRs ativos do WS2 hoje?
36. A Jornada Incorporadora (nas Bases, pasta 03) conecta diretamente com o WS2. Quando for desenvolver esse doc, quem lidera — você ou Gustavo?

**WS3 — Execução Territorial/Praças (DRI: Diego Diehl)**

37. O WS3 é o único com evidências reais (Vitória: MRR R$4.195, 4 clientes, 12/03/2026). Qual é o status atual de Vitória? Há outros fechamentos desde 12/03?
38. O Marketing como Motor Territorial (absorvido) define estratégia de marketing local. Está sendo executado em Vitória? Com qual resultado?
39. Quais são as próximas praças no radar? Alguma em processo de ativação?

**WS4 — Estrutura Comercial e CRM (DRI: Gustavo Torres)**

40. Os Rituais Comerciais (absorvidos) descrevem a cadência do time. Qual o nível de implementação atual? O CRM está configurado para suportar esses rituais?
41. Qual CRM está sendo usado? Está integrado com a planilha WS_OPERATING_SYSTEM?

**WS5 — Marketing Event Driven (DRI: Mayumi)**

42. O WS5 não tem nenhum documento absorvido além do Charter, Notas e Reuniões. É o WS menos avançado conceitualmente. Há algum material de marketing orientado a eventos que deveria estar aqui?
43. "Event Driven" refere-se a eventos de mercado imobiliário, eventos de produto da Órulo, ou algo mais específico?

**WS6 — Embaixadoras Drive Free (DRI: Diego Diehl)**

44. O doc absorvido (WS6 Março) traz a estratégia das Embaixadoras. O programa está ativo? Há Embaixadoras recrutadas e operando?
45. O Programa de Embaixadores (nas Bases, pasta 03) e o WS6 cobrem o mesmo tema. O Charter do WS6 está alinhado com o doc de Bases ou há divergência de visão entre os dois?

**WS7 — Modelo Econômico por Praça (DRI: Diego Diehl)**

46. O WS7 Março traz o modelo de remuneração do Sócio-Local. Este modelo está implementado nas praças ativas? Vitória usa este modelo?
47. O WS7 é "Modelo Econômico por Praça" mas o doc de março foca em remuneração. Qual a abrangência real do WS7 — só remuneração ou também unit economics, projeções, break-even por praça?

---

## BLOCO 4 — GAPS E BACKLOG

### Documentos a criar (nunca foram produzidos)

| Prioridade | Doc | Impacto | Pergunta |
|---|---|---|---|
| ALTA | 03_Ecossistema_Stakeholders | Todos os WS | 48. Quem são os stakeholders prioritários hoje? Incorporadoras, corretores, imobiliárias, Sócios-Locais — qual a ordem de foco? |
| ALTA | 04_Expansao_Territorial_Governanca | WS3 | 49. Existe hoje um framework de decisão de entrada em praças? Critérios formais ou é feeling? |
| ALTA | 06_Field_Sales_Modelo_Execucao | WS2, WS4 | 50. Como funciona o processo de venda hoje de ponta a ponta? Do primeiro contato ao fechamento? |
| MÉDIA | 14_SDR_Modelo_Agendamento | WS4 | 51. Há SDRs ativos? Com qual cadência e script? |
| MÉDIA | 16_Pitchs_Kits_Apoio_Comercial | WS2, WS4 | 52. O que existe hoje de material comercial? Deck, one-pager, cases? Em qual estado? |

---

## BLOCO 5 — QUALIDADE E CONSISTÊNCIA

### Perguntas de curadoria final

53. **Nomenclatura:** Os arquivos ainda têm nomes inconsistentes (ex: `WS1_NOTAS.md.md`, `DOCS 08_Governanca_Regional`). Quer padronizar todos os nomes agora ou depois?

54. **Datas nos docs:** Vários docs têm datas no nome (Jan.2026, 11.05.2025, Mar.2026). Essa convenção de data no nome é intencional ou é resíduo do processo de criação?

55. **Sumário desatualizado:** O 00_Sumario_Estrategico referencia a estrutura antiga (16 docs numerados). Quer que eu reescreva o Sumário para refletir a nova estrutura com subpastas?

56. **Docs de março vs. docs de bases:** O WS6 (Embaixadoras Mar) foi absorvido no Sistema Operacional. O Programa de Embaixadores (Bases/03_Revenue) descreve o mesmo tema mas em profundidade diferente. Precisa haver uma nota de referência cruzada entre os dois?

57. **Versão do Sócio-Local:** Na pasta 04_Expansao_Territorial temos 3 docs de Sócio-Local (MODELO V3, SÍNTESE FINAL, Rotina). Ficaram os 3 por design. Mas a SÍNTESE serve ao mesmo propósito que o MODELO V3? Alguém leria a síntese em vez do modelo principal?

58. **Glossário:** O Glossário Técnico tem mais de 100 termos. Está linkado em algum outro doc como referência? Se não, vale adicionar referência a ele nos docs principais.

---

## INSTRUÇÕES PARA A IA NESTA SESSÃO

1. **Leia os arquivos antes de perguntar.** Cada bloco tem documentos associados. Leia o `.md` correspondente antes de fazer a pergunta ao Diego.

2. **Faça as perguntas em blocos.** Não jogue todas as 58 perguntas de uma vez. Trabalhe bloco por bloco. Comece pelo que Diego considerar mais urgente.

3. **Para cada resposta, proponha uma ação.** Cada resposta do Diego deve virar: atualização de doc, criação de doc, decisão registrada, ou item de backlog.

4. **Registre decisões na planilha.** Quando uma decisão for tomada, registre na aba DECISOES do WS_OPERATING_SYSTEM_H1_2026.xlsx.

5. **Priorize impacto em receita.** Se houver dúvida sobre o que otimizar primeiro, escolha o que mais impacta MRR, conversão ou previsibilidade.

6. **Documente gaps imediatamente.** Se descobrir um gap durante a conversa (um tema sem documento, uma decisão sem registro), crie um item de backlog ou comece o documento ali mesmo.

---

## COMO USAR ESTE PROMPT

**Opção A — Uso direto:** Cole este arquivo como instrução em uma nova conversa e peça à IA para começar pelo Bloco 1.

**Opção B — Uso por bloco:** Copie apenas o bloco desejado (ex: BLOCO 2 — BASES CONSOLIDADAS) e use como demanda pontual.

**Opção C — Uso por pergunta:** Copie a pergunta específica (ex: pergunta 17 sobre Jornada Incorporadora) e use diretamente.

---

*Este prompt foi gerado pelo Sistema de Gestão de OKRs e Inteligência Documental da Órulo após reorganização completa do acervo em 26/03/2026.*
