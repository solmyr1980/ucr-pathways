# Counselor Batch Assignment

**Purpose:** Reusable execution wrapper for deterministic counselor-comparison batches  
**Default batch size:** 2 in-scope normalized counselor targets  
**Fixed UCR starting cohort:** Fall 2026  
**Repository:** `solmyr1980/ucr-pathways`  
**Academic methodology:** `docs/UCR_Pathways_Production_Instructions.md`

This assignment selects and runs a batch. It does **not** redefine counselor-production methodology.

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

1. a complete canonical JSON record at `data/counselor/comparisons/<counselor_programme_id>.json`;
2. all record-level counselor validation and completion gates passed; and
3. that completed record committed to the existing `main` branch.

Treat each selected target as an atomic resumable production unit. Do not develop several targets in parallel and postpone serialization, validation or GitHub persistence until the end of the batch. If execution stops partway through a batch, already completed and committed target records remain valid checkpoints; resume from the first selected target that does not yet have a completed current production record.

Do not restate, reinterpret or supplement the academic method from this batch assignment. If a genuine contract or registry problem is discovered, handle it in the appropriate upstream layer rather than inventing a batch-specific workaround.

Current counselor UCR scheduling uses the fixed Fall 2026 cohort defined in the Production Instructions.

Create successful production records at:

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

Commit each completed counselor comparison record to `main` before beginning the next selected target. Do not hold an entire batch as uncommitted or unserialized working state.

Do not modify public examples, `data/catalog.json`, website content, LinkedIn records, publication queues or generated PDFs as part of counselor corpus production.

Commit completed production records and only strictly necessary upstream fixes to `main`.

---

# 7. Final deliverable

Report concisely:

1. selected `counselor_programme_id`, `production_order`, programme name and institution(s);
2. number of completed comparison records;
3. unresolved/exception targets;
4. confirmation that every included UCR alternative passed mechanical feasibility validation;
5. distribution of records with one, two and three UCR alternatives, with stopping reasons for records below three;
6. material source discrepancies or registry exceptions;
7. GitHub commit containing the batch;
8. any issue that should be resolved before the next batch.

Do not stop for routine intermediate approval during a production batch.
