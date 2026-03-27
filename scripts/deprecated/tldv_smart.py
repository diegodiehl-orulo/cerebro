#!/usr/bin/env python3
"""
tldv_smart.py — Monitor inteligente de reuniões tl;dv
Lógica: Python checa email (gratuito) → IA só é chamada se houver reunião nova
Custo: zero para runs vazios; ~R$0.05 por reunião processada
"""
import json, pickle, re, os, sys, html, base64
from pathlib import Path
import urllib.request, urllib.error

# ── Configuração ──────────────────────────────────────────────────────────────
TOKEN_PATH     = Path('/root/.config/morfeu/gmail_token.pkl')
PROCESSED_PATH = Path('/root/.config/morfeu/tldv_processed.json')
OUTPUT_PATH    = Path('/root/.config/morfeu/tldv_latest.json')
AUTH_PROFILES  = Path('/root/.openclaw/agents/main/agent/auth-profiles.json')
OPENCLAW_JSON  = Path('/root/.openclaw/openclaw.json')
TELEGRAM_CHAT  = '8671853499'

def get_api_key():
    d = json.loads(AUTH_PROFILES.read_text())
    profiles = d.get('profiles', {})
    for k, v in profiles.items():
        if v.get('provider') == 'anthropic':
            return v.get('token', '')
    return ''

def get_telegram_token():
    d = json.loads(OPENCLAW_JSON.read_text())
    return d['channels']['telegram']['botToken']

# ── Gmail ─────────────────────────────────────────────────────────────────────
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

def load_processed():
    if PROCESSED_PATH.exists():
        return set(json.loads(PROCESSED_PATH.read_text()))
    return set()

def save_processed(ids):
    PROCESSED_PATH.write_text(json.dumps(list(ids)))

def decode_body(part):
    data = part.get('body', {}).get('data', '')
    if data:
        return base64.urlsafe_b64decode(data + '==').decode('utf-8', errors='ignore')
    return ''

def html_to_text(h):
    t = re.sub(r'<br\s*/?>', '\n', h, flags=re.IGNORECASE)
    t = re.sub(r'<p[^>]*>', '\n', t, flags=re.IGNORECASE)
    t = re.sub(r'<li[^>]*>', '\n• ', t, flags=re.IGNORECASE)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    return re.sub(r'\n{3,}', '\n\n', t).strip()

