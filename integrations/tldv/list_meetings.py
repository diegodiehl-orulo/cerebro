#!/usr/bin/env python3
"""
list_meetings.py — Lista reuniões da API tl;dv com paginação.
Uso: python3 list_meetings.py [--page N] [--page-size N]
Requer: TLDV_API_KEY definida no ambiente.
"""

import os
import sys
import argparse
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s — %(message)s",
)
logger = logging.getLogger("tldv.list_meetings")


def format_meeting(meeting: dict) -> str:
    """Formata uma reunião em linha legível (id, título, data, duração)."""
    mid = meeting.get("id", "?")
    title = meeting.get("name") or meeting.get("title") or "Sem título"
    happened = meeting.get("happenedAt", "")
    # Simplificar data: "Mon Apr 06 2026 18:00:00 GMT+0000" → "06/04 18:00"
    if happened:
        try:
            dt = datetime.strptime(happened[:25], "%a %b %d %Y %H:%M:%S")
            happened = dt.strftime("%d/%m %H:%M")
        except Exception:
            pass  # Keep original if parsing fails
    duration = meeting.get("duration", 0)
    if duration:
        mins = int(duration / 60)
        secs = int(duration % 60)
        duration_str = f"{mins}m{secs}s"
    else:
        duration_str = ""
    if len(title) > 55:
        title = title[:52] + "..."
    parts = [f"ID: {mid}", f"TÍTULO: {title}", f"DATA: {happened}"]
    if duration_str:
        parts.append(f"DURAÇÃO: {duration_str}")
    return "  |  ".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Lista reuniões do tl;dv")
    parser.add_argument("--page", type=int, default=1, help="Número da página (default: 1)")
    parser.add_argument("--page-size", type=int, default=10, help="Itens por página (default: 10)")
    args = parser.parse_args()

    api_key = os.environ.get("TLDV_API_KEY")
    if not api_key:
        print("ERRO: TLDV_API_KEY não definida no ambiente.")
        print("Defina com: export TLDV_API_KEY='sua-chave-aqui'")
        sys.exit(1)

    from tldv.client import TldvClient

    print(f"Listando reuniões — página={args.page}, pageSize={args.page_size}")
    print("-" * 80)

    try:
        client = TldvClient()
        result = client.list_meetings(page=args.page, page_size=args.page_size)

        # API retorna { page, pageSize, pages, total, results: [...] }
        meetings = result.get("results", [])
        total = result.get("total", 0)
        pages = result.get("pages", 0)
        current_page = result.get("page", args.page)

        if not meetings:
            print("Nenhuma reunião encontrada nesta página.")
        else:
            print(f"Página {current_page}/{pages} — Total: {total} reuniões")
            print()
            for m in meetings:
                print(format_meeting(m))

        print()
        print(f"Exibidas {len(meetings)} de {total} reuniões (página {current_page}/{pages}).")

    except PermissionError as e:
        print(f"ERRO de autenticação (401/403): {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"ERRO de rota (404): {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"ERRO de requisição (400): {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERRO inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
