from typing import Any, Dict, List, Optional

def list_campaigns(
    ad_account_id: str,
    limit: int = 25,
    status_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List campaigns for an ad account (MOCK for now).
    """
    campaigns: List[Dict[str, Any]] = [
        {"id": "cmp_001", "name": "Prospecting - Broad", "status": "ACTIVE"},
        {"id": "cmp_002", "name": "Retargeting - 7d", "status": "PAUSED"},
        {"id": "cmp_003", "name": "Brand - Always On", "status": "ACTIVE"},
    ]

    if status_filter:
        campaigns = [c for c in campaigns if c["status"] == status_filter]

    campaigns = campaigns[: max(1, min(limit, 100))]

    return {
        "ad_account_id": ad_account_id,
        "count": len(campaigns),
        "campaigns": campaigns,
        "note": "MOCK ONLY (no Meta API calls yet)",
    }
