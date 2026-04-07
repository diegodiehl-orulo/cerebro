#!/usr/bin/env python3
"""
pipeline.py — Orquestrador principal do tl;dv
============================================
Executa o pipeline completo ou por etapas.

Estágios:
  1. collect    — busca reuniões novas da API
  2. enrich      — baixa transcript + notes
  3. analyze     — gera análise executiva (LLM)
  4. persist     — extrai e persiste em memória/documentos
  5. digest      — produz sumário consolidado

Uso:
  python3 pipeline.py                    # executa estágios 1-5 completos
  python3 pipeline.py --stage collect   # só coleta
  python3 pipeline.py --stage enrich    # só enrich das pendentes
  python3 pipeline.py --stage analyze  # só analyze das pendentes
  python3 pipeline.py --stage persist  # só persist
  python3 pipeline.py --stage digest    # só digest

  python3 pipeline.py --meeting-id ID   # pipeline completo para 1 reunião
  python3 pipeline.py --dry-run        # mostra o que faria
  python3 pipeline.py --verbose        # log detalhado
  python3 pipeline.py --since YYYY-MM-DD  # só reuniões após data
  python3 pipeline.py --force           # reprocessa mesmo se já existe

Execução periódica sugerida (via cron ou openclaw cron):
  0 */6 * * *  /usr/bin/python3 .../pipeline.py --stage collect,enrich,analyze,persist >> .../logs/tldv_pipeline.log 2>&1

Para DIGEST, recomenda-se execução separada (1x/dia):
  0 08 * * *  /usr/bin/python3 .../pipeline.py --stage digest --since YYYY-MM-DD >> .../logs/tldv_digest.log 2>&1
"""

import argparse
import json
import os
import subprocess
import sys
import time
import logging
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path("/root/.openclaw/workspace")
INTEGRATIONS = WORKSPACE / "integrations/tldv"
LOG_DIR = WORKSPACE / "logs"

os.environ.setdefault("TLDV_API_KEY", "69f9a821-7286-46e8-a64c-7c1f20a01576")
os.environ.setdefault("PYTHONPATH", str(INTEGRATIONS.parent)


def log(msg, verbose_only=False):
    ts = datetime.now().isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    if verbose_only and not ARGS.verbose:
        return
    print(line)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_DIR / "tldv_pipeline.log", "a") as f:
        f.write(line + "\n")


def run_python(script: Path, extra_args: list[str] = (), timeout: int = 300) -> bool:
    """Executa script Python do pipeline. Retorna True se OK."""
    env = dict(os.environ)
    cmd = ["python3", str(script)] + extra_args
    log(f"  executando: {' '.join(cmd)}", verbose_only=True)
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
        )
        if result.returncode == 0:
            for line in result.stdout.strip().splitlines()[-5:]:
                log(f"    {line}", verbose_only=True)
            return True
        log(f"    FALHOU (rc={result.returncode}): {result.stderr[:200]}")
        return False
    except subprocess.TimeoutExpired:
        log(f"    TIMEOUT ({timeout}s)")
        return False
    except Exception as e:
        log(f"    ERRO: {e}")
        return False


def stage_collect(args) -> int:
    """Estágio 1: coleta reuniões novas."""
    log("=== ESTÁGIO 1: COLLECT ===")
    n_before = len(list((WORKSPACE / "memory/meetings/raw").glob("*.json")))
    ok = run_python(INTEGRATIONS / "collector.py", ["--dry-run"] if args.dry_run else [])
    n_after = len(list((WORKSPACE / "memory/meetings/raw").glob("*.json")))
    collected = n_after - n_before if ok else 0
    log(f"  Coletadas: {collected} reuniões (total: {n_after})")
    return collected


def stage_enrich(args) -> int:
    """Estágio 2: enrich reuniões pendentes."""
    log("=== ESTÁGIO 2: ENRICH ===")
    if args.dry_run:
        return run_python(INTEGRATIONS / "enricher.py", ["--dry-run"]) or 0
    ok = run_python(INTEGRATIONS / "enricher.py", ["--limit", "50"])
    return 50 if ok else 0


