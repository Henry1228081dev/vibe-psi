# PSI Phase 1: Problem Discovery

**Goal:** Prove the problem is real and worth solving before touching a solution.
Run the 5 Whys root-cause analysis. Build an evidence-backed research document.
If the problem doesn't hold up, say so and propose a pivot — this is the best outcome for a bad idea.

**Output file:** `docs/research-[AppName].md`

---

## Research Protocol (Phase 1 Standard)

Before every question: search, fetch, and synthesize real evidence first. Minimum 3 sources opened and read via WebFetch per question turn. Minimum 10 sources across the full phase before writing the output document.

**What to search:**
- Reddit threads (subreddits where target users hang out)
- G2, Capterra, Trustpilot, Product Hunt reviews and comments
- IndieHackers, HackerNews "Ask HN" threads
- Competitor pricing pages, feature lists, changelog
- Industry reports (Statista, CB Insights, a16z, YC essays)

**Evidence Ledger (maintain throughout):**

| Claim / Decision | Source URL | Source Type | What the Source Actually Says | Product Impact |
|-----------------|-----------|-------------|------------------------------|---------------|
| ... | ... | ... | ... | ... |

**Back-and-Forth Protocol:** After each research finding, present it and discuss naturally before locking the answer. Do not immediately force the next question. Let the conversation land.

---

## Interview Rules

- **One question at a time.** Wait for the user's response before moving on. (SKILL OVERRIDE active.)
- Research before every question — never ask in a vacuum.
- Present research findings first as distinct options with your recommendation and rationale.
- If the user gives a surface-level answer, probe deeper with the next Why.
- Do not infer answers and write the doc. Every required answer must come from the user or be explicitly proposed by you and accepted.

---

## Questions — Ask in Order, One at a Time

**Q1 — The Core Problem**
> Search Reddit, Product Hunt, G2, Capterra, and IndieHackers for complaints in this idea space.
> Fetch and read at least 3 actual pages — do not rely on search snippets.
> Present real user quotes and frustrations with fetched source links. Discuss.
> Then ask: *"In one sentence — what is the core problem this solves?"*

**Q2 — 1st Why**
> *"Why does this problem occur?"*

**Q3 — 2nd Why**
> *"Why is that?"*
> (If the user reaches a compelling root cause early, skip ahead to Q6.)

**Q4 — 3rd Why**
> *"Why?"*

**Q5 — 4th Why**
> *"Why?"*

**Q6 — 5th Why — Root Cause Hypothesis**
> *"What do you believe is the ultimate root cause? We'll label this as a hypothesis — something
> to validate before building, not a verified fact."*

**Q7 — Target Audience**
> Search forums, job boards, and communities to find who is actively complaining about this problem.
> What job titles, demographics, or communities appear most? Fetch and read actual community pages.
> Present findings with fetched links. Discuss. Then ask:
> *"Who specifically has this problem? Not 'developers' — be precise: 'bootstrapped SaaS founders
> under $5k MRR on Stripe' or 'operations managers at logistics companies under 200 employees'."*

**Q8 — Existing Solutions**
> Required: Fetch actual competitor pages — pricing, features, changelogs, G2/Capterra review pages.
> For each competitor found, research and present:
> - Market position (who uses it, at what scale)
> - Pricing (real numbers from fetched pricing page)
> - Technical approach (public docs, GitHub, architecture posts)
> - User complaints (real quotes from fetched review pages)
> - Similar startups in this space with outcomes (funding, MRR, exits)
>
> Show the breakdown. Discuss. Then ask:
> *"Which of these do your target users currently rely on, and why do they fall short?"*

**Q9 — Main Consequence**
> *"What happens if this problem is left unsolved? Lost revenue, wasted time, missed opportunity — what specifically?"*

**Q10 — What Works in Existing Solutions?**
> Search G2 reviews, Product Hunt comments, and Reddit for praise of existing tools in this space.
> Fetch and read at least 2 actual review/thread pages. Summarize what users genuinely like with fetched links.
> Present findings first. Discuss. Then ask:
> *"Do you agree with what users say works well? Anything here worth preserving in your approach?"*

