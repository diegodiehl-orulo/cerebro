#!/usr/bin/env python3
"""
Google Calendar CLI para Morfeu
用法:
  python3 gcal_morfeu.py list          # Lista eventos de hoje
  python3 gcal_morfeu.py tomorrow       # Lista eventos de amanhã
  python3 gcal_morfeu.py add "titulo" YYYY-MM-DD HH:MM
"""
import pickle, os, sys
from googleapiclient.discovery import build
from datetime import datetime, timedelta

TOKEN_FILE = os.path.expanduser('~/.local/share/gcalcli/oauth')

def get_service():
    if not os.path.exists(TOKEN_FILE):
        print("❌ Sem credenciais OAuth")
        return None
    with open(TOKEN_FILE, 'rb') as f:
        creds = pickle.load(f)
    return build('calendar', 'v3', credentials=creds)

def list_events(date_str=None, days=1):
    service = get_service()
    if not service:
        return
    
    if date_str:
        start = datetime.strptime(date_str, '%Y-%m-%d')
    else:
        start = datetime.now()
    
    for i in range(days):
        day = start + timedelta(days=i)
        day_str = day.strftime('%Y-%m-%d')
        
        events = service.events().list(
            calendarId='primary',
            timeMin=f'{day_str}T00:00:00Z',
            timeMax=f'{day_str}T23:59:59Z',
            singleEvents=True,
            orderBy='startTime'
        ).execute().get('items', [])
        
        print(f"\n📅 {day.strftime('%d/%m/%Y')} ({day.strftime('%A')}):")
        if not events:
            print("  Nenhum evento")
        for e in events:
            start_time = e['start'].get('dateTime', '')[:16].replace('T', ' ')
            print(f"  {start_time} - {e['summary']}")

def add_event(title, date_str, time_str, duration=1):
    service = get_service()
    if not service:
        return
    
    start_dt = f"{date_str}T{time_str}:00"
    end_dt = datetime.strptime(start_dt, "%Y-%m-%dT%H:%M:%S") + timedelta(hours=duration)
    end_dt = end_dt.strftime("%Y-%m-%dT%H:%M:%S")
    
    event = {
        'summary': title,
        'start': {'dateTime': f'{start_dt}-03:00', 'timeZone': 'America/Sao_Paulo'},
        'end': {'dateTime': f'{end_dt}-03:00', 'timeZone': 'America/Sao_Paulo'},
    }
    
    created = service.events().insert(calendarId='primary', body=event).execute()
    print(f"✅ Criado: {created['htmlLink']}")

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'today'
    
    if cmd == 'today':
        list_events()
    elif cmd == 'tomorrow':
        list_events(date_str=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))
    elif cmd == 'list' and len(sys.argv) > 2:
        list_events(date_str=sys.argv[2], days=int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    elif cmd == 'add' and len(sys.argv) >= 5:
        # python3 gcal_morfeu.py add "titulo" 2026-03-06 20:00
        add_event(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(__doc__)
