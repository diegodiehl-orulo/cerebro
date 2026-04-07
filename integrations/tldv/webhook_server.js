#!/usr/bin/env node
/**
 * webhook_server.js — Receptor de webhooks tl;dv
 * ==============================================
 * Escuta POST /webhook/tldv e armazena eventos em fila para processamento.
 * Não processa diretamente — só recebe e enfileira (pattern: fire-and-forget).
 *
 * Endpoints:
 *   POST /webhook/tldv    — recebe evento tl;dv
 *   GET  /health          — health check
 *   GET  /queue/status    — status da fila
 *   POST /queue/process   — força processamento da fila (internal)
 *
 * Eventos suportados:
 *   MeetingReady, TranscriptReady
 *
 * Estratégia de deduplicação:
 *   SHA256(eventType + meetingId + timestamp) como chave única.
 *   Eventos duplicados retornam 200 mas não são enfileirados.
 */

const http = require("http");
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");
const { URL } = require("url");

const PORT = process.env.TLDV_WEBHOOK_PORT || 18788;
const QUEUE_DIR = path.join("/root/.openclaw/workspace/memory/meetings/queue");
const HASH_FILE = path.join(QUEUE_DIR, ".dedup_hashes.txt");
const LOG_FILE = path.join("/root/.openclaw/workspace/logs", "tldv_webhook.log");
const WEBHOOK_SECRET = process.env.TLDV_WEBHOOK_SECRET || ""; // opcional

const SUPPORTED_EVENTS = ["MeetingReady", "TranscriptReady"];

// ── Logger ───────────────────────────────────────────────────────────────────

function log(level, msg, meta = {}) {
  const ts = new Date().toISOString();
  const entry = `[${ts}] [${level}] ${msg} ${JSON.stringify(meta)}`;
  console.error(entry);
  try {
    fs.appendFileSync(LOG_FILE, entry + "\n");
  } catch (_) {}
}

// ── Deduplicação ─────────────────────────────────────────────────────────────

function loadHashes() {
  try {
    return new Set(fs.readFileSync(HASH_FILE, "utf8").trim().split("\n").filter(Boolean));
  } catch (_) {
    return new Set();
  }
}

function saveHashes(hashes) {
  try {
    fs.mkdirSync(QUEUE_DIR, { recursive: true });
    fs.writeFileSync(HASH_FILE, Array.from(hashes).join("\n"));
  } catch (e) {
    log("ERROR", "Failed to save dedup hashes", { error: e.message });
  }
}

function isDuplicate(eventType, meetingId, timestamp) {
  const key = crypto
    .createHash("sha256")
    .update(`${eventType}:${meetingId}:${timestamp}`)
    .digest("hex")
    .slice(0, 32);
  const hashes = loadHashes();
  if (hashes.has(key)) {
    return true;
  }
  hashes.add(key);
  saveHashes(hashes);
  return false;
}

// ── Event Handler ────────────────────────────────────────────────────────────

function handleTldvEvent(body) {
  // tl;dv pode enviar como { event: "MeetingReady", meetingId: "...", ... }
  // ou como { event: "...", data: { meetingId: "...", ... } }
  const eventType = body.event || body.type || "";
  const data = body.data || body;
  const meetingId = data.meetingId || data.meeting_id || "";
  const timestamp = data.timestamp || data.happenedAt || body.timestamp || Date.now().toString();

  if (!meetingId) {
    log("WARN", "Evento sem meetingId", { body: JSON.stringify(body).slice(0, 200) });
    return { status: "rejected", reason: "missing meetingId" };
  }

  if (!SUPPORTED_EVENTS.includes(eventType)) {
    log("INFO", "Evento ignorado", { eventType, meetingId });
    return { status: "ignored", eventType };
  }

  const dupKey = `${eventType}:${meetingId}:${timestamp}`;
  if (isDuplicate(eventType, meetingId, timestamp)) {
    log("INFO", "Evento duplicado descartado", { dupKey });
    return { status: "duplicate", dupKey };
  }

  // Estrutura do evento na fila
  const event = {
    id: crypto.randomUUID(),
    eventType,
    meetingId,
    timestamp,
    receivedAt: new Date().toISOString(),
    payload: data,
    status: "pending",
    attempts: 0,
  };

  const eventFile = path.join(QUEUE_DIR, `${Date.now()}_${meetingId}_${eventType}.json`);
  fs.mkdirSync(QUEUE_DIR, { recursive: true });
  fs.writeFileSync(eventFile, JSON.stringify(event, null, 2));

  log("INFO", "Evento enfileirado", {
    id: event.id,
    eventType,
    meetingId,
    file: path.basename(eventFile),
  });

  return { status: "queued", eventId: event.id, meetingId, eventType };
}

