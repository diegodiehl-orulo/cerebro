#!/usr/bin/env python3
"""
Script para gerar refresh token do Google OAuth.
Execute no seu computador local (onde tem navegador).

Instalar dependências:
pip install google-auth google-auth-oauthlib

Executar:
python3 generate_refresh_token.py
"""

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Escopos necessários
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/docs',
    'https://www.googleapis.com/auth/spreadsheets'
]

# Client secrets - baixe do Google Cloud Console
CLIENT_SECRETS_FILE = 'client_secret.json'

def main():
    print("🔐 Gerando Refresh Token...")
    print("=" * 50)
    
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)
    
    # Isso vai abrir o navegador para você autorizar
    credentials = flow.run_local_server(port=0, prompt='consent')
    
    # Salva o refresh token
    print("\n✅ Autorização concedida!")
    print(f"Refresh Token: {credentials.refresh_token}")
    print("\n" + "=" * 50)
    print("COPIE O REFRESH TOKEN ACIMA E COLE NO OPENCLAW")
    print("=" * 50)

if __name__ == '__main__':
    main()
