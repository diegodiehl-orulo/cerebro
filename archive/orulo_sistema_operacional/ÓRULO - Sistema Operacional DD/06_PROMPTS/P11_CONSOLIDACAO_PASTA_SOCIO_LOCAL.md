# P11: CONSOLIDAÇÃO DA PASTA SÓCIO-LOCAL

**Versão:** 1.0
**Data de criação:** 26/03/2026
**Status:** PRONTO PARA RODAR
**DRI:** Diego Diehl
**WS associado:** WS7 — Modelo Econômico Praça
**Urgência:** MÉDIA — consolidar antes de abrir novas praças

---

## CONTEXTO

Na pasta `Bases CONSOLIDADAS/04_Expansao_Territorial/SOCIO_LOCAL/` existem atualmente **4 documentos** sobre o Sócio-Local:

| Arquivo | Conteúdo | Status |
|---|---|---|
| `00_README_SOCIO_LOCAL.md` | Índice da pasta | Auxiliar |
| `MODELO_SOCIO_LOCAL_ORULO_V3.md` | Modelo comercial completo (V3) | Principal |
| `SINTESE_MODELO_SOCIO_LOCAL.md` | Síntese executiva do modelo | Possivelmente redundante |
| `08_Governanca_Regional.md` | Governança regional (GDD, rituais) | Complementar |
| `20_Rotina_SocioLocal.md` | Rotina prescrita do dia a dia | Complementar |

**Problema:** sobreposição entre MODELO_V3 e SINTESE. Pasta fragmentada. Não está claro qual documento é a fonte primária para um Sócio-Local novo.

---

## INSTRUÇÃO PARA A IA

Você está atuando como Sistema Integrado de Gestão de OKRs e Inteligência Documental da Órulo.

Leia todos os documentos da pasta `SOCIO_LOCAL` antes de iniciar.

Seu objetivo é consolidar a pasta em uma estrutura limpa e funcional para dois públicos:
1. **Diego/Órulo** — referência interna para decisões e gestão
2. **Sócio-Local** — material que ele pode receber e entender

---

## ROTEIRO DE EXECUÇÃO

### ETAPA 1 — Leitura e diagnóstico

Leia todos os 5 documentos da pasta e responda:

> O MODELO_V3 e a SINTESE tratam os mesmos temas ou são complementares?
> A SINTESE é um subconjunto do MODELO_V3 ou traz informação adicional?
> O 08_Governanca_Regional está desatualizado após a implementação do WS7?
> A 20_Rotina_SocioLocal é prescritiva ou apenas aspiracional?

---

### ETAPA 2 — Proposta de consolidação

Com base no diagnóstico, proponha uma das duas opções:

**Opção A — Fusão:** Mesclar MODELO_V3 e SINTESE em um único documento `MODELO_SOCIO_LOCAL_CONSOLIDADO.md`, movendo partes únicas da SINTESE para o MODELO, e marcando a SINTESE como obsoleta.

**Opção B — Especialização:** Manter os dois com funções diferentes:
- MODELO_V3 = documento de referência interno completo
- SINTESE = material de apresentação para o Sócio-Local (mais enxuto)

Valide com Diego qual opção faz mais sentido.

---

### ETAPA 3 — Estrutura final da pasta

Após validação, a pasta SOCIO_LOCAL deve ter:

```
SOCIO_LOCAL/
├── 00_README_SOCIO_LOCAL.md       ← atualizado com mapa da pasta
├── MODELO_SOCIO_LOCAL_V3.md       ← referência interna completa
├── [SINTESE ou CONSOLIDADO]       ← conforme decisão acima
├── 08_Governanca_Regional.md      ← verificar atualidade
└── 20_Rotina_SocioLocal.md        ← verificar atualidade
```

---

### ETAPA 4 — Conexão com WS7

Após consolidar a pasta, garantir que:

1. O Charter do WS7 referencia a pasta SOCIO_LOCAL como fonte de documentos base
2. O `MODELO_SOCIO_LOCAL_V3.md` referencia o WS7 como local de gestão operacional
3. O modelo refinado (P8) ao ser criado vai para o WS7, não para a pasta SOCIO_LOCAL

---

### ETAPA 5 — Documentação

Atualize o `00_README_SOCIO_LOCAL.md` com:
- Mapa atualizado de todos os documentos
- Função clara de cada um
- Referência cruzada para WS7

---

## SAÍDA ESPERADA

- Pasta SOCIO_LOCAL limpa e sem redundâncias
- README da pasta atualizado
- Decisão clara: fusão ou especialização dos documentos
- Conexão formal com WS7 estabelecida

**Decisão obrigatória no final:**
Qual documento entregamos para um novo Sócio-Local no momento do recrutamento?

---

*Prompt criado em 26/03/2026 — Conexão: WS7 (P8) + Bases CONSOLIDADAS*
