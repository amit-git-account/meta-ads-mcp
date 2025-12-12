from typing import Any, Dict, Optional
import requests

from meta_ads_mcp.config.settings import Settings
from meta_ads_mcp.utils.errors import HttpError

class MetaGraphClient:
    def __init__(self, settings: Settings, timeout_s: int = 30):
        self.settings = settings
        self.timeout_s = timeout_s

    def _url(self, path: str) -> str:
        path = path.lstrip("/")
        return f"{self.settings.graph_base_url}/{self.settings.graph_version}/{path}"

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        params = dict(params or {})
        params["access_token"] = self.settings.access_token

        resp = requests.get(self._url(path), params=params, timeout=self.timeout_s)
        try:
            data = resp.json()
        except Exception:
            data = {"raw": resp.text}

        if resp.status_code >= 400:
            msg = "Request failed"
            # Meta errors usually appear under "error"
            if isinstance(data, dict) and "error" in data:
                err = data["error"]
                msg = err.get("message", msg)
            raise HttpError(resp.status_code, msg, payload=data)

        return data
