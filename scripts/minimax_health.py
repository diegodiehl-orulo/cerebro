#!/usr/bin/env python3
"""
MiniMax Health Check - Monitora saúde da API
Roda via cron: 0 9 * * 1-5
"""
import requests
import time
import json
from datetime import datetime

API_KEY = "sk-cp--KdotSlVuQe2kODU0wiSCN1xMwNwrUrd1cgN7rQk8wXYNjhDeG75i9UrCIhFj4EfH4TTxnqTInH41gXNGqvMR-OXUFIfd7bSc9gZ0rk0AXQaZk31Bi4nf8Y"
URL = "https://api.minimaxi.chat/v1/chat/completions"
LOG_FILE = "/root/.config/morfeu/minimax_health.log"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().isoformat()} - {msg}\n")

results = {"latency": [], "success": 0, "fail": 0}

# 3 requests de teste
for i in range(3):
    start = time.time()
    try:
        r = requests.post(URL, headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }, json={
            "model": "MiniMax-M2.5",
            "messages": [{"role": "user", "content": "ok"}],
            "temperature": 0.1
        }, timeout=30)
        latency = (time.time() - start) * 1000
        results["latency"].append(latency)
        if r.status_code == 200:
            results["success"] += 1
        else:
            results["fail"] += 1
            log(f"REQ{i+1} FAIL: {r.status_code} - {r.text[:100]}")
    except Exception as e:
        results["fail"] += 1
        log(f"REQ{i+1} ERROR: {str(e)}")
    time.sleep(0.5)

# Resumo
avg_latency = sum(results["latency"]) / len(results["latency"]) if results["latency"] else 0
p95 = sorted(results["latency"])[int(len(results["latency"])*0.95)] if results["latency"] else 0

log(f"HEALTH: {results['success']}/3 OK | avg: {avg_latency:.0f}ms | p95: {p95:.0f}ms")

print(f"✅ MiniMax Health: {results['success']}/3 OK")
print(f"📊 Latência: avg={avg_latency:.0f}ms p95={p95:.0f}ms")

if results["fail"] > 1:
    print("⚠️ ALERTA: Múltiplas falhas detectadas")
    exit(1)
