import pytest
from skills.pracas.skill_generate_onepager_for_sprint import skill_generate_onepager_for_sprint, TemplateNotFoundError

def test_generate_onepager_success(setup_workspace):
    """Testa a geracao bem-sucedida de um relatorio em Markdown."""
    results = {
        "praca_context": {"name": "Curitiba", "socio_local_dri": "Zanella"},
        "sprint_period": {"start_date": "2026-03-01", "end_date": "2026-03-31"},
        "kpis_validated": {"kpis": {"mrr": 150000, "corretores_ativos": 250, "deals_criados": 45}},
        "deviations": []
    }
    
    markdown_output = skill_generate_onepager_for_sprint(results)
    
    assert "# Relatorio de Sprint - Curitiba" in markdown_output
    assert "`2026-03-01` a `2026-03-31`" in markdown_output

def test_generate_onepager_template_not_found(tmp_path, monkeypatch):
    """Testa o erro quando o arquivo de template nao e encontrado."""
    monkeypatch.chdir(tmp_path)
    # Nao cria a pasta 'templates'
    
    with pytest.raises(TemplateNotFoundError):
        skill_generate_onepager_for_sprint({})
