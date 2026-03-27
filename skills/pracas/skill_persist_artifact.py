from pathlib import Path

def skill_persist_artifact(filepath: str, content: str, overwrite: bool = True) -> str:
    """
    Salva um conteudo de texto em um arquivo no workspace.

    Args:
        filepath: O caminho relativo do arquivo a ser salvo (a partir da raiz do workspace).
        content: O conteudo de texto a ser salvo.
        overwrite: Se True, sobrescreve o arquivo se ele ja existir.

    Returns:
        O caminho absoluto do arquivo salvo.

    Raises:
        FileExistsError: Se o arquivo ja existir e overwrite for False.
    """
    path = Path(filepath)
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    if path.exists() and not overwrite:
        raise FileExistsError(f"O arquivo {path} ja existe e a sobrescrita nao foi permitida.")
        
    path.write_text(content, encoding="utf-8")
    
    return str(path.resolve())
