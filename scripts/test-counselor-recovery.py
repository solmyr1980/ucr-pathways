#!/usr/bin/env python3
"""Exercise the actual workflow mode selector in isolated two-commit git fixtures."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / '.github/workflows/build-counselor-comparison.yml').read_text()
STEP = WORKFLOW.split('      - name: Select safe execution mode\n', 1)[1].split('\n      - name:', 1)[0]
SCRIPT = '\n'.join(line[10:] for line in STEP.split('        run: |\n', 1)[1].splitlines())
SCRIPT = SCRIPT.replace('${{ github.event_name }}', 'push')
DECISION = 'data/counselor/decisions/cp-000001.json'
CANONICAL = 'data/counselor/comparisons/cp-000001.json'


class RecoveryModeTests(unittest.TestCase):
    def select(self, before, after):
        with tempfile.TemporaryDirectory(prefix='ucr-recovery-') as name:
            root = Path(name)
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.DEVNULL, text=True).strip()
            git('init', '-q'); git('config', 'user.email', 'fixture@example.invalid'); git('config', 'user.name', 'Fixture')
            def put(files):
                for path, value in files.items():
                    target = root / path
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if value is None:
                        target.unlink()
                    else:
                        target.write_text(value)
            put({'seed.txt': 'fixture', **before}); git('add', '.'); git('commit', '-qm', 'baseline')
            put(after); git('add', '.'); git('commit', '-qm', 'change')
            output = root / 'output'
            result = subprocess.run(['bash', '-c', SCRIPT], cwd=root, env={**os.environ, 'GITHUB_SHA': git('rev-parse', 'HEAD'), 'GITHUB_OUTPUT': str(output)}, capture_output=True, text=True)
            values = dict(line.split('=', 1) for line in output.read_text().splitlines()) if output.exists() else {}
            return result.returncode, values.get('mode'), result.stderr

    def test_new_production(self):
        self.assertEqual(self.select({}, {DECISION: '{"id":"cp-000001"}'})[:2], (0, 'production'))

    def test_new_pending_not_allowed(self):
        self.assertNotEqual(self.select({}, {DECISION: '{"exception":{"type":"ucr-assessment-pending"}}'})[0], 0)

    def test_recovered_decision_replays_existing_pair(self):
        self.assertEqual(self.select({CANONICAL: 'old'}, {DECISION: '{}', CANONICAL: 'regenerated'})[:2], (0, 'repair'))

    def test_recovery_without_regenerated_pair_rejected(self):
        self.assertNotEqual(self.select({CANONICAL: 'old'}, {DECISION: '{}'})[0], 0)

    def test_existing_decision_repair(self):
        self.assertEqual(self.select({CANONICAL: 'old', DECISION: '{}'}, {DECISION: '{"id":"cp-000001"}', CANONICAL: 'new'})[:2], (0, 'repair'))

    def test_existing_decision_without_pair_rejected(self):
        self.assertNotEqual(self.select({CANONICAL: 'old', DECISION: '{}'}, {DECISION: '{"id":"cp-000001"}'})[0], 0)

    def test_competing_root_decisions_rejected(self):
        self.assertNotEqual(self.select({}, {DECISION: '{}', DECISION.replace('000001', '000002'): '{}'})[0], 0)

    def test_unpaired_withdrawal_rejected(self):
        self.assertNotEqual(self.select({DECISION: '{}', CANONICAL: '{}'}, {DECISION: None})[0], 0)


if __name__ == '__main__':
    unittest.main()