// ── HTTP Server ──────────────────────────────────────────────────────────────

function parseBody(req) {
  return new Promise((resolve, reject) => {
    let data = "";
    req.on("data", (chunk) => (data += chunk));
    req.on("end", () => {
      try {
        resolve(JSON.parse(data));
      } catch (_) {
        resolve({});
      }
    });
    req.on("error", reject);
  });
}

function sendJson(res, status, body) {
  res.writeHead(status, { "Content-Type": "application/json" });
  res.end(JSON.stringify(body));
}

const server = http.createServer(async (req, res) => {
  const start = Date.now();
  let remoteAddr = req.socket.remoteAddress;

  try {
    const url = new URL(req.url, `http://${req.headers.host}`);

    // ── Health ────────────────────────────────────────────────────────────
    if (url.pathname === "/health" && req.method === "GET") {
      return sendJson(res, 200, { status: "ok", service: "tldv-webhook" });
    }

    // ── Queue status ──────────────────────────────────────────────────────
    if (url.pathname === "/queue/status" && req.method === "GET") {
      try {
        const files = fs.readdirSync(QUEUE_DIR).filter((f) => f.endsWith(".json") && !f.startsWith("."));
        const pending = files.length;
        return sendJson(res, 200, { pending, queueDir: QUEUE_DIR, files: files.slice(0, 20) });
      } catch (e) {
        return sendJson(res, 500, { error: e.message });
      }
    }

    // ── Webhook tl;dv ─────────────────────────────────────────────────────
    if (url.pathname === "/webhook/tldv" && req.method === "POST") {
      const body = await parseBody(req);

      // Validar secret se configurado
      if (WEBHOOK_SECRET) {
        const sig = req.headers["x-tldv-signature"] || req.headers["x-webhook-secret"] || "";
        const expected = crypto.createHash("sha256").update(WEBHOOK_SECRET).digest("hex");
        if (sig !== expected && sig !== `sha256=${expected}`) {
          log("WARN", "Webhook com secret inválido", { sig: sig.slice(0, 10) });
          return sendJson(res, 401, { error: "Invalid signature" });
        }
      }

      const result = handleTldvEvent(body);
      const elapsed = Date.now() - start;
      log("INFO", "Webhook processado", { ...result, elapsedMs: elapsed });

      if (result.status === "rejected") {
        return sendJson(res, 400, result);
      }
      return sendJson(res, 200, result);
    }

    // 404
    sendJson(res, 404, { error: "Not found" });
  } catch (e) {
    log("ERROR", "Erro no handler", { error: e.message, stack: e.stack });
    sendJson(res, 500, { error: "Internal error" });
  }
});

// ── Start ─────────────────────────────────────────────────────────────────────

server.listen(PORT, "0.0.0.0", () => {
  log("INFO", `Webhook server started`, { port: PORT, QUEUE_DIR });
  console.error(`[tl;dv webhook] listening on port ${PORT}`);
});

// Graceful shutdown
process.on("SIGTERM", () => {
  log("INFO", "SIGTERM received, shutting down");
  server.close(() => {
    log("INFO", "Server closed");
    process.exit(0);
  });
});
