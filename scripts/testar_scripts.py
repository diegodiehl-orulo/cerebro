#!/usr/bin/env python3
"""
testar_scripts.py — Auditoria rápida de todos os scripts do workspace
Uso: python3 testar_scripts.py
"""

import os
import subprocess
import time
import signal

SCRIPTS_DIR = "/root/.openclaw/workspace/scripts"
TIMEOUT = 8  # segundos por script

# Scripts que não retornam cleanly — pular
SKIP = {
    "__pycache__",
    "deprecated",
    "apply_groq_config.sh",
    "backup_diego.sh",
    "minimax_health.py",      # não retorna exit 0
    "minimax_diagnostic.py",   # não retorna exit 0
    "gcal_morfeu.py",          # requer gcalcli auth
}

results = []

for filename in sorted(os.listdir(SCRIPTS_DIR)):
    if filename.startswith("."):
        continue
    if filename in SKIP:
        results.append(("⏭️  SKIP", "—", filename))
        print(f"⏭️  SKIP — {filename}")
        continue
    filepath = os.path.join(SCRIPTS_DIR, filename)
    if os.path.isdir(filepath):
        continue

    ext = os.path.splitext(filename)[1]
    if ext == ".sh":
        cmd = ["bash", filepath]
    elif ext == ".py":
        cmd = ["python3", filepath]
    else:
        continue

    start = time.time()
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            cwd=SCRIPTS_DIR,
            stdin=subprocess.DEVNULL,
        )
        duration = round(time.time() - start, 1)
        if proc.returncode == 0:
            status = "✅ OK"
        else:
            stderr = (proc.stderr or "").strip()[:80]
            stdout = (proc.stdout or "").strip()[:80]
            detail = stderr or stdout
            status = f"⚠️  ERR {proc.returncode} — {detail}"
        duration_str = f"{duration}s"
    except subprocess.TimeoutExpired:
        status = "⏱️  TIMEOUT"
        duration_str = f">{TIMEOUT}s"
    except Exception as e:
        status = f"🔴 EXCEPTION — {str(e)[:60]}"
        duration_str = "?"

    results.append((status, duration_str, filename))
    print(f"{status} ({duration_str}) — {filename}")

print()
ok = sum(1 for s, _, _ in results if s.startswith("✅"))
warn = sum(1 for s, _, _ in results if s.startswith("⚠️"))
err = sum(1 for s, _, _ in results if s.startswith("🔴"))
tout = sum(1 for s, _, _ in results if s.startswith("⏱️"))
skip = sum(1 for s, _, _ in results if s.startswith("⏭️"))
print(f"📊 RESUMO: {ok} OK | {warn} WARN | {err} ERR | {tout} TIMEOUT | {skip} SKIP | {len(results)} total")
