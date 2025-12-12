from typing import Any, Callable, Dict, TypeVar

from meta_ads_mcp.utils.errors import ConfigError, HttpError, MetaAdsMcpError

T = TypeVar("T")

def safe_execute(fn: Callable[..., T], **kwargs: Any) -> Dict[str, Any]:
    """
    Execute a function and return a structured response.
    Designed to be called INSIDE FastMCP tool functions so we don't alter signatures.
    """
    try:
        out = fn(**kwargs)
        return {"ok": True, "result": out}
    except ConfigError as e:
        return {"ok": False, "error_type": "config_error", "message": str(e)}
    except HttpError as e:
        return {
            "ok": False,
            "error_type": "http_error",
            "message": str(e),
            "status_code": e.status_code,
            "payload": e.payload,
        }
    except MetaAdsMcpError as e:
        return {"ok": False, "error_type": "meta_ads_mcp_error", "message": str(e)}
    except Exception as e:
        return {"ok": False, "error_type": "unexpected_error", "message": str(e)}
