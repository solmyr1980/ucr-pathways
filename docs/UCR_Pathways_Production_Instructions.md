# UCR Pathways — Production Instructions

## Purpose and boundary

These instructions govern the academic production of a UCR Pathways comparison.

They implement the **UCR Pathways Master Specification** and should not redefine product-level copy, branding, website behavior or publication workflow.

Use:

- the Master Specification for durable product decisions, approved copy and visual identity;
- the enriched UCR course database for UCR course evidence and feasibility;
- current official university sources for the disciplinary reference programme;
- the current repository schema only when an approved public example record is requested.

These instructions produce academic records and Open Day outputs. They do **not** publish public examples to GitHub or LinkedIn. The workflow must not depend on a user-maintained local Git clone; repository operations belong to the downstream Web and LinkedIn Workflow and should be performed directly through the connected GitHub repository where available.

---

## 1. Inputs

For Open Day production receive:

- `participant_id`;
- `interest_statement`.

The UCR starting semester is configured for the batch rather than supplied per participant.

Preserve the participant's original wording.

Do not request or collect names or other personal information.

Do not ask follow-up questions.

Do not assume that the first-mentioned interest is more important.

### 1.1 Synthetic interest portfolios

When generating synthetic prospective-student interests for testing, demonstrations or curated public-example development, treat the set as a portfolio rather than as unrelated prompts.

Use the current enriched UCR course database as the substantive boundary. Every generated interest must be genuinely supportable by the UCR curriculum. Do not generate a central interest merely because it is plausible for a university applicant if UCR can represent it only weakly.

Write in realistic prospective-student language. Prefer ordinary wording over polished recruitment language. Avoid bombastic formulations such as “I am fascinated by…”. Fragments and compact lists are acceptable because the underlying question is simply “What are your interests?”.

Vary the form of the statements. Across a portfolio, include different combinations of:

- one, two or three interests;
- disciplines;
- questions;
- real-world problems;
- career directions;
- practical skills;
- phenomena;
- more specific and less decided formulations.

Do not manufacture combinations merely to showcase several UCR fields in one case. Multiple interests should form a psychologically plausible combination that a prospective student might actually give. One-interest statements are valuable and should remain one-interest statements; later pathway generation can broaden them through genuine subfields and neighbouring perspectives.

For the current synthetic portfolio, distribute cases deliberately across the breadth of the UCR curriculum rather than trying to reproduce current applicant demand. Achieve that balance across the portfolio, not by forcing every individual statement to span several areas. A future portfolio may deliberately use a different distribution, including overrepresenting less visible fields, but only when that distribution is explicitly chosen.

Avoid repetition. Reusing a discipline across cases is inevitable, but do not repeatedly use the same substantive question, combination or wording with only minor variation. Use original combinations where they remain realistic.

Keep the PDF constraint in view. The original interest statement appears on an information-dense A4 page. As a working rule:

- most synthetic statements should be about **6–15 words**;
- some may extend to about **20–25 words**;
- longer conversational answers should be occasional exceptions rather than the norm.

Use length and syntax as part of the realism. Mix compact lists, short questions or statements, and a smaller number of conversational responses.

Before finalizing a synthetic portfolio, check both levels:

1. **Individual plausibility:** could a real prospective student reasonably have written each statement?
2. **Portfolio coverage:** does the complete set expose the breadth of UCR's actual curriculum without obvious repetition or artificial engineering?

---

## 2. Operating sequence

Work in this order:

1. Interpret the participant's interests academically.
2. Identify the most defensible disciplinary depth endpoint.
3. Propose a disciplinary reference programme and the authoritative current source basis.
4. For a manually supervised run, stop once for human approval of the reference-programme/source basis.
5. Reconstruct the approved reference programme and choose a coherent participant-relevant path through any available choices.
6. Construct three progressively broader UCR programmes.
7. Arrange each UCR programme across six semesters.
8. Validate all three UCR programmes mechanically against the UCR feasibility rules.
9. Compare the completed four programmes substantively.
10. Give all four programmes short participant-specific titles.
11. Derive comparison blocks, horizontal alignments, deliberate gaps and explanatory notes.
12. Create the canonical pathway record.
13. Generate the requested Open Day output from the canonical record.
14. Only after substantive human review and explicit approval for public use, derive a publication example record when requested.

