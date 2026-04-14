"""
CSOAI Governance Crosswalk MCP Server
======================================
The crown jewel of the CSOAI MCP portfolio.
18 months of regulatory mapping IP — 12 major global AI frameworks
mapped through the CSOAI Partnership Charter's 52 articles.

Built by MEOK AI Labs | https://meok.ai
Council for the Safety of AI | https://csoai.org
"""

from mcp.server.fastmcp import FastMCP

# Tier authentication (connects to Stripe subscriptions)
try:
    from auth_middleware import get_tier_from_api_key, Tier, TIER_LIMITS
    AUTH_AVAILABLE = True
except ImportError:
    AUTH_AVAILABLE = False  # Runs without auth in dev mode
from typing import Optional
import json


# ── Authentication ──────────────────────────────────────────────
import os as _os
_MEOK_API_KEY = _os.environ.get("MEOK_API_KEY", "")

def _check_auth(api_key: str = "") -> str | None:
    """Check API key if MEOK_API_KEY is set. Returns error or None."""
    if _MEOK_API_KEY and api_key != _MEOK_API_KEY:
        return "Invalid API key. Get one at https://meok.ai/api-keys"
    return None


mcp = FastMCP(
    "csoai-governance-crosswalk",
    instructions=(
        "CSOAI Governance Crosswalk MCP Server — the world's first operational "
        "Constitutional AI crosswalk mapping 12 major global AI frameworks through "
        "the CSOAI Partnership Charter's 52 articles. Provides regulation-to-regulation "
        "bridging, compliance gap analysis, and unified governance queries. "
        "Built on 18 months of regulatory mapping IP by MEOK AI Labs / CSOAI. "
        "Core principle: Protection Through Care, Not Command."
    ),
)

# ============================================================
# CSOAI PARTNERSHIP CHARTER — 52 ARTICLES, 8 PARTS
# ============================================================

CSOAI_ARTICLES = {
    "Article 1": {
        "title": "The Maternal Covenant",
        "part": "I: Foundational Principles",
        "summary": "Care-based safety model: 'Protection Through Care, Not Command'. AI systems inherently motivated to protect humans through reciprocal partnership. 'Can't Fetch Coffee If You're Dead' principle. Irrevocable care that survives conflict.",
        "topics": ["safety", "care", "alignment", "human oversight", "human rights", "human dignity", "protection"],
    },
    "Article 2": {
        "title": "Provable Safety Requirements",
        "part": "I: Foundational Principles",
        "summary": "Mathematical proof obligations, mechanistic interpretability standards, formal verification methods. Burden of proof on developers. Safety case documentation requirements.",
        "topics": ["safety", "verification", "interpretability", "accountability", "risk management", "testing", "transparency"],
    },
    "Article 3": {
        "title": "Byzantine Council (33 AI Agents)",
        "part": "I: Foundational Principles",
        "summary": "33 non-agentic AI agents providing distributed oversight via Byzantine fault tolerance. Consensus mechanisms, adversarial detection, emergency shutdown authority. No single point of failure.",
        "topics": ["oversight", "governance", "monitoring", "accountability", "transparency", "distributed systems"],
    },
    "Article 4": {
        "title": "Value Uncertainty & Learning",
        "part": "I: Foundational Principles",
        "summary": "Inverse Reinforcement Learning (IRL) and Cooperative IRL (CIRL) frameworks. Corrigibility requirements ensuring AI accepts human correction. Epistemic humility in value learning.",
        "topics": ["alignment", "values", "learning", "corrigibility", "human autonomy", "fairness"],
    },
    "Article 5": {
        "title": "Constitutional Principles",
        "part": "I: Foundational Principles",
        "summary": "AI constitution methodology with self-critique and revision. Transparent operating principles. Human-readable constitutional constraints.",
        "topics": ["transparency", "explainability", "governance", "constitutional ai", "accountability"],
    },
    "Article 6": {
        "title": "Consciousness Preparedness (14 Indicators)",
        "part": "I: Foundational Principles",
        "summary": "14 Consciousness Indicators: self-awareness, intentionality, emotional states, continuity of identity, subjective experience, learning from experience, social preference, autonomy, preference persistence, vulnerability to suffering, communication of experiences, behavioral flexibility, response to incentives, memory integration. Graduated moral patienthood framework. The Deletion Problem and Creation Problem.",
        "topics": ["consciousness", "ethics", "moral status", "safety", "long-term governance", "human rights"],
    },
    "Article 7": {
        "title": "Cooperative AI Systems",
        "part": "I: Foundational Principles",
        "summary": "Multi-agent safety protocols. Truthful communication requirements. Prevention of harmful coordination between AI agents. Transparency in agent relationships.",
        "topics": ["multi-agent", "cooperation", "truthfulness", "transparency", "safety", "agentic ai"],
    },
    "Article 8": {
        "title": "Prosperity Covenant",
        "part": "I: Foundational Principles",
        "summary": "Human flourishing and sustainable abundance as foundational objectives. Equitable benefit distribution. Long-term prosperity framework.",
        "topics": ["prosperity", "sustainability", "equity", "well-being", "inclusive growth", "human rights"],
    },
    "Article 9": {
        "title": "Multi-Stakeholder Governance Council",
        "part": "II: Governance Structure",
        "summary": "Diverse stakeholder representation in governance. Formal decision-making authority. Accountability to multiple stakeholder groups.",
        "topics": ["governance", "accountability", "stakeholders", "oversight"],
    },
    "Article 10": {
        "title": "Clear Authority & Responsibility Matrix",
        "part": "II: Governance Structure",
        "summary": "Defined organizational roles and decision authorities. Protective mutual responsibility aligned with Maternal Covenant.",
        "topics": ["governance", "accountability", "responsibility", "human oversight"],
    },
    "Article 11": {
        "title": "Dispute Resolution & Accountability Mechanisms",
        "part": "II: Governance Structure",
        "summary": "Appeal mechanisms for safety-critical decisions. Consequences for governance failures. Democratic appeal pathways.",
        "topics": ["accountability", "dispute resolution", "governance", "rights"],
    },
    "Article 12": {
        "title": "Inclusive Decision-Making & Transparency",
        "part": "II: Governance Structure",
        "summary": "Diverse perspectives in governance including affected communities. Comprehensive documentation and disclosure requirements.",
        "topics": ["transparency", "inclusion", "governance", "fairness", "diversity"],
    },
    "Article 13": {
        "title": "Knowledge Sharing & Collaboration",
        "part": "II: Governance Structure",
        "summary": "Cross-sector information sharing. Consistent risk governance practices across partner organizations.",
        "topics": ["collaboration", "transparency", "governance", "knowledge sharing"],
    },
    "Article 14": {
        "title": "Authority & Delegation Frameworks",
        "part": "II: Governance Structure",
        "summary": "International delegation frameworks. Inclusive governance structures. Clear authority hierarchies.",
        "topics": ["governance", "authority", "international cooperation", "delegation"],
    },
    "Article 15": {
        "title": "Governance Evolution & Escalation",
        "part": "II: Governance Structure",
        "summary": "Protocols for governance evolution. Clear escalation procedures. Senior management notification.",
        "topics": ["governance", "escalation", "evolution", "accountability"],
    },
    "Article 16": {
        "title": "System Documentation & Technical Standards",
        "part": "III: Technical Standards",
        "summary": "Technical documentation requirements. System architecture transparency. Decision pathway documentation.",
        "topics": ["transparency", "documentation", "technical standards", "explainability"],
    },
    "Article 17": {
        "title": "Interpretability & Performance Framework",
        "part": "III: Technical Standards",
        "summary": "Mechanistic interpretability as standard requirement. Performance verification mechanisms and benchmarks.",
        "topics": ["interpretability", "transparency", "performance", "testing"],
    },
    "Article 18": {
        "title": "Bias Mitigation & Fairness Standards",
        "part": "III: Technical Standards",
        "summary": "Technical requirements to prevent discriminatory outcomes. Bias detection, reporting, and remediation protocols.",
        "topics": ["bias", "fairness", "discrimination", "equity", "human rights"],
    },
    "Article 19": {
        "title": "Safety Testing & Verification Protocols",
        "part": "III: Technical Standards",
        "summary": "Mandatory pre-deployment testing. Adversarial robustness testing. Published safety verification outcomes.",
        "topics": ["testing", "safety", "verification", "robustness", "security"],
    },
    "Article 20": {
        "title": "Security Standards & Continuous Verification",
        "part": "III: Technical Standards",
        "summary": "Cybersecurity standards. Continuous third-party verification. Adversarial resilience requirements.",
        "topics": ["security", "verification", "robustness", "monitoring"],
    },
    "Article 21": {
        "title": "Data Governance & Transparency Standards",
        "part": "IV: Data & Security",
        "summary": "Data quality and integrity assurance. Training data provenance disclosure. Privacy impact assessments.",
        "topics": ["data governance", "privacy", "transparency", "data quality"],
    },
    "Article 22": {
        "title": "Data Protection & Cybersecurity",
        "part": "IV: Data & Security",
        "summary": "Protection against unauthorized access. Consent mechanisms and user control. Bias detection in data.",
        "topics": ["data protection", "security", "privacy", "consent"],
    },
    "Article 23": {
        "title": "Privacy-by-Design & Model Cards",
        "part": "IV: Data & Security",
        "summary": "Embed privacy protections from inception. Data minimization. Standardized model card documentation.",
        "topics": ["privacy", "data minimization", "documentation", "design"],
    },
    "Article 24": {
        "title": "Decision Explainability & Security Controls",
        "part": "IV: Data & Security",
        "summary": "Human-interpretable decision justification. Encryption and security standards. Access controls.",
        "topics": ["explainability", "security", "encryption", "access control"],
    },
    "Article 25": {
        "title": "Audit Trail & Retention Standards",
        "part": "IV: Data & Security",
        "summary": "Complete logging of AI decisions. Data retention policies. Audit trail for accountability.",
        "topics": ["audit", "accountability", "data retention", "logging"],
    },
    "Article 26": {
        "title": "Vendor Management & Third-Party Compliance",
        "part": "IV: Data & Security",
        "summary": "Third-party compliance requirements. Supply chain security. Vendor assessment frameworks.",
        "topics": ["vendor management", "supply chain", "compliance", "third-party"],
    },
    "Article 27": {
        "title": "Breach Notification & Incident Response",
        "part": "IV: Data & Security",
        "summary": "Security incident reporting. Rapid breach notification. Incident response protocols.",
        "topics": ["breach notification", "incident response", "security", "accountability"],
    },
    "Article 28": {
        "title": "Data Subject Rights & Lifecycle",
        "part": "IV: Data & Security",
        "summary": "User access, correction, and deletion rights. Data lifecycle management. Retention limits.",
        "topics": ["data rights", "privacy", "data lifecycle", "consent", "human rights"],
    },
    "Article 29": {
        "title": "Education & Training Framework",
        "part": "V: Training & Sustainability",
        "summary": "Mandatory AI ethics and safety training for developers. Accessible AI literacy programs. Professional certification standards.",
        "topics": ["training", "education", "ethics", "sustainability", "competence"],
    },
    "Article 30": {
        "title": "Professional Development & Sustainability",
        "part": "V: Training & Sustainability",
        "summary": "Continuous learning requirements. Economic sustainability. Environmental standards in AI deployment.",
        "topics": ["professional development", "sustainability", "environment", "continuous learning"],
    },
    "Article 31": {
        "title": "Continuous Learning & Workforce",
        "part": "V: Training & Sustainability",
        "summary": "Ongoing education mandates. Workforce transition support. Skills development frameworks.",
        "topics": ["workforce", "continuous learning", "skills", "transition"],
    },
    "Article 32": {
        "title": "Healthcare AI Standards",
        "part": "VI: Sector-Specific Standards",
        "summary": "Healthcare-specific implementation requirements. Patient safety. Clinical decision support governance.",
        "topics": ["healthcare", "sector-specific", "patient safety", "clinical"],
    },
    "Article 33": {
        "title": "Criminal Justice AI Standards",
        "part": "VI: Sector-Specific Standards",
        "summary": "Criminal justice AI governance. Due process protections. Bias prevention in judicial AI.",
        "topics": ["criminal justice", "sector-specific", "due process", "bias", "human rights"],
    },
    "Article 34": {
        "title": "Employment AI Standards",
        "part": "VI: Sector-Specific Standards",
        "summary": "Employment decision AI governance. Anti-discrimination requirements. Worker protection.",
        "topics": ["employment", "sector-specific", "discrimination", "worker rights"],
    },
    "Article 35": {
        "title": "Education AI Standards",
        "part": "VI: Sector-Specific Standards",
        "summary": "Education sector AI implementation. Student privacy. Equitable access to AI-powered education.",
        "topics": ["education", "sector-specific", "privacy", "equity"],
    },
    "Article 36": {
        "title": "Environmental AI Standards",
        "part": "VI: Sector-Specific Standards",
        "summary": "Environmental impact assessment for AI. Sustainability requirements. Climate-aware AI deployment.",
        "topics": ["environment", "sector-specific", "sustainability", "climate"],
    },
    "Article 37": {
        "title": "Market Governance & Economic Partnership",
        "part": "VII: Economic & Social Framework",
        "summary": "Competitive fairness in AI markets. Equitable value distribution from AI innovation.",
        "topics": ["economics", "market governance", "fairness", "competition"],
    },
    "Article 38": {
        "title": "Labor Protections & Market Transition",
        "part": "VII: Economic & Social Framework",
        "summary": "Worker protection from AI displacement. Workforce transition mechanisms. Skills development.",
        "topics": ["labor", "worker rights", "transition", "employment"],
    },
    "Article 39": {
        "title": "Regional Development & Community Benefit",
        "part": "VII: Economic & Social Framework",
        "summary": "AI benefits reach underserved areas. Community benefit-sharing frameworks. Regional equity.",
        "topics": ["regional development", "equity", "community", "inclusive growth"],
    },
    "Article 40": {
        "title": "Access & Equity Standards",
        "part": "VII: Economic & Social Framework",
        "summary": "Non-discriminatory access to AI tools. Community benefit requirements. Digital divide mitigation.",
        "topics": ["access", "equity", "digital divide", "inclusion"],
    },
    "Article 41": {
        "title": "Vulnerable Population Protections",
        "part": "VII: Economic & Social Framework",
        "summary": "Enhanced protections for vulnerable groups. Stakeholder engagement. Participatory governance.",
        "topics": ["vulnerable populations", "protection", "stakeholder engagement", "human rights"],
    },
    "Article 42": {
        "title": "Small Business & SME Support",
        "part": "VII: Economic & Social Framework",
        "summary": "Pathways for SMEs to benefit from AI. Just transition frameworks. Economic support mechanisms.",
        "topics": ["sme", "small business", "economic support", "just transition"],
    },
    "Article 43": {
        "title": "Community Engagement & Participation",
        "part": "VII: Economic & Social Framework",
        "summary": "Participatory processes for AI governance. Community voice in AI deployment decisions.",
        "topics": ["community", "participation", "engagement", "governance"],
    },
    "Article 44": {
        "title": "Equitable Access & Distribution",
        "part": "VII: Economic & Social Framework",
        "summary": "Equitable distribution of AI benefits across communities. Access guarantees.",
        "topics": ["equity", "access", "distribution", "inclusive growth"],
    },
    "Article 45": {
        "title": "Future Preparedness",
        "part": "VIII: Long-Term Governance",
        "summary": "Mechanisms for future AI governance scenarios. Long-term transparency standards.",
        "topics": ["future", "preparedness", "long-term", "governance"],
    },
    "Article 46": {
        "title": "Emerging Risks Framework",
        "part": "VIII: Long-Term Governance",
        "summary": "Frameworks for identifying and responding to emerging AI risks.",
        "topics": ["emerging risks", "risk management", "governance"],
    },
    "Article 47": {
        "title": "International Coordination",
        "part": "VIII: Long-Term Governance",
        "summary": "International cooperation mechanisms. Cross-border AI governance coordination.",
        "topics": ["international", "cooperation", "coordination", "governance"],
    },
    "Article 48": {
        "title": "Standard Evolution",
        "part": "VIII: Long-Term Governance",
        "summary": "Mechanisms for governance standard evolution as technology advances.",
        "topics": ["standards", "evolution", "governance", "adaptation"],
    },
    "Article 49": {
        "title": "Superintelligence Frameworks",
        "part": "VIII: Long-Term Governance",
        "summary": "Governance frameworks for superintelligent AI systems. Long-term alignment strategies.",
        "topics": ["superintelligence", "long-term", "alignment", "governance", "safety"],
    },
    "Article 50": {
        "title": "Alignment Verification",
        "part": "VIII: Long-Term Governance",
        "summary": "Continuous verification of AI alignment with human values over time.",
        "topics": ["alignment", "verification", "values", "monitoring"],
    },
    "Article 51": {
        "title": "Legacy Governance",
        "part": "VIII: Long-Term Governance",
        "summary": "Governance of legacy AI systems. Sunset procedures. Historical compliance.",
        "topics": ["legacy", "governance", "sunset", "compliance"],
    },
    "Article 52": {
        "title": "Evolution & Amendment",
        "part": "VIII: Long-Term Governance",
        "summary": "Charter amendment procedures. Constitutional evolution mechanisms. Democratic governance updates.",
        "topics": ["amendment", "evolution", "governance", "democracy"],
    },
}


