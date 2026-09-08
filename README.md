# PSI: Find a problem worth solving. Test a solution worth using.

**A co-founder skill, not a PRD generator.** PSI helps a user understand a problem,
compare explanations and mechanisms, and make the smallest justified investment.
It supports personal problems, commercial opportunity discovery, internal work,
learning and public-interest goals. Research can reduce uncertainty; it cannot
guarantee demand, safety, commercial success or product-market fit.

## Use it

Explicitly select `vibe-psi` and say “help me understand this problem”, “is this
worth building?”, or “help me find a problem in this audience”. A proposed app is
recorded as a hypothesis, not permission to jump to features. Independent
questions can be batched; unknown answers trigger investigation rather than guesses.

Install a reviewed checkout in your host's skill directory, with the folder name
`vibe-psi`. For a local development checkout, using GitHub CLI:

```sh
gh repo clone Henry1228081dev/vibe-psi .agents/skills/vibe-psi
```

Review the commit you install; this command follows the default branch and is
not an integrity-pinned release installer. No machine-specific path edits are
needed. Phase files resolve relative to the loaded SKILL.md; output resolves
relative to the **separately selected product root**. Global installations use
the same layout under the host's documented global skill path.

Python 3.11+ enables the included offline preflight. File tools are required;
external research needs search and page retrieval. An independent reviewer is
optional with an explicitly labeled self-review fallback. Host capability and
permission checks come first. Without execution support, PSI cannot claim
machine-checked transitions. A paste-only invocation is advisory, not checked.

## The learning loop

1. Orient safely; capture the user's purpose and recent experience.
2. Research the problem, competing causes, workarounds and counterevidence.
3. Confirm a solution-independent, evidence-calibrated problem statement.
4. Compare mechanisms and choose a cheap falsification experiment.
5. Define risk-matched prototype/scope, outcomes, guardrails and thresholds.
6. Run an authorized non-build experiment or hand off to an external builder.
7. Inspect actual observations; iterate, research more, pivot, stop or graduate.

Technical design and PRDs are conditional outputs. HTML, payment tests and market
sizing are not universal requirements. A low-cost experiment may test unproven
demand; no fake “validated” label is required to justify it. High-stakes exposure
still requires adequate safety/privacy review and action-specific authorization.

## Workspace and checked state

After product-root selection, initialization creates only:

```text
product-root/
└── docs/
    ├── psi-state.json
    ├── reviews/
    └── prototypes/
```

It does not copy helpers, initialize an app, create empty final documents, or
overwrite AGENTS.md. Namespaced versioned JSON artifacts are written as each
stage produces real content: brief, problem, solution, experiment, optional
handoff/return, outcome and decision. Human-readable Markdown is optional output,
not proof of state. See [the complete contract](references/state-contract.md).

Using your host command tool, replace and quote both paths:

```sh
python3 <skill-root>/scripts/psi_state.py init --root <product-root>
python3 <skill-root>/scripts/psi_state.py check --root <product-root>
python3 <skill-root>/scripts/psi_state.py check --root <product-root> --next SOLUTION_DISCOVERY
```

`check` is read-only and returns a nonzero status on rejection. PSI records an
approved transition afterward; the helper does not fabricate reviews/approvals.
Fingerprints bind exact bytes and upstream dependencies. Legacy filenames never
establish completion. Corrupt/moved manifests stop for explicit recovery.

**Limits:** this is a procedural skill plus an offline checker, not a sandbox,
authenticated approval service, or host-wide tool interceptor. It cannot force
skill selection, validate the truth of cited evidence, or prevent a permissive
agent from ignoring it. Use trusted single-writer workspaces; concurrent malicious
filesystem mutation is out of scope. Linux is exercised locally; other operating
systems require native validation before claiming support.

## Development verification

```sh
python3 -m unittest discover -s tests -v
```

Tests cover structural state/gate contracts and negative fixtures. Static prose
checks do not prove model obedience, nor do synthetic fixtures prove product
success. Live model replays should be reported separately with prompts, model,
results and limitations. See [implementation and issue map](docs/implementation-plan.md).

## Helpers and provenance

PSI is the only discoverable orchestrator. Original imported helper contents are
preserved as inactive Markdown under `references/vendor/`, not auto-installed
SKILL.md files. Do not execute archived commands. Provenance/license review is a
release blocker for redistributing those helpers; see [vendor status](references/vendor/README.md).

Made by taha.u. Credits to the /vibe-prd creators for the original inspiration.
