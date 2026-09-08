"""Static instruction contracts; live-agent compliance needs separate replays."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def test_canonical_entry_and_adaptive_research_replace_document_funnel(self):
        skill = (ROOT / 'SKILL.md').read_text()
        for required in ('FOUNDER_BRIEF', 'UNKNOWN', 'psi_state.py', 'capability', 'batch', 'problem hypothesis', 'solution hypothesis'):
            self.assertIn(required, skill)
        active = [ROOT / 'SKILL.md', ROOT / 'README.md', *sorted((ROOT / 'phases').glob('*.md'))]
        for path in active:
            text = path.read_text()
            for forbidden in ('c:\\Users\\henry', 'all 12 questions are answered', '10 opened/read sources minimum', 'fully validated product', 'npx -y', 'all phases complete', 'Copy all directories'):
                self.assertNotIn(forbidden, text, str(path))
        self.assertEqual(list((ROOT / 'subskills').rglob('SKILL.md')), [], 'Peer orchestrators must not remain discoverable')
        self.assertTrue((ROOT / 'phases/p6-learning.md').exists())
        self.assertIn('Do not list intervention directions during FOUNDER_BRIEF', skill)
        self.assertIn('Do not present possible causes before the recent incident', skill)

    def test_problem_contract_and_teaching_checkpoint_are_explicit(self):
        text = (ROOT / 'phases/p1-discovery.md').read_text()
        for required in ('solution-independent', 'counterevidence', 'falsifier', 'UNKNOWN', 'What it does not prove', 'What changed', 'WORTH_INVESTIGATING', 'RESEARCH_MORE', 'STOP'):
            self.assertIn(required, text)

    def test_readme_matches_manifest_directories(self):
        text = (ROOT / 'README.md').read_text()
        for required in ('psi-state.json', 'reviews/', 'prototypes/', 'python3 -m unittest discover -s tests -v'):
            self.assertIn(required, text)


if __name__ == '__main__':
    unittest.main()
