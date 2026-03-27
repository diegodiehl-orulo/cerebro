#!/usr/bin/env python3
"""
trinks_booking.py — Integração com Trinks para agendamento automático de cabelo

USO:
  python3 trinks_booking.py --check                 # Verifica disponibilidade próxima janela
  python3 trinks_booking.py --check --date 2026-03-24  # Verifica data específica
  python3 trinks_booking.py --book --date 2026-03-24 --time 10:00   # Simula (dry-run)
  python3 trinks_booking.py --book --date 2026-03-24 --time 10:00 --confirm  # Agenda de verdade

⚠️  ATENÇÃO: --confirm agenda de verdade. Nunca usar em scripts automatizados sem aprovação.

FLUXO DE AUTOMAÇÃO (cron de domingo):
  1. Verificar se Diego está em SP na janela (21–28 dias após último corte)
  2. Consultar disponibilidade do Moisés nos dias disponíveis
  3. Sugerir 2-3 horários via Telegram → aguardar aprovação de Diego
  4. Só após "bora" ou confirmação explícita: agendar com --confirm

CREDENCIAIS:
  - URL: https://www.trinks.com/barbearia-retrogol/framebusca
  - Login: diegodiehl0@gmail.com
  - Senha: variável de ambiente TRINKS_PASSWORD ou argumento --senha

CONSTANTES:
  - ESTAB_ID: 18557 (Barbearia RetroGol)
  - PROFISSIONAL_ID: 676076 (Moisés)
  - SERVICO_ID: 1329815 (Corte de Cabelo, 40min, R$137)
"""

import argparse
import json
import os
import sys
from datetime import date, timedelta
from typing import Optional

# ─────────────────────────────────────────
# CONSTANTES
# ─────────────────────────────────────────
BASE_URL       = "https://www.trinks.com"
ESTAB_ID       = 18557
PROFISSIONAL_ID = 676076
SERVICO_ID     = 1329815
DURACAO_MIN    = 40
PRECO          = 137.0

TRINKS_EMAIL   = "diegodiehl0@gmail.com"
TRINKS_PASSWORD_ENV = "TRINKS_PASSWORD"

# Janela padrão entre cortes (dias)
JANELA_MIN = 21
JANELA_MAX = 28


