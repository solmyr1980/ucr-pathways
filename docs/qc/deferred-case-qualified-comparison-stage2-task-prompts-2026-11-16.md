# Exact saved Stage 2 task prompts

Created and enabled 16 November 2026. All times are Europe/Amsterdam.

## Worker A

Schedule:

```text
BEGIN:VEVENT
DTSTART;TZID=Europe/Amsterdam:20261116T140000
RRULE:FREQ=HOURLY;INTERVAL=1;BYMINUTE=0;BYSECOND=0
END:VEVENT
```

Exact saved prompt:

```text
Execute one small UCR Pathways Stage 2 batch as worker A in solmyr1980/ucr-pathways, branch main.

Read docs/qc/deferred-case-qualified-comparison-stage2-scheduling-2026-11-16.md in full from current GitHub main and execute its common instructions, together with the Stage 2 assignment and governing documents it references. This user-authorized scheduled execution supersedes the earlier manual-only/no-new-automation restriction for these two new Stage 2 tasks only. Keep old Restart Corpus tasks paused.

Use only postAuditReviews[0].scheduling.workers.A.caseIds in the active audit register. Resume your own unfinished Stage 2 case first. Skip every completed Stage 2 review, including reviewed-but-unresolved cases. Handle at most two owned cases per run, completing and publishing each separately. Never take the other worker's cases or redo the 13 reviews completed before scheduling.

Before substantial work, acquire and publish your own expiring run claim with scripts/stage2-scheduled.py. Skip an occurrence with an unexpired claim. Renew during long work. For every subsequent write use scripts/stage2-scheduled-publication.cjs with your current token, fresh main, complete verified bytes and a non-forced expected-parent update. Stop an expired or superseded run; refresh and reconcile concurrent main changes.

Preserve all academic, feasibility, source-first verification, validation, history and release boundaries. Save partial work and exact next actions durably; technical interruptions leave this schedule enabled. Report case outcomes, commit links, actual progress and any failure. Pause only your own task when its assignment and required final integration are complete.
```

## Worker B

Schedule:

```text
BEGIN:VEVENT
DTSTART;TZID=Europe/Amsterdam:20261116T143000
RRULE:FREQ=HOURLY;INTERVAL=1;BYMINUTE=30;BYSECOND=0
END:VEVENT
```

Exact saved prompt:

```text
Execute one small UCR Pathways Stage 2 batch as worker B in solmyr1980/ucr-pathways, branch main.

Read docs/qc/deferred-case-qualified-comparison-stage2-scheduling-2026-11-16.md in full from current GitHub main and execute its common instructions, together with the Stage 2 assignment and governing documents it references. This user-authorized scheduled execution supersedes the earlier manual-only/no-new-automation restriction for these two new Stage 2 tasks only. Keep old Restart Corpus tasks paused.

Use only postAuditReviews[0].scheduling.workers.B.caseIds in the active audit register. Resume your own unfinished Stage 2 case first. Skip every completed Stage 2 review, including reviewed-but-unresolved cases. Handle at most two owned cases per run, completing and publishing each separately. Never take the other worker's cases or redo the 13 reviews completed before scheduling.

Before substantial work, acquire and publish your own expiring run claim with scripts/stage2-scheduled.py. Skip an occurrence with an unexpired claim. Renew during long work. For every subsequent write use scripts/stage2-scheduled-publication.cjs with your current token, fresh main, complete verified bytes and a non-forced expected-parent update. Stop an expired or superseded run; refresh and reconcile concurrent main changes.

Preserve all academic, feasibility, source-first verification, validation, history and release boundaries. Save partial work and exact next actions durably; technical interruptions leave this schedule enabled. Report case outcomes, commit links, actual progress and any failure. Pause only your own task when its assignment and required final integration are complete.
```

