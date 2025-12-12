from typing import Any, Dict, List, Optional

from meta_ads_mcp.adapters.meta.client import MetaGraphClient
from meta_ads_mcp.config.settings import load_settings
from meta_ads_mcp.utils.paging import normalize_paged_response

def list_campaigns(
    ad_account_id: str,
    limit: int = 25,
    status_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Real call: GET /act_{ad_account_id}/campaigns
    Accepts ad_account_id as either "act_123" or "123".
    """
    settings = load_settings(require_token=True)
    client = MetaGraphClient(settings=settings)

    act_id = ad_account_id if ad_account_id.startswith("act_") else f"act_{ad_account_id}"

    params: Dict[str, Any] = {
        "fields": "id,name,status,objective,buying_type,daily_budget,lifetime_budget",
        "limit": max(1, min(limit, 100)),
    }
    if status_filter:
        # Meta expects filtering JSON sometimes; keep v0 simple with server-side filter after fetch.
        pass

    data = client.get(f"{act_id}/campaigns", params=params)
    norm = normalize_paged_response(data)

    campaigns: List[Dict[str, Any]] = norm["data"]
    if status_filter:
        campaigns = [c for c in campaigns if c.get("status") == status_filter]
        norm["data"] = campaigns
        norm["count"] = len(campaigns)

    return {
        "ad_account_id": act_id,
        **norm,
    }
