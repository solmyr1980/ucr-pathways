# Counselor comparison data

This directory is the implementation home for counselor-app discovery data and the deterministic comparison corpus. It is separate from `data/examples/`, which contains only examples explicitly approved for the public website and/or LinkedIn.

## Authoritative programme identity and scope

The counselor corpus is keyed by the normalized registry in `data/registry/`. The stable identity is `counselor_programme_id` from `data/registry/programmes.csv`. Source rows, offered-programme UUIDs, programme-unit codes and recognized-programme codes are provenance/crosswalk identifiers, not comparison identity.

The current corpus includes only normalized targets with `production_eligible=true`, nonblank `production_order` and `programme_type=standard`. Joint/double/dual-degree targets remain valid normalized targets but are temporarily outside counselor comparison production until an approved presentation method exists.

## Production shape

Keep three concerns separate: `programmes.json` discovery metadata, `interests.json` discovery interests, and `comparisons/<counselor_programme_id>.json` deterministic comparisons. During incremental production, do not create the production indexes; leave pilot indexes unchanged until the comparison corpus is complete and quality-controlled.

## Current production contract

Current counselor production records use `schemaVersion: "1.3"`.

For every current production record, stable IDs and required normalized metadata must match `data/registry/programmes.csv`. `academicRationale` must contain `coreField`, `adjacentDirections`, `questionsApplications`, `balancedDirections`, an evidence-backed and scope-closed `thematicQuestion`, and `courseAlignment` covering exactly every scheduled course in each UCR programme.

Course traceability is role-specific: depth courses trace to `coreField`; balanced courses trace to `coreField` or selected balanced directions; thematic courses trace only to thematic basis labels. `ACCPPDE101` is the sole `ucr-required` exception.

Validate current normalized production records with `npm run validate:counselor`. The validator cross-checks registry metadata, validates rationale/course traceability, rejects fixed UCR credit allocation across comparison blocks, and emits batch warnings for suspicious thematic-course palette reuse.

## Comparison blocks

Comparison blocks are analytical alignments, not partitions. External curriculum components are not automatically blocks. There is no required number of blocks and no default 60/60/60 or fixed UCR credit allocation. Not every UCR course has to appear. Unequal EC totals and meaningful blanks are legitimate.

## Provenance and runtime

Use the crosswalks in `data/registry/` for source/offering/institution and identity-resolution provenance. `inherited-across-split-targets` interest evidence is not target-specific unless independently corroborated. Interest search locates a normalized target and then loads its fixed comparison; it never regenerates the comparison.

GitHub remains the version-controlled source of truth. The authoritative academic rules are in `docs/UCR_Pathways_Production_Instructions.md`; the reusable batch procedure is in `docs/Counselor_Batch_Assignment.md`.
