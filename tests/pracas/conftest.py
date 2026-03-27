import pytest
import json
import os
from pathlib import Path

@pytest.fixture(scope="function")
def setup_workspace(tmp_path, monkeypatch):
    """
    Cria uma estrutura de diretorios e arquivos temporaria para os testes,
    simulando o workspace real e ajustando o CWD.
    """
    # Muda o diretorio de trabalho atual para o diretorio temporario
    monkeypatch.chdir(tmp_path)

    # Cria a estrutura de pastas
    (tmp_path / "memory" / "pracas").mkdir(parents=True)
    (tmp_path / "data" / "pracas").mkdir(parents=True)
    (tmp_path / "templates" / "pracas").mkdir(parents=True)
    (tmp_path / "reports" / "pracas").mkdir(parents=True)

    # Cria o arquivo de contexto
    context_content = [
        {"praca_id": "CWB", "name": "Curitiba", "socio_local_dri": "Luiz Zanella"},
        {"praca_id": "VIX", "name": "Vitoria", "socio_local_dri": "Pedro Kneip"}
    ]
    with open(tmp_path / "memory/pracas/mem_pracas_contexto.json", "w") as f:
        json.dump(context_content, f)

    # Cria o arquivo de dados de KPI
    kpi_content = {
      "metadata": {"praca_id": "CWB", "source": "test_export.csv"},
      "records": [
        {"date": "2026-03-31", "mrr": 150000, "corretores_ativos": 250, "deals_criados": 45},
        {"date": "2026-02-28", "mrr": 120000, "corretores_ativos": 240, "deals_criados": 0},
        {"date": "2026-01-31", "mrr": 115000, "corretores_ativos": 235, "deals_criados": 50},
        {"date": "2025-12-31", "mrr": None, "corretores_ativos": 220, "deals_criados": 48}
      ]
    }
    with open(tmp_path / "data/pracas/CWB_kpis.json", "w") as f:
        json.dump(kpi_content, f)

    # Cria o template
    template_content = """# Relatorio de Sprint - {{ results.praca_context.name }}
**Periodo:** `{{ results.sprint_period.start_date }}` a `{{ results.sprint_period.end_date }}`
"""
    with open(tmp_path / "templates/pracas/template_onepager_praca.md", "w") as f:
        f.write(template_content)
    
    return tmp_path
