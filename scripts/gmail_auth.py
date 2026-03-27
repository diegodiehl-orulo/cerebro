#!/usr/bin/env python3
"""OAuth Gmail — gera token com escopo gmail.readonly"""
import json, pickle, socket
from pathlib import Path
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/calendar',
]
CLIENT_SECRET = Path('/root/.config/gcalcli/client_secret.json')
TOKEN_PATH = Path('/root/.config/morfeu/gmail_token.pkl')
TOKEN_PATH.parent.mkdir(parents=True, exist_ok=True)

# Encontrar porta livre
def find_free_port():
    with socket.socket() as s:
        s.bind(('', 0))
        return s.getsockname()[1]

port = find_free_port()
redirect_uri = f'http://localhost:{port}/'

flow = Flow.from_client_secrets_file(
    str(CLIENT_SECRET),
    scopes=SCOPES,
    redirect_uri=redirect_uri,
)

auth_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true',
    prompt='consent',
)

print(f"PORT={port}")
print(f"URL={auth_url}")

# Servidor local para capturar redirect
import http.server, urllib.parse, threading

code_received = {}

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        code_received['code'] = params.get('code', [None])[0]
        code_received['state'] = params.get('state', [None])[0]
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Autenticado! Pode fechar esta aba.")
        threading.Thread(target=self.server.shutdown).start()
    def log_message(self, *args): pass

server = http.server.HTTPServer(('', port), Handler)
server.serve_forever()

if code_received.get('code'):
    flow.fetch_token(code=code_received['code'])
    with open(TOKEN_PATH, 'wb') as f:
        pickle.dump(flow.credentials, f)
    print("TOKEN_OK")
else:
    print("TOKEN_FAIL")
