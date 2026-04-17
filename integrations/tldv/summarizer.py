#!/usr/bin/env python3
"""
summarizer.py — Estágio 2 do pipeline tl;dv
Resumo estruturado de cada reunião a partir do transcript completo.

Input:  memory/meetings/transcripts/{id}.txt
Output: memory/meetings/summaries/{id}.json
"""
import json, sys, re
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DIRS  # noqa: E402

TRANSCRIPT_DIR = DIRS["transcripts"]
SUMMARY_DIR = DIRS["summaries"]
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

def extract_metadata(transcript_text: str) -> dict:
    """Extrai metadata do início do transcript (se disponível)."""
    meta = {"title": "Reunião", "date": None, "participants": [], "duration_min": 0}
    
    lines = transcript_text.split("\n")
    if not lines:
        return meta
    
    # Tentar extrair data do nome do arquivo ou das primeiras linhas
    # e participantes dos primeiros [timestamp] Speaker: lines
    seen_speakers = set()
    for line in lines[:50]:
        m = re.match(r"\[(\d+):(\d+)\]\s+([^:]+):", line)
        if m:
            speaker = m.group(3).strip()
            if speaker and speaker not in ("Unknown", "?", "Speaker"):
                seen_speakers.add(speaker)
    
    if seen_speakers:
        meta["participants"] = sorted(list(seen_speakers))
    
    # Estimar duração do último timestamp
    timestamps = []
    for line in lines:
        m = re.search(r"\[(\d+):(\d+)\]", line)
        if m:
            timestamps.append(int(m.group(1)) * 60 + int(m.group(2)))
    if timestamps:
        meta["duration_min"] = max(timestamps) // 60
    
    return meta


def build_summary_blocks(transcript_text: str) -> list:
    """
    Segmenta o transcript em blocos temáticos e gera um resumo
    estruturado para cada bloco.
    
    Blocos: tema identificado + bullets de pontos discutidos.
    """
    lines = transcript_text.split("\n")
    
    # Separar por falantes para identificar trocas de assunto
    blocks = []
    current_block = {"speaker": None, "turns": []}
    
    for line in lines:
        m = re.match(r"\[(\d+):(\d+)\]\s+([^:]+):\s*(.*)", line)
        if not m:
            continue
        
        timestamp = int(m.group(1)) * 60 + int(m.group(2))
        speaker = m.group(3).strip()
        text = m.group(4).strip()
        
        if not text:
            continue
        
        # Nova fala do mesmo bloco
        if current_block["speaker"] is None:
            current_block["speaker"] = speaker
        
        # Se mudou de tema (muito tempo sem falar ou muitas pessoas)
        if current_block["speaker"] != speaker and timestamp > 0:
            # Quebrar bloco a cada ~5 minutos ou troca significativa
            if current_block["turns"]:
                blocks.append(current_block)
            current_block = {"speaker": speaker, "turns": []}
        
        if text:
            current_block["turns"].append({
                "speaker": speaker,
                "timestamp_sec": timestamp,
                "text": text
            })
    
    if current_block["turns"]:
        blocks.append(current_block)
    
    # Gerar resumo por bloco (primeiras frases de cada turno)
    summary_blocks = []
    for block in blocks:
        turns = block["turns"]
        if not turns:
            continue
        
        #拼接 as primeiras frases de cada turno como "resumo do bloco"
        sample_texts = []
        for turn in turns[:5]:
            text = turn["text"]
            # Primeiras 200 chars como preview
            sample_texts.append(text[:200])
        
        combined = " | ".join(sample_texts[:3])
        
        # Estimar tema pelo conteúdo (palavras mais frequentes nos primeiros turnos)
        first_words = " ".join([t["text"].lower() for t in turns[:3]])
        topic_hint = first_words[:80].strip()
        
        summary_blocks.append({
            "start_sec": turns[0]["timestamp_sec"],
            "speakers": list(dict.fromkeys(t["speaker"] for t in turns)),
            "topic_hint": topic_hint,
            "content_preview": combined[:300],
            "turn_count": len(turns)
        })
    
    return summary_blocks


def extract_action_items(transcript_text: str) -> list:
    """
    Extrai action items do transcript procurando padrões como:
    - [ACTION] tags (seexistirem)
    - Frases com verbo no imperativo + pessoa/futuro
    - Menção a tarefas, prazos, responsáveis
    """
    actions = []
    lines = transcript_text.split("\n")
    
    action_indicators = [
        "vou", "vai", "preciso", "precisamos", "tem que", "deveria",
        "vamos", "irei", "far", "ação", "tarefa", "entregar",
        "ligar", "enviar", "mandar", "reunir", "agendar",
        "talk", "will", "need", "must", "should", "going to"
    ]
    
    for line in lines:
        line_lower = line.lower()
        if any(ind in line_lower for ind in action_indicators):
            m = re.search(r"\[(\d+):(\d+)\]\s+([^:]+):\s*(.*)", line)
            if m:
                speaker = m.group(3).strip()
                text = m.group(4).strip()
                if len(text) > 20 and len(text) < 500:
                    actions.append({
                        "speaker": speaker,
                        "timestamp": int(m.group(1)) * 60 + int(m.group(2)),
                        "text": text
                    })
    
    return actions[:10]  # Máximo 10 ações


def main(meeting_id: str = None):
    if meeting_id:
        ids = [meeting_id]
    else:
        # Processar todos os transcripts sem summary
        existing = set(p.stem for p in SUMMARY_DIR.glob("*.json"))
        ids = [p.stem for p in TRANSCRIPT_DIR.glob("*.txt") if p.stem not in existing]
    
    print(f"SUMMARIZER — {len(ids)} transcripts para processar")
    
    for mid in ids:
        tx_file = TRANSCRIPT_DIR / f"{mid}.txt"
        if not tx_file.exists():
            print(f"  ○ Sem transcript: {mid}")
            continue
        
        try:
            transcript = tx_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  ✗ Erro leitura {mid}: {e}")
            continue
        
        meta = extract_metadata(transcript)
        blocks = build_summary_blocks(transcript)
        actions = extract_action_items(transcript)
        
        summary = {
            "meeting_id": mid,
            "generated_at": datetime.now().isoformat(),
            "stage": "summary_v1",
            "metadata": meta,
            "blocks": blocks,
            "action_items_raw": actions,
            "transcript_length": len(transcript),
            "block_count": len(blocks)
        }
        
        out_file = SUMMARY_DIR / f"{mid}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        
        print(f"  ✅ {mid}: {len(blocks)} blocos, {len(actions)} ações — {meta.get('participants', [])[:3]}")
    
    print(f"\nPronto. Summaries salvos em {SUMMARY_DIR}")


if __name__ == "__main__":
    mid = sys.argv[1] if len(sys.argv) > 1 else None
    main(mid)
