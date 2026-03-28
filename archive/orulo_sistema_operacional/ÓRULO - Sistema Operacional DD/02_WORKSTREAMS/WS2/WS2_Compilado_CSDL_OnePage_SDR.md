**Introdução**
==============

**Versão:** v1 • **Fonte:** exclusivamente o conteúdo deste chat • **Escopo temporal:** conversa atual (sem fontes externas)

**\# Propósito**
----------------

Organizar, de forma prática e rastreável, os **aprendizados, decisões, frameworks e artefatos operacionais** definidos neste chat sobre o modelo **CSDL (Customer Success para Distribuição Limitada)** aplicado ao **freemium DL**, com a criação e adoção da **OnePage SDR** como instrumento de execução diária.

**\# O que este documento contém**
----------------------------------

1.  **Parte 1 --- Sumário Executivo:** decisões, aprendizados, implicações, riscos e "o que mudou no playbook".

2.  **Parte 2 --- Corpo Analítico:** arquitetura CSDL+Sales Engagement, OnePage SDR (colunas/categorias), scoring & SLAs, métricas (TTFV, Ativação 7/30, DL→Pago 30/60), bundles por maturidade, handoffs (SDR→CS-DL→AE), rituais e glossário.

3.  **Parte 3 --- Anexos Operacionais:** modelos de mensagens (≤280), prompts operacionais, queries/filters, campos mínimos no CRM (Bitrix), estrutura da planilha e pseudorroteiros (Setup Express, Office Hour).

> **Rastreabilidade:** toda afirmação deriva **apenas** deste chat; quando houver consolidação interpretativa, está sinalizada como **(inferência)**.

**\# Como usar (leitura rápida e execução)**
--------------------------------------------

-   **Líderes/Coordenação:** validar guardrails (cap/cooldown), SLAs por classe (HOT/WARM/COOL), campos do CRM e rituais.

-   **SDR-CX/CS-DL/AE:** aplicar **scripts curtos com entrega de valor**, seguir handoffs por **SQDL** (2 de 3: Uso, Engajamento, ROI), alimentar métricas no CRM.

-   **Sócio-Local/GDD:** injetar **prova social territorial** e manter **priorização por dados** (thresholds de views, comandos Z2A, CTR p90).

-   **Marketing/Operações/Produto:** garantir eventos críticos (login, views, propostas, comandos Z2A) para acionar os **triggers** da OnePage SDR.

**\# Indicadores-âncora**
-------------------------

-   **TTFV (Time-to-First-Value)**, **Ativação 7/30** e **DL→Pago 30/60** como norte.

-   **KPI bar** (linha 1 do sheet): TTFV (mediana) \| Ativação 7/30 \| DL→Pago 30/60 \| HOTs abertos \| SLAs vencendo (24h).

**\# Limites e próximos passos**
--------------------------------

-   **Limites:** dependência de dados (Admin/Bitrix/PRM/Z2A/Movidesk), padronização do "evento de valor".

-   **Próximos passos:** definir **thresholds por praça** (views, comandos Z2A), padronizar **Aha Moment**, publicar **campos obrigatórios** no Bitrix e estabilizar **Office Hours** por praça/tema.

**Parte 1 --- Sumário Executivo**
=================================

Versão: v1 • Data: 2026-01-06

**\# Objetivo**
---------------

Consolidar os principais **aprendizados, decisões e implicações operacionais** desta conversa (somente este chat) sobre **CSDL (Customer Success para Distribuição Limitada)**, **freemium DL**, **Sales Engagement orientado por dados** e a criação da **OnePage SDR** para governança diária.

**\# Decisões e direções confirmadas (rastreáveis ao chat)**
------------------------------------------------------------

1.  **Modelo híbrido (CSDL + Sales Engagement leve)**: priorizar **interações com entrega de valor** em vez de insistência para reunião; usar cadências curtas e contextuais (Whats/Email) com **cap de 2 toques/semana/canal**.

2.  **Foco em TTFV e Aha Moment**: toda abordagem deve acionar **1º uso de valor** (ex.: **card ativo** ou **Z2A**) em até **D+14**, reduzindo **TTFV** e elevando **Ativação 7/30**.

3.  **OnePage SDR** em **uma única aba**: mapa das **alavancas de interação** com origem da lista, objetivo, mensagem, SLA, dono e bundle-alvo --- para o coordenador (Gustavo) **priorizar e cobrar execução**.

4.  **Prioridade por triggers de uso**: HOT ≤48h para: **muitas visualizações**, **acesso recente (≤48h)**, **proposta recebida**, **spike Z2A**, **pressão de corretores**.

5.  **Papéis e handoffs**: **SDR-CX** (abertura/ativação) → **CS-DL** (onboarding/valor) → **AE** (bundle/fechamento). **Sócio-Local** entra como prova social territorial; **GDD** classifica e agenda prioridades.

6.  **Bundles por maturidade**: **DA+Z2A** (engajamento inicial), **DA+PRM** (gestão), **DA+Ativação Digital** (performance).

7.  **Governança**: rituais **diários** (HOTs, SLAs), **semanais** (aprendizados e thresholds por praça) e **mensais** (TTFV/Ativação/DL→Pago).

8.  **Limites por canal**: WhatsApp e Email **máx. 2/semana**; **call** somente após interação positiva; **cooldown 30 dias** após 3 tentativas sem resposta.

> Observação: onde incluímos síntese/organização (ex.: score HOT/WARM/COOL), marcamos como **(inferência)** quando o raciocínio consolidou o que estava implícito.

**\# Principais aprendizados**
------------------------------

-   **Freemium é funil "dentro do produto"**: o "topo" não é awareness externo; é **ativação de uso**. Logo, **Sales Engagement** precisa estar acoplado ao **comportamento no app** (triggers) e não a listas frias.

-   **Mensagens têm de entregar valor** (micro-resultados): **mini-relatório de audiência**, **card pronto**, **insight de praça**, **organização PRM** --- isso acelera a passagem para **SQDL** (pronto para venda).

-   **Território importa**: **Sócio-Local** aumenta resposta/comparecimento ao trazer **case da praça** e **demanda dos corretores**; **GDD** estabiliza a priorização via dados.

-   **Menos "SDR clássico", mais "CSDL consultivo"**: cadências **curtas**, sem saturação, **clareza de propósito** (abrir conversa e ativar uso, não "empurrar demo").

-   **Métricas que importam**: **TTFV**, **Ativação 7/30** e **DL→Pago 30/60**; reuniões sem valor não são proxy confiável de progresso.

**\# Implicações operacionais (o que fazer)**
---------------------------------------------

1.  **Publicar e adotar a OnePage SDR** como **fonte única**:

    -   Colunas padrão (alavanca, origem, query, objetivo, mensagem, **SLA**, dono, **bundle**, automação).

    -   Linhas já mapeadas: **novos cadastros**, **acesso recente**, **muitas views**, **spike Z2A**, **proposta recebida**, **indicações/Embaixadoras**, **inativos**, **no-show** etc.

2.  **Implementar scoring e classes (inferência)**:

    -   **HOT (≥5)**, **WARM (3--4)**, **COOL (≤2)**, com **SLA** de 24--48h / 48--72h / 96--168h.

