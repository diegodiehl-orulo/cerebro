#!/usr/bin/env python3
"""
P3 — Health Check do Endpoint MiniMax
Verifica se a API do MiniMax está acessível e registra o estado.
Uso: python3 endpoint_health.py [--alert]

Saída:
  OK — API acessível
  ALERTA — Falha detectada (escreve /tmp/minimax_circuit_open)
  CIRCUIT_OPEN — Já estava em estado de falha
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error
from datetime import datetime

CIRCUIT_FILE = "/tmp/minimax_circuit_open"
LOG_FILE = "/root/.config/morfeu/endpoint_health_log.json"
HEALTH_URL = "https://api.minimaxi.chat/v1/models"
FAILURE_THRESHOLD = 3
CHECK_WINDOW = 600  # 10 minutos

def load_log():
    try:
        with open(LOG_FILE) as f:
            return json.load(f)
    except Exception:
        return {"checks": [], "circuit_open": False, "open_since": None}

def save_log(data):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def check_endpoint():
    try:
        req = urllib.request.Request(HEALTH_URL, headers={"User-Agent": "morfeu-healthcheck/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status < 500
    except urllib.error.HTTPError as e:
        return e.code < 500  # 4xx = API up, request bad (expected sem auth)
    except Exception:
        return False

def main():
    alert_mode = "--alert" in sys.argv
    data = load_log()
    now = time.time()

    # Verificar se circuit já está aberto
    if os.path.exists(CIRCUIT_FILE):
        # Verificar se passou mais de 30min — tentar reset automático
        try:
            open_since = float(open(CIRCUIT_FILE).read().strip())
            if (now - open_since) > 1800:  # 30 minutos
                os.remove(CIRCUIT_FILE)
                data["circuit_open"] = False
                data["open_since"] = None
                print("⟳ Circuit reset automático após 30 minutos.")
            else:
                print("CIRCUIT_OPEN — API em estado de falha. Aguardar reset.")
                return 2
        except Exception:
            pass

    # Executar check
    ok = check_endpoint()
    ts = datetime.now().isoformat()

    # Registrar resultado
    data["checks"].append({"ts": ts, "ok": ok})
    # Manter apenas últimos 20 checks
    data["checks"] = data["checks"][-20:]

    # Contar falhas na janela
    recent_failures = sum(
        1 for c in data["checks"]
        if not c["ok"] and (now - time.mktime(time.strptime(c["ts"][:19], "%Y-%m-%dT%H:%M:%S"))) < CHECK_WINDOW
    )

    if ok:
        print(f"OK — API MiniMax acessível ({ts})")
        data["circuit_open"] = False
        save_log(data)
        return 0
    else:
        print(f"⚠️ Falha detectada ({ts}). Falhas recentes: {recent_failures}/{FAILURE_THRESHOLD}")

        if recent_failures >= FAILURE_THRESHOLD:
            # Abrir circuit
            with open(CIRCUIT_FILE, "w") as f:
                f.write(str(now))
            data["circuit_open"] = True
            data["open_since"] = ts
            print(f"🔴 ALERTA — Circuit aberto após {recent_failures} falhas. /tmp/minimax_circuit_open criado.")
            save_log(data)
            return 1
        else:
            print(f"ALERTA — Falha isolada (não abre circuit ainda).")
            save_log(data)
            return 1

if __name__ == "__main__":
    sys.exit(main())