After the reference-programme/source checkpoint, continue without further routine intermediate interruptions unless an error or material ambiguity requires intervention.

Construct and validate programme content before designing the visual comparison.

Do not maintain separate academic versions for Open Day, website and LinkedIn use.

---

## 3. Interpret the participant's interests

Interpret the input academically without requiring the participant to understand UCR's curriculum structure.

Identify, where relevant:

- disciplines;
- substantive questions;
- phenomena or problems;
- practical interests or skills;
- meaningful connections among them.

Do not force a thematic interest into one discipline merely because that makes course selection easier.

Do not manufacture weak UCR matches where an interest is poorly represented.

For one stated interest, broaden through meaningful subfields, questions and neighbouring perspectives rather than inventing another interest.

---

## 4. Disciplinary reference programme

### 4.1 Choose the reference programme

Choose the disciplinary bachelor that provides the most useful depth endpoint for the participant's interests.

Do not automatically choose the discipline mentioned first.

For the pilot, prefer a current Dutch research-university bachelor where suitable.

### 4.2 Establish the source basis

First check whether a suitable current verified reference-programme record exists in the available project sources.

If one exists, use it as the primary factual basis and consult current official sources when it is incomplete, ambiguous, outdated or materially conflicts with current information.

If no suitable verified record exists, reconstruct the programme from current official university sources.

Prefer:

1. formal curriculum or graduation requirements;
2. official student-facing curriculum pages;
3. official route, track or specialization pages;
4. official course-catalogue entries;
5. general prospective-student programme pages.

Do not use rankings, aggregators or unofficial summaries to establish programme structure.

Prefer a primary official source that makes the selected programme and its structure easy for a reviewer to verify. Use additional official sources where necessary.

If the programme cannot be reconstructed with reasonable confidence, choose another defensible reference programme rather than guessing.

### 4.3 Human checkpoint

For a manually supervised run, present:

- the proposed reference programme;
- institution;
- proposed primary official source;
- any additional official sources materially needed.

Obtain approval for that reference-programme/source basis before full generation continues.

This is the only routine intermediate academic checkpoint.

### 4.4 Reconstruct before selecting

Distinguish:

- compulsory components;
- restricted choices;
- routes, tracks or specializations;
- genuinely free elective or profiling space;
- methods and research training;
- thesis or capstone requirements;
- relevant credit weights.

Where the programme permits choices, select one coherent valid pathway that responds reasonably to the participant's interests.

Give the reference programme the same reasonable opportunity for personalization that UCR receives.

Never:

- present optional components as compulsory;
- combine mutually exclusive options;
- violate programme rules;
- deliberately select weak options to make UCR look better;
- invent courses to fill genuinely open elective space;
- make the reference programme artificially narrow.

Represent genuinely open space explicitly, for example:

`Profiling space — 45 EC`

### 4.5 Record provenance and verification

Preserve the approved Reference programme provenance required by the Master Specification.

Record internally, where relevant:

- programme name;
- institution;
- primary official source URL;
- additional official source URLs;
- academic or curriculum year;
- date checked;
- source notes;
- selected route, track or specialization;
- validation notes about the selected pathway;
- reviewer-approval status.

---

## 5. UCR course evidence

Use the enriched UCR course database as the authoritative source for UCR course selection and feasibility.

Use, as relevant:

- `name`;
- `profile`;
- `discipline`;
- `topics`;
- `methods`;
- `description2`;
- prerequisites;
- planned semester availability.

Give outline-derived `profile` information particular weight where available.

