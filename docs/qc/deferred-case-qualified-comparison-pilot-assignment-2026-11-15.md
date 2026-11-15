# UCR Pathways — Deferred-case materiality standard and ten-case pilot

**Status:** User-authorized, non-production pilot assignment for ChatGPT Work (15 November 2026).  
**Repository:** `solmyr1980/ucr-pathways`, branch `main`.  
**Scope:** Draft and test a proposed acceptance policy, **without changing production decisions, records, review settings or release authority**. A further user decision is required before adopting any standard or implementing disposition changes.

## 1. Why this assignment exists

The full counselor-corpus restart review (`counselor-full-restart-2026-10-27`) completed on 14 November 2026. Both workers exhausted their normal queues and permitted revisits and disabled their automations. The fixed scope was 438 cases, of which **367 received verified final dispositions** and **71 remain deferred/incomplete** (Worker A: 28; Worker B: 43). Of the 367, the final assessment records 305 comparisons, 61 no-defensible-UCR-matches and one registry exception. The 71 deferrals are *not* approved comparisons or no-matches. Do not resume/restart the exhausted workers.

The current rules require reconstruction of a coherent external 180-EC pathway, including sufficiently supported curricular status and relevant progression conditions, before approval. During the audit, some cases remained deferred because external materials about the applicable cohort were unpublished, contradictory or inaccessible, even where the academic identity and UCR alternatives might already be sufficiently clear. The aim is to test whether **academic comparability** can sometimes be established without complete **administrative/curriculum reconstruction**, while protecting against misleading comparisons, unsupported content and invented credits.

On 15 November 2026, the user approved **developing a proposed materiality-based standard and testing it on ten selected cases**, but **did not authorize a permanent policy change, any new production approvals, data/schema/app edits or final release**. The user wants the pilot conducted in ChatGPT Work and its findings retained in GitHub. This file is the durable handoff; a new Work session should not need the previous ChatGPT conversation.

## 2. Sources and governing documents: read before the pilot

Read the **current** GitHub versions of the relevant files. Do not rely on conversation memory or outdated copies:

1. `AGENTS.md` — branch, GitHub publication and validation rules.
2. `docs/qc/counselor-comprehensive-reaudit-protocol.md` — six-stage audit protocol, especially **“Current full-restart: agreed next action after case processing (2 November 2026)”**. That section already authorizes analytical reassessment of deferrals and consideration of qualified comparisons, but not automatic policy revision or production approval.
3. `docs/UCR_Pathways_Production_Instructions.md` — current formal acceptance threshold, especially §§2.1 and 9 and the evidence/approval rules. This remains authoritative during the pilot. Consult `docs/UCR_Pathways_Master_Specification.md` only where product interpretation, presentation or technical compatibility materially affects the recommendation.
4. `data/counselor/qc/comprehensive-reaudit.json` — authoritative pointer to active audit. Follow to `data/counselor/qc/full-restart-2026-10-27.json` for the current case list and statuses.
5. **Final overall assessment:** `docs/qc/evidence/counselor-full-restart-2026-10-27/cp-000458/overall-assessment-37.json`. Its `remainingDeferrals` array enumerates all 71 and records each blocker and permitted revisit status. The full audit evidence of each pilot case is under `data/counselor/qc/full-restart-2026-10-27/cp-XXXXXX.json` and `docs/qc/evidence/counselor-full-restart-2026-10-27/cp-XXXXXX/`.
6. For each case, inspect the existing `data/counselor/decisions/cp-XXXXXX.json`, `data/counselor/comparisons/cp-XXXXXX.json`, relevant official-source references, and any material reviewed UCR course evidence and renderer/presentation rules. Inspect actual source records rather than accepting the summarized blocker uncritically.

Current research and previous audits may be reused where verifiable. If a fresh primary source is needed to answer a *material* question, check it selectively; do not automatically redo external research or seek unattainable new-cohort details. Do not mistake a source URL, summary or historical approval for direct verification.

## 3. Proposed standard to evaluate, not adopt

Consider four possible **academic dispositions**:

- **Verified comparison:** Meets the current complete, evidence-supported acceptance standard.
- **Qualified comparison:** The external programme's identity and defining academic substance are adequately evidenced; the UCR alternative is substantively relevant and independently feasible; the remaining uncertain detail does not plausibly reverse the comparison; the uncertainty and exact limits are communicated accurately without implying a fully verified external 180-EC pathway.
- **No defensible UCR match:** Sufficient evidence establishes that UCR cannot supply a meaningful academic alternative to the programme's defining substance. Incomplete administrative detail does not automatically block a defensible negative conclusion, but missing defining academic information does.
- **Unresolved:** Missing/contradictory information could materially change the external academic profile, route, substantive comparison, feasibility, or reader interpretation.

A qualified comparison must never fabricate missing course titles, credits, restrictions, prerequisites, thesis arrangements, routes or permission to enrol. It must not use a partial external curriculum as though it were complete. It should disclose the limitation in language useful to a prospective student or counselor, not transfer raw investigation logs to readers. Existing verified UCR alternatives do not in themselves establish that the external programme is comparable.

For each case explicitly test: **If the unknown fact were resolved in a plausible alternative way, could it materially change the external programme's defining content or the UCR comparison?** Assess both the strongest argument for qualification and the strongest reason to retain the deferral. Distinguish uncertainty about defining academic substance from mere formal credit bookkeeping or administrative progression. Verify whether a proposed qualification fits existing data/schema/UI semantics; if not, recommend the smallest supportable change rather than shoehorning it into current flags.

