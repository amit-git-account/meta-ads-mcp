Open source and unofficial Meta Ads MCP Server that integrates with your LLM

# Meta Ads MCP

**Meta Ads MCP** is a Model Context Protocol (MCP) server that exposes **Meta Ads APIs as callable tools** for LLMs.

It allows AI assistants (e.g. Claude, Cursor, etc.) to **query, inspect, and analyze Meta Ads data in real time** — without hallucinating, scraping, or relying on stale training data.

---

## What this solves

LLMs are great at reasoning, but **bad at real-time, authoritative data**.

Meta Ads MCP bridges that gap by turning **Meta Ads APIs into deterministic tools** that an LLM can call when it needs ground-truth answers.

**Instead of:**

> “I think your campaign spend looks high…”

**You get:**

> “Campaign `12345` spent `$12,431` yesterday with a CPA of `$18.20` (source: Meta Ads API).”

---

## What you can do with Meta Ads MCP

* List ad accounts
* Inspect campaigns, ad sets, and ads
* Pull performance insights (spend, impressions, CTR, CPA, ROAS, etc.)
* Run health checks to validate connectivity and permissions
* Use Meta Ads data directly inside LLM workflows

---

## Architecture (high level)

```
LLM (Claude / Cursor / IDE)
        |
        |  MCP Tool Call
        v
Meta Ads MCP Server
        |
        |  Official Meta Ads APIs
        v
Meta Ads Platform
```

The LLM **never guesses** — it asks the MCP server, which fetches live data from Meta.

---

## Requirements

* Python 3.10+
* A Meta Ads access token
* Access to at least one Meta Ad Account

---

## Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/<your-org>/meta-ads-mcp.git
cd meta-ads-mcp

python -m venv .venv
source .venv/bin/activate

pip install -e .
```

---

## Configuration

Set your Meta Ads access token as an environment variable:

```bash
export META_ACCESS_TOKEN="your_meta_access_token"
```

Restart the MCP server after setting the variable.

---

## Running the MCP server

```bash
meta-ads-mcp
```

Or directly:

```bash
python -m meta_ads_mcp.run_mcp
```

You should see logs similar to:

```text
Starting MCP server 'Meta Ads MCP'
```


## Updating LLM Config file
```
{
  "mcpServers": {
    "meta-ads-mcp": {
      "command": "/absolute/path/to/.venv/bin/meta-ads-mcp",
      "env": {
        "META_ACCESS_TOKEN": "YOUR_META_ACCESS_TOKEN"
      }
    }
  }
}
```
---

## Available tools

### `meta_ads_healthcheck`

Verify that credentials and API access are correctly configured.

```json
{
  "sample_accounts": 1
}
```

---

### `list_ad_accounts`

List Meta Ad Accounts accessible by the token.

---

### `list_campaigns`

Fetch campaigns for a given ad account.

---

### `get_insights`

Pull performance metrics for campaigns, ad sets, or ads.

Example metrics:

* spend
* impressions
* clicks
* CTR
* CPA
* ROAS

---

## Example prompt (LLM)

> “Show me yesterday’s spend and ROAS for my top 3 campaigns.”

The LLM will:

1. Call `list_campaigns`
2. Call `get_insights`
3. Return grounded, verifiable results

---

## Why MCP (and not RAG or fine-tuning)?

* **No embeddings**
* **No vector stores**
* **No retraining**
* **No hallucinations**

MCP gives the model **tools**, not more text.

---

## Security notes

* Tokens are read from environment variables only
* No credentials are logged
* You control exactly which tools are exposed

---

## Status

* ✅ Core Meta Ads read APIs supported
* 🚧 Write / mutation APIs (future)
* 🚧 Budget & optimization recommendations (future)

---

## License
MIT
