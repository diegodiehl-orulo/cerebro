from typing import Dict, Any

class KpiValidationError(Exception):
    """Excecao para falhas na validacao de dados de KPI."""
    pass

def skill_validate_kpi_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Valida e converte os dados de KPI brutos para um formato limpo e numerico.
    Valores nulos ou ausentes sao convertidos para 0.0.

    Args:
        data: Dicionario no formato schema_kpi_data_raw.

    Returns:
        Dicionario no formato schema_kpi_data_validated.

    Raises:
        KpiValidationError: Se a estrutura dos dados de entrada for invalida.
    """
    if "metadata" not in data or "kpis" not in data:
        raise KpiValidationError("Estrutura de dados de entrada invalida. 'metadata' ou 'kpis' ausente.")

    raw_kpis = data.get("kpis", {})
    validated_kpis = {}
    
    expected_keys = ["mrr", "corretores_ativos", "deals_criados"]

    for key in expected_keys:
        value = raw_kpis.get(key)
        if value is None:
            validated_kpis[key] = 0.0
        else:
            try:
                validated_kpis[key] = float(value)
            except (ValueError, TypeError):
                raise KpiValidationError(f"Nao foi possivel converter o valor '{value}' do KPI '{key}' para numero.")

    return {
        "metadata": data["metadata"],
        "kpis": validated_kpis
    }
