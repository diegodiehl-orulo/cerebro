#!/usr/bin/env python3
"""
config.py — Configuração central da integração tl;dv.

Single source of truth para:
  - Paths do workspace (auto-detectados do __file__, com override via CEREBRO_HOME)
  - Secrets (env vars obrigatórias: TLDV_API_KEY, MINIMAX_API_KEY)
  - Limites e constantes (retries, timeouts, pause entre chamadas)

Por que aqui (e não espalhado em cada módulo):
  - Antes: "/root/.openclaw/workspace" em 30+ arquivos → quebra ao mover repo.
  - Antes: TLDV_API_KEY literal versionada em 5+ arquivos → risco de vazamento.
  - Agora: um ponto de verdade, portátil, com erro claro se faltar config.

Uso:
    from config import WORKSPACE, DIRS, TLDV_API_KEY, require_tldv_key, ENV

    client = TldvClient(api_key=require_tldv_key())
    raw_file = DIRS["raw"] / f"{meeting_id}.json"
"""
from __future__ import annotations

import os
import sys
from pathlib import Path


# ── Workspace discovery ──────────────────────────────────────────────────────
# Ordem de prioridade:
#   1. CEREBRO_HOME env var (override explícito)
#   2. __file__ resolvido (integrations/tldv/config.py → workspace root)
#   3. Fallback /root/.openclaw/workspace (compat com ambiente antigo)

def _detect_workspace() -> Path:
    env_home = os.environ.get("CEREBRO_HOME") or os.environ.get("WORKSPACE_ROOT")
    if env_home:
        return Path(env_home).expanduser().resolve()

    here = Path(__file__).resolve()
    # integrations/tldv/config.py → parents[2] = workspace root
    candidate = here.parents[2]
    if (candidate / "integrations" / "tldv").is_dir():
        return candidate

    legacy = Path("/root/.openclaw/workspace")
    if legacy.is_dir():
        return legacy

    # Último recurso: dois níveis acima de config.py
    return candidate


WORKSPACE: Path = _detect_workspace()


# ── Directory layout ─────────────────────────────────────────────────────────

MEM = WORKSPACE / "memory" / "meetings"

DIRS: dict[str, Path] = {
    "workspace":  WORKSPACE,
    "memory":     WORKSPACE / "memory",
    "logs":       WORKSPACE / "logs",
    "tasks":      WORKSPACE / "tasks",
    "docs":       WORKSPACE / "docs",
    "integrations": WORKSPACE / "integrations",

    # Pipeline tl;dv
    "meetings":   MEM,
    "raw":        MEM / "raw",
    "transcripts": MEM / "transcripts",
    "notes":      MEM / "notes",
    "normalized": MEM / "normalized",
    "summaries":  MEM / "summaries",
    "analysis":   MEM / "analysis",
    "queue":      MEM / "queue",
    "queue_processed": MEM / "queue" / "processed",
    "queue_failed":    MEM / "queue" / "failed",
    "ledger":     MEM / "ledger",
    "per_meeting_tasks": MEM / "tasks",

    # Outputs humanos
    "generated_tasks": WORKSPACE / "tasks" / "generated-from-meetings",
    "consolidated":    WORKSPACE / "tasks" / "consolidated",
    "updates":         WORKSPACE / "docs" / "meeting-derived-updates",
}


# ── Ledger files ─────────────────────────────────────────────────────────────

LEDGERS: dict[str, Path] = {
    "processed":     DIRS["ledger"] / "processed_meetings.json",
    "enriched":      DIRS["ledger"] / "enriched_ledger.json",
    "analyzed":      DIRS["ledger"] / "analyzed_ledger.json",
    "persisted":     DIRS["ledger"] / "persisted_ledger.json",
    "tasks":         DIRS["ledger"] / "tasks_ledger.json",
    "persister_hashes": DIRS["ledger"] / "persister_hashes.txt",
    "task_sigs":     DIRS["ledger"] / "task_sigs.txt",
    "pending_retry": DIRS["ledger"] / "enrich_pending_retry.json",
    "analyze_pending": DIRS["ledger"] / "analyze_pending_2026.json",
}

LOCKS: dict[str, Path] = {
    "collector": DIRS["ledger"] / ".processing_lock",
    "enricher":  DIRS["ledger"] / ".enrich_lock",
    "persister": DIRS["ledger"] / ".persister_lock",
}


# ── API Endpoints ────────────────────────────────────────────────────────────

