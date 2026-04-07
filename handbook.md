# Phase-1 Clarification Addendum

**A. User Interface & Workflow Clause (Critical)**

**Structured Due Diligence Workspace**

In addition to any chat-based interface, the system must provide a structured Due Diligence Workspace with persistent sections, including at minimum:

* Executive Summary  
* Key Red Flags  
* Financial Overview  
* Legal & IP Considerations  
* Regulatory & Compliance Risks  
* Open Questions / Follow-ups

Each section must:

* Be generated independently  
* Be editable by the user  
* Be regenerable at section level without re-running the full analysis  
* Maintain linked source citations (document name \+ page)

This workspace shall serve as the primary DD output, not the chat interface.

**Why this matters:**  
This converts the tool from a “smart chat” into an **investment decision tool**.

---

**B. Provenance & Source Separation Clause**

**Source Attribution & Separation**

All generated outputs must explicitly label the origin of information as one of:

* “Derived from uploaded dataroom documents”  
* “Derived from public web sources”

Outputs must never mix internal dataroom facts and external web research without explicit labeling.

Each factual statement must include a citation pointing to the original source document and page, or to the external source URL.

**Why this matters:**  
This protects trust, auditability, and avoids fatal DD mistakes.  
---

**C. Early Screening / Quick Reject Mode**

**Quick Screening Mode**

The system must include a “Quick Screen” mode that generates a one-page preliminary assessment within minutes, including:

* Top 5 material risks  
* Preliminary deal viability score (Low / Medium / High risk)  
* Capital, regulatory, or structural deal-breakers

This mode is intended for rapid deal triage prior to full DD.

**Why this matters:**  
This directly supports your “weed out bad deals fast” requirement.

---

**D. Export & Editing Clause**

**Editable & Multi-Format Outputs**

Generated outputs must be exportable in:

* DOCX (editable)  
* PDF  
* PPTX (summary format)  
* XLSX (for extracted financials)

Users must be able to edit generated content prior to export.

---

**E. Phase-2 Readiness Clause (Future-Proofing)**

**Architectural Forward Compatibility**

All data models, embeddings, metadata schemas, and storage layers must be designed to support future multi-tenant SaaS deployment without requiring fundamental re-architecture.

---

# Core Principle: Sequential, Gated Due Diligence

*“Never spend money, time, or tokens before the previous gate is cleared.”*

Think of this as instructing a **junior assistant with a hard budget**:

* limited tokens  
* limited authority  
* must justify every escalation

This is exactly how real-world DD works.

---

**1️⃣ The Meta-Model (Applies to ALL Asset Classes)**

Every asset (Real Estate, Biotech, Infra, PE, Credit) follows the same **4-layer funnel**:

INPUT → SCREEN → VALIDATE → DEEP DD → IC

Each layer has:

* a **GO / NO-GO gate**  
* a **maximum analysis depth**  
* a **token budget**  
* a **hard stop condition**

This is how you prevent runaway costs and hallucination.

---

**2️⃣ Real Estate DD – Sequential Checklist (Token-Efficient)**

Below is a **production-grade DD flow** for Real Estate, aligned exactly with how professionals operate.

---

**STAGE 0 — Broker Teaser / Pitch Deck Intake**

📄 Input: Broker teaser, OM, Excel, email

**Objective**

*Answer ONE question only:*  
**“Is this even worth 30 more minutes?”**

**AI Tasks (Cheap)**

* Extract:  
  * Asset type  
  * Location  
  * Asking price  
  * NOI (claimed)  
  * Yield (claimed)  
  * Capex narrative  
* Normalize numbers  
* Flag missing info

**Output (1 screen, max 200 words)**

* Claimed IRR / Yield  
* Back-of-envelope sanity check  
* Confidence level: Low / Medium / High  
* **GO / NO-GO**

**Gate**

❌ Kill deal if:

* Returns rely on undefined assumptions  
* Numbers don’t reconcile  
* Location / asset type off-strategy

🟢 Proceed if:

* Claimed economics *could* make sense

💰 **Token spend:** very low  
🧠 **No assumptions allowed**

---

**STAGE 1 — Commercial Plausibility Check**

📄 Input: teaser \+ basic financials

**Objective**

*“If numbers are wrong, how wrong are they?”*

**AI Tasks**

* Rebuild simplified cash flow:  
  * NOI  
  * Conservative capex  
  * Exit yield stress  
* Compare to local benchmarks (if available)  
* Identify value drivers

**Output**

* Recalculated conservative IRR  
* Sensitivity summary (rent, exit cap)  
* Top 3 commercial risks  
* **Proceed / Stop recommendation**

**Gate**

❌ Stop if:

* Conservative IRR below your hurdle  
* Returns depend on heroic assumptions

🟢 Proceed if:

* Downside still acceptable

💰 **Token spend:** low–medium  
🧠 Still *no legal, no technical, no tax*

---

**STAGE 2 — Exclusivity Readiness Check**

📄 Input: more detailed model, rent roll, capex outline

**Objective**

*“Is this worth exclusivity?”*

**AI Tasks**

* Validate:  
  * Rent roll logic  
  * Vacancy assumptions  
  * Capex realism  
* Identify **what must be verified by humans later**

**Output**

* Deal attractiveness score  
* Clear list:  
  * “Can be verified internally”  
  * “Requires external advisors”  
* Draft **Exclusivity Decision Memo**

**Gate**

❌ Stop if:

* Too many unknowns  
* Risk is structural, not informational

🟢 Proceed if:

* Risks are *verifiable*, not fatal

💰 **Token spend:** medium  
🧠 Still internal-only DD

---

**STAGE 3 — Conditional Deep DD (Post-Exclusivity)**

📄 Input: full dataroom

**Objective**

*Support humans, not replace them*

**AI Tasks**

* Pre-read legal docs  
* Flag unusual clauses  
* Summarize technical reports  
* Cross-check assumptions vs reality

**Output**

* DD risk register  
* Advisor briefing notes  
* IC-ready materials

💰 **Token spend:** high  
🧠 External advisors now justified

---

**3️⃣ Why This Is Token-Efficient (Important)**

**Key design rules**

* **No stage can access future-stage documents**  
* **No stage can ask open-ended questions**  
* Each stage has:  
  * predefined prompts  
  * predefined output structure  
  * word limits

This prevents:

* hallucination  
* over-analysis  
* “AI enthusiasm creep”

---

**4️⃣ How This Translates Into Your Platform UI**

In your system this becomes:

Deal → Stage → Checklist → Gate → Unlock Next Stage

**UI Behavior**

* Locked stages (greyed out)  
* “Proceed” button only after checklist completion  
* Token usage shown per stage (optional but powerful)  
* Audit trail: *why* a deal advanced or died

This is **extremely VC/PE-grade**.

---

