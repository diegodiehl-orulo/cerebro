import pytest
import os
import yaml
from pathlib import Path

# Adiciona a pasta de skills ao path para que possam ser importadas
# NOTA: Em um ambiente OpenClaw real, isso pode nao ser necessario
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'skills' / 'pracas'))

# Importa as skills apos ajustar o path
from skill_get_context_for_praca import skill_get_context_for_praca
from skill_collect_kpis_from_praca import skill_collect_kpis_from_praca
from skill_validate_kpi_data import skill_validate_kpi_data
from skill_identify_kpi_deviations import skill_identify_kpi_deviations
from skill_build_sprint_results_for_praca import skill_build_sprint_results_for_praca
from skill_generate_onepager_for_sprint import skill_generate_onepager_for_sprint
from skill_persist_artifact import skill_persist_artifact

# Mapeia nomes de skills para funcoes
SKILL_REGISTRY = {
    "skill_get_context_for_praca": skill_get_context_for_praca,
    "skill_collect_kpis_from_praca": skill_collect_kpis_from_praca,
    "skill_validate_kpi_data": skill_validate_kpi_data,
    "skill_identify_kpi_deviations": skill_identify_kpi_deviations,
    "skill_build_sprint_results_for_praca": skill_build_sprint_results_for_praca,
    "skill_generate_onepager_for_sprint": skill_generate_onepager_for_sprint,
    "skill_persist_artifact": skill_persist_artifact,
}

def _resolve_param(value, context):
    """Resolve um parametro que pode ser uma referencia a um passo anterior."""
    if isinstance(value, str) and value.startswith("{{") and value.endswith("}}"):
        parts = value[3:-2].strip().split('.')
        ref_obj = context.get(parts[0], {})
        
        # Simplificacao para o teste: assume acesso a 'output'
        if len(parts) > 1 and parts[1] == 'output':
             return ref_obj
        return ref_obj

    # Lida com dicionarios como parametros (ex: sprint_period)
    if isinstance(value, dict):
        return {k: _resolve_param(v, context) for k, v in value.items()}

    return value

def test_workflow_ponta_a_ponta_success(setup_workspace):
    """Testa a execucao do workflow de ponta a ponta."""
    
    workflow_path = Path("workflows/pracas/wkf_review_sprint_readout.yaml")
    with open(workflow_path, "r") as f:
        workflow = yaml.safe_load(f)

    # Simula a injecao de inputs
    inputs = {
        "praca_id": "CWB",
        "current_period_start": "2026-03-01",
        "current_period_end": "2026-03-31",
        "previous_period_start": "2026-02-01",
        "previous_period_end": "2026-02-28",
    }
    
    # Contexto para armazenar os resultados dos passos
    run_context = {"inputs": inputs}

    # Executa cada passo do workflow
    for step in workflow["steps"]:
        skill_name = step["skill"]
        skill_func = SKILL_REGISTRY[skill_name]
        
        # Resolve parametros
        params = {k: _resolve_param(v, run_context) for k, v in step["params"].items()}
        
        # Executa a skill
        result = skill_func(**params)
        
        # Armazena o resultado no contexto
        run_context[step["id"]] = result

    # Verifica o output final
    final_output_def = workflow["outputs"][0]
    final_filepath = _resolve_param(final_output_def["value"], run_context)
    
    assert final_filepath is not None
    assert Path(final_filepath).exists()
    
    content = Path(final_filepath).read_text()
    assert "# Relatorio de Sprint - Curitiba" in content
    assert "deals_criados" in content # Verifica se o desvio de "deals_criados" foi capturado