TLDV_BASE_URL = os.environ.get("TLDV_BASE_URL", "https://pasta.tldv.io/v1alpha1")
MINIMAX_URL = os.environ.get("MINIMAX_URL", "https://api.minimaxi.chat/v1/chat/completions")
MINIMAX_MODEL = os.environ.get("MINIMAX_MODEL", "MiniMax-M2.5")


# ── Secrets (env vars; erro claro se faltar) ────────────────────────────────

def require_tldv_key() -> str:
    """Retorna TLDV_API_KEY ou levanta erro explicativo."""
    key = os.environ.get("TLDV_API_KEY", "").strip()
    if not key:
        raise EnvironmentError(
            "TLDV_API_KEY não definida. Exporte no shell ou use .env na raiz do workspace.\n"
            f"Esperado em: {WORKSPACE}/.env (ou env var direta)"
        )
    return key


def require_minimax_key() -> str:
    """Retorna MINIMAX_API_KEY ou levanta erro explicativo."""
    key = os.environ.get("MINIMAX_API_KEY", "").strip()
    if not key:
        raise EnvironmentError(
            "MINIMAX_API_KEY não definida. Exporte no shell ou use .env na raiz do workspace."
        )
    return key


# Acesso direto (para módulos que toleram None e fazem checagem própria)
TLDV_API_KEY: str | None = os.environ.get("TLDV_API_KEY") or None
MINIMAX_API_KEY: str | None = os.environ.get("MINIMAX_API_KEY") or None


# ── Limites e constantes ─────────────────────────────────────────────────────

HTTP_TIMEOUT = int(os.environ.get("TLDV_HTTP_TIMEOUT", "30"))
LLM_TIMEOUT = int(os.environ.get("TLDV_LLM_TIMEOUT", "90"))
RATE_LIMIT_PAUSE = float(os.environ.get("TLDV_RATE_LIMIT_PAUSE", "5"))
MAX_RETRIES = int(os.environ.get("TLDV_MAX_RETRIES", "3"))
MAX_CONSECUTIVE_ERRORS = int(os.environ.get("TLDV_MAX_CONSECUTIVE_ERRORS", "5"))
PAGE_SIZE = int(os.environ.get("TLDV_PAGE_SIZE", "50"))
WEBHOOK_PORT = int(os.environ.get("TLDV_WEBHOOK_PORT", "18788"))


# ── .env loader (opcional, sem dependência externa) ──────────────────────────

def load_dotenv(path: Path | None = None) -> dict[str, str]:
    """
    Lê um .env simples (KEY=VALUE, # comentário) e injeta em os.environ
    sem sobrescrever vars já definidas. Retorna dict com o que foi lido.
    """
    path = path or (WORKSPACE / ".env")
    loaded: dict[str, str] = {}
    if not path.exists():
        return loaded
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value
            loaded[key] = value
    return loaded


# Carrega .env automaticamente ao importar (não sobrescreve env vars existentes)
_LOADED_ENV = load_dotenv()
# Atualiza o cache após o .env ter sido lido
TLDV_API_KEY = os.environ.get("TLDV_API_KEY") or None
MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY") or None


# ── Helpers ──────────────────────────────────────────────────────────────────

def ensure_dirs(*keys: str) -> None:
    """Cria diretórios sob demanda (evita criar tudo na importação)."""
    for k in keys:
        if k in DIRS:
            DIRS[k].mkdir(parents=True, exist_ok=True)


def workspace_relative(p: Path) -> str:
    """Retorna path relativo ao workspace (para logs mais legíveis)."""
    try:
        return str(Path(p).resolve().relative_to(WORKSPACE))
    except ValueError:
        return str(p)


ENV = {
    "CEREBRO_HOME": str(WORKSPACE),
    "WORKSPACE_ROOT": str(WORKSPACE),
    "PYTHONPATH": str(DIRS["integrations"]),
}


if __name__ == "__main__":
    # Diagnóstico rápido: python3 config.py
    try:
        print(f"WORKSPACE: {WORKSPACE}")
        print(f"  exists: {WORKSPACE.is_dir()}")
        print(f"TLDV_API_KEY: {'set' if TLDV_API_KEY else 'MISSING'}")
        print(f"MINIMAX_API_KEY: {'set' if MINIMAX_API_KEY else 'MISSING'}")
        print(f".env loaded: {len(_LOADED_ENV)} vars from {WORKSPACE / '.env'}")
        print("\nDirectories:")
        for name, path in DIRS.items():
            mark = "✓" if path.exists() else "○"
            print(f"  {mark} {name}: {path}")
    except BrokenPipeError:
        sys.stdout = None  # downstream fechou (head/less); sair silenciosamente
