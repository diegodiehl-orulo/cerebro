#!/usr/bin/env python3
"""
tl;dv Sócio Detector — Morfeu
Verifica se uma reunião processada pelo tl;dv envolve sócios locais de praça.
Usado como check auxiliar ao Monitor tl;dv.
Saída: SOCIO_FOUND:<json> ou NONE
"""
import json, re
from pathlib import Path

PENDING_FILE   = '/root/.config/morfeu/tldv_pending.json'
PROCESSED_DIR  = '/root/.config/morfeu/tldv_processed/'

# Palavras-chave para detectar reunião de sprint/praça
SPRINT_KEYWORDS = [
    'sprint', 'one-pager', 'one pager', 'praça', 'praca',
    'governança', 'governanca', 'sócio local', 'socio local',
    'curitiba', 'vitória', 'vitoria',
]

# Sócios locais — nomes e variações
SOCIOS = [
    {'nome': 'Pedro Kneip', 'praca': 'Vitória',  'variantes': ['pedro kneip', 'kneip', 'pkneip']},
    {'nome': 'Zanella',     'praca': 'Curitiba', 'variantes': ['zanella', 'luiz zanella', 'gustavo zanella', 'luiz gustavo zanella']},
]

def check_for_socio(text):
    """Retorna o sócio encontrado no texto, ou None."""
    text_lower = text.lower()
    for socio in SOCIOS:
        if any(v in text_lower for v in socio['variantes']):
            return socio
    return None

def has_sprint_context(text):
    """Verifica se o texto tem contexto de sprint/praça."""
    text_lower = text.lower()
    return any(k in text_lower for k in SPRINT_KEYWORDS)

def main():
    # 1. Verificar pending file (reunião sendo processada agora)
    pending = Path(PENDING_FILE)
    if pending.exists():
        try:
            data = json.loads(pending.read_text())
            full_text = f"{data.get('subject','')} {data.get('body','')}"
            socio = check_for_socio(full_text)
            if socio:
                result = {
                    'source':   'tldv_pending',
                    'socio':    socio['nome'],
                    'praca':    socio['praca'],
                    'title':    data.get('subject', '(sem título)'),
                    'date':     data.get('date', ''),
                    'has_sprint_context': has_sprint_context(full_text),
                }
                print(f"SOCIO_FOUND:{json.dumps(result, ensure_ascii=False)}")
                return
        except Exception:
            pass

    # 2. Verificar últimas reuniões processadas (tldv_processed/)
    proc_dir = Path(PROCESSED_DIR)
    if proc_dir.exists():
        files = sorted(proc_dir.glob('*.json'), key=lambda f: f.stat().st_mtime, reverse=True)
        for f in files[:5]:  # últimas 5 reuniões
            try:
                data = json.loads(f.read_text())
                full_text = f"{data.get('subject','')} {data.get('body','')}"
                socio = check_for_socio(full_text)
                if socio:
                    already_flagged = data.get('sprint_flagged', False)
                    if not already_flagged:
                        result = {
                            'source':   f'tldv_processed:{f.name}',
                            'socio':    socio['nome'],
                            'praca':    socio['praca'],
                            'title':    data.get('subject', '(sem título)'),
                            'date':     data.get('date', ''),
                            'has_sprint_context': has_sprint_context(full_text),
                        }
                        # Marcar como flagged para não alertar duas vezes
                        data['sprint_flagged'] = True
                        f.write_text(json.dumps(data, ensure_ascii=False))
                        print(f"SOCIO_FOUND:{json.dumps(result, ensure_ascii=False)}")
                        return
            except Exception:
                continue

    print("NONE")

if __name__ == '__main__':
    main()