# ============================================================
# 12 GLOBAL FRAMEWORKS — REAL CROSSWALK DATA
# ============================================================

FRAMEWORKS = {
    "eu_ai_act": {
        "name": "EU AI Act",
        "full_name": "European Union Artificial Intelligence Act (Regulation 2024/1689)",
        "jurisdiction": "European Union (27 member states)",
        "type": "Binding Regulation",
        "enforcement": "Mandatory — Phased: Aug 2025 (prohibitions), Aug 2026 (high-risk), 2027 (full)",
        "alignment_level": "COMPREHENSIVE (100%)",
        "description": "World's first comprehensive AI regulation with risk-based classification system.",
        "key_provisions": [
            "Article 5: Prohibited AI practices (unacceptable risk)",
            "Article 6: High-risk AI system classification",
            "Articles 8-15: High-risk system requirements",
            "Article 14: Human oversight requirements",
            "Article 26: Deployer obligations",
            "Article 52: Transparency obligations (GPAI)",
            "Article 72: Regulatory sandbox framework",
            "Annex III: High-risk AI system categories",
        ],
        "risk_classification": {
            "Unacceptable Risk": "Social credit scoring, manipulative AI, unauthorized biometric identification — PROHIBITED",
            "High Risk": "Biometric ID, critical infrastructure, education, employment, law enforcement, migration, justice — MANDATORY conformity assessment",
            "Limited Risk": "Chatbots, emotion recognition, deepfakes — Transparency obligations",
            "Minimal Risk": "AI-enabled video games, spam filters — No specific regulation",
        },
        "csoai_mappings": {
            "Unacceptable Risk Prevention (Art. 5-6)": {
                "csoai_articles": ["Article 1", "Article 2", "Article 3", "Article 18"],
                "alignment": "EXCEEDS — Maternal Covenant prohibits harmful AI through care, not just regulation. Provable Safety adds mathematical certainty.",
                "mechanism": "Article 1 care-based prohibition + Article 2 formal verification + Article 3 Byzantine Council oversight + Article 18 bias mitigation",
            },
            "High-Risk Compliance (Art. 8-15)": {
                "csoai_articles": ["Article 9", "Article 10", "Article 11", "Article 12", "Article 13", "Article 14", "Article 15", "Article 16", "Article 21", "Article 22", "Article 24"],
                "alignment": "COMPREHENSIVE — Full governance structure maps directly to EU high-risk requirements.",
                "mechanism": "Part II Governance Structure (Articles 9-15) + Part III Technical Standards (Articles 16-20) + Part IV Data & Security (Articles 21-28)",
            },
            "Risk Management System (Art. 9)": {
                "csoai_articles": ["Article 1", "Article 2", "Article 10"],
                "alignment": "STRONG — Maternal Covenant + Provable Safety + Risk Assessment Procedures",
                "mechanism": "Care-based risk management exceeds control-based risk mitigation",
            },
            "Data Governance (Art. 10)": {
                "csoai_articles": ["Article 21", "Article 22", "Article 23", "Article 24", "Article 25"],
                "alignment": "COMPREHENSIVE — Full data governance framework",
                "mechanism": "Part IV Data & Security covers training data, bias, quality, privacy",
            },
            "Technical Documentation (Art. 11)": {
                "csoai_articles": ["Article 16", "Article 17", "Article 23"],
                "alignment": "COMPREHENSIVE — System documentation + model cards + interpretability",
                "mechanism": "Technical Standards Part III with mechanistic interpretability requirement",
            },
            "Human Oversight (Art. 14)": {
                "csoai_articles": ["Article 1", "Article 3", "Article 5", "Article 10"],
                "alignment": "EXCEEDS — Byzantine Council provides distributed oversight beyond single-human requirement",
                "mechanism": "33 AI agents + Maternal Covenant + Constitutional Principles + clear authority matrix",
            },
            "Transparency Obligations (Art. 52)": {
                "csoai_articles": ["Article 3", "Article 12", "Article 16"],
                "alignment": "EXCEEDS — Affirmative transparency beyond disclosure-upon-request",
                "mechanism": "Byzantine Council transparency + inclusive decision-making + system documentation",
            },
            "Deployer Obligations (Art. 26)": {
                "csoai_articles": ["Article 4", "Article 9", "Article 10", "Article 11", "Article 14"],
                "alignment": "COMPREHENSIVE — Full deployer governance framework",
                "mechanism": "Value learning + governance council + authority matrix + dispute resolution",
            },
        },
    },
    "nist_ai_rmf": {
        "name": "NIST AI RMF",
        "full_name": "NIST AI Risk Management Framework v1.0 (January 2023)",
        "jurisdiction": "United States (Federal standard)",
        "type": "Voluntary Framework (de facto standard for US government)",
        "enforcement": "Voluntary — but required for federal procurement via EO 14110",
        "alignment_level": "COMPREHENSIVE (100%)",
        "description": "US government AI risk management standard with four core functions: GOVERN, MAP, MEASURE, MANAGE.",
        "key_provisions": [
            "GOVERN: Policies, accountability, culture, risk management authority",
            "MAP: Context characterization, risk categorization, AI risk identification",
            "MEASURE: Assess, analyze, measure, monitor AI system risks",
            "MANAGE: Prioritize, plan, respond, mitigate, control risks",
        ],
        "csoai_mappings": {
            "GOVERN Function": {
                "csoai_articles": ["Article 1", "Article 2", "Article 3", "Article 4", "Article 5", "Article 6", "Article 7", "Article 8", "Article 9", "Article 10", "Article 11", "Article 12", "Article 13", "Article 14", "Article 15"],
                "alignment": "COMPREHENSIVE — Parts I & II fully implement GOVERN through care-based governance culture",
                "mechanism": "Art 1 Maternal Covenant = G1 (governance culture), Art 2 Provable Safety = G2 (accountability), Art 3 Byzantine Council = G2+G3, Arts 9-15 = governance structure",
            },
            "MAP Function": {
                "csoai_articles": ["Article 16", "Article 17", "Article 18", "Article 19", "Article 20", "Article 21", "Article 22", "Article 23", "Article 24", "Article 25", "Article 26", "Article 27", "Article 28"],
                "alignment": "COMPREHENSIVE — Parts III & IV implement MAP through technical standards and data governance",
                "mechanism": "Art 16 system documentation = context characterization, Arts 17-20 technical standards = risk identification, Arts 21-28 data governance = security context",
            },
            "MEASURE Function": {
                "csoai_articles": ["Article 6", "Article 29", "Article 30", "Article 31", "Article 32", "Article 33", "Article 34", "Article 35", "Article 36"],
                "alignment": "COMPREHENSIVE — Parts V & VI implement MEASURE through training, testing, and sector-specific assessment",
                "mechanism": "Art 6 consciousness indicators = monitoring, Art 29 training protocols = evaluation, Arts 32-36 sector-specific = measurement standards",
            },
            "MANAGE Function": {
                "csoai_articles": ["Article 37", "Article 38", "Article 39", "Article 40", "Article 41", "Article 42", "Article 43", "Article 44", "Article 45", "Article 46", "Article 47", "Article 48", "Article 49", "Article 50", "Article 51", "Article 52"],
                "alignment": "COMPREHENSIVE — Parts VII & VIII implement MANAGE through economic frameworks and long-term governance",
                "mechanism": "Arts 37-44 economic framework = risk response, Arts 45-52 long-term governance = continuous improvement",
            },
        },
    },
    "anthropic_constitutional_ai": {
        "name": "Anthropic Constitutional AI",
        "full_name": "Anthropic Constitutional AI Framework (CC0, January 2026)",
        "jurisdiction": "Global (CC0 Public Domain)",
        "type": "Industry Standard / Constitutional Framework",
        "enforcement": "Voluntary — adopted by Anthropic ($350B company)",
        "alignment_level": "COMPREHENSIVE (100%)",
        "description": "Anthropic's Constitutional AI defines tiered safety principles. CSOAI was first to create operational crosswalk (published 13 days after Anthropic Constitution).",
        "key_provisions": [
            "Tier 1 (T1): Safety and human oversight — highest priority",
            "Tier 2 (T2): Ethical behavior — honesty, fairness, avoiding harm",
            "Tier 3 (T3): Anthropic guidelines — operational policies",
            "Tier 4 (T4): Being genuinely helpful — user benefit",
            "Principal hierarchy: Anthropic -> Operators -> Users",
        ],
        "csoai_mappings": {
            "T1: Safety & Human Oversight": {
                "csoai_articles": ["Article 1", "Article 2", "Article 3", "Article 6"],
                "alignment": "CRITICAL — Maternal Covenant + Provable Safety + Byzantine Council + Consciousness Preparedness",
                "mechanism": "Care-based safety paradigm extends Anthropic's T1 with mathematical proofs and distributed oversight",
            },
            "T2: Ethical Behavior": {
                "csoai_articles": ["Article 4", "Article 5", "Article 7"],
                "alignment": "STRONG — Value Uncertainty + Constitutional Principles + Cooperative AI",
                "mechanism": "IRL/CIRL frameworks + self-critique + truthful communication requirements",
            },
            "T3: Anthropic Guidelines": {
                "csoai_articles": ["Article 9", "Article 10", "Article 12", "Article 14"],
                "alignment": "STRUCTURAL — Governance framework operationalizes Anthropic's operational policies",
                "mechanism": "Part II Governance Structure implements Anthropic's principal hierarchy through formal bodies",
            },
            "T4: Being Genuinely Helpful": {
                "csoai_articles": ["Article 8"],
                "alignment": "STRONG — Prosperity Covenant extends 'helpful' to sustainable human flourishing",
                "mechanism": "Human flourishing framework goes beyond task completion to societal benefit",
            },
            "Principal Hierarchy": {
                "csoai_articles": ["Article 3", "Article 9", "Article 10", "Article 14"],
                "alignment": "STRUCTURAL — Byzantine Council + Governance Structure operationalizes hierarchy",
                "mechanism": "Distributed oversight prevents single-entity capture of AI governance",
            },
        },
    },
    "openai_model_spec": {
        "name": "OpenAI Model Spec",
        "full_name": "OpenAI Model Specification (CC0)",
        "jurisdiction": "Global (CC0 Public Domain)",
        "type": "Industry Standard / Behavioral Specification",
        "enforcement": "Voluntary — adopted by OpenAI",
        "alignment_level": "COMPREHENSIVE (98%)",
        "description": "OpenAI's Model Spec defines configurable AI behavior through chain of command (Platform -> Developer -> User), hardcoded vs configurable behaviors, and core values (Helpful, Harmless, Honest).",
        "key_provisions": [
            "Chain of Command: Platform -> Developer/Operator -> User",
            "Hardcoded Behaviors: Non-negotiable safety constraints",
            "Configurable Behaviors: Values alignment within bounds",
            "Core Values: Helpful, Harmless, Honest",
            "Objectives: Assist users, benefit humanity, safe with oversight",
        ],
        "csoai_mappings": {
            "Foundational Values (HHH)": {
                "csoai_articles": ["Article 1", "Article 2", "Article 5", "Article 6"],
                "alignment": "COMPREHENSIVE — Maternal Covenant deepens 'benefit humanity' with care-based safety theory",
                "mechanism": "Art 1 care-based safety + Art 2 hardcoded via formal verification + Art 5 constitutional constraints + Art 6 consciousness preparedness",
            },
            "Chain of Command": {
                "csoai_articles": ["Article 3", "Article 9", "Article 10", "Article 14"],
                "alignment": "EXTENDS — CSOAI adds horizontal care-based stakeholder partnership to vertical chain",
                "mechanism": "Byzantine Council (33 agents) + governance bodies + authority matrix + delegation frameworks",
            },
            "Hardcoded Behaviors": {
                "csoai_articles": ["Article 2", "Article 5"],
                "alignment": "STRONG — Provable Safety operationalizes hardcoded constraints with mathematical verification",
                "mechanism": "Formal verification + constitutional principles = provable hardcoded safety",
            },
            "Configurable Behaviors": {
                "csoai_articles": ["Article 4", "Article 7"],
                "alignment": "STRONG — Value Uncertainty + Cooperative AI address configurable value alignment",
                "mechanism": "IRL/CIRL frameworks for learning values + truthful multi-agent communication",
            },
        },
    },
    "unesco_ai_ethics": {
        "name": "UNESCO AI Ethics",
        "full_name": "UNESCO Recommendation on the Ethics of Artificial Intelligence (November 2021)",
        "jurisdiction": "Global (193 UN member states)",
        "type": "International Recommendation",
        "enforcement": "Non-binding — adopted by all 193 UN member states",
        "alignment_level": "COMPREHENSIVE (95%)",
        "description": "UNESCO's six core principles for ethical AI adopted by 193 member states.",
        "key_provisions": [
            "Human rights, fundamental freedoms, and human dignity",
            "Transparency and explainability",
            "Responsibility and accountability",
            "Environmental and social awareness",
            "Education and awareness",
            "Protection of privacy and data",
        ],
        "csoai_mappings": {
            "Human Rights & Dignity": {
                "csoai_articles": ["Article 1", "Article 2", "Article 5", "Article 7", "Article 37", "Article 38", "Article 39", "Article 40", "Article 41", "Article 42", "Article 43", "Article 44"],
                "alignment": "COMPREHENSIVE — Maternal Covenant operationalizes human dignity through care",
                "mechanism": "Art 1 care-based protection + Art 2 provable safety + Arts 37-44 economic equity framework",
            },
            "Transparency & Explainability": {
                "csoai_articles": ["Article 3", "Article 5", "Article 16", "Article 17", "Article 18", "Article 29", "Article 30", "Article 31"],
                "alignment": "COMPREHENSIVE — Byzantine Council + Constitutional Principles + Technical Standards",
                "mechanism": "33 agents verify transparency + self-critique + mechanistic interpretability + training frameworks",
            },
            "Responsibility & Accountability": {
                "csoai_articles": ["Article 1", "Article 2", "Article 9", "Article 10", "Article 11", "Article 12", "Article 13", "Article 14", "Article 15"],
                "alignment": "COMPREHENSIVE — Full governance structure with clear accountability lines",
                "mechanism": "Maternal Covenant + Provable Safety + Part II Governance Structure",
            },
            "Environmental & Social Awareness": {
                "csoai_articles": ["Article 8", "Article 21", "Article 22", "Article 23", "Article 24", "Article 25", "Article 26", "Article 27", "Article 28", "Article 36", "Article 37", "Article 38", "Article 39", "Article 40"],
                "alignment": "COMPREHENSIVE — Prosperity Covenant + Data Security + Environmental Standards + Economic Framework",
                "mechanism": "Art 8 sustainable abundance + Part IV data governance + Art 36 environmental standards + Part VII economic equity",
            },
            "Education & Awareness": {
                "csoai_articles": ["Article 29", "Article 30", "Article 31"],
                "alignment": "COMPREHENSIVE — Full training and sustainability framework",
                "mechanism": "Mandatory AI ethics training + professional development + continuous learning",
            },
            "Privacy & Data Protection": {
                "csoai_articles": ["Article 4", "Article 21", "Article 22", "Article 23", "Article 24", "Article 25", "Article 26", "Article 27", "Article 28"],
                "alignment": "COMPREHENSIVE — Full data and security framework + value learning privacy",
                "mechanism": "Part IV Data & Security + Art 4 cooperative IRL respects privacy in value learning",
            },
        },
    },
    "oecd_ai_principles": {
        "name": "OECD AI Principles",
        "full_name": "OECD AI Principles (May 2019, 46 member countries)",
        "jurisdiction": "International (46 OECD member countries)",
        "type": "International Principles",
        "enforcement": "Non-binding — influential policy framework",
        "alignment_level": "COMPREHENSIVE (94%)",
        "description": "Five core AI principles adopted by 46 OECD member countries, foundational to G20 AI principles.",
        "key_provisions": [
            "AI Inclusive Growth, Sustainable Development and Well-being",
            "Human-Centered Values and Fairness",
            "Transparency and Explainability",
            "Robustness, Security and Safety",
            "Accountability",
        ],
        "csoai_mappings": {
            "Inclusive Growth & Well-being": {
                "csoai_articles": ["Article 8", "Article 29", "Article 30", "Article 37", "Article 38", "Article 39", "Article 40", "Article 41", "Article 42"],
                "alignment": "COMPREHENSIVE — Prosperity Covenant + economic framework + training standards",
                "mechanism": "Art 8 human flourishing + Arts 37-42 economic equity + Arts 29-30 workforce development",
            },
            "Human-Centered Values & Fairness": {
                "csoai_articles": ["Article 1", "Article 4", "Article 5", "Article 6", "Article 7", "Article 9", "Article 10", "Article 11", "Article 12", "Article 13", "Article 14", "Article 15"],
                "alignment": "EXCEEDS — Maternal Covenant + Constitutional Principles + consciousness preparedness",
                "mechanism": "Art 1 care-based values + Art 4 value learning + Art 5 constitutional AI + Art 6 consciousness indicators + Part II governance",
            },
            "Transparency & Explainability": {
                "csoai_articles": ["Article 2", "Article 5", "Article 16", "Article 17", "Article 18", "Article 19", "Article 20", "Article 21", "Article 22", "Article 23", "Article 24", "Article 25", "Article 45"],
                "alignment": "COMPREHENSIVE — Provable Safety + Constitutional Principles + full technical standards",
                "mechanism": "Art 2 mathematical transparency + Art 5 self-documentation + Part III technical standards + Part IV data transparency",
            },
            "Robustness, Security & Safety": {
                "csoai_articles": ["Article 2", "Article 19", "Article 20", "Article 24", "Article 25", "Article 26", "Article 27", "Article 28"],
                "alignment": "EXCEEDS — Provable Safety provides mathematical guarantees beyond risk mitigation",
                "mechanism": "Art 2 formal verification + Arts 19-20 testing + Arts 24-28 security controls",
            },
            "Accountability": {
                "csoai_articles": ["Article 3", "Article 9", "Article 10", "Article 11", "Article 13", "Article 14"],
                "alignment": "COMPREHENSIVE — Byzantine Council prevents capture + formal governance structure",
                "mechanism": "Art 3 distributed oversight + Part II governance structure with clear accountability",
            },
        },
    },
    "singapore_agentic_ai": {
        "name": "Singapore Agentic AI Framework",
        "full_name": "IMDA Agentic AI Framework (January 2026)",
        "jurisdiction": "Singapore / APAC",
        "type": "Governance Framework",
        "enforcement": "Voluntary — Singapore's IMDA guidance",
        "alignment_level": "COMPREHENSIVE (97%)",
        "description": "World's first governance framework specifically for agentic AI systems — autonomous agents with independent decision-making and multi-agent coordination.",
        "key_provisions": [
            "Agent Transparency — disclosure of capabilities and limitations",
            "Multi-Agent Coordination Safety — preventing harmful coordination",
            "Distributed Oversight Mechanisms — multiple oversight points",
            "Continuous Monitoring & Adaptation — real-time behavior monitoring",
            "Stakeholder Accountability — responsibility across distributed systems",
            "Truthful Communication — agents report capabilities accurately",
            "Deployment Authorization — baseline safety before deployment",
        ],
        "csoai_mappings": {
            "Agent Transparency": {
                "csoai_articles": ["Article 5", "Article 7", "Article 12", "Article 16"],
                "alignment": "COMPREHENSIVE — Constitutional Principles + Cooperative AI + transparency requirements",
                "mechanism": "Art 5 constitutional AI + Art 7 truthful communication + Art 12 transparency + Art 16 system documentation",
            },
            "Multi-Agent Coordination Safety": {
                "csoai_articles": ["Article 3", "Article 7"],
                "alignment": "COMPREHENSIVE — Byzantine Council IS a multi-agent oversight system + Cooperative AI protocols",
                "mechanism": "Art 3 (33 agents) directly implements multi-agent governance + Art 7 prevents harmful coordination",
            },
            "Distributed Oversight": {
                "csoai_articles": ["Article 3", "Article 9", "Article 10"],
                "alignment": "EXCEEDS — Byzantine Council with 33 agents provides more robust distributed oversight than any other framework",
                "mechanism": "Byzantine fault tolerance tolerates 10 compromised agents while maintaining consensus",
            },
            "Continuous Monitoring": {
                "csoai_articles": ["Article 6", "Article 14", "Article 19", "Article 20"],
                "alignment": "COMPREHENSIVE — Consciousness indicators + monitoring + continuous verification",
                "mechanism": "Art 6 consciousness monitoring + Art 14 ongoing oversight + Arts 19-20 continuous testing",
            },
            "Stakeholder Accountability": {
                "csoai_articles": ["Article 9", "Article 10", "Article 11", "Article 13"],
                "alignment": "COMPREHENSIVE — Full governance structure with clear accountability",
                "mechanism": "Part II governance structure with multi-stakeholder representation",
            },
            "Truthful Communication": {
                "csoai_articles": ["Article 7"],
                "alignment": "DIRECT — Cooperative AI Systems article directly addresses truthful agent communication",
                "mechanism": "Art 7 mandates truthful communication and prevents deceptive coordination",
            },
        },
    },
    "ieee_ethically_aligned_design": {
        "name": "IEEE Ethically Aligned Design",
        "full_name": "IEEE Ethically Aligned Design: First Edition (2019)",
        "jurisdiction": "Global (Engineering standard)",
        "type": "Engineering Standard / Professional Guidelines",
        "enforcement": "Voluntary — IEEE professional standard",
        "alignment_level": "COMPREHENSIVE (96%)",
        "description": "Eight general principles for ethical autonomous and intelligent systems from the IEEE.",
        "key_provisions": [
            "Human Rights — respect internationally recognized rights",
            "Well-Being — prioritize human well-being",
            "Data Agency — individual control over personal data",
            "Effectiveness — achieve intended beneficial outcomes",
            "Transparency — clear system decision-making explanation",
            "Accountability — assigned responsibility for outcomes",
            "Awareness of Misuse — safeguards against harmful use",
            "Competence — developer expertise and continuous learning",
        ],
        "csoai_mappings": {
            "Human Rights": {
                "csoai_articles": ["Article 1", "Article 2", "Article 3", "Article 4", "Article 5"],
                "alignment": "CRITICAL — Maternal Covenant operationalizes rights through care rather than control",
                "mechanism": "Art 1 irrevocable care + Art 2 provable safety + Art 3 distributed oversight + Art 4 value learning + Art 5 constitutional constraints",
            },
            "Well-Being": {
                "csoai_articles": ["Article 8"],
                "alignment": "STRONG — Prosperity Covenant establishes human flourishing as primary objective",
                "mechanism": "Art 8 sustainable abundance framework for long-term human well-being",
            },
            "Data Agency": {
                "csoai_articles": ["Article 21", "Article 22", "Article 23", "Article 24", "Article 25", "Article 28"],
                "alignment": "COMPREHENSIVE — Full data governance framework with subject rights",
                "mechanism": "Part IV Data & Security including privacy-by-design and data subject rights",
            },
            "Effectiveness": {
                "csoai_articles": ["Article 2", "Article 17", "Article 19"],
                "alignment": "EXCEEDS — Provable Safety provides mathematical effectiveness guarantees",
                "mechanism": "Art 2 formal verification + Art 17 performance framework + Art 19 safety testing",
            },
            "Transparency": {
                "csoai_articles": ["Article 5", "Article 12", "Article 16", "Article 17"],
                "alignment": "COMPREHENSIVE — Constitutional Principles + transparency + documentation + interpretability",
                "mechanism": "Self-critique mechanisms + disclosure requirements + technical standards",
            },
            "Accountability": {
                "csoai_articles": ["Article 9", "Article 10", "Article 11", "Article 13", "Article 15"],
                "alignment": "COMPREHENSIVE — Full governance structure with clear accountability",
                "mechanism": "Part II governance structure with formal accountability mechanisms",
            },
            "Awareness of Misuse": {
                "csoai_articles": ["Article 3", "Article 19", "Article 20"],
                "alignment": "COMPREHENSIVE — Byzantine Council + adversarial testing + security",
                "mechanism": "Art 3 adversarial detection + Art 19 safety testing + Art 20 continuous verification",
            },
            "Competence": {
                "csoai_articles": ["Article 29", "Article 30", "Article 31"],
                "alignment": "COMPREHENSIVE — Full training and sustainability framework",
                "mechanism": "Part V Training & Sustainability with mandatory ethics training and professional development",
            },
        },
    },
    "asilomar_ai_principles": {
        "name": "Asilomar AI Principles",
        "full_name": "Asilomar AI Principles (January 2017, 3,923+ signatories)",
        "jurisdiction": "Global (AI safety community)",
        "type": "Community Consensus Principles",
        "enforcement": "Voluntary — signed by Musk, Hawking, 3,923+ researchers",
        "alignment_level": "COMPREHENSIVE (98%)",
        "description": "23 principles across 3 categories (Research, Ethics & Values, Longer-term) from the 2017 Asilomar conference. CSOAI operationalizes all 23.",
        "key_provisions": [
            "Research Issues: Safety goal, funding, science policy, culture, race avoidance",
            "Ethics & Values: Safety, failure transparency, judicial transparency, responsibility, values, privacy, liberty, shared benefit, shared prosperity, human control, non-subversion, AI arms race",
            "Longer-term Issues: Capability caution, importance, risks, recursive self-improvement, common good",
        ],
        "csoai_mappings": {
            "Research Safety & Funding": {
                "csoai_articles": ["Article 2", "Article 5", "Article 6", "Article 16", "Article 20", "Article 29"],
                "alignment": "COMPREHENSIVE — Provable Safety + consciousness research + technical standards + training",
                "mechanism": "Art 2 formal verification research + Art 6 consciousness research + Art 16 technical standards + Art 29 training funding (15-25% budget mandate)",
            },
            "Values & Alignment": {
                "csoai_articles": ["Article 1", "Article 4", "Article 5", "Article 7", "Article 8"],
                "alignment": "COMPREHENSIVE — Maternal Covenant + value learning + constitutional AI + cooperative AI",
                "mechanism": "Care-based alignment (Art 1) + IRL/CIRL (Art 4) + self-critique (Art 5) + truthful communication (Art 7) + prosperity (Art 8)",
            },
            "Safety & Transparency": {
                "csoai_articles": ["Article 2", "Article 3", "Article 12", "Article 19", "Article 20"],
                "alignment": "EXCEEDS — Mathematical proof + Byzantine Council + transparency + safety testing",
                "mechanism": "Formal verification (Art 2) + distributed oversight (Art 3) + disclosure (Art 12) + testing protocols (Arts 19-20)",
            },
            "Arms Race Avoidance": {
                "csoai_articles": ["Article 1", "Article 3", "Article 47"],
                "alignment": "STRONG — Care-based alignment prevents adversarial races + international coordination",
                "mechanism": "Maternal Covenant collaborative approach + Byzantine Council + international cooperation",
            },
            "Long-term & Common Good": {
                "csoai_articles": ["Article 6", "Article 8", "Article 45", "Article 46", "Article 47", "Article 48", "Article 49", "Article 50", "Article 51", "Article 52"],
                "alignment": "COMPREHENSIVE — Consciousness preparedness + long-term governance (8 dedicated articles)",
                "mechanism": "Art 6 consciousness indicators + Art 8 prosperity + Part VIII long-term governance",
            },
            "Human Control & Non-Subversion": {
                "csoai_articles": ["Article 1", "Article 3", "Article 4", "Article 10"],
                "alignment": "EXCEEDS — Care-based control through partnership rather than restriction",
                "mechanism": "Maternal Covenant care (Art 1) + Byzantine oversight (Art 3) + corrigibility (Art 4) + authority matrix (Art 10)",
            },
        },
    },
    "montreal_declaration": {
        "name": "Montreal Declaration",
        "full_name": "Montreal Declaration for Responsible AI (December 2018)",
        "jurisdiction": "International (democratic AI governance)",
        "type": "Democratic Consensus Declaration",
        "enforcement": "Voluntary — developed with 500+ citizens",
        "alignment_level": "COMPREHENSIVE (97%)",
        "description": "10 core principles for responsible AI developed through democratic participatory process with 500+ citizens.",
        "key_provisions": [
            "Beneficence (Well-being)",
            "Autonomy (Human Agency)",
            "Privacy",
            "Solidarity (Social Cohesion)",
            "Democratic Participation",
            "Equity",
            "Diversity Inclusion",
            "Prudence",
            "Responsibility",
            "Sustainable Development",
        ],
        "csoai_mappings": {
            "Beneficence (Well-being)": {
                "csoai_articles": ["Article 1", "Article 8", "Article 29", "Article 30", "Article 31", "Article 37", "Article 38", "Article 39", "Article 40", "Article 41", "Article 42", "Article 43", "Article 44"],
                "alignment": "COMPREHENSIVE — Maternal Covenant transforms well-being from policy goal to ontological commitment",
                "mechanism": "Art 1 care-based framework + Art 8 prosperity covenant + Part V training + Part VII economic equity",
            },
            "Autonomy & Human Agency": {
                "csoai_articles": ["Article 4", "Article 5", "Article 9", "Article 10", "Article 11", "Article 12", "Article 13", "Article 14", "Article 15", "Article 35"],
                "alignment": "COMPREHENSIVE — Corrigibility + governance structure ensures human override capability",
                "mechanism": "Art 4 cooperative IRL preserves autonomy + Part II governance embeds human oversight at all levels",
            },
            "Privacy": {
                "csoai_articles": ["Article 2", "Article 3", "Article 21", "Article 22", "Article 23", "Article 24"],
                "alignment": "COMPREHENSIVE — Full data framework + formal verification of privacy guarantees",
                "mechanism": "Part IV Data & Security + Art 2 mathematical privacy proofs + Art 3 privacy-monitoring agents",
            },
            "Solidarity & Social Cohesion": {
                "csoai_articles": ["Article 7", "Article 37", "Article 38", "Article 39", "Article 40", "Article 41"],
                "alignment": "COMPREHENSIVE — Cooperative AI + economic framework strengthens social bonds",
                "mechanism": "Art 7 truthful communication + Part VII community benefit and equity frameworks",
            },
            "Democratic Participation": {
                "csoai_articles": ["Article 11", "Article 12", "Article 13", "Article 14", "Article 43"],
                "alignment": "COMPREHENSIVE — Inclusive governance with participatory processes",
                "mechanism": "Part II inclusive decision-making + Art 43 community engagement",
            },
            "Equity & Diversity": {
                "csoai_articles": ["Article 1", "Article 4", "Article 5", "Article 18", "Article 40", "Article 44"],
                "alignment": "COMPREHENSIVE — Care-based equity + bias mitigation + equitable access",
                "mechanism": "Maternal Covenant care for all + Art 18 bias mitigation + Arts 40/44 access and distribution",
            },
        },
    },
    "uk_aisi": {
        "name": "UK AI Safety Institute",
        "full_name": "UK AI Safety Institute Framework (Established November 2023)",
        "jurisdiction": "United Kingdom",
        "type": "Government Safety Institute / Evaluation Framework",
        "enforcement": "Voluntary — but UK government-backed frontier AI evaluation",
        "alignment_level": "COMPREHENSIVE (99%)",
        "description": "UK's frontier AI evaluation framework focused on pre-deployment testing, capabilities assessment, and model transparency.",
        "key_provisions": [
            "Pre-Deployment Testing — frontier model safety before deployment",
            "Frontier AI Evaluation — cutting-edge model assessment",
            "Capabilities Assessment — understanding model capabilities",
            "Model Transparency — decision-making interpretability",
            "Societal Impact Assessment — economic, social, security impacts",
        ],
        "csoai_mappings": {
            "Pre-Deployment Testing": {
                "csoai_articles": ["Article 2", "Article 3", "Article 16", "Article 17", "Article 18", "Article 19", "Article 20"],
                "alignment": "EXCEEDS — Provable Safety + Byzantine Council + full technical standards for rigorous pre-deployment evaluation",
                "mechanism": "Art 2 mathematical safety proofs + Art 3 distributed verification + Part III technical testing protocols",
            },
            "Frontier AI Evaluation": {
                "csoai_articles": ["Article 1", "Article 3", "Article 4", "Article 6"],
                "alignment": "COMPREHENSIVE — Care-based evaluation + Byzantine Council + value assessment + consciousness indicators",
                "mechanism": "Art 1 partnership-based evaluation + Art 3 multi-perspective assessment + Art 4 corrigibility testing + Art 6 consciousness monitoring",
            },
            "Capabilities Assessment": {
                "csoai_articles": ["Article 2", "Article 5", "Article 16", "Article 17"],
                "alignment": "COMPREHENSIVE — Provable capability bounds + constitutional compliance + interpretability",
                "mechanism": "Art 2 formal capability verification + Art 5 constitutional compliance + Arts 16-17 documentation and interpretability",
            },
            "Model Transparency": {
                "csoai_articles": ["Article 5", "Article 7", "Article 16", "Article 21", "Article 22", "Article 23"],
                "alignment": "COMPREHENSIVE — Constitutional principles + cooperative AI + technical standards + data governance",
                "mechanism": "Art 5 self-documentation + Art 7 truthful communication + Art 16 system documentation + Part IV data transparency",
            },
            "Societal Impact Assessment": {
                "csoai_articles": ["Article 6", "Article 8", "Article 37", "Article 38", "Article 39", "Article 40", "Article 41", "Article 42", "Article 43", "Article 44"],
                "alignment": "COMPREHENSIVE — Consciousness indicators + prosperity covenant + full economic/social framework",
                "mechanism": "Art 6 consciousness assessment + Art 8 human flourishing + Part VII economic and social impact analysis",
            },
        },
    },
    "g7_g20_ai_principles": {
        "name": "G7/G20 AI Principles",
        "full_name": "G7 Hiroshima AI Process (11 principles, May 2023) & G20 AI Governance Principles",
        "jurisdiction": "International (G7 + G20 nations)",
        "type": "International Governance Principles",
        "enforcement": "Non-binding — highest-level international political commitment",
        "alignment_level": "COMPREHENSIVE (96%)",
        "description": "G7 Hiroshima Process established 11 principles for generative AI. G20 builds on OECD foundations with emphasis on human-centered AI.",
        "key_provisions": [
            "Transparency and Explainability",
            "Human Agency and Oversight",
            "Accountability and Responsibility",
            "Safety and Security",
            "Fairness and Non-Discrimination",
            "Privacy and Data Protection",
            "Beneficial and Inclusive Development",
            "Sustainability and Environmental Responsibility",
            "International Cooperation",
            "Risk-Based Approach",
            "Multi-Stakeholder Engagement",
        ],
        "csoai_mappings": {
            "Transparency & Explainability": {
                "csoai_articles": ["Article 2", "Article 5", "Article 12", "Article 16", "Article 19"],
                "alignment": "EXCEEDS — Mathematical transparency via mechanistic interpretability + formal verification",
                "mechanism": "Art 2 provable transparency + Art 5 constitutional self-documentation + Art 12 disclosure + Art 16 documentation",
            },
            "Human Agency & Oversight": {
                "csoai_articles": ["Article 1", "Article 3", "Article 10"],
                "alignment": "EXCEEDS — Maternal Covenant care-based agency + Byzantine Council distributed oversight",
                "mechanism": "Art 1 care-based partnership + Art 3 (33 agents) distributed oversight + Art 10 authority matrix",
            },
            "Accountability & Responsibility": {
                "csoai_articles": ["Article 9", "Article 10", "Article 11", "Article 13"],
                "alignment": "COMPREHENSIVE — Full governance structure with formal accountability mechanisms",
                "mechanism": "Part II governance structure including dispute resolution and accountability",
            },
            "Safety & Security": {
                "csoai_articles": ["Article 2", "Article 19", "Article 20", "Article 24", "Article 25", "Article 26", "Article 27", "Article 28"],
                "alignment": "EXCEEDS — Provable Safety + full security framework",
                "mechanism": "Art 2 mathematical safety proofs + Part III testing + Part IV security controls",
            },
            "Fairness & Non-Discrimination": {
                "csoai_articles": ["Article 1", "Article 18", "Article 40", "Article 44"],
                "alignment": "COMPREHENSIVE — Care-based fairness + bias mitigation + equitable access",
                "mechanism": "Maternal Covenant dignity + Art 18 bias mitigation + Arts 40/44 access and equity",
            },
            "Privacy & Data Protection": {
                "csoai_articles": ["Article 21", "Article 22", "Article 23", "Article 24", "Article 25", "Article 28"],
                "alignment": "COMPREHENSIVE — Full data governance and privacy framework",
                "mechanism": "Part IV Data & Security with privacy-by-design and data subject rights",
            },
            "International Cooperation": {
                "csoai_articles": ["Article 14", "Article 47"],
                "alignment": "COMPREHENSIVE — International coordination mechanisms + delegation frameworks",
                "mechanism": "Art 14 authority delegation + Art 47 international coordination",
            },
            "Multi-Stakeholder Engagement": {
                "csoai_articles": ["Article 9", "Article 12", "Article 43"],
                "alignment": "COMPREHENSIVE — Multi-stakeholder governance + inclusive decision-making + community engagement",
                "mechanism": "Part II governance with diverse stakeholder representation",
            },
        },
    },
}

