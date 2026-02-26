# feedback/ — Registro de Aprovações e Rejeições

> O Morfeu consulta estes arquivos antes de sugerir algo pela segunda vez.
> Nunca repetir o que foi rejeitado. Sempre reforçar o que foi aprovado.

## Formato
```json
{
  "date": "YYYY-MM-DD",
  "context": "descrição breve da situação",
  "suggestion": "o que foi sugerido",
  "verdict": "approved | rejected",
  "reason": "por que Diego aprovou ou rejeitou",
  "apply_when": "em quais situações futuras considerar isso"
}
```

## Arquivos
- `approved.json` — o que funcionou bem
- `rejected.json` — o que não funcionou / Diego não quer que se repita
