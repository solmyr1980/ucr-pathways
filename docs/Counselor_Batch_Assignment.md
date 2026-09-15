# Counselor Batch Assignment

**Purpose:** Reusable execution wrapper for deterministic counselor-comparison batches  
**Default batch size:** 2 in-scope normalized counselor targets  
**Fixed UCR starting cohort:** Fall 2026  
**Repository:** `solmyr1980/ucr-pathways`  
**Academic methodology:** `docs/UCR_Pathways_Production_Instructions.md`

This assignment selects and runs a batch. It does **not** redefine counselor-production methodology.

---

# 0. Execution model and division of labour

Use **normal Chat as the default execution surface for routine counselor production**. Do not send ordinary production targets to Work merely because the task is substantial.

The intended division of labour is:

- **Normal Chat** owns the academic work: retrieving the governing GitHub rules, researching the external programme, assessing programme-interest evidence, using the enriched UCR course Project Source, designing alternatives, selecting and scheduling courses, writing the compact v2 decision file, committing that decision to `main`, monitoring the resulting GitHub Actions run, and repairing ordinary decision-level failures.
- **GitHub Actions** owns deterministic execution: compiling the compact decision into canonical schema 2.0, running the unchanged validators, publishing the canonical comparison only after validation passes, and refreshing the counselor review indexes.
- **Work** is reserved for one-time or exceptional infrastructure engineering that materially benefits from its own execution environment or full-repository filesystem access: compiler/schema development, migrations, regression-harness work, repository-wide diagnostics, or implementation problems that cannot be handled safely and efficiently through normal Chat plus GitHub Actions. Work is not the routine academic-production engine.

Conserve Work usage. If normal Chat can make the academic decisions and GitHub Actions can perform the deterministic build/validation/publish steps, do not use Work.

When Work is genuinely required, normal Chat must formulate a self-contained copy-paste assignment for it. The user should not have to translate the technical requirements between the two environments. That assignment must state, where relevant:

1. the exact objective and governing GitHub sources;
2. the files or behaviours that are frozen and must not change;
3. explicit non-destructive boundaries;
4. quantitative success criteria where the objective can otherwise be interpreted loosely;
5. regression cases and unchanged validators that must continue to pass;
6. clear stop conditions for unsafe or ambiguous outcomes; and
7. the exact final evidence/report required for independent review.

For risky infrastructure changes, separate **prototype/proof** from **migration**. First prove the proposed architecture in temporary or non-production state; only after independent review should a second assignment migrate it into production.

After Work reports completion, normal Chat must independently inspect the actual GitHub repository state, relevant diffs/files, and GitHub Actions results before accepting the implementation. A Work report by itself is not sufficient evidence that the intended objective was achieved.

Routine production failures remain in normal Chat. If the compiler succeeds but an unchanged validator rejects a decision, diagnose and repair the academic/decision input and rerun the same target. Do not weaken a validator or redesign the infrastructure merely to make one target pass. Escalate back to Work only when repeated failures reveal a genuine structural tooling problem rather than an ordinary decision inconsistency.

The responsibility boundary remains unchanged regardless of execution surface: **AI makes academic decisions; deterministic code expresses, checks and publishes them.** Work may implement or repair that code, but it must not become the source of routine academic judgement.

---

# 1. Retrieve the governing sources

Before starting a batch, retrieve the current GitHub versions of:

- `docs/UCR_Pathways_Master_Specification.md`;
- `docs/UCR_Pathways_Production_Instructions.md`.

For ordinary counselor production, do **not** load the Web/LinkedIn Workflow or Supporting Research Workflows; they govern different tasks.

Inspect the current implementation needed for the batch:

- `data/registry/programmes.csv`;
- `data/registry/programme_interests.csv`;
- `data/registry/README.md`;
- `data/counselor/README.md`;
- current counselor comparison schema and validator;
- the active v2 counselor decision contract and compiler;
- the current enriched UCR course database.

Inspect registry crosswalk/provenance files or existing comparison records only when they are needed to resolve a selected target or determine whether a current production record already exists.

Use current GitHub/Project Source data rather than remembered instructions or superseded copies.

---

# 2. Select the batch

Unless the user specifies otherwise, select the next **2** targets in ascending `production_order` from `data/registry/programmes.csv` that satisfy the current production-scope rules in the Master/Production Instructions and do not already have a completed current production record requiring no repair.