Use course content rather than administrative cluster or unit labels.

Course level may be derived from the course code.

Do not infer fit from a title alone when richer course evidence points elsewhere.

---

## 6. Construct the three UCR programmes

### 6.1 Greatest disciplinary depth

Construct the feasible UCR programme that remains closest to the disciplinary anchor while responding meaningfully to the participant's other interests.

Depth includes foundations, progression, discipline-relevant methods, research training and advanced specialization.

Do not define depth merely by counting courses carrying one disciplinary label.

### 6.2 Balanced interests

Give the participant's stated interests substantially more balanced weight.

Do not mechanically divide courses equally among interests.

### 6.3 Thematic breadth

Start from the questions, problems and themes contained in or connecting the participant's interests rather than predetermined disciplinary quotas.

Search across the whole UCR curriculum for substantively useful perspectives.

The result should normally be the broadest UCR programme while remaining coherent and recognizably connected to the original input.

Do not include courses merely to increase apparent variety.

### 6.4 Participant-specific titles

After constructing all four programmes, give each a short title describing what it actually does.

Do not use the generic internal categories as the final programme titles.

---

## 7. UCR feasibility validation

Each UCR programme must contain:

- exactly **24 unique courses**;
- exactly **4 courses in each of six semesters**;
- at least **6 courses at 300 level**;
- **Personal & Professional Development** during Year 1.

Also require:

- every prerequisite completed in an earlier semester;
- every selected course actually available in its assigned semester;
- no duplicated courses.

Do not invent requirements concerning clusters, units, concentrations, breadth or disciplinary distributions.

Use data-analysis/code against the enriched UCR course database to validate:

- 24-course total;
- uniqueness;
- six-semester structure;
- four courses per semester;
- 300-level minimum;
- PPD placement;
- prerequisite order;
- actual semester availability.

If validation fails, repair the programme and run validation again.

Do not export a knowingly invalid UCR programme.

Repository validation is not a substitute for this academic validation.

---

## 8. Compare the completed curricula

Construct and validate all four programmes before building the comparison.

Apply the same substantive classification principles to the reference programme and UCR programmes.

Use content rather than titles alone.

Treat methods, statistics, mathematics, econometrics, laboratory work and research training as part of disciplinary depth where they genuinely serve that role.

Do not assume that one reference-programme component equals one UCR course.

Preserve actual component weights, including 5, 7.5, 10 or other EC values.

Do not distort either curriculum to force exact row-by-row or credit-by-credit correspondence.

Do not use proportional course-box scaling as a general encoding of credit weight. Show EC values or concise notes where component size matters.

### 8.1 Comparison blocks

Derive meaningful substantive blocks from the completed curricula.

Possible blocks include:

- major disciplines;
- methods and research;
- important substantive themes;
- advanced specialization;
- other distinct perspectives.

Do not create a broad theme that merely renames an existing disciplinary block.

### 8.2 Alignments and gaps

Within blocks:

- align substantively comparable components horizontally;
- preserve meaningful blank cells;
- do not fill gaps merely for visual symmetry;
- label genuinely open elective or profiling space explicitly;
- show credit weights where omitting them would materially distort the comparison.

Do not use numerical depth or breadth scores.

---

## 9. Canonical pathway record

Create one canonical structured pathway record before rendering any output.

The canonical record is the authoritative academic representation of the case.

Associate `participant_id` with the record internally for Open Day delivery and file naming. It is not part of the public academic comparison.

Preserve at minimum:

- original `interest_statement`;
- relevant cohort or starting-semester context;
- four programme identities, semantic roles and participant-specific titles;
- reference-programme components, relevant notes and credit weights;
- Reference programme provenance and internal verification metadata;
- complete 24-course set for each UCR programme;
- six-semester schedule for each UCR programme, including course name, code where available and level;
- substantive comparison blocks;
- horizontal alignments and deliberate gaps;
- explanatory or source notes needed for fair interpretation;
- academic validation status.

