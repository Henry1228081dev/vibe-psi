# PSI Phase 5: Build Plan — AGENTS.md

**Goal:** Generate the AGENTS.md file that hands the fully validated product off to code.
This is the final PSI output. After this, building begins.

**Output file:** `AGENTS.md` (in the project root)

---

## What to Produce

Generate `AGENTS.md` using all context from Phases 1–4:

```markdown
# AGENTS.md — [AppName] Build Plan

## Project Overview
[One paragraph summary from the PRD — what it is, who it's for, what problem it solves,
and what the MVP launch goal is.]

## Mission
Build [AppName] — a product that solves [root cause hypothesis] for [target user].
The product is worth building because [one-sentence evidence summary from Phase 1 verdict].

## Current Phase
Phase 1: Foundation — IN PROGRESS

## Key Documents (read these before every session)
- Problem research: `docs/research-[AppName].md`
- Full PRD (features, non-goals, acceptance criteria, DoD): `docs/PRD-[AppName]-MVP.md`
- V2 features (DO NOT BUILD in V1): `docs/V2-Features-[AppName].md`
- Engineering spec (schema, endpoints, NFRs, deployment): `docs/TechDesign-[AppName]-MVP.md`
- MVP prototype reference: `docs/prototypes/0X-mvp-option-[chosen].html`

---

## Phases

### Phase 1: Foundation
**Goal:** Working skeleton — project setup, auth, database, scaffolding.

**Tasks:**
- [ ] Run `npx -y [framework]@latest --help`, confirm flags, then initialize in `./`
- [ ] Create `.gitignore` — add `.env.local` before first commit
- [ ] Configure all environment variables from TechDesign `.env.local` checklist
- [ ] Apply database schema migrations (from TechDesign schema)
- [ ] Set up auth flow (sign up, sign in, sign out, token refresh)
- [ ] Configure error monitoring ([Provider from TechDesign])
- [ ] Verify app runs locally

**Done when:** App starts locally, auth works end-to-end, DB is connected and migrations applied,
errors are captured in monitoring.

---

### Phase 2: Core Features
**Goal:** Build every Must-Have feature. Test each one before moving to the next.

**For each feature:**
1. Build the feature
2. Run its Given-When-Then acceptance criteria from the PRD — all must pass
3. Test edge cases defined in the PRD Edge Cases section
4. Only then move to the next feature

**Tasks:**
- [ ] [Primary Feature 1] — verify all acceptance criteria before next task
- [ ] [Primary Feature 2] — verify all acceptance criteria before next task
- [ ] [Primary Feature 3] — verify all acceptance criteria before next task
- [ ] All edge cases from PRD Edge Cases section handled

**Done when:** Core user journey works end-to-end. Every Must-Have feature passes its
Given-When-Then acceptance criteria.

---

### Phase 3: Secondary Features, Polish & Launch
**Goal:** Add approved secondary features, implement design direction, instrument metrics, ship.

**Tasks:**
- [ ] [Secondary Feature 1 — if approved for V1]
- [ ] [Secondary Feature 2 — if approved for V1]
- [ ] Implement aesthetic direction: "[vibe]" — [color/font/style from PRD Design Direction]
- [ ] Build landing page (value prop headline + CTA + pricing)
- [ ] Instrument success metrics: configure [Tool] to track [specific events]
- [ ] Complete deployment checklist from TechDesign
- [ ] Run full Definition of Done checklist from PRD
- [ ] Manual end-to-end test in production environment

**Done when:** Production build passes all DoD checklist items. MVP is live. Metrics are recording.

---

## Non-Negotiable Build Rules

- **One task at a time.** Run acceptance criteria after every feature before starting the next.
- **Test in production** before announcing the phase is done.
- **Never modify `.env.local`** directly — confirm with user first.
- **No premature optimization.** Ship over perfect. Performance can be tuned post-launch.
- **V2 scope is locked.** Before building anything, check: is this feature in the PRD Must-Have
  table? If not, check `docs/V2-Features-[AppName].md`. If it's in V2, do not build it in V1.
- **If scope creep appears:** Reference the PRD Non-Goals table. If someone requests a deferred
  feature, acknowledge it and add it to `docs/V2-Features-[AppName].md` if not already there.
- **If something breaks a fact-check or tool call:** Log what failed and why in the relevant
  doc's Appendix before continuing. Never silently skip failures.
- **If a framework CLI has changed:** Run `--help` first, read the output, then use the correct
  flags. Do not assume flags from memory.

---

## Success Condition
[AppName] is complete when:
1. Every Must-Have feature from the PRD passes its acceptance criteria
2. The primary success metric ([metric]) is being measured by [tool]
3. The core user journey works end-to-end in production
4. The Definition of Done checklist in the PRD is fully checked off
5. V2 features are NOT built into V1
```

---

## 🛑 Phase 5 Gate — PSI Handoff Complete

Present `AGENTS.md` to the user:

> "All 5 phases are complete.
>
> You have:
> - ✅ A validated problem worth solving (`docs/research-[AppName].md`)
> - ✅ A solution designed to solve it (`docs/PRD-[AppName]-MVP.md`)
> - ✅ A locked V1 feature list with Given-When-Then acceptance criteria
> - ✅ V2 scope documented and locked out (`docs/V2-Features-[AppName].md`)
> - ✅ A full engineering spec (`docs/TechDesign-[AppName]-MVP.md`)
> - ✅ A build plan (`AGENTS.md`)
>
> The next message you send to a coding agent should say:
> *'Read AGENTS.md and start Phase 1.'*
>
> Good luck. Now go build the thing."
