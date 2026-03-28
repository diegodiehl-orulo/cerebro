# ⚠️ PRIORITÁRIO — P8: REFINAMENTO DO MODELO ECONÔMICO POR PRAÇA (WS7)

**Versão:** 1.0
**Data de criação:** 26/03/2026
**Status:** PRONTO PARA RODAR
**DRI:** Diego Diehl
**WS associado:** WS7 — Modelo Econômico Praça
**Urgência:** ALTA — modelo implementado em Curitiba e Vitória, mas precisa de refinamento antes de escalar

---

## CONTEXTO

O WS7 define o modelo econômico por praça.

Seu escopo real vai além de remuneração:
- **Remuneração do Sócio-Local** (modelo implementado)
- **Projeções por praça** (parcialmente existentes)
- **Economico da praça** — unit economics, break-even, MRR esperado por praça

O modelo está **implementado em Curitiba e Vitória**, mas o próprio Diego reconhece que precisa ser refinado antes de escalar para novas praças.

Este prompt conduz esse refinamento de forma estruturada.

---

## INSTRUÇÃO PARA A IA

Você está atuando como Sistema Integrado de Gestão de OKRs e Inteligência Documental da Órulo.

Leia os arquivos do WS7 antes de iniciar (Charter, documentos absorvidos de março/2026).

Leia também os documentos de Bases CONSOLIDADAS relacionados a expansão territorial e modelo econômico.

Seu objetivo é conduzir uma revisão estruturada do modelo econômico por praça com Diego, propor refinamentos e documentar o modelo definitivo.

---

## ROTEIRO DE EXECUÇÃO

### ETAPA 1 — Diagnóstico do modelo atual (Curitiba e Vitória)

Conduza uma revisão do modelo vigente:

**Remuneração do Sócio-Local**

> Como está estruturada hoje em Curitiba? E em Vitória?
> É o mesmo modelo nas duas praças ou há variações?
> O que não está funcionando bem no modelo atual?
> O Sócio-Local entende claramente como é remunerado?

**Projeções por praça**

> Existe uma projeção de MRR por praça definida?
> Com qual horizonte (3 meses? 6 meses? 12 meses)?
> O modelo projetado está sendo comparado com o realizado?

**Unit economics**

> Qual o custo de ativação de uma praça (estimado)?
> Qual o MRR esperado no Break-even?
> Em quanto tempo Vitória deve atingir o break-even?
> E Curitiba?

---

### ETAPA 2 — Identificação de gaps e inconsistências

Com base nas respostas, identifique:

1. **O que está definido e funciona** → manter
2. **O que está definido mas não funciona** → corrigir
3. **O que está indefinido** → criar

Perguntas para detectar gaps:

> Quando entra uma nova praça, qual é o modelo econômico padrão de entrada?
> Existe um documento que Diego possa apresentar para um potencial Sócio-Local mostrando como o modelo funciona?
> O modelo tem gatilhos (ex: a partir de X MRR, a participação do Sócio-Local muda)?

---

### ETAPA 3 — Refinamento do modelo

Após o diagnóstico, proponha uma estrutura para o modelo refinado:

**Estrutura mínima do Modelo Econômico por Praça:**

```
1. ESTRUTURA DE REMUNERAÇÃO
   - Tipo: % de receita? Fix + variável? Participação?
   - Base de cálculo: sobre MRR, ARR ou new MRR?
   - Frequência de pagamento
   - Tabela de progressão (se existir)

2. PROJEÇÃO POR PRAÇA
   - MRR esperado: mês 3 / mês 6 / mês 12
   - Clientes esperados por estágio
   - Break-even: em MRR e em prazo

3. GATILHOS DE EVOLUÇÃO
   - O que muda quando a praça atinge X MRR?
   - Critério de expansão (segunda praça?)
   - Critério de encerramento (praça que não performa)

4. OBRIGAÇÕES DO SÓCIO-LOCAL
   - Métricas mínimas esperadas
   - Frequência de report
   - O que é responsabilidade dele vs da Órulo

5. OBRIGAÇÕES DA ÓRULO
   - Suporte que oferece
   - Ferramentas disponibilizadas
   - Acesso a eventos e materiais
```

---

### ETAPA 4 — Validação com praças ativas

Após propor o modelo refinado:

> O modelo descrito acima funciona para Curitiba como está hoje?
> E para Vitória?
> O que precisaria mudar para que ele funcione para uma terceira praça?

---

### ETAPA 5 — Documentação do modelo refinado

Após validação:

1. Crie `WS7_MODELO_ECONOMICO_PRACA_V2.md` na pasta do WS7
2. Estrutura obrigatória do documento:
   - Princípios do modelo
   - Estrutura de remuneração
   - Projeção por praça (tabela)
   - Gatilhos de evolução
   - Obrigações mútuas (Órulo x Sócio-Local)
   - Histórico: Curitiba e Vitória como casos de referência

3. Crie também uma versão simplificada (one-pager) para apresentar ao Sócio-Local durante recrutamento

---

## SAÍDA ESPERADA

- `WS7_MODELO_ECONOMICO_PRACA_V2.md` — modelo refinado e documentado
- One-pager do modelo (para apresentação ao Sócio-Local)
- Diagnóstico de aderência em Curitiba e Vitória
- Critérios claros para entrada de nova praça com base no modelo

**Decisão obrigatória no final:**
O modelo atual está pronto para ser apresentado a um novo Sócio-Local sem adaptações? Sim / Não / Com ajustes em X.

---

*Prompt criado em 26/03/2026 — Urgência: ALTA — DRI: Diego Diehl*