**5️⃣ This Is Also Your Commercial Differentiator**

Most DD AI tools:

* Run everything at once  
* Burn tokens  
* Produce fluffy output  
* Feel impressive but are useless in practice

Your system:

* Mimics real investment behavior  
* Saves money  
* Builds trust  
* Scales across asset classes

This is how you beat Manus, agent platforms, and generic copilots.

---

**6️⃣ Next Step (Highly Recommended)**

If you want, next I can:

1. Build the **exact checklist templates** for:  
   * Real Estate  
   * Biotech  
   * PE / Operating companies  
2. Convert each stage into **system prompts** (ready for engineering)  
3. Map **token budgets per stage** (so finance loves it)  
4. Design how **deal-kill reasons** are stored and reused (huge value)

Tell me **which asset class to finalize first**, and I’ll go all the way to implementation-level detail.

# Real Estate Checklists

Excellent. Below is a **production-grade, sequential DD checklist** designed exactly for what you described:

* **Capital- and token-efficient**  
* **Gated (GO / NO-GO at each step)**  
* **Usable by an AI assistant with “limited authority”**  
* **Configurable order for operated asset types**

I’ll first give you the **shared framework**, then **Checklist A** and **Checklist B**, and finally **how this becomes system logic in your platform**.

---

**🔑 GLOBAL RULES (Apply to All Real Estate Cases)**

**Hard constraints**

* No legal / tax / technical DD before commercial viability  
* No external advisors before exclusivity  
* Each stage has:  
  * fixed questions  
  * max output length  
  * explicit kill criteria

**Outputs are always**

* Bullet-based  
* Comparable across deals  
* Stored for benchmarking

---

### A) CONSTRUCTION GROUND – RESIDENTIAL (SELL-OUT OR GLOBAL EXIT)

**STAGE 0 — Broker Teaser Sanity Check**

📄 Input: teaser, map, price indication

**Objective**

“Is this site *potentially* developable and profitable?”

**Checklist**

* Location macro (city, district)  
* Plot size & zoning claim  
* Asking price per m² land  
* Claimed sellable area  
* Claimed exit(s):  
  * ☐ Individual unit sales  
  * ☐ Global exit (block sale)

**Output**

* Back-of-envelope land residual  
* Missing critical info list  
* GO / NO-GO

**Kill Criteria**

❌ Zoning incompatible  
❌ Price irreconcilable with local comps

---

**STAGE 1 — Development & Exit Logic Check**

📄 Input: teaser \+ planning assumptions

**Checklist**

* Net sellable area plausibility  
* Unit mix logic  
* Sales price vs market comps  
* Construction cost benchmarks  
* Timeline realism

**Exit Scenario A — Individual Sales**

* Average €/m² vs comps  
* Absorption speed  
* Sales risk sensitivity

**Exit Scenario B — Global Exit**

* Stabilized yield assumption  
* Exit cap vs market  
* Discount vs retail sales

**Output**

* IRR range per exit  
* Preferred exit rationale  
* Kill / Proceed

**Kill Criteria**

❌ Both exits fail hurdle rates

---

**STAGE 2 — Financial Robustness**

📄 Input: simplified model

**Checklist**

* Cost contingencies included?  
* Financing assumptions realistic?  
* Developer margin vs risk  
* Sensitivity: sales price –10%, costs \+10%

**Output**

* Downside IRR  
* Risk-adjusted return score  
* Exclusivity recommendation

**Kill Criteria**

❌ Margins evaporate under mild stress

---

**STAGE 3 — Pre-Exclusivity Risk Mapping**

📄 Input: site docs, high-level zoning docs

**Checklist**

* Planning risk level  
* Infrastructure dependencies  
* Community / political risk  
* Critical unknowns list

**Output**

* Risk register  
* “Advisor-needed” flags  
* Proceed to exclusivity: YES / NO

---

### B) CONSTRUCTION GROUND – OPERATED ASSETS

*(Hotel, Elderly Living, Serviced Apartments, Student Housing, etc.)*

**IMPORTANT DESIGN RULE**

The **user chooses the order** in which asset types are analyzed.

Example:

1. Hotel  
2. Serviced Apartments  
3. Student Housing

Only one asset type is analyzed at a time to save tokens.

---

**STAGE 0 — Highest & Best Use Pre-Screen**

📄 Input: teaser \+ zoning summary

**Checklist**

* Permitted uses  
* Location demand drivers  
* Size vs typical operator requirements

**Output**

* Ranked list of feasible uses  
* Kill infeasible uses immediately

---

**STAGE 1 — Asset-Type-Specific Commercial Screen**

*(Executed sequentially per selected asset type)*

---

**🏨 HOTEL MODULE**

* Star category fit  
* ADR vs comps  
* Occupancy realism  
* Brand dependence  
* Seasonality risk

Kill if:  
❌ No sustainable ADR  
❌ Demand is event-driven only

---

**🧓 ELDERLY LIVING MODULE**

* Catchment demographics  
* Public vs private pay mix  
* Staffing intensity  
* Regulatory exposure

Kill if:  
❌ Demographics don’t support demand  
❌ Regulation unclear

---

**🎓 STUDENT HOUSING MODULE**

* University proximity  
* Enrollment trends  
* Rent caps / regulation  
* Turnover risk

Kill if:  
❌ Declining enrollment  
❌ Rent caps kill economics

---

**🏢 SERVICED APARTMENTS MODULE**

* Corporate demand  
* Length-of-stay mix  
* Operational complexity  
* Competition

Kill if:  
❌ Overlap with hotels without ADR upside

---

**STAGE 2 — Operator & Economics Check**

📄 Input: indicative operator assumptions

**Checklist**

* Operator model:  
  * Lease  
  * Management  
  * Hybrid  
* Cost structure realism  
* Stabilized NOI plausibility  
* Exit yield realism

**Output**

* IRR per asset type  
* Preferred asset class  
* Proceed / Stop

---

**STAGE 3 — Exclusivity Readiness**

📄 Input: refined assumptions

**Checklist**

* Capital intensity vs return  
* Operational risk score  
* External advisors required?

**Output**

* Exclusivity memo  
* Asset type selection finalized

---

**6️⃣ HOW THIS BECOMES SYSTEM LOGIC (IMPORTANT)**

**Platform behavior**

* User selects:  
  * Asset category  
  * Exit scenarios  
  * Asset-type evaluation order  
* System:  
  * Locks future stages  
  * Enforces stage-by-stage progression  
  * Shows kill reasons clearly

**Token control**

* Each module:  
  * Fixed prompt  
  * Fixed word output  
  * No cross-stage context leakage

---

**7️⃣ Why This Is Institutional-Grade**

✔ Matches real investment workflows  
✔ Prevents premature advisor spend  
✔ Defensible decisions (audit trail)  
✔ Scales across geographies  
✔ Strong moat vs generic AI tools

