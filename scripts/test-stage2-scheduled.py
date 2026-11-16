"""Concurrency and resume tests for the scheduled Stage 2 claim contract."""
import datetime as dt
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('scheduled', Path(__file__).with_name('stage2-scheduled.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class Claims(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 11, 16, 13, tzinfo=dt.timezone.utc)
        self.state = {'activeClaim': None, 'claimHistory': []}
    def claim(self):
        self.state, _ = m.transition(self.state, 'claim', 'A', 'old', ['cp-000051'], self.now)
    def test_completed_unresolved_is_skipped_and_partial_is_resumed(self):
        self.assertEqual(m.select(['done', 'new', 'partial'], {'done'}, {'partial'}), ['partial', 'new'])
    def test_live_duplicate_is_rejected(self):
        self.claim()
        with self.assertRaises(ValueError):
            m.transition(self.state, 'claim', 'A', 'new', ['cp-000051'], self.now)
    def test_expired_claim_is_recoverable_and_old_token_is_fenced(self):
        self.claim()
        later = self.now + dt.timedelta(minutes=91)
        self.state, _ = m.transition(self.state, 'claim', 'A', 'new', ['cp-000051'], later)
        with self.assertRaises(ValueError):
            m.transition(self.state, 'check', 'A', 'old', [], later)
        self.assertEqual(self.state['claimHistory'][0]['closedAs'], 'expired')
    def test_expired_owner_cannot_renew(self):
        self.claim()
        with self.assertRaises(ValueError):
            m.transition(self.state, 'renew', 'A', 'old', [], self.now + dt.timedelta(minutes=90))
    def test_other_worker_cannot_release_claim(self):
        self.claim()
        with self.assertRaises(ValueError):
            m.transition(self.state, 'release', 'B', 'old', [], self.now)
    def test_release_allows_next_run(self):
        self.claim()
        self.state, _ = m.transition(self.state, 'release', 'A', 'old', [], self.now)
        self.state, _ = m.transition(self.state, 'claim', 'A', 'new', ['cp-000055'], self.now)
        self.assertEqual(self.state['activeClaim']['token'], 'new')
    def test_final_report_can_resume_after_last_case_and_interruption(self):
        self.state, result = m.transition(self.state, 'claim', 'A', 'final', [], self.now, integration=True)
        self.assertEqual(result['claim']['purpose'], 'final-integration')
    def test_empty_case_queue_exhausts_without_integration(self):
        _, result = m.transition(self.state, 'claim', 'A', 'none', [], self.now)
        self.assertEqual(result['status'], 'exhausted')

if __name__ == '__main__':
    unittest.main()
