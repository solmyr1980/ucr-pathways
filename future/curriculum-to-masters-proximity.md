# Curriculum-to-Master's Proximity via Alumni Trajectories

**Status:** Future idea

**Current decision:** Preserve this as a future methodological and implementation plan. Do not treat it as a current production requirement until explicitly activated.

## Purpose

Answer the student-facing question:

> Given this suggested UCR curriculum, what kinds of master's programmes have students with academically similar UCR curricula subsequently entered?

The method does not begin by building a complete master's-programme database. Instead, it uses observed UCR alumni trajectories as the empirical bridge between a proposed UCR curriculum and actual postgraduate destinations.

## Core architecture

The method uses three objects:

1. **Proposed UCR curriculum** — the curriculum generated for a counselor comparison or student record.
2. **Historical UCR curriculum** — the actual set of UCR courses completed by an alumnus.
3. **Observed master's destination** — the master's programme subsequently entered by that alumnus.

For alumni, the relationship between objects 2 and 3 is observed directly in the historical data.

The main methodological task is therefore to measure proximity between objects 1 and 2:

`proposed UCR curriculum -> proximity to historical UCR curriculum -> observed master's programme`

This avoids requiring complete coverage of the international master's-programme universe and uses actual UCR trajectories as evidence.

## Role of deterministic matching and the LLM

The intended production architecture is **hybrid**, not fully deterministic.

The deterministic component should not itself decide which master's programmes to recommend. Its main role is to retrieve a manageable set of historically similar alumni curricula from the full alumni corpus.

For each counselor comparison or student record:

1. the LLM constructs the proposed UCR curriculum using the enriched UCR course database under the existing production workflow;
2. deterministic code compares that curriculum with the historical alumni curricula;
3. the code returns a shortlist of the closest historical curricula, with their proximity scores and observed master's destinations;
4. the LLM inspects that shortlist and makes the final substantive judgment about which master's destinations are genuinely informative for the proposed curriculum;
5. the record is completed under the normal one-by-one production workflow.

This preserves the existing UCR Pathways principle that the LLM makes the final academic judgment for each record while using deterministic retrieval to avoid asking the model to search exhaustively through thousands of alumni trajectories.

With roughly 3,000 alumni and about 24 UCR courses per alumnus, the full corpus contains around 72,000 historical alumni-course observations. This is feasible for deterministic retrieval but should not be supplied wholesale to the LLM for every individual production task.

The size of the final shortlist remains to be tested. A working starting range might be approximately 20–50 historical curricula.

## Course-level proximity

The curriculum measure begins with a proximity score for every pair of UCR courses.

### Course corpus

Construct a comprehensive registry of every distinct UCR course that has existed.

For each course, create one canonical content profile using the best available evidence:

- course title;
- course description;
- aims;
- learning outcomes;
- substantive topics or content;
- methods or analytical approaches;
- other academically relevant material from course outlines.

Where several outlines exist, use the most recent representative outline initially. Do not create semester-specific course versions by default.

Where no outline is available, use the richest available metadata. Historical versioning can be introduced later for courses known to have changed materially.

Administrative material, assessment logistics, attendance rules and similar non-substantive content should not drive proximity.

### Primary proximity method

The current preferred approach is to use an LLM to assign a standardized academic proximity score to each unique pair of courses under a fixed rubric.

With roughly 600 distinct courses, this implies approximately 179,700 unique course pairs, which is computationally feasible as a one-off or infrequently repeated production step.

The rubric still needs to be designed and validated. It should judge substantive academic proximity rather than superficial wording overlap.

### Robustness measure

A deterministic embedding-based similarity measure should be considered as an independent robustness check.

The embedding measure and the LLM measure should initially remain separate rather than being combined automatically.

## Production workflow for course proximity

The likely development workflow is:

