#!/usr/bin/env python3
"""
Script para listar estrutura do Google Drive da Órulo
Usa a API do Google Drive com Service Account
"""

import pickle
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Escopo necessário: Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

SERVICE_ACCOUNT_FILE = '/root/.config/morfeu/secrets/drive_service_account.json'

def get_credentials():
    """Carrega credenciais da Service Account."""
    return Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, 
        scopes=SCOPES
    )

def list_folder_contents(service, folder_id, indent=0, save_to=None):
    """Lista recursivamente o conteúdo de uma pasta."""
    results = []
    
    query = f"'{folder_id}' in parents and trashed=false"
    response = service.files().list(
        q=query,
        pageSize=100,
        fields="files(id, name, mimeType, parents)",
        orderBy="folder, name"
    ).execute()
    
    files = response.get('files', [])
    
    for file in files:
        prefix = "  " * indent
        if file['mimeType'] == 'application/vnd.google-apps.folder':
            print(f"{prefix}📁 {file['name']} (ID: {file['id']})")
            results.append({
                'type': 'folder',
                'name': file['name'],
                'id': file['id'],
                'indent': indent,
                'children': list_folder_contents(service, file['id'], indent + 1)
            })
        else:
            icon = '📄' if 'document' in file['mimeType'] else '📊' if 'spreadsheet' in file['mimeType'] else '📋'
            print(f"{prefix}{icon} {file['name']}")
            results.append({
                'type': 'file',
                'name': file['name'],
                'id': file['id'],
                'mimeType': file['mimeType'],
                'indent': indent
            })
    
    return results

def main():
    print("🔍 Mapeando estrutura do Google Drive - Órulo")
    print("=" * 60)
    
    # ID da pasta-raiz ORULO
    ROOT_ID = '1O0o94EdOUwH9y5ClovbIJZ-VfrQBwstM'
    
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    
    print(f"\n📂 Pasta-raiz: ORULO (ID: {ROOT_ID})\n")
    structure = list_folder_contents(service, ROOT_ID)
    
    print("\n" + "=" * 60)
    print("✅ Mapeamento concluído!")

if __name__ == '__main__':
    main()
