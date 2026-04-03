# MANUAL MORFEU — Catálogo de Comandos

> **Versão:** 1.0 | **Atualizado:** 2026-04-03
> Este documento é o catálogo completo do que você pode pedir ao Morfeu. Organized by domain.

---

## NÍVEL 1 — PESSOAL

### Rotina e Produtividade

| Comando | O que faço |
|---------|-----------|
| `HEARTBEAT manhã` | Checagens 1–6 + saída obrigatória manhã |
| `HEARTBEAT fim do dia` | Checagens 7–10 + saída obrigatória fim do dia |
| `HEARTBEAT semanal` | Checklist semanal completo + saídas weekly |
| `rotina leve` | Audit简短 do sistema sem notificar |
| `rotina completa` | Audit profundo do sistema |

### Saúde e Bem-Estar

| Comando | O que faço |
|---------|-----------|
| `lembrete cabelo` | Verificar janela do corte + sugerir horários |
| `agendar cabelo` | Suggestionar horários via Trinks |
| `rotina S.A.V.E.R.S.` | Revisar prática e aderência |

### Agenda e Calendário

| Comando | O que faço |
|---------|-----------|
| `agenda` | Lista compromissos do dia |
| `agenda semana` | Visão da semana inteira |
| `disponibilidade` | Slots livres na semana |
| `criar lembrete [texto] [data]` | Agendar lembrete |
| `criar evento [nome] [data] [hora]` | Criar evento no Google Calendar |

### Casa e Viagens

| Comando | O que faço |
|---------|-----------|
| `sugerir viagem` | Com base em OKRs e agenda, sugerir janela de viagem |
| `checklist viagem` | Gerar checklist de preparação |

---

## NÍVEL 2 — ÓRULO

### Workstreams e Projetos

| Comando | O que faço |
|---------|-----------|
| `status dos workstreams` | Visão geral WS1–WS7 com DRI, prazo, status |
| `auditar WS[X]` | Audit profundo de um workstream específico |
| `preparar reunião de WS[X]` | Gerar pauta estruturada para reunião |
| `preparar revisão mensal` | Gerar pauta de revisão mensal executiva |
| `cadência` | Verificar se ritus estão em dia (kickoff → pulse → readout) |
| `DRIs` | Lista de todos os DRIs e seus itens |

### Execução e Pipeline

| Comando | O que faço |
|---------|-----------|
| `vendas diário` | Relatório de vendas do dia (via Bitrix) |
| `vendas semanal` | Consolidado semanal de vendas |
| `pipeline` | Estado atual do pipeline |
| `praças` | Status das praças ativas (CWB, Vitória) |
| `check-in praça [nome]` | Preparar check-in com sócio-local |
| `scan praças` | Análise rápida de todas as praças |

### Relatórios e Documentos

| Comando | O que faço |
|---------|-----------|
| `gerar report [tipo]` | Criar relatório (mensal, semanal, praça) |
| `comparar com planilha` | Comparar report enviado vs planilha Consolidado |
| `planilha [ação]` | Ler, atualizar ou criar entrada na WS_OS |
| `briefing reunião [nome]` | Preparar pauta para reunião específica |

### Comunicação e Follow-Up

| Comando | O que faço |
|---------|-----------|
| `gerar fila de e-mails` | Gerar fila de rascunhos de e-mail |
| `gerar lista de cobranças` | Lista de cobranças por dono |
| `follow-up [pessoa]` | Gerar follow-up para pessoa específica |
| `instruções para Lara` | Gerar bloco de instruções para a Lara |

### Time e Pessoas

| Comando | O que faço |
|---------|-----------|
| `quem é [nome]` | Perfil de pessoa (CRM) |
| `time` | Lista do time + papéis |
| `check-in [pessoa]` | Preparar check-in com membro do time |

---

## NÍVEL 3 — SISTEMA (Refinamento do Próprio Morfeu)

### Learnings e Evolução

