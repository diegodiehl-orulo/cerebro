#!/usr/bin/env python3
"""
Monitor de emails tl;dv
Detecta novos emails de reunião e salva para processamento
"""
import pickle, json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from pathlib import Path
import os

TOKEN_FILE = '/root/.config/morfeu/gmail_token.pkl'
PENDING_FILE = '/root/.config/morfeu/tldv_pending.json'
PROCESSED_FILE = '/root/.config/morfeu/tldv_processed.json'
PROCESSED_DIR = '/root/.config/morfeu/tldv_processed/'
PAUSE_FILE = '/root/.config/morfeu/tldv_pause_until'

def get_gmail():
    with open(TOKEN_FILE, 'rb') as f:
        creds = pickle.load(f)
    return build('gmail', 'v1', credentials=creds)

def load_processed():
    """Carrega lista de IDs já processados"""
    path = Path(PROCESSED_FILE)
    if path.exists():
        with open(path) as f:
            return set(json.load(f))
    return set()

def save_processed(processed_ids):
    """Salva lista de IDs processados"""
    Path(PROCESSED_FILE).write_text(json.dumps(list(processed_ids)))

def check_pause():
    """Verifica se está em rate limit"""
    path = Path(PAUSE_FILE)
    if path.exists():
        with open(path) as f:
            pause_until = int(f.read().strip())
        if datetime.now().timestamp() < pause_until:
            return True
    return False

def main():
    # Verifica pause
    if check_pause():
        print("RATE_LIMIT: em pausa")
        exit(0)
    
    service = get_gmail()
    
    # Últimos 7 dias
    cutoff = (datetime.now() - timedelta(days=7)).strftime('%Y/%m/%d')
    
    # Busca emails do tl;dv
    results = service.users().messages().list(
        userId='me',
        q=f'from:tldv.io after:{cutoff} -in:trash -in:spam',
        maxResults=20
    ).execute()
    
    messages = results.get('messages', [])
    
    if not messages:
        print("NONE: nenhum email tl;dv encontrado")
        exit(0)
    
    # Carrega processados
    processed = load_processed()
    
    # Procura novo
    for msg in messages:
        msg_id = msg['id']
        
        if msg_id in processed:
            continue
        
        # Pega conteúdo completo
        msg_data = service.users().messages().get(
            userId='me',
            id=msg_id,
            format='full'
        ).execute()
        
        headers = {h['name']: h['value'] for h in msg_data['payload']['headers']}
        subject = headers.get('Subject', '(sem assunto)')
        
        # Ignora se é notificação de sala de espera
        if 'saiu da sala de espera' in subject.lower():
            processed.add(msg_id)
            save_processed(processed)
            continue
        
        # Pega corpo
        body = ''
        if 'parts' in msg_data['payload']:
            for part in msg_data['payload']['parts']:
                if part.get('mimeType') == 'text/html':
                    body = part.get('body', {}).get('data', '')
                    break
                elif part.get('mimeType') == 'text/plain':
                    body = part.get('body', {}).get('data', '')
        
        if not body:
            body = msg_data.get('snippet', '')
        
        # Decodifica base64
        import base64
        try:
            body = base64.urlsafe_b64decode(body).decode('utf-8')
        except:
            pass
        
        # Salva como pendente
        pending_data = {
            'id': msg_id,
            'subject': subject,
            'date': headers.get('Date', ''),
            'body': body[:50000],  # limita tamanho
            'received_at': datetime.now().isoformat()
        }
        
        Path(PENDING_FILE).write_text(json.dumps(pending_data, ensure_ascii=False))
        
        # Adiciona aos processados (pra não reprocessar)
        processed.add(msg_id)
        save_processed(processed)
        
        print(f"NEW: {subject[:60]}")
        exit(0)
    
    print("NONE: nenhum email novo")

if __name__ == '__main__':
    main()
