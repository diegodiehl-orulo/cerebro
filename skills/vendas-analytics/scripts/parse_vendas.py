#!/usr/bin/env python3
"""
Vendas Analytics — Parser e Comparador
Lê a planilha Consolidado de Vendas e gera estrutura comparativa vs report Diego
"""
import subprocess
import json
import sys
from datetime import datetime

SPREADSHEET_ID = "1So9CV-9iU8uMG7OBK5xXuBDbwJgSmWwAOTVINfDF4xQ"
ABA = "Vendas"
COMMAND = ["gog-morfeu", "sheets", "get", SPREADSHEET_ID, f"{ABA}!A1:AA200", "--plain"]

def run():
    result = subprocess.run(COMMAND, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erro ao acessar planilha: {result.stderr}")
        sys.exit(1)
    
    lines = [l.strip() for l in result.stdout.split('\n') if l.strip()]
    if not lines:
        print("Planilha vazia ou inacessível")
        sys.exit(1)
    
    headers = lines[0].split('\t')
    deals = []
    for line in lines[1:]:
        cols = line.split('\t')
        deal = {}
        for i, h in enumerate(headers):
            deal[h.strip()] = cols[i].strip() if i < len(cols) else ""
        deals.append(deal)
    
    return headers, deals

def filtrar_por_mes_ano(deals, mes, ano):
    """Filtra deals por mês e ano de assinatura"""
    filtrados = []
    for d in deals:
        try:
            mes_str = d.get('Mês de Assinatura do Contrato', '').strip()
            ano_str = d.get('Ano de Assinatura do Contrato', '').strip()
            if mes_str.isdigit() and ano_str.isdigit():
                if int(mes_str) == mes and int(ano_str) == ano:
                    filtrados.append(d)
        except:
            pass
    return filtrados

def resumir_por_uf(deals):
    """Resumo de contratos e valor por UF"""
    resumo = {}
    for d in deals:
        uf = d.get('UF', 'N/I').strip()
        nome = d.get('Nome', '')
        mensalidade = d.get('Mensalidade Total', 'R$ 0,00')
        
        valor = 0
        if 'R$' in mensalidade:
            try:
                valor = float(mensalidade.replace('R$', '').replace('.', '').replace(',', '.').strip())
            except:
                valor = 0
        
        if uf not in resumo:
            resumo[uf] = {"contratos": 0, "valor": 0, "deals": []}
        
        resumo[uf]["contratos"] += 1
        resumo[uf]["valor"] += valor
        resumo[uf]["deals"].append({"nome": nome, "mensalidade": valor})
    
    return resumo

def auditoria_preenchimento(deals, ano_alvo=2026):
    """Verifica % de preenchimento das colunas estratégicas"""
    cols_estrategicas = [
        "(SDR) O que levou o contato a aceitar a reunião com a Órulo?",
        "(SDR) Qual foi o contexto atual da incorporadora que apareceu na conversa inicial?",
        "(CLOSER) Qual foi o principal gargalo comercial identificado na incorporadora?",
        "(CLOSER) O que mais chamou atenção do cliente durante a reunião ou demonstração?",
        "(CLOSER) Qual entrega de valor da Órulo mais se conectou com a necessidade do cliente?",
        "(CLOSER) O que levou o cliente a decidir contratar a Órulo neste momento?",
        "(CLOSER) Por que essa incorporadora ainda não tinha contratado a Órulo antes?",
        "(CLOSER) Foram abordadas outras frentes ou soluções da Órulo durante a negociação?"
    ]
    
    ano_deals = [d for d in deals if d.get('Ano de Assinatura do Contrato', '').strip() == str(ano_alvo)]
    total = len(ano_deals)
    
    resultado = {}
    for col in cols_estrategicas:
        preenchidas = sum(1 for d in ano_deals if d.get(col, '').strip())
        resultado[col] = {
            "preenchidas": preenchidas,
            "total": total,
            "pct": round(preenchidas / total * 100, 1) if total > 0 else 0
        }
    
    return resultado

def comparar_report(deals_mes, deals_planilha):
    """
    Compara deals do report de Diego com deals da planilha
    Retorna: matches, faltam_na_planilha, faltam_no_report
    """
    # Normalizar para comparação
    def normalizar(d):
        nome = d.get('Nome', '').lower().strip()
        uf = d.get('UF', '').lower().strip()
        return f"{uf}|{nome}"
    
    keys_planilha = set(normalizar(d) for d in deals_planilha)
    keys_report = set(normalizar(d) for d in deals_mes)
    
    faltam_na_planilha = [d for d in deals_mes if normalizar(d) not in keys_planilha]
    faltam_no_report = [d for d in deals_planilha if normalizar(d) not in keys_report]
    
    return faltam_na_planilha, faltam_no_report

if __name__ == "__main__":
    headers, deals = run()
    
    mes = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.now().month
    ano = int(sys.argv[2]) if len(sys.argv) > 2 else 2026
    
    deals_filtrados = filtrar_por_mes_ano(deals, mes, ano)
    resumo = resumir_por_uf(deals_filtrados)
    auditoria = auditoria_preenchimento(deals, ano)
    
    output = {
        "timestamp": datetime.now().isoformat(),
        "mes": mes,
        "ano": ano,
        "total_deals_mes": len(deals_filtrados),
        "resumo_uf": resumo,
        "auditoria_preenchimento_2026": auditoria,
        "headers": headers
    }
    
    print(json.dumps(output, indent=2, ensure_ascii=False))
