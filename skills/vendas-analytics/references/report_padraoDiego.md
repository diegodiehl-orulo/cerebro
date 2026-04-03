# Report Padrão Diego — Estrutura Comparativa

## Estrutura do Report Padrão (Placar Mensal)

```
🏆 PLACAR DO MÊS – [MÊS] (ATUALIZADO)

🎯 Meta de Valor: R$ [valor]
📦 Meta de Contratos: [N] fechamentos

💰 R$ [valor vendido] — [percentual] da meta de valor
📄 [N] de [N] contratos fechados — [percentual] da meta de contratos

🗓 [%] do tempo
📈 Linha de ritmo: R$ [valor] até hoje

⚠️ Percentual do valor esperado: [cálculo]
```

## Seções do Report

### 1. Fechamentos de Março (Vendas Normais)
Formato: `UF – Cidade – Incorporadora – SDR – Closer`
Organizado por tier de valor (R$524,48 | R$655,61 | R$959,03 | Outros)

### 2. Resumo por UF
```
UF: [N] contratos – R$ [valor]
```

### 3. Z2A (separado — 32,8% da mensalidade)
Lista de deals Z2A com valor líquido
Total Z2A separado no cálculo

### 4. Total Considerado para Meta
Soma de todas as vendas normais + Z2A

## Campos para comparar

| Campo Report | Campo Planilha | Verificar |
|---|---|---|
| Cidade/UF | B (UF) + C (RM) | UF correta |
| Incorporadora | A (Nome) | Nome exato |
| SDR | N (Nome do SDR) | Quem agendou |
| Closer | O (Pessoa responsável) | Quem fechou |
| Valor mensal | F (Mensalidade Total) | Valor exato R$ |
| Tipo | E (Tipo de Contrato) | DA / Z2A / etc |

## Divergências a detectar

1. **Deal no report mas não na planilha** → Gustavo precisa cadastrar
2. **Deal na planilha mas não no report** →verificar se é 2026 (ainda não fechado no report?)
3. **Valor diferente** →verificar se houve mudança de plano
4. **SDR diferente** →verificar alinhamento de crédito
5. **UF diferente** →erro de digitação na planilha

## Status de preenchimento (meta: 100% para deals 2026)

### Colunas SDR (Q, R)
- Q: "(SDR) O que levou o contato a aceitar a reunião com a Órulo?"
- R: "(SDR) Qual foi o contexto atual da incorporadora?"

### Colunas Closer (S, T, U, V, W, X)
- S: "(CLOSER) Principal gargalo identificado"
- T: "(CLOSER) O que mais chamou atenção do cliente?"
- U: "(CLOSER) Entrega de valor que mais se conectou"
- V: "(CLOSER) O que levou a decidir contratar?"
- W: "(CLOSER) Por que não tinha contratado antes?"
- X: "(CLOSER) Outras frentes/soluções abordadas"

## Tiers de valor (report padrão)
- R$ 524,48
- R$ 655,61
- R$ 959,03
- Outros (acima ou abaixo dos padrão)