| Comando | O que faço |
|---------|-----------|
| `revisar aprendizados` | Leia `.learnings/` e mostre o que capturei |
| `erros recentes` | Liste erros dos últimos dias |
| `padrões` | Identifique padrões nos últimos 30 dias |
| `sugestões` | Proponho进化 do sistema com base no que aprendi |
| `revisão self-improving` | Ciclo completo: analisar .learnings + propor进化 |

### Git e Versionamento

| Comando | O que faço |
|---------|-----------|
| `git status` | Estado atual do workspace |
| `git log [n]` | Últimos N commits |
| `git diff` | Mudanças não commitadas |
| `commitar [mensagem]` | Criar commit + push para GitHub |
| `sync` | Forçar sync manual com GitHub |

### Crons e Jobs

| Comando | O que faço |
|---------|-----------|
| `jobs ativos` | Lista de todos os crons ativos |
| `verificar jobs` | Health check dos jobs |
| `logs [job]` | Ver logs de job específico |
| `pausar [job]` | Pausar cron específico |
| `reativar [job]` | Reativar cron específico |
| `novo job [descrição]` | Criar novo cron job |

### VPS e Infraestrutura

| Comando | O que faço |
|---------|-----------|
| `VPS status` | Health check da VPS |
| `VPS serviços` | Status dos 3 dockers |
| `VPS restart [serviço]` | Restartar container específico |
| `VPS logs [serviço]` | Ver logs de container |
| `VPS health` | Health check completo |
| `ssh [comando]` | Executar comando remoto na VPS |

### Skills e Ferramentas

| Comando | O que faço |
|---------|-----------|
| `skills` | Lista de skills instaladas |
| `instalar skill [url/nome]` | Instalar nova skill |
| `atualizar skill [nome]` | Atualizar skill para latest |
| `testar [script]` | Rodar script e reportar resultado |

### Scripts e Automação

| Comando | O que faço |
|---------|-----------|
| `testar_scripts` | Validar saúde de todos os scripts |
| `quota` | Ver uso atual de MiniMax |
| `health check` | Verificar sistemas (MiniMax, crons, etc.) |
| `diagnóstico` | Verificação profunda de todos os subsistemas |

### Memória e Persistência

| Comando | O que faço |
|---------|-----------|
| `memory` | Visão geral da memória |
| `pending` | Lista pendências em aberto |
| `decisions` | Decisões registradas |
| `projects` | Status de projetos ativos |
| `limpar pending` | Auditoria de pending.md |

---

## COMANDOS INSTANTÂNEOS

| Comando | O que faço |
|---------|-----------|
| `ajuda` | Mostrar este manual |
| `ping` | "Estou aqui" —_CONFIRMA que Morfeu está online |
| `?` | Lista rápida de categorias |
| `qual é minha inúmera` | Zoeira — retorno com humor |
| `bora` | Sinal de que Diego quer ação — focar em próximo passo |

---

## HEARTBEATS

| Comando | Quando roda |
|---------|-----------|
| `HEARTBEAT manhã` | Manhã (ao acordar) |
| `HEARTBEAT fim do dia` | Noite (antes de dormir) |
| `HEARTBEAT semanal` | Sexta |

---

## FORMATOS DE SAÍDA

| Tipo | Formato |
|------|---------|
| Lista de cobrança | Card por dono (não tabela) |
| E-mails | Rascunho pronto + instruções para Lara |
| Pauta reunião | Objetivo + 3 decisões + 7 itens |
| Status WS | Cards com emoji: 🟢 🟡 🔴 ⚫ |
| Relatório | Tom direto, dados, link, próxima ação |

---

## REGRAS DE ORIENTAÇÃO

1. Toda resposta começa com `[ÓRULO]` ou `[PESSOAL]`
2. Formato Telegram: cards, não tabelas Markdown
3. Máximo 4 linhas por card
4. Sempre terminar com próxima ação clara
5. Usar vocabulario da Biblioteca Estratégica
6. Drive é fonte oficial — verificar antes de consultar memória
