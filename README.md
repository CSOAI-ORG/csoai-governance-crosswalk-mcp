<div align="center">

# Csoai Governance Crosswalk MCP

**CSOAI Governance Crosswalk MCP Server**

[![PyPI](https://img.shields.io/pypi/v/meok-csoai-governance-crosswalk-mcp)](https://pypi.org/project/meok-csoai-governance-crosswalk-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-MCP_Server-purple)](https://meok.ai)

</div>

## Overview

CSOAI Governance Crosswalk MCP Server
======================================
The crown jewel of the CSOAI MCP portfolio.
18 months of regulatory mapping IP — 12 major global AI frameworks
mapped through the CSOAI Partnership Charter's 52 articles.

Built by MEOK AI Labs | https://meok.ai
Council for the Safety of AI | https://csoai.org

## Tools

| Tool | Description |
|------|-------------|
| `query_crosswalk` | Query the CSOAI crosswalk mapping for a specific framework. |
| `crosswalk_bridge` | Bridge two frameworks through CSOAI — the killer feature. |
| `compliance_gap_analysis` | Identify compliance gaps across multiple frameworks. |
| `get_unified_crosswalk` | Return the CSOAI Master Unified Crosswalk showing all 12 frameworks mapped toget |
| `search_by_topic` | Search across all crosswalks by topic. |
| `list_frameworks` | List all supported frameworks with metadata. |
| `generate_compliance_report` | Generate a compliance requirements report for an organization. |
| `get_partnership_charter` | Return the CSOAI Partnership Charter information. |
| `predict_risk_neural` | Neural network-based risk prediction that improves from every compliance check. |
| `neural_insights` | Get aggregate learning insights from the neural compliance model. |
| `quick_compare` | Instant comparison of two AI governance frameworks. No API key needed. |
| `supported_frameworks` | Lists all supported AI governance frameworks with descriptions. No parameters ne |

## Installation

```bash
pip install meok-csoai-governance-crosswalk-mcp
```

## Usage with Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "csoai-governance-crosswalk-mcp": {
      "command": "python",
      "args": ["-m", "meok_csoai_governance_crosswalk_mcp.server"]
    }
  }
}
```

## Usage with FastMCP

```python
from mcp.server.fastmcp import FastMCP

# This server exposes 12 tool(s) via MCP
# See server.py for full implementation
```

## License

MIT © [MEOK AI Labs](https://meok.ai)
