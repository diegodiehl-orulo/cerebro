#!/bin/bash
# DEPRECATED — mantido apenas como wrapper de compatibilidade.
# A lista de IDs agora vive em integrations/tldv/id-lists/lote2_2026.txt
# e a rotina é run_tldv.sh (portável, .env-based).
#
# Use diretamente:
#   ./run_tldv.sh ids --ids-file integrations/tldv/id-lists/lote2_2026.txt

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "$SCRIPT_DIR/run_tldv.sh" ids --ids-file "$SCRIPT_DIR/integrations/tldv/id-lists/lote2_2026.txt" "$@"
