# Curriculum-to-Master's Proximity via Alumni Trajectories

**Status:** Future idea

**Current decision:** Preserve this as a future methodological plan. Do not treat it as a current production requirement until explicitly activated.

## Purpose

Answer the student-facing question:

> Given this suggested UCR curriculum, what kinds of master's programmes have students with academically similar UCR curricula subsequently entered?

The proposed method does not begin by building a complete master's-programme database. Instead, it uses observed UCR alumni trajectories as the empirical bridge between a proposed UCR curriculum and actual postgraduate destinations.

## Core architecture

The method uses three objects:

1. **Proposed UCR curriculum** — the 24-course curriculum generated in a counselor comparison.
2. **Historical UCR curriculum** — the actual set of UCR courses completed by an alumnus.
3. **Observed master's destination** — the master's programme subsequently entered by that alumnus.

For alumni, the relationship between objects 2 and 3 is observed directly in the historical data.

The main methodological task is therefore to measure proximity between objects 1 and 2:

`proposed UCR curriculum -> proximity to historical UCR curriculum -> observed master's programme`

This avoids requiring complete coverage of the international master's-programme universe and uses actual UCR trajectories as evidence.

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

With roughly 600 distinct courses, this implies approximately 180,000 unique course pairs, which is computationally feasible.

The rubric still needs to be designed and validated. It should judge substantive academic proximity rather than superficial wording overlap.

### Robustness measure

A deterministic embedding-based similarity measure should be considered as an independent robustness check.

The embedding measure and the LLM measure should initially remain separate rather than being combined automatically.

## Production workflow for course proximity

The likely development workflow is:

1. build a deliberately diverse sample of course profiles;
2. test the LLM rubric on that sample;
3. inspect difficult and borderline cases;
4. revise the rubric;
5. repeat quality-control checks until judgments are sufficiently stable;
6. apply the finalized method to the full local course corpus.

Because the full course database is large and stored locally, methodological development can use a representative sample in ChatGPT. Full production may then be executed against the local files using Microsoft CoWork or another suitable local-access workflow, subject to confirming that the required files are accessible in that environment.

## Curriculum-level proximity

Once the course-pair proximity matrix exists, compare a proposed curriculum with each historical alumni curriculum.

The raw comparison between two 24-course curricula is a 24 x 24 matrix of 576 course-pair proximities.

Do **not** average all pairwise proximities. That would incorrectly ask whether every course in one curriculum resembles every course in the other.

### Current preferred aggregation: optimal transport

Treat each curriculum as a distribution of academic content.

Optimal transport assigns the academic "mass" of courses in one curriculum across academically related courses in the other curriculum while minimizing total distance, where distance is derived from the course-pair proximity measure.

This allows one course to relate partly to several courses in the other curriculum. It therefore reflects similarity between the overall distributions of academic content rather than forcing one-to-one course correspondences.

The optimal-transport calculation can be implemented deterministically once the course-pair proximity matrix is available. No LLM is required at this stage.

This is the current preferred curriculum-level proximity measure, subject to later robustness checks against plausible alternatives.

## Historical curriculum data

Historical alumni curricula should not be forced into exactly 24 courses.

The alumni dataset should preserve the actual completed UCR course set for each alumnus, together with an anonymized identifier and the subsequent master's programme.

Conceptually:

`alumnus ID | completed UCR courses | master's programme`

The implementation should accommodate alumni who completed fewer or more courses than the standard 24-course curriculum.

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
- Use an LLM-based course-pair proximity measure as the primary candidate.
- Consider embedding similarity as an independent robustness measure.
- Use the full course-pair matrix when comparing curricula.
- Treat curricula as distributions of academic content.
- Use optimal transport as the current preferred curriculum-level aggregation method.
- Keep the curriculum-matching procedure separate from any claim about current master's admissions eligibility.

## Outstanding methodological decisions

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

3. **Course weights in optimal transport**
   - equal weight per course;
   - ECTS weighting;
   - possible alternative weighting for academically central or advanced courses.

4. **Unequal curriculum sizes**
   - exact normalization or penalty structure when alumni completed fewer or more than 24 courses.

5. **Exceptional course types**
   - PPD;
   - independent research;
   - internships;
   - exchange or externally completed courses;
   - other courses with weak or incomparable content descriptions.

6. **Validation and robustness**
   - deliberately chosen course pairs for rubric validation;
   - curriculum pairs with known substantive similarity or difference;
   - comparison of LLM and embedding proximity;
   - comparison of optimal transport with at least one simpler aggregation benchmark.

7. **Master's-level presentation**
   - threshold for considering an alumni curriculum sufficiently similar;
   - how to combine several alumni observations leading to the same master's;
   - how many master's destinations to show;
   - how to communicate proximity and uncertainty.

The master's-presentation layer should be designed only after the course-level and curriculum-level proximity measures have been validated.