3.  **Handoffs claros**:

    -   **SDR→CS-DL** quando existir **(i) uso + (ii) engajamento**.

    -   **CS-DL→AE** quando houver **(i)+(ii)** e **(iii) sinal de ROI** (ex.: audiência/proposta/PRM).

4.  **Instrumentar métricas no CRM/Movidesk/Admin**:

    -   **TTFV** (cadastro → 1º valor), **Ativação 7/30**, **DL→Pago 30/60**, **HOTs abertos** e **SLAs a vencer** (KPI bar).

5.  **Revisar cadências e scripts**:

    -   Mensagens **≤280 caracteres**, sem "pedido de reunião" vazio; sempre **um próximo passo de valor** (ex.: "deixo 1 card e te mando o alcance").

6.  **Rituais**:

    -   **Daily**: HOTs, SLAs, redistribuição. **Weekly**: learning por praça, thresholds de trigger. **Monthly**: saúde do funil (TTFV/Ativação/Conversão).

**\# Riscos, limites e lacunas (com próximos passos)**
------------------------------------------------------

-   **Risco de saturação** se cadências ignorarem o **cap** por canal. → **Ação**: bloquear regras no CRM e revisar templates quinzenalmente.

-   **Medição imperfeita de TTFV** se **"evento de valor"** não estiver padronizado. → **Ação**: padronizar (card ativo, Z2A executado ou PRM com próximo passo).

-   **Dependências de dados** (Admin/Bitrix/PRM/Movidesk) para acionar triggers. → **Ação**: priorizar integrações mínimas viáveis (login, views, propostas, Z2A).

-   **Territórios com baixa densidade** podem diluir taxa de resposta. → **Ação**: **Sócio-Local** ativa **office hours** temáticos com case local e embaixadoras.

-   **Confusão de papéis** em picos de demanda. → **Ação**: check diário de **handoffs** e fila HOT com dono explícito.

**\# O que mudou no playbook (5--10 bullets)**
----------------------------------------------

1.  **Meta de conversa/valor** substitui "meta de reunião": cada contato deve **entregar algo útil**.

2.  **Triggers de uso** guiam a ação (não listas frias); **SLA HOT ≤48h**.

3.  **Papéis/handoffs** definidos por **sinais de uso/engajamento/ROI (SQDL)**.

4.  **KPI bar** prioriza **TTFV**, **Ativação 7/30**, **DL→Pago 30/60** e **SLAs**.

5.  **Cap de cadência** por canal e **cooldown 30 dias** após silêncio.

6.  **Bundles por maturidade** (DA+Z2A / DA+PRM / DA+Ativação).

7.  **Sócio-Local + GDD** entram na **priorização territorial** e prova social.

8.  **Glossário comum** (office hour, setup express, spike Z2A...) para evitar ruído interno.

**\# Próximas perguntas (para a Parte 2 detalhar)**
---------------------------------------------------

-   Quais **thresholds** por praça para "muitas visualizações" e "spike Z2A"?

-   Qual **definição única** de **Aha Moment** para todos os squads?

-   Como **operacionalizar** o **KPI bar** (fonte, refresh, owner)?

-   Qual **roteiro mínimo** por persona (Diretoria, MKT, GP) nas primeiras 2 semanas?

-   Quais campos obrigatórios no **Bitrix** para suportar **SQDL** e **classes**?

**Parte 2 --- Corpo Analítico**
===============================

Versão: v1 • Data: 2026-01-06

**\# 2.1 Arquitetura geral (modelo híbrido Órulo: CSDL + Sales Engagement orientado por dados)**
------------------------------------------------------------------------------------------------

-   **Princípio:** freemium = funil "dentro do produto". Priorizar triggers de uso e interações com entrega de valor (não "pedido de demo").

-   **Fluxo macro:**

    -   **Detecção (GDD)** → 2) **Abertura/Ativação (SDR-CX)** → 3) **Onboarding de Valor (CS-DL)** → 4) **Proposta/Fechamento (AE)** → 5) **Prova social territorial (Sócio-Local)**.

-   **Objetivos primários por função:**

    -   **SDR-CX:** reduzir **TTFV** e provocar **Aha Moment** inicial.

    -   **CS-DL:** estabilizar **Ativação 7/30** e gerar evidências de ROI.

    -   **AE:** converter **DL→Pago 30/60** com bundle adequado.

    -   **Sócio-Local:** elevar resposta/comparecimento com **case e rede da praça**.

    -   **GDD:** priorização, score e governança de painéis.

**\# 2.2 OnePage SDR --- estrutura de uso (uma aba, governança diária)**
------------------------------------------------------------------------

**Colunas padrão (para cada alavanca):** Alavanca \| Origem \| Filtro/Query \| Contexto \| Objetivo primário \| Objetivo secundário \| Abordagem \| Script ≤280 \| Canal \| Cadência \| Cap/conta \| Dono \| Handoff (SQDL) \| SLA(h) \| Métrica-chave \| Métricas secundárias \| Bundle \| Automação (S/N) \| Observações.

**Categorias de alavancas (exemplos práticos):**

-   **Inbound/Freemium/Territorial:** Novos cadastros DL; Nova incorporadora (praça foco); Leads de eventos/OH.

-   **Usage Triggers:** Acesso recente (≤48h); Muitas visualizações; Spike Z2A; PRM sem follow; Pressão de corretores.

-   **Operacional/Suporte→CSDL:** Inclusão/atualização de produto; Solicitação de edição; Correção de informação; Tickets resolvidos (CSAT alto).

-   **Parcerias/Mercado:** Indicações Embaixadoras; Houses/Parcerias.

-   **Marketing Signals/Reengajamento:** Ativação Digital p90 (CTR alto); Listagem Patrocinada topo; Inativos; No-show.

-   **Governança:** Backlog HOT vencendo SLA.

**Regras de ouro de canal e cadência:**

-   **Cap por conta:** até **2 toques/semana** por canal (Whats/Email); **call** apenas após interação positiva.

-   **Cooldown:** após 3 tentativas sem resposta → **pausa 30 dias** (retoma por Marketing/OH).

-   **Mensagem = entrega:** cada contato deve **entregar algo** (card pronto, insight, mini-relatório, organização PRM).

**\# 2.3 Handoffs, SQDL e critérios de avanço**
-----------------------------------------------

-   **Definição de SQDL (pronto p/ venda):** atingiu **2 de 3 sinais**

    -   **Uso** (login + ação: card/Z2A/edição),

    -   **Engajamento** (resposta, participação em OH),

    -   **ROI sinal** (audiência relevante, proposta recebida, funil PRM ativo).

-   **Handoffs:**

    -   **SDR-CX → CS-DL**: quando houver **Uso + Engajamento**.

    -   **CS-DL → AE**: quando houver **Uso + Engajamento + ROI sinal**.

    -   **Sócio-Local** pode entrar **antes** do AE para elevar probabilidade (prova social territorial).

-   **Campos mínimos no CRM (Bitrix):** Classe (HOT/WARM/COOL), Score, SQDL (Y/N), Praça foco (Y/N), Último trigger, Próximo passo, Dono.