## 4. Pilot cases (process exactly these ten)

The sample deliberately contains small and large inconsistencies, formal-access questions and incomplete future-cohort curricula. Do not assume any candidate will qualify.

| Case | Programme | Recorded issue to test |
|---|---|---|
| `cp-000250` | Clinical Technology (TU Delft/Leiden/Erasmus) | 180 versus 181 EC documentation conflict |
| `cp-000060` | Dutch Language and Culture (Radboud) | Repeated 5 EC Psycholinguistics module |
| `cp-000033` | Business Administration (Radboud) | New curriculum versus old thesis-entry prerequisites |
| `cp-000396` | Tax Law (UvA) | Compulsory course apparently restricted to minor enrolment |
| `cp-000440` | Business and Consumer Studies (Wageningen) | Thesis-chair preparation guide unavailable |
| `cp-000317` | Law (Leiden) | Unpublished revised-cohort final 30 EC |
| `cp-000277` | African Studies (Leiden) | Unnamed compulsory second-year 5 EC module |
| `cp-000099` | Health and Life Sciences (VU) | Substantial later-year curriculum unknown; only 90 EC verified |
| `cp-000072` | Spanish Language and Culture (Radboud) | Duplicated credits and substantial route/thesis/mobility uncertainties |
| `cp-000266` | Industrial Design (Eindhoven) | Official 185 versus 180 EC framework conflict |

For each, review the latest deferral, all substantive prior findings and existing UCR alternatives; identify the controlling cohort and course-credit evidence where relevant. The pilot is a materiality evaluation, not a fresh six-stage production run.

## 5. Required case-by-case output

For **every** pilot case produce a compact but specific analytical record with:

1. Programme, institution, case ID, applicable cohort/route, existing status and what the audit actually established.
2. Precise unresolved facts, source references, and a clear separation of verified facts from inference or candidate assumptions.
3. What is sufficiently known about the external programme's defining substance and available UCR response. Distinguish substantial comparability from mere mechanical 24-course feasibility.
4. Materiality test: best case for approval/qualification; strongest counterargument; a plausible adverse resolution of the missing fact and its effect on the comparison; whether a no-match can instead be defended.
5. **Proposed disposition** under the *hypothetical* standard: verified / qualified / no-match / unresolved, with confidence and concise academic justification. No disposition is implemented during this pilot.
6. For a proposed qualified comparison: the **exact permitted assumptions or unknowns**, a concrete draft of honest reader-facing limitation text, and what **must not** be claimed.
7. Any narrow additional evidence that is indispensable; whether it is realistically obtainable; what already reviewed material can be preserved.
8. Any necessary change to case schema, validators, renderer, presentation, or approval/QC workflow **as a proposal only**, including risks of misunderstanding.

If a supposed administrative detail proves academically material, record that finding and keep the case unresolved. Treat the earlier 37/24/10 screening of the whole 71 as a preliminary conversational hypothesis, **not** a prior approval count or target.

## 6. Pilot assessment and decision recommendation

After the ten reviews, synthesize:

- A concise, operational proposed **materiality/qualified-comparison acceptance rule**, with necessary evidence, explicit decision thresholds, appropriate uncertainty wording, and failure conditions.
- Pilot disposition counts, with case IDs, and an explanation of genuinely hard or borderline examples.
- Risks of false-positive UCR comparability, incorrect claims about complete external curricula, user-facing confusion, and possible loss of comparability across the already verified corpus.
- The smallest necessary downstream changes to governing instructions, case representations, validation and UI, if any. Distinguish changes essential to support a qualified comparison from optional features. Do not assume a new status enum is necessary without checking the existing schema.
- Recommendation whether the pilot supports adopting the new standard, modifying it, or abandoning it; concrete scope and QA strategy for the other 61 unresolved cases, including opportunities to resolve shared issues together.
- Which decisions require the user's approval before any production changes. Explicitly note that **367 previously verified dispositions are preserved** unless later evidence identifies a material issue.

Do **not** promise that all 71 cases will be approved or that a particular number of qualified comparisons will succeed. Consider no-match where genuinely warranted.

## 7. Deliverable, publication and boundaries

Produce a polished, self-contained **pilot results and policy recommendation** document in the repository:

`docs/qc/deferred-case-qualified-comparison-pilot-results-2026-11-15.md`

It must include a case-by-case table and specific case explanations, the proposed acceptance rule, any required code/schema/presentation modifications, and a clear decision request to the user. Include direct links to relevant existing case evidence and sufficiently specific official sources.

The pilot may **create/update this analysis document only**. The other listed GitHub files are **read-only** for this pilot. Do not edit case decisions/canonicals, statuses, registries, audit registers, scripts, existing production instructions, the Master Specification, the protocol, app code or deployed data. Do not create/resume scheduled tasks, change model settings, publish discovery, deploy or authorize final release. Do not implement a new comparison policy before the user's separate decision on pilot results.

Follow `AGENTS.md`: work on `main` without a PR; use the authenticated GitHub connector for writes, verify the current parent and commit, and verify the published file. Report the document link and a short executive summary in Work mode. If a source is genuinely inaccessible, state precisely what was checked and how the limitation affects the recommendation; preserve the usable analysis rather than silently guessing.

**Success criterion:** A decision-quality test of whether a proportionate, academically safe qualified-comparison standard improves outcomes for the ten deliberately varied cases, with reproducible evidence and no changes to production dispositions.
