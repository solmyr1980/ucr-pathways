#!/usr/bin/env python3
"""Reconcile Step 1 RIO rows and clean the programme/provider candidate view."""
import csv, difflib, json, re, unicodedata
from collections import defaultdict
from pathlib import Path

OUT=Path('research/comparator_longlist')
RAW=OUT/'rio_wo_bachelor_fulltime_offerings.csv'
LONG=OUT/'dutch_wo_bachelor_fulltime_longlist.csv'
SUMMARY=OUT/'step1_summary.json'
README=OUT/'README.md'

PILOTS=[
 ('Psychobiologie',['Universiteit van Amsterdam']),
 ('Environmental Sciences',['Wageningen University','Wageningen University & Research']),
 ('Informatica',['Universiteit Utrecht','Utrecht University']),
 ('Health Sciences',['Universiteit Maastricht','Maastricht University']),
 ('Kunstgeschiedenis',['Universiteit Utrecht','Utrecht University']),
 ('Rechtsgeleerdheid',['Universiteit Utrecht','Utrecht University']),
 ('Biologie',['Universiteit Utrecht','Utrecht University']),
 ('Business Administration',['Universiteit van Amsterdam']),
 ('Psychology',['Tilburg University']),
 ('Communicatiewetenschap',['Universiteit van Amsterdam'])]

def norm(s):
 s=unicodedata.normalize('NFKD',s or '')
 s=''.join(c for c in s if not unicodedata.combining(c)).lower().replace('&',' en ')
 return re.sub(r'\s+',' ',re.sub(r'[^a-z0-9]+',' ',s)).strip()
def similar(a,b): return difflib.SequenceMatcher(None,norm(a),norm(b)).ratio()
def inst_ok(actual,allowed):
 a=norm(actual)
 return any((norm(x) in a or a in norm(x)) for x in allowed)

def read(path):
 with path.open(encoding='utf-8',newline='') as f: return list(csv.DictReader(f))
def write(path,rows):
 fields=list(rows[0].keys()) if rows else []
 with path.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

rows=read(RAW)
# Preserve one record per offered-programme UUID. This is a provenance view, not
# the final candidate universe: one recognised bachelor can have several offered
# records for language/location/premaster-style public names.
groups=defaultdict(list)
for r in rows:
 code=(r.get('AANGEBODEN_OPLEIDINGCODE') or '').strip()
 if code: groups[code].append(r)
offerings=[]
for code,rs in groups.items():
 f=rs[0]; names=[]
 for r in rs:
  for k in ('EIGENNAAM','NAAM_LANG','INTERNATIONALE_NAAM','EIGENNAAM_ENGELS'):
   v=(r.get(k) or '').strip()
   if v and v not in names: names.append(v)
 offerings.append({
  'offered_name':(f.get('EIGENNAAM') or f.get('NAAM_LANG') or '').strip(),
  'registered_programme':(f.get('NAAM_LANG') or '').strip(),
  'international_name':(f.get('INTERNATIONALE_NAAM') or '').strip(),
  'institution':(f.get('ONDERWIJSAANBIEDER_NAAM') or f.get('ONDERWIJSBESTUUR_NAAM') or '').strip(),
  'official_programme_code':(f.get('ERKENDEOPLEIDINGSCODE') or '').strip(),
  'rio_programme_unit_code':(f.get('OPLEIDINGSEENHEIDCODE') or '').strip(),
  'offered_programme_code':code,'form':(f.get('VORM') or '').strip(),
  'languages':' | '.join(sorted({(r.get('VOERTAAL') or '').strip() for r in rs if (r.get('VOERTAAL') or '').strip()})),
  'locations':' | '.join(sorted({(r.get('ONDERWIJSLOCATIEPLAATS') or '').strip() for r in rs if (r.get('ONDERWIJSLOCATIEPLAATS') or '').strip()})),
  'website':(f.get('WEBSITE') or '').strip(),'all_names':' | '.join(names),'rio_rows':len(rs)})
