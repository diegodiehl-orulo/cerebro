import pytest
from skills.pracas.skill_collect_kpis_from_praca import skill_collect_kpis_from_praca, SourceDataNotFoundError

def test_collect_kpis_success(setup_workspace):
    """Testa a coleta e agregacao de KPIs para um periodo valido."""
    result = skill_collect_kpis_from_praca(
        praca_id="CWB",
        start_date="2026-03-01",
        end_date="2026-03-31"
    )
    assert result["metadata"]["praca_id"] == "CWB"
    kpis = result["kpis"]
    assert kpis["mrr"] == 150000
    assert kpis["corretores_ativos"] == 250
    assert kpis["deals_criados"] == 45

def test_collect_kpis_sum_deals(setup_workspace):
    """Testa se 'deals_criados' e somado corretamente no periodo."""
    result = skill_collect_kpis_from_praca(
        praca_id="CWB",
        start_date="2026-01-01",
        end_date="2026-01-31"
    )
    assert result["kpis"]["deals_criados"] == 50

def test_collect_kpis_empty_period(setup_workspace):
    """Testa um periodo sem registros de dados."""
    result = skill_collect_kpis_from_praca(
        praca_id="CWB",
        start_date="2026-04-01",
        end_date="2026-04-30"
    )
    kpis = result["kpis"]
    assert kpis["mrr"] is None
    assert kpis["corretores_ativos"] is None
    assert kpis["deals_criados"] is None

def test_collect_kpis_source_not_found(setup_workspace):
    """Testa o erro quando o arquivo de dados da praca nao existe."""
    with pytest.raises(SourceDataNotFoundError):
        skill_collect_kpis_from_praca("XXX", "2026-03-01", "2026-03-31")
