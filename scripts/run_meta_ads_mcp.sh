#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/Users/amittomar-air/Desktop/projects/meta-ads-mcp"

# Load env from home (token + allowlist) if present
if [[ -f "$HOME/.meta_ads_mcp.env" ]]; then
  # shellcheck disable=SC1090
  source "$HOME/.meta_ads_mcp.env"
fi

cd "$REPO_DIR"

# Force src-layout imports to work even if editable install is flaky
export PYTHONPATH="$REPO_DIR/src"

# Use the repo venv's python explicitly (do NOT rely on console scripts)
exec "$REPO_DIR/.venv/bin/python" -m meta_ads_mcp.server
EOF

chmod +x /Users/amittomar-air/Desktop/projects/meta-ads-mcp/scripts/run_meta_ads_mcp.sh