offerings.sort(key=lambda r:(norm(r['institution']),norm(r['registered_programme']),norm(r['offered_name'])))
write(OUT/'dutch_wo_bachelor_fulltime_offerings.csv',offerings)

# Clean the actual Step-2 candidate universe. Its identity is the registered
# bachelor name, not an arbitrary first offered-name such as a premaster label.
cands=read(LONG)
for c in cands:
 if (c.get('registered_name') or '').strip(): c['programme']=c['registered_name'].strip()
 c['pilot_seed']=''; c['pilot_match_score']=''

pilot_matches=[]
for idx,(pname,allowed_inst) in enumerate(PILOTS,1):
 best=None; bestscore=-1
 for c in cands:
  if not inst_ok(c.get('institution',''),allowed_inst): continue
  names=[x.strip() for x in (c.get('all_registered_names') or c.get('programme') or '').split(' | ') if x.strip()]
  if not names: names=[c.get('programme','')]
  score=max(similar(pname,n) for n in names)
  if score>bestscore: best,bestscore=c,score
 if best is not None and bestscore>=0.58:
  best['pilot_seed']=f'pilot-{idx:02d}'; best['pilot_match_score']=f'{bestscore:.3f}'
  pilot_matches.append({'seed':best['pilot_seed'],'programme':best['programme'],'institution':best['institution'],'code':best['official_programme_code'],'score':best['pilot_match_score']})
cands.sort(key=lambda r:(norm(r['institution']),norm(r['programme'])))
write(LONG,cands)

summary=json.loads(SUMMARY.read_text(encoding='utf-8'))
summary['rio_unique_offered_programmes']=len(offerings)
summary['deduplicated_programme_provider_candidates']=len(cands)
summary['pilot_seeds_found']=len(pilot_matches)
summary['pilot_seed_matches']=pilot_matches
summary['reconciliation_note']=(
 'RIO offered-programme UUIDs are preserved as a provenance view. The Step-2 candidate universe uses the registered bachelor identity at programme/provider level, so alternate offered names (including premaster labels attached to the same recognised programme) do not become separate comparator programmes.')
SUMMARY.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')

sk=summary['studiekeuze123'].get('reported_full_time_offerings')
text=f'''# Step 1 — Dutch WO bachelor longlist

Generated: {summary['generated']}

## Scope

Current recognised Dutch WO bachelor programmes with a full-time route. This is an external candidate universe: **no UCR feasibility filtering has been applied**.

## Counts

- Studiekeuze123 reports **{summary['studiekeuze123'].get('reported_wo_bachelor_offerings')}** WO bachelor offerings, including **{sk}** with a full-time route.
- DUO RIO contributes {summary['duo_rio'].get('retained_full_time_wo_bachelor_rows')} retained current full-time WO-bachelor rows.
- Those rows contain **{len(offerings)} offered-programme UUIDs**; this is retained as an audit/provenance view because one registered bachelor can have several offered records.
- Collapsing to the registered bachelor + provider identity yields **{len(cands)} programme/institution candidates**. This is the frozen external longlist for Step 2.
- **{len(pilot_matches)}/10** existing pilot seeds were automatically located; this marker is diagnostic only and does not affect the longlist.

## Saved files

- `rio_wo_bachelor_fulltime_offerings.csv` — retained official RIO rows.
- `dutch_wo_bachelor_fulltime_offerings.csv` — RIO offered-programme provenance view.
- `dutch_wo_bachelor_fulltime_longlist.csv` — registered programme/provider candidate universe for Step 2.
- `step1_summary.json` — provenance and reconciliation counts.

## Boundary

No candidate has been removed because it looks difficult for UCR. UCR feasibility belongs to Step 2. Studiekeuze123 and RIO use different public-record units, so their counts are retained side by side rather than artificially forced to match. The candidate view uses the registered bachelor identity so premaster or other alternate offered names attached to that bachelor do not become separate comparator programmes.
'''
README.write_text(text,encoding='utf-8')
print(f'candidate programmes={len(cands)}; offered UUIDs={len(offerings)}; pilot matches={len(pilot_matches)}/10; SK123 full-time={sk}')
