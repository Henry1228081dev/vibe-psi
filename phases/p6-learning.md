# PSI — Real observations and the next decision

REAL_USER_VALIDATION starts only with an approved experiment; external-build
paths also require an inspected return. Read the precommitted protocol before
collecting results. Do not contact participants or expose private/live data
without authorization. The founder may provide existing results; label source,
sampling limitations and protocol deviations honestly.

## Outcome artifact

Write `docs/outcome-v1.json`, `kind: outcome`, depending on experiment. Record:
participant eligibility/recruitment, consent/privacy handling, version/exposure,
context/task, observed behavior, task outcomes and baseline separately from
opinions, feature requests and founder interpretation. Include failures,
workarounds, adverse outcomes, missing data and deviations. Avoid identifying
participants unnecessarily. For external builds, cite the approved return hash
inside the artifact and verify it in the semantic review.

Compare observations to the original thresholds. Never move the goalposts to
turn failure into success. Small/convenience samples do not establish prevalence;
payment does not establish sustained usefulness; a useful prototype does not
establish safe deployment. Personal N-of-1 findings apply to that person/context.

No results → wait or RESEARCH_MORE, not fabricated validation. Inconclusive is a
legitimate result. Read-only critique checks sampling, cherry-picking, opinions
versus behavior, missingness, competing explanations and justified inferences.

## Decision and learning loop

Review and approve outcome → DECISION_ITERATION. Write `docs/decision-v1.json`,
`kind: decision`, depending on outcome; record rationale, all four assessments,
uncertainties, what the user learned, next test and `next_state`:
- ITERATE_SOLUTION → SOLUTION_DISCOVERY.
- ITERATE_PROTOTYPE → LEARNING_PROTOTYPE.
- REBUILD_HANDOFF → MVP_EXPERIMENT_HANDOFF.
- PIVOT → FOUNDER_BRIEF.
- STOP → STOP.
- GRADUATE → GRADUATE, only with outcome-based justification appropriate to purpose.

INCONCLUSIVE normally chooses another investigation, not GRADUATE. Unresolved
safety blockers forbid exposure even if a product outcome improved. Preserve
previous versions and review findings; remove superseded active registry entries
only after archiving their metadata/history. Rework retains valid upstream
findings. V2 promotion requires a new reviewed experiment/scope, never a hidden
addition to the builder's tasks. Explain what changed, not just which doc exists.
