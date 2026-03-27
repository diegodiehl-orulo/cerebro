import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

class SourceDataNotFoundError(Exception):
    """Excecao para quando o arquivo de dados de uma praca nao e encontrado."""
    pass

def skill_collect_kpis_from_praca(praca_id: str, start_date: str, end_date: str) -> Dict[str, Any]:
    """
    Coleta e agrega os KPIs de uma praca para um determinado periodo.

    Regras de Agregacao:
    - mrr: ultimo valor nao nulo do periodo.
    - corretores_ativos: ultimo valor nao nulo do periodo.
    - deals_criados: soma de todos os valores do periodo.

    Args:
        praca_id: O identificador da praca.
        start_date: Data de inicio do periodo (formato YYYY-MM-DD).
        end_date: Data de fim do periodo (formato YYYY-MM-DD).

    Returns:
        Um dicionario no formato schema_kpi_data_raw.
    """
    source_file = Path(f"data/pracas/{praca_id}_kpis.json")
    if not source_file.exists():
        raise SourceDataNotFoundError(f"Arquivo de dados nao encontrado para a praca {praca_id} em {source_file}")

    with open(source_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    start_dt = datetime.fromisoformat(start_date).date()
    end_dt = datetime.fromisoformat(end_date).date()
    
    records_in_period = [
        r for r in data.get("records", []) 
        if start_dt <= datetime.fromisoformat(r["date"]).date() <= end_dt
    ]
    
    # Ordena do mais antigo para o mais recente para pegar o ultimo valor
    records_in_period.sort(key=lambda r: r['date'])

    mrr = None
    corretores_ativos = None
    deals_criados = 0

    for record in records_in_period:
        if record.get("mrr") is not None:
            mrr = record["mrr"]
        if record.get("corretores_ativos") is not None:
            corretores_ativos = record["corretores_ativos"]
        if record.get("deals_criados") is not None:
            deals_criados += record["deals_criados"]

    return {
        "metadata": {
            "praca_id": praca_id,
            "start_date": start_date,
            "end_date": end_date,
        },
        "kpis": {
            "mrr": mrr,
            "corretores_ativos": corretores_ativos,
            "deals_criados": deals_criados if records_in_period else None,
        }
    }