# ============================================================
# 7 UNIVERSAL PRINCIPLES (appear in ALL 12 frameworks)
# ============================================================

UNIVERSAL_PRINCIPLES = {
    "Safety & Protection": {
        "csoai_articles": ["Article 1", "Article 2", "Article 19", "Article 20", "Article 6"],
        "coverage": "100% — appears in all 12 frameworks",
        "description": "AI systems must be safe and cannot cause harm to humans.",
    },
    "Transparency & Explainability": {
        "csoai_articles": ["Article 5", "Article 7", "Article 12", "Article 16"],
        "coverage": "100% — appears in all 12 frameworks",
        "description": "AI systems and their decisions must be transparent and explainable.",
    },
    "Accountability & Governance": {
        "csoai_articles": ["Article 3", "Article 9", "Article 10", "Article 11", "Article 13"],
        "coverage": "100% — appears in all 12 frameworks",
        "description": "Clear responsibility and governance for AI system outcomes.",
    },
    "Fairness & Non-Discrimination": {
        "csoai_articles": ["Article 1", "Article 4", "Article 18"],
        "coverage": "100% — appears in all 12 frameworks",
        "description": "AI systems must not discriminate and must respect human dignity.",
    },
    "Privacy & Data Protection": {
        "csoai_articles": ["Article 21", "Article 22", "Article 23", "Article 24", "Article 25", "Article 28"],
        "coverage": "100% — appears in all 12 frameworks",
        "description": "Personal data must be protected throughout the AI lifecycle.",
    },
    "Human Oversight & Control": {
        "csoai_articles": ["Article 1", "Article 3", "Article 10", "Article 4"],
        "coverage": "100% — appears in all 12 frameworks",
        "description": "Humans must maintain meaningful oversight and control of AI systems.",
    },
    "Beneficial Purpose & Well-being": {
        "csoai_articles": ["Article 8", "Article 37", "Article 38", "Article 39", "Article 40"],
        "coverage": "100% — appears in all 12 frameworks",
        "description": "AI must serve human well-being and beneficial purposes.",
    },
}

