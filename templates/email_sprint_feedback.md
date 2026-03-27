# templates/email_sprint_feedback.md
# Template: Retorno do Diego ao Sócio Local (após leitura do One-Pager)
*Sistema: Sprint Quinzenal de Praças | v1.0*

---

> **Uso:** Morfeu gera este e-mail após analisar o One-Pager recebido.
> Diego revisa, ajusta se quiser e autoriza a Lara enviar.
> Sempre personalizado com base no One-Pager real.

---

**Para:** {NOME_SOCIO} <{EMAIL_SOCIO}>
**CC:** Gustavo Torres <gustavo.torres@orulo.com.br>
**Assunto:** Re: ÓRULO | Sprint Quinzenal | Praça: {PRAÇA} | Período: {DD/MM–DD/MM} | One-Pager

---

{NOME_SOCIO_PRIMEIRO_NOME},

One-Pager recebido e analisado. Bom nível de detalhe — vou te dar o retorno direto.

---

**DIAGNÓSTICO DO SPRINT ANTERIOR**

- Planejado vs. Executado: {DIAGNÓSTICO_RESUMO}
- O que funcionou: {O_QUE_FUNCIONOU}
- O que não foi: {O_QUE_NAO_FOI}
- Aprendizado principal: {APRENDIZADO}

---

**GARGALO #1 IDENTIFICADO**

{GARGALO_DESCRICAO}

Hipótese de causa: {HIPOTESE_CAUSA}
Teste desta semana: {TESTE_VALIDACAO}

---

**CONTRATO DO PRÓXIMO SPRINT — VALIDADO**

| | Compromisso | Dono | Prazo | Evidência |
|--|-------------|------|-------|-----------|
| **C1** | {C1} | {C1_DONO} | {C1_PRAZO} | {C1_EVIDENCIA} |
| **C2** | {C2} | {C2_DONO} | {C2_PRAZO} | {C2_EVIDENCIA} |
| **C3** | {C3} | {C3_DONO} | {C3_PRAZO} | {C3_EVIDENCIA} |

**Checkpoint assíncrono:** {DATA_CHECKPOINT}
→ Me manda um e-mail nessa data: % executado de cada compromisso + bloqueios.

---

**3 PERGUNTAS DE ESCLARECIMENTO**

1. {PERGUNTA_1}
2. {PERGUNTA_2}
3. {PERGUNTA_3}

Me responde no e-mail ou por WhatsApp se preferir.

---

**PEDIDO DE AJUDA À MATRIZ**

Recebi: *"{PEDIDO_MATRIZ}"*
Responsável: {RESPONSAVEL_MATRIZ}
Retorno até: {PRAZO_RESPOSTA_MATRIZ}

---

Bora executar. Check-in na terça e sexta.

Diego


---

## INSTRUÇÕES PARA O MORFEU (ao gerar este e-mail)

Substituir todas as variáveis `{...}` com base no One-Pager recebido:
- `{DIAGNÓSTICO_RESUMO}` — comparar planejado vs. executado em 1 linha
- `{GARGALO_DESCRICAO}` — 1 linha, o ponto que mais trava
- `{C1}`, `{C2}`, `{C3}` — extrair da seção 7 do One-Pager; se [PREENCHER], manter assim
- `{PERGUNTA_1–3}` — perguntas geradas pela análise do Morfeu (esclarecimento ou aprofundamento)
- `{PEDIDO_MATRIZ}` — extrair da seção 9 do One-Pager

Se algum bloco estiver ausente no One-Pager → usar `[PREENCHER]` e sinalizar para Diego.

---

## INSTRUÇÕES PARA LARA

1. Enviar para: {EMAIL_SOCIO}
2. CC: gustavo.torres@orulo.com.br
3. Assunto: verificar se está exatamente no padrão `Re: ÓRULO | Sprint Quinzenal | ...`
4. Não alterar o corpo além das variáveis já preenchidas pelo Morfeu
5. Registrar data/hora de envio

⚠️ **OK para a Lara enviar?** [Diego confirmar → Instruções via @larissa_personal_assistant_bot]
