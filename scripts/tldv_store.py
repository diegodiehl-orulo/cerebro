#!/usr/bin/env python3
"""
tldv_store.py — Processa reuniões tl;dv e extrai valor
Etapa 2 do pipeline: Lê pending, processa com IA, salva estruturado
"""
import json, re, sys
from pathlib import Path
from datetime import datetime

PENDING_PATH = Path('/root/.config/morfeu/tldv_pending.json')
PROCESSED_LIST = Path('/root/.config/morfeu/tldv_processed.json')
STORE_DIR = Path('/root/.config/morfeu/tldv_store')
ACTIONS_DIR = Path('/root/.config/morfeu/tldv_actions')

def load_processed():
    if PROCESSED_LIST.exists():
        return set(json.loads(PROCESSED_LIST.read_text()))
    return set()

def save_processed(ids):
    PROCESSED_LIST.write_text(json.dumps(list(ids)))

def extract_actions_from_body(body):
    """Extrai action items do body HTML"""
    actions = []
    
    # Padrões de action items
    patterns = [
        r'([A-Z][a-z]+)\s+(revisar|enviar|criar|montar|preparar|alinh|confirmar|verificar|definir|agendar)\s+(.+?)(?:\n|$)',
        r'•\s+([A-Z][a-z]+)\s+—\s+(.+?)(?:\n|$)',
        r'([A-Z][a-z]+)\s+(?:vai|irá|deve)\s+(.+?)(?:\n|$)',
    ]
    
    # Palavras-chave de ação
    action_keywords = ['revisar', 'enviar', 'criar', 'montar', 'preparar', 'alinh', 
                       'confirmar', 'verificar', 'definir', 'agendar', 'compartilhar',
                       'atualizar', 'produzir', 'mandar', 'passar', 'fazer']
    
    lines = body.split('\n')
    current_action = None
    current_owner = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Detecta início de lista de ações
        if 'Itens de Ação' in line or 'Próximos passos' in line or 'Action Items' in line:
            current_action = 'actions'
            continue
            
        # Se tem • ou numeração, extrai
        if line.startswith('•') or re.match(r'^\d+[\.\)]', line):
            text = re.sub(r'^[•\d\.\)]+\s*', '', line)
            
            # Extrai dono (primeira palavra que parece nome)
            words = text.split()
            owner = None
            action_text = text
            
            for i, word in enumerate(words):
                if word and word[0].isupper() and len(word) > 2:
                    # Assume que é nome se tiver pelo menos 2 letras maiúsculas
                    if sum(1 for c in word if c.isupper()) >= 1 and word.lower() not in action_keywords:
                        owner = word
                        action_text = ' '.join(words[i+1:])
                        break
            
            # Limpa texto
            action_text = re.sub(r'\s+\d{2}:\d{2}.*$', '', action_text)  # Remove timestamps
            action_text = action_text.strip('.,;:')
            
            if action_text and len(action_text) > 5:
                actions.append({
                    'owner': owner,
                    'action': action_text,
                    'source': 'bullet'
                })
    
    return actions

def generate_email_prompt(meeting_data, actions):
    """Gera texto pronto para email/follow-up"""
    title = meeting_data.get('subject', '').replace('Anotações e respostas por IA da reunião "', '').replace('" estão prontas ✅', '')
    
    text = f"Resumo: {title}\n\n"
    
    if actions:
        text += "Ações:\n"
        for a in actions[:5]:
            owner = a.get('owner', '[don@]')
            text += f"- {owner}: {a.get('action', '')}\n"
    
    text += "\nPróximos passos: a definir"
    
    return text

def process_meeting(meeting_data):
    """Processa uma reunião e salva estruturado"""
    meeting_id = meeting_data.get('id', '')
    date_str = meeting_data.get('date', '')
    
    # Parse data
    try:
        dt = datetime.strptime(date_str[:25], '%a, %d %b %Y %H:%M:%S')
        date_folder = dt.strftime('%Y-%m-%d')
    except:
        date_folder = datetime.now().strftime('%Y-%m-%d')
    
    # Cria diretórios
    meeting_dir = STORE_DIR / date_folder
    meeting_dir.mkdir(parents=True, exist_ok=True)
    
    # Extrai actions
    actions = extract_actions_from_body(meeting_data.get('body', ''))
    
    # Prepara dados estruturados
    structured = {
        'id': meeting_id,
        'subject': meeting_data.get('subject', ''),
        'date': date_str,
        'processed_at': datetime.now().isoformat(),
        'actions_count': len(actions),
        'actions': actions,
        'body_preview': meeting_data.get('body', '')[:500]
    }
    
    # Salva meeting completo
    meeting_file = meeting_dir / f"{meeting_id}.json"
    meeting_file.write_text(json.dumps(structured, ensure_ascii=False, indent=2))
    
    # Salva actions separado
    if actions:
        actions_file = ACTIONS_DIR / f"{meeting_id}_actions.json"
        actions_file.write_text(json.dumps(actions, ensure_ascii=False, indent=2))
    
    # Gera email prompt
    email_prompt = generate_email_prompt(meeting_data, actions)
    
    return structured, email_prompt

def main():
    # Garante diretórios
    STORE_DIR.mkdir(parents=True, exist_ok=True)
    ACTIONS_DIR.mkdir(parents=True, exist_ok=True)
    
    if not PENDING_PATH.exists():
        print("NONE")
        sys.exit(0)
    
    # Lê pending
    meeting_data = json.loads(PENDING_PATH.read_text())
    
    # Processa
    processed = load_processed()
    meeting_id = meeting_data.get('id', '')
    
    if meeting_id in processed:
        print("ALREADY_PROCESSED")
        sys.exit(0)
    
    structured, email_prompt = process_meeting(meeting_data)
    
    # Marca como processado
    processed.add(meeting_id)
    save_processed(processed)
    
    # Limpa pending
    PENDING_PATH.unlink()
    
    # Output
    print(f"PROCESSED: {structured['subject'][:50]}")
    print(f"ACTIONS: {len(structured['actions'])}")
    print(f"EMAIL_PROMPT:\n{email_prompt}")

if __name__ == '__main__':
    main()
