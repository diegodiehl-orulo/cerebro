# PROPOSTA — Estrutura de Grupos no Telegram

> **Data:** 06/03/2026
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
- Não interacts diretamente (apenas recebe alertas)
- Ejecuta as rotinas automaticamente

---

### 4. Grupos Temáticos (opcional)

#### Órulo — Diretoria
- Time comercial
- Decisões operacionais do negócio
- Coordenação de praças

#### Pessoal
- Assuntos pessoais
- Rotinas de saúde
- Agenda pessoal

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

## 📝 Próximos Passos

- [ ] Validar estrutura com Diego
- [ ] Definir quais grupos criar
- [ ] Configurar permissões
- [ ] Migrar conversas existentes
- [ ] Documentar regras de uso

---

## ❓ Perguntas para Definir

1. Quais grupos são necessários?
2. Quem tem acesso a cada grupo?
3. Quais agents devem participar de quais grupos?
4. Como lidar com mensagens que chegam no grupo errado?
5. Qual é o fluxo de escalation?

---

*Documento criado para discussão em 07/03/2026*
