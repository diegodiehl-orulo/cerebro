#!/usr/bin/env python3
"""
archive_daily.py — G3 Transcript Pruning (Sprint 2 FASE 2)
Arquiva automaticamente arquivos de memory/daily/ com mais de 60 dias de inatividade.

Uso:
  python3 archive_daily.py           # dry-run (não move nada)
  python3 archive_daily.py --execute # arquiva de verdade

Saída: relatório de arquivos arquivados + pendentes.
"""

import os
import sys
import shutil
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace")
DAILY_DIR = WORKSPACE / "memory" / "daily"
ARCHIVE_BASE = WORKSPACE / "memory" / "archive"
DAYS_THRESHOLD = 60
DRY_RUN = "--execute" not in sys.argv


def get_quarter(date: datetime) -> str:
    q = (date.month - 1) // 3 + 1
    return f"daily_{date.year}-Q{q}"


def should_archive(filepath: Path) -> bool:
    stat = filepath.stat()
    mtime = datetime.fromtimestamp(stat.st_mtime)
    age_days = (datetime.now() - mtime).days
    return age_days >= DAYS_THRESHOLD


def run():
    if not DAILY_DIR.exists():
        print("❌ Diretório memory/daily/ não encontrado.")
        return

    files = list(DAILY_DIR.iterdir())
    to_archive = []
    to_keep = []

    for f in files:
        if f.is_file():
            if should_archive(f):
                to_archive.append(f)
            else:
                to_keep.append(f)

    print(f"📂 memory/daily/ — {len(files)} arquivos analisados")
    print(f"📦 Para arquivar (>{DAYS_THRESHOLD} dias): {len(to_archive)}")
    print(f"✅ Manter (recentes): {len(to_keep)}")
    print()

    if not to_archive:
        print("✅ Nada a arquivar. Todos os arquivos estão dentro do prazo.")
        return

    for f in to_archive:
        stat = f.stat()
        mtime = datetime.fromtimestamp(stat.st_mtime)
        age = (datetime.now() - mtime).days
        quarter = get_quarter(mtime)
        dest_dir = ARCHIVE_BASE / quarter
        dest_file = dest_dir / f.name

        if DRY_RUN:
            print(f"  [DRY-RUN] {f.name} ({age} dias) → archive/{quarter}/")
        else:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(f), str(dest_file))
            print(f"  ✅ Arquivado: {f.name} ({age} dias) → archive/{quarter}/")

    if DRY_RUN:
        print()
        print("⚠️  DRY-RUN ativo. Para executar: python3 archive_daily.py --execute")
    else:
        print()
        print(f"✅ {len(to_archive)} arquivo(s) arquivado(s) com sucesso.")
        # Logar no daily de hoje
        log_file = DAILY_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.md"
        with open(log_file, "a") as log:
            log.write(f"\n## archive_daily.py — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            log.write(f"- Arquivados: {len(to_archive)} arquivo(s)\n")
            for f in to_archive:
                log.write(f"  - {f.name}\n")


if __name__ == "__main__":
    run()
