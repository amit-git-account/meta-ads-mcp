import os
from dataclasses import dataclass

from meta_ads_mcp.utils.errors import ConfigError

@dataclass(frozen=True)
class Settings:
    access_token: str
    graph_version: str = "v21.0"  # safe default; adjust later if you want
    graph_base_url: str = "https://graph.facebook.com"

def load_settings(require_token: bool = True) -> Settings:
    token = os.getenv("META_ACCESS_TOKEN", "").strip()
    graph_version = os.getenv("META_GRAPH_VERSION", "v21.0").strip()
    graph_base_url = os.getenv("META_GRAPH_BASE_URL", "https://graph.facebook.com").strip()

    if require_token and not token:
        raise ConfigError(
            "Missing META_ACCESS_TOKEN. Set it in your shell/env (never commit it)."
        )

    return Settings(access_token=token, graph_version=graph_version, graph_base_url=graph_base_url)
