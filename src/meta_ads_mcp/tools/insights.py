from typing import Any, Dict, List, Optional

from meta_ads_mcp.adapters.meta.client import MetaGraphClient
from meta_ads_mcp.config.settings import load_settings
from meta_ads_mcp.utils.errors import ConfigError
from meta_ads_mcp.utils.paging import normalize_paged_response

def get_insights(
    entity_id: str,
    level: str = "campaign",
    date_preset: str = "last_7d",
    breakdowns: Optional[List[str]] = None,
    fields: Optional[List[str]] = None,
    limit: int = 100,
) -> Dict[str, Any]:
    """
    Real call: GET /{entity_id}/insights

    entity_id can be act_{id}, campaign id, adset id, or ad id depending on level.
    """
    settings = load_settings(require_token=True)
    client = MetaGraphClient(settings=settings)

    # Allowlist enforcement if this is an account-level query
    if entity_id.startswith("act_") and settings.ad_account_allowlist and entity_id not in settings.ad_account_allowlist:
        raise ConfigError(
            f"Ad account {entity_id} is not in AD_ACCOUNT_ALLOWLIST. "
            f"Allowed: {settings.ad_account_allowlist}"
        )

    breakdowns = breakdowns or []
    fields = fields or [
        "spend",
        "impressions",
        "clicks",
        "ctr",
        "cpc",
        "cpm",
        "actions",
        "action_values",
        "purchase_roas",
    ]

    params: Dict[str, Any] = {
        "level": level,
        "date_preset": date_preset,
        "fields": ",".join(fields),
        "limit": max(1, min(limit, 500)),
    }
    if breakdowns:
        params["breakdowns"] = ",".join(breakdowns)

    data = client.get(f"{entity_id}/insights", params=params)
    norm = normalize_paged_response(data)
    return {"entity_id": entity_id, "level": level, "date_preset": date_preset, "breakdowns": breakdowns, **norm}
