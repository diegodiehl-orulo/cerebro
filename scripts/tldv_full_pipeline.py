#!/usr/bin/env python3
"""
tldv_full_pipeline.py — Executa o pipeline completo de tl;dv
1. Busca emails novos do tl;dv
2. Processa cada um (extrai actions + gera resumo)
3. Salva estruturado
4. Retorna resumo formatado para enviar ao Diego
"""
import json, re, sys, pickle, html
from pathlib import Path
from datetime import datetime
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64

TOKEN_PATH = Path('/root/.config/morfeu/gmail_token.pkl')
PROCESSED_LIST = Path('/root/.config/morfeu/tldv_processed.json')
STORE_DIR = Path('/root/.config/morfeu/tldv_store')
ACTIONS_DIR = Path('/root/.config/morfeu/tldv_actions')

def get_gmail_service():
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

def get_email_body(service, msg_id):
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
    return body, headers

def extract_actions(body):
    """Extrai action items do body"""
    actions = []
    lines = body.split('\n')
    
    in_actions = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if 'Itens de Ação' in line or 'Próximos passos' in line or 'Action Items' in line:
            in_actions = True
            continue
        if line.startswith('•') or re.match(r'^\d+[\.\)]', line):
            text = re.sub(r'^[•\d\.\)]+\s*', '', line)
            text = re.sub(r'\s+\d{2}:\d{2}.*$', '', text).strip('.,;:')
            if text and len(text) > 5:
                # Tenta extrair dono
                words = text.split()
                owner = None
                for word in words:
                    if word and word[0].isupper() and len(word) > 2:
                        if word.lower() not in ['revisar', 'enviar', 'criar', 'montar', 'preparar', 'diego', 'gustavo', 'mayumi']:
                            owner = word
                            break
                actions.append({'owner': owner, 'action': text})
    
    return actions

def load_processed():
    if PROCESSED_LIST.exists():
        return set(json.loads(PROCESSED_LIST.read_text()))
    return set()

def save_processed(ids):
    PROCESSED_LIST.write_text(json.dumps(list(ids)))

def main():
    STORE_DIR.mkdir(parents=True, exist_ok=True)
    ACTIONS_DIR.mkdir(parents=True, exist_ok=True)
    
    service = get_gmail_service()
    processed = load_processed()
    
    # Busca emails do tl;dv dos últimos 2 dias
    results = service.users().messages().list(
        userId='me', 
        q='from:no-reply@tldv.io after:2026/03/05',
        maxResults=10
    ).execute()
    
    messages = results.get('messages', [])
    new = [m for m in messages if m['id'] not in processed]
    
    if not new:
        print("NONE")
        sys.exit(0)
    
    # Processa cada reunião nova
    output = []
    for msg in new[:5]:  # Max 5 por vez
        body, headers = get_email_body(service, msg['id'])
        
        # Skip se sem conteúdo
        if 'nenhum som foi detectado' in body.lower():
            processed.add(msg['id'])
            continue
            
        subject = headers.get('Subject', '(sem título)')
        date = headers.get('Date', '')
        
        # Extrai actions
        actions = extract_actions(body)
        
        # Salva estruturado
        try:
            dt = datetime.strptime(date[:25], '%a, %d %b %Y %H:%M:%S')
            date_folder = dt.strftime('%Y-%m-%d')
        except:
            date_folder = datetime.now().strftime('%Y-%m-%d')
        
        meeting_dir = STORE_DIR / date_folder
        meeting_dir.mkdir(parents=True, exist_ok=True)
        
        structured = {
            'id': msg['id'],
            'subject': subject,
            'date': date,
            'processed_at': datetime.now().isoformat(),
            'actions': actions
        }
        
        meeting_file = meeting_dir / f"{msg['id']}.json"
        meeting_file.write_text(json.dumps(structured, ensure_ascii=False, indent=2))
        
        if actions:
            actions_file = ACTIONS_DIR / f"{msg['id']}_actions.json"
            actions_file.write_text(json.dumps(actions, ensure_ascii=False, indent=2))
        
        processed.add(msg['id'])
        
        # Adiciona ao output
        title = subject.replace('Anotações e respostas por IA da reunião "', '').replace('" estão prontas ✅', '').replace('Notas e respostas por IA da reunião "', '')
        
        output.append({
            'id': msg['id'],
            'title': title,
            'date': date[:25],
            'actions': actions
        })
    
    save_processed(processed)
    
    # Output formatado
    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
