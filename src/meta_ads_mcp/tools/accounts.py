from typing import Any, Dict, List

from meta_ads_mcp.adapters.meta.client import MetaGraphClient
from meta_ads_mcp.config.settings import load_settings

def list_ad_accounts(limit: int = 25) -> Dict[str, Any]:
    """
    Real call: GET /me/adaccounts
    Requires a user/system token with ads permissions (e.g., ads_read).
    """
    settings = load_settings(require_token=True)
    client = MetaGraphClient(settings=settings)

    data = client.get(
        "me/adaccounts",
        params={
            "fields": "id,name,account_status,currency",
            "limit": max(1, min(limit, 100)),
        },
    )

    accounts: List[Dict[str, Any]] = data.get("data", [])
    return {
        "count": len(accounts),
        "accounts": accounts,
        "paging": data.get("paging", {}),
    }