# ─────────────────────────────────────────
# AUTH
# ─────────────────────────────────────────
def _get_cookies(password: str) -> dict:
    """Autentica na Trinks via Playwright e retorna os cookies de sessão."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Erro: playwright não instalado. Execute: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
        )
        page = ctx.new_page()

        page.goto(f"{BASE_URL}/login", wait_until="domcontentloaded", timeout=20000)
        page.wait_for_timeout(2000)

        page.locator('input[type="text"]').nth(0).fill(TRINKS_EMAIL)
        page.locator('input[type="password"]').nth(0).fill(password)
        page.wait_for_timeout(500)
        page.get_by_role("button", name="Entrar").click()
        page.wait_for_timeout(3500)

        cookies = {c["name"]: c["value"] for c in ctx.cookies()}
        browser.close()

        if "TokenApiTrinks" not in cookies:
            print("Erro: login falhou — TokenApiTrinks não encontrado nos cookies.", file=sys.stderr)
            sys.exit(1)

        return cookies


def _auth_headers(cookies: dict) -> dict:
    token = cookies.get("TokenApiTrinks", "")
    cookie_str = "; ".join([f"{k}={v}" for k, v in cookies.items()])
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "Cookie": cookie_str,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }


# ─────────────────────────────────────────
# DISPONIBILIDADE
# ─────────────────────────────────────────
def get_availability(cookies: dict, target_date: date) -> list[str]:
    """
    Retorna lista de horários disponíveis com Moisés na data informada.
    Ex: ['10:00', '10:15', '10:30', ...]
    Retorna [] se sem horários ou fora do expediente.
    """
    import urllib.request

    url = (
        f"{BASE_URL}/api/v2/servicos/{SERVICO_ID}/profissionais"
        f"?IdProfissionalEstabelecimento={PROFISSIONAL_ID}"
        f"&data={target_date.isoformat()}"
    )

    req = urllib.request.Request(url, headers=_auth_headers(cookies))
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"Erro ao consultar disponibilidade para {target_date}: {e}", file=sys.stderr)
        return []

    if not data or not isinstance(data, list):
        return []

    for prof in data:
        if prof.get("id") == PROFISSIONAL_ID:
            return prof.get("horarios", [])

    return []


def check_window(cookies: dict, start_date: date, end_date: date) -> dict:
    """
    Verifica disponibilidade em um range de datas.
    Retorna dict {data_iso: [horários]}, ignorando datas sem horários.
    """
    results = {}
    current = start_date
    while current <= end_date:
        horarios = get_availability(cookies, current)
        if horarios:
            results[current.isoformat()] = horarios
        current += timedelta(days=1)
    return results


# ─────────────────────────────────────────
# AGENDAMENTO
# ─────────────────────────────────────────
def book_appointment(
    cookies: dict,
    target_date: date,
    time_str: str,
    dry_run: bool = True,
    comment: str = "",
) -> dict:
    """
    Agenda Corte de Cabelo com Moisés.

    Args:
        cookies: cookies de sessão autenticada
        target_date: data do agendamento
        time_str: horário no formato HH:MM (ex: '10:00')
        dry_run: se True (padrão), apenas simula — NÃO agenda de verdade
        comment: comentário opcional para o barbeiro

    Returns:
        dict com resultado ou simulação
    """
    payload = {
        "idServicoEstabelecimento": str(SERVICO_ID),
        "idProfissional": str(PROFISSIONAL_ID),
        "idEstabelecimento": ESTAB_ID,
        "dataHora": f"{target_date.isoformat()} {time_str}",
        "comentarios": comment,
        "origem": 4,
    }

    if dry_run:
        print(f"\n[DRY-RUN] Agendamento simulado:")
        print(f"  Data/hora : {target_date.isoformat()} {time_str}")
        print(f"  Serviço   : Corte de Cabelo (ID {SERVICO_ID})")
        print(f"  Profissional: Moisés (ID {PROFISSIONAL_ID})")
        print(f"  Valor     : R$ {PRECO:.2f}")
        print(f"  Payload   : {json.dumps(payload, ensure_ascii=False)}")
        print(f"\n  ⚠️  Para agendar de verdade, use --confirm")
        return {"dry_run": True, "payload": payload}

    # ─── AGENDAMENTO REAL ───
    import urllib.request

    url = f"{BASE_URL}/api/v2/agendamentos"
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=_auth_headers(cookies), method="POST")

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read())
            print(f"\n✅ Agendamento confirmado!")
            print(f"  ID: {result.get('idAgendamento')}")
            print(f"  Status: {result.get('descricao')}")
            return result
    except Exception as e:
        print(f"Erro ao agendar: {e}", file=sys.stderr)
        return {"error": str(e)}


# ─────────────────────────────────────────
# SUGESTÃO AUTOMÁTICA (para cron)
# ─────────────────────────────────────────
def suggest_for_cron(
    cookies: dict,
    ultimo_corte: date,
    viagens: list[tuple[date, date]] = None,
) -> str:
    """
    Verifica disponibilidade na janela de 21-28 dias após último corte.
    Filtra dias em que Diego está em viagem.
    Retorna mensagem formatada para enviar via Telegram.

    Args:
        cookies: cookies autenticados
        ultimo_corte: data do último corte
        viagens: lista de (data_inicio, data_fim) de viagens previstas
    """
    janela_inicio = ultimo_corte + timedelta(days=JANELA_MIN)
    janela_fim    = ultimo_corte + timedelta(days=JANELA_MAX)
    hoje          = date.today()

    # Não sugerir datas passadas
    if janela_inicio < hoje:
        janela_inicio = hoje

    print(f"Janela: {janela_inicio} a {janela_fim}")

    # Dias em viagem (não considerar)
    dias_viagem = set()
    if viagens:
        for v_ini, v_fim in viagens:
            d = v_ini
            while d <= v_fim:
                dias_viagem.add(d)
                d += timedelta(days=1)

    # Consultar disponibilidade
    disponiveis = {}
    current = janela_inicio
    while current <= janela_fim:
        # Pular fins de semana? Não — barbearia abre sábado
        # Pular viagens
        if current not in dias_viagem:
            horarios = get_availability(cookies, current)
            if horarios:
                # Filtrar horários úteis (evitar horários de reunião fixas)
                # Horários preferenciais: manhã 09-11h ou tarde 12-15h
                preferenciais = [h for h in horarios if (
                    ("09:" in h or "10:" in h or "11:" in h or
                     "12:" in h or "13:" in h or "14:" in h or "15:" in h)
                )]
                if preferenciais:
                    # Priorizar segunda-feira 11:30 (preferência de Diego)
                    if current.weekday() == 0:  # Segunda-feira
                        preferred_first = [h for h in preferenciais if h in ("11:15", "11:30", "11:45", "12:00")]
                        others = [h for h in preferenciais if h not in preferred_first]
                        preferenciais = preferred_first + others
                    disponiveis[current] = preferenciais[:4]  # sempre 4 opções
        current += timedelta(days=1)

    if not disponiveis:
        msg = (
            f"💈 *Cabelo — Nenhum horário disponível*\n"
            f"Janela: {janela_inicio.strftime('%d/%m')} a {janela_fim.strftime('%d/%m')}\n"
            f"Moisés não tem horários disponíveis no período. "
            f"Verificar manualmente: https://www.trinks.com/barbearia-retrogol/framebusca"
        )
    else:
        linhas = [f"💈 *Cabelo — Horários disponíveis com Moisés*"]
        linhas.append(f"_Janela: {janela_inicio.strftime('%d/%m')} a {janela_fim.strftime('%d/%m')}_\n")
        for d, horarios in sorted(disponiveis.items()):
            dia_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"][d.weekday()]
            linhas.append(f"*{dia_semana} {d.strftime('%d/%m')}:* {' · '.join(horarios)}")
        linhas.append(f"\nPara confirmar, me diga a data e horário.")
        msg = "\n".join(linhas)

    return msg


# ─────────────────────────────────────────
# CLI
# ─────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Integração Trinks — Consulta e agendamento com Moisés (Barbearia RetroGol)"
    )
    parser.add_argument("--check", action="store_true",
                        help="Verificar disponibilidade na janela padrão ou data específica")
    parser.add_argument("--book", action="store_true",
                        help="Simular (ou confirmar) agendamento")
    parser.add_argument("--suggest", action="store_true",
                        help="Modo cron: gerar sugestão de horários para Telegram")
    parser.add_argument("--date", type=str, help="Data alvo (YYYY-MM-DD)")
    parser.add_argument("--time", type=str, help="Horário (HH:MM) — necessário com --book")
    parser.add_argument("--confirm", action="store_true",
                        help="⚠️ CONFIRMAR agendamento real (sem isso, apenas simula)")
    parser.add_argument("--ultimo-corte", type=str, help="Data do último corte (YYYY-MM-DD) — para --suggest")
    parser.add_argument("--senha", type=str,
                        help=f"Senha Trinks (ou use env {TRINKS_PASSWORD_ENV})")
    args = parser.parse_args()

    # Resolver senha
    senha = args.senha or os.environ.get(TRINKS_PASSWORD_ENV)
    if not senha:
        print(f"Erro: informe --senha ou defina {TRINKS_PASSWORD_ENV}", file=sys.stderr)
        sys.exit(1)

    print("Autenticando na Trinks...")
    cookies = _get_cookies(senha)
    print("✅ Autenticado\n")

    # ─── --check ───
    if args.check:
        if args.date:
            target = date.fromisoformat(args.date)
            horarios = get_availability(cookies, target)
            print(f"Disponibilidade em {target.strftime('%d/%m/%Y')} com Moisés:")
            if horarios:
                # Agrupar por período
                manha  = [h for h in horarios if int(h.split(":")[0]) < 12]
                tarde  = [h for h in horarios if 12 <= int(h.split(":")[0]) < 18]
                noite  = [h for h in horarios if int(h.split(":")[0]) >= 18]
                if manha:  print(f"  Manhã: {', '.join(manha)}")
                if tarde:  print(f"  Tarde: {', '.join(tarde)}")
                if noite:  print(f"  Noite: {', '.join(noite)}")
            else:
                print("  Sem horários disponíveis nesta data.")
        else:
            # Janela padrão: próximos 14 dias
            inicio = date.today()
            fim    = inicio + timedelta(days=14)
            resultado = check_window(cookies, inicio, fim)
            if resultado:
                print(f"Horários disponíveis ({inicio.strftime('%d/%m')} a {fim.strftime('%d/%m')}):")
                for d, horarios in sorted(resultado.items()):
                    dt = date.fromisoformat(d)
                    dia = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"][dt.weekday()]
                    print(f"  {dia} {dt.strftime('%d/%m')}: {', '.join(horarios)}")
            else:
                print("Nenhum horário disponível nos próximos 14 dias.")

    # ─── --book ───
    elif args.book:
        if not args.date or not args.time:
            print("Erro: --book requer --date (YYYY-MM-DD) e --time (HH:MM)", file=sys.stderr)
            sys.exit(1)
        target = date.fromisoformat(args.date)
        dry_run = not args.confirm

        if args.confirm:
            print("⚠️  MODO REAL ATIVADO — vai agendar de verdade!")

        result = book_appointment(cookies, target, args.time, dry_run=dry_run)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    # ─── --suggest ───
    elif args.suggest:
        if args.ultimo_corte:
            ultimo = date.fromisoformat(args.ultimo_corte)
        else:
            ultimo = date(2026, 3, 2)  # padrão: último corte registrado
            print(f"(usando último corte padrão: {ultimo})")

        msg = suggest_for_cron(cookies, ultimo)
        print("\n=== MENSAGEM PARA TELEGRAM ===")
        print(msg)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