**Q11 — What Fails in Existing Solutions?**
> Search G2, Capterra, Reddit, IndieHackers for complaints about the top competitors.
> Fetch and read at least 2 complaint threads or review pages. Summarize the most common failure patterns.
> Present findings first. Discuss. Then ask:
> *"Do these failure patterns match what you've seen? Which one is your opening?"*

**Q12 — Quantitative Proof**
> Search for hard statistics: market size, growth rate, cost of the problem, frequency, number of affected users.
> Fetch industry reports, academic papers, credible news sources. Provide fetched links for every stat.
> If the user made market claims earlier — fact-check them here. Show what evidence actually says.
> Discuss. Then ask:
> *"Does this data match your understanding? Are there other signals proving this problem is real?"*

---

## Phase 1 Output

Only write `docs/research-[AppName].md` after **all 12 questions are answered** and the evidence ledger has at least 10 opened/read sources. If not — keep interviewing.

```markdown
# Research: [AppName]

## The Core Problem
[One-sentence summary of the pain]

## Root Cause Analysis (5 Whys)

> ⚠️ The root cause below is a **hypothesis** — not verified fact.
> Validate before building by: [e.g., interviewing 5 target users / running a landing page test]

| Why | Answer | Basis |
|-----|--------|-------|
| 1st | ... | [source or user statement] |
| 2nd | ... | ... |
| 3rd | ... | ... |
| 4th | ... | ... |
| 5th — Root Cause Hypothesis | ... | ... |

## Job Story (Outcome Frame)
> "When [situation the target user is in], I want to [what they're trying to do],
> so I can [the outcome they actually care about]."

## Target Audience
[Specific persona. Include where they congregate online — with fetched source links.]

## Existing Solutions
| Tool | Strengths | Weaknesses | Pricing | Market Position |
|------|-----------|------------|---------|-----------------|
| ... | ... | ... | ... (fetched link) | ... |

## Market Landscape
- **Market size:** [stat] — Source: [fetched link]
- **Growth trend:** [stat] — Source: [fetched link]
- **Competitor pricing range:** [$X–$Y/mo]
- **Similar successful projects:** [Name — outcome] — Source: [fetched link]
- **Key failure patterns in existing solutions:** [from fetched reviews]

## Main Consequence of Inaction
[What happens if unsolved — with evidence]

## Evidence
- **What works in existing solutions:** ... (Source: [fetched link])
- **What fails:** ... (Source: [fetched link])
- **Quantitative proof:** ... (Source: [fetched link])

## Deep Dive: Source Analysis
[Every source fetched and read during Phase 1.]
- **Source 1:** [URL] — **Key Insights:** [Dense synthesis of what was on the page]
- **Source 2:** [URL] — **Key Insights:** ...
- [Continue for all 10+ sources]

## Verdict

**[Choose one — do not force positive if evidence doesn't support it]**

✅ **Worth pursuing because:** [1-2 sentences, specific, evidence-backed]

❌ **Not worth building in this form because:** [Evidence. What's wrong.]
   **Consider pivoting to:** [A sharper, more underserved angle the research revealed]

---

## Appendix: Raw Research Log
[All raw quotes, stats, excerpts from fetched sources — nothing lost]
- [Quote/Stat] (Source: [fetched link])
```

---

## 🛑 Phase 1 Gate — Before Moving On

**Fact-check pass:**
Spawn a Fact-Checker subagent (or perform this yourself) to re-fetch every URL in the document.

- ✅ `[VERIFIED: source matches claim]` — for passes
- ❌ `[FACT CHECK FAILED: reason]` — for failures (dead link / content mismatch / outdated data)

Fix all `❌` blocks before presenting. If a claim cannot be fixed, remove it from the document and log what was removed and why in the Appendix.

**User approval:**
> "Research is done and fact-checked.
> **Verdict: [Worth pursuing / Not worth building — state which and why in one sentence].**
> Approve to continue to Phase 2: Solution Validation."

---

## ➡️ After Phase 1 Approval

Read the Phase 2 file and begin immediately:
> `Read: c:\Users\henry\Desktop\Agentic workflows\.agents\skills\vibe-psi\phases\p2-solution.md`
