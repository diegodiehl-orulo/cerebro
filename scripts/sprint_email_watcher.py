#!/usr/bin/env python3
"""
Sprint Email Watcher — Morfeu
Detecta e-mails de One-Pager de Sprint dos sócios locais (Zanella, Kneip).
Salva para processamento pelo Morfeu.
"""
import pickle, json, base64, re
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from pathlib import Path

TOKEN_FILE     = '/root/.config/morfeu/gmail_token.pkl'
PENDING_FILE   = '/root/.config/morfeu/sprint_email_pending.json'
PROCESSED_FILE = '/root/.config/morfeu/sprint_email_processed.json'

# Sócios locais monitorados
SOCIOS = {
    'luiz.zanella@orulo.com.br': {'nome': 'Zanella', 'praca': 'Curitiba'},
    'pkneip@orulo.com.br':       {'nome': 'Pedro Kneip', 'praca': 'Vitória'},
}

# Padrão de assunto — aceita variações
SUBJECT_PATTERNS = [
    'sprint quinzenal',
    'one-pager',
    'one pager',
    'sprint | praça',
    'sprint | praca',
    'órulo | sprint',
    'orulo | sprint',
]

def get_gmail():
    with open(TOKEN_FILE, 'rb') as f:
        creds = pickle.load(f)
    return build('gmail', 'v1', credentials=creds)

def load_processed():
    path = Path(PROCESSED_FILE)
    if path.exists():
        with open(path) as f:
            return set(json.load(f))
    return set()

def save_processed(ids):
    Path(PROCESSED_FILE).write_text(json.dumps(list(ids)))

def extract_email_addr(from_header):
    match = re.search(r'<(.+?)>', from_header)
    if match:
        return match.group(1).lower()
    return from_header.strip().lower()

def decode_body(payload):
    """Extrai corpo do e-mail (plain text preferencial)."""
    body = ''
    if payload.get('mimeType') == 'text/plain':
        data = payload.get('body', {}).get('data', '')
        if data:
            body = base64.urlsafe_b64decode(data + '==').decode('utf-8', errors='replace')
    elif payload.get('parts'):
        for part in payload['parts']:
            if part.get('mimeType') == 'text/plain':
                data = part.get('body', {}).get('data', '')
                if data:
                    body = base64.urlsafe_b64decode(data + '==').decode('utf-8', errors='replace')
                    break
            elif part.get('mimeType', '').startswith('multipart/'):
                body = decode_body(part)
                if body:
                    break
    return body.strip()

def is_sprint_subject(subject):
    subject_lower = subject.lower()
    return any(p in subject_lower for p in SUBJECT_PATTERNS)

def main():
    service = get_gmail()
    processed = load_processed()
    
    # Últimos 7 dias
    cutoff = (datetime.now() - timedelta(days=7)).strftime('%Y/%m/%d')
    
    # Query: e-mails dos sócios nos últimos 7 dias
    sender_query = ' OR '.join([f'from:{email}' for email in SOCIOS.keys()])
    query = f'({sender_query}) after:{cutoff} -in:trash -in:spam'
    
    results = service.users().messages().list(
        userId='me',
        q=query,
        maxResults=20
    ).execute()
    
    messages = results.get('messages', [])
    found = []
    
    for msg in messages:
        msg_id = msg['id']
        if msg_id in processed:
            continue
        
        msg_data = service.users().messages().get(
            userId='me', id=msg_id, format='full'
        ).execute()
        
        headers = {h['name'].lower(): h['value'] 
                   for h in msg_data['payload']['headers']}
        
        from_email  = extract_email_addr(headers.get('from', ''))
        subject     = headers.get('subject', '(sem assunto)')
        date_header = headers.get('date', '')
        
        # Só processa se é de um sócio E tem padrão de sprint
        if from_email in SOCIOS and is_sprint_subject(subject):
            socio_info = SOCIOS[from_email]
            body = decode_body(msg_data['payload'])
            
            entry = {
                'id':         msg_id,
                'from':       from_email,
                'nome':       socio_info['nome'],
                'praca':      socio_info['praca'],
                'subject':    subject,
                'date':       date_header,
                'body':       body[:8000],  # máx 8k chars
                'detected_at': datetime.now().isoformat(),
            }
            found.append(entry)
            processed.add(msg_id)
    
    save_processed(processed)
    
    if found:
        # Salva para o Morfeu processar
        Path(PENDING_FILE).write_text(
            json.dumps(found, ensure_ascii=False, indent=2)
        )
        print(f'FOUND:{len(found)}')
        for f in found:
            print(f"  → {f['praca']} ({f['nome']}) | {f['subject'][:60]}")
    else:
        print('NONE')

if __name__ == '__main__':
    main()