---

**🚀 Next (Strongly Recommended)**

I can now:

1. Convert these checklists into **exact system prompts**  
2. Define **input schemas** (what documents per stage)  
3. Create **IC memo auto-draft templates**  
4. Extend this to **existing assets / refurbishments**

Tell me which one you want next.

Below is a **production-grade, sequential Due Diligence checklist for EXISTING ASSETS / REFURBISHMENTS**, designed exactly in the same **capital- and token-efficient, gated logic** you specified earlier.

This is **not** a generic checklist. It mirrors how senior investors actually behave:

* kill deals early  
* escalate spend only when justified  
* never involve advisors too early  
* preserve an audit trail of *why* decisions were made

---

### C) EXISTING ASSET / REFURBISHMENT

**Sequential Due Diligence Checklist (Token-Efficient)**

---

**🔑 GLOBAL RULES (Non-Negotiable)**

* No technical, legal, tax, or ESG DD before commercial viability  
* No external advisors before exclusivity  
* Every stage produces:  
  * **GO / NO-GO**  
  * **Reasoned justification**  
  * **Explicit next-step authorization**

---

**STAGE 0 — TEASER & REALITY CHECK**

📄 Input: broker teaser, OM, email pitch

**Objective**

*“Does this asset exist in reality and could it be interesting?”*

**Checklist**

* Asset type & age  
* Location & micro-location  
* Current use vs zoning claim  
* Reported NOI vs rent roll logic  
* Asking price vs headline yield

**Output (≤200 words)**

* Sanity-checked headline yield  
* Missing information list  
* Initial risk flags  
* **GO / NO-GO**

**Kill Criteria**

❌ Yield doesn’t reconcile  
❌ Location off-strategy  
❌ Asset condition unclear

💰 Token spend: **Very low**

---

**STAGE 1 — COMMERCIAL PLAUSIBILITY**

📄 Input: teaser \+ basic financials

**Objective**

*“If numbers are wrong, how wrong are they?”*

**Checklist**

* Rent roll coherence  
* Vacancy vs market norms  
* Operating costs vs benchmarks  
* Tenant concentration  
* Capex narrative (if any)

**Output**

* Rebuilt conservative NOI  
* Adjusted yield  
* Top 3 commercial risks  
* **Proceed / Stop**

**Kill Criteria**

❌ Conservative yield \< hurdle  
❌ Single-tenant dependency without mitigation

💰 Token spend: **Low**

---

**STAGE 2 — VALUE-ADD / REFURB LOGIC**

📄 Input: high-level capex assumptions

**Objective**

*“Is value-add real or cosmetic?”*

**Checklist**

* Capex purpose:  
  * Maintenance  
  * Repositioning  
  * Change of use  
* Rent upside realism  
* Re-letting risk  
* Phasing & downtime impact

**Output**

* Value-add plausibility score  
* Upside vs risk trade-off  
* Kill / Proceed

**Kill Criteria**

❌ Upside depends on heroic rent assumptions  
❌ Capex underestimated materially

💰 Token spend: **Low–Medium**

---

**STAGE 3 — CASH FLOW & DOWNSIDE STRESS**

📄 Input: simplified financial model

**Objective**

*“Can this survive bad luck?”*

**Checklist**

* NOI stress (–10%)  
* Capex overrun (+15%)  
* Exit yield expansion  
* Financing sensitivity

**Output**

* Downside IRR / equity multiple  
* Break-even analysis  
* Exclusivity recommendation

**Kill Criteria**

❌ Equity impaired under mild stress  
❌ No downside protection

💰 Token spend: **Medium**

---

**STAGE 4 — PRE-EXCLUSIVITY RISK MAPPING**

📄 Input: selected docs only

**Objective**

*“Are risks verifiable or structural?”*

**Checklist**

* Technical red flags (high-level only)  
* Lease structure risks  
* Regulatory exposure  
* ESG showstoppers

**Output**

* Risk register  
* Advisor dependency map:  
  * Technical  
  * Legal  
  * Tax  
* Go / No-Go for exclusivity

💰 Token spend: **Medium**

---

**STAGE 5 — POST-EXCLUSIVITY DEEP DD (HUMAN-LED)**

📄 Input: full dataroom

**Objective**

*Support humans, don’t replace them*

**AI Role**

* Pre-read reports  
* Flag anomalies  
* Summarize leases  
* Cross-check assumptions

**Output**

* DD issue tracker  
* IC memo draft  
* Closing risk summary

💰 Token spend: **High (justified)**

---

**OPTIONAL MODULES (ACTIVATED ONLY IF RELEVANT)**

**🏨 OPERATED ASSETS (HOTEL, PBSA, SENIOR LIVING)**

* NOI quality vs GOP  
* Operator dependency  
* Management agreement risks  
* Exit liquidity

**🏢 MULTI-TENANT COMMERCIAL**

* WAULT quality  
* Break options  
* Re-letting capex  
* Tenant credit risk

---

**HOW THIS FITS INTO YOUR PLATFORM**

**System Logic**

Deal → Stage → Checklist → Gate → Unlock Next Stage

**Governance**

* Each stage requires explicit approval  
* Kill reasons stored and reused  
* Benchmarking across deals enabled

---

**WHY THIS CHECKLIST IS INVESTMENT-GRADE**

✔ Mirrors institutional DD  
✔ Prevents premature spend  
✔ Token-efficient by design  
✔ Creates institutional memory  
✔ Works across geographies

---

**NEXT (OPTIONAL BUT POWERFUL)**

I can now:

1. Convert this into **exact system prompts**  
2. Create **IC memo templates**  
3. Map **token budgets per stage**  
4. Merge this with the development checklists into **one unified RE DD engine**

Tell me how deep you want to go next.

Below is a **production-grade, sequential Due Diligence checklist for BIOTECH COMPANIES**, explicitly designed for:

* **capital discipline**  
* **token efficiency**  
* **early kill decisions**  
* **no premature expert spend**  
* **human-in-the-loop escalation only when justified**

This mirrors how **top-tier VC / growth / PE biotech investors** actually operate, not how generic DD checklists look.

---

### D) BIOTECH COMPANY

**Sequential Due Diligence Checklist (Token-Efficient, Gated)**

---

**🔑 GLOBAL GOVERNANCE RULES (NON-NEGOTIABLE)**

* No deep science DD before commercial logic  
* No regulatory / IP law firms before technical plausibility  
* No KOLs / advisors before exclusivity  
* Each stage must produce:  
  * **GO / NO-GO**  
  * **Explicit kill reason**  
  * **Next-step authorization**

---

**STAGE 0 — TEASER & REALITY CHECK**

📄 Input: pitch deck, teaser, executive summary

**Objective**

*“Does this company solve a real problem in a plausible way?”*

**Checklist**

