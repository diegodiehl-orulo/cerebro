#!/usr/bin/env python3
"""
Script OAuth para Google Drive - Método manual
"""

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRETS_FILE = '/root/.config/gcalcli/client_secret.json'
TOKEN_FILE = '/root/.config/morfeu/drive_token.pkl'

def main():
    print("🔐 OAuth Google Drive - Método Manual")
    print("=" * 60)
    
    # Verifica se token já existe
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as f:
            creds = pickle.load(f)
        if creds and creds.valid:
            print("✅ Token válido já existe!")
            return
        elif creds and creds.expired and creds.refresh_token:
            print("🔄 Token expirado. Tentando refresh...")
            try:
                creds.refresh(None)
                with open(TOKEN_FILE, 'wb') as f:
                    pickle.dump(creds, f)
                print("✅ Token refreshado!")
                return
            except Exception as e:
                print(f"⚠️ Refresh falhou: {e}")
    
    # Criar flow
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    
    # Pegar URL de autorização SEM abrir browser
    auth_url, _ = flow.authorization_url(prompt='consent')
    
    print("\n📋 INSTRUÇÕES:")
    print("-" * 60)
    print("1. Copie a URL abaixo e abra no seu navegador:")
    print(f"\n{auth_url}\n")
    print("2. Faça login e permita o acesso")
    print("3. Você será redirecionado para uma página de erro/localhost")
    print("4. Copie a URL COMPLETA da barra de endereços (após '?code=')")
    print("5. Cole abaixo")
    print("-" * 60)
    
    code = input("\nCole o código aqui: ").strip()
    
    # Trocar código por token
    flow.fetch_token(code=code)
    creds = flow.credentials
    
    # Salvar token
    with open(TOKEN_FILE, 'wb') as f:
        pickle.dump(creds, f)
    
    print("\n✅ Token salvo com sucesso!")
    print(f"   Arquivo: {TOKEN_FILE}")

if __name__ == '__main__':
    main()
