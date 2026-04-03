#!/usr/bin/env python3
"""
Daily Vendas Report — 18h
Roda parse_vendas + audit_vendas e gera output para Telegram
"""
import subprocess
import json
import sys
from datetime import datetime

def run_script(script_path, args=None):
    cmd = ["python3", script_path]
    if args:
        cmd.extend(args)
    result = subprocess.run(
        cmd,
        capture_output=True, text=True, cwd="/root/.openclaw/workspace"
    )
    return result.stdout

def main():
    # Tenta mês atual, senão pega último mês com dados
    mes_atual = datetime.now().month
    
    # Testa meses do mais recente ao mais antigo
    meses_tentar = [mes_atual, mes_atual - 1]
    dados = None
    
    for m in meses_tentar:
        if m < 1:
            continue
        parse_out = run_script("skills/vendas-analytics/scripts/parse_vendas.py", [str(m), "2026"])
        try:
            dados_tmp = json.loads(parse_out)
            if dados_tmp.get("total_deals_mes", 0) > 0:
                dados = dados_tmp
                break
        except:
            continue
    
    if dados is None:
        print("📊 VENDAS — Sem dados disponíveis")
        sys.exit(0)
    
    # Dados gerais
    deals = dados.get("resumo_uf", {})
    total_valor = sum(v["valor"] for v in deals.values())
    total_contratos = sum(v["contratos"] for v in deals.values())
    mes_num = int(dados.get("mes", 0))
    mes_nome = ["","Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
    mes_str = mes_nome[mes_num] if 1 <= mes_num <= 12 else str(mes_num)
    
    today = datetime.now().strftime("%d/%m")
    ano = datetime.now().strftime("%Y")
    
    # Monta output Telegram
    lines = []
    lines.append(f"🔵 VENDAS DIÁRIAS — {today}")
    lines.append(f"📅 {mes_str}/{ano} | Planilha atualizada em: {dados.get('timestamp','')[:10]}")
    lines.append("")
    lines.append(f"💰 {total_contratos} contratos | R$ {total_valor:,.2f}")
    lines.append("")
    lines.append("Por UF:")
    for uf, info in sorted(deals.items(), key=lambda x: -x[1]["valor"]):
        lines.append(f"  {uf}: {info['contratos']} contratos | R$ {info['valor']:,.2f}")
    
    lines.append("")
    lines.append("━━━━━━━━━━━━━━━━━━━━")
    lines.append("📊 Preenchimento 2026")
    aud = dados.get("auditoria_preenchimento_2026", {})
    
    # SDR
    sdr_total = sum(1 for c in ["Q","R"] for v in aud.values() if c in [c for c in ["Q","R"]])
    sdr_cols = {k:v for k,v in aud.items() if "SDR" in k}
    if sdr_cols:
        linhas_sdr = []
        for col, vals in sdr_cols.items():
            if vals["total"] > 0:
                nome = col.split(") ")[1][:25] if ") " in col else col[:25]
                linhas_sdr.append(f"{vals['preenchidas']}/{vals['total']} ({vals['pct']:.0f}%)")
        lines.append(f"SDR (Q+R): {' | '.join(linhas_sdr)}")
    
    # Closer
    closer_cols = {k:v for k,v in aud.items() if "CLOSER" in k}
    if closer_cols:
        for col, vals in closer_cols.items():
            if vals["total"] > 0:
                nome = col.split(") ")[1][:25] if ") " in col else col[:25]
                emoji = "✅" if vals["pct"] >= 80 else ("🟡" if vals["pct"] >= 50 else "🔴")
                lines.append(f"{emoji} {nome}: {vals['preenchidas']}/{vals['total']} ({vals['pct']:.0f}%)")
    
    lines.append("")
    lines.append("🔗 https://bit.ly/orulo-consolidado-vendas")
    
    print('\n'.join(lines))

if __name__ == "__main__":
    main()
