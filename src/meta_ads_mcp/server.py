import logging
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

# IMPORTANT: For stdio MCP servers, don't write to stdout (no print()).
# Use logging to stderr instead.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("meta-ads-mcp")

mcp = FastMCP("Meta Ads MCP")


@mcp.tool
def meta_ads_list_campaigns(
    ad_account_id: str,
    limit: int = 25,
    status_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List campaigns for an ad account (MOCK for now).

    Args:
      ad_account_id: e.g. "act_123"
      limit: max number of campaigns to return
      status_filter: e.g. "ACTIVE", "PAUSED"
    """
    # Mock data so we can test MCP end-to-end before adding Meta auth + API calls.
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


def main() -> None:
    logger.info("Starting Meta Ads MCP (stdio)")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
