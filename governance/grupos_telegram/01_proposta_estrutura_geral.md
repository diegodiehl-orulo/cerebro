# PROPOSTA — Estrutura de Grupos no Telegram

> **Data:** 06/03/2026  
> **Versão:** 1.0  
> **Status:** Pendente de validação  
> **Objetivo:** Organizar conversas por agent e tema para otimizar comunicação e automações

---

## 🎯 Contexto

Hoje existem múltiplos agents e canais de comunicação. A proposta é criar uma estrutura clara para separar:
- O que é discutido com cada agent
- O que é executado automaticamente
- O que precisa de validação humana

---

## 📋 Estrutura Proposta

### 1. Morfeu — Diego (Direct)

**Propósito:** Contexto profundo, decisões estratégicas, rascunhos

| O que faz | O que NÃO faz |
|-----------|---------------|
| Conversas estratégicas | Envio automático de emails |
| Análise de reuniões | Crons de rotina |
| Rascunhos de documentos | Follow-ups operacionais |
| Propostas de ações | Execução de tarefas |

**Quando usar:**
- Decisões que exigem reflexão
- Análise de dados ou reuniões
- Criação de documentos
- Discussões estratégicas

---

### 2. Larissa — Diego (Direct)

**Propósito:** Secretaria executiva, follow-ups, envio de mensagens

| O que faz | O que NÃO faz |
|-----------|---------------|
| Enviar e-mails (com aprovação) | Decisões estratégicas |
| Follow-ups operacionais | Análise profunda |
| Lembretes de compromissos | Criação de documentos |
| Coordenação de agenda | Crons |

**Quando usar:**
- Pedir para enviar email
- Follow-up de tarefas
- Coordenação de reuniões
- Lembretes

---

### 3. Claudinei — Rotinas (Grupo/Canal)

**Propósito:** Crons, automações, alertas de sistema

| O que faz | O que NÃO faz |
|-----------|---------------|
| Daily briefings | Decisões estratégicas |
| Alertas de contratos | Conversas diretas |
| Monitoramento de reuniões | Execução manual |
| Check-ins de sprint | Respostas complexas |

**Quando usar:**
- Não interage diretamente (apenas recebe alertas)
- Executa as rotinas automaticamente

---

### 4. Órulo — Diretoria (Grupo)

**Propósito:** Discussões operacionais do negócio

| O que faz | O que NÃO faz |
|-----------|---------------|
| Coordenação do time | Decisões pessoais |
| Operações comerciais | Assuntos de saúde |
| Aprovações rápidas | Rotinas de automação |

---

### 5. Pessoal (Grupo ou Direct)

**Propósito:** Assuntos pessoais

| O que faz | O que NÃO faz |
|-----------|---------------|
| Rotinas de saúde | Discussões de trabalho |
| Agenda pessoal | Decisões estratégicas |
| Lembretes pessoais | Operações comerciais |

---

## 🔄 Fluxo de Trabalho Proposto

```
Diego quer discutir algo estratégico
         ↓
Morfeu (análise + rascunho)
         ↓
Diego aprova
         ↓
Larissa (executa/envia)
         ↓
Claudinei (registra em pendências/segue)
```

---

## 📝 Checklist de Implementação

- [ ] Validar estrutura com Diego
- [ ] Definir quais grupos criar
- [ ] Criar grupos no Telegram
- [ ] Configurar permissões
- [ ] Migrar conversas existentes
- [ ] Documentar regras de uso
- [ ] Treinar time (se aplicável)

---

## ❓ Perguntas para Definir

1. Quais grupos são necessários?
2. Quem tem acesso a cada grupo?
3. Quais agents devem participar de quais grupos?
4. Como lidar com mensagens que chegam no grupo errado?
5. Qual é o fluxo de escalação?
6. Quais grupos devem ter notificação silenciada?

---

## 📊 Resumo por Agent

| Agent | Função Principal | Canal | Tipo |
|-------|-------------------|-------|------|
| Morfeu | Estratégia e contexto | Direct | Agent principal |
| Larissa | Secretaria e execução | Direct | Secretária |
| Claudinei | Crons e automações | Grupo/Canal | Sistema |
| Órulo | Operações | Grupo | Time |
| Pessoal | Vida pessoal | Direct/Grupo | Pessoal |

---

*Documento criado em 06/03/2026 para discussão em 07/03/2026*
