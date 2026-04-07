"""
tl;dv API Client — v1alpha1
Cliente genérico e reutilizável para a API do tl;dv.
Autenticação via header x-api-key (variável de ambiente TLDV_API_KEY).
"""

import os
import logging
import requests
from typing import Any, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("tldv.client")


class TldvClient:
    """Cliente para a API tl;dv v1alpha1."""

    BASE_URL = "https://pasta.tldv.io/v1alpha1"
    DEFAULT_TIMEOUT = 30

    def __init__(self, timeout: Optional[int] = None):
        api_key = os.environ.get("TLDV_API_KEY")
        if not api_key:
            raise EnvironmentError(
                "TLDV_API_KEY não encontrada no ambiente. "
                "Defina a variável antes de instanciar o cliente."
            )
        self._api_key = api_key
        self._timeout = timeout or self.DEFAULT_TIMEOUT
        self._session = requests.Session()
        self._session.headers.update({"x-api-key": self._api_key})
        logger.info("TldvClient inicializado com sucesso.")

    # ─── Helpers ───────────────────────────────────────────────────────────────

    def _get(self, path: str, params: Optional[dict] = None) -> dict[str, Any]:
        """Executa GET e retorna o JSON. Trata erros com mensagens úteis."""
        url = f"{self.BASE_URL}{path}"
        logger.info("GET %s params=%s", url, params)

        response = self._session.get(url, params=params, timeout=self._timeout)

        # Não expor API key no log — já está no header, log não mostra headers
        if response.status_code == 401:
            logger.error("401 Unauthorized — API key inválida ou ausente.")
            raise PermissionError("Credenciais inválidas (401). Verifique TLDV_API_KEY.")
        if response.status_code == 403:
            logger.error("403 Forbidden — acesso negado ao recurso.")
            raise PermissionError("Acesso negado (403). API key sem permissão para este recurso.")
        if response.status_code == 404:
            logger.error("404 Not Found — recurso inexistente: %s", url)
            raise FileNotFoundError(f"Recurso não encontrado (404): {path}")
        if response.status_code == 400:
            logger.error("400 Bad Request — params=%s | body=%s", params, response.text[:500])
            raise ValueError(f"Requisição inválida (400): {response.text[:500]}")
        if not response.ok:
            logger.error(
                "Erro HTTP %d — body=%s", response.status_code, response.text[:500]
            )
            raise RuntimeError(
                f"Erro HTTP {response.status_code} inesperado. "
                f"Resposta: {response.text[:300]}"
            )

        logger.info("GET %s → %d OK", url, response.status_code)
        return response.json()

    # ─── Endpoints ─────────────────────────────────────────────────────────────

    def health(self) -> dict[str, Any]:
        """GET /health — verifica se a API está acessível."""
        return self._get("/health")

    def list_meetings(
        self,
        page: int = 1,
        page_size: int = 50,
    ) -> dict[str, Any]:
        """
        GET /meetings — lista reuniões com paginação.
        Params: page (1-indexed), page_size.
        """
        return self._get("/meetings", params={"page": page, "pageSize": page_size})

    def get_meeting(self, meeting_id: str) -> dict[str, Any]:
        """GET /meetings/{meetingId} — retorna detalhes de uma reunião."""
        return self._get(f"/meetings/{meeting_id}")

    def get_transcript(self, meeting_id: str) -> dict | None:
        """
        GET /meetings/{meetingId}/transcript — retorna transcript ou None se 204.
        204 = transcript ainda não foi processado (não é erro, é pending).
        """
        url = f"{self.BASE_URL}/meetings/{meeting_id}/transcript"
        logger.info("GET %s", url)
        response = self._session.get(url, timeout=self._timeout)
        if response.status_code == 204:
            logger.info("GET %s → 204 (transcript pendente de processamento)", url)
            return None
        if response.status_code == 401:
            raise PermissionError("Credenciais inválidas (401).")
        if response.status_code == 404:
            raise FileNotFoundError(f"Reunião não encontrada (404): {meeting_id}")
        if not response.ok:
            raise RuntimeError(f"Erro HTTP {response.status_code} em transcript.")
        return response.json()

    def get_notes(self, meeting_id: str) -> dict | None:
        """
        GET /meetings/{meetingId}/notes — retorna notes ou None se 204/empty.
        """
        url = f"{self.BASE_URL}/meetings/{meeting_id}/notes"
        logger.info("GET %s", url)
        response = self._session.get(url, timeout=self._timeout)
        if response.status_code == 204 or response.status_code == 200:
            data = response.json()
            has_content = bool(
                data.get("structuredNotes")
                or data.get("markdownContent")
                or data.get("topics")
            )
            if not has_content:
                logger.info("GET %s → 200 (notes vazias)", url)
                return None
            return data
        if response.status_code == 401:
            raise PermissionError("Credenciais inválidas (401).")
        if response.status_code == 404:
            raise FileNotFoundError(f"Reunião não encontrada (404): {meeting_id}")
        if not response.ok:
            raise RuntimeError(f"Erro HTTP {response.status_code} em notes.")
        return response.json()
