#!/usr/bin/env python3
"""
email_digest.py — Digest semanal de emails (Python puro)
Lê os últimos 7 dias do Gmail, agrupa por remetente/domínio/padrão.
Saída: JSON estruturado para o cron processar com IA.
Zero custo — não chama Anthropic.
"""
import pickle, json, re, sys
from pathlib import Path
from datetime import datetime, timedelta, timezone
from collections import Counter, defaultdict

TOKEN_PATH  = Path('/root/.config/morfeu/gmail_token.pkl')
OUTPUT_PATH = Path('/root/.config/morfeu/email_digest.json')

def get_service():
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    with open(TOKEN_PATH, 'rb') as f:
        creds = pickle.load(f)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, 'wb') as f:
            pickle.dump(creds, f)
    return build('gmail', 'v1', credentials=creds)

def extract_sender(from_header):
    """Extrai nome e domínio do campo From."""
    email_match = re.search(r'<([^>]+)>', from_header)
    email = email_match.group(1) if email_match else from_header.strip()
    name_match = re.match(r'^"?([^"<]+)"?\s*<', from_header)
    name = name_match.group(1).strip() if name_match else email.split('@')[0]
    domain = email.split('@')[-1] if '@' in email else email
    return name, email, domain

def normalize_subject(subject):
    """Remove prefixos Re/Fwd e números para agrupar subjects similares."""
    s = re.sub(r'^(Re|Fwd|FWD|RE|RES|ENC):\s*', '', subject, flags=re.IGNORECASE).strip()
    s = re.sub(r'\s*#\d+\s*', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:80]

def main():
    service = get_service()

    # Últimos 7 dias
    since = (datetime.now(timezone.utc) - timedelta(days=7)).strftime('%Y/%m/%d')
    query = f'after:{since} -category:promotions -category:social'

    # Busca paginada (max 150 emails — limite para evitar timeout de 3min)
    messages = []
    page_token = None
    while len(messages) < 150:
        params = dict(userId='me', q=query, maxResults=50)
        if page_token:
            params['pageToken'] = page_token
        result = service.users().messages().list(**params).execute()
        batch = result.get('messages', [])
        messages.extend(batch)
        page_token = result.get('nextPageToken')
        if not page_token:
            break

    total = len(messages)
    if total == 0:
        print("EMPTY")
        sys.exit(0)

    # Busca headers de cada email (barato — só metadata)
    by_sender    = Counter()   # email → count
    by_domain    = Counter()   # domain → count
    by_subject   = Counter()   # normalized subject → count
    sender_names = {}          # email → display name
    unread_count = 0
    orulo_emails = []          # emails do domínio orulo.com.br
    high_freq_subjects = []

    for msg in messages:
        try:
            detail = service.users().messages().get(
                userId='me', id=msg['id'],
                format='metadata',
                metadataHeaders=['From', 'Subject', 'Date']
            ).execute()
        except Exception:
            continue

        headers = {h['name']: h['value'] for h in detail.get('payload', {}).get('headers', [])}
        labels  = detail.get('labelIds', [])

        from_h   = headers.get('From', '')
        subject  = headers.get('Subject', '(sem assunto)')
        name, email_addr, domain = extract_sender(from_h)

        sender_names[email_addr] = name
        by_sender[email_addr]   += 1
        by_domain[domain]       += 1
        by_subject[normalize_subject(subject)] += 1

        if 'UNREAD' in labels:
            unread_count += 1

        if 'orulo.com.br' in domain:
            orulo_emails.append({
                'from': name,
                'subject': subject[:80],
                'date': headers.get('Date', ''),
            })

    # Top senders (top 15)
    top_senders = [
        {'name': sender_names.get(e, e), 'email': e, 'count': c}
        for e, c in by_sender.most_common(15)
    ]

    # Top domains (top 10)
    top_domains = [
        {'domain': d, 'count': c}
        for d, c in by_domain.most_common(10)
    ]

    # Subjects repetitivos (aparecem 3+ vezes)
    repetitive = [
        {'subject': s, 'count': c}
        for s, c in by_subject.most_common(20)
        if c >= 3
    ]

    # Emails Órulo (últimos 20)
    orulo_recent = orulo_emails[:20]

    digest = {
        'period': f'últimos 7 dias (desde {since})',
        'total_emails': total,
        'unread': unread_count,
        'top_senders': top_senders,
        'top_domains': top_domains,
        'repetitive_subjects': repetitive,
        'orulo_emails': orulo_recent,
        'orulo_count': len(orulo_emails),
    }

    OUTPUT_PATH.write_text(json.dumps(digest, ensure_ascii=False, indent=2))
    print(f"OK: {total} emails analisados")

if __name__ == '__main__':
    main()
