# Adslens MCP

An MCP server that gives LLMs safe, structured access to Meta Ads insights (read-only by default).

## Dev
- Python 3.10+
- `python -m venv .venv && source .venv/bin/activate`

## Configuration
Set these env vars (do not commit secrets):

- `META_ACCESS_TOKEN` (required)
- `AD_ACCOUNT_ALLOWLIST` (recommended, comma-separated): e.g. `act_123,act_456`
- `META_GRAPH_VERSION` (optional, default v21.0)

Example:
```bash
export META_ACCESS_TOKEN="..."
export AD_ACCOUNT_ALLOWLIST="act_123"
