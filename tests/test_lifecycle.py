"""Synthetic fixtures exercise the guard, never claim real user evidence."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('psi_state', ROOT / 'scripts/psi_state.py')
assert SPEC is not None and SPEC.loader is not None
api = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(api)

FIELDS = ('user', 'situation', 'desired_progress', 'difficulty', 'workaround', 'frequency', 'severity', 'consequence', 'counterevidence', 'falsifier')


class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = api.initialize(self.root)

    def put(self, kind, dependencies=(), **data):
        payload = {'project_id': self.state['project_id'], 'kind': kind, **data}
        if kind == 'problem':
            payload.update(statement={k: {'text': 'Synthetic observation', 'status': 'SUPPORTED', 'evidence_ids': ['E1']} for k in FIELDS}, evidence=[{'id': 'E1', 'class': 'founder_observation', 'source': 'Synthetic fixture', 'limitations': 'Not empirical evidence'}], verdict='WORTH_INVESTIGATING')
        if kind == 'solution':
            payload['verdict'] = 'WORTH_TESTING'
        path = self.root / ('docs/' + kind + '-v1.json')
        path.write_text(json.dumps(payload))
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        self.state['artifacts'][kind] = {'path': path.relative_to(self.root).as_posix(), 'sha256': digest,
            'dependencies': {k: self.state['artifacts'][k]['sha256'] for k in dependencies},
            'review': {'verdict': 'PASS', 'sha256': digest, 'reviewer': 'synthetic critic', 'blockers': []},
            'approval': {'sha256': digest, 'decision': 'APPROVE', 'actor': 'synthetic user'}}
        return path

    def advance(self, target):
        api.check_transition(self.root, self.state, target)
        self.state['current_state'] = target

    def through_solution(self):
        self.put('brief')
        self.advance('PROBLEM_DISCOVERY')
        self.put('problem', ('brief',))
        self.advance('SOLUTION_DISCOVERY')
        self.put('solution', ('problem',))

    def test_complete_experiment_and_return_loop(self):
        self.through_solution()
        self.advance('LEARNING_PROTOTYPE')
        self.put('experiment', ('solution',), v1_feature_ids=['F1'])
        self.advance('READY_FOR_EXPERIMENT')
        self.advance('REAL_USER_VALIDATION')
        self.put('outcome', ('experiment',), result='INCONCLUSIVE')
        self.advance('DECISION_ITERATION')
        self.put('decision', ('outcome',), next_state='ITERATE_SOLUTION')
        self.advance('SOLUTION_DISCOVERY')

    def test_decision_labels_authorize_only_matching_targets(self):
        self.through_solution()
        self.put('experiment', ('solution',), v1_feature_ids=['F1'])
        self.put('outcome', ('experiment',), result='INCONCLUSIVE')
        self.state['current_state'] = 'DECISION_ITERATION'
        self.put('decision', ('outcome',), next_state='ITERATE_SOLUTION')
        with self.assertRaises(ValueError):
            api.check_transition(self.root, self.state, 'STOP')
        self.assertEqual(
            api.check_transition(self.root, self.state, 'SOLUTION_DISCOVERY'),
            'SOLUTION_DISCOVERY')

    def test_graduate_resume_requires_matching_decision(self):
        self.through_solution()
        self.put('experiment', ('solution',), v1_feature_ids=['F1'])
        self.put('outcome', ('experiment',), result='INCONCLUSIVE')
        self.state['current_state'] = 'GRADUATE'
        for next_state in ('SOLUTION_DISCOVERY', 'GRADUATE'):
            self.put('decision', ('outcome',), next_state=next_state)
            (self.root / 'docs/psi-state.json').write_text(json.dumps(self.state))
            before = {p.relative_to(self.root): p.read_bytes()
                      for p in self.root.rglob('*') if p.is_file()}
            for command in ('init', 'check'):
                with self.subTest(next_state=next_state, command=command):
                    result = subprocess.run(
                        [sys.executable, str(ROOT / 'scripts/psi_state.py'),
                         command, '--root', str(self.root)],
                        capture_output=True, text=True)
                    payload = json.loads(result.stdout)
                    if next_state == 'GRADUATE':
                        self.assertEqual(result.returncode, 0, result.stdout)
                        self.assertEqual(payload['status'], 'PASS')
                        self.assertEqual(payload['state'], 'GRADUATE')
                    else:
                        self.assertEqual(result.returncode, 1, result.stdout)
                        self.assertEqual(payload['status'], 'BLOCKED')
                        self.assertIn('Decision does not authorize', payload['reason'])
                    self.assertEqual(before, {p.relative_to(self.root): p.read_bytes()
                                             for p in self.root.rglob('*') if p.is_file()})

    def test_external_build_does_not_finish_validation(self):
        self.through_solution()
        self.advance('LEARNING_PROTOTYPE')
        self.put('experiment', ('solution',), v1_feature_ids=['F1'])
        self.advance('MVP_EXPERIMENT_HANDOFF')
        self.put('handoff', ('experiment',), v1_feature_ids=['F1'])
        self.advance('READY_FOR_EXTERNAL_BUILD')
        self.advance('EXTERNAL_BUILD')
        with self.assertRaises(ValueError):
            self.advance('REAL_USER_VALIDATION')
        self.put('return', ('handoff',))
        self.advance('REAL_USER_VALIDATION')
        with self.assertRaises(ValueError):
            self.advance('GRADUATE')

    def test_stale_problem_invalidates_downstream_even_after_reapproval(self):
        self.through_solution()
        path = self.root / self.state['artifacts']['problem']['path']
        path.write_text(path.read_text() + '\n')
        with self.assertRaises(ValueError):
            api.check_transition(self.root, self.state, 'LEARNING_PROTOTYPE')
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        record = self.state['artifacts']['problem']
        record['sha256'] = record['review']['sha256'] = record['approval']['sha256'] = digest
        with self.assertRaises(ValueError):
            api.check_transition(self.root, self.state, 'LEARNING_PROTOTYPE')

    def test_missing_dependency_is_not_an_optional_escape_hatch(self):
        self.through_solution()
        self.state['artifacts']['solution']['dependencies'] = {}
        with self.assertRaises(ValueError):
            api.check_transition(self.root, self.state, 'LEARNING_PROTOTYPE')

    def test_unknown_or_unsupported_problem_clauses(self):
        self.through_solution()
        path = self.root / self.state['artifacts']['problem']['path']
        original = json.loads(path.read_text())
        for status, ids, accepted in [('SUPPORTED', ['missing'], False), ('INVENTED', [], False), ('UNKNOWN', [], True)]:
            payload = copy.deepcopy(original)
            payload['statement']['frequency'].update(status=status, evidence_ids=ids)
            path.write_text(json.dumps(payload))
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            r = self.state['artifacts']['problem']
            r['sha256'] = r['review']['sha256'] = r['approval']['sha256'] = digest
            self.state['current_state'] = 'PROBLEM_DISCOVERY'
            if accepted:
                api.check_transition(self.root, self.state, 'SOLUTION_DISCOVERY')
            else:
                with self.assertRaises(ValueError):
                    api.check_transition(self.root, self.state, 'SOLUTION_DISCOVERY')

    def test_corrupt_schema_and_spoofed_terminal_state_are_rejected(self):
        self.assertTrue(hasattr(api, 'validate_state'), 'Missing resume validator')
        for key, value in [('schema_version', 99), ('current_state', 'ALL_VALIDATED'), ('current_state', 'READY_FOR_EXTERNAL_BUILD'), ('artifacts', []), ('project_id', '')]:
            state = copy.deepcopy(self.state)
            state[key] = value
            with self.assertRaises(ValueError):
                api.validate_state(self.root, state)

    def test_manifest_identity_schema_and_routing_fields_are_required(self):
        invalid = {
            'schema_version': (True, False, 1.0, '1', None, [], {}, 99),
            'project_id': ({'not': 'an identifier'}, ['id'], 1, True, None, '', '  '),
            'purpose': ({}, [], 1, True, None, '', '  '),
            'modality': ({}, [], 1, True, None, '', '  '),
        }
        for field, values in invalid.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    state = copy.deepcopy(self.state)
                    state[field] = value
                    with self.assertRaises(ValueError):
                        api.validate_state(self.root, state)
            with self.subTest(field=field, missing=True):
                state = copy.deepcopy(self.state)
                del state[field]
                with self.assertRaises(ValueError):
                    api.validate_state(self.root, state)

    def test_manifest_allows_unknown_and_custom_routing_labels(self):
        for purpose, modality in [('UNKNOWN', 'UNKNOWN'), ('Custom purpose', 'Custom modality')]:
            with self.subTest(purpose=purpose, modality=modality):
                state = copy.deepcopy(self.state)
                state.update(project_id='non-uuid-project', purpose=purpose, modality=modality)
                self.assertEqual(api.validate_state(self.root, state), state)

    def test_weak_solution_preserves_problem(self):
        self.through_solution()
        path = self.root / self.state['artifacts']['solution']['path']
        data = json.loads(path.read_text())
        data['verdict'] = 'RESEARCH_MORE'
        path.write_text(json.dumps(data))
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        r = self.state['artifacts']['solution']
        r['sha256'] = r['review']['sha256'] = r['approval']['sha256'] = digest
        problem = copy.deepcopy(self.state['artifacts']['problem'])
        with self.assertRaises(ValueError):
            self.advance('LEARNING_PROTOTYPE')
        api.check_transition(self.root, self.state, 'SOLUTION_DISCOVERY')
        self.assertEqual(problem, self.state['artifacts']['problem'])

    def test_cli_is_read_only_on_check_and_nonzero_on_rejection(self):
        cmd = [sys.executable, str(ROOT / 'scripts/psi_state.py'), 'check', '--root', str(self.root), '--next', 'SOLUTION_DISCOVERY']
        before = (self.root / 'docs/psi-state.json').read_bytes()
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('BLOCKED', result.stdout)
        self.assertEqual(before, (self.root / 'docs/psi-state.json').read_bytes())


if __name__ == '__main__':
    unittest.main()
