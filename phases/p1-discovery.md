# PSI — Founder brief and problem discovery

Read the installed root SKILL.md and references/evidence-safety.md first.
No solution, feature, architecture, or MVP recommendation is legal here.

## FOUNDER_BRIEF

Capture purpose, affected person, recent incident, desired outcome, constraints,
workaround, origin of belief, proposed solution, and unknowns. For opportunity
discovery, investigate accessible audiences and repeated workflows; do not ask
the user to invent pain. Capture money/time ceilings, skills, access and risk
only to the extent relevant to their purpose. A no-code workspace is normal.

Use independent question batches if requested. An experiential question needs
no preliminary browsing. Do not prime the user's incident with a preferred
causal explanation. Store the proposed mechanism separately. A provisional
statement is a working hypothesis, not a market verdict.

Write `docs/brief-v1.json` using the common artifact envelope in the state
contract. Review for accurate intent capture and get explicit approval before
PROBLEM_DISCOVERY. If the user disagrees, revise rather than relabel agreement.

## PROBLEM_DISCOVERY

1. Define the decision and the critical unknowns. Build a revisable question
   tree: who/when → observed difficulty → consequence → possible causes →
   current response → why it persists → intervention points.
2. Investigate external claims that could change the decision. Open actual
   sources and triangulate independent evidence; seek praise of alternatives
   as well as complaints. Use official sources for features/pricing, original
   data for prevalence, user accounts for lived experience, and appropriate
   research for causal mechanisms. Source counts are not stopping criteria.
3. Compare at least two plausible causes for consequential causal conclusions;
   if only one is plausible, justify that limit and seek counterevidence.
   Record support, contradiction, prediction, **falsifier**, and cheapest
   discriminating test for each. Five Whys is optional, not five required facts.
4. Stop when the next decision is justified at its risk level or additional
   accessible research cannot resolve the blocker. Record missing access,
   uncertainty and next observation/recruitment steps. UNKNOWN is allowed;
   consequential unknowns may still require RESEARCH_MORE, not a positive gate.
5. Rewrite the canonical **solution-independent** statement from the accumulated
   evidence. Do not preserve the first sentence merely because the user liked it.

## Canonical problem artifact

`docs/problem-v1.json` contains `project_id`, `kind: problem`, `statement`,
`evidence`, `hypotheses`, `verdict`, and the research synthesis. Register it with
its approved brief dependency. Version new revisions; never overwrite history.

Required `statement` dimensions (the CLI checks completeness/provenance):
- `user`: specific enough to recruit or the identified personal user.
- `situation`: actual trigger/context.
- `desired_progress`: what they want to accomplish.
- `difficulty`: observable behavior or failure, not a missing technology.
- `workaround`: present response, including doing nothing.
- `frequency` and `severity`: sourced, or explicitly UNKNOWN; no invented rates.
- `consequence`: meaningful cost, risk, wellbeing, time or other purpose outcome.
- `counterevidence`: disagreement and strongest alternative interpretation.
- `falsifier`: what would change or reject this framing.

Each dimension is an object with `text`, `status` (SUPPORTED, ASSUMPTION,
UNKNOWN, CONFLICTING), and `evidence_ids`. Supported/conflicting clauses need
resolvable evidence IDs. The state contract specifies the evidence records.

Natural rendering: “When [user] is in [situation] trying to [progress], they
experience [difficulty], respond with [workaround], and suffer [consequence].
Evidence supports [limited inference]; [uncertainty] remains.” Do not force
awkward prose. Keep root causes and the proposed solution outside this statement.

## Teaching checkpoint and review

Return a concise briefing:
- What I found.
- Why it matters.
- **What it does not prove**.
- Alternative explanation.
- **What changed** in the problem map.
- Next question/test, only if it changes the next decision.

A semantic critic checks specific user/context, solution contamination, clause
support, sampling, falsifiability, founder bias, conflicts and the investment
recommendation. The CLI cannot determine these from prose. Present the revised
statement for intent confirmation separately from its evidence verdict.

Legal verdicts:
- WORTH_INVESTIGATING: enough to compare mechanisms, not proof of demand.
- RESEARCH_MORE: stay here and name the next informative action.
- PIVOT: return to FOUNDER_BRIEF with changed framing/segment.
- STOP: stop the cycle.

Only reviewed, approved WORTH_INVESTIGATING permits SOLUTION_DISCOVERY. A user
saying “continue anyway” does not change the evidence label or bypass the guard.
An explicitly requested speculative build belongs to a separate builder task;
record that PSI's gate was not passed. Desk research never proves paid demand.
