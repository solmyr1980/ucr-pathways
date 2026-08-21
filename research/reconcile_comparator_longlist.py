#!/usr/bin/env python3
"""Reconcile RIO row data to the public 'offering' unit used in Step 1."""
import csv, json
from collections import defaultdict
from pathlib import Path

OUT=Path('research/comparator_longlist')
RAW=OUT/'rio_wo_bachelor_fulltime_offerings.csv'
SUMMARY=OUT/'step1_summary.json'
README=OUT/'README.md'

with RAW.open(encoding='utf-8', newline='') as f:
    rows=list(csv.DictReader(f))

groups=defaultdict(list)
for r in rows:
    code=(r.get('AANGEBODEN_OPLEIDINGCODE') or '').strip()
    if code:
        groups[code].append(r)

offerings=[]
for code,rs in groups.items():
    f=rs[0]
    names=[]
    for r in rs:
        for k in ('EIGENNAAM','NAAM_LANG','INTERNATIONALE_NAAM','EIGENNAAM_ENGELS'):
            v=(r.get(k) or '').strip()
            if v and v not in names: names.append(v)
    offerings.append({
        'programme':(f.get('EIGENNAAM') or f.get('NAAM_LANG') or '').strip(),
        'registered_name':(f.get('NAAM_LANG') or '').strip(),
        'international_name':(f.get('INTERNATIONALE_NAAM') or '').strip(),
        'institution':(f.get('ONDERWIJSAANBIEDER_NAAM') or f.get('ONDERWIJSBESTUUR_NAAM') or '').strip(),
        'official_programme_code':(f.get('ERKENDEOPLEIDINGSCODE') or '').strip(),
        'rio_programme_unit_code':(f.get('OPLEIDINGSEENHEIDCODE') or '').strip(),
        'offered_programme_code':code,
        'form':(f.get('VORM') or '').strip(),
        'languages':' | '.join(sorted({(r.get('VOERTAAL') or '').strip() for r in rs if (r.get('VOERTAAL') or '').strip()})),
        'locations':' | '.join(sorted({(r.get('ONDERWIJSLOCATIEPLAATS') or '').strip() for r in rs if (r.get('ONDERWIJSLOCATIEPLAATS') or '').strip()})),
        'website':(f.get('WEBSITE') or '').strip(),
        'all_names':' | '.join(names),
        'rio_rows':len(rs),
    })
offerings.sort(key=lambda r:(r['institution'].lower(),r['programme'].lower(),r['offered_programme_code']))

fields=list(offerings[0].keys()) if offerings else []
with (OUT/'dutch_wo_bachelor_fulltime_offerings.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(offerings)

summary=json.loads(SUMMARY.read_text(encoding='utf-8'))
summary['rio_unique_offered_programmes']=len(offerings)
summary['reconciliation_note']=(
    'AANGEBODEN_OPLEIDINGCODE is the RIO identifier for one provider offering of a programme. '
    'The offering-level view is therefore retained separately from the deduplicated programme/provider candidate view.'
)
SUMMARY.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')

sk=summary['studiekeuze123'].get('reported_full_time_offerings')
programme_count=summary.get('deduplicated_public_candidates')
text=f'''# Step 1 — Dutch WO bachelor longlist

Generated: {summary['generated']}

## Scope

Current recognised Dutch WO bachelor offerings with a full-time route. This is an external candidate universe: **no UCR feasibility filtering has been applied**.

## Counts

- Studiekeuze123 reports **{summary['studiekeuze123'].get('reported_wo_bachelor_offerings')}** WO bachelor offerings, including **{sk}** with a full-time route.
- DUO RIO contributes {summary['duo_rio'].get('retained_full_time_wo_bachelor_rows')} retained current full-time WO-bachelor rows.
- Grouping those rows by RIO `AANGEBODEN_OPLEIDINGCODE` yields **{len(offerings)} official offered-programme records**.
- Collapsing further to programme/provider identity yields **{programme_count} programme/institution candidates** for later portfolio selection.
- Existing pilot-seed marking is diagnostic only; it is not used to include or exclude candidates.

## Saved files

- `rio_wo_bachelor_fulltime_offerings.csv` — official retained RIO rows, untouched after filtering.
- `dutch_wo_bachelor_fulltime_offerings.csv` — offering-level RIO view keyed by `AANGEBODEN_OPLEIDINGCODE`.
- `dutch_wo_bachelor_fulltime_longlist.csv` — deduplicated programme/provider candidate view for Step 2.
- `step1_summary.json` — provenance and reconciliation counts.

## Boundary

No candidate has been removed because it looks difficult for UCR. UCR feasibility belongs to Step 2. Studiekeuze123 and RIO do not use exactly the same public-record unit, so their counts are retained side by side rather than artificially forced to match.
'''
README.write_text(text,encoding='utf-8')
print(f'RIO unique offered-programme codes: {len(offerings)}; programme/provider candidates: {programme_count}; Studiekeuze123 full-time count: {sk}')
