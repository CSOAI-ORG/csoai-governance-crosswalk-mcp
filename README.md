<!-- mcp-name: CSOAI-ORG/csoai-governance-crosswalk-mcp -->
# Csoai Governance Crosswalk MCP

> **⚖️ Built by [MEOK AI Labs](https://meok.ai) / [CSOAI](https://csoai.org).** Need this applied to _your_ system fast? Book a 30-min Founder Office Hour (£29) → **https://meok.ai/work** · Full governance platform → **https://meok.ai**

[![MEOK AI Labs](https://img.shields.io/badge/MEOK-AI%20Labs-667eea)](https://meok.ai)
[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-Compliant-22c55e)](https://councilof.ai)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-Install-3775a9)](https://pypi.org/project/csoai_governance_crosswalk_mcp/)
<div align="center">

# CSOAI Governance Crosswalk MCP

**Unified AI Governance Framework Mapper — 12 Frameworks, 52 Articles, One Query**

[![MCP](https://img.shields.io/badge/MCP-Server-blue)](https://github.com/CSOAI-ORG)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](pyproject.toml)

> AI governance crosswalk MCP — map controls across 13 frameworks (EU AI Act, ISO 42001, NIST AI RM...

AI governance crosswalk MCP — map controls across 13 frameworks (EU AI Act, ISO 42001, NIST AI RMF, GDPR, SOC 2, HIPAA, FedRAMP, CCPA, PIPEDA, DPDPA, LGPD, CSA, OWASP).

---

## 🚀 Quick Start

```bash
# Install via pip
pip install csoai_governance_crosswalk_mcp

# Or install via Smithery
npx -y @smithery/cli@latest install csoai-governance-crosswalk-mcp --client claude
```

## ✨ Features

- MCP protocol compliant
- Easy installation
- Well-documented API
- Production-ready
- Active maintenance

## 📖 Documentation

- [Full Documentation](https://docs.meok.ai/csoai-governance-crosswalk-mcp)
- [API Reference](https://api.meok.ai)
- [EU AI Act Compliance Guide](https://councilof.ai/compliance)

## 🛡️ Compliance

This MCP server is built with **EU AI Act compliance** built-in:

- ✅ Article 9 — Risk Management System
- ✅ Article 13 — Transparency & Instructions for Use
- ✅ Article 15 — Bias Detection & Testing
- ✅ Article 26 — FRIA Support (where applicable)
- ✅ Article 50 — AI Content Watermarking (where applicable)

Need help getting compliant? **[Book a free 15-min diagnostic →](https://cal.com/csoai/august-audit)**

## 🏢 Enterprise

Need custom development, SLA guarantees, or white-label deployment?

- **Pro:** $99/mo — Full MCP suite + EU AI Act tracking
- **Enterprise:** $499/mo — Custom dev + SLA + Dedicated support

[View Pricing →](https://councilof.ai/pricing) | [Contact Sales →](mailto:sales@csoai.org)

## 🤝 Part of the MEOK Ecosystem

This server is part of the **[MEOK AI Labs](https://meok.ai)** ecosystem — 300+ MCP servers for sovereign AI governance.

| Domain | Purpose |
|--------|---------|
| [councilof.ai](https://councilof.ai) | EU AI Act compliance marketplace |
| [safetyof.ai](https://safetyof.ai) | AI safety & monitoring |
| [meok.ai](https://meok.ai) | Sovereign AI platform |
| [cobolbridge.ai](https://cobolbridge.ai) | Legacy modernization |

## 📜 License

MIT © [CSOAI-ORG](https://github.com/CSOAI-ORG)

---

<p align="center">
  <sub>Built with 💜 by <a href="https://meok.ai">MEOK AI Labs</a> · UK Companies House 16939677</sub>
</p>
The crown jewel of the CSOAI MCP portfolio. Maps requirements across 12 governance frameworks (EU AI Act, GDPR, NIST RMF, ISO 42001, SOC 2, HIPAA, PCI DSS, DORA, NIS2, CRA, UK AI Bill, Canada AIDA) through 52 unified crosswalk articles. One query tells you what every regulation says about any compliance topic.

## Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `query_crosswalk` | Query all 12 frameworks on any compliance topic | `query` (str, required), `frameworks` (list, optional filter) |
| `crosswalk_bridge` | Find framework-to-framework requirement mappings | `source_framework`, `target_framework`, `topic` |
| `compliance_gap_analysis` | Identify gaps between current posture and regulation | `framework`, `current_controls` |
| `framework_comparison` | Side-by-side comparison of two frameworks | `framework_a`, `framework_b`, `dimension` |
| `get_article_details` | Full text and interpretation of a specific article | `article_id`, `framework` |
| `regulatory_timeline` | Key dates and deadlines for a framework | `framework` |
| `risk_profile` | Generate cross-framework risk profile | `industry`, `jurisdiction`, `ai_types` |
| `control_mapping` | Map existing controls to framework requirements | `framework`, `control_ids` |
| `audit_scoping` | Scope an audit across multiple frameworks | `frameworks`, `systems` |
| `remediation_plan` | Generate prioritized remediation plan | `gaps`, `framework`, `timeline` |
| `evidence_requirements` | List evidence needed for each framework article | `framework`, `article_ids` |
| `stakeholder_report` | Generate stakeholder-ready compliance report | `framework`, `findings` |

## Installation

```bash
pip install mcp
```

### Claude Desktop
```json
{
  "mcpServers": {
    "csoai-governance-crosswalk": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

### Cursor / VS Code / Windsurf
```json
{
  "mcpServers": {
    "csoai-governance-crosswalk": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Usage Examples

### Query all frameworks on bias requirements
```json
{
  "query": "bias detection and mitigation requirements",
  "frameworks": ["eu_ai_act", "nist_rmf", "iso_42001"]
}
```

### Gap analysis against EU AI Act
```json
{
  "framework": "eu_ai_act",
  "current_controls": ["manual review process", "quarterly audits", "basic documentation"]
}
```

## Pricing

- **Free:** 10 queries/day
- **Pro:** $99/mo — unlimited queries + export reports
- **Enterprise:** $499/mo — custom framework add-ons + attestation

---

*Built by MEOK AI Labs | [meok.ai](https://meok.ai)*

<!-- BUY-LADDER:START -->

## 💸 Try MEOK in 30 seconds — instant buy ladder

| Tier | Price | What you get | Stripe |
|---|---|---|---|
| Smoke test | **£1** | Signed sample MCP-Hardening report + Article 50 PDF | <https://buy.stripe.com/dRmcN75ScdQS7oh1Uc8k90U> |
| Quick Kit | **£9** | EU AI Act Article 50 implementation guide (C2PA + EU-Icon) | <https://buy.stripe.com/cNi00la8s1460ZT0Q88k90V> |
| Founder Call | **£29** | 30-min 1-on-1 with the founder | <https://buy.stripe.com/8x228ta8s6oqbExaqI8k90W> |

> Refundable. UK Stripe — VAT-clean. Builds on the 81-MCP MEOK fleet.
> Verify any signed report at <https://meok.ai/verify>.

<!-- BUY-LADDER:END -->

