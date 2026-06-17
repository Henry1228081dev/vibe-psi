# PSI Phase 3: Feature Funnel & PRD Completion

**Goal:** Filter all possible ideas into a locked V1 feature list through iterative visual
prototyping. Complete the PRD document. Formally document V2 scope.

**Phase 3 completes the PRD** — Non-Goals, MVP Feature Requirements, Edge Cases, and Definition
of Done are all finalized here, not before.

**Output files:**
- `docs/PRD-[AppName]-MVP.md` — completed (status changes from "Phase 2 of 3" → "Final")
- `docs/V2-Features-[AppName].md` — new
- `docs/prototypes/01-feature-showcase.html` through `04-*.html`

---

## Step 3.1 — Ideation

Ask: *"List every feature you can think of — useful, cool, or speculative. Don't filter yet."*

> Also suggest features based on Phase 1 problem research and Phase 2 solution. Pull ideas from
> competitor feature lists found in Phase 1. Present your suggestions alongside the user's list.
> Nothing is off-limits at this stage — filter happens next.

---

## Step 3.2 — Prototype 1: Feature Showcase

After collecting all ideated features, generate a standalone HTML prototype.

**Save to:** `docs/prototypes/01-feature-showcase.html`

Requirements:
- Display every ideated feature as a visual card or panel
- Feature name, one-line description, visual icon or tag per card
- Visually flag features most aligned with Phase 2 value prop (different color/border/badge)
- Single self-contained HTML/CSS/JS file — no external CDN dependencies
- Polished and readable — not a rough wireframe. Realistic copy using PRD context.

Then ask (one at a time):

1. *"Looking at this overview — which features are **primary**? Meaning the app is completely
   useless without them. These are your non-negotiables."*
2. *"Which features are **secondary**? They add real value but the core works without them."*

---

## Step 3.3 — Refinement & V2 Gate

Group features into logical MVP stacks based on the primary/secondary split. Present groupings. Ask:

- *"Do these groupings make sense? What would you add or move?"*
- *"What features are you intentionally saving for V2? Name them — we'll formally document them so they're not lost."*

Create `docs/V2-Features-[AppName].md`:

```markdown
# V2+ Features: [AppName]

> These features were intentionally excluded from MVP scope. Documented here so they're not
> lost and can be properly planned for future versions.

## Quality-of-Life Improvements (V2)
- **[Feature]:** [What it is] — *Why deferred: [reason]*

## Power User Features (V2/V3)
- **[Feature]:** [What it is] — *Why deferred: [reason]*

## Long-Term Vision (V3+)
- **[Feature]:** [What it is] — *Why deferred: [reason]*

## Revisit Conditions
[Under what circumstances should any of these move to V1? e.g., "If retention drops below X%
after launch, prioritize [Feature] for V1.1"]
```

---

## Step 3.4 — Final V1 Feature List Lock

Lock in 3–4 Must-Have V1 features based on:
- User's stated primary features
- Alignment with Phase 2 solution and root cause hypothesis
- Feasibility within stated timeline and budget

> Cross-check: If any chosen feature contradicts or doesn't directly support the Phase 2 value
> prop, flag it and ask the user to confirm they still want it.

For each final V1 feature, define using **Given-When-Then** acceptance criteria:

- **User story:** `As a [target user], I want to [action], so that [benefit].`
- **Acceptance criteria (3–5 per feature — must be testable and unambiguous):**
  - `Given [initial state], When [user action], Then [observable outcome]`
  - `Given [edge case state], When [user action], Then [graceful behavior]`
- **Success signal:** The metric, event, or behavior proving this feature works.
- **Dependencies:** Data, integrations, permissions, or other features it requires.
- **Feature non-goals:** What this specific feature will NOT do in V1.

---

## Step 3.5 — Prototypes 2, 3, 4: MVP Options

Generate 3 distinct HTML MVP prototypes showing different choices about which secondary features to include in V1:

**Save to:**
- `docs/prototypes/02-mvp-option-a.html`
- `docs/prototypes/03-mvp-option-b.html`
- `docs/prototypes/04-mvp-option-c.html`

Each prototype must:
- Be a fully functional HTML/CSS/JS single-file mockup of the actual MVP UI
- Include all primary (Must-Have) features
- Include a *different* selection of secondary features so the user can compare tradeoffs
- Reflect the aesthetic vibe from Step 3.6 below
- Use realistic copy from the PRD — no "Lorem ipsum"

