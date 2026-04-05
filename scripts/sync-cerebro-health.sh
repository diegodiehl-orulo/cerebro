#!/usr/bin/env python3
"""
Health check: sync-cerebro
Verifica se o sync com GitHub está acontecendo
Saída: 0 = OK, 1 = problema
"""
import datetime, subprocess, os, re, sys

LOG = '/root/.openclaw/logs/sync-cerebro.log'
WORKSPACE = '/root/.openclaw/workspace'
WINDOW_HOURS = 25

try:
    # 1. Log existe?
    if not os.path.exists(LOG):
        print('ERRO: log não encontrado')
        sys.exit(1)

    # 2. Última linha com data
    with open(LOG) as f:
        lines = f.readlines()

    last_line = ''
    for l in reversed(lines):
        l = l.strip()
        if any(m in l for m in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']):
            last_line = l
            break

    if not last_line:
        print('ERRO: nenhuma linha com data no log')
        sys.exit(1)

    # 3. Parse data
    last_line = re.sub(r'[\[\]]', '', last_line)
    parts = last_line.split()
    parts[4] = parts[4] + '00'  # -03 -> -0300
    ts_str = ' '.join(parts[:6])
    last_epoch = datetime.datetime.strptime(ts_str, '%a %b %d %H:%M:%S %z %Y').timestamp()

    now_epoch = datetime.datetime.now().timestamp()
    diff_h = int((now_epoch - last_epoch) / 3600)

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