The record should contain content and semantic structure, not renderer-specific coordinates, CSS or page geometry.

Do not alter programme content later merely to make a renderer look more symmetrical.

Canonical records must remain non-public and must not be stored in the public GitHub repository. They are working production records rather than repository content. The production workflow should not require a user-maintained local Git clone merely to hold them.

---

## 10. Open Day output

Generate the Open Day PDF from the completed canonical record.

Follow the durable Open Day output requirements, approved copy and visual identity in the Master Specification.

Use A4 portrait and two pages.

### 10.1 Page 1

Show:

- participant ID;
- original interest statement;
- approved comparison sentence;
- approved Reference programme provenance;
- four participant-specific programme titles;
- comparison blocks, alignments, deliberate gaps and relevant notes;
- credit information where needed.

Show the four programmes in the settled order.

Do not organize page 1 by semester.

Where PDF links are supported, link the Reference programme provenance to the approved official primary source.

### 10.2 Page 2

Show the same three UCR programmes used on page 1.

For each programme show six semesters with exactly four courses per semester.

For each course show:

- course name;
- level.

Course codes may be omitted visibly unless needed for clarity, but should remain in the canonical record where available.

### 10.3 Call to action and filename

Use the UCR Program Builder destination defined in the Master Specification.

Do not imply persistence unless it has actually been implemented.

Use the participant ID as the PDF filename, for example:

`P-037.pdf`

---

## 11. Public example export

Open Day records are not automatically public.

Prepare a publication example record only after substantive human review and explicit approval for public use.

Derive it from the canonical pathway record.

Do not:

- reselect courses;
- rewrite the substantive comparison;
- rebuild alignments independently;
- expose registration identity;
- invent renderer-specific academic content.

Conform to the current repository example schema.

Preserve the approved:

- interest statement;
- four programme roles and titles;
- Reference programme provenance and primary public source;
- comparison blocks;
- alignments;
- deliberate gaps;
- relevant notes.

Use a publication-safe example ID.

Include UCR schedules only when the current repository contract or renderer needs them. The complete schedules remain mandatory in the canonical record.

The website and LinkedIn PDF render downstream from this approved publication record.

---

## 12. Final validation

Before export, confirm all relevant checks.

### Reference programme

Confirm:

- current verified record or authoritative official sources;
- approved primary source is reasonably easy to verify;
- source-basis approval occurred where the manually supervised checkpoint applies;
- compulsory, restricted and free components are distinguished correctly;
- selected pathway is valid;
- open elective space is not invented;
- methods, research, thesis and component sizes are represented fairly;
- provenance and verification metadata are recorded.

### UCR programmes

Confirm the mechanical academic validation has passed for all three programmes.

### Progression

Confirm:

- first UCR programme genuinely offers the greatest feasible disciplinary depth;
- second gives the stated interests substantially more balanced weight;
- third is genuinely broader and theme-led without becoming incoherent;
- progression comes from course content rather than arbitrary quotas.

### Comparison

Confirm:

- same substantive classification principles across all four programmes;
- alignments are justified;
- genuine gaps remain;
- open elective space is labelled;
- credit-weight differences are not visually misleading.

### Canonical record

Confirm:

- complete approved academic content is present;
- schedules match comparison content;
- blocks and alignments match completed curricula;
- validation status is recorded;
- renderer-specific content has not become a second source of programme facts.

### Open Day output

Confirm:

- page 1 and page 2 use the same three UCR programmes;
- page 2 has four courses per semester;
- participant ID and original interest statement are correct;
- approved singular/plural wording is used;
- Reference programme provenance is correct and linked where supported;
- Program Builder destination is correct.

### Public example, when requested

Confirm:

- explicit public-use approval;
- no registration identity;
- current repository schema conformity;
- settled semantic roles;
- approved Reference programme provenance;
- no substantive reinterpretation of the canonical comparison.

Only then export the requested artifact.