**\# 2.4 Scoring e SLAs (priorização objetiva)**
------------------------------------------------

**Score por sinais (ajustável por praça):**

-   **+3:** Proposta recebida; Muitas visualizações (pico); Spike Z2A; Pressão de corretores ≥N; Acesso ≤24h **com** interação.

-   **+2:** Inclusão/atualização de produto; Solicitação de edição; LP topo; Ativação Digital p90; Novos usuários vinculados.

-   **+1:** Novo cadastro DL; Reunião cancelada; Correção de informação; Inativo reengajável.

-   **Bônus:** Praça foco **(+1)**; Indicação Embaixadora/House **(+1)**.

**Classes e SLAs:**

-   **HOT (Score ≥5):** reagir em **24--48h**; rota **CS-DL/AE**.

-   **WARM (3--4):** **48--72h**; rota **SDR-CX → CS-DL**.

-   **COOL (≤2):** **96--168h**; nutrir com OH/campanhas.

**KPI Bar (topo da aba):** **TTFV (mediana)** \| **Ativação 7/30** \| **DL→Pago 30/60** \| **HOTs abertos** \| **SLAs vencendo (24h)**.

**\# 2.5 Métricas e instrumentação**
------------------------------------

-   **TTFV (Time-to-First-Value):** cadastro DL → 1º evento de valor (card ativo / Z2A executado / PRM com próximo passo).

-   **Ativação 7/30:** % de DL com ≥1 ação-chave em 7 e 30 dias.

-   **DL→Pago 30/60:** % de DL que viram pagantes em 30/60 dias.

-   **Conversão PRM:** % de oportunidades com **próximo passo** e avanço de etapa.

-   **Reativação %:** contas inativas que voltam a usar após campanha/insight.

-   **Operacionais:** taxa de resposta por canal, comparecimento OH, no-show, tempo de publicação (produto), tempo de resolução (ticket).

**Fontes de dados:** Admin (cadastro/produtos/edições), Bitrix/CRM (cadências, estágios, no-show), Logs web/app (login, views), PRM (oportunidades, next step), Z2A (comandos), Movidesk (CSAT), Marketing (CTR/LP).

**\# 2.6 Bundles por maturidade (conectar evidência → oferta)**
---------------------------------------------------------------

-   **Nível 1 -- Engajamento inicial (descoberta):** **DA + Z2A** → visibilidade + automação básica; alvo: ativação rápida (card + 1 comando).

-   **Nível 2 -- Gestão e escala (consideração):** **DA + PRM** → organização do funil e prova de ROI; alvo: reduzir dispersão e perda de calor.

-   **Nível 3 -- Performance (decisão):** **DA + Ativação Digital** (e eventual LP) → captura de demanda e giro; alvo: exploração de picos (CTR/LP/pressão).

**Regras:** bundle é proposto **apenas** após evidência de uso/ROI emergente (evitar pitch precoce).

**\# 2.7 Playbooks curtos por alavanca (scripts ≤280 + ação de valor)**
-----------------------------------------------------------------------

**Acesso recente (≤48h) -- WhatsApp**

> "Oi {{nome}}, vi seu acesso hoje. Ativo **1 card** em **20'** e te mando um mini-relatório de audiência. **Amanhã 10h ou 15h?**"

**Muitas visualizações -- WhatsApp**

> "{{produto}} teve **{{N}} views** em **{{bairro}}**. Posso ampliar hoje com **card + Z2A** e te entregar o alcance?"

**Proposta recebida -- WhatsApp + Call**

> "Chegou proposta. Estruturo **PRM + follow** agora para não perder calor. **15'**?"

**Solicitação de edição -- WhatsApp**

> "Corrigi e deixei **1 card pronto** pra testar alcance. Quer medir agora?"

**No-show -- WhatsApp**

> "Deixei **1 card pronto**. Reagendo **15'** só pra ativar e encerrar?"

**Indicação Embaixadora -- WhatsApp (Sócio-Local)**

> "Top corretores pediram seu produto. Em **20'** mostro **DA+Z2A** pra escalar isso com prova social da praça."

**\# 2.8 Rituais de gestão (disciplinas que garantem execução)**
----------------------------------------------------------------

-   **Diário (15 min, coordenação):** HOTs novos; SLAs a vencer; handoffs pendentes; reatribuição.

-   **Semanal (30--45 min):** lições de cópia; thresholds por praça (views, comandos Z2A, CTR p90); impedimentos de dados/CRM; agenda de OH.

-   **Mensal (60 min):** **TTFV/Ativação/DL→Pago**, casos por praça, revisão de bundles, ajustes de cap/cooldown.

-   **Ponto crítico:** "mensagem tem que **entregar**" --- qualquer cadência que não entrega valor **é revisada**.

**\# 2.9 Glossário resumido (operacional)**
-------------------------------------------

