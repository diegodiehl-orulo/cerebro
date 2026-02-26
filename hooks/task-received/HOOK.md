---
name: task-received
description: "Confirma recebimento de mensagem antes de começar a processar"
metadata:
  { "openclaw": { "emoji": "🔵", "events": ["message:received"] } }
---

# Task Received Hook

Quando Diego envia uma mensagem, o Morfeu confirma imediatamente que recebeu e vai começar — antes de processar a resposta.
