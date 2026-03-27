#!/usr/bin/env python3
"""
Cria eventos de viagem no Google Calendar
"""
import pickle
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

TOKEN_FILE = '/root/.config/morfeu/gmail_token.pkl'

VIAGENS = [
    # Ciclo 1
    {"data": "2026-03-04", "cidade": "Vitória", "estado": "ES", "tipo": "Solo"},
    {"data": "2026-03-18", "cidade": "Curitiba", "estado": "PR", "tipo": "Solo"},
    {"data": "2026-04-14", "cidade": "Porto Alegre", "estado": "RS", "tipo": "Pareado"},
    {"data": "2026-04-16", "cidade": "Capão da Canoa", "estado": "RS", "tipo": "Pareado"},
    {"data": "2026-05-05", "cidade": "João Pessoa", "estado": "PB", "tipo": "Pareado"},
    {"data": "2026-05-07", "cidade": "Recife", "estado": "PE", "tipo": "Pareado"},
    {"data": "2026-05-12", "cidade": "São Paulo", "estado": "SP", "tipo": "Pareado"},
    {"data": "2026-05-14", "cidade": "Campinas", "estado": "SP", "tipo": "Pareado"},
    {"data": "2026-05-27", "cidade": "Goiânia", "estado": "GO", "tipo": "Solo"},
    {"data": "2026-06-16", "cidade": "Florianópolis", "estado": "SC", "tipo": "Pareado"},
    {"data": "2026-06-18", "cidade": "Vale do Itajaí", "estado": "SC", "tipo": "Pareado"},
    {"data": "2026-07-08", "cidade": "Rio de Janeiro", "estado": "RJ", "tipo": "Solo"},
    # Ciclo 2
    {"data": "2026-08-18", "cidade": "Porto Alegre", "estado": "RS", "tipo": "Pareado"},
    {"data": "2026-08-20", "cidade": "Capão da Canoa", "estado": "RS", "tipo": "Pareado"},
    {"data": "2026-08-26", "cidade": "Curitiba", "estado": "PR", "tipo": "Solo"},
    {"data": "2026-09-01", "cidade": "João Pessoa", "estado": "PB", "tipo": "Pareado"},
    {"data": "2026-09-03", "cidade": "Recife", "estado": "PE", "tipo": "Pareado"},
    {"data": "2026-09-15", "cidade": "São Paulo", "estado": "SP", "tipo": "Pareado"},
    {"data": "2026-09-17", "cidade": "Campinas", "estado": "SP", "tipo": "Pareado"},
    {"data": "2026-09-23", "cidade": "Goiânia", "estado": "GO", "tipo": "Solo"},
    {"data": "2026-11-04", "cidade": "Vitória", "estado": "ES", "tipo": "Solo"},
    {"data": "2026-11-10", "cidade": "Florianópolis", "estado": "SC", "tipo": "Pareado"},
    {"data": "2026-11-12", "cidade": "Vale do Itajaí", "estado": "SC", "tipo": "Pareado"},
    {"data": "2026-11-25", "cidade": "Rio de Janeiro", "estado": "RJ", "tipo": "Solo"},
]

def get_calendar():
    with open(TOKEN_FILE, 'rb') as f:
        creds = pickle.load(f)
    return build('calendar', 'v3', credentials=creds)

def criar_evento(service, data, cidade, estado, tipo):
    from datetime import datetime
    
    # Parse date
    dt = datetime.strptime(data, "%Y-%m-%d")
    
    start = dt.replace(hour=7, minute=0)
    end = dt.replace(hour=14, minute=0)
    
    event = {
        'summary': f'Workshop {cidade}',
        'location': f'{cidade}, {estado}',
        'description': f'Tipo: {tipo}\nViagem de campo - Órulo',
        'start': {'dateTime': start.isoformat(), 'timeZone': 'America/Sao_Paulo'},
        'end': {'dateTime': end.isoformat(), 'timeZone': 'America/Sao_Paulo'},
    }
    
    result = service.events().insert(
        calendarId='primary',
        body=event
    ).execute()
    
    return f"✅ {data} - {cidade}/{estado} - {tipo}"

def main():
    service = get_calendar()
    
    print(f"Criando {len(VIAGENS)} eventos...")
    print()
    
    for viagem in VIAGENS:
        try:
            resultado = criar_evento(
                service,
                viagem['data'],
                viagem['cidade'],
                viagem['estado'],
                viagem['tipo']
            )
            print(resultado)
        except Exception as e:
            print(f"❌ {viagem['data']} - {viagem['cidade']}: {e}")
    
    print()
    print("🎉 Concluído!")

if __name__ == '__main__':
    main()
