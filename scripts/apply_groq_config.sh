#!/bin/bash
# apply_groq_config.sh — Substitui Codex pelo Groq Llama 3.3 no config do OpenClaw
# Uso: bash apply_groq_config.sh gsk_SUA_KEY_AQUI

set -e

GROQ_KEY="${1}"

if [ -z "$GROQ_KEY" ]; then
  echo "❌ Uso: bash apply_groq_config.sh gsk_SUA_KEY_AQUI"
  exit 1
fi

if [[ "$GROQ_KEY" != gsk_* ]]; then
  echo "⚠️  Aviso: keys Groq normalmente começam com 'gsk_'. Continuar mesmo assim? (s/n)"
  read -r resp
  [[ "$resp" != "s" ]] && exit 0
fi

CONFIG="/root/.openclaw/openclaw.json"
BACKUP="/root/.openclaw/openclaw.json.bak.$(date +%Y%m%d_%H%M%S)"

cp "$CONFIG" "$BACKUP"
echo "✅ Backup criado: $BACKUP"

python3 << PYEOF
import json, sys

config_path = "/root/.openclaw/openclaw.json"
with open(config_path) as f:
    cfg = json.load(f)

groq_key = "${GROQ_KEY}"

# 1. Remover Codex do fallback e adicionar Groq
cfg["agents"]["defaults"]["model"] = {
    "primary": "anthropic/claude-sonnet-4-6",
    "fallbacks": ["groq/llama-3.3-70b-versatile"]
}

# 2. Remover Codex dos models, adicionar Groq com alias
models = cfg["agents"]["defaults"].get("models", {})
models.pop("openai-codex/gpt-5.3-codex-spark", None)
models["groq/llama-3.3-70b-versatile"] = {"alias": "groq"}
cfg["agents"]["defaults"]["models"] = models

# 3. Remover auth profile do Codex
profiles = cfg.get("auth", {}).get("profiles", {})
profiles.pop("openai-codex:default", None)
cfg.setdefault("auth", {})["profiles"] = profiles

# 4. Adicionar provider Groq com API openai-completions
cfg.setdefault("models", {}).setdefault("providers", {})["groq"] = {
    "baseUrl": "https://api.groq.com/openai/v1",
    "apiKey": groq_key,
    "auth": "api-key",
    "api": "openai-completions",
    "models": [
        {
            "id": "llama-3.3-70b-versatile",
            "name": "Llama 3.3 70B (Groq)",
            "contextWindow": 128000,
            "maxTokens": 32768
        }
    ]
}

with open(config_path, "w") as f:
    json.dump(cfg, f, indent=2, ensure_ascii=False)

print("✅ Config atualizado com sucesso")
print("   Codex removido: fallback + auth profile + alias")
print("   Groq adicionado: groq/llama-3.3-70b-versatile (alias: groq)")
PYEOF

# Restart OpenClaw para aplicar
echo "🔄 Reiniciando OpenClaw..."
systemctl restart openclaw 2>/dev/null || openclaw gateway restart 2>/dev/null || true
echo "✅ Pronto. Fallback agora: Sonnet → Llama 3.3 (Groq)"
