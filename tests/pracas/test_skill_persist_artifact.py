import pytest
from pathlib import Path
from skills.pracas.skill_persist_artifact import skill_persist_artifact

def test_persist_artifact_success(setup_workspace):
    """Testa a criacao de um novo arquivo de artefato."""
    filepath = "reports/pracas/test_report.md"
    content = "Hello, World!"
    
    result_path_str = skill_persist_artifact(filepath, content)
    result_path = Path(result_path_str)
    
    assert result_path.exists()
    assert result_path.read_text(encoding="utf-8") == content
    assert result_path.is_absolute()

def test_persist_artifact_overwrite(setup_workspace):
    """Testa a sobrescrita de um arquivo existente."""
    filepath = "reports/pracas/test_overwrite.md"
    skill_persist_artifact(filepath, "initial content")
    
    final_content = "final content"
    skill_persist_artifact(filepath, final_content, overwrite=True)
    
    assert Path(filepath).read_text(encoding="utf-8") == final_content

def test_persist_artifact_no_overwrite_fail(setup_workspace):
    """Testa o erro ao tentar escrever em arquivo existente sem permissao de sobrescrita."""
    filepath = "reports/pracas/test_no_overwrite.md"
    skill_persist_artifact(filepath, "initial content")
    
    with pytest.raises(FileExistsError):
        skill_persist_artifact(filepath, "new content", overwrite=False)
