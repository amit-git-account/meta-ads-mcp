import logging
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

from .tools.accounts import list_ad_accounts
from .tools.campaigns import list_campaigns
from .tools.insights import get_insights

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("meta-ads-mcp")

mcp = FastMCP("Meta Ads MCP")


@mcp.tool
def meta_ads_list_ad_accounts(limit: int = 25) -> Dict[str, Any]:
    return list_ad_accounts(limit=limit)


@mcp.tool
def meta_ads_list_campaigns(
    ad_account_id: str,
    limit: int = 25,
    status_filter: Optional[str] = None,
) -> Dict[str, Any]:
    return list_campaigns(ad_account_id=ad_account_id, limit=limit, status_filter=status_filter)


@mcp.tool
def meta_ads_get_insights(
    entity_id: str,
    level: str = "campaign",
    date_preset: str = "last_7d",
    breakdowns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return get_insights(entity_id=entity_id, level=level, date_preset=date_preset, breakdowns=breakdowns)


def main() -> None:
    logger.info("Starting Meta Ads MCP (stdio)")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
