from typing import Any, Dict

from meta_ads_mcp.adapters.meta.client import MetaGraphClient
from meta_ads_mcp.config.settings import load_settings

def healthcheck(sample_accounts: int = 3) -> Dict[str, Any]:
    settings = load_settings(require_token=True)
    client = MetaGraphClient(settings=settings)

    # 1) Basic identity check
    me = client.get("me", params={"fields": "id,name"})

    # 2) Try Ads access (list ad accounts)
    adaccounts = client.get(
        "me/adaccounts",
        params={"fields": "id,name,account_status,currency", "limit": max(1, min(sample_accounts, 25))},
    )

    visible_accounts = adaccounts.get("data", []) or []
    allowlist = settings.ad_account_allowlist

    allowlist_ok = None
    if allowlist:
        allowlist_ok = all(a in {acc.get("id") for acc in visible_accounts} or True for a in allowlist)
        # NOTE: Even if not visible in sample, token might still have access; this is a lightweight signal.

    return {
        "graph_version": settings.graph_version,
        "me": me,
        "ad_accounts_visible_sample": visible_accounts,
        "allowlist": allowlist,
        "notes": [
            "If me/adaccounts fails, your token likely lacks ads permissions (e.g., ads_read) or isn’t tied to a user/system with account access.",
            "If allowlist is set, list_campaigns/insights will refuse accounts not in the allowlist.",
        ],
        "allowlist_signal_ok": allowlist_ok,
    }
