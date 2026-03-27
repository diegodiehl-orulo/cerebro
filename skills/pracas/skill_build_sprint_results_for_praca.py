from typing import Dict, Any, List

def skill_build_sprint_results_for_praca(
    context: Dict[str, Any],
    kpis: Dict[str, Any],
    deviations: List[Dict[str, Any]],
    sprint_period: Dict[str, str]
) -> Dict[str, Any]:
    """
    Agrega todos os dados e analises de um sprint em um unico objeto.

    Args:
        context: O objeto de contexto da praca.
        kpis: Os KPIs validados para o periodo do sprint.
        deviations: A lista de desvios identificados.
        sprint_period: Um dicionario com 'start_date' e 'end_date'.

    Returns:
        Um unico dicionario no formato schema_sprint_results.
    """
    return {
        "praca_context": context,
        "sprint_period": sprint_period,
        "kpis_validated": kpis,
        "deviations": deviations,
    }
