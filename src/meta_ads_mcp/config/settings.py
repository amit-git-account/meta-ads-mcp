import os
from dataclasses import dataclass
from typing import List, Optional

from meta_ads_mcp.utils.errors import ConfigError

@dataclass(frozen=True)
class Settings:
    access_token: str
    graph_version: str = "v21.0"
    graph_base_url: str = "https://graph.facebook.com"
    ad_account_allowlist: Optional[List[str]] = None  # e.g. ["act_123", "act_456"]

def _parse_allowlist(raw: str) -> List[str]:
    items = []
    for part in raw.split(","):
        v = part.strip()
        if not v:
            continue
        items.append(v if v.startswith("act_") else f"act_{v}")
    return items

def load_settings(require_token: bool = True) -> Settings:
    token = os.getenv("META_ACCESS_TOKEN", "").strip()
    graph_version = os.getenv("META_GRAPH_VERSION", "v21.0").strip()
    graph_base_url = os.getenv("META_GRAPH_BASE_URL", "https://graph.facebook.com").strip()

    raw_allow = os.getenv("AD_ACCOUNT_ALLOWLIST", "").strip()
    allowlist = _parse_allowlist(raw_allow) if raw_allow else None

    if require_token and not token:
        raise ConfigError("Missing META_ACCESS_TOKEN. Set it in your shell/env (never commit it).")

    return Settings(
        access_token=token,
        graph_version=graph_version,
        graph_base_url=graph_base_url,
        ad_account_allowlist=allowlist,
    )
