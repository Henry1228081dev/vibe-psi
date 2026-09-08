# Evidence-led PSI repair: findings, decisions and issue coverage

Status: implementation plus explicit follow-up plan; not a claim that every
acceptance criterion in issues #1–#5 is complete. No issue should auto-close from
this PR. Base inspected: `9a28904` on `master`. Research and independent baseline
audits used two `gpt-5.6-luna` workers; Astra read the issues, audited findings and
implemented the changes. Sources and external claims were checked by Astra.

## Best way to achieve the stated purpose

Keep PSI a co-founder/investigator: understand the person's situation, test
competing explanations, recommend the least expensive informative next action,
and return to actual outcomes. A document is a learning record, not the finish
line. Gates should control the next investment rather than require complete
market certainty before a cheap experiment.

The strongest alternative interpretation is that a rigorous spec-first funnel
prevents wasted coding. That helps when the uncertainty is implementation detail,
but it cannot establish whether the target problem, mechanism or behavior matters.
The revised workflow retains specifications and acceptance criteria when useful,
while adding problem, mechanism and outcome decisions before greater investment.

Government discovery guidance explicitly recommends reframing a predefined
solution as a problem and deciding whether further investigation merits cost.[1]
Alpha guidance describes trying different solutions to discovery findings.[2]
The Magenta Book's Test and Learn guidance supports early critical-assumption
tests, iterative adaptation and proportionality to decision importance and the
consequences of error.[5] Prototype guidance allows forms from paper to code and
says to use the form that meets the current need.[6]

These are public-service methods, not controlled evidence that PSI improves
startup success. Their principles inform the design; this PR does not import
mandatory government durations, production standards or study designs into every
personal project. No causal improvement in PSI's real-user outcomes is established.

## Confirmed baseline defects and changes

- `SKILL.md:40–67` wrote/copy-installed before establishing product identity and
  used filenames as stage markers. New orientation selects root first; CLI init
  preserves existing content and requires a project-bound manifest.
- `SKILL.md:91` and phase tails had a checkout-specific Windows path. Routing now
  resolves from the active skill root with no user-specific path edits.
- `phases/p1-discovery.md:13,112,194–204` used quotas and an unconditional
  continuation after even a negative verdict. Adaptive research and explicit
  limited verdicts replace that; the CLI blocks negative problem progression.
- `phases/p2-solution.md:297–312` offered no structural weak-mechanism rework.
  Problem and solution verdicts are separate; a weak solution stays in discovery.
- `phases/p3-features.md:26–37,100–130` forced four HTML prototypes and gathered
  design direction afterward. Experiment form now follows the riskiest assumption;
  design direction precedes visual generation, when needed at all.
- `phases/p4-techspec.md:24` prefilled approval; `p5-build.md:121–138` ended with
  validation/completion claims. Reviewed fingerprints replace status prose, and
  actual outcome/decision stages follow external handoff or a non-build experiment.
- Six discoverable helper SKILL.md files competed for orchestration. Their bytes
  are preserved as inactive vendor Markdown; no helper is copied during init.

Line references above describe the base commit, not rewritten file positions.
The baseline audits support these static defects; they do not establish exploit
success or behavior frequency across models.

## Existing issues — do not replace or close prematurely

### #1 — Canonical discovery → solution → prototype → learning loop

Implemented: single owner, portable routing, canonical states, bounded research,
competing hypotheses, conditional experiment/technical output, external return,
real observations and legal rework/stop/graduate paths. Added dependency-bound
review/approval checks and an explicit self-review fallback.

Remaining: all-stage semantic payload schemas, authenticated approval events,
transactional state writing/migration, host-level routing/action interception,
full independent replay matrix and measured user-learning effectiveness. The
CLI validates structural records; it cannot judge evidence truth or review quality.

### #2 — Raw idea bypasses discovery

Implemented: intake stores problem and mechanism separately; no early MVP/UI
recommendation; capability preflight; helper authority restrictions; checked
transition rejects solution discovery without reviewed problem prerequisites.
Custom-browser plus named-helper and no-web personal scenarios are live-replay
acceptance targets, reported separately in verification evidence.

Remaining: guarantee of PSI selection among external host skills and interception
of unguarded model outputs. Explicit selection is required when automatic routing
misses PSI. A repository skill alone cannot enforce a host-wide entry router.

### #3 — Canonical evidence-backed problem statement

