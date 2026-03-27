#!/usr/bin/env python3
"""
Script para auditar completamente o Google Drive da Órulo
Detalha conteúdo de cada pasta
"""

import pickle
import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/root/.config/morfeu/secrets/drive_service_account.json'

def get_credentials():
    return Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def list_folder_details(service, folder_id, indent=0):
    """Lista conteúdo detalhado de uma pasta."""
    results = []
    
    query = f"'{folder_id}' in parents and trashed=false"
    response = service.files().list(
        q=query,
        pageSize=100,
        fields="files(id, name, mimeType, parents, size)",
        orderBy="folder, name"
    ).execute()
    
    files = response.get('files', [])
    
    for file in files:
        prefix = "  " * indent
        if file['mimeType'] == 'application/vnd.google-apps.folder':
            print(f"{prefix}📁 {file['name']}")
            results.append({
                'type': 'folder',
                'name': file['name'],
                'id': file['id'],
                'children': list_folder_details(service, file['id'], indent + 1)
            })
        else:
            icon = '📄' if 'document' in file['mimeType'] else '📊' if 'spreadsheet' in file['mimeType'] else '📋'
            size_kb = int(file.get('size', 0)) / 1024 if file.get('size') else 0
            print(f"{prefix}{icon} {file['name']} ({size_kb:.1f}KB)")
            results.append({
                'type': 'file',
                'name': file['name'],
                'id': file['id'],
                'mimeType': file['mimeType'],
                'size': size_kb
            })
    
    return results

def main():
    print("🔍 Auditoria detalhada do Google Drive - Órulo")
    print("=" * 60)
    
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    
    ROOT_ID = '1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM'
    
    # 1. Pasta raiz
    print("\n📂 RAIZ (ORULO)")
    print("-" * 40)
    root_contents = list_folder_details(service, ROOT_ID)
    
    # 2. 01_GOVERNANCA_GERAL
    print("\n📂 01_GOVERNANCA_GERAL")
    print("-" * 40)
    gov_id = '1hx7pJ62kMmk-YlMX3VzQ2nZe8YPATWRl'
    list_folder_details(service, gov_id)
    
    # 3. 05_TEMPLATES
    print("\n📂 05_TEMPLATES")
    print("-" * 40)
    templates_id = '1y-X29d-B0czGm_b_B1P7Zw_XsJ-BpD14'
    list_folder_details(service, templates_id)
    
    # 4. Cada Workstream
    workstreams = {
        'WS1': '1wdlFacplD2h1wv2y-GSG3TgoyC2nKT8a',
        'WS2': '10d9t8smVInh1Pw1h0z6RWNQnkc6KjeTi',
        'WS3': '1OTtBlAYJQvst4mo_eMeFWH85gGeLP98Z',
        'WS4': '1HK3kLSedC3WAqbY8590Q3PrzxUC-C3Uy',
        'WS5': '1udL9HaJowwM8zzhAGR9wIlAjhPF0S2J1',
        'WS6': '1KeFybFL1qIv-CGnpR6qMZziO9WOT3AFI',
        'WS7': '1EqJezOFtZYFM7H9X8gcFd8KObdHD-YUA'
    }
    
    for ws, ws_id in workstreams.items():
        print(f"\n📂 {ws}")
        print("-" * 40)
        list_folder_details(service, ws_id)
    
    print("\n" + "=" * 60)
    print("✅ Auditoria concluída!")

if __name__ == '__main__':
    main()
