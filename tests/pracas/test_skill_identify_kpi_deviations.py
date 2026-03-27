import pytest
from skills.pracas.skill_identify_kpi_deviations import skill_identify_kpi_deviations

@pytest.fixture
def sample_kpis():
    current = {
        "metadata": {},
        "kpis": {"mrr": 110.0, "deals_criados": 50.0, "corretores_ativos": 95.0}
    }
    previous = {
        "metadata": {},
        "kpis": {"mrr": 100.0, "deals_criados": 0.0, "corretores_ativos": 100.0}
    }
    return current, previous

def test_identify_no_significant_deviation(sample_kpis):
    """Testa o caso onde a variacao esta abaixo do limiar."""
    current, previous = sample_kpis
    current["kpis"]["mrr"] = 105.0 # 5% de aumento
    deviations = skill_identify_kpi_deviations(current, previous)
    assert len(deviations) == 0

def test_identify_positive_deviation(sample_kpis):
    """Testa a deteccao de um desvio positivo significativo."""
    current, previous = sample_kpis
    current["kpis"]["mrr"] = 120.0 # 20% de aumento
    deviations = skill_identify_kpi_deviations(current, previous)
    assert len(deviations) == 1
    assert deviations[0]["kpi_name"] == "mrr"
    assert deviations[0]["delta_percent"] == 20.0

def test_identify_from_zero_deviation(sample_kpis):
    """Testa a deteccao de crescimento a partir de zero."""
    current, previous = sample_kpis
    deviations = skill_identify_kpi_deviations(current, previous)
    assert len(deviations) == 1
    assert deviations[0]["kpi_name"] == "deals_criados"
    assert deviations[0]["current_value"] == 50.0
    assert deviations[0]["previous_value"] == 0.0
    assert deviations[0]["delta_percent"] == "N/A (de 0)"

def test_identify_no_deviation_from_zero_to_zero(sample_kpis):
    """Testa o caso de 0 para 0, que nao e um desvio."""
    current, previous = sample_kpis
    current["kpis"]["deals_criados"] = 0.0
    deviations = skill_identify_kpi_deviations(current, previous)
    assert len(deviations) == 0
