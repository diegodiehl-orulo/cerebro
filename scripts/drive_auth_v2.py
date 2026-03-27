#!/usr/bin/env python3
"""
Script de autenticação Google Drive para Morfeu (método alternativo)
Executa OAuth sem necessidade de browser local
"""

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

# Escopos necessários
SCOPES = [
    'https://www.googleapis.com/auth/drive',
]

CLIENT_SECRETS_FILE = '/root/.config/gcalcli/client_secret.json'
TOKEN_FILE = '/root/.config/morfeu/drive_token.pkl'

def main():
    print("🔐 Autenticação Google Drive - Morfeu")
    print("=" * 60)
    print("Método: OAuth com servidor local")
    print()
    
    # Executa OAuth flow com servidor local
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    
    # Usa porta 8080fixed
    creds = flow.run_local_server(
        port=8080, 
        prompt='consent',
        bind_addr='0.0.0.0'
    )
    
    # Salva token
    with open(TOKEN_FILE, 'wb') as f:
        pickle.dump(creds, f)
    
    print("=" * 60)
    print("✅ Autenticação concluída!")
    print(f"   Token salvo em: {TOKEN_FILE}")
    print(f"   Scopes autorizados: {list(creds.scopes)}")

if __name__ == '__main__':
    main()