* Unmet medical need  
* Target indication size  
* Competitive landscape (headline)  
* Claimed differentiation  
* Stage of development

**Output (≤200 words)**

* Plain-English problem statement  
* Claimed value proposition  
* Immediate red flags  
* **GO / NO-GO**

**Kill Criteria**

❌ No clear unmet need  
❌ “Platform” without focus  
❌ Science buzzwords without clarity

💰 Token spend: **Very low**

---

**STAGE 1 — BIOLOGY & MECHANISM PLAUSIBILITY (NON-DEEP)**

📄 Input: pitch \+ public references

**Objective**

*“Does the biology make sense at a high level?”*

**Checklist**

* Target biology relevance  
* Mechanism of action (MoA) logic  
* Disease causality link  
* Prior validation (literature, precedents)

**Output**

* Biology plausibility score  
* Comparable approved / failed drugs  
* Key scientific unknowns  
* Proceed / Stop

**Kill Criteria**

❌ No biological precedent  
❌ Weak causal link to disease

💰 Token spend: **Low**

---

**STAGE 2 — PIPELINE & DEVELOPMENT REALISM**

📄 Input: pipeline slides, timelines

**Objective**

*“Is the development plan realistic?”*

**Checklist**

* Current phase (pre-clinical / Ph I / II / III)  
* Key upcoming inflection points  
* Trial design clarity  
* Timeline vs norms

**Output**

* Development risk score  
* Timeline realism assessment  
* Binary risk map  
* Proceed / Stop

**Kill Criteria**

❌ Over-optimistic timelines  
❌ No clear value inflection ahead

💰 Token spend: **Low–Medium**

---

**STAGE 3 — COMMERCIAL LOGIC (EARLY)**

📄 Input: market slides

**Objective**

*“Even if it works, is it worth anything?”*

**Checklist**

* Addressable market (realistic)  
* Pricing logic  
* Reimbursement pathway  
* Competitive displacement logic

**Output**

* Commercial upside range  
* Key adoption risks  
* Preliminary valuation logic  
* Exclusivity recommendation

**Kill Criteria**

❌ Market too small  
❌ Reimbursement implausible

💰 Token spend: **Medium**

---

**STAGE 4 — IP & REGULATORY PRE-SCREEN (LIGHT)**

📄 Input: patent summary, regulatory claims

**Objective**

*“Are there fatal legal/regulatory risks?”*

**Checklist**

* Patent family scope  
* Expiry horizon  
* Freedom-to-operate claims  
* Regulatory path (FDA / EMA)

**Output**

* IP risk score  
* Regulatory clarity score  
* Advisor-required flags  
* Go / No-Go for exclusivity

**Kill Criteria**

❌ IP weak or expiring  
❌ Regulatory path unclear

💰 Token spend: **Medium**

---

**STAGE 5 — TEAM & EXECUTION CAPABILITY**

📄 Input: bios, track records

**Objective**

*“Can this team actually execute?”*

**Checklist**

* Prior drug approvals  
* Clinical development experience  
* CEO / CSO credibility  
* Board relevance

**Output**

* Execution risk score  
* Key hiring gaps  
* Proceed / Stop

**Kill Criteria**

❌ No execution experience  
❌ Science-only team

💰 Token spend: **Medium**

---

**STAGE 6 — FINANCIAL & FUNDING LOGIC**

📄 Input: financials, cap table

**Objective**

*“Will this survive to the next inflection?”*

**Checklist**

* Burn rate vs milestones  
* Runway adequacy  
* Dilution risk  
* Financing strategy

**Output**

* Funding sufficiency score  
* Capital efficiency assessment  
* Final exclusivity decision

**Kill Criteria**

❌ Funding gap before value inflection

💰 Token spend: **Medium**

---

**STAGE 7 — POST-EXCLUSIVITY DEEP DD (HUMAN-LED)**

📄 Input: full dataroom

**AI Role**

* Literature synthesis  
* Trial protocol analysis  
* Patent claim mapping  
* Risk register drafting

**Output**

* IC memo draft  
* Scientific risk register  
* Decision support only

💰 Token spend: **High (justified)**

---

**OPTIONAL MODULES (ACTIVATED ONLY IF RELEVANT)**

**🧪 PLATFORM TECHNOLOGIES**

* Platform vs product risk  
* Repeatability evidence  
* Capital intensity

**🌍 RARE DISEASE**

* Patient identification  
* Trial feasibility  
* Pricing sustainability

---

**HOW THIS FITS YOUR PLATFORM PERFECTLY**

**System Behavior**

* Stages locked until cleared  
* Fixed prompt \+ fixed output per stage  
* Kill reasons stored and benchmarked  
* Advisor spend gated

---

**WHY THIS IS INVESTOR-GRADE**

✔ Matches institutional biotech DD  
✔ Prevents science-first bias  
✔ Token-efficient by design  
✔ Strong kill discipline  
✔ Scales across therapeutic areas

---

**NEXT (LOGICAL EXTENSIONS)**

If you want, I can:

1. Convert this into **exact system prompts**  
2. Create **IC memo auto-generation**  
3. Add **probability-weighted valuation logic**  
4. Integrate **scientific literature ingestion (we have to check this – are there free/paid sources available)**

Tell me how far you want to take it.

Below is a **production-grade, sequential Due Diligence checklist for a MATURE TARGET COMPANY in an LBO / MBO context**, built to the same principles you’ve enforced throughout:

* **capital & token discipline**  
* **early kill logic**  
* **sequential gating**  
* **no premature advisor spend**  
* **investment-committee defensible outputs**

This mirrors how **serious PE funds actually run DD**, not how generic DD templates look.

---

### E) MATURE TARGET COMPANY

**LBO / MBO Due Diligence Checklist (Sequential, Gated)**

---

**🔑 GLOBAL GOVERNANCE RULES**

* No deep operational or legal DD before leverage works  
* No QoE, legal, tax, or IT advisors before exclusivity  
* Every stage must end with:  
  * **GO / NO-GO**  
  * **Explicit kill reason**  
  * **Authorization to escalate**

---

**STAGE 0 — TEASER & INVESTMENT LOGIC CHECK**

📄 Input: teaser, CIM, broker email

**Objective**

*“Why does this business exist as an LBO candidate?”*

**Checklist**

* Business model clarity  
* Revenue sources  
* EBITDA quality (headline)  
* Market position  
* Ownership motivation (why selling?)

**Output (≤200 words)**

* Plain-English investment thesis (draft)  
* Immediate red flags  
* **GO / NO-GO**

**Kill Criteria**

❌ EBITDA unclear or overstated  
❌ No value-creation angle

💰 Token spend: **Very low**

---

**STAGE 1 — LEVERAGE & RETURNS FEASIBILITY**

📄 Input: teaser \+ basic financials

**Objective**

