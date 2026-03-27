---
title: "Memória Operacional: Piloto Estruturado HEARTBEAT v1.1"
status: "Ativo"
activation_date: "2026-03-13"
---

## Piloto do Modelo Estruturado HEARTBEAT — Ativo (13/03/2026)

### 1. Memória Executiva Consolidada
- **Status:** A fase “Piloto controlado do modelo estruturado HEARTBEAT” foi concluída com sucesso. O piloto está **ATIVO** em modo controlado.
- **Operação Híbrida:** `memory/pending.md` opera em modo híbrido (legado + estruturado).
- **Fonte de Verdade para Decisões:** `memory/decisions_pending.md` é a única fonte oficial para o registro de **novas** decisões pendentes.
- **Regra de Criação:** Todas as novas tarefas e decisões devem ser registradas no formato estruturado (YAML Front Matter).
- **Legado:** Itens antigos em `pending.md` permanecem intactos. Não haverá migração em massa nesta fase.

### 2. Regras Operacionais Ativas
1.  **DRI Único:** O campo `owner` deve conter um único responsável pela tarefa.
2.  **IDs Automáticos:** `task_id` e `decision_id` são gerados e atribuídos automaticamente pelo agente na criação do item.
3.  **`updated_at` Automático:** O campo é preenchido e atualizado automaticamente pelo agente a cada modificação.
4.  **Skills Baseadas em Estrutura:** As skills analíticas do HEARTBEAT (priorização, riscos, etc.) usam os dados estruturados como fonte primária.
5.  **Fallback de Qualidade:** Itens criados com campos obrigatórios ausentes recebem `status: "corrigir"` para garantir que não sejam perdidos.
6.  **Vínculo Explícito:** A ligação entre uma tarefa e uma decisão bloqueadora é feita pelo campo `blocked_by`.

### 3. Próximo Marco do Sistema
- **Escopo Atual:** O foco é estritamente no piloto do HEARTBEAT. Não fazem parte desta fase: rollout completo, migração do histórico legado em massa ou novas automações fora do escopo.
- **Próximo Marco Lógico:** Estabilização do piloto em ambiente de produção, monitoramento da adoção e coleta de feedback para definir os critérios de saída do modo controlado.
