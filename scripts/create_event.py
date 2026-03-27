#!/usr/bin/env python3
import pickle
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Carrega credenciais
creds = None
token_file = os.path.expanduser('~/.local/share/gcalcli/oauth')

if os.path.exists(token_file):
    with open(token_file, 'rb') as f:
        creds = pickle.load(f)

if not creds:
    print("❌ Sem credenciais")
    exit(1)

# API
service = build('calendar', 'v3', credentials=creds)

# Cria evento para amanhã (06/03/2026) às 20:00
# Amanhã = 2026-03-06
start_time = "2026-03-06T20:00:00"
end_time = "2026-03-06T21:00:00"

event = {
    'summary': 'teste openclaw',
    'start': {'dateTime': f'{start_time}-03:00', 'timeZone': 'America/Sao_Paulo'},
    'end': {'dateTime': f'{end_time}-03:00', 'timeZone': 'America/Sao_Paulo'},
}

created_event = service.events().insert(calendarId='primary', body=event).execute()
print(f"✅ Evento criado: {created_event['htmlLink']}")
