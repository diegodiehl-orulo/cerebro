import pytest
from skills.pracas.skill_get_context_for_praca import skill_get_context_for_praca, PracaNotFoundError

def test_get_context_success(setup_workspace):
    """Valida o carregamento de um contexto de praca existente."""
    context = skill_get_context_for_praca("CWB")
    assert context is not None
    assert context["name"] == "Curitiba"
    assert context["praca_id"] == "CWB"

def test_get_context_not_found(setup_workspace):
    """Valida o erro quando uma praca nao e encontrada."""
    with pytest.raises(PracaNotFoundError, match="Praca com id 'XXX' nao encontrada"):
        skill_get_context_for_praca("XXX")

def test_get_context_file_not_found(tmp_path, monkeypatch):
    """Valida o erro quando o arquivo de memoria nao existe."""
    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        skill_get_context_for_praca("CWB")
