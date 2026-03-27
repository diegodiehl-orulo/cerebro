#!/usr/bin/env python3
import pickle
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Carrega credenciais
creds = None
token_file = os.path.expanduser('~/.local/share/gcalcli/oauth')

if os.path.exists(token_file):
    with open(token_file, 'rb') as f:
        creds = pickle.load(f)

if not creds:
    print("❌ Sem credenciais")
    exit(1)

# Testa API
service = build('calendar', 'v3', credentials=creds)

# Lista eventos de hoje
from datetime import datetime
today = datetime.now().strftime('%Y-%m-%d')
events_result = service.events().list(
    calendarId='primary',
    timeMin=f'{today}T00:00:00Z',
    maxResults=10,
    singleEvents=True,
    orderBy='startTime'
).execute()

events = events_result.get('items', [])
if not events:
    print("Nenhum evento hoje")
else:
    print(f"✅ Eventos de hoje ({today}):")
    for e in events:
        start = e['start'].get('dateTime', e['start'].get('date'))
        print(f"  {start} - {e['summary']}")
