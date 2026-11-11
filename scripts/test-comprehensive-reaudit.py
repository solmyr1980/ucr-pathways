"""Regression checks for final curriculum gates, including identity exceptions."""
import sys
sys.dont_write_bytecode = True
import importlib.util
from pathlib import Path
import unittest
spec = importlib.util.spec_from_file_location('reaudit', Path(__file__).with_name('validate-comprehensive-reaudit.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class FinalCurriculum(unittest.TestCase):
    def record(self, kind=None):
        row = {'comparator': {'components': [{'id': 'degree', 'credits': 180}]},
               'audience': {'curriculum': {'status': 'complete', 'componentIds': ['degree']}},
               'programmes': []}
        if kind:
            row.update(recordStatus='exception', exception={'type': kind})
        return row

    def test_complete_comparison_and_no_match(self):
        for kind in (None, 'no-defensible-ucr-match'):
            module.validate_approved_curriculum(self.record(kind), 'fixture')

    def test_missing_credits_cannot_approve(self):
        for kind in (None, 'no-defensible-ucr-match', 'external-programme-unresolved'):
            row = self.record(kind)
            row['comparator']['components'][0]['credits'] = 168
            with self.assertRaises(ValueError):
                module.validate_approved_curriculum(row, 'fixture')

    def identity(self):
        row = self.record('registry-exception')
        row['comparator']['components'] = []
        row['audience']['curriculum'] = {'status': 'unresolved', 'componentIds': [], 'limitation': 'Current official identity conflicts with the normalized target.'}
        return row

    def test_supported_identity_exception_without_invented_credits(self):
        module.validate_approved_curriculum(self.identity(), 'fixture')

    def test_identity_exception_cannot_hide_invented_content(self):
        for change in ('credits', 'ucr', 'limitation', 'status'):
            row = self.identity()
            if change == 'credits': row['comparator']['components'] = [{'id': 'invented', 'credits': 180}]
            if change == 'ucr': row['programmes'] = [{'id': 'ucr-1', 'family': 'ucr'}]
            if change == 'limitation': row['audience']['curriculum']['limitation'] = ''
            if change == 'status': row['audience']['curriculum']['status'] = 'complete'
            with self.assertRaises(ValueError):
                module.validate_approved_curriculum(row, 'fixture')

    def test_unresolved_source_exception_still_cannot_approve(self):
        row = self.identity()
        row['exception']['type'] = 'external-programme-unresolved'
        with self.assertRaises(ValueError):
            module.validate_approved_curriculum(row, 'fixture')

if __name__ == '__main__': unittest.main()
