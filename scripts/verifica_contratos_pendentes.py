#!/usr/bin/env python3
"""
Verifica emails de plataformas de assinatura de documentos
Clicksign, DocuSign, Adobe Sign, Bitrix24
VERSÃO REFINADA - Status real do documento
"""
import pickle, json, os, re
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from pathlib import Path

TOKEN_FILE = '/root/.config/morfeu/gmail_token.pkl'
OUTPUT_FILE = '/root/.config/morfeu/contratos_pendentes.json'

def get_gmail():
    with open(TOKEN_FILE, 'rb') as f:
        creds = pickle.load(f)
    return build('gmail', 'v1', credentials=creds)

def get_status(subject, snippet):
    """Determina o status real do documento"""
    content = (subject + ' ' + snippet).lower()
    
    # Status de conclusão
    if any(kw in content for kw in ['documento assinado', 'signed', 'completed', 'concluído', 'concluido', 'assinatura confirmada']):
        return 'assinado'
    
    # Status cancelado
    if 'documento cancelado' in content or 'cancelado' in content:
        return 'cancelado'
    
    # Se tem token/code e não é assinado/cancelado = pendente
    if any(kw in content for kw in ['token:', 'código para', 'assinar documento', 'solicitação de assinatura', 'para assinar']):
        return 'pendente'
    
    return 'outros'

def extract_client(subject):
    """Extrai nome do cliente/doc do assunto"""
    # Remove prefixos comuns
    text = subject
    text = re.sub(r'^(Assinar documento:|Token:|Documento cancelado:|Documento assinado:)\s*', '', text, flags=re.IGNORECASE)
    # Pega primeira parte relevante
    if ' - ' in text:
        return text.split(' - ')[0].strip()
    return text[:60].strip()

def main():
    service = get_gmail()
    
    # Últimos 30 dias
    cutoff = (datetime.now() - timedelta(days=30)).strftime('%Y/%m/%d')
    
    # Query: emails de plataformas de assinatura
    query = f'''
    (clicksign OR docusign OR adobesign OR "bitrix24.sign" OR "brysigner")
    after:{cutoff} -in:trash -in:spam
    '''
    
    results = service.users().messages().list(
        userId='me',
        q=query.strip(),
        maxResults=100
    ).execute()
    
    messages = results.get('messages', [])
    
    contratos = {'assinado': [], 'cancelado': [], 'pendente': [], 'outros': []}
    
    for msg in messages:
        msg_data = service.users().messages().get(
            userId='me', 
            id=msg['id'], 
            format='full'
        ).execute()
        
        headers = {h['name']: h['value'] for h in msg_data['payload']['headers']}
        
        subject = headers.get('Subject', '(sem assunto)')
        from_hdr = headers.get('From', '')
        date = headers.get('Date', '')
        snippet = msg_data.get('snippet', '')
        
        # Extrai email do remetente
        match = re.search(r'<(.+?)>|^(.+?@.+?)$', from_hdr)
        email = match.group(1) or match.group(2) if match else from_hdr
        
        # Determina plataforma
        content = (subject + ' ' + snippet).lower()
        if 'clicksign' in content:
            plataforma = 'clicksign'
        elif 'bitrix24' in content:
            plataforma = 'bitrix'
        elif 'docusign' in content:
            plataforma = 'docusign'
        elif 'brysigner' in content:
            plataforma = 'brysigner'
        else:
            plataforma = 'outros'
        
        # Status
        status = get_status(subject, snippet)
        cliente = extract_client(subject)
        
        item = {
            'id': msg['id'],
            'data': date[:16],
            'remetente': email,
            'plataforma': plataforma,
            'documento': cliente,
            'assunto': subject[:100],
            'snippet': snippet[:100]
        }
        
        contratos[status].append(item)
    
    # Salva resultado refinado
    output = {
        'generated': datetime.now().isoformat(),
        'periodo': f'{cutoff} a {datetime.now().strftime("%Y/%m/%d")}',
        'total_encontrados': len(messages),
        'resumo': {
            'assinados': len(contratos['assinado']),
            'cancelados': len(contratos['cancelado']),
            'pendentes': len(contratos['pendente']),
            'outros': len(contratos['outros'])
        },
        'contratos': contratos
    }
    
    Path(OUTPUT_FILE).write_text(json.dumps(output, ensure_ascii=False, indent=2))
    
    print(f"✅ Análise concluída")
    print(f"📝 {len(contratos['assinado'])} assinados")
    print(f"❌ {len(contratos['cancelado'])} cancelados")
    print(f"⏳ {len(contratos['pendente'])} pendentes")
    
    return output

if __name__ == '__main__':
    main()
