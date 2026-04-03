#!/usr/bin/env python3
"""
autodream.py — M3 autoDream (Sprint 2 FASE 2)
Micro-consolidação de memória: detecta inconsistências entre daily/ e topic files.

Uso:
  python3 autodream.py           # roda consolidação + gera relatório
  python3 autodream.py --dry-run # apenas diagnostica, não escreve

Saída: relatório em memory/AUTODREAM_LOG.md + alertas se encontrar inconsistências.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace")
DAILY_DIR = WORKSPACE / "memory" / "daily"
TOPIC_DIR = WORKSPACE / "memory"
MEMORY_INDEX = WORKSPACE / "MEMORY.md"
LOG_FILE = WORKSPACE / "memory" / "AUTODREAM_LOG.md"
DRY_RUN = "--dry-run" in sys.argv


def read_file_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def get_today_daily() -> Path | None:
    today = datetime.now().strftime("%Y-%m-%d")
    candidate = DAILY_DIR / f"{today}.md"
    return candidate if candidate.exists() else None


def get_all_topic_files() -> list[Path]:
    return [
        f for f in TOPIC_DIR.iterdir()
        if f.is_file() and f.suffix == ".md" and f.name != "AUTODREAM_LOG.md"
    ]


def count_index_entries(content: str) -> int:
    return sum(1 for line in content.splitlines() if line.startswith("| memory/") or line.startswith("| governance/"))


def check_stale_entries(index_content: str, topic_files: list[Path]) -> list[str]:
    """Verifica se há entradas no índice apontando para arquivos inexistentes."""
    stale = []
    topic_names = {f.name for f in topic_files}
    for line in index_content.splitlines():
        if line.startswith("| memory/"):
            parts = line.split("|")
            if len(parts) > 1:
                ref = parts[1].strip()
                filename = Path(ref).name
                if filename not in topic_names and not (WORKSPACE / ref).exists():
                    stale.append(ref)
    return stale


def check_orphan_files(index_content: str, topic_files: list[Path]) -> list[str]:
    """Topic files que existem mas não estão no índice."""
    orphans = []
    for tf in topic_files:
        ref = f"memory/{tf.name}"
        if ref not in index_content:
            orphans.append(tf.name)
    return orphans


def run():
    print(f"🌙 autoDream — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    index_content = read_file_safe(MEMORY_INDEX)
    topic_files = get_all_topic_files()
    today_daily = get_today_daily()

    # --- Diagnóstico ---
    entry_count = count_index_entries(index_content)
    stale = check_stale_entries(index_content, topic_files)
    orphans = check_orphan_files(index_content, topic_files)

    print(f"📊 MEMORY.md: {entry_count} entradas ativas (limite: 30)")
    print(f"📂 Topic files: {len(topic_files)} arquivos em memory/")
    print(f"📅 Daily de hoje: {'✅ Existe' if today_daily else '⚠️ Não criado'}")
    print()

    alerts = []

    if entry_count > 30:
        msg = f"⚠️ MEMORY.md com {entry_count} entradas — limite é 30. Arquivar entries antigas."
        print(msg)
        alerts.append(msg)

    if stale:
        msg = f"⚠️ {len(stale)} entrada(s) no índice apontando para arquivo inexistente:"
        print(msg)
        for s in stale:
            print(f"   - {s}")
        alerts.append(msg + " " + ", ".join(stale))

    if orphans:
        # Filtrar os conhecidos como arquivos de sistema
        ignore = {"ARQUITETURA_3CAMADAS.md", "AUTODREAM_LOG.md"}
        real_orphans = [o for o in orphans if o not in ignore]
        if real_orphans:
            msg = f"ℹ️  {len(real_orphans)} topic file(s) não indexado(s) no MEMORY.md:"
            print(msg)
            for o in real_orphans:
                print(f"   - memory/{o}")
            alerts.append(msg + " " + ", ".join(real_orphans))

    if not alerts:
        print("✅ Nenhuma inconsistência detectada.")
    print()

    # --- Log ---
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    status = "✅ OK" if not alerts else f"⚠️ {len(alerts)} alerta(s)"
    log_entry = f"""
## {now_str} — autoDream {status}

- Entradas MEMORY.md: {entry_count}/30
- Topic files: {len(topic_files)}
- Daily hoje: {'sim' if today_daily else 'não'}
- Alertas: {len(alerts)}
"""
    if alerts:
        log_entry += "### Alertas\n"
        for a in alerts:
            log_entry += f"- {a}\n"

    if not DRY_RUN:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"📝 Log registrado em memory/AUTODREAM_LOG.md")
    else:
        print("[DRY-RUN] Log não escrito.")

    return len(alerts)


if __name__ == "__main__":
    exit_code = run()
    sys.exit(exit_code)
