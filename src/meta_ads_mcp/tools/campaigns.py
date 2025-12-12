from typing import Any, Dict, List, Optional

from meta_ads_mcp.adapters.meta.client import MetaGraphClient
from meta_ads_mcp.config.settings import load_settings
from meta_ads_mcp.utils.errors import ConfigError
from meta_ads_mcp.utils.paging import normalize_paged_response

def list_campaigns(
    ad_account_id: str,
    limit: int = 25,
    status_filter: Optional[str] = None,
) -> Dict[str, Any]:
    settings = load_settings(require_token=True)
    client = MetaGraphClient(settings=settings)

    act_id = ad_account_id if ad_account_id.startswith("act_") else f"act_{ad_account_id}"

    if settings.ad_account_allowlist and act_id not in settings.ad_account_allowlist:
        raise ConfigError(
            f"Ad account {act_id} is not in AD_ACCOUNT_ALLOWLIST. "
            f"Allowed: {settings.ad_account_allowlist}"
        )

    params: Dict[str, Any] = {
        "fields": "id,name,status,objective,buying_type,daily_budget,lifetime_budget",
        "limit": max(1, min(limit, 100)),
    }

    data = client.get(f"{act_id}/campaigns", params=params)
    norm = normalize_paged_response(data)

    campaigns: List[Dict[str, Any]] = norm["data"]
    if status_filter:
        campaigns = [c for c in campaigns if c.get("status") == status_filter]
        norm["data"] = campaigns
        norm["count"] = len(campaigns)

    return {"ad_account_id": act_id, **norm}