*“Does leverage work without heroics?”*

**Checklist**

* EBITDA normalization (high level)  
* Debt capacity (market norms)  
* Entry multiple sanity check  
* Base-case IRR logic

**Output**

* Max sustainable leverage  
* Equity check estimate  
* Base-case IRR range  
* Proceed / Stop

**Kill Criteria**

❌ Returns only work with aggressive leverage  
❌ Entry multiple unjustifiable

💰 Token spend: **Low**

---

**STAGE 2 — CASH FLOW QUALITY & DOWNSIDE**

📄 Input: historical P\&L, cash flow

**Objective**

*“Can this service debt under stress?”*

**Checklist**

* EBITDA → cash conversion  
* Working capital stability  
* Capex requirements  
* Cyclicality exposure

**Output**

* Free cash flow reliability score  
* Downside debt coverage  
* Exclusivity recommendation

**Kill Criteria**

❌ Weak cash conversion  
❌ High cyclicality without buffers

💰 Token spend: **Low–Medium**

---

**STAGE 3 — BUSINESS & MARKET DURABILITY**

📄 Input: CIM, market overview

**Objective**

*“Will this business still exist in 5 years?”*

**Checklist**

* Market growth vs GDP  
* Customer concentration  
* Switching costs  
* Competitive moat

**Output**

* Business durability score  
* Revenue risk drivers  
* Proceed / Stop

**Kill Criteria**

❌ Structural decline  
❌ Customer concentration fatal

💰 Token spend: **Medium**

---

**STAGE 4 — VALUE CREATION LEVERS (NO DETAIL YET)**

📄 Input: management plan, IC hypothesis

**Objective**

*“Where does upside come from?”*

**Checklist**

* Pricing power  
* Cost levers  
* Operational improvements  
* M\&A / roll-up potential

**Output**

* Credible value-creation map  
* Execution risk assessment  
* Go / No-Go for exclusivity

**Kill Criteria**

❌ No controllable levers  
❌ Upside relies solely on multiple expansion

💰 Token spend: **Medium**

---

**STAGE 5 — MANAGEMENT & MBO READINESS**

📄 Input: management bios, incentives

**Objective**

*“Can and should management run this?”*

**Checklist**

* Track record  
* Depth of bench  
* Alignment (roll-over, incentives)  
* Key-man risk

**Output**

* Management credibility score  
* MBO feasibility assessment  
* Proceed / Stop

**Kill Criteria**

❌ Weak management depth  
❌ Misaligned incentives

💰 Token spend: **Medium**

---

**STAGE 6 — PRE-EXCLUSIVITY RISK MAPPING**

📄 Input: selected documents

**Objective**

*“Are risks verifiable or structural?”*

**Checklist**

* Legal / regulatory exposure (high-level)  
* IT & systems maturity (headline)  
* ESG showstoppers  
* Accounting complexity

**Output**

* Risk register  
* Advisor dependency map  
* Go / No-Go for exclusivity

💰 Token spend: **Medium**

---

**STAGE 7 — POST-EXCLUSIVITY DEEP DD (HUMAN-LED)**

📄 Input: full dataroom

**AI Role**

* QoE prep support  
* Contract summarization  
* Risk cross-checks  
* IC memo drafting

**Output**

* IC-ready investment memo  
* Downside / base / upside cases  
* Closing risk summary

💰 Token spend: **High (justified)**

---

**OPTIONAL MODULES (ACTIVATED ONLY IF RELEVANT)**

**🔄 CARVE-OUTS**

* Standalone cost estimation  
* TSA risks  
* Systems separation

**🌍 INTERNATIONAL OPERATIONS**

* FX exposure  
* Transfer pricing risk  
* Country risk

---

**HOW THIS MAPS PERFECTLY TO YOUR PLATFORM**

**System Logic**

Deal → Stage → Checklist → Gate → Unlock

**Controls**

* Locked future stages  
* Token budget per stage  
* Kill-reason memory  
* IC-defensible audit trail

---

**WHY THIS IS INSTITUTIONAL-GRADE**

✔ Mirrors PE reality  
✔ Protects IRR discipline  
✔ Prevents early advisor spend  
✔ Token-efficient by design  
✔ Scales across strategies

---

**NEXT (OPTIONAL BUT VERY POWERFUL)**

I can now:

1. Convert this into **system prompts**  
2. Create **LBO model validation logic**  
3. Build **IC memo auto-generation**  
4. Add **portfolio benchmarking**

Tell me how far you want to go.

---

# External (Human) Consultants Interface (or how to save a shitload of fees)

You **cannot eliminate external consultants entirely** in serious transactions — but you *can* reduce their scope by **50–80%** if your DD system is designed correctly.

#### *The Core Idea*

**Replace “consultants as explorers” with consultants as validators**

Today, consultants:

* explore blindly  
* re-read everything  
* rediscover obvious issues  
* bill by the hour

Your system should:

* **pre-read everything**  
* **pre-flag issues**  
* **pre-structure questions**  
* hire consultants only to **confirm or refute specific hypotheses**

That’s how you cut cost without increasing risk.

---

**1️⃣ The “Minimum Spend DD” Operating Model**

Think in **3 layers**, not “consultants yes/no”.

AI \+ Internal Team → Targeted Validation → Surgical External DD

---

**2️⃣ What AI \+ Internal Team Should Do FIRST (Free / Cheap)**

**A. Document Pre-Reading (Massive Savings)**

AI should:

* read 100% of the dataroom  
* summarize every contract  
* extract:  
  * termination clauses  
  * change-of-control  
  * penalties  
  * unusual provisions

👉 Consultants should **never be paid to read**.

---

**B. Risk Hypothesis Generation**

Instead of “do a legal DD”, you give consultants:

“Please confirm whether clauses X, Y, Z create enforceable risks.”

Examples:

* “We believe lease 12 has an unwaivable break option in 2026 — confirm.”  
* “We think this patent claim is narrow — validate or refute.”

This alone cuts **30–40% of hours**.

---

**C. DD Scoping Pack (Critical)**

Before hiring anyone, your system produces a **1–2 page DD Scope Pack**:

* What we think is fine  
* What we think is risky  
* What we *need confirmed*  
* What we explicitly **don’t want reviewed**

This is where most savings happen.

---

**3️⃣ Minimal-Spend Strategy by DD Type**

Below is how you minimize spend **per advisor**.

---

**⚖️** *LEGAL DD (Target: –60–70% cost)*

**What AI does first**

* Clause extraction  
* Contract clustering  
* Red-flag detection  
* Litigation history scan

**How to hire lawyers**

* Fixed-fee, capped scope  
* Only review:  
  * flagged clauses  
  * top 20 contracts  
  * deal-breaker items

**What NOT to pay for**

❌ Full contract review  
❌ “General comfort” memos

---

