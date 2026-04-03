#!/usr/bin/env python3
"""
Vendas Report — Comparar report Diego vs Planilha
Uso: python3 compare_report.py [MES] [ANO]
      python3 compare_report.py 3 2026
"""
import subprocess
import re
import sys
from datetime import datetime

SPREADSHEET_ID = "1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ"
ABA = "Vendas"
LINK = "https://bit.ly/orulo-consolidado-vendas"

def get_planilha():
    result = subprocess.run(
        ["gog-morfeu", "sheets", "get", SPREADSHEET_ID, f"{ABA}!A1:X201", "--plain"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Erro planilha: {result.stderr}")
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

def normalizar_nome(nome):
    """Normaliza nome para comparação fuzzy"""
    nome = nome.lower().strip()
    nome = re.sub(r'[^a-z0-9\s]', '', nome)
    nome = re.sub(r'\s+', ' ', nome)
    # Abreviações comuns
    replacements = {
        'incorporadora': 'inc',
        'incorporações': 'inc',
        'construções': 'const',
        'construção': 'const',
        'engenharia': 'eng',
        'empresa': 'emp',
    }
    for old, new in replacements.items():
        nome = nome.replace(old, new)
    return nome

def similar(a, b, threshold=0.75):
    """Verifica se dois nomes são similares (fuzzy match)"""
    a_norm = normalizar_nome(a)
    b_norm = normalizar_nome(b)
    if a_norm == b_norm:
        return True
    # Check if one is contained in the other
    if a_norm in b_norm or b_norm in a_norm:
        return True
    # Levenshtein-like simple check
    from difflib import SequenceMatcher
    ratio = SequenceMatcher(None, a_norm, b_norm).ratio()
    return ratio >= threshold

def parse_report_text(report_text, mes, ano):
    """
    Extrai vendas do texto do report enviado por Diego.
    Retorna lista de dicts com: nome, uf, cidade, sdr, closer, valor
    """
    deals = []
    lines = report_text.strip().split('\n')
    
    current_value = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Captura bloco de valor: 🔹 *R$ 524,48*
        valor_match = re.search(r'R\$\s*([\d.,]+)', line)
        if valor_match:
            val_str = valor_match.group(1).replace('.', '').replace(',', '.')
            try:
                current_value = float(val_str)
            except:
                current_value = None
            continue
        
        # Linha de venda: UF – Cidade – Nome – SDR – Closer
        # Aceita: • - UF – Cidade – Nome – SDR – Closer
        #         UF – Cidade – Nome – SDR – Closer
        pattern = r'(?:[•\-\*]\s*)?([A-Z]{2})\s*[–\-]\s*([A-Za-zÀ-ÿ\s]+?)\s*[–\-]\s*([A-Za-zÀ-ÿ\s\./]+?)\s*[–\-]\s*([A-Za-zÀ-ÿ\s./]+?)\s*(?:[–\-]\s*([A-Za-zÀ-ÿ\s./]+))?$'
        
        match = re.match(pattern, line)
        if match:
            uf = match.group(1).strip()
            cidade = match.group(2).strip()
            # Remove trailing SDR/Closer from nome
            nome_raw = match.group(3).strip()
            sdr_raw = match.group(4).strip() if match.group(4) else ''
            closer_raw = match.group(5).strip() if match.group(5) else sdr_raw
            
            # Clean nome — sometimes it's "Nome – R$ X"
            nome = re.sub(r'\s*–\s*R\$\s*[\d.,]+\s*$', '', nome_raw).strip()
            
            deals.append({
                'uf': uf,
                'cidade': cidade,
                'nome': nome,
                'sdr': sdr_raw,
                'closer': closer_raw,
                'valor': current_value
            })
            continue
        
        # Fallback: try simpler pattern
        if '–' in line or '-' in line:
            parts = re.split(r'\s*[–\-]\s*', line.strip('•-* '))
            if len(parts) >= 3:
                uf = parts[0].strip()
                cidade = parts[1].strip()
                nome = parts[2].strip()
                sdr = parts[3].strip() if len(parts) > 3 else ''
                closer = parts[4].strip() if len(parts) > 4 else (parts[3].strip() if len(parts) > 3 else '')
                if len(uf) == 2 and uf.isupper():
                    deals.append({
                        'uf': uf, 'cidade': cidade, 'nome': nome,
                        'sdr': sdr, 'closer': closer, 'valor': current_value
                    })
    
    return deals

def comparar(report_deals, planilha_deals, mes, ano):
    """Compara vendas do report com planilha"""
    
    # Filtra planilha por mês/ano
    planilha_filtrada = [
        d for d in planilha_deals
        if d.get('Ano de Assinatura do Contrato', '').strip() == str(ano)
        and d.get('Mês de Assinatura do Contrato', '').strip() == str(mes)
    ]
    
    matched = []
    falta_planilha = []
    falta_report = []
    divergencias = []
    
    planilha_keys = set()
    for p in planilha_filtrada:
        key = f"{p.get('UF','').strip().upper()}|{normalizar_nome(p.get('Nome',''))}"
        planilha_keys.add(key)
    
    planilha_nomes_map = {
        normalizar_nome(p.get('Nome', '')): p 
        for p in planilha_filtrada
    }
    
    # Para cada venda do report
    for r in report_deals:
        r_key = f"{r['uf'].upper()}|{normalizar_nome(r['nome'])}"
        r_nome_norm = normalizar_nome(r['nome'])
        
        # Procura match na planilha
        match = None
        for p in planilha_filtrada:
            p_nome = p.get('Nome', '').strip()
            p_uf = p.get('UF', '').strip().upper()
            
            if p_uf == r['uf'].upper() and similar(r['nome'], p_nome):
                match = p
                break
        
        if match:
            # Verifica divergências
            divs = []
            if r.get('sdr'):
                # SDR pode vir no formato "Jade/Mirla" — aceitar se overlap
                sdr_match = r['sdr'].lower().replace('/', ' ').split()
                p_sdr = match.get('Nome do SDR que agendou', '').lower()
                if not any(s in p_sdr for s in sdr_match if len(s) > 3):
                    divs.append(f"SDR: report={r['sdr']} planilha={match.get('Nome do SDR que agendou','')}")
            
            if r.get('closer'):
                cl_match = r['closer'].lower().replace('/', ' ').split()
                p_cl = match.get('Pessoa responsável', '').lower()
                if not any(s in p_cl for s in cl_match if len(s) > 3):
                    divs.append(f"Closer: report={r['closer']} planilha={match.get('Pessoa responsável','')}")
            
            if divs:
                divergencias.append({'report': r, 'planilha': match, 'divs': divs})
            else:
                matched.append({'report': r, 'planilha': match})
        else:
            falta_planilha.append(r)
    
    # Faltam no report (estão na planilha mas não no report)
    report_nomes = {normalizar_nome(r['nome']) for r in report_deals}
    for p in planilha_filtrada:
        p_nome = p.get('Nome', '').strip()
        p_uf = p.get('UF', '').strip().upper()
        # Verificar se já está no report
        found = False
        for r in report_deals:
            if p_uf == r['uf'].upper() and similar(r['nome'], p_nome):
                found = True
                break
        if not found:
            falta_report.append(p)
    
    return matched, falta_planilha, falta_report, divergencias

def gerar_output(matched, falta_planilha, falta_report, divergencias, mes, ano):
    mes_nome = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    mes_str = mes_nome[int(mes)] if 1 <= int(mes) <= 12 else mes
    
    lines = []
    lines.append(f"📋 COMPARAÇÃO — {mes_str}/{ano}")
    lines.append(f"Report: {len(matched) + len(falta_planilha)} vendas | Planilha: {len(matched) + len(falta_report)} vendas")
    lines.append(f"🔗 {LINK}")
    lines.append("")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if matched:
        lines.append(f"✅ MATCHES: {len(matched)}")
        if divergencias:
            lines.append(f"⚠️ DIVERGÊNCIAS: {len(divergencias)}")
            for d in divergencias:
                r = d['report']
                lines.append(f"  • {r['nome']} ({r['uf']}) — {d['divs'][0]}")
        lines.append("")
    
    if falta_planilha:
        lines.append(f"🔴 FALTAM NA PLANILHA ({len(falta_planilha)}) — Gustavo precisa cadastrar")
        for r in falta_planilha:
            closer_str = f" / {r['closer']}" if r.get('closer') else ""
            lines.append(f"  • {r['nome']} ({r['uf']} — {r['cidade']}) — {r['sdr']}{closer_str}")
        lines.append("")
    
    if falta_report:
        lines.append(f"🔵 FALTAM NO REPORT ({len(falta_report)}) — Verificar")
        for p in falta_report[:10]:
            lines.append(f"  • {p.get('Nome','')} ({p.get('UF','')}) — {p.get('Pessoa responsável','')}")
        if len(falta_report) > 10:
            lines.append(f"  ... e mais {len(falta_report)-10}")
        lines.append("")
    
    if not falta_planilha and not falta_report and not divergencias:
        lines.append("✅ TUDO ALIGN — planilha e report compatíveis")
        lines.append("")
    
    if falta_planilha:
        lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        lines.append(f"👉 Cobrar Gustavo para cadastrar {len(falta_planilha)} vendas até sexta 17h")
        lines.append(f"🔗 {LINK}")
    
    return '\n'.join(lines)

if __name__ == "__main__":
    mes = sys.argv[1] if len(sys.argv) > 1 else str(datetime.now().month)
    ano = sys.argv[2] if len(sys.argv) > 2 else "2026"
    
    headers, planilha_deals = get_planilha()
    
    # Lê report do stdin se piped
    report_text = ""
    if not sys.stdin.isatty():
        report_text = sys.stdin.read()
    
    if report_text:
        report_deals = parse_report_text(report_text, mes, ano)
        print(f"Vendas extraídas do report: {len(report_deals)}", file=sys.stderr)
    else:
        print("Erro: é necessário enviar o texto do report via pipe", file=sys.stderr)
        print("Exemplo: cat report.txt | python3 compare_report.py 3 2026", file=sys.stderr)
        sys.exit(1)
    
    matched, falta_planilha, falta_report, divergencias = comparar(
        report_deals, planilha_deals, mes, ano
    )
    
    output = gerar_output(matched, falta_planilha, falta_report, divergencias, mes, ano)
    print(output)
