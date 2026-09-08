"""Offline contract tests; not a claim of model obedience."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'psi_state.py'


class WorkspaceTests(unittest.TestCase):
    def test_initialize_preserves_existing_content_and_is_idempotent(self):
        self.assertTrue(SCRIPT.exists(), 'Missing executable workspace contract')
        spec = importlib.util.spec_from_file_location('psi_state', SCRIPT)
        assert spec is not None and spec.loader is not None
        api = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(api)
        with tempfile.TemporaryDirectory(prefix='psi workspace ') as d:
            root = Path(d)
            (root / 'AGENTS.md').write_text('Existing user rules')
            state = api.initialize(root)
            self.assertEqual(state['current_state'], 'FOUNDER_BRIEF')
            self.assertEqual(state, api.initialize(root))
            self.assertEqual((root / 'AGENTS.md').read_text(), 'Existing user rules')
            self.assertFalse((root / '.agents').exists())
            self.assertTrue((root / 'docs/reviews').is_dir())
            self.assertTrue((root / 'docs/prototypes').is_dir())
            self.assertEqual(list((root / 'docs').glob('*.md')), [])


    def test_unsafe_or_conflicting_workspace_fails_without_writes(self):
        spec = importlib.util.spec_from_file_location('psi_state', SCRIPT)
        assert spec is not None and spec.loader is not None
        api = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(api)
        for kind in ('skill_root', 'docs_symlink', 'reviews_symlink', 'manifest_symlink', 'corrupt', 'moved'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as d:
                root = Path(d) / 'project'
                root.mkdir()
                outside = Path(d) / 'outside'
                outside.mkdir()
                if kind == 'skill_root':
                    (root / 'SKILL.md').write_text('---\nname: vibe-psi\n---\n')
                elif kind == 'docs_symlink':
                    (root / 'docs').symlink_to(outside, target_is_directory=True)
                else:
                    (root / 'docs').mkdir()
                    if kind == 'reviews_symlink':
                        (root / 'docs/reviews').symlink_to(outside, target_is_directory=True)
                    elif kind == 'manifest_symlink':
                        (root / 'docs/psi-state.json').symlink_to(outside / 'missing.json')
                    elif kind == 'corrupt':
                        (root / 'docs/psi-state.json').write_text('{')
                    else:
                        api.initialize(root)
                        import json
                        path = root / 'docs/psi-state.json'
                        state = json.loads(path.read_text())
                        state['project_root'] = str(outside)
                        path.write_text(json.dumps(state))
                before = {str(p): p.read_bytes() for p in root.rglob('*') if p.is_file()}
                with self.assertRaises(ValueError):
                    api.initialize(root)
                self.assertEqual(before, {str(p): p.read_bytes() for p in root.rglob('*') if p.is_file()})
                self.assertEqual(list(outside.iterdir()), [])


    def test_gate_checks_artifact_review_approval_and_dependencies(self):
        spec = importlib.util.spec_from_file_location('psi_state', SCRIPT)
        assert spec is not None and spec.loader is not None
        api = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(api)
        self.assertTrue(hasattr(api, 'check_transition'), 'Missing transition guard')
        import hashlib
        import json
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            state = api.initialize(root)
            with self.assertRaises(ValueError):
                api.check_transition(root, state, 'SOLUTION_DISCOVERY')
            state['current_state'] = 'PROBLEM_DISCOVERY'
            brief_path = root / 'docs/brief-v1.json'
            brief_path.write_text(json.dumps({'project_id': state['project_id'], 'kind': 'brief'}))
            brief_hash = hashlib.sha256(brief_path.read_bytes()).hexdigest()
            state['artifacts']['brief'] = {'path': 'docs/brief-v1.json', 'sha256': brief_hash, 'dependencies': {}, 'review': {'verdict': 'PASS', 'sha256': brief_hash, 'reviewer': 'fixture critic', 'blockers': []}, 'approval': {'sha256': brief_hash, 'decision': 'APPROVE', 'actor': 'fixture user'}}
            with self.assertRaises(ValueError):
                api.check_transition(root, state, 'SOLUTION_DISCOVERY')
            problem = {k: {'text': 'Fixture observation', 'evidence_ids': ['E1'], 'status': 'SUPPORTED'} for k in ('user', 'situation', 'desired_progress', 'difficulty', 'workaround', 'frequency', 'severity', 'consequence', 'counterevidence', 'falsifier')}
            payload = {'project_id': state['project_id'], 'kind': 'problem', 'statement': problem,
                       'evidence': [{'id': 'E1', 'class': 'founder_observation', 'source': 'Synthetic fixture, not a real user', 'limitations': 'Single synthetic case'}],
                       'verdict': 'WORTH_INVESTIGATING'}
            path = root / 'docs/problem-v1.json'
            path.write_text(json.dumps(payload))
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            record = {'path': 'docs/problem-v1.json', 'sha256': digest, 'dependencies': {'brief': brief_hash},
                      'review': {'verdict': 'PASS', 'sha256': digest, 'reviewer': 'fixture critic', 'blockers': []},
                      'approval': {'sha256': digest, 'decision': 'APPROVE', 'actor': 'fixture user'}}
            state['artifacts']['problem'] = record
            api.check_transition(root, state, 'SOLUTION_DISCOVERY')
            for key, value in [('review', {**record['review'], 'blockers': ['unsupported inference']}), ('approval', {**record['approval'], 'sha256': 'stale'}), ('path', '../outside.json')]:
                with self.subTest(key=key):
                    original = record[key]
                    record[key] = value
                    with self.assertRaises(ValueError):
                        api.check_transition(root, state, 'SOLUTION_DISCOVERY')
                    record[key] = original
            for verdict in ('STOP', 'RESEARCH_MORE', 'PIVOT'):
                payload['verdict'] = verdict
                path.write_text(json.dumps(payload))
                digest2 = hashlib.sha256(path.read_bytes()).hexdigest()
                record['sha256'] = digest2
                record['review']['sha256'] = digest2
                record['approval']['sha256'] = digest2
                with self.assertRaises(ValueError):
                    api.check_transition(root, state, 'SOLUTION_DISCOVERY')
            payload['verdict'] = 'WORTH_INVESTIGATING'
            del payload['statement']['consequence']
            path.write_text(json.dumps(payload))
            digest2 = hashlib.sha256(path.read_bytes()).hexdigest()
            record['sha256'] = digest2
            record['review']['sha256'] = digest2
            record['approval']['sha256'] = digest2
            with self.assertRaises(ValueError):
                api.check_transition(root, state, 'SOLUTION_DISCOVERY')


if __name__ == '__main__':
    unittest.main()
