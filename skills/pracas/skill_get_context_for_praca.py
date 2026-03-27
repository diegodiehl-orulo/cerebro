import json
from pathlib import Path
from typing import Dict, Any

class PracaNotFoundError(Exception):
    """Excecao para quando uma praca nao e encontrada."""
    pass

def skill_get_context_for_praca(praca_id: str) -> Dict[str, Any]:
    """
    Carrega os metadados de uma praca a partir do arquivo de memoria.

    Args:
        praca_id: O identificador da praca (ex: "CWB").

    Returns:
        Um dicionario com o contexto da praca.

    Raises:
        FileNotFoundError: Se o arquivo de contexto nao for encontrado.
        PracaNotFoundError: Se a praca com o ID especificado nao for encontrada.
    """
    context_path = Path("memory/pracas/mem_pracas_contexto.json")
    
    if not context_path.exists():
        raise FileNotFoundError(f"Arquivo de contexto nao encontrado em {context_path}")

    with open(context_path, "r", encoding="utf-8") as f:
        all_contexts = json.load(f)
    
    for context in all_contexts:
        if context.get("praca_id") == praca_id:
            return context
            
    raise PracaNotFoundError(f"Praca com id '{praca_id}' nao encontrada no arquivo de contexto.")
