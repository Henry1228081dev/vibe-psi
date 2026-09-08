"""Offline PSI preflight; not a sandbox or proof of evidence/approval authenticity.

Only init writes. check validates proposed transitions without changing state.
Use in a trusted, single-writer workspace; hostile concurrent writers are out
of scope. Semantic reviews and explicit user approval remain host duties.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import uuid

DEPENDENCIES = {
    'brief': (), 'problem': ('brief',), 'solution': ('problem',),
    'experiment': ('solution',), 'handoff': ('experiment',),
    'return': ('handoff',), 'outcome': ('experiment',), 'decision': ('outcome',),
}
EDGES = {
    'FOUNDER_BRIEF': {'PROBLEM_DISCOVERY'},
    'PROBLEM_DISCOVERY': {'SOLUTION_DISCOVERY'},
    'SOLUTION_DISCOVERY': {'LEARNING_PROTOTYPE'},
    'LEARNING_PROTOTYPE': {'READY_FOR_EXPERIMENT', 'MVP_EXPERIMENT_HANDOFF'},
    'MVP_EXPERIMENT_HANDOFF': {'READY_FOR_EXTERNAL_BUILD'},
    'READY_FOR_EXTERNAL_BUILD': {'EXTERNAL_BUILD'},
    'EXTERNAL_BUILD': {'REAL_USER_VALIDATION'},
    'READY_FOR_EXPERIMENT': {'REAL_USER_VALIDATION'},
    'REAL_USER_VALIDATION': {'DECISION_ITERATION'},
    'DECISION_ITERATION': {'SOLUTION_DISCOVERY', 'LEARNING_PROTOTYPE', 'MVP_EXPERIMENT_HANDOFF', 'FOUNDER_BRIEF', 'STOP', 'GRADUATE'},
    'STOP': set(), 'GRADUATE': set(),
}
REQUIRED = {
    'FOUNDER_BRIEF': (), 'PROBLEM_DISCOVERY': ('brief',),
    'SOLUTION_DISCOVERY': ('problem',), 'LEARNING_PROTOTYPE': ('solution',),
    'READY_FOR_EXPERIMENT': ('experiment',), 'MVP_EXPERIMENT_HANDOFF': ('experiment',),
    'READY_FOR_EXTERNAL_BUILD': ('handoff',), 'EXTERNAL_BUILD': ('handoff',),
    'REAL_USER_VALIDATION': ('experiment',), 'DECISION_ITERATION': ('outcome',),
    'GRADUATE': ('decision',), 'STOP': (),
}
PROBLEM_FIELDS = ('user', 'situation', 'desired_progress', 'difficulty', 'workaround',
                  'frequency', 'severity', 'consequence', 'counterevidence', 'falsifier')
EVIDENCE_CLASSES = {'founder_observation', 'secondary', 'direct_user', 'observed_behavior', 'commercial_commitment'}
DECISION_TARGETS = {
    'ITERATE_SOLUTION': 'SOLUTION_DISCOVERY',
    'ITERATE_PROTOTYPE': 'LEARNING_PROTOTYPE',
    'REBUILD_HANDOFF': 'MVP_EXPERIMENT_HANDOFF',
    'PIVOT': 'FOUNDER_BRIEF',
    'STOP': 'STOP',
    'GRADUATE': 'GRADUATE',
}


def artifact_path(root, relative):
    if not isinstance(relative, str) or not re.fullmatch(r'docs/(?:[a-z0-9_-]+/)*[a-z0-9_-]+\.(?:json|md)', relative):
        raise ValueError('Unsafe artifact path')
    path = Path(root)
    for part in relative.split('/'):
        if part.split('.')[0].upper() in {'CON', 'PRN', 'AUX', 'NUL', *(f'COM{i}' for i in range(1, 10)), *(f'LPT{i}' for i in range(1, 10))}:
            raise ValueError('Reserved path component')
        path = path / part
        if path.is_symlink() or getattr(path, 'is_junction', lambda: False)():
            raise ValueError('Symlink/junction artifact')
    return path


def problem_preflight(payload):
    statement, evidence = payload.get('statement'), payload.get('evidence')
    if not isinstance(statement, dict) or not isinstance(evidence, list):
        raise ValueError('Missing statement/evidence')
    ids = set()
    for item in evidence:
        if not isinstance(item, dict) or not item.get('id') or item['id'] in ids or item.get('class') not in EVIDENCE_CLASSES or not item.get('source') or not item.get('limitations'):
            raise ValueError('Invalid evidence record')
        ids.add(item['id'])
    for field in PROBLEM_FIELDS:
        clause = statement.get(field)
        if not isinstance(clause, dict) or not isinstance(clause.get('text'), str) or not clause['text'].strip():
            raise ValueError('Missing problem dimension: ' + field)
        refs = clause.get('evidence_ids')
        if clause.get('status') not in {'SUPPORTED', 'ASSUMPTION', 'UNKNOWN', 'CONFLICTING'} or not isinstance(refs, list) or any(ref not in ids for ref in refs):
            raise ValueError('Invalid clause provenance: ' + field)
        if clause['status'] in {'SUPPORTED', 'CONFLICTING'} and not refs:
            raise ValueError('Unsupported clause: ' + field)


def approved_artifact(root, state, kind, visiting=()):
    if kind in visiting or kind not in DEPENDENCIES:
        raise ValueError('Cyclic or unknown artifact')
    record = state['artifacts'].get(kind)
    if not isinstance(record, dict):
        raise ValueError('Missing approved ' + kind)
    path = artifact_path(root, record.get('path'))
    try:
        raw = path.read_bytes()
        payload = json.loads(raw)
    except (OSError, ValueError) as exc:
        raise ValueError('Unreadable artifact: ' + kind) from exc
    digest = hashlib.sha256(raw).hexdigest()
    review, approval = record.get('review'), record.get('approval')
    if not isinstance(review, dict) or not isinstance(approval, dict):
        raise ValueError('Missing review/approval')
    if (record.get('sha256') != digest or review.get('sha256') != digest
            or approval.get('sha256') != digest or review.get('verdict') != 'PASS'
            or review.get('blockers') != [] or not review.get('reviewer')
            or approval.get('decision') != 'APPROVE' or not approval.get('actor')):
        raise ValueError('Stale or failed review/approval: ' + kind)
    if not isinstance(payload, dict) or payload.get('project_id') != state['project_id'] or payload.get('kind') != kind:
        raise ValueError('Artifact identity mismatch')
    dependencies = record.get('dependencies')
    if not isinstance(dependencies, dict) or set(dependencies) != set(DEPENDENCIES[kind]):
        raise ValueError('Missing or unexpected dependencies: ' + kind)
    for parent, expected in dependencies.items():
        approved_artifact(root, state, parent, (*visiting, kind))
        if expected != state['artifacts'][parent]['sha256']:
            raise ValueError('Stale dependency: ' + parent)
    if kind == 'problem':
        problem_preflight(payload)
    return payload


def validate_state(root, state):
    if not isinstance(state, dict):
        raise ValueError('Invalid manifest identity/schema')
    if (isinstance(state.get('schema_version'), bool)
            or not isinstance(state.get('schema_version'), int)
            or state.get('schema_version') != 1
            or not isinstance(state.get('project_id'), str)
            or not state['project_id'].strip()
            or not isinstance(state.get('purpose'), str)
            or not state['purpose'].strip()
            or not isinstance(state.get('modality'), str)
            or not state['modality'].strip()):
        raise ValueError('Invalid manifest identity/schema')
    if state.get('project_root') != str(Path(root).resolve(strict=True)):
        raise ValueError('RESUME_CONFLICT: project root mismatch')
    if state.get('current_state') not in EDGES or not isinstance(state.get('artifacts'), dict):
        raise ValueError('Invalid state/artifact registry')
    for field in ('active_hypotheses', 'user_decisions', 'history'):
        if not isinstance(state.get(field), list):
            raise ValueError('Invalid manifest field: ' + field)
    for kind in REQUIRED[state['current_state']]:
        payload = approved_artifact(root, state, kind)
        if state['current_state'] == 'GRADUATE' and kind == 'decision' and payload.get('next_state') != 'GRADUATE':
            raise ValueError('Decision does not authorize GRADUATE')
    return state


def check_transition(root, state, target):
    validate_state(root, state)
    current = state['current_state']
    if current in {'STOP', 'GRADUATE'}:
        raise ValueError('Terminal state: start an explicitly approved new cycle')
    # Rework stays in the current investigation or returns to intake; it never
    # upgrades evidence. Keep superseded artifacts/history outside active registry.
    if target in {current, 'FOUNDER_BRIEF', 'STOP'} and current != 'DECISION_ITERATION':
        return target
    if target not in EDGES[current]:
        raise ValueError('Illegal transition')
    if current == 'DECISION_ITERATION':
        decision = approved_artifact(root, state, 'decision')
        if DECISION_TARGETS.get(str(decision.get('next_state'))) != target:
            raise ValueError('Decision does not authorize next state')
    for kind in REQUIRED[target]:
        approved_artifact(root, state, kind)
    if target in {'SOLUTION_DISCOVERY', 'LEARNING_PROTOTYPE', 'READY_FOR_EXPERIMENT', 'MVP_EXPERIMENT_HANDOFF', 'READY_FOR_EXTERNAL_BUILD', 'EXTERNAL_BUILD', 'REAL_USER_VALIDATION', 'DECISION_ITERATION', 'GRADUATE'}:
        if approved_artifact(root, state, 'problem').get('verdict') != 'WORTH_INVESTIGATING':
            raise ValueError('Problem verdict blocks forward transition')
    if target not in {'SOLUTION_DISCOVERY', 'PROBLEM_DISCOVERY'}:
        if approved_artifact(root, state, 'solution').get('verdict') != 'WORTH_TESTING':
            raise ValueError('Solution verdict blocks forward transition')
    if current == 'EXTERNAL_BUILD' and target == 'REAL_USER_VALIDATION':
        approved_artifact(root, state, 'return')
    return target


def initialize(root):
    root = Path(root).resolve(strict=True)
    if (root / 'SKILL.md').exists():
        raise ValueError('Select a product workspace, not a skill installation')
    docs = root / 'docs'
    manifest = docs / 'psi-state.json'
    for path in (docs, docs / 'reviews', docs / 'prototypes', manifest):
        if path.is_symlink() or getattr(path, 'is_junction', lambda: False)():
            raise ValueError('Symlink/junction output is forbidden')
        if path.exists() and path != manifest and not path.is_dir():
            raise ValueError('Directory collision')
    if manifest.exists():
        return validate_state(root, json.loads(manifest.read_text(encoding='utf-8')))
    docs.mkdir(exist_ok=True)
    for directory in ('reviews', 'prototypes'):
        (docs / directory).mkdir(exist_ok=True)
    state = {
        'schema_version': 1, 'project_id': str(uuid.uuid4()),
        'project_root': str(root), 'current_state': 'FOUNDER_BRIEF',
        'purpose': 'UNKNOWN', 'modality': 'UNKNOWN',
        'artifacts': {}, 'active_hypotheses': [], 'user_decisions': [], 'history': [],
    }
    with manifest.open('x', encoding='utf-8') as stream:
        json.dump(state, stream, indent=2)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    return state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('init', 'check'))
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--next', dest='target')
    args = parser.parse_args()
    try:
        if args.command == 'init':
            if args.target:
                raise ValueError('--next is only valid with check')
            state = initialize(args.root)
        else:
            path = artifact_path(args.root, 'docs/psi-state.json')
            state = validate_state(args.root, json.loads(path.read_text(encoding='utf-8')))
            if args.target:
                check_transition(args.root, state, args.target)
        print(json.dumps({'status': 'PASS', 'state': state['current_state'], 'checked_next': args.target, 'project_id': state['project_id']}))
        return 0
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(json.dumps({'status': 'BLOCKED', 'reason': str(exc)}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
