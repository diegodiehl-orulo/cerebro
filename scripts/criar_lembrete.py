#!/usr/bin/env python3
"""
Cria lembretes no Google Calendar
"""
import pickle, json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import sys

TOKEN_FILE = '/root/.config/morfeu/gmail_token.pkl'

def get_calendar():
    with open(TOKEN_FILE, 'rb') as f:
        creds = pickle.load(f)
    return build('calendar', 'v3', credentials=creds)

def criar_lemmbrete(titulo, minutos_antes, data_hora, descricao=''):
    """Cria um lembrete (evento com reminder)"""
    service = get_calendar()
    
    # Calcula horário
    from dateutil import parser
    start = parser.parse(data_hora)
    end = start + timedelta(minutes=15)
    
    event = {
        'summary': titulo,
        'description': descricao,
        'start': {'dateTime': start.isoformat(), 'timeZone': 'America/Sao_Paulo'},
        'end': {'dateTime': end.isoformat(), 'timeZone': 'America/Sao_Paulo'},
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': minutos_antes}
            ]
        }
    }
    
    result = service.events().insert(
        calendarId='primary',
        body=event
    ).execute()
    
    return result.get('htmlLink')

def listar_proximos():
    """Lista próximos eventos com lembretes"""
    service = get_calendar()
    
    now = datetime.now().isoformat() + '-03:00'
    
    events = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    return events.get('items', [])

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python3 criar_lembrete.py 'titulo' 'minutos' 'YYYY-MM-DD HH:MM' [descricao]")
        sys.exit(1)
    
    titulo = sys.argv[1]
    minutos = int(sys.argv[2])
    quando = sys.argv[3]
    desc = sys.argv[4] if len(sys.argv) > 4 else ''
    
    link = criar_lemmbrete(titulo, minutos, quando, desc)
    print(f"✅ Lembrete criado: {link}")