def stage_analyze(args) -> int:
    """Estágio 3: analisar reuniões enriquecidas."""
    log("=== ESTÁGIO 3: ANALYZE ===")
    if args.dry_run:
        return run_python(INTEGRATIONS / "analyzer.py", ["--dry-run", "--limit", "3"]) or 0

    # Roda analyzer em loop até não haver mais pendentes
    total = 0
    errors_seq = 0
    for _ in range(200):  # max 200 iterações
        # Contar pendentes
        analyzed_set = set()
        ledger = WORKSPACE / "memory/meetings/ledger/analyzed_ledger.json"
        if ledger.exists():
            with open(ledger) as f:
                analyzed_set = set(json.load(f).get("analyzed", []))

        norm_dir = WORKSPACE / "memory/meetings/normalized"
        normalized = [p.stem for p in norm_dir.glob("*.json")]
        pending = [m for m in normalized if m not in analyzed_set]

        if not pending:
            break

        next_id = pending[0]
        log(f"  Analisando: {next_id} ({len(pending)} pendentes)")
        ok = run_python(INTEGRATIONS / "analyzer.py", ["--meeting-id", next_id], timeout=300)

        if ok:
            total += 1
            errors_seq = 0
        else:
            errors_seq += 1
            log(f"  Erro #{errors_seq}")
            if errors_seq >= 5:
                log("  5 erros seguidos — abortando enrich")
                break
        time.sleep(5)

    log(f"  Total analisadas nesta execução: {total}")
    return total


def stage_persist(args) -> dict:
    """Estágio 4: persistir análises em memória."""
    log("=== ESTÁGIO 4: PERSIST ===")
    if args.dry_run:
        run_python(WORKSPACE / "integrations/tldv/persister.py", ["--dry-run"])
        return {}

    ledger = WORKSPACE / "memory/meetings/ledger/persisted_ledger.json"
    before = 0
    if ledger.exists():
        with open(ledger) as f:
            before = len(json.load(f).get("persisted", []))

    run_python(WORKSPACE / "integrations/tldv/persister.py", [], timeout=60)

    if ledger.exists():
        with open(ledger) as f:
            after = json.load(f)
        written = len(after.get("persisted", [])) - before
        result = {"written": written, "total": len(after.get("persisted", []))}
        log(f"  Novos itens persistidos: {written}")
        return result
    return {}


