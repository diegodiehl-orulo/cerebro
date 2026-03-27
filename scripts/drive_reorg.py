#!/usr/bin/env python3
"""
Script para criar planilha WS_OPERATING_SYSTEM_H1_2026 no Google Drive
"""

import pickle
import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/root/.config/morfeu/secrets/drive_service_account.json'

def get_credentials():
    return Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def create_spreadsheet(service, title, folder_id=None):
    """Cria uma planilha Google Sheets."""
    body = {
        'name': title,
        'mimeType': 'application/vnd.google-apps.spreadsheet',
    }
    if folder_id:
        body['parents'] = [folder_id]
    
    try:
        file = service.files().create(body=body, fields='id, name, webViewLink').execute()
        print(f"✅ Criado: {title} (ID: {file.get('id')})")
        print(f"   Link: {file.get('webViewLink')}")
        return file
    except HttpError as e:
        print(f"❌ Erro ao criar {title}: {e}")
        return None

def create_document(service, title, folder_id=None):
    """Cria um documento Google Docs."""
    body = {
        'name': title,
        'mimeType': 'application/vnd.google-apps.document',
    }
    if folder_id:
        body['parents'] = [folder_id]
    
    try:
        file = service.files().create(body=body, fields='id, name, webViewLink').execute()
        print(f"✅ Criado: {title} (ID: {file.get('id')})")
        print(f"   Link: {file.get('webViewLink')}")
        return file
    except HttpError as e:
        print(f"❌ Erro ao criar {title}: {e}")
        return None

def create_folder(service, title, parent_id=None):
    """Cria uma pasta."""
    body = {
        'name': title,
        'mimeType': 'application/vnd.google-apps.folder',
    }
    if parent_id:
        body['parents'] = [parent_id]
    
    try:
        file = service.files().create(body=body, fields='id, name').execute()
        print(f"✅ Criada pasta: {title} (ID: {file.get('id')})")
        return file
    except HttpError as e:
        print(f"❌ Erro ao criar pasta {title}: {e}")
        return None

def delete_file(service, file_id):
    """Deleta um arquivo."""
    try:
        service.files().delete(fileId=file_id).execute()
        print(f"🗑️ Deletado: {file_id}")
        return True
    except HttpError as e:
        print(f"❌ Erro ao deletar {file_id}: {e}")
        return False

def main():
    print("🔨 Criando estrutura do Modelo V1 - Google Drive Órulo")
    print("=" * 60)
    
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    
    # IDs das pastas
    GOV_ID = '1hx7pJ62kMmk-YlMX3VzQ2nZe8YPATWRl'
    WORKSTREAMS_ID = '18X6LnY0epWKnblk7pr1nyvvdmEO4CfbL'
    TEMPLATES_ID = '1y-X29d-B0czGm_b_B1P7Zw_XsJ-BpD14'
    
    results = {
        'created': [],
        'deleted': [],
        'errors': []
    }
    
    # 1. DELETAR arquivos de teste em 05_TEMPLATES
    print("\n[1] Deletando arquivos de teste...")
    test_files = {
        'TESTE': '1y-X29d-B0czGm_b_B1P7Zw_XsJ-BpD14',  # Need actual ID
        'teste.txt': '1y-X29d-B0czGm_b_B1P7Zw_XsJ-BpD14'
    }
    
    # Listar arquivos em 05_TEMPLATES para pegar IDs
    query = f"'{TEMPLATES_ID}' in parents and trashed=false"
    response = service.files().list(q=query, pageSize=100, fields="files(id, name, mimeType)").execute()
    for f in response.get('files', []):
        print(f"   Encontrado: {f['name']} ({f['id']})")
        if f['name'] in ['TESTE', 'teste.txt']:
            delete_file(service, f['id'])
            results['deleted'].append({'name': f['name'], 'id': f['id']})
    
    # 2. CRIAR WS_OPERATING_SYSTEM_H1_2026 em 01_GOVERNANCA_GERAL
    print("\n[2] Criando WS_OPERATING_SYSTEM_H1_2026...")
    spreadsheet = create_spreadsheet(service, 'WS_OPERATING_SYSTEM_H1_2026', GOV_ID)
    if spreadsheet:
        results['created'].append({
            'name': spreadsheet['name'],
            'id': spreadsheet['id'],
            'link': spreadsheet.get('webViewLink'),
            'type': 'spreadsheet',
            'path': '01_GOVERNANCA_GERAL'
        })
    
    # 3. CRIAR TEMPLATES em 05_TEMPLATES
    print("\n[3] Criando templates...")
    
    # TEMPLATE_ONEPAGE_CHARTER
    doc1 = create_document(service, 'TEMPLATE_ONEPAGE_CHARTER', TEMPLATES_ID)
    if doc1:
        results['created'].append({
            'name': doc1['name'],
            'id': doc1['id'],
            'link': doc1.get('webViewLink'),
            'type': 'document',
            'path': '05_TEMPLATES'
        })
    
    # TEMPLATE_REUNIOES
    doc2 = create_document(service, 'TEMPLATE_REUNIOES', TEMPLATES_ID)
    if doc2:
        results['created'].append({
            'name': doc2['name'],
            'id': doc2['id'],
            'link': doc2.get('webViewLink'),
            'type': 'document',
            'path': '05_TEMPLATES'
        })
    
    # 4. CRIAR estrutura em cada WORKSTREAM
    print("\n[4] Criando estrutura nos Workstreams...")
    
    workstreams = {
        'WS1': '1wdlFacplD2h1wv2y-GSG3TgoyC2nKT8a',
        'WS2': '10d9t8smVInh1Pw1h0z6RWNQnkc6KjeTi',
        'WS3': '1OTtBlAYJQvst4mo_eMeFWH85gGeLP98Z',
        'WS4': '1HK3kLSedC3WAqbY8590Q3PrzxUC-C3Uy',
        'WS5': '1udL9HaJowwM8zzhAGR9wIlAjhPF0S2J1',
        'WS6': '1KeFybFL1qIv-CGnpR6qMZziO9WOT3AFI',
        'WS7': '1EqJezOFtZYFM7H9X8gcFd8KObdHD-YUA'
    }
    
    for ws_name, ws_id in workstreams.items():
        print(f"\n   {ws_name}:")
        
        # WSX_ONEPAGE_CHARTER
        doc = create_document(service, f'{ws_name}_ONEPAGE_CHARTER', ws_id)
        if doc:
            results['created'].append({
                'name': doc['name'],
                'id': doc['id'],
                'link': doc.get('webViewLink'),
                'type': 'document',
                'path': f'02_WORKSTREAMS/{ws_name}'
            })
        
        # WSX_REUNIOES (criar pasta se não existir)
        # Já existe 07_REUNIOES - verificar se está vazia
        query = f"'{ws_id}' in parents and trashed=false and name='07_REUNIOES'"
        response = service.files().list(q=query, fields="files(id, name)").execute()
        if not response.get('files'):
            folder = create_folder(service, '07_REUNIOES', ws_id)
    
    print("\n" + "=" * 60)
    print("✅ Reorganização concluída!")
    print(f"\nResumo: {len(results['created'])} criados, {len(results['deleted'])} deletados")
    
    # Salvar resultado
    with open('/root/.openclaw/workspace/scripts/drive_reorg_result.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResultado salvo em: /root/.openclaw/workspace/scripts/drive_reorg_result.json")

if __name__ == '__main__':
    main()
