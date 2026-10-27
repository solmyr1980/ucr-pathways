# Repository operating rules

## GitHub destination and branch policy

- The canonical repository is `solmyr1980/ucr-pathways`.
- Work directly on the existing `main` branch. Do not create another branch or pull request unless the user explicitly requests one.
- Never force-push or rewrite published history.

## ChatGPT Work GitHub writes

- In ChatGPT Work, use the authenticated GitHub connector for repository writes. Do not first attempt an HTTPS `git push`; the execution environment does not provide GitHub HTTPS credentials.
- When the user says to push or upload work in this project without naming another destination, use `solmyr1980/ucr-pathways:main`.
- Immediately before writing, verify the current remote `main` SHA. Create one atomic commit on that parent and update `main` only as a fast-forward.
- After writing, verify that remote `main` points to the new commit and report the GitHub commit link.

## Validation

- Run the relevant repository validators and tests before publishing changes.

## Active counselor audit authority

- Before every counselor review publication, read fresh `data/counselor/qc/comprehensive-reaudit.json`. When `activeAudit` is present, follow its register and case directory; earlier run state is historical.
- On 27 October 2026 the user superseded the 402-case continuation with a full 438-case restart. Old continuation workers/tasks must checkpoint and stop without further academic publication. Both old schedules are paused. Do not alter the new tasks from a superseded execution.
- New workers must check their active register and `systemicPause` again immediately before each write, preserve prior evidence, and count only newly verified reviews in this audit.