def stage_digest(args) -> Path:
    """Estágio 5: gerar digest consolidado."""
    log("=== ESTÁGIO 5: DIGEST ===")

    # Lê análises recentes
    analysis_dir = WORKSPACE / "memory/meetings/analysis"
    since_dt = None
    if args.since:
        since_dt = datetime.fromisoformat(args.since)

    analyses = []
    for p in sorted(analysis_dir.glob("*.json")):
        try:
            with open(p) as f:
                d = json.load(f)
            if since_dt:
                happened = d.get("happened_at", "")
                if happened:
                    dt = datetime.fromisoformat(happened.replace("Z", "+00:00"))
                    if dt < since_dt:
                        continue
            analyses.append(d)
        except Exception:
            pass

    if not analyses:
        log("  Nenhuma análise para gerar digest.")
        return None

    # Sumário agregado
    decisions = []
    tasks = []
    risks = []
    opportunities = []
    meetings_with_tx = []
    meetings_without_tx = []

    for a in analyses:
        mid = a.get("meeting_id", "?")
        happened = a.get("happened_at", "")[:10] if a.get("happened_at") else "?"
        name = a.get("name", "?")[:60]
        has_tx = a.get("transcript_status") == "available"
        has_notes = a.get("notes_status") == "available"

        if has_tx:
            meetings_with_tx.append(mid)
        else:
            meetings_without_tx.append(mid)

        for d in a.get("decisions", []):
            if d.get("confidence") in ("confirmed", "likely"):
                decisions.append(f"[{happened}] {d['description'][:100]}")
        for t in a.get("tasks", []):
            tasks.append(f"[{happened}] {t['description'][:100]}")
        for r in a.get("risks_and_alerts", []):
            if r.get("severity") == "high":
                risks.append(f"[{happened}] [{r.get('type','?')}] {r['description'][:100]}")
        for o in a.get("opportunities", []):
            if o.get("potential_impact") == "high":
                opportunities.append(f"[{happened}] {o['description'][:100]}")

    # Gerar digest
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    since_str = f" desde {args.since}" if args.since else " (última execução)"

    digest_lines = [
        f"# tl;dv Digest{since_str}",
        f"**Gerado em:** {now}",
        f"**Reuniões analisadas:** {len(analyses)}",
        f"**Com transcript:** {len(meetings_with_tx)} | **Sem:** {len(meetings_without_tx)}",
        "",
        "---",
        "",
        f"## Decisões ({len(decisions)})",
        *[f"- {d}" for d in decisions[:20]],
        "",
        f"## Tarefas Geradas ({len(tasks)})",
        *[f"- {t}" for t in tasks[:15]],
        "",
        f"## Riscos High ({len(risks)})",
        *[f"- {r}" for r in risks[:10]],
        "",
        f"## Oportunidades High ({len(opportunities)})",
        *[f"- {o}" for o in opportunities[:10]],
        "",
        f"## Reuniões sem Transcript ({len(meetings_without_tx)})",
        *[f"- `{m}`" for m in meetings_without_tx[:10]],
        "",
        "---",
        f"*Digest gerado por Morfeu | pipeline tl;dv*",
    ]

    digest_file = LOG_DIR / f"tldv_digest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    digest_file.write_text("\n".join(digest_lines))
    log(f"  Digest gerado: {digest_file.name}")
    return digest_file


def run(args):
    stages = args.stages  # comma-separated

    log(f"=== PIPELINE tl;dv | stages={stages} | dry={args.dry_run} ===")
    results = {}

    if "collect" in stages:
        results["collect"] = stage_collect(args)

    if "enrich" in stages:
        results["enrich"] = stage_enrich(args)

    if "analyze" in stages:
        results["analyze"] = stage_analyze(args)

    if "persist" in stages:
        results["persist"] = stage_persist(args)

    if "digest" in stages:
        digest_file = stage_digest(args)
        results["digest"] = str(digest_file) if digest_file else None

    log("=== PIPELINE FINALIZADO ===")
    for k, v in results.items():
        log(f"  {k}: {v}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Pipeline tl;dv — Morfeu")
    parser.add_argument(
        "--stage",
        type=str,
        default="collect,enrich,analyze,persist",
        help="Estágios a executar (comma-separated). Default: collect,enrich,analyze,persist",
    )
    parser.add_argument("--meeting-id", type=str, default="", help="Pipeline para uma reunião específica")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--since", type=str, default="", help="Data mínima (YYYY-MM-DD)")
    parser.add_argument("--force", action="store_true", help="Reprocessa mesmo se já existe")
    global ARGS
    ARGS = parser.parse_args()

    if ARGS.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    stages = [s.strip() for s in ARGS.stage.split(",")]

    if ARGS.meeting_id:
        # Executa pipeline completo para 1 reunião
        for stage_fn, name in [
            (stage_enrich, "enrich"),
            (stage_analyze, "analyze"),
            (stage_persist, "persist"),
        ]:
            log(f"=== {name.upper()} para {ARGS.meeting_id} ===")
            if name == "enrich":
                # enricher não tem --meeting-id, usa collector → enricher
                run_python(WORKSPACE / "integrations/tldv/enricher.py", ["--meeting-id", ARGS.meeting_id])
            elif name == "analyze":
                run_python(WORKSPACE / "integrations/tldv/analyzer.py", ["--meeting-id", ARGS.meeting_id])
            else:
                stage_fn(ARGS)
        return

    run(ARGS)


ARGS = None  # global for log()

if __name__ == "__main__":
    main()