-   **Office hour (OH):** sessão coletiva semanal (30--45'), 1:many, para ativar, demonstrar e tirar dúvidas; eleva comparecimento e adoção.

-   **Setup Express:** onboarding prático (15--30') para colocar **um** caso de uso no ar (card/Z2A) e capturar o **1º valor**.

-   **Spike Z2A:** pico de comandos/uso do "Zé" (ex.: z2a\_cmd\_7d\>=X); sinal de adoção/escala.

-   **Card:** peça rápida rastreável para medir **alcance e interesse**.

-   **PRM:** gestão de oportunidades com parceiros (corretores/imobiliárias) com **próximo passo** e automações.

-   **LP (Listagem Patrocinada):** destaque pago em resultados; acoplar PRM para capturar intenção.

-   **Pressão de corretores:** volume de pedidos do canal; forte prova social local.

-   **SQDL:** conta DL pronta p/ venda (2 de 3: Uso, Engajamento, ROI sinal).

**\# 2.10 Riscos e controles (guardrails)**
-------------------------------------------

-   **Saturação por canal:** respeitar **cap** e revisar templates quinzenais.

-   **Medição frágil de TTFV:** padronizar evento-alvo (card/Z2A/PRM).

-   **Dependências de dados:** priorizar integrações mínimas (login, views, proposta, comandos Z2A).

-   **Ambiguidade de papéis:** campo **Dono** + handoff explícito em CRM; checagem diária.

-   **Territórios com baixa densidade:** ativar OH temáticos e Embaixadoras para elevar resposta.

**Parte 3 --- Anexos Operacionais**
===================================

Versão: v1 • Data: 2026-01-06

> Escopo: somente o conteúdo deste chat. Onde houver consolidação de ideias implícitas, marcado como **(inferência)**.

**\# 3.1 Modelos de mensagem (≤280 caracteres)**
------------------------------------------------

### **Acesso recente (≤48h) --- WhatsApp**

> Oi {{nome}}, vi seu acesso hoje. Ativo **1 card** em **20'** e te mando um mini-relatório de audiência. **Amanhã 10h ou 15h?**

### **Muitas visualizações --- WhatsApp**

> {{produto}} teve **{{N}} views** em **{{bairro}}**. Posso **ampliar hoje** com **card + Z2A** e te entregar o alcance?

### **Proposta recebida --- WhatsApp + call curta**

> Chegou proposta. Estruturo **PRM + follow** para não perder calor. **15'** agora ou fim do dia?

### **Solicitação de edição --- WhatsApp**

> Corrigi os dados e deixei **1 card pronto** pra testar alcance. Quer medir agora comigo? Leva **20'**.

### **No-show (reagendamento com valor) --- WhatsApp**

> Deixei **1 card pronto**. Reagendo **15'** só pra ativar e encerrar?

### **Indicação Embaixadora / pressão do canal --- WhatsApp (Sócio-Local)**

> Top corretores da praça pediram seu produto. Em **20'** te mostro **DA+Z2A** pra escalar com prova social local.

### **Reengajamento inativos --- Email (quinzenal)**

Assunto: Seu produto na mira dos corretores da {{cidade}}\
Corpo (curto):

-   **Top 5 buscas** da praça esta semana ({{bairros}}).

-   Sugestão: publicar **1 card** e ligar **Z2A** para captar a demanda.

-   Se quiser, configuro em **20'** e envio o alcance. **Responder "OK"** já ativa.

*(Todas seguem cap: máx. 2 toques/semana/canal; call só após interação positiva.)*

**\# 3.2 Prompts operacionais (coláveis)**
------------------------------------------

### **Master Prompt --- OnePage SDR (alimentar o mapa)**

> Atue como estrategista CSDL/PLG. A partir do conteúdo **deste chat**, extraia alavancas de interação e entregue **tabela** com: Alavanca \| Origem \| Filtro/Query \| Contexto \| Objetivo prim/seg \| Abordagem \| Script ≤280 \| Canal \| Cadência \| Cap \| Dono \| Handoff (SQDL) \| SLA(h) \| Métrica-chave \| Métricas secundárias \| Bundle \| Automação (S/N) \| Observações. Inclua triggers de uso (login, views, spike Z2A, proposta), operacional (edição, correção), parcerias (Embaixadoras/Houses), marketing (CTR p90, LP topo), reengajamento (inativos, no-show) e governança (HOT vencendo SLA). **Sem fontes externas**.

### **Prompt --- KPI Bar (atualização textual)**

> Usando apenas dados deste chat como referência estrutural, gere um bloco "KPI Bar" com placeholders: **TTFV (mediana)** \| **Ativação 7/30** \| **DL→Pago 30/60** \| **HOTs abertos** \| **SLAs vencendo (24h)**. Formato em 1 linha, pronto para colar no topo do Google Docs.

### **Prompt --- Roteiro Setup Express (15--30')**

> Crie um roteiro de **Setup Express (15--30')** com: objetivo (1º valor), agenda (5' contexto, 10' card, 5' Z2A, 5' próximos passos), checklist (acessos, produto, arte/card, CTA), evidência de valor (alcance inicial) e follow em 24h. Somente com conteúdo deste chat (**sem fontes externas**).

**\# 3.3 Queries/filters (pseudo-SQL/pseudo-CRM)**
--------------------------------------------------

-   **Novos cadastros DL\
    > **cadastro\_date \>= today - 2 AND perfil = \'incorporadora\'

-   **Acesso recente\
    > **last\_login\_hours \<= 48 AND perfil = \'incorporadora\'

-   **Muitas visualizações** *(threshold por praça --- **(inferência)**)\
    > *views\_7d \>= X OR views\_24h\_delta \>= Y

-   **Spike Z2A** *(uso do "Zé")\
    > *z2a\_commands\_7d \>= X

-   **PRM sem follow\
    > **opp\_age\_days \> 5 AND next\_step IS NULL

-   **Pressão de corretores\
    > **broker\_requests\_14d \>= N

-   **Nova incorporadora (praça foco)\
    > **cidade IN (\'SP int\',\'POA\',\'RJ\',\'GYN\') AND cadastro\_date \>= today - 7

-   **Inativos / risco\
    > **last\_action\_days \>= 14

-   **Tickets resolvidos (CSAT alto)\
    > **csat \>= 4 AND status = \'resolvido\'

*(X, Y, N ajustados por praça; GDD define e revisa semanalmente --- **(inferência)**.)*

**\# 3.4 Campos mínimos no CRM (Bitrix) --- checklist**
-------------------------------------------------------

**Identificação:** Conta / CNPJ / Praça / Persona principal (Diretoria, MKT, GP).\
**Status & Prioridade:** Classe (HOT/WARM/COOL) \| **Score** \| **Praça foco (Y/N)** \| Último trigger \| SLA\_due.\
**Jornada & Qualificação:** **SQDL (Y/N)** \| Motivo (Uso/Engajamento/ROI) \| Aha atingido (Y/N).\
**Operação & Passos:** Dono atual \| Próximo passo \| Data do próximo passo \| Canal preferido \| Opt-out (Y/N).\
**Métricas de valor:** TTFV (data/hora) \| Ações 7/30 \| Propostas (qtd) \| PRM ativo (Y/N).\
**Handoffs:** SDR→CS (data) \| CS→AE (data) \| Observações da passagem.

**\# 3.5 Estrutura da planilha (uma aba)**
------------------------------------------

**Colunas padrão (já consolidadas neste chat):\
**Alavanca \| Categoria \| Origem da lista \| Filtro/Query \| Contexto (sinal) \| Objetivo primário \| Objetivo secundário \| Abordagem \| **Script ≤280** \| Canal prioritário \| Cadência inicial \| **Cap/conta** \| Dono \| **Handoff (SQDL)** \| **SLA (h)** \| **Métrica-chave** \| Métrica(s) secundária(s) \| **Bundle** \| **Automação (S/N)** \| Observações

**KPI Bar (linha 1 do Sheet):\
**TTFV (mediana) \| Ativação 7/30 \| DL→Pago 30/60 \| HOTs abertos \| SLAs vencendo (24h)

**\# 3.6 Pseudorroteiros (execução rápida)**
--------------------------------------------

### **Office Hour (30--45') --- por praça/tema**

-   **Objetivo:** impulsionar comparecimento e ativação 1:many.

-   **Agenda:**

    1.  5' --- Case local (Sócio-Local).

    2.  10' --- Card + Z2A (demonstração).

    3.  10' --- PRM (como não perder calor).

    4.  5' --- Próximo passo: "deixo 1 card pronto para cada participante".

-   **Follow:** enviar alcance inicial + convite para Setup Express individual.

### **Setup Express (15--30') --- 1:1**

-   **Objetivo:** 1º valor tangível (**TTFV baixo**).

-   **Agenda:** 5' contexto → 10' card → 5' Z2A → 5' próximos passos.

-   **Saída:** card publicado + 1 comando Z2A executado + PRM (se houver proposta).

-   **Follow 24h:** mini-relatório de alcance e próxima meta (Ativação 7d).

**\# 3.7 Governança (diário/semanal/mensal)**
---------------------------------------------

-   **Diário (15'):** HOTs novos, **SLAs a vencer (24h)**, handoffs pendentes, reatribuição.

-   **Semanal (30--45'):** aprendizados de copy, thresholds por praça (views X, Z2A X, CTR p90), impedimentos de dados.

-   **Mensal (60'):** **TTFV/Ativação/DL→Pago**, casos por praça, ajustes de bundles e cap/cooldown.

**\# 3.8 Glossário rápido (complementar)**
------------------------------------------

-   **Office hour (OH):** sessão online semanal 1:many para ativar e tirar dúvidas.

-   **Setup Express:** onboarding prático de 15--30' para publicar **1 card** e executar **1 Z2A**.

-   **Spike Z2A:** pico de comandos do "Zé" (ex.: z2a\_cmd\_7d\>=X).

-   **Card:** peça rastreável para medir alcance/interesse.

-   **PRM:** gestão de oportunidades com próximos passos e automações.

-   **LP (Listagem Patrocinada):** destaque pago --- acoplar PRM.

-   **SQDL:** DL pronto para venda (2 de 3: Uso, Engajamento, ROI).

-   **Cap / cooldown:** limites de contato (cap 2/semana/canal; cooldown 30 dias após silêncio).

**Mini pílula de inglês**
-------------------------

-   **"Call to action (CTA)"** = chamada para ação.

-   **"Proof of value"** = evidência de valor.

-   **"Next step"** = próximo passo (campo obrigatório no CRM).

Deseja que eu produza agora **Título + Introdução** (início do compilado)? Se quiser, também posso sugerir **Partes adicionais** (ex.: "Playbooks por Persona" e "Guia Bitrix") --- **(inferência)**.

Lives

Lives

**1) Live / Treinamento aberto para clientes pagantes (retenção + uso)**
------------------------------------------------------------------------

### **Nome**

**"Órulo DA na Prática --- Rotina de 30 dias (Parcerias + Marketing)"**

### **Promessa (bem direta)**

Em 60 minutos, o cliente sai com:

-   **rotina mínima viável** (o feijão com arroz do DA)

-   como transformar **audiência → lista → abordagem**

-   como provar **capilaridade** (vitrines/sistemas) e evitar "produto invisível"

-   como usar **comparação/concorrência** sem virar "relatório"

> Isso casa com a lógica de retenção via **conteúdos educativos e workshops**, que o documento recomenda como camada de máquina comercial/CS.

### **Formato (pra gravar e virar ativo)**

**45 min conteúdo + 15 min clínica/Q&A\
**E gravar para biblioteca (igual ao ritual de treinamento contínuo interno).

### **Pré-trabalho (para render de verdade)**

-   Escolher **1 empreendimento prioridade**

-   Separar **1 concorrente**

-   Trazer **2 sites de imobiliárias locais** (para checar presença)

-   (Opcional) 1 dúvida real ("não gerou venda", "já tenho CRM", etc.)

### **Agenda sugerida (slide-roteiro)**

1.  **Setup de vitrine (10 min)\
    > **checklist: materiais, tabela, contato (anúncio "pronto pra corretor agir")

2.  **Audiência → ação (15 min)\
    > **como montar lista Top 20 e o script "vi que você acessou..."

3.  **Capilaridade (10 min)\
    > **checagem ao vivo em site/vitrine + "onde meu produto aparece e onde não"

4.  **Comparação (10 min)\
    > **2 conclusões objetivas (onde ganha/perde atenção)

5.  **Clínica (15 min)\
    > **escolher 2--3 clientes "voluntários" e fazer mini-audit ao vivo

### **CTA (sem cara de upsell)**

"Se você fizer só isso por 30 dias, você usa **o núcleo do DA**. Se travar, marca uma clínica 1:1 com CS/Time."

**2) Live aberta para topo de funil (incorporadoras não pagantes)**
-------------------------------------------------------------------

Aqui é seu "pitch disfarçado" perfeito: **ensinar a vender mais com a Órulo mesmo no gratuito**, focando em "anúncio nota 10" + "link oficial" + "presença no caminho do corretor".\
E no fim você mostra: "pra potencializar, existe DA".

### **Nome**

**"Como vender mais com a Órulo (mesmo sem pagar): Anúncio Nota 10 + Link Oficial"**

### **Promessa**

Em 60 min, a incorporadora sai sabendo:

-   como o corretor realmente usa a Órulo (ferramenta, não portal)

-   como deixar o anúncio "irresistível" (conteúdo + tabela + contato + materiais)

-   como gerar **lembrança** e recorrência com o **link da Órulo**

-   como checar se está perdendo disputa por "ausência de vitrine"

> A lógica de entrada do corretor é: valor simples, rápido e sem atrito (vitória rápida). Isso aparece claramente na jornada de engajamento: descoberta → ativação com "vitória rápida" e lives/treinamentos como reforço.

### **Formato**

**45 min conteúdo + 15 min Q&A** (gravado e vira ativo de aquisição em escala).

### **Agenda sugerida (slide-roteiro)**

1.  **Como o corretor consulta e decide (10 min)\
    > **"o que ele precisa em 30 segundos" (materiais, preço, filtro, contato)

2.  **Checklist do anúncio nota 10 (15 min)\
    > **o que deixa o produto "compartilhável" via link da Órulo

3.  **Link da Órulo como fonte oficial (10 min)\
    > **como divulgar para corretores/imobiliárias e virar rotina

4.  **3 erros comuns no gratuito (5 min)\
    > **(anúncio incompleto, preço desatualizado, contato confuso)

5.  **Como potencializar (5 min)\
    > **"se você quiser ampliar vitrine/capilaridade e enxergar interesse, existe o DA" (sem aprofundar)

6.  **Q&A (15 min)**

### **CTA "soft"**

-   "Queremos auditar seu anúncio ao vivo no próximo encontro"

-   "Baixe o checklist do anúncio nota 10 + mande seu link"

*(Isso vira gatilho pra próxima live, e cria loop de aquisição sem parecer venda.)*

**3) Terceira sugestão (a que mais dá "autoridade" + prova social)**
--------------------------------------------------------------------

Você pediu "talvez uma terceira" --- eu recomendo uma que serve **pros dois mundos** (pagantes e não pagantes) e cria **prova social territorial**.

### **Nome**

**"Mesa Redonda: Como os Top Corretores escolhem o que vender (com Oráculo + Incorporadora)"**

**Por quê funciona:**

-   corretor tem credibilidade instantânea

-   incorpora prova social (buzz/autoridade)

-   vira conteúdo gravado em cortes (Reels/LinkedIn)

-   puxa incorporadora pro "mundo real" sem você vender

> O próprio material sugere lives com "oráculos" e treinamentos como construção de autoridade e utilidade, além de eventos/mini ações como prova social territorial.

### **Formato**

**60 min**

-   10 min: contexto (você)

-   35 min: bate-papo (corretor top + incorporadora case)

-   15 min: Q&A

### **Roteiro de perguntas (bem pé no chão)**

-   "O que te faz lembrar de um produto?"

-   "O que te faz desistir de divulgar um produto?"

-   "O que um anúncio precisa ter pra você compartilhar?"

-   "Onde você pesquisa antes de falar com o cliente?"

### **CTA natural**

-   Para não pagantes: "arrume seu anúncio (checklist) e volte na próxima"

-   Para pagantes: "como ativar capilaridade/audiência/rotina com DA"

**Como operar isso como "máquina" (sem improviso)**
---------------------------------------------------

-   **Cadência fixa** (mensal ou quinzenal): previsibilidade aumenta adesão

-   **Gravar tudo** e subir numa biblioteca (CS/SDR usam depois)

-   **Clipes curtos** (1--2 min) com: "erro comum + ajuste + prova"

-   "Mirror Strategy" (se quiser territorializar): tema nacional, exemplos locais

Se você topar, eu já escrevo **os slides instrutivos (Gama)** do **Treinamento Pagantes** e do **Treinamento Topo de Funil** (igual fiz no DA Rush), com:

-   agenda minuto a minuto

-   "o que mostrar na plataforma"

-   perguntas para puxar discussão

-   CTA final e follow-up (material + replay).

1\) Live / Treinamento aberto para DAs

According to a document from **18 Sep 2025**, a forma mais eficiente de transformar uma live em "máquina" na Órulo é: **padronizar o formato, usar ativos já validados (WhatsApp, cards, reels, disparos), gravar e virar biblioteca**, e tratar isso como **campanha de retenção** (não evento isolado).

Abaixo está um **briefing completo da Live 1** (clientes pagantes), já pronto para o Marketing divulgar e para quem for "tocar" a live executar sem improviso.

**Briefing completo --- Live 1 (Clientes Pagantes)**
====================================================

**Órulo DA na Prática: Rotina de 30 dias (Parcerias + Marketing)**
------------------------------------------------------------------

### **1) Por que essa live existe (contexto de negócio)**

-   **Problema real:** muita incorporadora paga DA e usa pouco (ou usa só uma entrega), o que aumenta ruído de valor e risco de churn.

-   **Oportunidade:** "ensino operacional" vira retenção, reduz custo de suporte e aumenta percepção de ROI --- exatamente a categoria "retenção com conteúdos educativos e workshops".

-   **Estratégia de ativo escalável:** gravar, editar em microconteúdos e criar uma biblioteca para CS/SDR reutilizarem (reduz custo marginal).

**2) Público-alvo (quem convidar e por quê)**
---------------------------------------------

**Primário (quem mais ganha valor):**

-   Coordenador/gerente de parcerias (rotina de abordagem e priorização)

-   Marketing (vitrine, materiais, posicionamento e "link oficial")

**Secundário (influencia e cobra execução):**

-   Dono/diretor comercial (quer previsibilidade e "presença")

-   CS (para replicar pós-live em onboarding/re-onboarding)

**Critério de lista (ideal):**

-   Clientes pagantes DA e DL (principalmente os que não "operam" toda semana)

-   Segmentos por praça também funcionam (versão "mirrored" local) se você quiser, mas não é obrigatório aqui.

**3) Promessa (a frase que o marketing vai vender)**
----------------------------------------------------

**"Em 60 minutos você sai com uma rotina simples de 30 dias para extrair o núcleo do DA: vitrine + capilaridade + audiência acionável + comparação de concorrência (sem relatório, sem enrolação)."**

**Entregáveis do participante (tangíveis):**

1.  Checklist "Anúncio/Produto pronto para corretor agir"

2.  Roteiro de "Top 20 corretores da semana" (audiência → lista → ação)

3.  Rotina de checagem de capilaridade (2 sites + 1 portal)

4.  2 conclusões objetivas de comparação/concorrência

5.  Plano de 30 dias (1 página)

**4) Formato e dinâmica (para a live ser boa ao vivo e boa gravada)**
---------------------------------------------------------------------