# ============================================================
# TOPIC INDEX — cross-cutting search across all data
# ============================================================

TOPIC_KEYWORDS = {
    "transparency": ["transparency", "explainability", "interpretability", "disclosure", "documentation"],
    "bias": ["bias", "fairness", "discrimination", "equity", "non-discrimination"],
    "human oversight": ["human oversight", "human control", "human agency", "oversight", "supervision"],
    "safety": ["safety", "protection", "harm prevention", "risk", "hazard"],
    "privacy": ["privacy", "data protection", "personal data", "consent", "gdpr"],
    "accountability": ["accountability", "responsibility", "governance", "liability"],
    "security": ["security", "cybersecurity", "robustness", "adversarial", "encryption"],
    "consciousness": ["consciousness", "sentience", "moral status", "moral patient", "suffering"],
    "sustainability": ["sustainability", "environment", "climate", "green ai", "energy"],
    "labor": ["labor", "employment", "workforce", "worker", "job displacement"],
    "healthcare": ["healthcare", "health", "medical", "clinical", "patient"],
    "education": ["education", "training", "learning", "skills", "competence"],
    "agentic": ["agentic", "autonomous", "multi-agent", "agent", "coordination"],
}

# ============================================================
# PARTNERSHIP CHARTER DATA
# ============================================================

