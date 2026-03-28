# SCANNER DE SAÚDE DOS WORKSTREAMS — ÓRULO

## Objetivo

O scanner de saúde dos workstreams existe para verificar, de forma simples e recorrente, se os workstreams da Órulo estão sendo atualizados e operados com cadência mínima.

O scanner não cria estratégia.

O scanner não substitui o trabalho dos DRIs.

O scanner apenas verifica saúde operacional.

---

## Fonte principal de leitura

A principal fonte de leitura do scanner é a planilha:

WS_OPERATING_SYSTEM_H1_2026

Abas principais:

- PORTFOLIO
- STATUS_QUINZENAL
- DECISOES
- EVIDENCIAS
- PLANO_DE_ACAO
- RITUAIS
- DRIS_E_RESPONSAVEIS

---

## O que o scanner deve verificar por workstream

Para cada workstream, verificar:

1. existe linha no PORTFOLIO?
2. existe DRI definido?
3. existe atualização recente no STATUS_QUINZENAL?
4. existe decisão recente registrada?
5. existe evidência recente registrada?
6. existe ação em aberto no PLANO_DE_ACAO?
7. existe ritual futuro definido?
8. existe algum gap claro de atualização?

---

## Classificação de saúde

### VERDE

O workstream está saudável quando:

- tem atualização recente
- tem decisão recente
- tem evidência recente
- tem ação clara
- tem ritual definido

### AMARELO

O workstream está em atenção quando:

- falta 1 ou 2 elementos
- ou a atualização parece superficial

### VERMELHO

O workstream está em risco quando:

- faltam 3 ou mais elementos
- ou não há atualização relevante
- ou o workstream parece parado

---

## Saída esperada

O scanner deve gerar um relatório contendo:

### 1. Visão geral

- quantidade de workstreams em verde
- quantidade em amarelo
- quantidade em vermelho

### 2. Tabela por workstream

- WS
- DRI
- saúde
- última atualização
- última decisão
- última evidência
- próximo ritual
- principal gap

### 3. Resumo executivo

- principais riscos
- workstreams mais saudáveis
- workstreams mais frágeis
- próximo passo recomendado

---

## Regra de simplicidade

O scanner deve ser simples. Ele não deve:

- reescrever os documentos dos workstreams
- criar novos documentos no Drive
- inferir estratégia
- produzir texto excessivamente longo

---

## Regra operacional

Na dúvida, o scanner deve preferir apontar:

- ausência de atualização
- ausência de decisão
- ausência de evidência
- ausência de ritual

em vez de tentar interpretar profundamente o conteúdo.
