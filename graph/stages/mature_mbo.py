MATURE_MBO_STAGES = [
    {
        "name": "Stage 0 — Teaser & Investment Logic Check",
        "objective": "Why does this business exist as a credible LBO/MBO candidate?",
        "checklist": [
            "Identify and summarize the core business model clearly",
            "Assess revenue sources and predictability",
            "Evaluate headline EBITDA quality and believability",
            "Determine market position and competitive dynamics",
            "Assess ownership motivation — why is management or seller exiting?",
        ],
        "kill_criteria": [
            "EBITDA is unclear, inconsistent, or materially overstated",
            "No credible value-creation angle for a PE buyer",
        ],
        "max_words": 350,
    },
    {
        "name": "Stage 1 — Leverage & Returns Feasibility",
        "objective": "Does leverage work without heroic assumptions?",
        "checklist": [
            "Normalize EBITDA at a headline level (identify obvious one-offs)",
            "Estimate debt capacity using market norms (leverage multiples)",
            "Sanity-check entry multiple against comp transactions",
            "Build base-case IRR logic at stated price",
            "Assess whether returns require aggressive leverage or multiples",
        ],
        "kill_criteria": [
            "Returns only viable with aggressive leverage beyond market norms",
            "Entry multiple unjustifiable versus comparable transactions",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 2 — Cash Flow Quality & Downside",
        "objective": "Can this business service debt reliably under stress?",
        "checklist": [
            "Assess EBITDA to free cash flow conversion quality",
            "Evaluate working capital stability and seasonality",
            "Identify capex requirements vs. maintenance and growth",
            "Flag cyclicality exposure and historical EBITDA volatility",
            "Stress test: what happens to DSCR if EBITDA drops 20%?",
        ],
        "kill_criteria": [
            "Weak EBITDA-to-cash conversion undermines debt serviceability",
            "Significant cyclicality with no structural buffer identified",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 3 — Business & Market Durability",
        "objective": "Will this business still be relevant and growing in 5 years?",
        "checklist": [
            "Assess market growth rate (growing, stable, or declining?)",
            "Evaluate customer concentration risk",
            "Identify switching costs and customer stickiness",
            "Assess competitive moat: pricing power, scale, brand, IP",
            "Flag any structural threats: disruption, regulation, substitution",
        ],
        "kill_criteria": [
            "Business operates in a structurally declining market",
            "Customer concentration is fatal (e.g., 1 customer >50% revenue)",
        ],
        "max_words": 450,
    },
    {
        "name": "Stage 4 — Value Creation Levers",
        "objective": "Where does the PE upside actually come from?",
        "checklist": [
            "Identify pricing power opportunities",
            "Assess cost reduction levers (SG&A, procurement, headcount)",
            "Evaluate operational improvement potential",
            "Assess M&A / bolt-on / roll-up potential",
            "Rate each lever: credible vs. speculative",
        ],
        "kill_criteria": [
            "No controllable levers beyond multiple expansion",
            "All upside scenarios require market-level tailwinds only",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 5 — Management & MBO Readiness",
        "objective": "Can and should management run this as an MBO?",
        "checklist": [
            "Review management team track record in similar situations",
            "Assess depth and breadth of leadership bench",
            "Evaluate management equity roll-over and incentive alignment",
            "Flag key-man dependencies",
            "Assess MBO financing plan and personal commitment level",
        ],
        "kill_criteria": [
            "Management lacks track record to execute independently",
            "Misaligned incentives or insufficient skin in the game",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 6 — Pre-Exclusivity Risk Mapping",
        "objective": "Are remaining risks verifiable (informational) or structural (fatal)?",
        "checklist": [
            "Identify legal or regulatory exposure at headline level",
            "Assess IT and systems maturity for standalone operation",
            "Flag ESG showstoppers or regulatory concerns",
            "Evaluate accounting complexity or quality-of-earnings risk",
            "Categorize each risk: verifiable vs. structural",
        ],
        "kill_criteria": [
            "Structural risks identified that no amount of DD can resolve",
        ],
        "max_words": 450,
    },
    {
        "name": "Stage 7 — Post-Exclusivity Deep DD",
        "objective": "Full IC-ready synthesis",
        "checklist": [
            "Synthesize all prior stage findings into a complete investment thesis",
            "Identify top 5 deal risks with severity and mitigation",
            "Model base / downside / upside cases with explicit assumptions",
            "Assess deal structure and entry valuation fairness",
            "Draft IC recommendation: Invest / Conditional / Pass",
        ],
        "kill_criteria": [],
        "max_words": 800,
    },
]