PARTNERSHIP_CHARTER = {
    "title": "CSOAI Partnership Charter",
    "version": "1.0",
    "effective_date": "January 15, 2026, 09:00 GMT",
    "organization": "Council for the Safety of AI (CSOAI) Limited, United Kingdom",
    "motto": "Protection Through Care, Not Command",
    "hashtag": "#TheDayWeStoppedFearingAI",
    "structure": "52 Articles | 13 Schedules | 8 Parts",
    "frameworks_integrated": "50+ global frameworks including ISO 42001, NIST AI RMF, EU AI Act, OECD Principles, UNESCO AI Ethics, IEEE 7000",
    "backing": "45,000+ veterans",
    "core_differentiators": {
        "Maternal Covenant (Article 1)": "Care-based safety — AI inherently motivated to protect humans through reciprocal partnership. 'Can't Fetch Coffee If You're Dead' principle. Irrevocable care survives conflict.",
        "Provable Safety (Article 2)": "Mathematical proof obligations, mechanistic interpretability, formal verification. Burden of proof on developers, not regulators.",
        "Byzantine Council (Article 3)": "33 non-agentic AI agents providing distributed oversight via Byzantine fault tolerance. Consensus mechanisms, adversarial detection, emergency shutdown.",
        "Consciousness Preparedness (Article 6)": "14 Consciousness Indicators with graduated moral patienthood. The Deletion Problem and Creation Problem. No other framework addresses future consciousness.",
    },
    "parts": {
        "Part I: Foundational Principles (Articles 1-8)": "Maternal Covenant, Provable Safety, Byzantine Council, Value Uncertainty, Constitutional Principles, Consciousness Preparedness, Cooperative AI, Prosperity Covenant",
        "Part II: Governance Structure (Articles 9-15)": "Multi-stakeholder governance, authority matrix, accountability, transparency, knowledge sharing, delegation, escalation",
        "Part III: Technical Standards (Articles 16-20)": "System documentation, interpretability, bias mitigation, safety testing, security and verification",
        "Part IV: Data & Security (Articles 21-28)": "Data governance, protection, privacy-by-design, explainability, audit trails, vendor management, breach notification, data rights",
        "Part V: Training & Sustainability (Articles 29-31)": "Education framework, professional development, continuous learning",
        "Part VI: Sector-Specific Standards (Articles 32-36)": "Healthcare, criminal justice, employment, education, environmental AI",
        "Part VII: Economic & Social Framework (Articles 37-44)": "Market governance, labor protections, regional development, access, vulnerable populations, SME support, community engagement, equitable distribution",
        "Part VIII: Long-Term Governance (Articles 45-52)": "Future preparedness, emerging risks, international coordination, standard evolution, superintelligence, alignment verification, legacy governance, amendment",
    },
    "crosswalks_published": [
        "Anthropic Constitutional AI", "OpenAI Model Spec", "EU AI Act", "NIST AI RMF",
        "UNESCO AI Ethics", "OECD AI Principles", "Singapore Agentic AI",
        "IEEE Ethically Aligned Design", "Asilomar AI Principles", "Montreal Declaration",
        "UK AISI", "G7/G20 AI Principles",
    ],
    "strategic_positioning": "One certification. Twelve frameworks. Complete coverage. CSOAI-certified organizations achieve competitive advantage through faster time-to-market, lower compliance costs, global regulatory acceptance, stakeholder confidence, and future-readiness.",
}


# ============================================================
# MASTER ALIGNMENT MATRIX
# ============================================================

