const handler = async (event: any) => {
  if (event.type !== "message" || event.action !== "received") return;

  const content = event.context?.content ?? "";

  // Ignorar mensagens vazias ou comandos do sistema
  if (!content || content.startsWith("/")) return;

  event.messages.push("🔵 Recebi. Vou começar agora.");
};

export default handler;