#### *🧮 FINANCIAL DD / QoE (Target: –40–50%)*

**What AI \+ internal team does**

* Normalize EBITDA  
* Identify one-offs  
* Rebuild cash flow  
* Flag revenue recognition issues

**How to hire auditors**

* Confirm **specific adjustments only**  
* No re-modeling  
* No scenario building

---

#### *🏗️ TECHNICAL / REAL ESTATE DD (Target: –50%)*

**What AI does**

* Read technical reports  
* Flag inconsistencies  
* Identify missing inspections

**How to hire engineers**

* Site walk only  
* Validate 5–10 critical assumptions  
* No full-condition survey unless needed

---

#### *🧪 BIOTECH / SCIENTIFIC DD (Target: –50–70%)*

**What AI does**

* Literature synthesis  
* Trial precedent mapping  
* Mechanism plausibility  
* Competitive failure analysis

**How to hire KOLs**

* Single, narrow questions  
* Written opinion only  
* No open-ended advisory

---

**4️⃣ The “Stop-Loss” Rule (Very Important)**

You must **hard-cap DD spend before exclusivity**.

Example:

* Pre-exclusivity DD budget: €20–50k  
* Post-exclusivity DD budget: €100–250k

Once hit:

* DD stops  
* Decision forced

This discipline alone saves millions over a fund life.

---

**5️⃣ How Your Platform Makes This Possible (Key Differentiator)**

Your DD system should automatically generate:

**A. Advisor Briefing Pack**

For each advisor:

* Context  
* Hypotheses  
* Documents to review  
* Explicit non-scope

**B. Advisor Cost vs Risk Dashboard**

* Cost incurred  
* Risk reduced  
* Remaining unknowns

This lets partners ask:

“Why are we still paying these people?”

---

**6️⃣ Reality Check (Very Important)**

**Do not**:

* try to replace legal sign-off  
* try to replace regulatory confirmation  
* try to bluff ICs

**Do**:

* replace wasted exploration  
* replace redundant reading  
* replace unfocused scopes

This is how **top funds actually operate**, even if they don’t talk about it publicly.

---

**7️⃣ Quantified Impact (Realistic)**

| DD Area | Typical Cost | With This Model |
| :---- | :---- | :---- |
| Legal DD | €60–120k | €20–40k |
| Financial DD | €50–100k | €25–50k |
| Technical DD | €40–80k | €15–30k |
| Scientific DD | €40–100k | €15–30k |

**Total saving per deal:** 50–70%

---

**8️⃣ Next (If You Want to Implement This)**

I can:

1. Design **advisor scoping templates** (copy-paste ready)  
2. Create **pre-DD risk hypothesis generators**  
3. Build **DD spend stop-loss logic**  
4. Simulate a full deal with costs vs risk reduction

If you want to build a **truly differentiated DD platform**, this is the layer that separates tools from institutions.

Tell me what you want next.

# A Venture Feasibility DD Engine — but applied to your own startup ideas, not external targets.

This is extremely powerful if structured correctly.  
Below is a **precise, implementation-ready framework** your agency can build into the DD Companion as a dedicated module:

---

## 🚀 VENTURE CREATION DD ENGINE

*(Internal Opportunity Validation Framework)*

This is structured exactly like institutional DD:

IDEA → MARKET → COMPETITION → PRODUCT → BUILD → GTM → FINANCIALS → RISK → DECISION

Each stage is:

* Sequential  
* Gated  
* Token-efficient  
* IC-defensible

---

#### *MODULE 0 — IDEA DEFINITION (MANDATORY INPUT STRUCTURE)*

**Objective**

Force clarity before analysis.

**Required Inputs (Structured Form)**

* Problem statement (1 sentence)  
* Target customer  
* Industry  
* Business model (SaaS, Marketplace, Asset-heavy, etc.)  
* Geographic focus  
* Revenue logic (subscription, transaction, spread, etc.)  
* Why now?

**Output**

* Clear thesis summary  
* Internal coherence score  
* Kill / Proceed

---

#### *MODULE 1 — TAM & MARKET STRUCTURE*

**Objective**

Validate whether the opportunity is large enough and accessible.

**Checklist**

* TAM (theoretical max)  
* SAM (realistically addressable)  
* SOM (achievable 5-year share)  
* Growth rate  
* Market fragmentation  
* Buyer behavior

**Output**

* TAM/SAM/SOM table  
* Market attractiveness score  
* Time-to-scale estimate  
* Kill / Proceed

---

#### *MODULE 2 — INCUMBENT ANALYSIS (SWOT \+ DEFENSIBILITY)*

**Objective**

Determine if incumbents are weak enough to attack.

**For each key incumbent:**

* Revenue estimate  
* Pricing model  
* Core strengths  
* Structural weaknesses  
* Switching costs  
* Tech stack maturity  
* Customer lock-in

**Output**

* SWOT comparison table  
* Entry barrier map  
* Attack vector identification  
* Kill / Proceed

---

#### *MODULE 3 — PRODUCT DEFINITION & DIFFERENTIATION*

**Objective**

Define the **minimum product needed to win**, not just to exist.

**Checklist**

* Core features (MVP)  
* “Table stakes” features  
* Differentiation features  
* Required integrations  
* UX advantage potential  
* Switching trigger for customers

**Output**

* MVP feature list  
* Phase-2 roadmap  
* Differentiation clarity score  
* Kill / Proceed

---

#### *MODULE 4 — BUILD FEASIBILITY (TIME & COST)*

**Objective**

Estimate build complexity and cost with realism.

**Checklist**

* Tech stack recommendation  
* Vibe coding feasibility  
* Required dev skill level  
* Build time estimate (MVP)  
* Full product build time  
* Initial CAPEX estimate  
* Ongoing dev cost

**Output**

* CAPEX estimate  
* Timeline (months)  
* Team composition needed  
* Kill / Proceed

---

#### *MODULE 5 — GO-TO-MARKET STRATEGY*

**Objective**

Define cheapest and most efficient penetration strategy.

**Checklist**

* Target segment sequencing  
* Customer acquisition channels  
* Sales model (PLG / outbound / hybrid)  
* CAC estimate  
* Pricing strategy  
* Early traction strategy

**Output**

* GTM roadmap (0–24 months)  
* CAC/LTV logic  
* Market penetration timeline  
* Kill / Proceed

---

#### *MODULE 6 — FINANCIAL MODEL (CORE)*

**Objective**

Determine whether this makes economic sense.

**Required Outputs**

* Revenue ramp (5 years)  
* CAC & retention assumptions  
* Operating cost build-up  
* Burn rate  
* Break-even month  
* CAPEX recovery point  
* Cash flow positive month  
* Stabilized EBITDA  
* Stabilized FCF

**Sensitivities**

