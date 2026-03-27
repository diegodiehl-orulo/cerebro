#!/usr/bin/env python3
"""
Script de autenticação Google Drive para Morfeu
Executar: python3 /root/.openclaw/workspace/scripts/drive_auth.py
"""

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

# Escopos necessários: Gmail, Calendar, Drive
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/drive',  # Drive incluso!
]

CLIENT_SECRETS_FILE = '/root/.config/gcalcli/client_secret.json'
TOKEN_FILE = '/root/.config/morfeu/drive_token.pkl'

def main():
    print("🔐 Autenticação Google — Morfeu (Drive + Gmail + Calendar)")
    print("=" * 60)
    
    creds = None
    
    # Verifica se token já existe
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as f:
            creds = Credentials.from_authorized_user_info(creds.to_json(), SCOPES) if hasattr(creds, 'to_json') else pickle.load(f)
        
        # Recarregar corretamente
        with open(TOKEN_FILE, 'rb') as f:
            creds = pickle.load(f)
        
        if creds and creds.valid:
            print("✅ Token válido encontrado!")
            print(f"   Scopes: {creds.scopes}")
            return
        elif creds and creds.expired and creds.refresh_token:
            print("🔄 Token expirado. Tentando refresh...")
            try:
                creds.refresh(None)
                print("✅ Token refreshado!")
                with open(TOKEN_FILE, 'w') as f:
                    f.write(creds.to_json())
                return
            except Exception as e:
                print(f"⚠️ Refresh falhou: {e}")
                print("   Precisamos de nova autorização...")
    
    # Executa OAuth flow
    print("🔑 Abrindo navegador para autorização...")
    print(f"   Escopos: {SCOPES}")
    
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    creds = flow.run_local_server(port=0, prompt='consent')
    
    # Salva token
    with open(TOKEN_FILE, 'wb') as f:
        pickle.dump(creds, f)
    
    print("=" * 60)
    print("✅ Autenticação concluída!")
    print(f"   Token salvo em: {TOKEN_FILE}")
    print(f"   Scopes autorizados: {creds.scopes}")

if __name__ == '__main__':
    main()
