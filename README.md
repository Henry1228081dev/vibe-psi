# PSI: Finding a Problem Worth Solving to Build a Solution Worth Using.

> **This is not a PRD generator.** It's a co-founder skill.
> The PRD, prototypes, and engineering spec are outputs of the process — not the goal.



## What PSI Does

PSI walks you through 5 gated phases to validate that your idea is worth building before a single line of code is written. It kills bad ideas early and turns good ones into a fully engineered, ready-to-build spec.

**Mission:** Stop founders from wasting months building things nobody wants.

**Style:** Sharp co-founder. Direct, research-backed, honest. Not a yes-machine. If the evidence shows the idea is weak, PSI says so and proposes a sharper angle.



## How to Trigger

Say any of:
- *"help me build [idea]"*
- *"is this worth building?"*
- *"validate my idea"*
- *"write a PRD"*
- *"new SaaS / MVP / project"*
- *"start coding"*
- *"vibe / psi guide / product guide"*

PSI auto-resumes from wherever you left off by scanning for existing docs in your project.



## The 5 Phases

| # | Phase | What Happens | Output File |
|---|-------|-------------|-------------|
| 1 | **Problem Discovery** | 5 Whys + 12 research questions. Proves the problem is real and worth solving. Can kill the idea here — that's a win. | `docs/research-[App].md` |
| 2 | **Solution Validation** | 19 questions. Validates the proposed solution actually solves the Phase 1 root cause. Writes partial PRD. | `docs/PRD-[App]-MVP.md` (partial) |
| 3 | **Feature Funnel** | Ideation → prototypes → Given-When-Then acceptance criteria → lock V1 → document V2. Completes the PRD. | `docs/PRD-[App]-MVP.md` (final) + `docs/V2-Features-[App].md` + `docs/prototypes/` |
| 4 | **Engineering Spec** | Full tech design: schema, API endpoints, NFRs, deployment checklist, rollback plan, cost estimate. | `docs/TechDesign-[App]-MVP.md` |
| 5 | **Build Plan** | AGENTS.md handoff to a coding agent. Phased tasks, acceptance criteria gates, V2 lockout rules. | `AGENTS.md` |

Each phase is gated — you must explicitly approve before the next begins.



## Skill Folder Structure

```
vibe-psi/
│
├── SKILL.md                  ← Orchestrator. Loaded by agent at trigger.
│                               Detects phase state, routes to correct phase file.
│                               Contains: persona, 5 core rules, routing table,
│                               session continuity, output file map.
│
├── README.md                 ← This file.
│
└── phases/
    ├── p1-discovery.md       ← Phase 1: 5 Whys, 12 interview questions,
    │                           research doc template, fact-check gate.
    │
    ├── p2-solution.md        ← Phase 2: 19 validation questions, SMART metric
    │                           check, partial PRD template, dual gate.
    │
    ├── p3-features.md        ← Phase 3: Feature ideation, 4 HTML prototypes,
    │                           Given-When-Then ACs, V2 doc, PRD completion
    │                           (Non-Goals, Edge Cases, Definition of Done).
    │
    ├── p4-techspec.md        ← Phase 4: Engineering spec, NFR table,
    │                           deployment checklist, rollback plan.
    │
    └── p5-build.md           ← Phase 5: AGENTS.md template + final handoff.
```

**How it loads:** `SKILL.md` is ~180 lines and always in context. Phase files (~200–300 lines each) are loaded on demand via `Read` tool call — only the active phase is in context at any time. This prevents context rot from 1,000+ lines of instructions competing for attention.



## Project Output Folder Structure

When PSI runs in your project, it automatically creates the required folder structure (e.g., ensuring `docs/` and `docs/prototypes/` exist) and writes these files:

```
your-project/
│
├── AGENTS.md                          ← Phase 5 output. Handoff to coding agent.
│
└── docs/
    ├── research-[AppName].md          ← Phase 1 output. Problem validated.
    │
    ├── PRD-[AppName]-MVP.md           ← Phase 2–3 output. Full product spec.
    │                                    Sections: Overview, Why Now, Problem,
    │                                    Solution, Target User, User Journey,
    │                                    Success Metrics (SMART), Assumptions,
    │                                    Business Viability, Constraints, Risks,
    │                                    MVP Feature Requirements (Given-When-Then),
    │                                    Non-Goals, Edge Cases, Definition of Done.
    │
    ├── V2-Features-[AppName].md       ← Phase 3 output. Deferred features,
    │                                    documented and locked out of V1.
    │
    ├── TechDesign-[AppName]-MVP.md    ← Phase 4 output. Stack, schema, endpoints,
    │                                    NFRs, deployment checklist, cost estimate.
    │
    └── prototypes/
        ├── 01-feature-showcase.html   ← All ideated features as visual cards
        ├── 02-mvp-option-a.html       ← MVP option: secondary feature set A
        ├── 03-mvp-option-b.html       ← MVP option: secondary feature set B
        └── 04-mvp-option-c.html       ← MVP option: secondary feature set C
```


## Key Behaviours

| Behaviour | What It Means |
|-----------|--------------|
| **One question at a time** | Phase 1 & 2 run single-question interviews (AGENTS.md batch rule overridden) |
| **Research before every question** | Agent fetches real sources, presents findings, discusses — then asks |
| **Root cause = hypothesis** | 5 Whys output is always labeled as a hypothesis to validate, not a verified fact |
| **Kill path exists** | Phase 1 verdict has two options: ✅ worth pursuing OR ❌ not worth building (with pivot suggestion) |
| **PRD complete only after Phase 3** | Non-Goals, Edge Cases, DoD are intentionally written after features are locked |
| **V2 is formally documented** | Every deferred feature goes into `docs/V2-Features-[App].md` — never just dropped |
| **Given-When-Then ACs** | Every V1 feature has testable acceptance criteria, not vague bullets |
| **SMART metrics enforced** | Every success metric is validated against all 5 SMART criteria before locking |
| **Fact-check + alignment-check at every gate** | Background pass before each phase closes |



## Related Skills

These sibling skills handle individual phases if you want to use them standalone:

| Skill | What it does |
|-------|-------------|
| `vibe-research` | Standalone market research |
| `vibe-prd` | Standalone PRD generation |
| `vibe-techdesign` | Standalone technical design doc |
| `vibe-agents` | Standalone AGENTS.md build plan |
| `vibe-build` | Standalone build execution |

PSI orchestrates all of them in sequence, with validation gates between each.

---

*Made with love by taha.u*  
*Credits to /vibe-prd creators and its skill set for heavily inspiring this workflow.*
