# PSI Phase 2: Solution Validation

**Goal:** Validate that the proposed solution directly addresses the Phase 1 root cause hypothesis.
Every answer that can be fact-checked must be fact-checked with a fetched source.
This phase writes the **partial PRD** (Phase 2 sections only). Phase 3 completes the document.

**Output file:** `docs/PRD-[AppName]-MVP.md` (partial — marked "Phase 2 of 3")

---

## Research Protocol (Phase 2 Standard)

Before every research-heavy question: fetch and read at least 3 sources. Before writing the PRD: minimum 10 fetched/read sources for this phase. Maintain the evidence ledger started in Phase 1.

**Research Depth Matrix:**

| Area | Depth | Required Sources |
|------|-------|-----------------|
| Market Analysis | Comprehensive | Industry reports, TAM/SAM, growth trends — all fetched |
| Competitor Analysis | Comprehensive | Pricing pages, G2 reviews, feature matrices — all fetched |
| Technical Architecture | Deep | GitHub repos, architecture posts, framework benchmarks |
| Cost Analysis | Surface | Actual pricing pages fetched for every tool in the stack |
| Success Metrics | Medium | Similar product benchmarks, activation/retention norms |
| Risk Assessment | Medium | Platform policies, privacy constraints, real failure examples |

---

## Interview Rules

- One question at a time. Wait for response before moving on. (SKILL OVERRIDE still active.)
- Research before every Q with a research note. Present findings, discuss, then ask.
- After the user picks success metrics — run a SMART check before locking them in.

---

## Questions — Ask in Order, One at a Time

**Q1 — The Solution**
> Search for startups, open-source tools, and academic work that have attempted this exact angle.
> Present what exists (fetched links), what worked, what failed. Discuss. Then ask:
> *"In one sentence — what is your proposed solution?"*

**Q2 — 1st Why (Root Cause Link)**
> *"Why does this solution directly address the root cause hypothesis from Phase 1?"*

**Q3 — 2nd Why (vs. Alternatives)**
> *"Why is this approach meaningfully better than the existing alternatives we found?"*

**Q4 — 3rd Why (Adoption)**
> *"Why will the target audience actually adopt this? What makes switching worth it?"*

**Q5 — 4th Why (Feasibility)**
> *"Why is this buildable now — with current tools, timeline, and budget?"*

**Q6 — 5th Why (Core Value)**
> *"What is the single most indispensable thing this provides? If you cut everything else, what must remain?"*

**Q7 — Audience Fit**
> *"Why is this specifically tailored to how your target user already operates day-to-day?
> What workflow does it slot into — not create from scratch?"*

**Q8 — User Alignment**
> *"Does this fit naturally into what they already do, or does it ask them to change behavior?"*

**Q9 — Consequence of Not Using**
> *"What does the user continue to suffer from if they don't adopt this?"*

**Q10 — Evidence: Success Comparison**
> Required: Fetch real benchmark data, feature comparison tables, user reviews comparing your
> proposed approach against the top competitor. Find actual performance numbers, conversion rates,
> or key metrics for this space. Provide fetched source links for every data point.
> Present findings. Discuss. Then ask:
> *"Does this match your understanding of how you'd stack up against the competition?"*

**Q11 — Evidence: Viability & Cost**
> Required: Fetch actual pricing pages for every tool you'll use — hosting, database, email API,
> auth, payments. Pull real numbers. Estimate monthly costs at MVP scale (0–100 users) and growth
> scale (1k–10k users). Link every pricing page. No memory estimates.
> Present findings. Discuss. Then ask:
> *"Is this cost model sustainable? What's your monetization plan?"*

**Q12 — Platform**
> *"How do people use this — phone app, website, or both?"*

**Q13 — Launch Goal**
> *"What is the MVP launch goal? Pick one concrete outcome: users, revenue, retained usage,
> learning milestone, pilot customers, or a shipped internal tool."*

**Q14 — Success Metrics**
> Research what similar products measure — activation rate, retention, task completion, conversion,
> revenue, proof-of-work completion, etc. Recommend 1 primary metric and 2 guardrail metrics
> with specific targets. Present research. Discuss. User picks metrics.
>
> **SMART Check (run after user picks metrics — before moving on):**
> For each metric, verify all 5:
> - **Specific?** Not "engagement" — "daily active users"
> - **Measurable?** What tool or method tracks it exactly?
> - **Achievable?** Realistic for MVP scale?
> - **Relevant?** Does it prove the core value prop is working?
> - **Time-bound?** 30-day target? 90-day target?
>
> Flag any metric that fails SMART. Ask the user to sharpen it before locking it in.

