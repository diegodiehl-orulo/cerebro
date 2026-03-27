# jobs/cron_plan.md — Plano de Jobs: Governança de Praças
*Versão: 1.0 | Criado: 2026-03 | Morfeu*

> **Regra global de segurança:** Nenhum job envia e-mail automaticamente.
> Todo job que gera comunicação externa → produz "INSTRUÇÕES PARA LARA" + pede aprovação de Diego.

---

## VISÃO GERAL

| Job | Frequência | Gatilho | Saída | Arquivo de prompt |
|-----|-----------|---------|-------|-------------------|
| `sprint-reminder` | Semanal/quinzenal | D-2 antes da reunião | Lembrete ao sócio local + pedido de One-Pager | `jobs/prompts/sprint_reminder.txt` |
| `sprint-checkpoint` | Meio do sprint | Data definida no contrato | Cobrança assíncrona do checkpoint | `jobs/prompts/sprint_checkpoint.txt` |
| `sprint-facilitator` | Pós-reunião (manual) | Diego cola o One-Pager | Diagnóstico + Contrato + E-mails + Instrução Lara | `jobs/prompts/sprint_facilitator.txt` |
| `sprint-followup-tracker` | D+3 após sprint fechado | Automático | Verificar follow-ups abertos; alertar Diego | `jobs/prompts/sprint_followup_tracker.txt` |
| `praças-weekly-scan` | Segunda-feira 08:30 | Automático | Escaneamento semanal de praças sem sprint fechado | `jobs/prompts/praças_weekly_scan.txt` |

---

## DETALHAMENTO DOS JOBS

---

### JOB 1: `sprint-reminder`

| Campo | Valor |
|-------|-------|
| **Nome** | Sprint Reminder — Praças |
| **Frequência** | Configurar manualmente por praça (quinzenal recomendado) |
| **Gatilho** | D-2 antes da data da reunião de sprint |
| **Entradas** | Nome da praça, nome do sócio local, data da reunião |
| **Saídas** | Rascunho de e-mail para o sócio local + INSTRUÇÕES PARA LARA |
| **Segurança** | ❌ Não envia. Gera rascunho + pede aprovação. |
| **Prompt** | `jobs/prompts/sprint_reminder.txt` |

**Configuração OpenClaw (quando ativar):**
```yaml
name: sprint-reminder-curitiba
schedule:
  kind: cron
  expr: "0 8 * * MON"   # ajustar para D-2 da reunião
  tz: America/Sao_Paulo
payload:
  kind: agentTurn
  message: |
    [Ver jobs/prompts/sprint_reminder.txt]
    PRAÇA: Curitiba | SÓCIO: Zanella | DATA REUNIÃO: [PREENCHER]
sessionTarget: isolated
delivery:
  mode: announce
```

---

### JOB 2: `sprint-checkpoint`

| Campo | Valor |
|-------|-------|
| **Nome** | Sprint Checkpoint Assíncrono |
| **Frequência** | Uma vez por sprint (data definida no contrato) |
| **Gatilho** | Data de checkpoint combinada na ata |
| **Entradas** | Praça, sócio local, C1/C2/C3 do sprint |
| **Saídas** | Rascunho de e-mail de cobrança + INSTRUÇÕES PARA LARA |
| **Segurança** | ❌ Não envia. Gera rascunho + pede aprovação. |
| **Prompt** | `jobs/prompts/sprint_checkpoint.txt` |

**Configuração OpenClaw (quando ativar):**
```yaml
name: sprint-checkpoint-vitoria
schedule:
  kind: at
  at: "[ISO timestamp do checkpoint]"
payload:
  kind: agentTurn
  message: |
    [Ver jobs/prompts/sprint_checkpoint.txt]
    PRAÇA: Vitória | SÓCIO: Pedro Kneip | C1: [PREENCHER] | C2: [PREENCHER] | C3: [PREENCHER]
sessionTarget: isolated
delivery:
  mode: announce
```

---

### JOB 3: `sprint-facilitator`

| Campo | Valor |
|-------|-------|
| **Nome** | Sprint Facilitator (ritual completo) |
| **Frequência** | Manual (acionado por Diego após receber One-Pager) |
| **Gatilho** | Diego cola o One-Pager preenchido |
| **Entradas** | One-Pager do sócio local (qualquer formato) |
| **Saídas** | A) Diagnóstico → B) Gargalo → C) Contrato → D) Follow-ups → E) E-mails → F) Instruções Lara |
| **Segurança** | ❌ Não envia. Gera rascunho + pede aprovação. |
| **Prompt** | `jobs/prompts/sprint_facilitator.txt` |

> **Nota:** Este job é executado como sessão interativa — Diego cola o One-Pager diretamente no chat do Morfeu.

---

### JOB 4: `sprint-followup-tracker`

| Campo | Valor |
|-------|-------|
| **Nome** | Follow-up Tracker — Praças |
| **Frequência** | D+3 após sprint fechado |
| **Gatilho** | Automático (3 dias após data da reunião) |
| **Entradas** | Lista de follow-ups da ata (extraída de `memory/projects_orulo.md`) |
| **Saídas** | Relatório de follow-ups abertos + alerta para Diego |
| **Segurança** | Apenas alerta interno. Não gera e-mail externo automaticamente. |
| **Prompt** | `jobs/prompts/sprint_followup_tracker.txt` |

**Configuração OpenClaw (quando ativar):**
```yaml
name: sprint-followup-tracker
schedule:
  kind: at
  at: "[ISO timestamp D+3 da reunião]"
payload:
  kind: agentTurn
  message: |
    [Ver jobs/prompts/sprint_followup_tracker.txt]
sessionTarget: isolated
delivery:
  mode: announce
```

---

### JOB 5: `praças-weekly-scan`

| Campo | Valor |
|-------|-------|
| **Nome** | Escaneamento Semanal de Praças |
| **Frequência** | Toda segunda-feira, 08:30 BRT |
| **Gatilho** | Automático |
| **Entradas** | `memory/projects_orulo.md` + `governance/praças.md` |
| **Saídas** | Alerta: praças sem sprint fechado / sem checkpoint / com pedido à Matriz em aberto |
| **Segurança** | Apenas alerta interno para Diego. |
| **Prompt** | `jobs/prompts/praças_weekly_scan.txt` |

**Configuração OpenClaw (quando ativar):**
```yaml
name: praças-weekly-scan
schedule:
  kind: cron
  expr: "30 8 * * MON"
  tz: America/Sao_Paulo
payload:
  kind: agentTurn
  message: |
    [Ver jobs/prompts/praças_weekly_scan.txt]
sessionTarget: isolated
delivery:
  mode: announce
```

---

## STATUS DE ATIVAÇÃO

| Job | Status | Bloqueio |
|-----|--------|---------|
| `sprint-reminder` | ⏸ Pendente | Aguarda datas de reunião por praça |
| `sprint-checkpoint` | ⏸ Pendente | Aguarda primeiro sprint fechado |
| `sprint-facilitator` | ✅ Pronto (manual) | — |
| `sprint-followup-tracker` | ⏸ Pendente | Aguarda primeiro sprint fechado |
| `praças-weekly-scan` | 🔜 Pronto para ativar | Diego confirma "OK para ativar" |

---

*Atualizar este arquivo quando ativar cada job com o jobId gerado pelo OpenClaw.*