1. Microsoft CoWork builds the comprehensive canonical course database from the local course outlines and metadata;
2. a deliberately diverse sample of that database is brought into ChatGPT;
3. the LLM course-pair proximity rubric is designed and tested on the sample;
4. difficult and borderline cases are inspected and the rubric is revised;
5. quality-control checks are repeated until judgments are sufficiently stable;
6. ChatGPT applies the finalized rubric to all unique course pairs, in manageable batches, to produce the complete course-pair proximity matrix.

Microsoft CoWork's role in this stage is **data extraction and structuring from local files**, not substantive course-pair scoring.

The resulting course-pair proximity matrix is a reusable research asset. It should be generated once and refreshed only when the underlying course corpus or proximity method changes materially.

## Curriculum-level proximity

Once the course-pair proximity matrix exists, compare a proposed curriculum with each historical alumni curriculum.

The raw comparison between two 24-course curricula is a 24 x 24 matrix of 576 course-pair proximities.

Do **not** average all pairwise proximities. That would incorrectly ask whether every course in one curriculum resembles every course in the other.

### Current preferred family of methods: optimal transport

Treat each curriculum as a distribution of academic content.

An optimal-transport-style method assigns the academic "mass" of courses in one curriculum across academically related courses in the other curriculum while minimizing total distance, where distance is derived from the course-pair proximity measure.

The conceptual attraction is that curriculum similarity should compare two distributions of academic content rather than force a simple course-by-course correspondence.

The calculation can be implemented deterministically once the course-pair proximity matrix is available. No LLM is required at this stage.

### Important unresolved technical point

The exact transport formulation is **not yet settled**.

With two curricula containing the same number of equally weighted courses, classical balanced optimal transport can reduce to an optimal one-to-one assignment. If the intended interpretation genuinely requires academic content from one course to distribute across several courses in the other curriculum, the implementation may require a different formulation, for example a regularized, unbalanced or otherwise modified transport model.

The final formulation should therefore be tested against the conceptual objective rather than adopting classical balanced optimal transport mechanically.

## Historical curriculum data

Historical alumni curricula should not be forced into exactly 24 courses.

The alumni dataset should preserve the actual completed UCR course set for each alumnus, together with an anonymized identifier and the subsequent master's programme.

Conceptually:

`alumnus ID | completed UCR courses | master's programme`

The implementation should accommodate alumni who completed fewer or more courses than the standard 24-course curriculum.

Personal identities are not required for matching and should not be included in the production matching bundle.

Microsoft CoWork may be used to extract and structure this anonymized alumni curriculum dataset from the full local alumni records. It should not determine curriculum proximity or master's relevance.

## Technical integration with existing UCR Pathways workflows

The implementation should follow the existing separation between version-controlled code and private operational data.

### Public GitHub repository

GitHub should contain the reproducible machinery, for example:

- a script or module that calculates curriculum proximity and retrieves the nearest historical curricula;
- any helper script needed to assemble a compact production matching bundle from already-structured inputs;
- tests and validation fixtures;
- documentation of the matching method.

The raw alumni histories should **not** be stored in the public repository.

### Private matching bundle

A compact private bundle should contain only the information required during production, such as:

- the course-to-course proximity matrix generated through the validated ChatGPT scoring workflow;
- anonymized alumni curriculum records prepared from the local alumni database;
- observed master's destinations;
- any minimal metadata required by the matching algorithm.

A columnar format such as Parquet is likely appropriate because the data are structured and should compress efficiently.

The compact bundle should be assembled from these prepared inputs and stored as a private UCR Pathways Project Source or another private source accessible to the production workflow. It should be replaced only when the underlying alumni data, course corpus or proximity method changes materially.

The detailed course outlines used to build the canonical course database do not need to be loaded during each student or counselor production run once the reusable proximity matrix has been created.

### Per-record production flow

From the operator's perspective, the workflow should remain essentially unchanged.

For a new counselor comparison or student record:

