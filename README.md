# CSOAI Governance Crosswalk MCP

The world's first operational Constitutional AI governance crosswalk. **17 global AI frameworks** mapped through the CSOAI Partnership Charter's 52 articles — the most comprehensive in existence.

Built by [MEOK AI Labs](https://meok.ai) / [Council for the Safety of AI (CSOAI)](https://csoai.org)

**Core Principle:** Protection Through Care, Not Command

---

## 🏢 Enterprise & Pro Licensing

| Plan | Price | Link |
|------|-------|------|
| **Core MCP Pack** | £49/mo | [Subscribe](https://buy.stripe.com/4gM4gB2G05kmeQJ42k8k805) |
| **Compliance Trinity** | £79/mo | [Subscribe](https://buy.stripe.com/eVq5kF2G0aEG3812Yg8k82i) |
| **Full Suite** (9 MCPs) | £999/mo | [Subscribe](https://buy.stripe.com/6oU14p0xS4giaAtbuM8k82q) |
| **Premium Assessment** | £15,000 | [Book Now](https://buy.stripe.com/bJefZj80kcMObEx2Yg8k82r) |

> Built by [CSOAI](https://csoai.org) — 7+ regulatory framework crosswalk.

---
**MEOK AI Labs** | [meok.ai](https://meok.ai) | [csoai.org](https://csoai.org) | nicholas@meok.ai
## What This Does

This MCP server provides queryable access to 18 months of regulatory mapping IP -- the CSOAI Partnership Charter crosswalked against **17 major global AI governance frameworks**:

### 🌍 Major Frameworks (12 original)
1. **EU AI Act** -- Binding regulation, 27 EU member states
2. **NIST AI RMF** -- US federal AI risk management standard
3. **Anthropic Constitutional AI** -- Industry standard (CC0)
4. **OpenAI Model Spec** -- Behavioral specification (CC0)
5. **UNESCO AI Ethics** -- 193 UN member states
6. **OECD AI Principles** -- 46 member countries
7. **Singapore Agentic AI Framework** -- Newest (Jan 2026)
8. **IEEE Ethically Aligned Design** -- Engineering standard
9. **Asilomar AI Principles** -- AI safety community
10. **Montreal Declaration** -- Democratic AI governance
11. **UK AI Safety Institute** -- Frontier AI evaluation
12. **G7/G20 AI Principles** -- International governance

### 🆕 NEW for 2026 (5 added)
13. **Canada AIDA** -- Federal AI law (pending enactment)
14. **Colorado AI Act** -- US state AI law (effective Feb 2026)
15. **China AI Regulations** -- Tiered regulatory framework
16. **US Executive Order** -- Biden's EO on AI (Oct 2023)
17. *(More coming)*

## Tools (8)

| Tool | Description |
|------|-------------|
| `query_crosswalk` | Query CSOAI mapping for any framework with article-by-article alignment details |
| `crosswalk_bridge` | Bridge two frameworks through CSOAI -- the killer feature. Regulation-to-regulation mapping |
| `compliance_gap_analysis` | Identify compliance gaps across multiple frameworks |
| `get_unified_crosswalk` | Full Master Unified Crosswalk with all 12 frameworks mapped together |
| `search_by_topic` | Search across all crosswalks by topic (transparency, bias, oversight, etc.) |
| `list_frameworks` | List all 12 supported frameworks with metadata |
| `generate_compliance_report` | Generate compliance report for jurisdiction(s) and AI use cases |
| `get_partnership_charter` | Return CSOAI Partnership Charter structure and differentiators |

## Quick Start

```bash
# Install
pip install mcp

# Run
python server.py
```

### Claude Desktop Configuration

```json
{
  "mcpServers": {
    "csoai-governance-crosswalk": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

## Example Queries

- "What EU AI Act articles map to CSOAI?" -> `query_crosswalk("EU AI Act")`
- "How do EU AI Act and NIST RMF relate?" -> `crosswalk_bridge("EU AI Act", "NIST RMF")`
- "What do I need for EU + US compliance?" -> `compliance_gap_analysis(["EU AI Act", "NIST RMF"])`
- "Show me everything about transparency" -> `search_by_topic("transparency")`
- "Generate compliance report for EU healthcare AI" -> `generate_compliance_report(["EU"], ["medical diagnosis"], "enterprise")`

## The CSOAI Partnership Charter

52 Articles | 8 Parts | 13 Schedules | 50+ Global Frameworks Integrated

**Three Critical Differentiators:**

1. **Maternal Covenant (Article 1)** -- Care-based safety: AI inherently motivated to protect humans
2. **Provable Safety (Article 2)** -- Mathematical proof obligations for AI developers
3. **Consciousness Preparedness (Article 6)** -- 14 Indicators for graduated moral patienthood

**Backed by AI safety researchers and governance experts.**

## License

MIT (server code). The CSOAI Partnership Charter and crosswalk analysis represent proprietary IP of CSOAI/MEOK AI Labs.
