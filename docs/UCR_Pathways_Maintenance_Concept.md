# UCR Pathways — Maintenance Concept Note

**Status:** Exploratory design note — no maintenance approach has yet been adopted.

**Date:** 2026-09-17

## Purpose

This note records current thinking about how UCR Pathways might be maintained across academic years. It is intended to preserve the reasoning developed during the initial production phase so that future maintenance does not have to be designed from scratch.

This document is **not authoritative**. It does not change the Master Specification, Production Instructions, Web and LinkedIn Workflow, registry rules, production scope or validation requirements. If a maintenance approach is later adopted, the durable rules should be incorporated into the appropriate authoritative documentation.

## Working principle

The initial production year creates a substantial corpus of normalized programme identities, programme-interest evidence, reconstructed external curricula and validated UCR comparisons. Annual maintenance should therefore normally be **incremental rather than a full rebuild**.

The working assumption is:

> Preserve stable records, detect meaningful changes, and re-research or regenerate only the records affected by those changes.

A full regeneration of the complete counselor corpus should be unnecessary unless a future change to the product model, source data or validation rules makes existing records structurally obsolete.

## 1. Programme registry refresh

A future annual refresh would begin with a new DUO/RIO source snapshot and reconcile it against the existing normalized counselor registry.

Existing `counselor_programme_id` values should remain permanent. The refresh should distinguish at least:

- unchanged programmes;
- administrative or naming changes that do not alter the academic target;
- materially changed programmes;
- discontinued, inactive or teach-out programmes;
- genuinely new programme targets.

Existing targets should retain their IDs wherever academic identity is continuous. Only genuinely new normalized targets should receive new IDs.

The purpose of the refresh is therefore reconciliation, not recreation of the normalized registry from worksheet order.

## 2. External bachelor curriculum refresh

Existing counselor comparisons already depend on current official university evidence and preserve source and curriculum metadata. A future maintenance cycle could use that provenance to check whether each external comparator has materially changed.

Possible outcomes include:

- **no material change** — retain the existing comparator and update verification metadata if appropriate;
- **minor presentational or source change** — update source metadata without reconstructing the comparison;
- **material curriculum change** — reconstruct the affected external comparator and reassess the corresponding UCR alternatives and comparison structure;
- **programme discontinuation or identity change** — treat as a registry/lifecycle case rather than silently retaining an obsolete comparator.

The threshold for what counts as a material curriculum change has not yet been defined.

## 3. UCR curriculum refresh

A new annual enriched UCR course database could be compared with the preceding version to identify changes such as:

- courses added;
- courses removed;
- changed prerequisites;
- changed semester availability;
- materially revised course content or profile;
- changed course codes or identities where relevant.

Changes that directly affect courses already used in counselor comparisons create a clear dependency: every affected comparison can be identified and revalidated or repaired selectively.

Examples:

- a removed UCR course affects every comparison that currently uses that course;
- a changed prerequisite may make some existing semester schedules infeasible;
- changed semester availability may require rescheduling or replacement;
- a major content revision may make a course more or less suitable for the concept it currently serves.

## 4. New UCR courses require a broader check

New UCR courses create a different maintenance problem. Existing records cannot refer to a course that did not exist when they were produced, yet the new course may improve some existing counselor comparisons.

A simple dependency check would therefore be insufficient. A possible annual approach is to identify the academic areas materially affected by new or substantially revised UCR courses and re-examine the counselor targets connected to those areas.

This should remain targeted. The presence of a new course should not automatically trigger regeneration of the entire corpus.

The exact method for identifying affected targets has not yet been designed.

## 5. Programme-interest evidence

The existing programme-interest corpus should be treated as accumulated production evidence rather than something that is routinely discarded and regenerated each year.

A future refresh would most likely concentrate on:

- genuinely new programme targets;
- programmes whose academic identity has materially changed;
- programmes for which current official evidence shows that earlier interest evidence has become misleading or obsolete;
- specific areas where maintenance of counselor discovery or production requires updated evidence.

Routine annual re-research of the full programme-interest corpus would normally be unnecessary.

## 6. Comparison-level maintenance

The intended maintenance model would distinguish several levels of intervention:

| Situation | Likely action |
| --- | --- |
| Sources and curricula materially unchanged | Keep existing record; reverify metadata where needed |
| Minor source or administrative change | Update metadata only |
| UCR course becomes infeasible in an existing alternative | Repair and revalidate the affected alternative/comparison |
| External curriculum changes materially | Reconstruct comparator and reconsider affected UCR alternatives |
| New UCR course materially improves an academic area | Targeted reassessment of relevant counselor comparisons |
| New or substantially changed UCR courses address the documented gap in a `no-defensible-ucr-match` exception | Reconsider that exception and publish a comparison only if a defensible 24-course closest match is now possible |
| New normalized Dutch bachelor target | Run normal production for the new target |
| Programme discontinued or structurally transformed | Apply registry/lifecycle decision and update or retire downstream comparison as appropriate |

Any repaired or regenerated canonical record would then flow through the existing downstream rendering and publication architecture rather than requiring separate manual maintenance of each surface.

## 7. Possible annual maintenance sequence

A future maintenance cycle could therefore follow this broad order:

1. obtain the new DUO/RIO snapshot;
2. reconcile the normalized programme registry while preserving permanent counselor IDs;
3. compare the new UCR enriched course database with the previous version;
4. check external programme curricula for meaningful changes;
5. identify counselor comparisons affected by external or UCR changes;
6. identify academic areas that may benefit from newly introduced UCR courses;
7. refresh programme-interest evidence only where required;
8. revalidate, repair or regenerate the affected comparisons;
9. produce comparisons for genuinely new targets;
10. rebuild downstream counselor/public representations from the maintained canonical records.

This sequence is provisional. It records the present logic rather than an adopted operating procedure.

## 8. Design questions left open

Before an annual maintenance workflow is adopted, at least the following questions would need explicit decisions:

- What constitutes a **material** external curriculum change?
- How should changes in official programme URLs or source structure be detected efficiently?
- How should yearly UCR course-database versions be compared mechanically?
- How should new UCR courses be mapped to potentially affected counselor targets without reviewing the entire corpus?
- When does an improved new UCR course justify revising an otherwise valid existing comparison?
- How much annual revalidation should occur even when no source change is detected?
- Should maintenance status and last-checked information become explicit fields in canonical records or a separate maintenance index?
- How should discontinued or teach-out external programmes be represented in the counselor corpus over time?
- At what point should programme-interest evidence be treated as stale enough to require re-research?

These questions should be resolved only when the maintenance workflow is actually designed and tested.

## 9. Current conclusion

The current UCR Pathways architecture appears compatible with a maintenance model in which the expensive first-year production creates durable assets and later years focus on reconciliation, change detection, targeted revalidation and selective regeneration.

This is preferable in principle to rebuilding the entire corpus annually, but it remains a design hypothesis rather than an adopted rule. The next maintenance cycle should use this note as a starting point, assess what has actually changed in the data and curricula, and then formalize only the rules that prove necessary.
