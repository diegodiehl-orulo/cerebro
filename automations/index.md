# automations/index.md — Mapa de Automações Ativas

> **Última atualização:** 2026-02-28
> **Propósito:** Referência única de todas as automações ativas do sistema Morfeu — crons OpenClaw e crontabs do sistema.

---

## 🔵 Crons OpenClaw (agendados via cron tool)

| Nome | Schedule | Modelo | Propósito |
|------|----------|--------|-----------|
| **Monitor tl;dv — Processador** | A cada 30min | claude-sonnet-4-6 | Detecta arquivo `tldv_pending.json`, processa reunião e envia resumo via Telegram. Filtra reuniões > 7 dias. Pausa 4h em caso de rate limit. |
| **Daily Briefing — Morfeu** | Seg–Sex às 08:45 BRT | claude-sonnet-4-6 | Agenda do dia via Google Calendar + pendências + projetos em atenção + viagens próximas. |
| **Digest Semanal de Emails** | Quartas às 10:00 BRT | claude-sonnet-4-6 | Resumo semanal de emails via Gmail: volume, remetentes, assuntos repetitivos, insights. |
| **Revisão Semanal — Morfeu** | Sextas às 16:00 BRT | claude-sonnet-4-6 | Consolida notas diárias, revisa projetos parados, pendências antigas, propõe foco da semana seguinte. |
| **Lembrete: refinamento de tom de voz** | 02/03 às 12:00 UTC | claude-sonnet-4-6 | One-shot. Lembrar Diego de enviar vídeo/palestra para refinamento do SOUL.md. |
| **Lembrete Pré-Viagem — Vitória ES** | 03/03 às 11:00 UTC | claude-sonnet-4-6 | One-shot. Checklist pré-viagem para Vitória (04/03). |

---

## ⚙️ Crontabs do Sistema (crontab -l)

| Script | Schedule | Propósito |
|--------|----------|-----------|
| `scripts/tldv_check.py` | A cada 15min (8h–18h, seg–sex) + a cada 3h | Etapa 1 do pipeline tl;dv: checa Gmail, detecta emails tl;dv e grava `tldv_pending.json` para o cron OpenClaw processar. Zero custo de IA. |
| `scripts/send_scheduled_email.py` | 02/03 às 11:40 UTC (one-shot) | Envia e-mail agendado para Gustavo (draft: `draft_gustavo_segunda.txt`). |

---

## 📁 Scripts Ativos

| Script | Função |
|--------|--------|
| `scripts/tldv_check.py` | Monitora Gmail, extrai emails tl;dv, grava flag para processamento |
| `scripts/email_digest.py` | Gera digest de emails para o cron Digest Semanal |
| `scripts/gmail_auth.py` | Utilitário de autenticação OAuth Gmail (leitura) |
| `scripts/gmail_send_auth.py` | Utilitário de autenticação OAuth Gmail (envio) |
| `scripts/send_scheduled_email.py` | Envia emails agendados com autenticação OAuth |

## 🗄️ Scripts Deprecated

| Script | Motivo |
|--------|--------|
| `scripts/deprecated/tldv_monitor.py` | Versão anterior do monitor tl;dv — substituído por tldv_check.py |
| `scripts/deprecated/tldv_smart.py` | Versão intermediária do monitor — substituído por tldv_check.py |

---

## 🔄 Pipeline tl;dv (como funciona)

```
Gmail (email tl;dv chega)
    → tldv_check.py (crontab sistema, a cada 15min)
        → detecta email novo
        → extrai conteúdo da reunião
        → salva em /root/.config/morfeu/tldv_pending.json
            → Monitor tl;dv — Processador (cron OpenClaw, a cada 30min)
                → lê o arquivo
                → checa data (descarta > 7 dias)
                → processa com IA
                → envia resumo via Telegram
                → deleta tldv_pending.json
```

---

## 📋 Arquivos de Estado (runtime)

| Arquivo | Propósito |
|---------|-----------|
| `/root/.config/morfeu/tldv_pending.json` | Reunião tl;dv aguardando processamento |
| `/root/.config/morfeu/tldv_pause_until` | Timestamp de pausa por rate limit (4h) |
| `/root/.config/morfeu/email_digest.json` | Output do digest de emails |
| `/var/log/tldv_check.log` | Log do script tldv_check.py |
| `/var/log/email_send.log` | Log do send_scheduled_email.py |
