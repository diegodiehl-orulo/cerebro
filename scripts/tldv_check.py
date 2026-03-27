#!/usr/bin/env python3
"""
tldv_check.py — Etapa 1 (Python puro, zero custo de IA)
Checa Gmail, se achar email novo escreve flag para o OpenClaw processar.
Roda via crontab do sistema — não usa API da Anthropic.
"""
import pickle, json, re, html, base64, sys
from pathlib import Path

TOKEN_PATH     = Path('/root/.config/morfeu/gmail_token.pkl')
PROCESSED_PATH = Path('/root/.config/morfeu/tldv_processed.json')
FLAG_PATH      = Path('/root/.config/morfeu/tldv_pending.json')  # flag para o OpenClaw

def load_processed():
    if PROCESSED_PATH.exists():
        return set(json.loads(PROCESSED_PATH.read_text()))
    return set()

def save_processed(ids):
    PROCESSED_PATH.write_text(json.dumps(list(ids)))

def get_gmail_service():
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    with open(TOKEN_PATH, 'rb') as f:
        creds = pickle.load(f)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, 'wb') as f:
            pickle.dump(creds, f)
    return build('gmail', 'v1', credentials=creds)

def decode_body(part):
    data = part.get('body', {}).get('data', '')
    return base64.urlsafe_b64decode(data + '==').decode('utf-8', errors='ignore') if data else ''

def html_to_text(h):
    t = re.sub(r'<br\s*/?>', '\n', h, flags=re.IGNORECASE)
    t = re.sub(r'<li[^>]*>', '\n• ', t, flags=re.IGNORECASE)
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'\n{3,}', '\n\n', html.unescape(t)).strip()

def get_email(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    payload = msg.get('payload', {})
    body = ''

    def extract(parts):
        nonlocal body
        for p in parts:
            mime = p.get('mimeType', '')
            if mime == 'text/plain': body += decode_body(p)
            elif mime == 'text/html' and not body: body = html_to_text(decode_body(p))
            elif 'parts' in p: extract(p['parts'])

    if 'parts' in payload: extract(payload['parts'])
    elif 'html' in payload.get('mimeType', ''): body = html_to_text(decode_body(payload))
    else: body = decode_body(payload)

    headers = {h['name']: h['value'] for h in payload.get('headers', [])}
    return {
        'id': msg_id,
        'subject': headers.get('Subject', ''),
        'date': headers.get('Date', ''),
        'body': body,
    }

def main():
    # Se já existe uma flag pendente não processada, não sobrescreve
    if FLAG_PATH.exists():
        sys.exit(0)

    service = get_gmail_service()
    processed = load_processed()
    results = service.users().messages().list(
        userId='me', q='from:no-reply@tldv.io is:unread', maxResults=10
    ).execute()
    messages = results.get('messages', [])
    new = [m for m in messages if m['id'] not in processed]

    if not new:
        sys.exit(0)  # Nada novo — saída silenciosa

    email = get_email(service, new[0]['id'])

    # Pula reuniões sem conteúdo
    if 'nenhum som foi detectado' in email['body'] or \
       'não conseguiu gerar anotações' in email['body']:
        processed.add(new[0]['id'])
        save_processed(processed)
        sys.exit(0)

    # Escreve flag — OpenClaw vai processar no próximo ciclo
    FLAG_PATH.write_text(json.dumps(email, ensure_ascii=False, indent=2))
    processed.add(new[0]['id'])
    save_processed(processed)
    print(f"FLAG: {email['subject'][:60]}")

if __name__ == '__main__':
    main()
