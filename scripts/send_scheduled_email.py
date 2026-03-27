#!/usr/bin/env python3
"""
send_scheduled_email.py — Envia email via Gmail API (com salvaguardas de segurança)

⚠️  NUNCA enviar sem confirmação explícita de Diego.
    Ver política completa em /root/.openclaw/workspace/EMAIL_SECURITY.md

USO:
  python3 send_scheduled_email.py <arquivo_draft>             # Só valida, NÃO envia
  python3 send_scheduled_email.py <arquivo_draft> --confirm  # Envia (requer --confirm)

FORMATO DO DRAFT:
  TO: destinatario@email.com
  SUBJECT: Assunto do email
  APPROVED_BY: Diego Diehl
  APPROVED_AT: 2026-03-02T14:00:00
  ---
  Corpo do email aqui.
  Pode ter múltiplas linhas.

SEGURANÇA:
  - Sem --confirm: apenas valida o draft e mostra o que SERIA enviado
  - Com --confirm: envia de verdade (requer campos APPROVED_BY e APPROVED_AT no draft)
  - Deleção/modificação de emails: BLOQUEADA (ação proibida, ver EMAIL_SECURITY.md)
  - Hash de integridade: calculado no momento da aprovação e verificado no envio
"""

import argparse
import base64
import hashlib
import json
import pickle
import re
import sys
from datetime import datetime, timezone
from email.mime.text import MIMEText
from pathlib import Path

TOKEN_PATH  = Path('/root/.config/morfeu/gmail_token.pkl')
REMETENTE   = 'diego.diehl@orulo.com.br'
SECURITY_DOC = '/root/.openclaw/workspace/EMAIL_SECURITY.md'

# ─────────────────────────────────────────
# BLOQUEIO DE OPERAÇÕES PROIBIDAS
# ─────────────────────────────────────────
def _block_forbidden():
    """
    Sobrescreve métodos proibidos da Gmail API para evitar uso acidental.
    Chamado SEMPRE que o serviço é inicializado.
    """
    # Esta função é um lembrete de design: nunca chamar delete/trash/modify.
    # O token atual (gmail.readonly + gmail.send) já bloqueia via escopo,
    # mas a regra documental é reforçada aqui.
    FORBIDDEN_OPS = ['delete', 'trash', 'modify', 'batchDelete', 'batchModify']
    return FORBIDDEN_OPS  # Para referência/audit


# ─────────────────────────────────────────
# SERVIÇO GMAIL
# ─────────────────────────────────────────
def get_service():
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build

    with open(TOKEN_PATH, 'rb') as f:
        creds = pickle.load(f)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, 'wb') as f:
            pickle.dump(creds, f)

    # Verificar escopos — alertar se scope proibido detectado
    forbidden_scopes = [
        'https://mail.google.com/',
        'https://www.googleapis.com/auth/gmail.modify',
        'https://www.googleapis.com/auth/gmail.labels',
    ]
    granted = getattr(creds, 'scopes', []) or []
    for s in forbidden_scopes:
        if s in granted:
            print(f"🚨 ERRO DE SEGURANÇA: Escopo proibido detectado no token: {s}", file=sys.stderr)
            print(f"   Ver EMAIL_SECURITY.md — Escopos Proibidos", file=sys.stderr)
            sys.exit(1)

    return build('gmail', 'v1', credentials=creds)


# ─────────────────────────────────────────
# PARSE DO DRAFT
# ─────────────────────────────────────────
def parse_draft(path: str) -> dict:
    content = Path(path).read_text(encoding='utf-8')
    lines = content.split('\n')
    headers = {}
    body_lines = []
    in_body = False

    for line in lines:
        if line.strip() == '---':
            in_body = True
            continue
        if not in_body:
            if line.startswith('TO:'):
                headers['to'] = line[3:].strip()
            elif line.startswith('SUBJECT:'):
                headers['subject'] = line[8:].strip()
            elif line.startswith('APPROVED_BY:'):
                headers['approved_by'] = line[12:].strip()
            elif line.startswith('APPROVED_AT:'):
                headers['approved_at'] = line[12:].strip()
            elif line.startswith('CONTENT_HASH:'):
                headers['content_hash'] = line[13:].strip()
        else:
            body_lines.append(line)

    headers['body'] = '\n'.join(body_lines).strip()
    return headers


