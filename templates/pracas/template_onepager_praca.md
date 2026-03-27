# Relatorio de Sprint - {{ results.praca_context.name }}

**Periodo:** `{{ results.sprint_period.start_date }}` a `{{ results.sprint_period.end_date }}`
**Responsavel:** {{ results.praca_context.socio_local_dri }}

---

## Performance Geral

| Metrica | Valor |
|---|---|
| MRR | R$ {{ "%.2f"|format(results.kpis_validated.kpis.mrr) }} |
| Corretores Ativos | {{ results.kpis_validated.kpis.corretores_ativos }} |
| Deals Criados | {{ results.kpis_validated.kpis.deals_criados }} |

---

## Analise de Desvios

*Comparacao com o periodo anterior. Limiar: 10%.*

{% if results.deviations %}
| Metrica | Valor Atual | Valor Anterior | Variacao % |
|---|---|---|---|
{% for dev in results.deviations %}
| **{{ dev.kpi_name }}** | {{ dev.current_value }} | {{ dev.previous_value }} | **{{ "%.1f"|format(dev.delta_percent) if dev.delta_percent is number else dev.delta_percent }}** |
{% endfor %}
{% else %}
- Nenhum desvio significativo (>10%) identificado.
{% endif %}
