#!/usr/bin/env python3
"""
Smart Email Scan — Identifica emails importantes e sugere tarefas
Classifica por: URGENTE | CONTRATO | PROPOSTA | REUNIÃO | TIME
"""
import pickle, json, os, re
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from pathlib import Path

TOKEN_FILE = '/root/.config/morfeu/gmail_token.pkl'
OUTPUT_FILE = '/root/.config/morfeu/smart_email_scan.json'

# TIME ÓRULO — Lista completa de pessoas importantes
TIME_ORULO = {
    # Coordenação e Comercial
    'gustavo.torres@orulo.com.br': {'nome': 'Gustavo Torres', 'papel': 'Coordenador Comercial'},
    'jade.rosa@orulo.com.br': {'nome': 'Jade Rosa', 'papel': 'BDR'},
    'mirla.menezes@orulo.com.br': {'nome': 'Mirla Menezes', 'papel': 'BDR'},
    'joaovitor.silva@orulo.com.br': {'nome': 'João Vitor', 'papel': 'Closer'},
    'luan.souza@orulo.com.br': {'nome': 'Luan Souza', 'papel': 'Closer'},
    
    # Sócios Locais
    'luiz.zanella@orulo.com.br': {'nome': 'Luiz Gustavo Zanella', 'papel': 'Sócio-Local Curitiba'},
    'pkneip@orulo.com.br': {'nome': 'Pedro Kneip', 'papel': 'Sócio-Local Vitória'},
    
    # Liderança e Operação
    'felipe@orulo.com.br': {'nome': 'Felipe Goettems', 'papel': 'Fundador/Produtos Financeiros'},
    'alejandro@orulo.com.br': {'nome': 'Alejandro', 'papel': 'CTO'},
    'eduardo@orulo.com.br': {'nome': 'Eduardo', 'papel': 'COO'},
    'marcelo@orulo.com.br': {'nome': 'Marcelo Rodrigues', 'papel': 'Diretor Ops/CS'},
    'mayumi@orulo.com.br': {'nome': 'Mayumi', 'papel': 'Marketing/Comunidade'},
    'ester.rodrigues@orulo.com.br': {'nome': 'Ester Elisa', 'papel': 'Comunicação Corretores'},
}

# Config
IMPORTANT_SENDERS = list(TIME_ORULO.keys())

# Remetentes e padrões a IGNORAR (mensagens automáticas do sistema)
IGNORE_PATTERNS = [
    'noreply@',
    'no-reply@', 
    'notification@',
    'notifications@',
    '[orulo] nova proposta',
    'nova proposta de',
    'proposta automática',
    'noreply@zenvia',
    'noreply@whatsapp',
    '@mailgun.org',
    '@sendgrid.net',
]

KEYWORDS = {
    'URGENTE': ['urgente', 'prioridade', 'crítico', 'bloqueio', 'imediato', 'problema crítico', 'erro'],
    'SEGUIR': ['follow-up', 'lembrete', 'não respondeu', 'em aberto', 'pendente', 'aguardo', 'sem resposta'],
    'PROPOSTA': ['proposta', 'proposta comercial', 'orçamento', 'proposal', 'valor', 'cotação'],
    'REUNIÃO': ['reunião', 'reuniao', 'meeting', 'call', 'videoconferência', 'google meet', 'zoom', 'meet.google.com'],
    'CONTRATO': ['contrato', 'assinatura', 'clicksign', 'adobe sign', 'assinar', 'documento', 'enviado para assinatura'],
}

def get_gmail():
    with open(TOKEN_FILE, 'rb') as f:
        creds = pickle.load(f)
    return build('gmail', 'v1', credentials=creds)

def classify_email(subject, from_email, snippet=''):
    text = f"{subject} {snippet} {from_email}".lower()
    
    # Ignorar mensagens automáticas
    for pattern in IGNORE_PATTERNS:
        if pattern.lower() in text:
            return None
    
    # Prioridade máxima: urgência
    for kw in KEYWORDS['URGENTE']:
        if kw in text:
            return 'URGENTE'
    
    # Contratos
    for kw in KEYWORDS['CONTRATO']:
        if kw in text:
            return 'CONTRATO'
    
    # Propostas
    for kw in KEYWORDS['PROPOSTA']:
        if kw in text:
            return 'PROPOSTA'
    
    # Reuniões
    for kw in KEYWORDS['REUNIÃO']:
        if kw in text:
            return 'REUNIÃO'
    
    # TIME (prioridade mais baixa)
    for imp in IMPORTANT_SENDERS:
        if imp.lower() in from_email.lower():
            return 'TIME'
    
    return None

