from typing import Any, Callable, Dict, TypeVar
from meta_ads_mcp.utils.errors import ConfigError, HttpError, MetaAdsMcpError

T = TypeVar("T")

def safe_tool(fn: Callable[..., T]) -> Callable[..., Dict[str, Any]]:
    """
    Wrap tool functions so failures return structured, friendly JSON
    (instead of raw tracebacks).
    """
    def _wrapped(*args, **kwargs) -> Dict[str, Any]:
        try:
            out = fn(*args, **kwargs)
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
    return _wrapped
