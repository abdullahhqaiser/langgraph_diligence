REAL_ESTATE_STAGES = [
    {
        "name": "Stage 0 — Teaser & Reality Check",
        "objective": "Does this asset exist in reality and could it be interesting?",
        "checklist": [
            "Identify asset type, age, and current use",
            "Assess location and micro-location quality",
            "Verify current use versus zoning claim",
            "Evaluate reported NOI versus rent roll logic",
            "Sanity-check asking price against headline yield",
        ],
        "kill_criteria": [
            "Headline yield does not reconcile with stated numbers",
            "Location is off-strategy or unacceptable",
            "Asset condition is unclear or undisclosed",
        ],
        "max_words": 300,
    },
    {
        "name": "Stage 1 — Commercial Plausibility",
        "objective": "If the numbers are wrong, how wrong are they?",
        "checklist": [
            "Assess rent roll coherence — are tenants, rents, and terms believable?",
            "Compare vacancy rate against market norms for this asset class",
            "Benchmark operating costs against comparable assets",
            "Identify tenant concentration risk",
            "Evaluate capex narrative plausibility",
        ],
        "kill_criteria": [
            "Conservative yield falls below investment hurdle rate",
            "Single-tenant dependency with no mitigation strategy",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 2 — Value-Add & Refurbishment Logic",
        "objective": "Is the value-add thesis real or cosmetic?",
        "checklist": [
            "Clarify capex purpose: maintenance vs. repositioning vs. change of use",
            "Assess rent upside realism versus current market evidence",
            "Evaluate re-letting risk and void assumptions",
            "Assess phasing and income downtime during works",
            "Stress test: does the deal work if capex runs 20% over?",
        ],
        "kill_criteria": [
            "Upside depends entirely on heroic rent assumptions without evidence",
            "Capex appears materially underestimated for scope of works",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 3 — Cash Flow & Downside Stress",
        "objective": "Can this deal survive bad luck?",
        "checklist": [
            "Stress NOI by 10% revenue decline",
            "Apply 15% capex overrun scenario",
            "Test exit yield expansion of 50–75bps",
            "Assess financing sensitivity (rate increase, LTV covenant)",
            "Calculate break-even occupancy and exit yield",
        ],
        "kill_criteria": [
            "Equity is materially impaired under a mild stress scenario",
            "No downside protection from deal structure or asset quality",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 4 — Pre-Exclusivity Risk Mapping",
        "objective": "Are the remaining risks verifiable or structural?",
        "checklist": [
            "Flag technical red flags from available documents",
            "Identify lease structure risks (break options, change-of-control clauses)",
            "Assess planning or regulatory exposure",
            "Identify ESG showstoppers (contamination, flood, energy rating)",
            "Categorize all risks: verifiable vs. structural",
        ],
        "kill_criteria": [
            "Structural risks identified that cannot be mitigated through DD",
        ],
        "max_words": 450,
    },
    {
        "name": "Stage 5 — Post-Exclusivity Deep DD",
        "objective": "Full IC-ready analysis",
        "checklist": [
            "Synthesize all prior stage findings into a complete investment thesis",
            "Cross-check financial model assumptions against dataroom evidence",
            "Rank top 5 material risks with probability and severity scores",
            "Identify advisor briefing priorities (legal, technical, tax)",
            "Draft IC recommendation: Acquire / Conditional / Pass",
        ],
        "kill_criteria": [],
        "max_words": 800,
    },
]
