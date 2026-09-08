# PSI — Conditional technical investigation

This is an optional substep of MVP_EXPERIMENT_HANDOFF, not a compulsory product
stage. Skip with a reason for service/manual/nontechnical experiments. Do not
force frontend, database, JWT, landing page, domain or deployment onto a CLI,
hardware, personal or noncommercial problem.

For a coded experiment, derive only necessary architecture from the approved
experiment's canonical V1 IDs and measurement requirements. Compare feasible
options. Consult current official documentation for technical claims and actual
pricing for selected services. Costs remain estimates with usage assumptions,
retrieval dates, ranges, sales/support/maintenance burden where applicable.
Changing service choices invalidates dependent costs and handoff review.

Cover only relevant interfaces, data model, failure behavior, accessibility,
privacy/data flows, permissions, performance constraints and verification steps.
For safety-sensitive or regulated use, identify jurisdiction, claims, hazards,
classification and qualified-review needs. Unknown classification blocks live
data or participant exposure; desk research is not legal/medical clearance.

Store the technical section **inside the versioned handoff artifact** so its
reviewed hash covers it. Optional human-readable TechDesign is a rendering, not
an independent source of state. Label DRAFT_AWAITING_REVIEW until reviewed and
explicitly approved; never prefill Approved in a template.

PSI does not initialize frameworks, install packages, run repository scripts,
commit, deploy or production-test the generated application. Document required
capabilities and package versions only after review; execution and permission
checks belong to the chosen external builder. Never provide moving-version or
automatic-execution boilerplate as if it were approved.