* \+/– 20% CAC  
* \+/– 20% churn  
* \+/– 20% pricing  
* Delayed traction by 6–12 months

**Output**

* Base / downside / upside  
* IRR equivalent (if self-funded)  
* Kill / Proceed

---

#### *MODULE 7 — DEFENSIBILITY & MOAT ANALYSIS*

**Objective**

Estimate durability of stable cash flow.

**Checklist**

* Network effects?  
* Data moat?  
* Switching costs?  
* Brand?  
* Regulatory barriers?  
* Scale advantages?

**Output**

* Moat score  
* Defensibility duration estimate (years)  
* Risk of disruption

---

#### *MODULE 8 — CAPITAL STRATEGY*

**Objective**

Decide funding structure.

**Options evaluated:**

* Bootstrap  
* Angel  
* Family Office  
* VC  
* Strategic partner

**Output**

* Optimal capital structure  
* Dilution scenarios  
* Investor pitch positioning

---

#### *MODULE 9 — FINAL INVESTMENT MEMO*

Headlines only:

* Executive Summary  
* Problem & Market  
* Competitive Positioning  
* Product Strategy  
* Build Plan  
* GTM Strategy  
* Financial Projections  
* Sensitivity Analysis  
* Risk Matrix  
* Go / No-Go Decision  
* Required Capital & Milestones

---

**🎯 HOW THIS SHOULD BE IMPLEMENTED (AGENCY SPECIFICATION)**

**1\. Stage-Gated System**

* Cannot skip modules  
* Cannot run financial model before TAM defined

**2\. Token Control**

* Fixed word outputs per stage  
* No open-ended analysis

**3\. Editable Templates**

* All outputs modifiable  
* Downloadable:  
  * DOCX  
  * PDF  
  * PPT

**4\. Benchmark Storage**

Store:

* All killed ideas  
* Kill reasons  
* Assumption errors

This creates institutional learning.

---

**WHY THIS IS EXTREMELY POWERFUL**

You now have:

* A **venture IC machine**  
* A filter against idea hype  
* A cost estimation engine  
* A defensibility predictor  
* A capital planning tool

Most founders operate on emotion.

You would operate on structured capital discipline.

---

Perfect. Below are the **four components**, clearly separated, structured, and implementation-ready for your agency.

This is designed to become a **“Venture DD Companion Module”** inside your platform.

---

## PART 1 — INVESTOR-READY OUTPUT TEMPLATE (HEADLINES ONLY)

This is the structured document that can be exported to Family Offices, HNIs, Institutions.

---

#### *1\. Executive Summary*

* Investment Thesis  
* Capital Required  
* Expected Return Profile  
* Key Risk Factors  
* Decision Recommendation

---

#### *2\. Problem Definition*

* Pain Point Description  
* Target Customer Segment  
* Urgency & Timing (“Why Now?”)

---

#### *3\. Market Opportunity*

* Total Addressable Market (TAM)  
* Serviceable Available Market (SAM)  
* Serviceable Obtainable Market (SOM)  
* Market Growth Rate  
* Structural Drivers

---

#### *4\. Competitive Landscape*

* Key Incumbents  
* Market Share Estimates  
* SWOT Comparison Table  
* Entry Barriers  
* Switching Costs

---

#### *5\. Product Strategy*

* MVP Definition  
* Core Features  
* Differentiation Features  
* Product Roadmap (Phase 1–3)  
* Integration & Tech Dependencies

---

#### *6\. Build & Operational Plan*

* Tech Stack  
* Development Timeline  
* Required Team Structure  
* CAPEX Estimate  
* Ongoing OPEX Estimate

---

#### *7\. Go-To-Market Strategy*

* Target Segment Sequencing  
* Pricing Strategy  
* Sales Model  
* Customer Acquisition Channels  
* CAC Estimate  
* Conversion Funnel Logic

---

#### *8\. Financial Projections*

* Revenue Ramp (5 Years)  
* Gross Margin  
* EBITDA Projection  
* Free Cash Flow  
* Break-Even Point  
* Cash Flow Positive Month  
* Stabilized EBITDA

---

#### *9\. Sensitivity Analysis*

* Revenue Sensitivity  
* CAC Sensitivity  
* Churn Sensitivity  
* Cost Overrun Sensitivity  
* Delayed Traction Scenario

---

#### *10\. Defensibility & Moat*

* Competitive Moat Type  
* Durability Estimate  
* Replication Risk  
* Regulatory Exposure

---

#### *11\. Capital Strategy*

* Funding Structure Options  
* Dilution Scenarios  
* Exit Scenarios  
* Target IRR

---

#### *12\. Risk Matrix*

* Market Risks  
* Execution Risks  
* Financial Risks  
* Competitive Risks  
* Regulatory Risks

---

#### *13\. Final Investment Decision*

* Go / No-Go  
* Required Milestones  
* Capital Release Triggers

---

## PART 2 — SYSTEM PROMPTS (FOR AGENCY IMPLEMENTATION)

Each module must run as a **separate structured prompt**.

---

#### *Prompt 1 — Market Analysis*

“Estimate TAM, SAM, SOM based on available data.  
Use bottom-up logic where possible.  
State all assumptions explicitly.  
Provide numeric ranges, not single values.  
Limit output to 400 words \+ table.”

---

#### *Prompt 2 — Competitive Mapping*

“Identify top 5 incumbents.  
For each, analyze pricing model, switching costs, strengths, weaknesses.  
Estimate structural entry barriers.  
Provide attack vectors.  
Limit output to 500 words.”

---

#### *Prompt 3 — Build Feasibility*

“Estimate realistic MVP build time and cost given current tooling.  
Break into phases.  
Provide team composition.  
Provide CAPEX range and OPEX run rate.  
Avoid speculative over-optimization.”

---

#### *Prompt 4 — Financial Model Assumptions*

“Construct a 5-year financial projection using conservative base case.  
Provide downside and upside case.  
Clearly list key assumptions.  
Include break-even month and stabilized EBITDA.”

---

#### *Prompt 5 — Sensitivity Engine*

“Stress test the base model using ±20% variation in revenue, CAC, churn and build delay.  
Output IRR and break-even impact.”

---

#### *Prompt 6 — Moat & Defensibility*

“Assess structural defensibility.  
Estimate durability of competitive advantage in years.  
State basis for estimate.”

---

#### *PART 3 — QUANTITATIVE SCORING MODEL*

Each module produces a weighted score.

---

**Scoring Dimensions (0–10 Each)**

1. Market Attractiveness  
2. Competitive Penetrability  
3. Product Differentiation  
4. Build Feasibility  
5. Capital Efficiency  
6. Revenue Scalability  
7. Defensibility  
8. Risk Level (reverse score)

---

**Weighted Composite Score**

Example Weights:

* Market: 20%  
* Competition: 15%  
* Product: 10%  
* Build: 10%  
* Financials: 20%  
* Moat: 15%  
* Risk Adjustment: 10%

