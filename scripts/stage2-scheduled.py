#!/usr/bin/env python3
"""Select and fence disjoint Stage 2 scheduled runs; publish changes through Work's connector.

This writes only the selected worker's small claim file. It does not publish,
approve a case, or infer that an unresolved academic case is complete.
"""
import argparse
import datetime as dt
import json
from pathlib import Path
import uuid

ROOT = Path(__file__).resolve().parents[1]
REGISTER = 'data/counselor/qc/full-restart-2026-10-27.json'
PROCESS = 'qualified-comparison-stage2-2026-11-15'

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def stamp(now):
    return now.astimezone(dt.timezone.utc).isoformat().replace('+00:00', 'Z')

def instant(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00'))

def context(root):
    pointer = read(root / 'data/counselor/qc/comprehensive-reaudit.json')
    if pointer.get('activeAudit', {}).get('register') != REGISTER:
        raise ValueError('Stage 2 active audit was superseded')
    audit = read(root / REGISTER)
    if audit.get('systemicPause') is not None:
        raise ValueError('Active audit has a systemic pause')
    review = next(x for x in audit['postAuditReviews'] if x['id'] == PROCESS)
    config = review['scheduling']
    if config.get('status') != 'enabled':
        raise ValueError('Stage 2 scheduling is paused or exhausted')
    queues = [config['workers'][k]['caseIds'] for k in ['A', 'B']]
    all_ids = config['completedBeforeScheduling'] + queues[0] + queues[1]
    if len(all_ids) != len(set(all_ids)) or set(all_ids) != set(review['caseIds']):
        raise ValueError('Scheduled assignments overlap or do not partition Stage 2')
    complete = set()
    active = set()
    for case_id in review['caseIds']:
        case = read(root / audit['caseEvidenceDirectory'] / f'{case_id}.json')
        progress = case.get('stage2Review', {})
        if progress.get('process') == PROCESS:
            if progress.get('status') == 'completed':
                complete.add(case_id)
            elif progress.get('status') == 'in-progress':
                active.add(case_id)
    # Full evidence hashes/input versions are checked by validate-comprehensive-reaudit.py.
    if not set(config['completedBeforeScheduling']) <= complete:
        raise ValueError('A protected completed Stage 2 review was reopened')
    return config, complete, active

def select(queue, complete, active):
    pending = [i for i in queue if i not in complete]
    return ([i for i in pending if i in active] + [i for i in pending if i not in active])[:2]

def transition(state, action, worker, token, selected, now, lease_minutes=90, integration=False):
    current = state.get('activeClaim')
    live = current and instant(current['expiresAt']) > now
    if action == 'claim':
        if live:
            raise ValueError(f"Worker {worker} already has an unexpired claim; skip this occurrence")
        if not selected and not integration:
            return state, {'status': 'exhausted', 'worker': worker}
        if current:
            state.setdefault('claimHistory', []).append({**current, 'closedAs': 'expired', 'closedAt': stamp(now)})
        current = {'token': token or str(uuid.uuid4()), 'worker': worker,
                   'caseIds': selected, 'startedAt': stamp(now), 'heartbeatAt': stamp(now),
                   'expiresAt': stamp(now + dt.timedelta(minutes=lease_minutes))}
        if integration:
            current['purpose'] = 'final-integration'
        state['activeClaim'] = current
    else:
        if not live or current.get('token') != token or current.get('worker') != worker:
            raise ValueError('Lost, expired or superseded run claim; stop without publishing case changes')
        if action == 'renew':
            current['heartbeatAt'] = stamp(now)
            current['expiresAt'] = stamp(now + dt.timedelta(minutes=lease_minutes))
        elif action == 'release':
            state.setdefault('claimHistory', []).append({**current, 'closedAs': 'released', 'closedAt': stamp(now)})
            state['activeClaim'] = None
    return state, {'status': action, 'worker': worker, 'claim': current}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['status', 'claim', 'check', 'renew', 'release'])
    parser.add_argument('--worker', choices=['A', 'B'], required=True)
    parser.add_argument('--token')
    parser.add_argument('--case')
    args = parser.parse_args()
    config, complete, active = context(ROOT)
    worker = config['workers'][args.worker]
    claim_path = ROOT / worker['claimRef']
    state = read(claim_path)
    selected = select(worker['caseIds'], complete, active)
    if args.action == 'status':
        print(json.dumps({'worker': args.worker, 'completedStage2': len(complete),
                          'remainingOwn': [i for i in worker['caseIds'] if i not in complete],
                          'nextCases': selected, 'activeClaim': state.get('activeClaim')}, indent=2))
        return
    if args.action != 'claim' and not args.token:
        parser.error('--token is required after acquiring a claim')
    state, result = transition(state, args.action, args.worker, args.token, selected,
                               dt.datetime.now(dt.timezone.utc), config['leaseMinutes'],
                               integration=len(complete) == 61 and not (ROOT / config['finalReportRef']).is_file())
    if args.case and (args.case not in result.get('claim', {}).get('caseIds', [])
                      or args.case not in worker['caseIds']):
        raise ValueError('Case is outside this run claim or worker assignment')
    if args.action in ['claim', 'renew', 'release'] and result['status'] != 'exhausted':
        claim_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    try:
        main()
    except ValueError as error:
        raise SystemExit(str(error))