**Duração:** 60 min (45 conteúdo + 15 clínica/Q&A)\
**Princípio:** prova na plataforma \> explicação.\
**Modelo de execução:** conteúdo prático e padronizado, gravado e transformado em biblioteca.

**Interações (para manter audiência):**

-   2 enquetes rápidas no chat ("qual seu gargalo hoje?" / "qual entrega você mais subutiliza?")

-   1 bloco "clínica ao vivo": escolher 2 clientes voluntários e fazer mini-audit (5 min cada)

**5) Roteiro completo (minuto a minuto) --- conteúdo da live**
--------------------------------------------------------------

### **Bloco A --- Setup: "Produto pronto para corretor agir" (0:00--0:10)**

**Objetivo:** eliminar fricção e "anúncio feio / incompleto".

-   Checklist de vitrine:

    -   materiais (book, fotos, info completa)

    -   tabela/condições atualizadas

    -   contato e caminho claro

-   Mini-demonstração: "o que o corretor enxerga e por que ele compartilha"

**Output do participante:** checklist preenchido para 1 empreendimento.

### **Bloco B --- Audiência → Lista → Ação (0:10--0:25)**

**Objetivo:** transformar sinal em rotina de parcerias.

-   Passo a passo:

    1.  ver quem acessou / quem está quente

    2.  criar "Top 20 da semana"

    3.  abordagem com script curto ("vi que você acessou...")

