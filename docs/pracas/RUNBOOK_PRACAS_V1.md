# RUNBOOK - Frente Pracas v1

Este runbook fornece instruções operacionais para executar e testar a v1 da frente Pracas.

## 1. Pré-requisitos

### 1.1. Estrutura de Arquivos
- A estrutura de arquivos e todos os artefatos definidos no `CHANGELOG_PRACAS_V1.md` devem estar presentes no workspace.

### 1.2. Dependências de Software
- Python 3.9+
- As seguintes bibliotecas Python precisam estar instaladas:
  ```bash
  pip install pytest jinja2 PyYAML
  ```

### 1.3. Arquivos de Dados
- O arquivo `memory/pracas/mem_pracas_contexto.json` deve estar preenchido com as praças desejadas.
- Para cada praça a ser analisada, deve existir um arquivo de dados correspondente em `data/pracas/[praca_id]_kpis.json`.

## 2. Como Executar os Testes

1.  Navegue até a raiz do workspace.
2.  Execute o seguinte comando no terminal:
    ```bash
    python3 -m pytest -v tests/pracas/
    ```
3.  **Comportamento Esperado:** Todos os testes devem passar ("green"). Isso valida que as skills e o workflow estão funcionando corretamente em um ambiente controlado.

## 3. Como Executar o Workflow Manualmente

Para gerar um relatório para uma praça específica, siga os passos abaixo. Usaremos a praça "CWB" como exemplo.

1.  **Crie um script de execução:** Crie um arquivo temporário na raiz do workspace, por exemplo `run_manual.py`.

2.  **Cole o seguinte código no script:**
    ```python
    import yaml
    import json
    from pathlib import Path
    import sys

    # Adiciona a pasta de skills ao path para importacao
    sys.path.insert(0, str(Path.cwd() / 'skills' / 'pracas'))

    # Importa todas as funcoes das skills
    from skill_get_context_for_praca import skill_get_context_for_praca
    from skill_collect_kpis_from_praca import skill_collect_kpis_from_praca
    from skill_validate_kpi_data import skill_validate_kpi_data
    from skill_identify_kpi_deviations import skill_identify_kpi_deviations
    from skill_build_sprint_results_for_praca import skill_build_sprint_results_for_praca
    from skill_generate_onepager_for_sprint import skill_generate_onepager_for_sprint
    from skill_persist_artifact import skill_persist_artifact

    SKILL_REGISTRY = {
        "skill_get_context_for_praca": skill_get_context_for_praca,
        "skill_collect_kpis_from_praca": skill_collect_kpis_from_praca,
        "skill_validate_kpi_data": skill_validate_kpi_data,
        "skill_identify_kpi_deviations": skill_identify_kpi_deviations,
        "skill_build_sprint_results_for_praca": skill_build_sprint_results_for_praca,
        "skill_generate_onepager_for_sprint": skill_generate_onepager_for_sprint,
        "skill_persist_artifact": skill_persist_artifact,
    }

    def run_workflow(workflow_path, inputs):
        with open(workflow_path, "r") as f:
            workflow = yaml.safe_load(f)
        
        context = {"inputs": inputs}
        print(f"Iniciando workflow: {workflow['name']}...")

        for step in workflow["steps"]:
            step_id = step["id"]
            skill_name = step["skill"]
            print(f"  Executando passo: {step_id} ({skill_name})")
            
            skill_func = SKILL_REGISTRY[skill_name]
            
            # Resolucao de parametros simples para o runbook
            params = {}
            for key, value in step.get("params", {}).items():
                if isinstance(value, str) and "{{" in value:
                     # Remove {{ }} e espacos, depois divide
                    parts = value.strip()[2:-2].strip().split('.')
                    if parts[0] in context:
                        params[key] = context[parts[0]] # Simplificado: passa o objeto inteiro
                else:
                    params[key] = value

            result = skill_func(**params)
            context[step_id] = result
            # print(f"    -> Resultado: {json.dumps(result, indent=2, ensure_ascii=False)}")

        print("Workflow concluido.")
        final_output_def = workflow["outputs"][0]
        final_filepath = context[final_output_def["value"].strip()[2:-2].strip().split('.')[0]]
        print(f"Relatorio final salvo em: {final_filepath}")
        return final_filepath

    if __name__ == "__main__":
        # Defina os inputs para o workflow aqui
        workflow_inputs = {
            "praca_id": "CWB",
            "current_period_start": "2026-03-01",
            "current_period_end": "2026-03-31",
            "previous_period_start": "2026-02-01",
            "previous_period_end": "2026-02-28",
        }
        
        run_workflow("workflows/pracas/wkf_review_sprint_readout.yaml", workflow_inputs)

    ```
3.  **Execute o script a partir da raiz do workspace:**
    ```bash
    python3 run_manual.py
    ```

## 4. Como Interpretar o Output

- **Saída no Terminal:** O script irá imprimir o progresso da execução de cada passo do workflow e, ao final, o caminho do arquivo de relatório que foi gerado.
- **Arquivo de Relatório:** Navegue até a pasta `reports/pracas/`. Você encontrará um arquivo chamado `CWB_sprint_2026-03-31.md`. Abra este arquivo para ver o relatório final.

## 5. Como Regenerar um Relatório

Para gerar um relatório para um período ou praça diferente, simplesmente edite a seção `workflow_inputs` no script `run_manual.py` com os novos parâmetros e execute-o novamente. A política de `overwrite` está ativada, então um arquivo existente com o mesmo nome será sobrescrito.
