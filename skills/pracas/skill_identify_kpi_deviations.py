from typing import Dict, Any, List

def _calculate_delta_percent(current: float, previous: float) -> float | str:
    """Calcula a variacao percentual com tratamento especial para o caso de o valor anterior ser 0."""
    if previous == 0:
        if current > 0:
            return "N/A (de 0)"
        return 0.0
    
    return ((current - previous) / abs(previous)) * 100.0

def skill_identify_kpi_deviations(
    current_kpis: Dict[str, Any], 
    previous_kpis: Dict[str, Any],
    threshold_percent: float = 10.0
) -> List[Dict[str, Any]]:
    """
    Compara dois conjuntos de KPIs validados e identifica desvios significativos.

    Args:
        current_kpis: Dados validados do periodo atual.
        previous_kpis: Dados validados do periodo anterior.
        threshold_percent: O limiar percentual para considerar um desvio como significativo.

    Returns:
        Uma lista de dicionarios, cada um representando um desvio no formato schema_kpi_deviation.
    """
    deviations = []
    
    current_values = current_kpis.get("kpis", {})
    previous_values = previous_kpis.get("kpis", {})
    
    all_keys = sorted(list(set(current_values.keys()) | set(previous_values.keys())))

    for key in all_keys:
        current = current_values.get(key, 0.0)
        previous = previous_values.get(key, 0.0)
        
        delta_percent_raw = _calculate_delta_percent(current, previous)
        
        is_significant = (
            isinstance(delta_percent_raw, float) and abs(delta_percent_raw) >= threshold_percent
        ) or (isinstance(delta_percent_raw, str) and current > 0)

        if is_significant:
            deviation = {
                "kpi_name": key,
                "current_value": current,
                "previous_value": previous,
                "delta_absolute": current - previous,
                "delta_percent": delta_percent_raw,
            }
            deviations.append(deviation)
            
    return deviations