-   Reforço: "DA dá munição para o coordenador --- não substitui pessoa"

**Output:** lista Top 20 + 1 script padrão.

### **Bloco C --- Capilaridade: prova em vitrines externas (0:25--0:35)**

**Objetivo:** parar de "achar" e começar a **provar presença**.

-   Ao vivo:

    -   abrir site de imobiliária (integrada) e buscar tipologia/região

    -   checar presença do produto (e de concorrente)

-   Checklist capilaridade (simples):

    -   2 sites de imobiliárias

    -   1 portal (Zap/VivaReal/ImovelWeb --- o que fizer sentido na praça)

**Output:** "3 vitrines checadas" + correção de gap.

### **Bloco D --- Comparação/Concorrência: 2 conclusões (0:35--0:45)**

**Objetivo:** tirar valor sem virar BI.

-   Ao vivo:

    -   abrir comparação/concorrência

    -   responder duas perguntas:

        1.  onde estou perdendo atenção?

        2.  qual ajuste simples aumenta minha chance (material, preço, tipologia, foco)?

**Output:** 2 insights objetivos + 1 ação.

### **Bloco E --- Clínica + Q&A guiado (0:45--1:00)**

**Formato:**

-   10 min clínica (2 auditorias rápidas)

-   5 min Q&A aberto

**Perguntas guiadas (boas pra manter nível alto):**

-   "Qual parte do DA você paga e não usa?"

-   "Qual vitrine você quer checar agora?"

-   "Qual rotina cabe no seu time (30 min/semana)?"

**6) "O que mostrar na plataforma" (runbook para o apresentador)**
------------------------------------------------------------------

**Checklist do operador (antes de entrar ao vivo):**

-   Separar 1 empreendimento exemplo (com materiais bons) e 1 com "gap" (para ensinar)

-   Separar 1 concorrente

-   Separar 1 site de imobiliária para prova de capilaridade

-   Deixar 3 abas prontas: Produto \| Audiência/Interesse \| Comparação

**Regra do apresentador:** escolher **1 prova por minuto**, sem navegar demais.

**7) Divulgação (Marketing) --- plano completo**
------------------------------------------------

O documento recomenda tratar isso como **campanha de retenção** (conteúdo educativo + workshop), usando ativos já validados (WhatsApp, cards, reels, disparos).

### **Segmentação e mensagem (3 criativos, 3 dores)**

