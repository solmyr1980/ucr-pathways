#!/usr/bin/env python3
"""Verify explicitly reviewed modal descriptions against their recorded workbook evidence.

Legacy cache entries remain untouched. New reviewed entries cite a selected source
field, workbook blob and hashes. This is a fidelity check, not prose approval.
"""
from pathlib import Path
import hashlib
import json
import openpyxl

root = Path(__file__).resolve().parents[1]
workbook = root / 'data/reference/ucr_courses_enriched.xlsx'
data = workbook.read_bytes()
blob = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
sheet = openpyxl.load_workbook(workbook, data_only=True).active
headers = [c.value for c in sheet[1]]
rows = {r[headers.index('osiris')]: dict(zip(headers, r)) for r in sheet.iter_rows(min_row=2, values_only=True)}
count = 0
for file in (root / 'pilot/shiny/data/courses').glob('???.json'):
    cache = json.loads(file.read_text())
    for code, source in cache.get('descriptionSources', {}).items():
        assert source['workbook'] == 'data/reference/ucr_courses_enriched.xlsx', code
        assert source['workbookBlob'] == blob, f'{code}: source workbook changed; review required'
        field = source['sourceField']
        assert field in ['profile', 'description2'], f'{code}: unsupported display-source field'
        original = rows[code][field]
        description = cache['descriptions'][code]
        assert original and description and source['reviewNote'] and source['reviewedOn'], code
        assert source['descriptionSha256'] == hashlib.sha256(description.encode()).hexdigest(), f'{code}: description changed without review'
        assert source['sourceSha256'] == hashlib.sha256(original.encode()).hexdigest(), f'{code}: source changed'
        assert source['mode'] in ['verbatim', 'edited'], code
        if source['mode'] == 'verbatim':
            assert original == description, f'{code}: verbatim source mismatch'
        count += 1
assert count >= 2, 'Reviewed modal evidence missing'
print(f'{count} reviewed course descriptions match their declared workbook evidence and text hashes.')