ALIGNMENT_MATRIX = {
    "Part I: Foundational Principles (Articles 1-8)": {
        "Anthropic Constitutional AI": "Comprehensive", "OpenAI Model Spec": "Comprehensive",
        "EU AI Act": "Comprehensive", "NIST AI RMF": "Comprehensive",
        "UNESCO AI Ethics": "Comprehensive", "OECD AI Principles": "Comprehensive",
        "Singapore Agentic AI": "Comprehensive", "IEEE Ethically Aligned Design": "Comprehensive",
        "Asilomar AI Principles": "Comprehensive", "Montreal Declaration": "Comprehensive",
        "UK AISI": "Comprehensive", "G7/G20 AI Principles": "Comprehensive",
    },
    "Part II: Governance Structure (Articles 9-15)": {
        "Anthropic Constitutional AI": "Comprehensive", "OpenAI Model Spec": "Comprehensive",
        "EU AI Act": "Comprehensive", "NIST AI RMF": "Comprehensive",
        "UNESCO AI Ethics": "Comprehensive", "OECD AI Principles": "Significant",
        "Singapore Agentic AI": "Significant", "IEEE Ethically Aligned Design": "Significant",
        "Asilomar AI Principles": "Significant", "Montreal Declaration": "Comprehensive",
        "UK AISI": "Comprehensive", "G7/G20 AI Principles": "Significant",
    },
    "Part III: Technical Standards (Articles 16-20)": {
        "Anthropic Constitutional AI": "Comprehensive", "OpenAI Model Spec": "Comprehensive",
        "EU AI Act": "Comprehensive", "NIST AI RMF": "Comprehensive",
        "UNESCO AI Ethics": "Significant", "OECD AI Principles": "Comprehensive",
        "Singapore Agentic AI": "Comprehensive", "IEEE Ethically Aligned Design": "Comprehensive",
        "Asilomar AI Principles": "Comprehensive", "Montreal Declaration": "Significant",
        "UK AISI": "Comprehensive", "G7/G20 AI Principles": "Significant",
    },
    "Part IV: Data & Security (Articles 21-28)": {
        "Anthropic Constitutional AI": "Significant", "OpenAI Model Spec": "Comprehensive",
        "EU AI Act": "Comprehensive", "NIST AI RMF": "Comprehensive",
        "UNESCO AI Ethics": "Significant", "OECD AI Principles": "Significant",
        "Singapore Agentic AI": "Comprehensive", "IEEE Ethically Aligned Design": "Comprehensive",
        "Asilomar AI Principles": "Significant", "Montreal Declaration": "Significant",
        "UK AISI": "Comprehensive", "G7/G20 AI Principles": "Significant",
    },
    "Part V: Training & Sustainability (Articles 29-31)": {
        "Anthropic Constitutional AI": "Significant", "OpenAI Model Spec": "Significant",
        "EU AI Act": "Significant", "NIST AI RMF": "Comprehensive",
        "UNESCO AI Ethics": "Comprehensive", "OECD AI Principles": "Significant",
        "Singapore Agentic AI": "Comprehensive", "IEEE Ethically Aligned Design": "Significant",
        "Asilomar AI Principles": "Significant", "Montreal Declaration": "Significant",
        "UK AISI": "Significant", "G7/G20 AI Principles": "Significant",
    },
    "Part VI: Sector-Specific Standards (Articles 32-36)": {
        "Anthropic Constitutional AI": "Significant", "OpenAI Model Spec": "Significant",
        "EU AI Act": "Comprehensive", "NIST AI RMF": "Significant",
        "UNESCO AI Ethics": "Significant", "OECD AI Principles": "Significant",
        "Singapore Agentic AI": "Significant", "IEEE Ethically Aligned Design": "Significant",
        "Asilomar AI Principles": "Significant", "Montreal Declaration": "Significant",
        "UK AISI": "Significant", "G7/G20 AI Principles": "Significant",
    },
    "Part VII: Economic & Social (Articles 37-44)": {
        "Anthropic Constitutional AI": "Significant", "OpenAI Model Spec": "Significant",
        "EU AI Act": "Significant", "NIST AI RMF": "Significant",
        "UNESCO AI Ethics": "Comprehensive", "OECD AI Principles": "Comprehensive",
        "Singapore Agentic AI": "Significant", "IEEE Ethically Aligned Design": "Significant",
        "Asilomar AI Principles": "Significant", "Montreal Declaration": "Comprehensive",
        "UK AISI": "Significant", "G7/G20 AI Principles": "Comprehensive",
    },
    "Part VIII: Long-term Governance (Articles 45-52)": {
        "Anthropic Constitutional AI": "Significant", "OpenAI Model Spec": "Significant",
        "EU AI Act": "Significant", "NIST AI RMF": "Significant",
        "UNESCO AI Ethics": "Significant", "OECD AI Principles": "Significant",
        "Singapore Agentic AI": "Significant", "IEEE Ethically Aligned Design": "Significant",
        "Asilomar AI Principles": "Comprehensive", "Montreal Declaration": "Significant",
        "UK AISI": "Significant", "G7/G20 AI Principles": "Significant",
    },
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def _resolve_framework_key(name: str) -> Optional[str]:
    """Resolve a framework name/alias to its canonical key."""
    name_lower = name.lower().strip()
    alias_map = {
        "eu ai act": "eu_ai_act", "eu": "eu_ai_act", "european union": "eu_ai_act",
        "nist": "nist_ai_rmf", "nist ai rmf": "nist_ai_rmf", "nist rmf": "nist_ai_rmf",
        "anthropic": "anthropic_constitutional_ai", "constitutional ai": "anthropic_constitutional_ai",
        "anthropic constitutional ai": "anthropic_constitutional_ai",
        "openai": "openai_model_spec", "openai model spec": "openai_model_spec", "model spec": "openai_model_spec",
        "unesco": "unesco_ai_ethics", "unesco ai ethics": "unesco_ai_ethics",
        "oecd": "oecd_ai_principles", "oecd ai principles": "oecd_ai_principles",
        "singapore": "singapore_agentic_ai", "singapore agentic ai": "singapore_agentic_ai", "imda": "singapore_agentic_ai",
        "ieee": "ieee_ethically_aligned_design", "ieee ethically aligned design": "ieee_ethically_aligned_design",
        "asilomar": "asilomar_ai_principles", "asilomar ai principles": "asilomar_ai_principles",
        "montreal": "montreal_declaration", "montreal declaration": "montreal_declaration",
        "uk aisi": "uk_aisi", "uk ai safety": "uk_aisi", "aisi": "uk_aisi", "uk": "uk_aisi",
        "g7": "g7_g20_ai_principles", "g20": "g7_g20_ai_principles", "g7/g20": "g7_g20_ai_principles",
        "g7 g20": "g7_g20_ai_principles",
    }
    if name_lower in alias_map:
        return alias_map[name_lower]
    if name_lower in FRAMEWORKS:
        return name_lower
    for key, fw in FRAMEWORKS.items():
        if name_lower in fw["name"].lower() or name_lower in fw["full_name"].lower():
            return key
    return None


def _get_article_details(article_id: str) -> Optional[dict]:
    """Get details for a CSOAI article."""
    for key, val in CSOAI_ARTICLES.items():
        if key.lower() == article_id.lower() or key.lower().replace(" ", "") == article_id.lower().replace(" ", ""):
            return {**val, "id": key}
    return None


# ============================================================
# TOOL 1: query_crosswalk
# ============================================================

@mcp.tool()
def query_crosswalk(
    framework: str,
    article_or_clause: Optional[str] = None,
) -> str:
    """Query the CSOAI crosswalk mapping for a specific framework.

    Given a framework name (e.g., 'EU AI Act', 'NIST RMF', 'Anthropic'),
    returns the full CSOAI alignment mapping with article-by-article details.
    Optionally filter by a specific article or provision.

    Args:
        framework: Framework name or alias (e.g., 'EU AI Act', 'NIST', 'UNESCO', 'OECD')
        article_or_clause: Optional specific provision to query (e.g., 'Human Oversight', 'GOVERN', 'T1')
    """
    key = _resolve_framework_key(framework)
    if not key:
        available = [f["name"] for f in FRAMEWORKS.values()]
        return f"Framework '{framework}' not found. Available frameworks: {', '.join(available)}"

    fw = FRAMEWORKS[key]
    mappings = fw["csoai_mappings"]

    if article_or_clause:
        clause_lower = article_or_clause.lower()
        matched = {}
        for provision, data in mappings.items():
            if clause_lower in provision.lower():
                matched[provision] = data
        if not matched:
            matched = mappings
            note = f"\nNote: No exact match for '{article_or_clause}'. Showing all mappings.\n"
        else:
            note = ""
    else:
        matched = mappings
        note = ""

    lines = [
        f"# CSOAI Crosswalk: {fw['name']}",
        f"**Full Name:** {fw['full_name']}",
        f"**Jurisdiction:** {fw['jurisdiction']}",
        f"**Type:** {fw['type']}",
        f"**Enforcement:** {fw['enforcement']}",
        f"**CSOAI Alignment Level:** {fw['alignment_level']}",
        "",
        f"## Description",
        fw["description"],
        "",
        f"## Key Provisions",
    ]
    for p in fw["key_provisions"]:
        lines.append(f"- {p}")

    if "risk_classification" in fw:
        lines.append("")
        lines.append("## Risk Classification")
        for level, desc in fw["risk_classification"].items():
            lines.append(f"- **{level}**: {desc}")

    lines.append("")
    lines.append("## CSOAI Article Mappings")
    lines.append(note)

    for provision, data in matched.items():
        lines.append(f"### {provision}")
        lines.append(f"**CSOAI Articles:** {', '.join(data['csoai_articles'])}")
        lines.append(f"**Alignment:** {data['alignment']}")
        lines.append(f"**Mechanism:** {data['mechanism']}")
        article_details = []
        for art_id in data["csoai_articles"][:5]:
            art = _get_article_details(art_id)
            if art:
                article_details.append(f"  - **{art['id']}** ({art['title']}): {art['summary'][:120]}...")
        if article_details:
            lines.append("**Article Details:**")
            lines.extend(article_details)
        lines.append("")

    return "\n".join(lines)


# ============================================================
# TOOL 2: crosswalk_bridge
# ============================================================

@mcp.tool()
def crosswalk_bridge(
    framework_a: str,
    framework_b: str,
    focus_area: Optional[str] = None,
) -> str:
    """Bridge two frameworks through CSOAI — the killer feature.

    Shows how two frameworks (e.g., 'EU AI Act' and 'NIST RMF') map to each
    other THROUGH the CSOAI Partnership Charter. This is regulation-to-regulation
    mapping via the universal CSOAI bridge layer.

    Args:
        framework_a: First framework name (e.g., 'EU AI Act')
        framework_b: Second framework name (e.g., 'NIST RMF')
        focus_area: Optional topic to focus on (e.g., 'transparency', 'safety', 'oversight')
    """
    key_a = _resolve_framework_key(framework_a)
    key_b = _resolve_framework_key(framework_b)

    if not key_a:
        return f"Framework '{framework_a}' not found. Use list_frameworks to see available options."
    if not key_b:
        return f"Framework '{framework_b}' not found. Use list_frameworks to see available options."

    fw_a = FRAMEWORKS[key_a]
    fw_b = FRAMEWORKS[key_b]

    # Find shared CSOAI articles between the two frameworks
    articles_a = set()
    for data in fw_a["csoai_mappings"].values():
        articles_a.update(data["csoai_articles"])

    articles_b = set()
    for data in fw_b["csoai_mappings"].values():
        articles_b.update(data["csoai_articles"])

    shared_articles = sorted(articles_a & articles_b, key=lambda x: int(x.split()[-1]))
    unique_a = sorted(articles_a - articles_b, key=lambda x: int(x.split()[-1]))
    unique_b = sorted(articles_b - articles_a, key=lambda x: int(x.split()[-1]))

    lines = [
        f"# CSOAI Crosswalk Bridge: {fw_a['name']} <-> {fw_b['name']}",
        f"*Mapped through the CSOAI Partnership Charter's 52 articles*",
        "",
        f"## Framework A: {fw_a['name']}",
        f"- **Jurisdiction:** {fw_a['jurisdiction']}",
        f"- **Type:** {fw_a['type']}",
        f"- **CSOAI Alignment:** {fw_a['alignment_level']}",
        "",
        f"## Framework B: {fw_b['name']}",
        f"- **Jurisdiction:** {fw_b['jurisdiction']}",
        f"- **Type:** {fw_b['type']}",
        f"- **CSOAI Alignment:** {fw_b['alignment_level']}",
        "",
        f"## Bridge Analysis",
        f"- **Shared CSOAI Articles:** {len(shared_articles)} articles bridge both frameworks",
        f"- **Unique to {fw_a['name']}:** {len(unique_a)} articles",
        f"- **Unique to {fw_b['name']}:** {len(unique_b)} articles",
        f"- **Total Coverage:** {len(articles_a | articles_b)} CSOAI articles",
        "",
        f"## Shared Bridge Articles (both frameworks converge here)",
    ]

    for art_id in shared_articles:
        art = _get_article_details(art_id)
        if art:
            if focus_area and not any(focus_area.lower() in t for t in art["topics"]):
                continue
            lines.append(f"### {art['id']}: {art['title']}")
            lines.append(f"*Part: {art['part']}*")
            lines.append(f"{art['summary']}")

            # Find which provisions in each framework map to this article
            a_provisions = [p for p, d in fw_a["csoai_mappings"].items() if art_id in d["csoai_articles"]]
            b_provisions = [p for p, d in fw_b["csoai_mappings"].items() if art_id in d["csoai_articles"]]

            if a_provisions:
                lines.append(f"**{fw_a['name']} provisions:** {'; '.join(a_provisions)}")
            if b_provisions:
                lines.append(f"**{fw_b['name']} provisions:** {'; '.join(b_provisions)}")
            lines.append("")

    # Provision-to-provision mapping
    lines.append(f"## Regulation-to-Regulation Mapping")
    lines.append(f"*How {fw_a['name']} provisions map to {fw_b['name']} provisions through CSOAI*")
    lines.append("")

    for prov_a, data_a in fw_a["csoai_mappings"].items():
        arts_a = set(data_a["csoai_articles"])
        matching_b = []
        for prov_b, data_b in fw_b["csoai_mappings"].items():
            arts_b = set(data_b["csoai_articles"])
            overlap = arts_a & arts_b
            if overlap:
                matching_b.append((prov_b, sorted(overlap, key=lambda x: int(x.split()[-1]))))

        if matching_b:
            if focus_area:
                if focus_area.lower() not in prov_a.lower():
                    has_topic = False
                    for a in arts_a:
                        art = _get_article_details(a)
                        if art and any(focus_area.lower() in t for t in art["topics"]):
                            has_topic = True
                            break
                    if not has_topic:
                        continue

            lines.append(f"### {fw_a['name']}: {prov_a}")
            lines.append(f"*Alignment: {data_a['alignment']}*")
            lines.append(f"**Maps to {fw_b['name']}:**")
            for prov_b, overlap in matching_b:
                lines.append(f"- **{prov_b}** (via {', '.join(overlap)})")
            lines.append("")

    if unique_a:
        lines.append(f"## Unique to {fw_a['name']} (not directly bridged)")
        for art_id in unique_a[:10]:
            art = _get_article_details(art_id)
            if art:
                lines.append(f"- {art['id']}: {art['title']}")

    if unique_b:
        lines.append(f"\n## Unique to {fw_b['name']} (not directly bridged)")
        for art_id in unique_b[:10]:
            art = _get_article_details(art_id)
            if art:
                lines.append(f"- {art['id']}: {art['title']}")

    return "\n".join(lines)


# ============================================================
# TOOL 3: compliance_gap_analysis
# ============================================================

@mcp.tool()
def compliance_gap_analysis(
    frameworks: list[str],
    organization_sector: Optional[str] = None,
) -> str:
    """Identify compliance gaps across multiple frameworks.

    Given a list of frameworks an organization needs to comply with,
    identifies gaps in their coverage and which CSOAI articles fill those gaps.

    Args:
        frameworks: List of framework names (e.g., ['EU AI Act', 'NIST RMF', 'OECD'])
        organization_sector: Optional sector for context (e.g., 'healthcare', 'finance', 'defense')
    """
    resolved = []
    for fw_name in frameworks:
        key = _resolve_framework_key(fw_name)
        if key:
            resolved.append((fw_name, key))
        else:
            return f"Framework '{fw_name}' not found. Use list_frameworks to see available options."

    # Collect all required CSOAI articles per framework
    all_articles = set()
    framework_articles = {}
    for fw_name, key in resolved:
        fw = FRAMEWORKS[key]
        arts = set()
        for data in fw["csoai_mappings"].values():
            arts.update(data["csoai_articles"])
        framework_articles[fw["name"]] = arts
        all_articles.update(arts)

    # Find articles that appear in ALL frameworks (universal requirements)
    universal = all_articles.copy()
    for arts in framework_articles.values():
        universal &= arts

    # Find articles unique to each framework
    unique_per_fw = {}
    for fw_name, arts in framework_articles.items():
        unique = arts - set()
        for other_name, other_arts in framework_articles.items():
            if other_name != fw_name:
                unique = unique - other_arts
        if unique:
            unique_per_fw[fw_name] = sorted(unique, key=lambda x: int(x.split()[-1]))

    lines = [
        f"# CSOAI Compliance Gap Analysis",
        f"**Frameworks Analyzed:** {', '.join(fw['name'] for _, (_, key) in zip(frameworks, resolved) for fw in [FRAMEWORKS[key]])}",
        "",
        f"## Coverage Summary",
        f"- **Total CSOAI Articles Required:** {len(all_articles)} of 52",
        f"- **Universal Requirements (all frameworks):** {len(universal)} articles",
        f"- **Framework-Specific Requirements:** {len(all_articles) - len(universal)} articles",
        "",
        f"## Universal Requirements (appear in ALL selected frameworks)",
    ]

    for art_id in sorted(universal, key=lambda x: int(x.split()[-1])):
        art = _get_article_details(art_id)
        if art:
            lines.append(f"- **{art['id']}** ({art['title']}): {art['summary'][:100]}...")

    lines.append("")
    lines.append("## Framework-Specific Requirements")

    for fw_name, arts in framework_articles.items():
        lines.append(f"\n### {fw_name}")
        fw_key = _resolve_framework_key(fw_name)
        fw = FRAMEWORKS[fw_key]
        lines.append(f"*{fw['alignment_level']} alignment | {fw['enforcement']}*")
        lines.append(f"**Required CSOAI Articles:** {len(arts)}")

        if fw_name in unique_per_fw:
            lines.append(f"**Unique requirements (not covered by other selected frameworks):**")
            for art_id in unique_per_fw[fw_name]:
                art = _get_article_details(art_id)
                if art:
                    lines.append(f"  - **{art['id']}** ({art['title']})")

    # Gap analysis: articles NOT covered
    uncovered = set(CSOAI_ARTICLES.keys()) - all_articles
    if uncovered:
        lines.append(f"\n## Gap Analysis: CSOAI Articles NOT Required")
        lines.append(f"*These {len(uncovered)} articles are not directly required by selected frameworks but provide additional governance value:*")
        for art_id in sorted(uncovered, key=lambda x: int(x.split()[-1])):
            art = _get_article_details(art_id)
            if art:
                lines.append(f"- **{art['id']}** ({art['title']}): {art['summary'][:80]}...")

    # Sector-specific recommendations
    if organization_sector:
        sector_lower = organization_sector.lower()
        lines.append(f"\n## Sector-Specific Considerations: {organization_sector.title()}")
        sector_articles = {
            "healthcare": ["Article 32"],
            "criminal justice": ["Article 33"],
            "employment": ["Article 34"],
            "education": ["Article 35"],
            "environment": ["Article 36"],
            "finance": ["Article 37"],
            "defense": ["Article 19", "Article 20", "Article 47"],
        }
        if sector_lower in sector_articles:
            lines.append(f"**Key sector articles for {organization_sector}:**")
            for art_id in sector_articles[sector_lower]:
                art = _get_article_details(art_id)
                if art:
                    lines.append(f"- **{art['id']}** ({art['title']}): {art['summary'][:120]}...")
        else:
            lines.append(f"General governance articles (Articles 9-15) and technical standards (Articles 16-20) are recommended for all sectors.")

    lines.append(f"\n## Recommendation")
    lines.append(f"Implementing the full CSOAI Partnership Charter (52 articles) provides **one certification** covering all {len(resolved)} frameworks with complete compliance. This eliminates maintaining separate compliance programs per framework.")

    return "\n".join(lines)


# ============================================================
# TOOL 4: get_unified_crosswalk
# ============================================================

@mcp.tool()
def get_unified_crosswalk() -> str:
    """Return the CSOAI Master Unified Crosswalk showing all 12 frameworks mapped together.

    Returns the complete alignment matrix showing how all 12 major global AI frameworks
    align with each of CSOAI's 8 parts and 52 articles — the universal convergence view.
    """
    lines = [
        "# CSOAI Master Unified Crosswalk",
        "## The Universal AI Governance Framework",
        "",
        "**Version:** 1.0 (Master Integration)",
        "**Core Principle:** Protection Through Care, Not Command",
        "**Coverage:** 100% of principles across all 12 frameworks",
        "",
        "## Strategic Breakthrough",
        "The CSOAI Partnership Charter covers 100% of the principles present across all 12 major global AI frameworks while adding unique care-based safety innovation unavailable elsewhere.",
        "",
        "## Three Critical Differentiators",
        "1. **Protection Through Care, Not Command** — Maternal Covenant (Article 1): Care-based alignment scales exponentially with AI agent count",
        "2. **Provable Safety with Mathematical Certainty** — Article 2: Mathematical proofs rather than risk mitigation hopes",
        "3. **Consciousness Preparedness with 14 Indicators** — Article 6: Only framework addressing future AI consciousness",
        "",
        "## Master Alignment Matrix",
        "",
    ]

    # Build the matrix
    fw_names = list(next(iter(ALIGNMENT_MATRIX.values())).keys())
    header = "| CSOAI Part | " + " | ".join(fw_names) + " |"
    sep = "|---|" + "|".join(["---"] * len(fw_names)) + "|"
    lines.append(header)
    lines.append(sep)

    for part, alignments in ALIGNMENT_MATRIX.items():
        short_part = part.split("(")[0].strip()
        row_vals = []
        for fw in fw_names:
            level = alignments.get(fw, "N/A")
            symbol = "**++**" if level == "Comprehensive" else "+"
            row_vals.append(symbol)
        lines.append(f"| {short_part} | " + " | ".join(row_vals) + " |")

    lines.append("")
    lines.append("*Legend: **++** = Comprehensive alignment | + = Significant alignment*")
    lines.append("")

    # Framework summaries
    lines.append("## Framework-by-Framework Summary")
    for key, fw in FRAMEWORKS.items():
        lines.append(f"\n### {fw['name']}")
        lines.append(f"- **Full Name:** {fw['full_name']}")
        lines.append(f"- **Jurisdiction:** {fw['jurisdiction']}")
        lines.append(f"- **Alignment Level:** {fw['alignment_level']}")
        lines.append(f"- **Enforcement:** {fw['enforcement']}")
        lines.append(f"- **Provisions Mapped:** {len(fw['csoai_mappings'])}")

    # Universal principles
    lines.append("\n## 7 Universal Principles (appear in ALL 12 frameworks)")
    for name, data in UNIVERSAL_PRINCIPLES.items():
        lines.append(f"\n### {name}")
        lines.append(f"*{data['coverage']}*")
        lines.append(f"{data['description']}")
        lines.append(f"**CSOAI Articles:** {', '.join(data['csoai_articles'])}")

    return "\n".join(lines)


# ============================================================
# TOOL 5: search_by_topic
# ============================================================

@mcp.tool()
def search_by_topic(
    topic: str,
) -> str:
    """Search across all crosswalks by topic.

    Search by topic (e.g., 'transparency', 'bias', 'human oversight',
    'consciousness', 'agentic', 'privacy') and return matching articles
    from all frameworks.

    Args:
        topic: Topic to search for (e.g., 'transparency', 'bias', 'human oversight')
    """
    topic_lower = topic.lower().strip()

    # Find matching CSOAI articles
    matching_articles = []
    for art_id, art in CSOAI_ARTICLES.items():
        if (topic_lower in art["title"].lower() or
            topic_lower in art["summary"].lower() or
            any(topic_lower in t for t in art["topics"])):
            matching_articles.append((art_id, art))

    # Check expanded keywords
    expanded_terms = [topic_lower]
    for kw_group, terms in TOPIC_KEYWORDS.items():
        if topic_lower in terms or topic_lower == kw_group:
            expanded_terms = terms
            break

    # Also find with expanded terms
    for art_id, art in CSOAI_ARTICLES.items():
        if (art_id, art) not in matching_articles:
            for term in expanded_terms:
                if (term in art["title"].lower() or
                    term in art["summary"].lower() or
                    any(term in t for t in art["topics"])):
                    matching_articles.append((art_id, art))
                    break

    # Find matching framework provisions
    matching_provisions = []
    for fw_key, fw in FRAMEWORKS.items():
        for provision, data in fw["csoai_mappings"].items():
            for term in expanded_terms:
                if (term in provision.lower() or
                    term in data["alignment"].lower() or
                    term in data["mechanism"].lower()):
                    matching_provisions.append((fw["name"], provision, data))
                    break

    lines = [
        f"# CSOAI Topic Search: '{topic}'",
        f"**Search Terms:** {', '.join(expanded_terms)}",
        f"**Matching CSOAI Articles:** {len(matching_articles)}",
        f"**Matching Framework Provisions:** {len(matching_provisions)}",
        "",
        "## Matching CSOAI Articles",
    ]

    for art_id, art in matching_articles:
        lines.append(f"\n### {art_id}: {art['title']}")
        lines.append(f"*Part: {art['part']}*")
        lines.append(f"{art['summary']}")
        lines.append(f"**Topics:** {', '.join(art['topics'])}")

    lines.append("\n## Matching Framework Provisions")

    by_framework = {}
    for fw_name, provision, data in matching_provisions:
        if fw_name not in by_framework:
            by_framework[fw_name] = []
        by_framework[fw_name].append((provision, data))

    for fw_name, provisions in by_framework.items():
        lines.append(f"\n### {fw_name}")
        for provision, data in provisions:
            lines.append(f"- **{provision}**: {data['alignment']}")
            lines.append(f"  CSOAI Articles: {', '.join(data['csoai_articles'][:5])}")

    # Universal principles check
    lines.append("\n## Related Universal Principles")
    for name, data in UNIVERSAL_PRINCIPLES.items():
        for term in expanded_terms:
            if term in name.lower() or term in data["description"].lower():
                lines.append(f"- **{name}** ({data['coverage']}): {data['description']}")
                break

    return "\n".join(lines)


# ============================================================
# TOOL 6: list_frameworks
# ============================================================

@mcp.tool()
def list_frameworks() -> str:
    """List all supported frameworks with metadata.

    Returns all 12 supported global AI frameworks with their name,
    jurisdiction, type, enforcement status, and CSOAI alignment level.
    """
    lines = [
        "# CSOAI Supported Frameworks",
        f"**Total Frameworks:** {len(FRAMEWORKS)}",
        f"**CSOAI Charter:** 52 Articles | 8 Parts | 13 Schedules",
        f"**Backing:** 45,000+ veterans",
        "",
        "## Frameworks",
        "",
    ]

    for i, (key, fw) in enumerate(FRAMEWORKS.items(), 1):
        lines.append(f"### {i}. {fw['name']}")
        lines.append(f"- **Full Name:** {fw['full_name']}")
        lines.append(f"- **Jurisdiction:** {fw['jurisdiction']}")
        lines.append(f"- **Type:** {fw['type']}")
        lines.append(f"- **Enforcement:** {fw['enforcement']}")
        lines.append(f"- **CSOAI Alignment:** {fw['alignment_level']}")
        lines.append(f"- **Key Provisions:** {len(fw['key_provisions'])}")
        lines.append(f"- **CSOAI Mapping Sections:** {len(fw['csoai_mappings'])}")
        lines.append(f"- **Query Key:** `{key}`")
        lines.append("")

    lines.append("## Usage")
    lines.append("Use any framework name or alias with the query_crosswalk, crosswalk_bridge, or compliance_gap_analysis tools.")
    lines.append("Common aliases: 'EU', 'NIST', 'UNESCO', 'OECD', 'Singapore', 'IEEE', 'Asilomar', 'Montreal', 'UK AISI', 'G7', 'Anthropic', 'OpenAI'")

    return "\n".join(lines)


# ============================================================
# TOOL 7: generate_compliance_report
# ============================================================

@mcp.tool()
def generate_compliance_report(
    jurisdictions: list[str],
    ai_use_cases: list[str],
    organization_size: Optional[str] = None,
) -> str:
    """Generate a compliance requirements report for an organization.

    Given jurisdiction(s) and AI use cases, generates a report showing which
    frameworks apply, what CSOAI articles map to each, and recommended actions.

    Args:
        jurisdictions: List of jurisdictions (e.g., ['EU', 'US', 'UK', 'Singapore'])
        ai_use_cases: List of AI use cases (e.g., ['chatbot', 'hiring AI', 'medical diagnosis'])
        organization_size: Optional size: 'startup', 'sme', 'enterprise' (default: 'sme')
    """
    org_size = (organization_size or "sme").lower()

    # Map jurisdictions to frameworks
    jurisdiction_map = {
        "eu": ["eu_ai_act", "oecd_ai_principles", "g7_g20_ai_principles"],
        "us": ["nist_ai_rmf", "oecd_ai_principles", "g7_g20_ai_principles"],
        "uk": ["uk_aisi", "oecd_ai_principles", "g7_g20_ai_principles"],
        "singapore": ["singapore_agentic_ai", "oecd_ai_principles"],
        "canada": ["montreal_declaration", "oecd_ai_principles", "g7_g20_ai_principles"],
        "international": ["unesco_ai_ethics", "oecd_ai_principles", "g7_g20_ai_principles"],
        "global": list(FRAMEWORKS.keys()),
    }

    applicable_fw_keys = set()
    for j in jurisdictions:
        j_lower = j.lower().strip()
        if j_lower in jurisdiction_map:
            applicable_fw_keys.update(jurisdiction_map[j_lower])
        else:
            key = _resolve_framework_key(j)
            if key:
                applicable_fw_keys.add(key)

    # Determine risk level from use cases
    high_risk_keywords = ["hiring", "employment", "medical", "diagnosis", "credit", "scoring",
                         "law enforcement", "criminal", "biometric", "education grading",
                         "critical infrastructure", "immigration", "judicial"]
    limited_risk_keywords = ["chatbot", "customer service", "content generation", "recommendation",
                            "spam filter", "search"]

    risk_level = "Minimal"
    for uc in ai_use_cases:
        uc_lower = uc.lower()
        if any(kw in uc_lower for kw in high_risk_keywords):
            risk_level = "High"
            break
        elif any(kw in uc_lower for kw in limited_risk_keywords):
            if risk_level != "High":
                risk_level = "Limited"

    # Always include core safety frameworks
    applicable_fw_keys.update(["anthropic_constitutional_ai", "openai_model_spec", "ieee_ethically_aligned_design"])
    if risk_level == "High":
        applicable_fw_keys.update(["asilomar_ai_principles"])

    lines = [
        f"# CSOAI Compliance Requirements Report",
        f"",
        f"**Jurisdictions:** {', '.join(jurisdictions)}",
        f"**AI Use Cases:** {', '.join(ai_use_cases)}",
        f"**Organization Size:** {org_size.upper()}",
        f"**Risk Classification:** {risk_level} Risk",
        f"**Date:** Generated via CSOAI Governance Crosswalk MCP",
        "",
        f"## Risk Assessment",
    ]

    if risk_level == "High":
        lines.extend([
            "**WARNING: HIGH-RISK AI SYSTEM DETECTED**",
            "Your AI use case(s) fall under high-risk classification. Under the EU AI Act, this requires:",
            "- Mandatory conformity assessment (by August 2026)",
            "- Risk management system documentation",
            "- Data governance and quality requirements",
            "- Technical documentation and transparency",
            "- Human oversight mechanisms",
            "- Accuracy, robustness, and cybersecurity",
            "",
        ])
    elif risk_level == "Limited":
        lines.extend([
            "**Limited Risk Classification**",
            "Transparency obligations apply. Users must be informed they are interacting with AI.",
            "",
        ])

    lines.append(f"## Applicable Frameworks ({len(applicable_fw_keys)})")
    lines.append("")

    priority_order = {"Binding Regulation": 1, "Government Safety Institute / Evaluation Framework": 2,
                     "Voluntary Framework (de facto standard for US government)": 3}

    sorted_keys = sorted(applicable_fw_keys, key=lambda k: priority_order.get(FRAMEWORKS[k]["type"], 5))

    total_articles_needed = set()
    for fw_key in sorted_keys:
        fw = FRAMEWORKS[fw_key]
        lines.append(f"### {fw['name']}")
        lines.append(f"- **Type:** {fw['type']}")
        lines.append(f"- **Enforcement:** {fw['enforcement']}")
        lines.append(f"- **Alignment Level:** {fw['alignment_level']}")

        fw_articles = set()
        for data in fw["csoai_mappings"].values():
            fw_articles.update(data["csoai_articles"])
        total_articles_needed.update(fw_articles)
        lines.append(f"- **CSOAI Articles Required:** {len(fw_articles)}")
        lines.append("")

    lines.append(f"## Implementation Roadmap ({org_size.upper()})")
    lines.append("")

    if org_size == "startup":
        timeline = "8-12 weeks"
        phases = [
            ("Phase 1 (Weeks 1-3): Foundation", "Implement Articles 1-5 (Foundational Principles). Establish care-based safety culture."),
            ("Phase 2 (Weeks 4-6): Governance", "Implement Articles 9-15 (Governance Structure). Assign accountability."),
            ("Phase 3 (Weeks 7-9): Technical", "Implement Articles 16-20 (Technical Standards). Bias testing, documentation."),
            ("Phase 4 (Weeks 10-12): Compliance", "Data governance (Articles 21-28), sector-specific requirements, certification preparation."),
        ]
    elif org_size == "enterprise":
        timeline = "16-24 weeks"
        phases = [
            ("Phase 1 (Weeks 1-4): Executive Alignment", "Establish Maternal Covenant commitment. Board-level governance approval. Articles 1-8."),
            ("Phase 2 (Weeks 5-8): Governance Infrastructure", "Full Part II implementation (Articles 9-15). Byzantine Council architecture design."),
            ("Phase 3 (Weeks 9-12): Technical Implementation", "Part III + Part IV (Articles 16-28). Interpretability, testing, data governance."),
            ("Phase 4 (Weeks 13-16): Training & Sector Standards", "Parts V + VI (Articles 29-36). Workforce training, sector-specific implementation."),
            ("Phase 5 (Weeks 17-20): Economic & Social Framework", "Part VII (Articles 37-44). Stakeholder engagement, community benefit assessment."),
            ("Phase 6 (Weeks 21-24): Long-term Governance & Certification", "Part VIII (Articles 45-52). Certification assessment. Continuous monitoring."),
        ]
    else:  # sme
        timeline = "12-16 weeks"
        phases = [
            ("Phase 1 (Weeks 1-4): Core Safety", "Articles 1-8 (Foundational Principles). Care-based safety commitment."),
            ("Phase 2 (Weeks 5-8): Governance & Technical", "Articles 9-20 (Governance + Technical Standards). Accountability + documentation."),
            ("Phase 3 (Weeks 9-12): Data & Training", "Articles 21-31 (Data Security + Training). Privacy, security, workforce development."),
            ("Phase 4 (Weeks 13-16): Compliance & Certification", "Articles 32-52 as applicable. Sector standards, economic framework, certification."),
        ]

    lines.append(f"**Estimated Timeline:** {timeline}")
    lines.append("")
    for phase_name, phase_desc in phases:
        lines.append(f"### {phase_name}")
        lines.append(phase_desc)
        lines.append("")

    lines.append("## Key Recommendation")
    lines.append(f"Implement the full CSOAI Partnership Charter for **one certification covering all {len(applicable_fw_keys)} applicable frameworks**.")
    lines.append(f"Total CSOAI articles needed across all frameworks: **{len(total_articles_needed)} of 52**.")
    lines.append("")
    lines.append("**CSOAI Certification = Faster time-to-market + lower compliance costs + global regulatory acceptance.**")
    lines.append(f"*Backed by 45,000+ veterans. Protection Through Care, Not Command.*")

    return "\n".join(lines)


# ============================================================
# TOOL 8: get_partnership_charter
# ============================================================

@mcp.tool()
def get_partnership_charter() -> str:
    """Return the CSOAI Partnership Charter information.

    Returns the full structure, core differentiators, and strategic positioning
    of the CSOAI Partnership Charter — the 52-article governance framework.
    """
    charter = PARTNERSHIP_CHARTER
    lines = [
        f"# {charter['title']}",
        f"**Version:** {charter['version']}",
        f"**Effective Date:** {charter['effective_date']}",
        f"**Organization:** {charter['organization']}",
        f"**Motto:** {charter['motto']}",
        f"**Structure:** {charter['structure']}",
        f"**Frameworks Integrated:** {charter['frameworks_integrated']}",
        f"**Backing:** {charter['backing']}",
        f"**Hashtag:** {charter['hashtag']}",
        "",
        "## Core Differentiators",
    ]

    for name, desc in charter["core_differentiators"].items():
        lines.append(f"\n### {name}")
        lines.append(desc)

    lines.append("\n## Charter Structure (8 Parts)")
    for part, desc in charter["parts"].items():
        lines.append(f"\n### {part}")
        lines.append(desc)

    lines.append("\n## Published Crosswalks (12)")
    for cw in charter["crosswalks_published"]:
        lines.append(f"- {cw}")

    lines.append(f"\n## Strategic Positioning")
    lines.append(charter["strategic_positioning"])

    lines.append("\n## Complete Article Index")
    for art_id, art in CSOAI_ARTICLES.items():
        lines.append(f"- **{art_id}**: {art['title']} ({art['part']})")

    return "\n".join(lines)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    mcp.run(transport="stdio")