1.  **"Uso mínimo viável do DA"** (para quem não usa)

2.  **"Top 20 corretores por semana"** (para parcerias)

3.  **"Capilaridade: seu produto está aparecendo?"** (para marketing/diretoria)

### **Canais recomendados (com o jeito Órulo)**

-   **WhatsApp** (comunidade + lista de transmissão) --- canal direto e rápido

-   **Cards rastreáveis** (convite com CTA + link) --- atribuição e conversão

-   **Reels / vídeos curtos** (30--60s) com "1 erro + 1 ajuste"

-   **E-mail** (convite + lembrete + replay) --- principalmente para stakeholders corporativos

### **Peças que o Marketing precisa produzir (kit completo)**

-   1 landing page simples (título + promessa + agenda + botão)

-   2 cards (WhatsApp):

    -   convite (D-7)

    -   "é amanhã" (D-1)

-   1 reels teaser (D-3): "3 coisas que você vai ajustar em 30 dias"

-   1 arte "entregáveis" (o que a pessoa leva)

-   1 slide/arte "certificado" opcional ("DA Sprint --- concluído") pra aumentar comparecimento

### **Timeline sugerida (curta e eficiente)**

-   **D-7:** convite + LP

-   **D-3:** reels teaser + disparo segmentado

-   **D-1:** lembrete WhatsApp + e-mail

-   **D0:** lembrete 2h antes (WhatsApp)

-   **D+1:** replay + checklist + CTA de clínica

**8) Pós-live (onde o dinheiro mora)**
--------------------------------------

A estratégia recomendada é capturar a sabedoria e transformar em conteúdo gravado e escalável.

### **Entregas pós-live (1 e-mail/WhatsApp)**

-   Replay

-   PDF 1 página: "Rotina DA em 30 dias"

-   Checklist: "Produto pronto para corretor agir"

-   CTA: "clínica 1:1 de 20 min" (agenda com CS) para quem quiser audit do próprio caso

### **Conteúdo reciclável (para virar máquina)**

-   cortar 6 clipes (45--90s):

    1.  checklist de vitrine

    2.  Top 20 corretores

    3.  script de abordagem

    4.  prova capilaridade

    5.  2 conclusões de comparação

    6.  "rotina de 30 min por semana"

-   subir na biblioteca (YouTube/unlisted ou hub interno), como ativo para CS/SDR.

**9) Métricas (para marketing + comercial + CS ficarem alinhados)**
-------------------------------------------------------------------

**Métricas de funil da live**

-   inscritos

-   taxa de presença (show rate)

-   retenção média (minutos assistidos)

-   perguntas feitas / engajamento no chat

**Métricas de impacto (30 dias)**

-   \% clientes que executaram "Top 20 semanal" (autodeclaração via formulário simples)

-   nº de clientes que pediram clínica 1:1

-   redução de tickets "básicos" (se CS medir)

-   sinal de risco reduzido (clientes com baixa atividade passam a ter rotina)

**Para fechar: "o que vai no briefing do marketing" (copiar e colar)**
======================================================================

-   Nome, promessa, público, agenda minuto a minuto

-   Kit de peças + timeline de disparos

-   Runbook do apresentador (o que abrir na plataforma)

-   Pós-live (replay + materiais + CTA)

-   Métricas

Se você quiser, eu já transformo esse briefing em:

1.  **script do host (fala por minuto)** + "frases-âncora" no seu tom;

2.  **copy pronta** (WhatsApp + e-mail + LP) --- sem inventar, já alinhado a "retenção com workshop" e aos ativos validados (cards/reels/disparos).

Live 2 (Topo de Funil \| Não pagantes)

**Briefing completo --- Live 2 (Topo de Funil \| Não pagantes)**
================================================================

**Como vender mais com a Órulo (mesmo sem pagar): Anúncio Nota 10 + Link Oficial**
----------------------------------------------------------------------------------

**1) Por que essa live existe (contexto de negócio)**
-----------------------------------------------------

**Dor real do mercado (não pagantes):**

-   a incorporadora está na Órulo (ou poderia estar) mas o "anúncio" / presença está fraco: incompleto, difícil de consultar, pouco compartilhável.

-   ela quer mais procura de corretores, mas não organiza o básico do que o corretor precisa (tabela/material/contato).

-   muitas vezes compara Órulo com "portal"; não entende o lugar da Órulo na rotina do corretor.

**Oportunidade Órulo:**

-   ensinar o **básico que já dá resultado sem pagar** aumenta:

    -   volume e qualidade da presença (conteúdo melhor),

    -   percepção de valor (entende como o corretor usa),

    -   e abre a ponte natural: "se você quiser ampliar vitrine/capilaridade e enxergar interesse, existe DA".

**Estratégia de aquisição + educação:**

-   live aberta gera lead qualificado (intenção real)

-   grava e vira ativo "evergreen" (SDR/Inbound/CS usam depois).

**2) Público-alvo (quem convidar)**
-----------------------------------

**Primário (melhor fit):**

-   incorporadoras **não pagantes** (ou DL) com lançamentos em curso / próximos 90 dias

-   perfis: coordenador comercial, parcerias, marketing, produto/gestão de lançamentos

**Secundário:**

-   incorporadoras pequenas/médias com estrutura comercial enxuta

-   imobiliárias "braços de venda" (podem participar como influência)

**Como segmentar listas (marketing)**

-   Segmento A: incorporadora já cadastrada na Órulo mas não paga (lista quente)

-   Segmento B: incorporadora que ainda não usa (lista fria/inbound)

-   Segmento C: marketing/comercial (personas diferentes → criativos diferentes)

**3) Promessa (frase que o marketing divulga)**
-----------------------------------------------

**"Em 60 minutos você vai aprender a deixar seu anúncio na Órulo 'nota 10' e transformar o link da Órulo na sua fonte oficial para corretores --- para aumentar consulta, compartilhamento e presença do seu produto, mesmo sem pagar."**

**Entregáveis do participante (tangíveis)**

1.  Checklist "Anúncio Nota 10" (o que precisa ter para o corretor agir)

2.  Template de mensagem "Link oficial da Órulo" (para corretores/imobiliárias)

3.  Mini-roteiro de auditoria: "como checar se você está perdendo vitrine"

4.  "Próximo passo opcional": como potencializar com DA (sem pressão)

**4) Posicionamento e "pitch disfarçado" (interno, para orientar o time)**
--------------------------------------------------------------------------

**O que a live *é* publicamente:** educação prática para vender mais "no gratuito".\
**O que ela *faz* na operação:** move a incorporadora para um estado de:

-   anúncio melhor (mais compartilhável)

-   link oficial circulando (mais audiência orgânica)

-   percepção clara de que existe um "próximo degrau": DA.

**Regra de ouro:**

> DA aparece como "camada de potência", só no final, em 3--5 min, com 1 slide.

**5) Formato (para ser boa ao vivo e boa gravada)**
---------------------------------------------------

-   **45 min conteúdo + 15 min Q&A**

-   2 momentos de interação (chat/enquete)

-   1 mini-audit opcional ao vivo (se quiser, mas cuidado para não virar "suporte individual")

E gravar para virar ativo e cortes, como recomendado.

