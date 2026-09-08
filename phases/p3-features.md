# PSI — Risk-matched learning prototype

Only LEARNING_PROTOTYPE may scope an MVP or choose prototype form. Start from
the approved solution and its riskiest remaining assumption, not a feature list.

## Design the test before producing the artifact

Select the cheapest credible form: interview, observation, paper/task simulation,
concierge service, process change, landing-page test, clickable interface, CLI
spike, hardware mockup, or external coded prototype. Explain why its fidelity
answers the uncertainty. No compulsory HTML or fixed variant count. A risky
problem hypothesis may instead require returning to discovery.

Write `docs/experiment-v1.json`, `kind: experiment`, depending on solution:
- hypothesis and causal alternatives; what the test can/cannot establish;
- participant eligibility/recruitment and consent; personal N-of-1 where relevant;
- task/context, baseline/comparison, observation method and missing-data handling;
- primary outcome, guardrails, threshold rationale, sample rationale, timeframe;
- success, failure, inconclusive and stopping rules committed before observations;
- budget/time, safety/privacy constraints and required external approvals;
- prototype form/fidelity and optional design direction;
- canonical `v1_feature_ids`, requirements mapped to problem/outcome and test;
- Given/When/Then criteria including failures, dependencies and non-goals;
- V2 parking lot and revisit conditions, excluded from the current test.

For a non-feature experiment use an empty feature-ID set and describe test tasks.
Aesthetic direction comes before visual generation if relevant. Generate only
what the decision requires. Use inert text, escaping/textContent, no remote
assets or executable source copy; sandbox scripted prototypes. Do not auto-open
untrusted HTML. Scope or cost changes require a new version and review.

## Gate and execution boundary

A critic checks risk-to-test fit, outcome measurement, participant fit, threshold
integrity, scope leakage and safety. Preference for a mockup is not adoption.
Structural PASS cannot prove sample quality or experiment adequacy.

Reviewed, explicitly approved experiment:
- no application build needed → READY_FOR_EXPERIMENT → REAL_USER_VALIDATION;
- external builder needed → MVP_EXPERIMENT_HANDOFF (load p5-build.md; optional
  p4-techspec.md only when engineering detail reduces a relevant uncertainty).

READY_FOR_EXPERIMENT authorizes the defined plan, not blanket outreach, payment,
real-user exposure or live data access. Obtain action-specific approval. Do not
claim a test ran because its checklist exists. Wait for actual observations.
