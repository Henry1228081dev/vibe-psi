# PSI — Solution discovery

Enter only after a current approved problem artifact and a successful transition
check to SOLUTION_DISCOVERY. Import that exact canonical statement and its hash;
do not silently rewrite it in a PRD. A change to it requires new problem review
and invalidates the dependent solution approval.

Compare the user's proposed mechanism against credible alternatives, including
the current workaround/status quo and doing nothing when applicable. Seek at
least two plausible alternative mechanisms for a consequential decision; justify
an exception rather than inventing competitors. Match each to causal hypotheses,
expected outcome, adoption behavior, switching cost, feasibility, maintenance,
privacy/safety, constraints, contradictions and a falsification condition.

Use external research for checkable consequential claims. If access fails, name
the blocker and stay in discovery; do not replace findings with plausible quotes.
Do not demand exact infrastructure prices before the service choices are known.

## Separate assessments

Record four independent assessments with evidence IDs, limits and unknowns:
problem importance; solution mechanism; purpose-specific viability; observed
outcome. These are not sequential rungs that automatically upgrade one another.

- Personal: relief, recurring usefulness, burden, privacy and cost.
- Internal/team: baseline workflow, owner, access, adoption and operational cost.
- Learning/public-interest: learning/impact goal, resources, safety and timebox.
- Commercial: user/champion/buyer, budget/authority, acquisition access, switching,
  commitment signals, revenue and full delivery/sales/support cost assumptions.
  Record channel and unit-economics unknowns. Enthusiasm is not payment; a letter
  of intent is conditional, not equivalent to revenue. Test distribution first
  when it is the riskiest assumption. These are not gates for unrelated purposes.

The best next move is the cheapest safe test that could overturn the mechanism,
not necessarily software. Define an outcome independent of app usage, a baseline,
and plausible alternative explanations before selecting the experiment.

## Output and gate

Write `docs/solution-v1.json`, `kind: solution`, depending on the approved
problem hash. Include comparison, four assessments, recommendation, limitations,
and `verdict: WORTH_TESTING | RESEARCH_MORE | PIVOT | STOP`.

WORTH_TESTING means a bounded experiment merits its cost. It does not require
already-proven commercial demand: the experiment may test exactly that unknown.
Missing safety clearance cannot be waived by an enthusiasm/learning label.

Review causal fit, alternatives, access, negative evidence and relevance to the
chosen purpose. A weak mechanism returns RESEARCH_MORE in SOLUTION_DISCOVERY;
preserve the supported problem. Keep warning/resolution history. Explicit
approval and a passing check permit LEARNING_PROTOTYPE, not automatic building.
