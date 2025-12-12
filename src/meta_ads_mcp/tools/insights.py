from typing import Any, Dict, List, Optional

def get_insights(
    entity_id: str,
    level: str = "campaign",
    date_preset: str = "last_7d",
    breakdowns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Fetch insights (MOCK for now).

    entity_id: campaign/adset/ad id (or act_... later)
    level: account|campaign|adset|ad
    date_preset: last_7d, last_14d, last_30d, etc.
    breakdowns: e.g. ["age", "gender"]
    """
    breakdowns = breakdowns or []

    # Minimal mock that looks like Ads metrics
    rows = [
        {"entity_id": entity_id, "spend": 123.45, "impressions": 12000, "clicks": 210, "ctr": 0.0175, "cpc": 0.59},
        {"entity_id": entity_id, "spend": 98.10, "impressions": 9000, "clicks": 140, "ctr": 0.0156, "cpc": 0.70},
    ]

    return {
        "entity_id": entity_id,
        "level": level,
        "date_preset": date_preset,
        "breakdowns": breakdowns,
        "rows": rows,
        "note": "MOCK ONLY (no Meta API calls yet)",
    }
