# Alumni Outcomes Enrichment Layer

**Status:** Future idea

**Current decision:** Do not interrupt counselor comparison production. Implement this only after the counselor comparison corpus is sufficiently complete.

**Core principle:** Alumni outcomes enrich completed comparisons but do not influence academic programme construction.

## Purpose

Create a separate post-production enrichment layer that shows demonstrated post-UCR educational trajectories. Its basic claim should remain limited and factual: UCR graduates have subsequently attended particular master's programmes.

The layer should help counselors and students understand the range of destinations that UCR graduates have actually reached. It should not be used to infer that a generated UCR curriculum guarantees admission to a particular master's programme.

## Architectural boundary

The current counselor comparison remains the authoritative academic object. Alumni outcomes must not determine:

- which UCR courses are selected;
- which UCR alternatives are generated;
- whether an alternative is academically coherent;
- whether a UCR alternative is feasible;
- whether a current student is eligible for a particular master's programme.

An alumni precedent is evidence of a historical trajectory, not an admissions guarantee.

Keep the alumni layer in a separate normalized dataset that can be joined to counselor comparisons when needed. Do not insert alumni data manually into every canonical counselor record. This separation must allow the matching logic to evolve without regenerating the academic comparison corpus.

Conceptually:

`counselor target -> canonical academic comparison`

`counselor target -> alumni-outcomes relevance layer -> normalized master's destinations`

The second relationship must never feed back into the first.

## Proposed implementation stages

### 1. Normalize the alumni records

Transform the existing post-UCR degree fields into one row per alumnus × postgraduate degree. Preserve the original source wording alongside normalized fields such as:

- country;
- city;
- institution;
- degree level;
- programme name;
- field or disciplinary direction where defensible.

Personal identity should not be required in the application-facing dataset.

### 2. Create a destination registry

For Dutch destinations, map alumni master's programmes against the current DUO/RIO WO-master programme-provider universe.

Preserve historical programme names where programmes have been renamed, merged, or discontinued rather than treating the historical destination as automatically identical to a current programme.

International master's destinations should eventually receive their own normalized identities rather than being forced into the Dutch registry.

### 3. Preserve mapping confidence

Every alumni-destination normalization should carry an explicit mapping status, for example:

- `exact`;
- `renamed-successor`;
- `probable`;
- `unresolved`.

Only sufficiently reliable mappings should appear automatically in user-facing output. Ambiguous historical records should remain available for research rather than being guessed.

### 4. Build the relevance layer

Create a separate relationship between counselor targets and alumni master's destinations.

A master's destination should not be linked to a counselor comparison merely because one alumnus attended it. The relationship must be academically defensible and may draw on:

- the counselor target's field;
- its programme-interest evidence;
- the substantive nature of the master's programme.

Do not rely on superficial title similarity alone.

At minimum, distinguish relevance such as:

- closely related continuation;
- related or adjacent destination;
- broader or interdisciplinary application.

### 5. Keep relevance and frequency separate

Store both:

- the substantive relevance classification; and
- the number of observed alumni trajectories to that destination.

Frequency may be informative but must not determine academic relevance automatically.

## First user-facing implementation: counselor app

Add a section such as:

**Where UCR graduates went next**

or

**Examples of related master's destinations pursued by UCR graduates**

Show a small, curated number of highly relevant destinations, with institution and master's programme. Make clear that these are historical examples.

Do not initially attach master's destinations to individual generated UCR alternatives. We generally do not know the exact 24-course programme that an alumnus followed, so saying that a particular generated alternative "led to" a master's would overstate the evidence.

Initially, alumni destinations should attach to the comparison or field as a whole.

## Later student-facing use

Once the counselor implementation is stable, the same layer could support student-facing questions such as:

> Where have UCR students with interests like mine gone afterwards?

This should remain an illustration of outcomes, not an admissions prediction.

## Possible later reverse-search feature

A later navigation mode could allow users to begin with a master's destination, for example:

> I am interested in a Neuroscience master's. What might studying at UCR look like?

This should be treated as a separate later feature because stronger claims about preparation would require current master's admissions requirements.

## Admissions-requirement layer remains separate

If UCR Pathways later aims to say that a generated UCR curriculum currently satisfies or helps satisfy entry requirements for a particular master's, that requires a separate evidence layer based on current official admissions requirements and course-level comparison.

Alumni outcomes alone cannot establish current eligibility.

## Internal analytical use

The alumni outcomes layer may also be used internally to examine:

- fields with substantial demonstrated postgraduate trajectories;
- recurring master's destinations;
- the breadth of UCR alumni destinations across the Dutch master's landscape;
- counselor comparisons that have strong historical analogues;
- areas where generated pathways have little or no observed alumni precedent.

These are diagnostics only. Absence of an alumni precedent must not be used as a veto on a valid UCR pathway.

## Quality-control principles

Every displayed alumni outcome should be traceable to an actual alumni record and, where a current master's identity is claimed, to a normalized programme identity.

Prefer omission to an uncertain match.

Use historical destinations to demonstrate range and plausible trajectories, not to imply guaranteed progression.

## Aggregate institutional statistics

Preliminary analysis suggests that UCR alumni have reached a broad share of the Dutch WO-master landscape. Any aggregate statistic derived from this analysis should remain provisional until the full alumni normalization and destination-matching workflow has been completed with explicit quality control.

Do not publish a coverage percentage as a product claim until that validation is complete.

## Implementation timing

Continue counselor comparison production under the current rules.

After the counselor corpus is substantially or fully produced:

1. normalize alumni postgraduate-degree records;
2. normalize master's destinations;
3. create and quality-control the counselor-target-to-destination relevance layer;
4. test the output against a deliberately diverse sample of counselor comparisons;
5. apply the enrichment across the corpus;
6. add the counselor-app presentation;
7. evaluate whether the student-facing and reverse-search uses are worth implementing.
