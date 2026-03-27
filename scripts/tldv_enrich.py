#!/usr/bin/env python3
"""
tldv_enrich.py — Versão rica: extrai ações específicas, insights e topics
Enriquecido para fornecer valor real ao Diego
"""
import json, re, sys, pickle, html, base64
from pathlib import Path
from datetime import datetime
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

TOKEN_PATH = Path('/root/.config/morfeu/gmail_token.pkl')
PROCESSED_LIST = Path('/root/.config/morfeu/tldv_processed.json')
STORE_DIR = Path('/root/.config/morfeu/tldv_store')

def get_gmail():
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
    else: body = html_to_text(decode_body(payload))
    headers = {h['name']: h['value'] for h in payload.get('headers', [])}
    return body, headers

def extract_actions(body):
    """Extrai ações e insights separando por tipo"""
    raw_actions = re.findall(r'\* ([^*]+?)(?:\s+\d{2}:\d{2}|\s+https|$)', body)
    
    actions = []
    insights = []
    
    # Verbos de ação
    action_verbs = ['agendar', 'estabelecer', 'trabalhar', 'garantir', 'dedicar', 
                    'baixar', 'fazer', 'ligar', 'limpar', 'enviar', 'atualizar',
                    'preparar', 'validar', 'criar', 'montar', 'definir', 'testar',
                    'discutir', 'aprender', 'colocar', 'focar', 'comprar', 'contatar',
                    'formalizar', 'posicionar', 'equilibrar', 'otimizar', 'limitar',
                    'enviar', 'comprar', 'contatar']
    
    valid_owners = ['Gustavo', 'Diego', 'João', 'Paloma', 'Luana', 'Luan', 'Mila', 
                    'Mayumi', 'Felipe', 'Ale', 'Alejandro', 'Neno', 'Marcelo', 'Jade', 'Mirla']
    
    for a in raw_actions:
        a = a.strip()
        if len(a) < 15:
            continue
        
        is_action = any(a.lower().startswith(v) for v in action_verbs)
        a = re.sub(r'^\d+\.\s*', '', a)
        a = a[:180]
        
        if is_action:
            first_word = a.split()[0] if a.split() else ''
            if first_word in valid_owners:
                owner = first_word
                action = ' '.join(a.split()[1:])
            else:
                owner = '[dono]'
                action = a
            actions.append({'owner': owner, 'action': action})
        else:
            insights.append(a)
    
    return actions, insights

def process_meeting(msg_id, body, headers):
    """Processa uma reunião completa"""
    
    # Limpa título
    subject = headers.get('Subject', '')
    title = re.sub(r'^(Anotações|Notas)\s+(e\s+)?respostas\s+(por\s+)?IA\s+da\s+reunião\s+"', '', subject)
    title = re.sub(r'"\s+(estão\s+prontas|estão\s+prontas\s+✅)', '', title)
    
    # Parse data
    date_str = headers.get('Date', '')
    try:
        dt = datetime.strptime(date_str[:25], '%a, %d %b %Y %H:%M:%S')
        date_fmt = dt.strftime('%d/%m às %Hh%M')
    except:
        date_fmt = date_str[:20]
    
    actions, insights = extract_actions(body)
    
    return {
        'id': msg_id,
        'title': title,
        'date': date_fmt,
        'actions': actions,
        'insights': insights
    }

def generate_rich_report(meeting):
    """Gera relatório rico para Telegram"""
    
    title = meeting['title']
    date = meeting['date']
    actions = meeting.get('actions', [])
    insights = meeting.get('insights', [])
    
    report = []
    report.append(f"📋 *{title}*")
    report.append(f"🕐 {date}")
    report.append("")
    
    if actions:
        report.append("✅ *AÇÕES ESPECÍFICAS:*")
        for a in actions[:6]:
            report.append(f"• [{a['owner']}] {a['action']}")
        report.append("")
    
    if insights:
        report.append("💡 *INSIGHTS:*")
        for i in insights[:4]:
            report.append(f"• {i[:120]}")
        report.append("")
    
    return "\n".join(report)

def generate_followup_text(meetings):
    """Gera texto pronto para copy/paste em follow-ups"""
    
    text = "RESUMO DAS REUNIÕES — [DATA]\n\n"
    
    for m in meetings:
        text += f"\n📌 {m['title']}\n"
        if m.get('actions'):
            for a in m['actions'][:5]:
                text += f"- [{a['owner']}] {a['action']}\n"
        if m.get('insights'):
            text += "\nInsights:\n"
            for i in m['insights'][:3]:
                text += f"- {i[:100]}\n"
    
    return text

def main():
    STORE_DIR.mkdir(parents=True, exist_ok=True)
    
    service = get_gmail()
    
    # Carrega processados
    processed = set()
    if PROCESSED_LIST.exists():
        processed = set(json.loads(PROCESSED_LIST.read_text()))
    
    # Busca meetings dos últimos 2 dias
    results = service.users().messages().list(
        userId='me', 
        q='from:no-reply@tldv.io after:2026/03/05',
        maxResults=10
    ).execute()
    
    messages = results.get('messages', [])
    new_msgs = [m for m in messages if m['id'] not in processed]
    
    if not new_msgs:
        print("NONE")
        sys.exit(0)
    
    meetings = []
    for msg in new_msgs[:5]:
        body, headers = get_email(service, msg['id'])
        
        # Skip sem conteúdo
        if 'nenhum som foi detectado' in body.lower():
            processed.add(msg['id'])
            continue
        
        meeting = process_meeting(msg['id'], body, headers)
        meetings.append(meeting)
        
        # Salva estruturado
        date_folder = meeting['date'][:5].replace('/', '-')
        meeting_dir = STORE_DIR / f"2026-03-{date_folder}"
        meeting_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = meeting_dir / f"{msg['id']}_riched.json"
        file_path.write_text(json.dumps(meeting, ensure_ascii=False, indent=2))
        
        processed.add(msg['id'])
    
    # Salva processados
    PROCESSED_LIST.write_text(json.dumps(list(processed)))
    
    # Gera relatórios
    reports = [generate_rich_report(m) for m in meetings]
    followup = generate_followup_text(meetings)
    
    # Output JSON para cron usar
    output = {
        'meetings': meetings,
        'report': "\n---\n".join(reports),
        'followup_text': followup
    }
    
    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
