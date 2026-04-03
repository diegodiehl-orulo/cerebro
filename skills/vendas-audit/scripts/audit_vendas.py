#!/usr/bin/env python3
"""
Vendas Audit — Script de auditoria de preenchimento
Lê planilha e gera ranking + mensagens personalizadas
"""
import subprocess
import json
import sys
from datetime import datetime

SPREADSHEET_ID = "1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ"
ABA = "Vendas"
LINK = "https://bit.ly/orulo-consolidado-vendas"

COMMAND = [
    "gog-morfeu", "sheets", "get",
    SPREADSHEET_ID, f"{ABA}!A1:X201", "--plain"
]

def run():
    result = subprocess.run(COMMAND, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erro: {result.stderr}")
        sys.exit(1)
    lines = [l.strip() for l in result.stdout.split('\n') if l.strip()]
    headers = lines[0].split('\t')
    deals = []
    for line in lines[1:]:
        cols = line.split('\t')
        cols += [''] * (len(headers) - len(cols))
        deal = {h.strip(): cols[i].strip() for i, h in enumerate(headers)}
        deals.append(deal)
    return headers, deals

def idx(headers, name):
    try:
        return headers.index(name)
    except:
        return -1

def audit(deals):
    # Índices
    h = deals[0] if deals else {}
    hdrs = list(h.keys())

    def get(deal, name):
        return deal.get(name, '')

    ano_idx = 'Ano de Assinatura do Contrato'
    sdr_idx = 'Nome do SDR que agendou'
    closer_idx = 'Pessoa responsável'
    nome_idx = 'Nome'
    uf_idx = 'UF'
    mes_idx = 'Mês de Assinatura do Contrato'

    COLS_Q = '(SDR) O que levou o contato a aceitar a reunião com a Órulo?'
    COLS_R = '(SDR) Qual foi o contexto atual da incorporadora que appeareda conversa inicial?'
    COLS_R_CORRETO = '(SDR) Qual foi o contexto atual da incorporadora que apareceu na conversa inicial?'
    COLS_S = '(CLOSER) Qual foi o principal gargalo comercial identificado na incorporadora?'
    COLS_T = '(CLOSER) O que mais chamou atenção do cliente durante a reunião ou demonstração?'
    COLS_U = '(CLOSER) Qual entrega de valor da Órulo mais se conectou com a necessidade do cliente?'
    COLS_V = '(CLOSER) O que levou o cliente a decidir contratar a Órulo neste momento?'
    COLS_W = '(CLOSER) Por que essa incorporadora ainda não tinha contratado a Órulo antes?'
    COLS_X = '(CLOSER) Foram abordadas outras frentes ou soluções da Órulo durante a negociação?'

    sdr_pend = {}
    closer_pend = {}

    for d in deals:
        if get(d, ano_idx) != '2026':
            continue

        nome = get(d, nome_idx)
        uf = get(d, uf_idx)
        mes = get(d, mes_idx)
        sdr = get(d, sdr_idx).strip()
        closer = get(d, closer_idx).strip()

        # SDR
        if sdr and sdr not in ['SEM_SDR', '', 'Z2A']:
            if sdr not in sdr_pend:
                sdr_pend[sdr] = {'vendas': [], 'q_empty': 0, 'r_empty': 0}
            q_val = get(d, COLS_Q).strip()
            r_val = get(d, COLS_R_CORRETO).strip()
            falta_q = not bool(q_val)
            falta_r = not bool(r_val)
            if falta_q or falta_r:
                sdr_pend[sdr]['vendas'].append({
                    'nome': nome, 'uf': uf, 'mes': mes,
                    'q': falta_q, 'r': falta_r
                })
                if falta_q:
                    sdr_pend[sdr]['q_empty'] += 1
                if falta_r:
                    sdr_pend[sdr]['r_empty'] += 1

        # Closer
        if closer and closer not in ['SEM_CLOSER', '', 'Z2A']:
            if closer not in closer_pend:
                closer_pend[closer] = {'vendas': [], 'empty': 0}
            falta = []
            for c_n, c_label in [
                ('S', COLS_S), ('T', COLS_T), ('U', COLS_U),
                ('V', COLS_V), ('W', COLS_W), ('X', COLS_X)
            ]:
                if not get(d, c_label).strip():
                    falta.append(c_n)
            if falta:
                closer_pend[closer]['vendas'].append({
                    'nome': nome, 'uf': uf, 'mes': mes, 'falta': falta
                })
                closer_pend[closer]['empty'] += len(falta)

    return sdr_pend, closer_pend

def gerar_ranking(sdr_pend, closer_pend):
    today = datetime.now().strftime('%d/%m')
    total_vendas = sum(len(v['vendas']) for v in sdr_pend.values()) // 2 + sum(len(v['vendas']) for v in closer_pend.values())

    lines = []
    lines.append(f"📊 AUDITORIA — Preenchimento Estratégico 2026")
    lines.append(f"🔗 {LINK}")
    lines.append(f"{total_vendas} vendas | Semana {today}")
    lines.append("")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    lines.append("SDR — Colunas Q + R")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # SDR sorted by total empty fields
    sdr_sorted = sorted(sdr_pend.items(), key=lambda x: -(x[1]['q_empty'] + x[1]['r_empty']))
    for name, data in sdr_sorted:
        total_empty = data['q_empty'] + data['r_empty']
        n_vendas = len(data['vendas'])
        if total_empty == 0:
            continue
        emoji = '🔴' if total_empty > 5 else '🟡'
        lines.append(f"{emoji} {name:<20} {n_vendas:>3} vendas pendentes  {total_empty:>3} campos vazios")

    lines.append("")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    lines.append("CLOSER — Colunas S+T+U+V+W+X")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    cl_sorted = sorted(closer_pend.items(), key=lambda x: -x[1]['empty'])
    for name, data in cl_sorted:
        n_vendas = len(data['vendas'])
        empty = data['empty']
        if empty == 0:
            continue
        emoji = '🔴' if empty > 10 else '🟡'
        lines.append(f"{emoji} {name:<20} {n_vendas:>3} vendas pendentes  {empty:>3} campos vazios")

    return '\n'.join(lines)

def gerar_mensagens(sdr_pend, closer_pend):
    mensagens = []

    PERGUNTAS = {
        'Q': 'O que levou o contato a aceitar a reunião com a Órulo?',
        'R': 'Qual foi o contexto atual da incorporadora?',
        'S': 'Principal gargalo identificado',
        'T': 'O que mais chamou atenção do cliente?',
        'U': 'Entrega de valor que mais se conectou',
        'V': 'O que levou a decidir contratar?',
        'W': 'Por que não tinha contratado antes?',
        'X': 'Outras frentes/soluções abordadas?',
    }

    def cor(vazios):
        return '🔴' if vazios > 5 else '🟡'

    # SDR
    for nome, data in sorted(sdr_pend.items(), key=lambda x: -len(x[1]['vendas'])):
        if len(data['vendas']) == 0:
            continue
        total = len(data['vendas'])
        msg = []
        msg.append(f"{nome}, tudo bem?")
        msg.append("")
        msg.append(f"Temos {total} venda{'s' if total > 1 else ''} sua{'s' if total > 1 else ''} de 2026 sem os campos Q e R preenchidos na planilha:")
        msg.append("")
        msg.append(f"🔗 {LINK}")
        msg.append("")
        q_empty = data['q_empty']
        r_empty = data['r_empty']
        msg.append(f"{cor(q_empty+r_empty)} {total} venda{'s' if total > 1 else ''} pendentes — {q_empty + r_empty} campos vazios")
        msg.append("")
        msg.append("Vendas:")
        for v in data['vendas']:
            status = f"Q:❌ R:❌" if (v['q'] and v['r']) else (f"Q:{'❌' if v['q'] else '✅'} R:{'❌' if v['r'] else '✅'}")
            msg.append(f"• {v['nome']} ({v['uf']}) — Mês {v['mes']}")
        msg.append("")
        msg.append("Campos a preencher:")
        if q_empty > 0:
            msg.append("• Q: O que levou o contato a aceitar a reunião?")
            msg.append("• R: Qual foi o contexto atual da incorporadora?")
        msg.append("")
        msg.append("Consegue preencher até sexta 17h?")
        msg.append("")
        msg.append("abs")
        msg.append("Diego")
        mensagens.append(('SDR', nome, '\n'.join(msg)))

    # Closer
    for nome, data in sorted(closer_pend.items(), key=lambda x: -x[1]['empty']):
        if len(data['vendas']) == 0:
            continue
        total = len(data['vendas'])
        empty = data['empty']
        msg = []
        msg.append(f"{nome}, tudo bem?")
        msg.append("")
        msg.append(f"Temos pendências suas na planilha de 2026:")
        msg.append("")
        msg.append(f"🔗 {LINK}")
        msg.append("")
        msg.append(f"{cor(empty)} {total} venda{'s' if total > 1 else ''} pendentes — {empty} campos vazios")
        msg.append("")
        msg.append("Vendas:")
        for v in data['vendas']:
            msg.append(f"• {v['nome']} ({v['uf']}) — Mês {v['mes']} — Faltam: {','.join(v['falta'])}")
        msg.append("")
        msg.append("Campos a preencher:")
        falta_set = set()
        for v in data['vendas']:
            for f in v['falta']:
                falta_set.add(f)
        for col in ['S','T','U','V','W','X']:
            if col in falta_set:
                msg.append(f"• {col}: {PERGUNTAS[col]}")
        msg.append("")
        msg.append("Consegue preencher até sexta 17h?")
        msg.append("")
        msg.append("abs")
        msg.append("Diego")
        mensagens.append(('CLOSER', nome, '\n'.join(msg)))

    return mensagens

if __name__ == "__main__":
    headers, deals = run()
    sdr_pend, closer_pend = audit(deals[1:])

    ranking = gerar_ranking(sdr_pend, closer_pend)
    msgs = gerar_mensagens(sdr_pend, closer_pend)

    print("=== RANKING ===")
    print(ranking)
    print()
    print("=== MENSAGENS ===")
    for tipo, nome, msg in msgs:
        print(f"--- {tipo}: {nome} ---")
        print(msg)
        print()
