from typing import Dict, Any
from pathlib import Path
import jinja2

class TemplateNotFoundError(Exception):
    """Excecao para quando o arquivo de template nao e encontrado."""
    pass

def skill_generate_onepager_for_sprint(results: Dict[str, Any]) -> str:
    """
    Gera o relatorio de sprint em formato Markdown usando um template Jinja2.

    Args:
        results: O objeto de resultados do sprint no formato schema_sprint_results.

    Returns:
        Uma string contendo o relatorio em Markdown.
    """
    template_path = Path("templates/pracas")
    template_file = "template_onepager_praca.md"
    
    if not (template_path / template_file).exists():
        raise TemplateNotFoundError(f"Template nao encontrado em {template_path / template_file}")

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(template_path)),
        trim_blocks=True,
        lstrip_blocks=True
    )
    template = env.get_template(template_file)
    
    return template.render(results=results)