Final Output:

* Composite Score (0–100)  
* Investment Grade Classification:  
  * 80–100: Strong Investable  
  * 60–79: Conditional  
  * \<60: Reject

---

#### *PART 4 — SENSITIVITY-DRIVEN DECISION MATRIX*

This is critical for disciplined capital allocation.

---

**Scenario Matrix**

| Scenario | IRR | Break Even | Cash Burn | Decision |
| :---- | :---- | :---- | :---- | :---- |
| Base | X% | Month X | €X | Invest |
| Revenue –20% | X% | Month X | €X | Conditional |
| CAC \+20% | X% | Month X | €X | Review |
| Delay 12m | X% | Month X | €X | Reject |

---

**Capital Release Triggers**

Stage-based funding:

* Phase 1: MVP completed  
* Phase 2: First 50 paying users  
* Phase 3: CAC validated  
* Phase 4: Unit economics proven

Capital only released after trigger met.

---

**What This Achieves**

You now have:

* A venture IC engine  
* A structured thesis validator  
* A risk-adjusted capital discipline tool  
* An exportable investor document generator  
* A benchmark memory across ideas

This turns brainstorming into institutional capital allocation.

---

Excellent. Below are the two requested components, clearly separated and implementation-ready.

---

## PART 1 — AI “RED TEAM” MODULE

*(Systematically Attack Your Own Venture Thesis)*

This module exists to **destroy weak ideas early**.

It must run **after the base case analysis is complete**, but before final investment approval.

---

#### *🔴 MODULE OBJECTIVE*

Identify structural flaws, unrealistic assumptions, hidden risks, and capital traps.

The Red Team is not allowed to be optimistic.

Tone: analytical, skeptical, institutional.

---

#### *🔴 RED TEAM STRUCTURE (HEADLINES ONLY)*

**1\. Core Thesis Attack**

* Why This Idea Might Be Fundamentally Wrong  
* Structural Assumption Dependencies  
* Hidden Circular Logic

---

**2\. Market Skepticism**

* Overestimated TAM Risks  
* Market Access Friction  
* Buyer Behavior Misinterpretation  
* “Market Exists But Won’t Pay” Risk

---

**3\. Competitive Reality Check**

* Incumbent Reaction Risk  
* Pricing Compression Scenarios  
* Switching Cost Overestimation  
* Hidden Competitive Advantages of Incumbents

---

**4\. Product Risk Attack**

* Feature Parity Risk  
* “Nice-to-Have” vs “Must-Have”  
* Adoption Friction  
* Integration Complexity Underestimation

---

**5\. Build & Execution Risk**

* Development Underestimation  
* Talent Availability Risk  
* Technical Debt Accumulation Risk  
* Scaling Risk

---

**6\. Financial Fragility**

* CAC Underestimation Risk  
* Churn Underestimation Risk  
* Burn Rate Escalation Risk  
* Working Capital Blind Spots

---

**7\. Capital Trap Scenarios**

* Infinite Fundraising Risk  
* “Zombie Startup” Risk  
* Delayed PMF Risk  
* Overfunding Risk

---

**8\. Worst-Case Scenario Narrative**

* 24-Month Failure Timeline  
* Capital Lost Before Realization  
* Reputation Risk

---

**9\. Kill Criteria Confirmation**

* Conditions Under Which Investment Must Be Rejected  
* Required Validation Before Capital Release

---

#### *🔴 SYSTEM PROMPT FOR IMPLEMENTATION*

The Red Team prompt must:

* Assume base case is flawed  
* Identify minimum 5 structural risks  
* Quantify downside where possible  
* Propose stress scenarios  
* Recommend GO / CONDITIONAL / REJECT

---

#### *🔴 OUTPUT FORMAT*

* Structured bullet format  
* No more than 1,000 words  
* Clear final recommendation

---

## PART 3 — AGENCY TECHNICAL SPECIFICATION (SOW-READY)

Below is a formal, structured implementation outline:

---

**FEATURE: VENTURE FEASIBILITY DD ENGINE**

---

**1\. System Architecture**

**1.1 Modular, Sequential Engine**

* Idea Definition  
* Market Analysis  
* Competition  
* Product Definition  
* Build Feasibility  
* Financial Modeling  
* Sensitivity Analysis  
* Moat Analysis  
* Red Team  
* Final Memo

Each module:

* Locked until previous completed  
* Outputs stored in database  
* Editable by user

---

**2\. Input Layer Requirements**

Structured input fields:

* Industry  
* Geography  
* Business Model  
* Target Customer  
* Revenue Model  
* Assumption Overrides

---

**3\. Prompt Layer**

Each module runs:

* Predefined system prompt  
* Max token limit  
* Word-limited output  
* Deterministic temperature settings (low hallucination mode)

---

**4\. Financial Engine Requirements**

Must include:

* 5-year revenue ramp  
* CAC model  
* Churn model  
* OPEX breakdown  
* CAPEX modeling  
* Burn rate calculation  
* Break-even calculation  
* Cash flow calculation  
* Stabilized EBITDA  
* Sensitivity module

Must output:

* Base  
* Downside  
* Upside

---

**5\. Scoring Engine**

Each module produces:

* Score (0–10)  
* Confidence level  
* Weighting

System calculates:

* Composite Score (0–100)  
* Investment Grade

---

**6\. Sensitivity Engine**

Must automatically run:

* Revenue –20%  
* CAC \+20%  
* Churn \+20%  
* Build delay \+6 months  
* OPEX \+15%

Outputs:

* IRR impact  
* Break-even shift  
* Burn increase

---

**7\. Red Team Module**

Runs after financial model.

Must:

* Stress-test assumptions  
* Identify fatal flaws  
* Produce kill criteria  
* Output investment recommendation

---

**8\. Export Engine**

Must generate:

* DOCX  
* PDF  
* PPT (IC version)  
* Editable text

Sections selectable:

* Full memo  
* Executive summary only  
* Red team only

---

**9\. Governance Layer**

* Stage-based approval  
* Kill reason logging  
* Assumption tracking  
* Version history

---

**10\. Performance Constraints**

* Fixed token budget per module  
* Max word output enforced  
* No open-ended generation  
* No cross-stage contamination

---

**11\. Dashboard Requirements**

For portfolio view:

* Idea name  
* Composite score  
* Capital required  
* Break-even timeline  
* Red Team verdict  
* Decision status

---

**12\. Security & Control**

* Role-based access  
* Investor-only view mode  
* Audit log

---

**WHAT THIS ACHIEVES**

You now have:

* An institutional-grade venture vetting machine  
* A capital-discipline enforcement layer  
* A self-destruct mechanism for bad ideas  
* A defendable IC process  
* A scalable internal opportunity factory

---
