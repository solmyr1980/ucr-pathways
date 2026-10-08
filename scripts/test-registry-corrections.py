"""Guard retained-alias normalization and preserve upstream evidence."""
import copy
import csv
import importlib.util
import io
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('corrections', ROOT / 'scripts/apply-registry-corrections.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class RetainedAliasTests(unittest.TestCase):
    def setUp(self):
        self.ledger = json.loads((ROOT / 'data/registry/post-build-corrections.json').read_text())
        self.registry = (ROOT / 'data/registry/programmes.csv').read_text()
        self.alias = self.ledger['target_aliases'][0]

    def test_replay_is_idempotent_and_retains_ids(self):
        result = m.apply(self.registry, self.ledger)
        self.assertEqual(result, self.registry)
        rows = list(csv.DictReader(io.StringIO(result)))
        self.assertEqual(len(rows), 460)
        alias = next(r for r in rows if r['counselor_programme_id'] == self.alias['alias_id'])
        self.assertEqual(alias['current_status'], 'retained-alias')
        self.assertEqual(alias['production_eligible'], 'false')
        self.assertEqual(alias['production_order'], '')
        for field, value in self.alias['alias_guard'].items():
            self.assertEqual(alias[field], value)

    def test_replay_from_original_owner_and_alias(self):
        rows = list(csv.DictReader(io.StringIO(self.registry)))
        for row in rows:
            if row['counselor_programme_id'] == self.alias['owner_id']:
                row.update(self.alias['owner_guard'])
                attrs = json.loads(row['corrected_attributes_json'])
                for k in ['absorbed_alias_ids', 'post_build_alias_id']:
                    attrs.pop(k, None)
                row['corrected_attributes_json'] = json.dumps(attrs, separators=(',', ':'), ensure_ascii=False)
            if row['counselor_programme_id'] == self.alias['alias_id']:
                row.update(self.alias['alias_before'])
                row['corrected_attributes_json'] = '{}'
        out = io.StringIO(); writer = csv.DictWriter(out, fieldnames=rows[0], lineterminator='\n');writer.writeheader();writer.writerows(rows)
        self.assertEqual(m.apply(out.getvalue(), self.ledger), self.registry)

    def test_alias_chains_and_duplicate_aliases_rejected(self):
        bad = copy.deepcopy(self.ledger);bad['target_aliases'][0]['owner_id'] = self.alias['alias_id']
        with self.assertRaises(ValueError):m.apply(self.registry, bad)
        bad = copy.deepcopy(self.ledger);bad['target_aliases'].append(copy.deepcopy(self.alias))
        with self.assertRaises(ValueError):m.apply(self.registry, bad)

    def test_changed_alias_or_owner_identity_rejected(self):
        for field in ['canonical_name', 'offering_ids_json', 'source_excel_rows_json']:
            for guard in ['alias_guard', 'owner_guard']:
                bad = copy.deepcopy(self.ledger);bad['target_aliases'][0][guard][field] = '[]' if field.endswith('_json') else 'Different programme'
                with self.assertRaises(ValueError):m.apply(self.registry, bad)

    def test_crosswalks_replay_without_changing_evidence_or_row_order(self):
        for kind in ['programme_offerings', 'programme_source_rows', 'programme_interests']:
            current = (ROOT / ('data/registry/' + kind + '.csv')).read_text()
            self.assertEqual(m.alias_crosswalk(current, kind, self.ledger), current)
            rows = list(csv.DictReader(io.StringIO(current)))
            original = copy.deepcopy(rows)
            for row in original:
                if row['source_excel_row'] in {str(x) for x in json.loads(self.alias['alias_guard']['source_excel_rows_json'])}:
                    row['counselor_programme_id'] = self.alias['alias_id']
                    if kind == 'programme_source_rows':row.update(mapping_status='one-to-one', mapping_basis='step1-no-ambiguity')
                elif kind == 'programme_source_rows' and row['source_excel_row'] in {str(x) for x in json.loads(self.alias['owner_guard']['source_excel_rows_json'])}:
                    row['mapping_status'] = 'one-to-one'
            out = io.StringIO();writer = csv.DictWriter(out, fieldnames=rows[0], lineterminator='\n');writer.writeheader();writer.writerows(original)
            self.assertEqual(m.alias_crosswalk(out.getvalue(), kind, self.ledger), current)
            for before, after in zip(original, rows):
                self.assertEqual({k:v for k,v in before.items() if k not in ['counselor_programme_id','mapping_status','mapping_basis']}, {k:v for k,v in after.items() if k not in ['counselor_programme_id','mapping_status','mapping_basis']})

    def test_conflicting_crosswalk_owner_is_rejected(self):
        current = (ROOT / 'data/registry/programme_offerings.csv').read_text()
        current = current.replace(self.alias['alias_guard']['offering_ids_json'].strip('[]"') + ',212,' + self.alias['owner_id'], self.alias['alias_guard']['offering_ids_json'].strip('[]"') + ',212,cp-000200')
        with self.assertRaises(ValueError):m.alias_crosswalk(current, 'programme_offerings', self.ledger)


if __name__ == '__main__':
    unittest.main()
