BIOTECH_STAGES = [
    {
        "name": "Stage 0 — Teaser & Reality Check",
        "objective": "Does this company solve a real problem in a plausible way?",
        "checklist": [
            "Identify the unmet medical need with specifics",
            "Assess target indication size (patient population)",
            "Summarize competitive landscape at headline level",
            "Evaluate claimed differentiation vs current standard of care",
            "State current development stage and key data readouts",
        ],
        "kill_criteria": [
            "No clear unmet medical need identified",
            "Platform technology with no focused indication",
            "Science buzzwords without biological clarity",
        ],
        "max_words": 350,
    },
    {
        "name": "Stage 1 — Biology & Mechanism Plausibility",
        "objective": "Does the biology make sense at a high level?",
        "checklist": [
            "Assess target biology relevance to the indicated disease",
            "Evaluate mechanism of action (MoA) logic and rationale",
            "Identify disease causality link (target drives disease?)",
            "Find prior validation evidence — literature, approved drugs, failed attempts",
        ],
        "kill_criteria": [
            "No biological precedent supporting the mechanism",
            "Weak or absent causal link between target and disease",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 2 — Pipeline & Development Realism",
        "objective": "Is the development plan realistic?",
        "checklist": [
            "Determine current clinical phase (pre-clinical / Ph I / Ph II / Ph III)",
            "Identify key upcoming inflection points and data readouts",
            "Evaluate clinical trial design clarity and patient selection",
            "Assess timelines versus industry phase norms",
            "Flag any binary risk events (pivotal readouts, regulatory submissions)",
        ],
        "kill_criteria": [
            "Timelines are significantly more optimistic than industry norms",
            "No clear value inflection point defined in the near term",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 3 — Commercial Logic",
        "objective": "Even if it works, is it commercially valuable?",
        "checklist": [
            "Estimate realistic addressable patient population",
            "Evaluate pricing logic and comparable drug pricing",
            "Assess reimbursement pathway plausibility (FDA/EMA, payer dynamics)",
            "Identify competitive displacement logic vs existing therapies",
            "Estimate peak sales potential range",
        ],
        "kill_criteria": [
            "Addressable market too small to justify development costs",
            "Reimbursement pathway implausible given clinical profile",
        ],
        "max_words": 450,
    },
    {
        "name": "Stage 4 — IP & Regulatory Pre-Screen",
        "objective": "Are there fatal legal or regulatory structural risks?",
        "checklist": [
            "Assess patent family scope — composition, method of use, formulation",
            "Evaluate patent expiry horizon relative to expected launch date",
            "Review any freedom-to-operate claims or blocking IP mentioned",
            "Assess regulatory path clarity: orphan designation, fast track, breakthrough?",
            "Identify any prior clinical holds or regulatory concerns flagged",
        ],
        "kill_criteria": [
            "Core IP is weak, narrow, or expiring before product launch",
            "Regulatory path is fundamentally unclear or blocked",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 5 — Team & Execution Capability",
        "objective": "Can this team actually execute a drug development program?",
        "checklist": [
            "Review founders / management prior drug approval track records",
            "Assess clinical development and regulatory affairs experience",
            "Evaluate CEO and CSO credibility and domain expertise",
            "Assess board / advisors composition and scientific relevance",
            "Identify key-man risks or critical hires needed",
        ],
        "kill_criteria": [
            "No prior drug development or approval experience in the team",
            "Science-only team with no operational or commercial leadership",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 6 — Financial & Funding Logic",
        "objective": "Will this company survive to the next value inflection point?",
        "checklist": [
            "Assess current cash position and projected burn rate",
            "Evaluate runway adequacy versus next key milestone",
            "Identify dilution risk from future rounds and cap table structure",
            "Assess financing strategy: who are likely future investors?",
            "Evaluate capital efficiency vs comparable programs",
        ],
        "kill_criteria": [
            "Funding gap exists before reaching the next value inflection",
        ],
        "max_words": 400,
    },
    {
        "name": "Stage 7 — Post-Exclusivity Deep DD",
        "objective": "Full synthesis to support IC decision",
        "checklist": [
            "Synthesize all 7 prior stage findings into a coherent investment thesis",
            "Cross-reference scientific claims with clinical data in the dataroom",
            "Rank top 5 material risks with probability and severity",
            "Assess deal terms, valuation, and Series C entry price reasonableness",
            "Draft investment recommendation: Invest / Conditional / Pass",
        ],
        "kill_criteria": [],
        "max_words": 800,
    },
]