def format_output(important):
    """Formata saída organizada por classificação"""
    summary = {
        'URGENTE': [],
        'CONTRATO': [],
        'PROPOSTA': [],
        'REUNIÃO': [],
        'TIME': [],
    }
    
    priority_order = {'URGENTE': 0, 'CONTRATO': 1, 'PROPOSTA': 2, 'REUNIÃO': 3, 'TIME': 4}
    
    for item in important:
        cat = item['classification']
        emoji = {'URGENTE': '🔴', 'CONTRATO': '📝', 'PROPOSTA': '💰', 'REUNIÃO': '📅', 'TIME': '👤'}.get(cat, '•')
        
        # Enrich com info do time
        sender_info = TIME_ORULO.get(item['from_email'], {})
        nome = sender_info.get('nome', item['from_name'])
        papel = sender_info.get('papel', '')
        
        summary[cat].append({
            'emoji': emoji,
            'nome': nome,
            'papel': papel,
            'subject': item['subject'],
            'date': item['date'][:16],  # Data resumida
            'link': item['link']
        })
    
    return summary

def main():
    service = get_gmail()
    
    # Últimas 48h
    cutoff = (datetime.now() - timedelta(hours=48)).strftime('%Y/%m/%d')
    
    results = service.users().messages().list(
        userId='me',
        q=f'after:{cutoff} -in:trash -in:spam -in:chats',
        maxResults=100
    ).execute()
    
    messages = results.get('messages', [])
    important = []
    
    for msg in messages[:50]:
        msg_data = service.users().messages().get(
            userId='me', 
            id=msg['id'], 
            format='full',
            metadataHeaders=['From', 'Subject', 'Date']
        ).execute()
        
        headers = {h['name']: h['value'] for h in msg_data['payload']['headers']}
        from_hdr = headers.get('From', '')
        subject = headers.get('Subject', '(sem assunto)')
        date = headers.get('Date', '')
        
        match = re.search(r'<(.+?)>|^(.+?@.+?)$', from_hdr)
        sender_email = match.group(1) or match.group(2) if match else from_hdr
        sender_name = re.sub(r'<.+?>', '', from_hdr).strip()
        
        classification = classify_email(subject, sender_email)
        
        if classification:
            important.append({
                'id': msg['id'],
                'classification': classification,
                'from_name': sender_name[:40],
                'from_email': sender_email[:50],
                'subject': subject[:100],
                'date': date[:40],
                'link': f"https://mail.google.com/mail/u/0/#inbox/{msg['id']}"
            })
    
    # Ordena
    priority_order = {'URGENTE': 0, 'CONTRATO': 1, 'PROPOSTA': 2, 'REUNIÃO': 3, 'TIME': 4}
    important.sort(key=lambda x: priority_order.get(x['classification'], 99))
    
    # Formata saída
    formatted = format_output(important)
    
    # Gera resumo
    total = {k: len(v) for k, v in formatted.items()}
    
    output = {
        'generated': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'period_hours': 48,
        'total_emails': len(messages),
        'important_count': len(important),
        'summary': total,
        'items': formatted,
    }
    
    Path(OUTPUT_FILE).write_text(json.dumps(output, ensure_ascii=False, indent=2))
    
    # Printa formato bonito
    print("\n" + "="*60)
    print(f"📧 SMART EMAIL SCAN — {output['generated']}")
    print("="*60)
    print(f"\n📊 Resumo: {len(messages)} emails | {len(important)} importantes\n")
    
    emojis = {'URGENTE': '🔴', 'CONTRATO': '📝', 'PROPOSTA': '💰', 'REUNIÃO': '📅', 'TIME': '👤'}
    
    for cat, items in formatted.items():
        if items:
            print(f"{emojis.get(cat, '•')} {cat}: {len(items)}")
            for item in items[:5]:  # Max 5 por categoria
                print(f"   • {item['nome'][:25]}")
                print(f"     {item['subject'][:50]}")
            if len(items) > 5:
                print(f"   ... e mais {len(items)-5}")
            print()
    
    return output

if __name__ == '__main__':
    main()
