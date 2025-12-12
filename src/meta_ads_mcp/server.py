import logging
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

from meta_ads_mcp.tools.accounts import list_ad_accounts
from meta_ads_mcp.tools.campaigns import list_campaigns
from meta_ads_mcp.tools.health import healthcheck
from meta_ads_mcp.tools.insights import get_insights
from meta_ads_mcp.utils.safe_tool import safe_tool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("meta-ads-mcp")

mcp = FastMCP("Meta Ads MCP")


@mcp.tool
@safe_tool
def meta_ads_healthcheck(sample_accounts: int = 3) -> Dict[str, Any]:
    return healthcheck(sample_accounts=sample_accounts)


@mcp.tool
@safe_tool
def meta_ads_list_ad_accounts(limit: int = 25) -> Dict[str, Any]:
    return list_ad_accounts(limit=limit)


@mcp.tool
@safe_tool
def meta_ads_list_campaigns(
    ad_account_id: str,
    limit: int = 25,
    status_filter: Optional[str] = None,
) -> Dict[str, Any]:
    return list_campaigns(
        ad_account_id=ad_account_id,
        limit=limit,
        status_filter=status_filter,
    )


@mcp.tool
@safe_tool
def meta_ads_get_insights(
    entity_id: str,
    level: str = "campaign",
    date_preset: str = "last_7d",
    breakdowns: Optional[List[str]] = None,
    fields: Optional[List[str]] = None,
    limit: int = 100,
) -> Dict[str, Any]:
    return get_insights(
        entity_id=entity_id,
        level=level,
        date_preset=date_preset,
        breakdowns=breakdowns,
        fields=fields,
        limit=limit,
    )


def main() -> None:
    logger.info("Starting Meta Ads MCP (stdio)")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
