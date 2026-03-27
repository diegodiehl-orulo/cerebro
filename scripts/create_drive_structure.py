#!/usr/bin/env python3
"""
create_drive_structure.py — Versão simplificada
Cria estrutura de pastas no Google Drive de forma idempotente.

Uso:
  python3 create_drive_structure.py --tree '[
    {"name": "2026", "parent_id": "ROOT"},
    {"name": "H1_2026", "parent_id": "2026"},
    {"name": "03_Marco", "parent_id": "H1_2026"}
  ]'
  
  python3 create_drive_structure.py --file estrutura.json
"""

import json
import os
import sys
import argparse
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SERVICE_ACCOUNT_FILE = '/root/.config/morfeu/secrets/drive_service_account.json'
DEFAULT_ROOT_ID = '1vtEur0eJihRF1qYddVBeiRea_Dol5Ccl'

class DriveManager:
    def __init__(self):
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/drive'])
        self.service = build('drive', 'v3', credentials=creds)
    
    def find_folder(self, name, parent_id):
        """Busca pasta por nome e pai."""
        query = f"name='{name}' and '{parent_id}' in parents and trashed=false"
        results = self.service.files().list(
            q=query, spaces='drive', fields='files(id, name)').execute()
        return results.get('files', [])
    
    def create_folder(self, name, parent_id):
        """Cria pasta."""
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_id]
        }
        return self.service.files().create(
            body=file_metadata, fields='id, name').execute()
    
    def get_or_create(self, name, parent_id):
        """Get or create — idempotente."""
        existing = self.find_folder(name, parent_id)
        if existing:
            return {'id': existing[0]['id'], 'name': name, 'status': 'already_exists'}
        
        created = self.create_folder(name, parent_id)
        return {'id': created['id'], 'name': name, 'status': 'created'}
    
    def create_structure(self, tree, root_id):
        """Cria estrutura completa."""
        # Mapeia referências de nome para ID
        name_to_id = {'ROOT': root_id}
        result = {'created': [], 'errors': []}
        
        for item in tree:
            name = item['name']
            parent_ref = item.get('parent_id', 'ROOT')
            
            # Resolve parent_id
            if parent_ref in name_to_id:
                parent_id = name_to_id[parent_ref]
            else:
                result['errors'].append({
                    'name': name,
                    'error': f"Pai '{parent_ref}' não encontrado"
                })
                continue
            
            # Cria ou pega existente
            try:
                r = self.get_or_create(name, parent_id)
                name_to_id[name] = r['id']
                result['created'].append(r)
            except Exception as e:
                result['errors'].append({'name': name, 'error': str(e)})
        
        return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root-id', default=DEFAULT_ROOT_ID)
    parser.add_argument('--tree', help='JSON array')
    parser.add_argument('--file', help='JSON file')
    args = parser.parse_args()
    
    # Carrega tree
    if args.tree:
        tree = json.loads(args.tree)
    elif args.file:
        with open(args.file) as f:
            tree = json.load(f)
    else:
        print("Use --tree ou --file")
        sys.exit(1)
    
    dm = DriveManager()
    result = dm.create_structure(tree, args.root_id)
    
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    if result['errors']:
        sys.exit(1)


if __name__ == '__main__':
    main()