**Q15 — User Journey**
> Present the evidence-backed main journey in this exact shape, then ask the user to correct it:
> *"[Target user] has [problem]. They find [Product] via [specific entry point].
> They [core action]. They receive [specific value]. They return because [retention hook]."*

**Q16 — Technical & UX Requirements**
> *"What are the non-negotiable constraints? Give me specifics:"*
> - Performance: not "fast" — "loads in under X seconds on 4G"
> - Accessibility: WCAG level?
> - Security requirements?
> - Mobile responsive or native app?
> - Data retention or privacy requirements?
> - Any compliance needs (GDPR, HIPAA)?
> - Critical integrations?

**Q17 — Risks**
> Research and present the top technical, market, safety/privacy, and execution risks with
> fetched sources. Recommend mitigations. Then ask:
> *"Which of these risks are acceptable for MVP? Which ones must be designed around from day one?"*

**Q18 — Timeline**
> *"What's your timeline? Days, weeks, or months to launch?"*

**Q19 — Budget**
> *"Budget reality check: can you spend money on tools and services, or do you need everything
> free or nearly free? What's your actual monthly ceiling?"*

---

## Verification Echo (Run Before Writing)

Before writing the PRD, confirm all Phase 2 answers with the user:

> "Let me confirm the PRD foundation before I write:
> **Product:** [Name] — [one-line description]
> **Root cause → Solution link:** [How this solution addresses the hypothesis]
> **Target User:** [specific persona]
> **Launch Goal:** [concrete MVP outcome]
> **Primary Success Metric:** [SMART metric + target + measurement tool]
> **Platform:** [surface]
> **Timeline / Budget:** [constraints]
> **Non-negotiable requirements:** [top 3]
> **Major Risks:** [top 3]
> Is this accurate before I write?"

---

## Phase 2 Output

Write `docs/PRD-[AppName]-MVP.md` (Phase 2 sections only):

