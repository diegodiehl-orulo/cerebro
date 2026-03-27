#!/usr/bin/env python3
"""OAuth Gmail — adiciona escopo gmail.send ao token existente"""
import pickle, socket, threading, http.server, urllib.parse
from pathlib import Path
from google_auth_oauthlib.flow import Flow

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/calendar',
]
CLIENT_SECRET = Path('/root/.config/gcalcli/client_secret.json')
TOKEN_PATH    = Path('/root/.config/morfeu/gmail_token.pkl')

def find_free_port():
    with socket.socket() as s:
        s.bind(('', 0))
        return s.getsockname()[1]

port = find_free_port()
redirect_uri = f'http://localhost:{port}/'

flow = Flow.from_client_secrets_file(str(CLIENT_SECRET), scopes=SCOPES, redirect_uri=redirect_uri)
auth_url, state = flow.authorization_url(access_type='offline', prompt='consent')

print(f"PORT={port}")
print(f"URL={auth_url}")

code_received = {}

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        code_received['code'] = params.get('code', [None])[0]
        self.send_response(200); self.end_headers()
        self.wfile.write(b"Autorizado! Pode fechar.")
        threading.Thread(target=self.server.shutdown).start()
    def log_message(self, *args): pass

http.server.HTTPServer(('', port), Handler).serve_forever()

if code_received.get('code'):
    flow.fetch_token(code=code_received['code'])
    with open(TOKEN_PATH, 'wb') as f:
        pickle.dump(flow.credentials, f)
    print("TOKEN_OK")
