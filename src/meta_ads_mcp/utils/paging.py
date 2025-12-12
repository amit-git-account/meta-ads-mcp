from typing import Any, Dict, List, Optional

def normalize_paged_response(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize Meta Graph-style paged responses:
    { "data": [...], "paging": { "cursors": {...}, "next": "..." } }
    """
    items: List[Dict[str, Any]] = data.get("data", []) or []
    paging: Dict[str, Any] = data.get("paging", {}) or {}
    return {"count": len(items), "data": items, "paging": paging}

def next_page_url(paging: Dict[str, Any]) -> Optional[str]:
    return (paging or {}).get("next")