def get_email(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    payload = msg.get('payload', {})
    body = ''

    def extract(parts):
        nonlocal body
        for p in parts:
            mime = p.get('mimeType', '')
            if mime == 'text/plain':
                body += decode_body(p)
            elif mime == 'text/html' and not body:
                body = html_to_text(decode_body(p))
            elif 'parts' in p:
                extract(p['parts'])

    if 'parts' in payload:
        extract(payload['parts'])
    elif payload.get('mimeType') == 'text/html':
        body = html_to_text(decode_body(payload))
    else:
        body = decode_body(payload)

    headers = {h['name']: h['value'] for h in payload.get('headers', [])}
    return {
        'id': msg_id,
        'subject': headers.get('Subject', ''),
        'sender': headers.get('From', ''),
        'date': headers.get('Date', ''),
        'body': body,
    }

def check_email():
    service = get_gmail_service()
    processed = load_processed()
    results = service.users().messages().list(
        userId='me', q='from:no-reply@tldv.io is:unread', maxResults=10
    ).execute()
    messages = results.get('messages', [])
    new = [m for m in messages if m['id'] not in processed]
    if not new:
        return None, processed
    email = get_email(service, new[0]['id'])
    processed.add(new[0]['id'])
    return email, processed

# ── Anthropic ─────────────────────────────────────────────────────────────────
def summarize(email):
    api_key = get_api_key()
    if not api_key:
        return None

    # Limpar subject
    subject = email['subject']
    subject = re.sub(r'Anota[çc][õo]es e respostas por IA da reuni[ãa]o\s*["\u201c]?', '', subject)
    subject = re.sub(r'["\u201c\u201d]["\u201d]?\s*est[ãa]o prontas\s*✅?', '', subject).strip()

    prompt = f"""Você é o Morfeu, assistente estratégico de Diego Diehl. Analise esta reunião do tl;dv e retorne APENAS o resumo formatado abaixo, sem texto adicional antes ou depois.

REUNIÃO: {subject}
DATA: {email['date']}

CONTEÚDO DO EMAIL:
{email['body'][:4000]}

Formate assim (Telegram MarkdownV2 — escape pontos, hífens e parênteses com \\):

🔵 *Nova reunião processada — tl;dv*
📋 *{subject}*
🕐 [data/hora em BRT: DD/MM às HH:MM]

👥 *Participantes:* [nomes dos itens de ação]

📌 *Principais tópicos:*
• [tópico 1]
• [tópico 2]
• [tópico 3]

✅ *Seus itens de ação:*
• [timestamp] — [ação de Diego]

✅ *Time:*
• [Pessoa] → [ação]

❓ *Perguntas de esclarecimento:*
1\\. [pergunta]
2\\. [pergunta]

🎯 *Próximas ações sugeridas:*
• [ação concreta alinhada à Órulo]
• [ação concreta]

Se Diego não tiver itens de ação, omita essa seção. Máximo 40 linhas."""

    payload = json.dumps({
        "model": "claude-3-5-haiku-20241022",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}]
    }).encode()

    req = urllib.request.Request(
        'https://api.anthropic.com/v1/messages',
        data=payload,
        headers={
            'x-api-key': api_key,
            'anthropic-version': '2023-06-01',
            'content-type': 'application/json',
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            result = json.loads(r.read())
            return result['content'][0]['text']
    except Exception as e:
        print(f"AI error: {e}", file=sys.stderr)
        return None

# ── Telegram ──────────────────────────────────────────────────────────────────
def send_telegram(text):
    bot_token = get_telegram_token()
    payload = json.dumps({
        'chat_id': TELEGRAM_CHAT,
        'text': text,
        'parse_mode': 'MarkdownV2'
    }).encode()
    req = urllib.request.Request(
        f'https://api.telegram.org/bot{bot_token}/sendMessage',
        data=payload,
        headers={'content-type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            result = json.loads(r.read())
            return result.get('ok', False)
    except Exception as e:
        print(f"Telegram error: {e}", file=sys.stderr)
        return False

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    email, processed = check_email()
    if not email:
        sys.exit(0)  # Sem email novo — saída limpa, zero custo de IA

    # Reunião sem conteúdo
    if 'nenhum som foi detectado' in email['body'] or \
       'não conseguiu gerar anotações' in email['body']:
        save_processed(processed)
        sys.exit(0)

    # Salva para debug
    OUTPUT_PATH.write_text(json.dumps(email, ensure_ascii=False, indent=2))

    # Resumo via IA (só aqui entra custo)
    summary = summarize(email)
    if not summary:
        sys.exit(1)

    # Envia pro Telegram
    ok = send_telegram(summary)
    if ok:
        save_processed(processed)
        print(f"OK: {email['subject'][:60]}")
    else:
        # Tenta envio sem markdown se falhar
        plain = re.sub(r'[*_`\[\]()~>#+\-=|{}.!\\]', '', summary)
        ok2 = send_telegram_plain(plain, bot_token=get_telegram_token())
        if ok2:
            save_processed(processed)

def send_telegram_plain(text, bot_token):
    payload = json.dumps({
        'chat_id': TELEGRAM_CHAT,
        'text': text,
    }).encode()
    req = urllib.request.Request(
        f'https://api.telegram.org/bot{bot_token}/sendMessage',
        data=payload,
        headers={'content-type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read()).get('ok', False)
    except:
        return False

if __name__ == '__main__':
    main()
