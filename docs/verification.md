# Verification report

Status: verified on Linux against the working tree for this PR. This report
records structural checks and synthetic behavior probes; it does not claim that
PSI can authenticate approvals, enforce host permissions, or establish real-user
outcomes.

## Automated checks

- `python3 -m unittest discover -s tests -v`: **18 tests passed**.
- `python3 -m unittest discover -s tests -p 'test_*.py'`: **18 tests passed**.
- `python3 -m compileall -q scripts tests`: **passed**.
- `git diff --check`: **passed**.

The regression suite covers workspace ownership and preservation, unsafe paths,
review/approval and dependency fingerprints, negative gates, stale artifacts,
problem evidence clauses, read-only rejected checks, terminal graduation resume,
and manifest identity/schema/routing validation.

## Independent review and fixes

An independent Luna review reproduced two structural validation defects before
the final fixes:

1. A resumed `GRADUATE` manifest could pass while its approved decision named a
   different next state. Validation now requires `decision.next_state` to be
   `GRADUATE`; the regression checks both `init` and `check` and verifies no
   files change.
2. Manifest validation accepted `schema_version=true`, non-string/blank
   `project_id`, and missing or blank `purpose`/`modality`. Validation now
   requires integer schema version `1` (excluding booleans), nonblank strings for
   project identity and routing fields, while retaining `UNKNOWN` and custom
   labels.

The review found no hardcoded secrets, shell execution, `eval`/`exec`, pickle
use, or reported security concern within the trusted offline preflight scope.

## Synthetic live replays

Four retained Luna runs exercised two isolated empty product roots across the
original and revised intake instructions. The runs used no web capability and
were instructed not to edit the PSI source repository or perform external
actions. The revised runs initialized `FOUNDER_BRIEF`, saved only the supplied
product-root artifacts, kept the browser idea as a hypothesis, and asked for a
recent incident before defining an MVP. Raw prompts, final responses, tool
names, commands, states, and artifacts are retained in `docs/evaluations.json`.

These are single-run acceptance probes, not reliability estimates. Earlier
revisions are retained because they include observed semantic drift; the final
replay set still needs repeated runs across the full issue fixture matrix.

## Remaining work

Open issues #1–#5 remain open and authoritative. Follow-up work is documented in
`docs/implementation-plan.md`, including transactional state migration,
complete typed semantic payloads, host adapters, repeated behavioral evaluation,
prompt-injection/HTML fixtures, provenance/license resolution, release
integrity, and native-platform testing.