```markdown
# PRD: [AppName] MVP
**Version:** 1.0  |  **Status:** Draft — Phase 2 of 3  |  **Updated:** [Date]
**Owner:** [Name]  |  **Launch Target:** [Date]

---

## Document Health
| Check | Status |
|-------|--------|
| Problem validated with sourced evidence | ✅ / ❌ |
| Root cause labeled as hypothesis | ✅ |
| Non-goals defined | ⏳ Phase 3 |
| Success metrics are SMART | ✅ / ❌ |
| Assumptions labeled | ✅ / ❌ |
| Open questions listed | ✅ / ❌ |

---

## 1. Product Overview
- **Name:** [Name]
- **Tagline:** [Short literal promise — what it does, not how it feels]
- **MVP Goal:** [Concrete, measurable launch outcome]
- **Timeline:** [Launch target]
- **Summary:** [One paragraph — what it is and who it's for]

## 2. Why Now?
[One paragraph: What changed — market shift, technology enablement, competitor exit, regulatory
change, or timing opportunity — that makes this the right moment?
At least one fetched, sourced data point required.]

## 3. Problem Statement
[From Phase 1 research. Core pain, who has it, frequency, cost. At least one sourced data point.]

> ⚠️ **Root Cause — Hypothesis (validate before building):**

| Why | Answer | Basis |
|-----|--------|-------|
| 1st | ... | ... |
| 2nd | ... | ... |
| 3rd | ... | ... |
| 4th | ... | ... |
| 5th — Root Cause Hypothesis | ... | ... |

**Validation method:** [How we confirm this hypothesis before building starts]

## 4. Solution
[One paragraph. What it is, how it works, the specific mechanism by which it solves the root cause.]

**Root Cause → Solution Mapping:**
| Root Cause (hypothesis) | How This Solution Directly Addresses It |
|------------------------|----------------------------------------|
| [From table above] | [Specific mechanism — not vague] |

## 5. Target User
- **Who exactly:** [Specific — "bootstrapped SaaS founder <$5k MRR on Stripe" not "developer"]
- **Job Story:** *"When [situation], I want to [motivation], so I can [outcome]."*
- **Where they are:** [Reddit/r/X, IndieHackers, HN, Discord — with fetched source]
- **Current solution:** [What they use today and why it falls short]

## 6. User Journey
> [Specific user] has [problem]. They find [Product] via [specific entry point].
> They [core action]. They receive [specific value]. They return because [retention hook].

## 7. Audience Fit & User Alignment
[Why this slots into their existing workflow — not creates a new behavior from scratch]

## 8. Competitive Advantage
[How it specifically beats the top alternative — fetched source links and real data.
Not "better UX" — an actual measurable differentiator.]

## 9. Success Metrics (SMART — all 5 criteria verified)

| Metric | Target | Timeframe | Measurement Method |
|--------|--------|-----------|-------------------|
| **Primary:** [Metric] | [Number] | 30 / 90 days | [Specific tool / method] |
| **Guardrail 1:** [Metric] | ≥/≤ [threshold] | Ongoing | [Tool / method] |
| **Guardrail 2:** [Metric] | ≥/≤ [threshold] | Ongoing | [Tool / method] |

> **Qualitative signal:** [The specific user behavior or quote that proves value is real]

## 10. Assumptions & Open Questions
> [ASSUMPTION] = believed but unproven. [OPEN] = undecided — needs decision by [date].

- [ASSUMPTION] Users already have [X]
- [ASSUMPTION] Primary acquisition channel will be [Y]
- [OPEN] [Decision needed — by when]

## 11. Business Viability

| Item | Detail | Source |
|------|--------|--------|
| Monthly cost at MVP (0–100 users) | $X/mo | [fetched pricing links] |
| Monthly cost at growth (1k users) | $X/mo | [fetched pricing links] |
| Monetization model | [Freemium / $X/mo / one-time / etc.] | |
| Break-even | [Users or revenue needed] | |

## 12. Platform & Constraints
- **Platform:** [Web / Mobile / Both]
- **Timeline:** [X days/weeks/months]
- **Budget:** [Free tier only / Up to $X/mo]
- **Performance:** [e.g., "Page load < 2s on 4G"]
- **Security:** [e.g., "JWT auth on all API endpoints"]
- **Accessibility:** [e.g., "WCAG 2.1 AA minimum"]
- **Compliance:** [GDPR / HIPAA / N/A]
- **Other non-negotiables:** [From Q16]

## 13. Risk Assessment
| Risk | Type | Likelihood | Impact | MVP Mitigation |
|------|------|------------|--------|----------------|
| ... | Technical / Market / Safety / Execution | H/M/L | H/M/L | ... |

---

## MVP Feature Requirements
> ⏳ Completed in Phase 3 after Feature Funnel and V2 scope are locked.

## Non-Goals (Out of Scope)
> ⏳ Completed in Phase 3 after V2 features are formally deferred.

## Edge Cases & Error States
> ⏳ Completed in Phase 3 alongside feature acceptance criteria.

## Definition of Done
> ⏳ Completed after Phase 3 and Phase 4.

---

## Deep Dive: Source Analysis
[Every source fetched and read during Phase 2.]
- **Source 1:** [URL] — **Key Insights:** [Dense synthesis of what was on the page]
- [Continue for all sources...]

---

## Appendix: Raw Research Log
[All raw quotes, stats, excerpts from fetched sources]
- [Quote/Stat] (Source: [fetched link])
```

---

## 🛑 Phase 2 Gate — Before Moving On

**Fact-check pass:**
Spawn a Fact-Checker subagent (or perform this yourself) to re-fetch every URL in the Phase 2 sections.
- ✅ `[VERIFIED]` for passes
- ❌ `[FACT CHECK FAILED: reason]` for failures

**Alignment-check pass:**
Spawn an Alignment-Checker subagent (or perform this yourself) to verify the Phase 2 solution directly addresses the Phase 1 root cause hypothesis.
- ⚠️ `[ALIGNMENT WARNING: reason]` if solution drifts from root cause

Fix all `❌` and `⚠️` blocks before presenting. Log what was fixed and why in the Appendix.

**User approval:**
> "Phase 2 complete — fact-checked and alignment-verified. Does this capture your solution accurately?
> Approve to continue to Phase 3: Feature Funnel."

---

## ➡️ After Phase 2 Approval

Read the Phase 3 file and begin immediately:
> `Read: c:\Users\henry\Desktop\Agentic workflows\.agents\skills\vibe-psi\phases\p3-features.md`