A target outside the current production scope does not consume a batch slot.

Do not replace a genuinely blocked selected in-scope target with a later target merely to maintain 2 completed records. Complete the remainder and report the blocker.

Pilot search fixtures and public examples do not count as completed production counselor records.

---

# 3. Execute each target

Process **one selected target end-to-end before moving to the next**.

For each target, execute the canonical counselor production pipeline in **Section 4 of the Production Instructions** exactly as written, including its evidence, sequential alternative-selection, course-traceability, feasibility, comparison and record gates.

A target is not considered processed merely because its comparator, alternative concepts, course sets or schedules have been worked out. Before beginning work on the next selected target, the current target must have:

1. a complete compact `decisionSchemaVersion: "2.0"` academic decision file committed at `data/counselor/decisions/<counselor_programme_id>.json`;
2. a successful GitHub Actions compiler and validation run;
3. a complete canonical JSON record published at `data/counselor/comparisons/<counselor_programme_id>.json`;
4. all record-level counselor validation and completion gates passed; and
5. that completed canonical record committed to the existing `main` branch.

Treat each selected target as an atomic resumable production unit. Do not develop several targets in parallel and postpone serialization, validation or GitHub persistence until the end of the batch. If execution stops partway through a batch, already completed and committed target records remain valid checkpoints; resume from the first selected target that does not yet have a completed current production record.

Do not restate, reinterpret or supplement the academic method from this batch assignment. If a genuine contract or registry problem is discovered, handle it in the appropriate upstream layer rather than inventing a batch-specific workaround.

Current counselor UCR scheduling uses the fixed Fall 2026 cohort defined in the Production Instructions.

Record completed academic decisions at:

`data/counselor/decisions/<counselor_programme_id>.json`

The production workflow publishes successful canonical records at:

`data/counselor/comparisons/<counselor_programme_id>.json`

During incremental production, leave pilot discovery indexes unchanged and do not create final production discovery indexes until the corpus is complete and quality-controlled.

---

# 4. Exceptions

Follow the exception rules in the Production Instructions.

In particular:

- do not guess unresolved external-programme structure;
- do not silently change normalized target identity;
- do not substitute a later target for a blocked selected target;
- do not manufacture an additional UCR alternative merely to reach three;
- if the next alternative fails the evidence, coherence, distinctness or feasibility gates, stop at the number already completed and record the stopping reason.

Continue with the remaining selected targets and report the exception.

---

# 5. Batch quality control

After every individually completed record has passed the record-level completion gates in the Production Instructions and has been committed as required by Section 3:

1. run automated counselor validation across all completed current production records;
2. run the **batch-level counselor QC** in Section 9.2 of the Production Instructions;
3. repair only genuine failures; do not alter sound records merely to create superficial variety.

Batch-level QC may produce a later corrective commit, but it does not replace the per-target persistence checkpoint in Section 3.

---

# 6. GitHub working rules

Work only on the existing `main` branch.

Do not create another branch, pull request, duplicate repository structure or repository reorganization.

Commit one completed counselor decision file to `main`. Let the counselor compiler workflow generate, validate and publish its canonical comparison before beginning the next selected target. Do not hand-edit or directly commit a new canonical comparison, and do not hold an entire batch as uncommitted or unserialized working state.

New production decision files must use v2. Decision schema v1 and its compiler remain available only as a documented recovery fallback and regression reference; do not submit a new v1 production decision unless a manual recovery decision explicitly authorizes it.

Do not modify public examples, `data/catalog.json`, website content, LinkedIn records, publication queues or generated PDFs as part of counselor corpus production.

Commit completed decision files and only strictly necessary upstream fixes to `main`. The GitHub Action commits the validated canonical production record. It must not overwrite an existing canonical comparison.

---

# 7. Final deliverable

Report concisely:

1. selected `counselor_programme_id`, `production_order`, programme name and institution(s);
2. number of completed comparison records;
3. unresolved/exception targets;
4. confirmation that every included UCR alternative passed mechanical feasibility validation;
5. distribution of records with one, two and three UCR alternatives, with stopping reasons for records below three;
6. material source discrepancies or registry exceptions;
7. GitHub decision and generated-canonical commits containing the batch;
8. any issue that should be resolved before the next batch.

Do not stop for routine intermediate approval during a production batch.