Show all 3 and ask:
> *"Which of these best captures the V1 you want to ship? Or should I adjust — add something
> from one, remove something from another?"*

Keep iterating until the user explicitly approves. Each iteration = a new numbered prototype file.
Confirm the chosen design aligns with Phase 2 solution before closing.

---

## Step 3.6 — Aesthetic Direction

Ask: *"Describe the vibe in 3–5 words. Examples: 'clean and fast', 'bold and dramatic', 'friendly and approachable'."*

> Interpret into a specific color palette and font choice for the prototypes.
> Keep it lightweight — the goal is a useful product that solves a real problem, not a brand exercise.

---

## Phase 3 Output — Complete the PRD

Update the PRD status header from "Phase 2 of 3" to "Final". Append these sections:

```markdown
---
*PRD Status updated: Phase 3 complete — document finalized.*

## Feature Funnel

### Ideation — All Ideas Considered
- [Full list from brainstorming]

### Primary Features — Non-Negotiable (V1 is useless without these)
1. **[Feature]:** [Why it's essential]

### Secondary Features — Add Value (evaluated for V1)
1. **[Feature]:** [Why beneficial but not blocking]

### Final V1 Feature List — Must-Have Only
1. **[Feature]:** [Description + link back to value prop]

---

## MVP Feature Requirements

> ⚠️ If a feature is not in this table, it does not get built. Reference this before every
> new build task. Full V2+ features live in `docs/V2-Features-[AppName].md`.

| Feature | Priority | User Story | Acceptance Criteria (Given-When-Then) | Success Signal | Dependencies | Feature Non-Goals |
|---------|----------|------------|--------------------------------------|----------------|--------------|-------------------|
| [Feature] | Must-Have | As a..., I want..., so that... | Given..., When..., Then... | [Observable event/metric] | [What it needs] | [What it won't do] |

---

## Non-Goals — Explicitly Out of Scope

> Deliberate decisions. If it's not in the Must-Have table, it's deferred.
> Check this list whenever a new feature request comes up during building.
> Full V2 scope documented in `docs/V2-Features-[AppName].md`.

- ❌ [Feature/Capability] — *Why deferred: [one-line reason]*
- ❌ [Feature/Capability] — *Why deferred: [one-line reason]*

---

## Edge Cases & Error States

> Must be designed for — not discovered in production.

- **If [user tries X before completing Y]:** [Expected behavior or message]
- **If [API or external service fails]:** [Fallback behavior]
- **If [data is empty or missing]:** [Graceful empty state]
- **If [user hits a permission boundary]:** [Expected behavior]
- [Add all edge cases surfaced during feature definition]

---

## Design Direction
- **Vibe:** "[User's 3–5 word description]"
- **Interpretation:** [Color scheme, font, layout in one line]
- **Chosen Prototype:** `docs/prototypes/0X-mvp-option-[chosen].html`
- **Secondary features included in V1:** [list]
- **Secondary features deferred to V2:** [list]

---

## Definition of Done — Launch Checklist
- [ ] Every Must-Have feature passes all its Given-When-Then acceptance criteria
- [ ] Primary success metric is instrumented and measurable (tool configured)
- [ ] Core user journey works end-to-end without errors
- [ ] Non-Goals have not been built (audit against Non-Goals table)
- [ ] All edge cases are handled — no broken or dead-end states
- [ ] Budget and timeline constraints respected
- [ ] At least 3 real target users have tested the core flow
- [ ] V2 features are documented in `docs/V2-Features-[AppName].md` — not in V1
```

Also update Document Health at the top of the PRD:
- Non-goals defined → ✅
- Edge cases designed for → ✅

---

## 🛑 Phase 3 Gate — Before Moving On

**Alignment-check pass:**
Spawn an Alignment-Checker (or perform this yourself) to audit the final MVP feature list against the Phase 1 root cause hypothesis and Phase 2 solution. Inject `⚠️ [ALIGNMENT WARNING]` for any feature that doesn't directly solve the root cause. Fix or justify all flags, remove all blocks.

**User approval:**
> "PRD is complete and alignment-verified.
> Feature list locked. Non-Goals locked. V2 features documented.
> Does this match what you want to build?
> Approve and I'll generate the full Engineering Spec."

---

## ➡️ After Phase 3 Approval

Read the Phase 4 file and begin immediately:
> `Read: c:\Users\henry\Desktop\Agentic workflows\.agents\skills\vibe-psi\phases\p4-techspec.md`
