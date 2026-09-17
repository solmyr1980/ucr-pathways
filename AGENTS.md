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
