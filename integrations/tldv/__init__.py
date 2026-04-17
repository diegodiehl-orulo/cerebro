"""tl;dv integration package — Morfeu pipeline de reuniões.

Módulos:
    client       — wrapper HTTP para tl;dv API
    collector    — coleta metadata de reuniões novas
    enricher     — baixa e processa transcrições
    analyzer     — análise LLM estágio 3
    persister    — salva resultados em memory/meetings/
    pipeline     — orquestra collect → enrich → analyze → persist → digest
    task_generator — gera tarefas para memory/tasks/ a partir de análises
    queue_processor — processa fila de webhooks tl;dv
    indexer      — mantém índice consultável
    summarizer   — gera resumos diários

Requer: TLDV_API_KEY no ambiente (ver .env.example).
"""