Implemented: provisional-to-revised statement, ten explicit dimensions,
clause-level evidence/unknown status, separate causal hypotheses, semantic
solution-contamination rubric and exact-byte dependency invalidation.

Remaining: deterministic semantic specificity/contamination assessment, complete
sampling/evidence schema enforcement and broad live fixtures for every wording
failure. The CLI permits explicit unknowns; a semantic critic must decide whether
those unknowns block the proposed investment. Agreement never upgrades evidence.

### #4 — Workspace initialization and ownership

Implemented: explicit product root, structural-only/idempotent init, stable ID,
no app-name invention, preservation of unrelated AGENTS/docs, conflict rejection,
no helper install, conservative legacy policy and digest-based prerequisite checks.

Remaining: safe transactional manifest/registry update commands, explicit legacy
migration tooling, moved-root reconciliation, hostile concurrent-filesystem tests,
Windows/macOS native tests and builder-specific AGENTS/agent_docs merge adapters.
The helper deliberately refuses corrupt/moved manifests rather than repairing
unverified approvals. Linux checks are not a portability guarantee.

### #5 — Adversarial validation/safety/state audit

Implemented: negative-gate blocking, four separate evidence assessments, no
validation overclaims, persistent instruction/data and privacy boundaries,
purpose/modality routing, high-stakes exposure limits, safe-output policy,
quarantined competing helpers and offline regression tests.

Remaining: host-enforced permissions, authenticated/signed review events,
end-to-end prompt-injection/HTML testing, automatic evidence/privacy validation,
full commercial/distribution and regulatory rubrics, canonical scope machine
validation across every rendering, vendored upstream license/provenance resolution,
integrity-pinned release packaging and full cross-platform evaluation.

OWASP describes indirect prompt injection through externally supplied content,
and recommends validating output formats and segregating external content.[4]
Those support a layered boundary; the added prose and JSON checker do not make
prompt injection impossible or establish a sandbox.

The Agent Skills specification supports a root SKILL.md with progressively loaded
resources.[3] Official reference validation is a metadata/layout check, not a
semantic quality or permission-enforcement certificate.

## Implementation order after this PR

1. **Harden state ownership:** transactional init/update/migration, schema versions,
   immutable event records and explicit recovery. Acceptance: corrupt/moved roots,
   symlink escapes, simultaneous writers and stale review/dependency failures are
   exercised on native supported platforms without losing user bytes.
2. **Complete typed semantic payloads:** scope equality, full problem/evidence
   provenance, four assessments, experiment protocol, actual return and observation
   contracts. Acceptance: each issue #3/#5 fixture has a decision/verdict/blocker
   oracle; structural checks alone cannot generate a positive semantic verdict.
3. **Integrate host adapters:** explicit entry selection, guarded question/action
   interfaces, constrained helpers and builder-specific exports. Acceptance:
   named external skills cannot advance a PSI-owned session or leak source commands.
4. **Behavioral evaluation:** repeated model runs for weak/strong problem,
   weak mechanism, unknown cause, no web, commercial/no channel/no payment,
   personal/internal/service/API/hardware, injection, stale resume and inconclusive
   return. Review transcripts, actual tools and retained artifacts, not self-grades.
5. **Release hygiene:** establish upstream provenance/licenses; do not invent a
   license. Package only approved material at immutable versions, run official
   metadata validation in supported layouts, and publish native-platform evidence.

## Decisions that deliberately narrow issue proposals

- A cheap approved experiment can test unproven demand. Payment is not a universal
  prerequisite for a prototype; commercial certainty remains UNKNOWN if untested.
- Personal and public-interest problems do not inherit SaaS/TAM/monetization gates.
- Independent critique is preferred, not falsely claimed when unavailable.
- Fixed question/source/prototype/sample counts are not a substitute for evidence.
- No application-build executor is added to PSI. Repairing this repository is
  distinct from the generated-product workflow it defines.

## Acceptance evidence

See [verification report](verification.md) for actual commands, model replays,
observed outputs and remaining limitations. Keep open issues as the authoritative
backlog; this PR addresses concrete portions without claiming their full closure.

## Sources

[1] https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works
[2] https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works
[3] https://agentskills.io/specification
[4] https://genai.owasp.org/llmrisk/llm01-prompt-injection
[5] https://www.gov.uk/government/publications/the-magenta-book/test-and-learn-html
[6] https://www.gov.uk/service-manual/design/making-prototypes