**6) Roteiro completo (minuto a minuto)**
=========================================

### **Bloco A --- "Como o corretor usa" (0:00--0:10)**

**Objetivo:** tirar o frame de "portal" e botar o frame correto: "ferramenta de trabalho".

-   O que o corretor quer em 30 segundos:

    -   tabela/condições

    -   materiais (book, fotos, vídeo)

    -   filtros (pra achar rápido)

    -   contato (pra agir)

-   Mostre rapidamente (demo leve) o "caminho de consulta".

**Interação \#1 (chat):\
**"Hoje, o corretor consulta seu produto onde primeiro?"

### **Bloco B --- Checklist "Anúncio Nota 10" (0:10--0:30)**

**Objetivo:** ensinar o básico que dá resultado sem pagar.\
Checklist prático:

1.  **Título e identidade** do produto claros (sem confusão)

2.  **Materiais completos** (book, imagens boas, diferenciais)

3.  **Tabela/condições** atualizadas e coerentes

4.  **Tipologia, metragem, status** (sem ruído)

5.  **Contato e CTA** (quem fala com a incorporadora e como)

6.  **Compartilhável**: um link único que o corretor consegue mandar

**Demonstração sugerida:**

-   mostrar 1 exemplo "bom" e 1 "ruim" (comum) e explicar "por que o corretor não compartilha".

**Entrega:** disponibilizar o checklist para download/WhatsApp.

### **Bloco C --- "Link oficial da Órulo" (0:30--0:40)**

**Objetivo:** ensinar a ação de distribuição orgânica que funciona mesmo no gratuito.

-   como usar o **link da Órulo** como "fonte oficial" para:

    -   corretores

    -   imobiliárias parceiras

    -   até em materiais e assinatura

-   mensagem pronta (template) + boas práticas:

    -   curto, direto, com CTA

    -   "tabela + book + contato num lugar só"

**Interação \#2 (enquete):\
**"Você já manda um link único oficial para corretores? (sim/não)"

### **Bloco D --- "3 erros comuns que derrubam resultado" (0:40--0:45)**

1.  anúncio incompleto → corretor não confia / não compartilha

2.  preço/material desatualizado → ruído e frustração

3.  contato confuso → o corretor desiste

### **Bloco E --- "Como potencializar (DA) sem virar pitch" (0:45--0:50)**

**Mensagem curta e limpa:**

-   No gratuito, você já melhora muito com:

    -   anúncio nota 10 + link oficial

-   Se quiser **potencializar**, DA adiciona:

    -   mais vitrine (mais presença)

    -   capilaridade via integração (mais caminhos)

    -   sinais de interesse/audiência (mais ação)

    -   leitura de concorrência (mais clareza)

**Regra:** 1 slide, 3--5 min, sem entrar em detalhes.

### **Bloco F --- Q&A (0:50--1:05)**

Perguntas guiadas (boa qualidade):

-   "Qual parte do checklist você mais subestima hoje?"

-   "Qual material falta para o corretor agir rápido?"

-   "Qual é seu produto prioridade do mês? Vamos auditar ao vivo em 2 min?"

-   "O que faz o corretor não compartilhar um produto seu hoje?"

**7) Runbook (para quem vai tocar a live)**
-------------------------------------------

**Antes da live (15 min)**

-   Separar 2 exemplos:

    -   1 produto "nota 10"

    -   1 produto "nota 4" (com gaps comuns)

-   Ter 1 template de mensagem do link oficial

-   Ter 1 slide final "como potencializar com DA"

-   Cronômetro na tela / roteiro em bullet

**Durante a live**

-   evitar navegação longa

-   manter regra: **mostrar → explicar em 20s → avançar**

**8) Divulgação (Marketing + Digital) --- plano completo**
==========================================================

**Mensagens principais (3 criativos)**
--------------------------------------

1.  **Anúncio Nota 10** (para marketing/lançamento)

2.  **Link oficial da Órulo** (para parcerias/comercial)

3.  **Como o corretor usa** (para diretores e quem acha que é "portal")

**Canais recomendados (mix Órulo)**
-----------------------------------

-   WhatsApp (listas, parceiros, comunidades) e cards com CTA

-   Reels/shorts teaser (30--60s) com "erro comum + ajuste"

-   E-mail (convite + lembrete + replay)

-   LinkedIn (post do Diretor Comercial + corte de 45s)

-   Tráfego pago leve (opcional): remarketing para quem visitou LP/baixou checklist

**Peças para o kit de divulgação**
----------------------------------

-   Landing page simples (título + promessa + agenda + botão + checklist)

-   2 cards WhatsApp:

    -   D-7 "Convite"

    -   D-1 "Amanhã + checklist"

-   1 reels teaser: "3 coisas que travam seu anúncio"

-   1 arte "Checklist Anúncio Nota 10" (isca)

-   1 e-mail "Replay + checklist + auditoria"

**Timeline sugerida**
---------------------

-   D-7: LP + convite (WhatsApp/e-mail/LinkedIn)

-   D-3: teaser (reels + remarketing leve)

-   D-1: lembrete + envio do checklist (pré)

-   D0: lembrete 2h antes

-   D+1: replay + CTA auditoria

**9) CTA e Follow-up (para gerar pipeline sem forçar venda)**
-------------------------------------------------------------

**CTA principal (educacional):**

-   "Baixe o checklist e envie o link do seu anúncio para auditoria."

**CTA secundário (vendas, soft):**

-   "Quer potencializar vitrine e distribuição? Agende uma conversa de 20 min para entender se DA faz sentido."

**Follow-up recomendado (simples e eficaz):**

-   Formulário pós-live com 3 perguntas:

    1.  "Você já aplica o checklist hoje?" (sim/não)

    2.  "Qual seu empreendimento prioridade?"

    3.  "Você quer auditoria do anúncio?" (sim/não)

Daqui sai:

-   trilha de nutrição (quem quer auditoria)

-   e triagem para SDR (quem pediu conversa)

**10) Métricas (marketing + vendas alinhados)**
-----------------------------------------------

**Topo de funil**

-   inscritos

-   show rate (presença)

-   retenção média (minutos assistidos)

-   downloads do checklist

-   envios de link para auditoria

**Meio de funil**

-   nº auditorias feitas

-   nº reuniões agendadas (soft)

-   conversão para DL/DA (se houver)

**Qualidade**

-   perguntas no chat

-   \% participantes por persona (marketing/parcerias/diretoria)

**11) Como transformar em máquina (pós-gravação)**
--------------------------------------------------

-   cortar 6 clipes:

    1.  "o que o corretor precisa em 30s"

    2.  "checklist nota 10"

    3.  "template link oficial"

    4.  "3 erros comuns"

    5.  "mini-audit de exemplo"

    6.  "como potencializar (DA) em 60s"

-   subir em biblioteca e usar em cadência de inbound/outbound.

Se você quiser, eu já entrego também:

1.  **Copy pronta** (WhatsApp + e-mail + LinkedIn) com 3 versões por persona;

2.  **Checklist "Anúncio Nota 10"** em formato 1 página para anexar no pós-live;

3.  **Slides Gama** dessa live (instrutivos + demo cues).