1. produce the UCR curriculum using the existing enriched course database and current production rules;
2. load the private matching bundle;
3. run the deterministic retrieval code against the proposed curriculum;
4. return the closest historical alumni curricula and associated master's destinations;
5. let the LLM make the final academic selection and explanation;
6. continue the ordinary validation and publication workflow.

The retrieval step should therefore be an internal production component, not a separate manual task for the operator.

## Relationship to the alumni outcomes layer

This method complements the separate alumni-outcomes enrichment plan.

The alumni record provides evidence that a historical UCR curriculum was followed by a particular master's destination. It does **not** establish that the master's currently admits every student with a similar curriculum, nor that the proposed curriculum formally satisfies current admissions requirements.

Any future claim about current eligibility requires a separate admissions-requirement evidence layer.

## Decisions already made

- Do not begin by constructing a complete Dutch master's-programme database.
- Use actual UCR alumni trajectories as the empirical bridge to master's destinations.
- Compare proposed UCR curricula with historical UCR curricula.
- Build course-level proximity from substantive course content.
- Use one canonical course profile per course initially rather than semester-specific profiles.
- Use Microsoft CoWork to build the comprehensive canonical course database from local course outlines and metadata.
- Use an LLM-based course-pair proximity measure as the primary candidate.
- Use ChatGPT, not Microsoft CoWork, to apply the validated course-pair rubric and produce the full course-pair proximity matrix.
- Consider embedding similarity as an independent robustness measure.
- Generate and reuse a full course-pair proximity matrix rather than asking the LLM to re-evaluate course pairs during each record.
- Treat curricula as distributions of academic content.
- Use an optimal-transport-style method as the current preferred family of curriculum-level aggregation methods, while leaving the exact formulation open.
- Use deterministic curriculum matching primarily as a **retrieval mechanism**, not as the final master's recommendation.
- Let the LLM make the final academic judgment over a short list of historically similar alumni curricula.
- Keep the existing one-record-at-a-time counselor and student production workflows.
- Keep code in GitHub and private alumni matching data outside the public repository.
- Keep the curriculum-matching procedure separate from any claim about current master's admissions eligibility.

## Outstanding methodological and implementation decisions

The following issues remain open:

1. **Course-pair LLM rubric**
   - precise definition of academic proximity;
   - score scale;
   - required output;
   - treatment of topic similarity versus methodological or disciplinary similarity.

2. **Canonical course profile**
   - exact fields to include;
   - rules for combining multiple source documents;
   - treatment of sparse metadata.

3. **Curriculum transport formulation and course weights**
   - classical balanced versus modified transport;
   - equal weight per course versus ECTS weighting;
   - whether genuinely many-to-many content allocation is required;
   - possible alternative weighting for academically central or advanced courses.

4. **Unequal curriculum sizes**
   - exact normalization or penalty structure when alumni completed fewer or more than 24 courses.

5. **Exceptional course types**
   - PPD;
   - independent research;
   - internships;
   - exchange or externally completed courses;
   - other courses with weak or incomparable content descriptions.

6. **Retrieval design**
   - number of historical curricula returned to the LLM;
   - whether to use a fixed top-N list, a proximity threshold, or both;
   - how to avoid near-duplicate historical curricula overwhelming the shortlist.

7. **Validation and robustness**
   - deliberately chosen course pairs for rubric validation;
   - curriculum pairs with known substantive similarity or difference;
   - comparison of LLM and embedding proximity;
   - comparison of the chosen transport method with simpler aggregation benchmarks;
   - checks that the deterministic shortlist contains the alumni analogues an expert would expect.

8. **LLM master's-selection rule**
   - criteria for selecting master's destinations from the retrieved alumni analogues;
   - how to combine several alumni observations leading to the same master's;
   - how many master's destinations to show;
   - how to communicate proximity, historical evidence and uncertainty without implying current admissions eligibility.

The master's-presentation layer should be finalized only after the course-level proximity, curriculum-level retrieval and LLM selection stages have been validated together.
