#!/usr/bin/env python3
"""
Health check: sync-cerebro
Verifica se o sync com GitHub está acontecendo
Saída: 0 = OK, 1 = problema
"""
import datetime, subprocess, os, re, sys

LOG = '/root/.openclaw/workspace/logs/sync-cerebro.log'
WORKSPACE = '/root/.openclaw/workspace'
WINDOW_HOURS = 25

try:
    # 1. Log existe?
    if not os.path.exists(LOG):
        print('ERRO: log não encontrado')
        sys.exit(1)

    with open(LOG) as f:
        lines = f.readlines()

    # 2. Procurar última linha com [YYYY-MM-DD HH:MM] — formato novo do sync-cerebro.sh
    last_ts = None
    for l in reversed(lines):
        m = re.findall(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]', l)
        if m:
            last_ts = datetime.datetime.strptime(m[0], '%Y-%m-%d %H:%M')
            last_ts = last_ts.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-3)))
            break

    # 3. Se não achou formato novo, cairback para mês abreviado
    if last_ts is None:
        for l in reversed(lines):
            l = l.strip()
            if any(mon in l for mon in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']):
                last_line = re.sub(r'[\[\]]', '', l)
                parts = last_line.split()
                if len(parts) >= 6:
                    parts[4] = parts[4] + '00'
                    ts_str = ' '.join(parts[:6])
                    last_ts = datetime.datetime.strptime(ts_str, '%a %b %d %H:%M:%S %z %Y')
                    break

    if last_ts is None:
        print('ERRO: nenhuma linha com data no log')
        sys.exit(1)

    now_epoch = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).timestamp()
    diff_h = int((now_epoch - last_ts.timestamp()) / 3600)

    if diff_h > WINDOW_HOURS:
        print(f'ERRO: último sync há {diff_h}h (máximo {WINDOW_HOURS}h)')
        sys.exit(1)

    # 4. Working tree clean?
    r = subprocess.run(['git', 'diff-index', '--quiet', 'HEAD'], cwd=WORKSPACE, capture_output=True)
    if r.returncode != 0:
        print('ATENÇÃO: há alterações locais sem commit')
        sys.exit(1)

    print(f'OK — sync rodou há {diff_h}h')
    sys.exit(0)

except Exception as e:
    print(f'ERRO: {e}')
    sys.exit(1)
