import pytest
from skills.pracas.skill_build_sprint_results_for_praca import skill_build_sprint_results_for_praca

def test_build_sprint_results():
    """Testa a agregacao de dados em um unico objeto de resultados."""
    context = {"praca_id": "CWB", "name": "Curitiba"}
    kpis = {"metadata": {}, "kpis": {"mrr": 150.0}}
    deviations = [{"kpi_name": "mrr", "delta_percent": 25.0}]
    sprint_period = {"start_date": "2026-03-01", "end_date": "2026-03-31"}

    results = skill_build_sprint_results_for_praca(context, kpis, deviations, sprint_period)

    assert results["praca_context"] == context
    assert results["kpis_validated"] == kpis
    assert results["deviations"] == deviations
    assert results["sprint_period"] == sprint_period
    assert "praca_context" in results
    assert "sprint_period" in results
