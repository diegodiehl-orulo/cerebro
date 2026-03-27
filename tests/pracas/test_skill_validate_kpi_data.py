import pytest
from skills.pracas.skill_validate_kpi_data import skill_validate_kpi_data, KpiValidationError

def test_validate_kpi_success():
    """Testa a validacao de um objeto de dados bruto valido."""
    raw_data = {
        "metadata": {"praca_id": "CWB", "start_date": "2026-03-01", "end_date": "2026-03-31"},
        "kpis": {"mrr": 150000, "corretores_ativos": 250, "deals_criados": None}
    }
    validated = skill_validate_kpi_data(raw_data)
    kpis = validated["kpis"]
    assert kpis["mrr"] == 150000.0
    assert kpis["corretores_ativos"] == 250.0
    assert kpis["deals_criados"] == 0.0

def test_validate_kpi_missing_key():
    """Testa a validacao quando uma chave de KPI esperada esta ausente."""
    raw_data = {
        "metadata": {"praca_id": "CWB", "start_date": "2026-03-01", "end_date": "2026-03-31"},
        "kpis": {"mrr": 150000}
    }
    validated = skill_validate_kpi_data(raw_data)
    assert validated["kpis"]["corretores_ativos"] == 0.0

def test_validate_kpi_invalid_value():
    """Testa o erro quando um valor de KPI nao pode ser convertido para numero."""
    raw_data = {
        "metadata": {"praca_id": "CWB", "start_date": "2026-03-01", "end_date": "2026-03-31"},
        "kpis": {"mrr": "invalid"}
    }
    with pytest.raises(KpiValidationError):
        skill_validate_kpi_data(raw_data)

def test_validate_kpi_invalid_structure():
    """Testa o erro quando a estrutura do objeto de entrada e invalida."""
    with pytest.raises(KpiValidationError):
        skill_validate_kpi_data({"invalid_structure": True})
