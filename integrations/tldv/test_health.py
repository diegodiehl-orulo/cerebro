#!/usr/bin/env python3
"""
test_health.py — Health check da API tl;dv.
Uso: python3 test_health.py
Requer: TLDV_API_KEY definida no ambiente.
"""

import os
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s — %(message)s",
)
logger = logging.getLogger("tldv.test_health")


def main():
    from tldv.client import TldvClient

    api_key = os.environ.get("TLDV_API_KEY")
    if not api_key:
        print("ERRO: TLDV_API_KEY não definida no ambiente.")
        print("Defina com: export TLDV_API_KEY='sua-chave-aqui'")
        sys.exit(1)

    print(f"API Key: {'*' * 20}{api_key[-4:]}")
    print(f"Endpoint: https://pasta.tldv.io/v1alpha1/health")
    print("-" * 50)

    try:
        client = TldvClient()
        result = client.health()
        print(f"Status: {result}")
        print("SUCESSO — API tl;dv acessível.")
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
