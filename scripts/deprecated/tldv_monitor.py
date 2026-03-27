#!/usr/bin/env python3
"""
Monitor de emails tl;dv — Morfeu
Detecta emails do tl;dv, extrai conteúdo e salva para processamento.
"""
import pickle, json, re, os, sys
from pathlib import Path
from datetime import datetime
import base64, html

TOKEN_PATH = Path('/root/.config/morfeu/gmail_token.pkl')
PROCESSED_PATH = Path('/root/.config/morfeu/tldv_processed.json')
OUTPUT_PATH = Path('/root/.config/morfeu/tldv_latest.json')

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
    if data:
        return base64.urlsafe_b64decode(data + '==').decode('utf-8', errors='ignore')
    return ''

def extract_text_from_html(html_content):
    # Remove tags HTML e decodifica entidades
    text = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<li[^>]*>', '\n• ', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    # Remove linhas em branco excessivas
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def get_message_body(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    payload = msg.get('payload', {})
    body_text = ''

    def extract_parts(parts):
        nonlocal body_text
        for part in parts:
            mime = part.get('mimeType', '')
            if mime == 'text/plain':
                body_text += decode_body(part)
            elif mime == 'text/html' and not body_text:
                body_text = extract_text_from_html(decode_body(part))
            elif 'parts' in part:
                extract_parts(part['parts'])

    if 'parts' in payload:
        extract_parts(payload['parts'])
    elif payload.get('mimeType') == 'text/html':
        body_text = extract_text_from_html(decode_body(payload))
    elif payload.get('mimeType') == 'text/plain':
        body_text = decode_body(payload)

    # Extrair headers
    headers = {h['name']: h['value'] for h in payload.get('headers', [])}
    subject = headers.get('Subject', '')
    sender = headers.get('From', '')
    date = headers.get('Date', '')

    return {
        'id': msg_id,
        'subject': subject,
        'sender': sender,
        'date': date,
        'body': body_text,
    }

def main():
    service = get_gmail_service()
    processed = load_processed()

    # Buscar emails do tl;dv
    query = 'from:no-reply@tldv.io is:unread'
    results = service.users().messages().list(userId='me', q=query, maxResults=10).execute()
    messages = results.get('messages', [])

    if not messages:
        print("NONE")
        return

    new_emails = [m for m in messages if m['id'] not in processed]
    if not new_emails:
        print("NONE")
        return

    # Processar o mais recente
    msg_data = get_message_body(service, new_emails[0]['id'])
    
    # Salvar para processamento pelo agente
    OUTPUT_PATH.write_text(json.dumps(msg_data, ensure_ascii=False, indent=2))
    
    # Marcar como processado
    processed.add(new_emails[0]['id'])
    save_processed(processed)
    
    print(f"NEW:{new_emails[0]['id']}")
    print(f"SUBJECT:{msg_data['subject']}")

if __name__ == '__main__':
    main()
