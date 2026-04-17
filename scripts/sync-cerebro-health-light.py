#!/usr/bin/env python3
"""
Health check: sync-cerebro — SCRIPT-ONLY version
Sem LLM. Verifica se o sync com GitHub está acontecendo.
Saída: 0 = OK, 1 = problema
Alerta Diego via Telegram se der problema.
"""
import datetime, subprocess, os, re, sys, http.client
import json

LOG = '/root/.openclaw/logs/sync-cerebro.log'
WORKSPACE = '/root/.openclaw/workspace'
WINDOW_HOURS = 25
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN') or os.environ.get('MORFEU_TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID_DIEGO', '8671853499')

def send_telegram(message):
    """Envia alerta via Telegram bot. Silencioso se TELEGRAM_TOKEN ausente."""
    if not TELEGRAM_TOKEN:
        print('WARN: TELEGRAM_TOKEN ausente — alerta não enviado', file=sys.stderr)
        return False
    try:
        conn = http.client.HTTPSConnection('api.telegram.org', timeout=10)
        url = f'/bot{TELEGRAM_TOKEN}/sendMessage'
        data = json.dumps({'chat_id': TELEGRAM_CHAT_ID, 'text': message, 'parse_mode': 'Markdown'}).encode()
        headers = {'Content-Type': 'application/json'}
        conn.request('POST', url, data, headers)
        resp = conn.getresponse()
        return resp.status == 200
    except Exception as e:
        print(f'ERRO Telegram: {e}')
        return False

def check_sync():
    """Verifica se sync recent."""
    if not os.path.exists(LOG):
        return 'ERRO: log não encontrado', 1

    with open(LOG) as f:
        lines = f.readlines()

    last_ts = None
    for l in reversed(lines):
        m = re.findall(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]', l)
        if m:
            last_ts = datetime.datetime.strptime(m[0], '%Y-%m-%d %H:%M')
            last_ts = last_ts.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3)))
            break

    if last_ts is None:
        return 'ERRO: nenhuma linha com data no log', 1

    now_epoch = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).timestamp()
    diff_h = int((now_epoch - last_ts.timestamp()) / 3600)

    if diff_h > WINDOW_HOURS:
        return f'🔴 Sync GitHub: último sync há {diff_h}h (máximo {WINDOW_HOURS}h)', 1

    return f'OK — sync rodou há {diff_h}h', 0

def check_git_dirty():
    """Verifica se working tree está suja."""
    r = subprocess.run(['git', 'diff-index', '--quiet', 'HEAD'], cwd=WORKSPACE, capture_output=True)
    return r.returncode != 0

def main():
    status_msg, sync_exit = check_sync()
    print(status_msg)

    if sync_exit != 0:
        send_telegram(f'⚠️ *Cron Job Alert*\n\n{status_msg}\n\n👉 Verificar: cron rodou? credencial expirou?')
        sys.exit(1)

    # Sync OK — verifica se tree está suja (só alerta, não bloqueia sync check)
    if check_git_dirty():
        send_telegram(f'⚠️ *Cron Job Alert*\n\n🔴 Alerta: Sync GitHub desativado\n\nATENÇÃO: há alterações locais sem commit\n\n👉 Verificar: cron job está rodando? Script funcionou?')
        sys.exit(1)  #tree suja = alerta, mas sync OK

    sys.exit(0)

if __name__ == '__main__':
    main()
