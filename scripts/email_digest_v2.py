#!/usr/bin/env python3
"""
Email Digest simplificado para Morfeu
Usa API direta do Google (mesmo credentials do tldv_check)
"""
import pickle, json, os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from pathlib import Path

TOKEN_FILE = '/root/.config/morfeu/gmail_token.pkl'
OUTPUT_FILE = '/root/.config/morfeu/email_digest.json'

def get_gmail():
    with open(TOKEN_FILE, 'rb') as f:
        creds = pickle.load(f)
    return build('gmail', 'v1', credentials=creds)

def main():
    service = get_gmail()
    
    # Ultimos 3 dias
    cutoff = (datetime.now() - timedelta(days=3)).strftime('%Y/%m/%d')
    
    # Busca emails
    results = service.users().messages().list(
        userId='me',
        q=f'after:{cutoff} -in:trash -in:spam',
        maxResults=50
    ).execute()
    
    messages = results.get('messages', [])
    
    # Agrupa por remetente
    senders = {}
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = {h['name']: h['value'] for h in msg_data['payload']['headers']}
        from_hdr = headers.get('From', '')
        subject = headers.get('Subject', '(sem assunto)')
        
        # Extrai email
        import re
        match = re.search(r'<(.+?)>|^(.+?@.+?)$', from_hdr)
        email = match.group(1) or match.group(2) if match else from_hdr
        
        if email not in senders:
            senders[email] = {'count': 0, 'subjects': []}
        senders[email]['count'] += 1
        senders[email]['subjects'].append(subject[:80])
    
    # Top remetentes
    top = sorted(senders.items(), key=lambda x: x[1]['count'], reverse=True)[:10]
    
    output = {
        'generated': datetime.now().isoformat(),
        'period': f'{cutoff} a {datetime.now().strftime("%Y/%m/%d")}',
        'total': len(messages),
        'top_senders': [{'email': e, 'count': d['count'], 'sample': d['subjects'][0]} for e, d in top]
    }
    
    Path(OUTPUT_FILE).write_text(json.dumps(output, ensure_ascii=False, indent=2))
    print(f"✅ {len(messages)} emails, {len(senders)} remetentes")
    print(f"📧 Top: {top[0][0]} ({top[0][1]['count']} emails)" if top else "Nenhum")

if __name__ == '__main__':
    main()