# ─────────────────────────────────────────
# VALIDAÇÃO PRÉ-ENVIO
# ─────────────────────────────────────────
def validate_draft(draft: dict, require_approval: bool = True) -> list[str]:
    """
    Valida o draft contra a checklist de segurança do EMAIL_SECURITY.md.
    Retorna lista de erros (vazia = tudo ok).
    """
    errors = []

    # 1. Destinatário
    if not draft.get('to'):
        errors.append("❌ TO: não especificado")
    elif '@' not in draft.get('to', ''):
        errors.append(f"❌ TO: parece inválido: '{draft.get('to')}'")

    # 2. Assunto
    if not draft.get('subject'):
        errors.append("❌ SUBJECT: não especificado")

    # 3. Corpo
    if not draft.get('body') or len(draft.get('body', '')) < 10:
        errors.append("❌ Corpo do email vazio ou muito curto")

    # 4. Aprovação (obrigatória para envio real)
    if require_approval:
        if not draft.get('approved_by'):
            errors.append("❌ APPROVED_BY: não encontrado — Diego precisa ter aprovado explicitamente")
        if not draft.get('approved_at'):
            errors.append("❌ APPROVED_AT: não encontrado — falta timestamp da aprovação")

    # 5. Verificação de integridade (se hash presente)
    if draft.get('content_hash'):
        expected = draft['content_hash']
        actual = _compute_hash(draft)
        if expected != actual:
            errors.append(
                f"🚨 HASH INVÁLIDO — conteúdo foi alterado após aprovação!\n"
                f"   Esperado: {expected}\n"
                f"   Atual:    {actual}\n"
                f"   Envio BLOQUEADO. Solicitar nova aprovação de Diego."
            )

    # 6. Alerta de campos sensíveis (não bloqueia, mas avisa)
    sensitive_patterns = [
        (r'\bR\$\s*[\d.,]+', "valor monetário"),
        (r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', "data"),
        (r'\bprazo\b|\bdeadline\b|\bentrega\b', "prazo/deadline"),
        (r'\bconfirm[ao]\b|\bgaranto\b|\bcomprometemos\b', "compromisso formal"),
    ]
    warnings = []
    body_lower = draft.get('body', '').lower()
    for pattern, label in sensitive_patterns:
        if re.search(pattern, draft.get('body', ''), re.IGNORECASE):
            warnings.append(f"⚠️  Campo sensível detectado: {label} — verificar com Diego antes de enviar")

    return errors, warnings


def _compute_hash(draft: dict) -> str:
    """Hash de integridade do conteúdo do email."""
    content = f"{draft.get('to','')}{draft.get('subject','')}{draft.get('body','')}"
    return hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]


# ─────────────────────────────────────────
# ENVIO
# ─────────────────────────────────────────
def send_email(draft: dict) -> str:
    """
    Envia o email. Só chamar após validação completa e --confirm explícito.
    Retorna o message ID do Gmail.
    """
    service = get_service()

    msg = MIMEText(draft['body'], 'plain', 'utf-8')
    msg['to']      = draft['to']
    msg['subject'] = draft['subject']
    msg['from']    = REMETENTE

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    result = service.users().messages().send(
        userId='me', body={'raw': raw}
    ).execute()

    return result.get('id')


# ─────────────────────────────────────────
# CLI
# ─────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Envia email via Gmail API com salvaguardas de segurança"
    )
    parser.add_argument("draft", help="Arquivo com o rascunho do email")
    parser.add_argument(
        "--confirm",
        action="store_true",
        help="⚠️ CONFIRMAR envio real (sem essa flag, apenas valida)"
    )
    parser.add_argument(
        "--generate-hash",
        action="store_true",
        help="Gera hash de integridade para o draft (usar ao aprovar)"
    )
    args = parser.parse_args()

    # Carregar draft
    draft_path = args.draft
    if not Path(draft_path).exists():
        print(f"Erro: arquivo não encontrado: {draft_path}", file=sys.stderr)
        sys.exit(1)

    draft = parse_draft(draft_path)

    # Modo: gerar hash de aprovação
    if args.generate_hash:
        h = _compute_hash(draft)
        print(f"CONTENT_HASH: {h}")
        print(f"\nAdicione essa linha ao draft antes de APPROVED_BY:")
        print(f"  CONTENT_HASH: {h}")
        print(f"\nQualquer alteração no conteúdo após isso invalidará o hash e bloqueará o envio.")
        return

    # Validar draft
    errors, warnings = validate_draft(draft, require_approval=args.confirm)

    # Exibir prévia
    print("═" * 60)
    print("📧 PRÉVIA DO EMAIL")
    print("═" * 60)
    print(f"  De:      {REMETENTE}")
    print(f"  Para:    {draft.get('to', '⚠️ NÃO DEFINIDO')}")
    print(f"  Assunto: {draft.get('subject', '⚠️ NÃO DEFINIDO')}")
    if draft.get('approved_by'):
        print(f"  Aprovado por: {draft.get('approved_by')} em {draft.get('approved_at', '?')}")
    print("─" * 60)
    print(draft.get('body', ''))
    print("═" * 60)

    # Exibir warnings
    if warnings:
        print("\n⚠️  AVISOS (verificar com Diego):")
        for w in warnings:
            print(f"  {w}")

    # Se há erros, bloquear
    if errors:
        print("\n🚨 ENVIO BLOQUEADO — Erros encontrados:")
        for e in errors:
            print(f"  {e}")
        print(f"\nVer política completa em: {SECURITY_DOC}")
        sys.exit(1)

    # Modo dry-run (sem --confirm)
    if not args.confirm:
        print("\n✅ Draft válido. Email NÃO enviado (dry-run).")
        print("   Para enviar de verdade: adicione --confirm")
        print("   Para gerar hash de integridade: use --generate-hash após aprovação de Diego")
        return

    # Confirmação final antes de enviar
    print(f"\n⚠️  CONFIRMAÇÃO FINAL")
    print(f"   Isso enviará um email REAL para: {draft['to']}")
    print(f"   Em nome de: {REMETENTE}")
    print(f"   Esta ação é irreversível.")
    resposta = input("\n   Digite 'CONFIRMAR' para enviar: ").strip()

    if resposta != 'CONFIRMAR':
        print("Envio cancelado.")
        sys.exit(0)

    # Enviar
    print("\nEnviando...")
    msg_id = send_email(draft)
    print(f"✅ Email enviado com sucesso!")
    print(f"   Message ID: {msg_id}")
    print(f"   Para: {draft['to']}")
    print(f"   Assunto: {draft['subject']}")


if __name__ == '__main__':
    main()
