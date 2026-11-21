# UCR curriculum video — pilot production brief and handoff

**Status:** The animated review cut (3:17) was completed on 18 November 2026. It can be reproduced with [GitHub Actions](#render-with-github-actions). See [render and verification notes](#9-review-cut-and-reproduction).
**Established:** 18 November 2026  
**Repository:** `solmyr1980/ucr-pathways`, branch `main`  
**Purpose:** Preserve the design decisions, inputs, initial narration and implementation findings from the curriculum-video discussion so the work can resume without restarting the concept design.

## 1. Purpose and intended output

Create a short, landscape video showing **how a particular prospective student's academic interests can be turned into one coherent, six-semester UCR curriculum**. The video is a public *teaser* of the process, not a replacement for the full interactive student-record experience. A viewer who wants a complete, personalized curriculum is invited to submit an interest statement.

The intended audience is **everyone watching**, not solely the student whose interests inspired the example. Make one illustrative video per interest statement or approved public example; different examples can foreground different UCR clusters.

The video should communicate an academically reasoned selection process through actual UCR course data and animated curriculum components. It must not imply that courses were selected or scheduled arbitrarily for visual effect.

**Target:** Approximately three minutes (roughly 2½–3½ minutes while testing), landscape 16:9. A shorter or longer cut is acceptable if it improves comprehension. Maintain the possibility of generating further videos programmatically and without paid services.

## 2. Settled creative decisions

These decisions were explicitly established in the conversation. Preserve them unless the user revises them.

1. **Begin with a short, reusable hook about educational choice, then introduce the butterfly.** Set up the familiar decision to choose a disciplinary degree, then make the contrast explicit with **“But what if your interests cross those boundaries?”** Use simple animated subject blocks for the hook, not the UCR curriculum image. After the hook, reveal the six-cluster butterfly and explain the open-curriculum idea before beginning the individual student's programme. See [opening direction below](#21-opening-direction-for-the-next-video).
2. **After the shared introduction, show the specific student's interests in the butterfly's white space**, preferably upper-left, in large readable type. The original wording is preferred. Avoid a separate title-only scene unless testing demonstrates a clear benefit. The precise introduction and zoom transition may be refined.
3. **Narration and selection happen together.** As the narrator explains a coherent academic grouping and why it responds to the student's interests, the corresponding source courses light up in the currently displayed cluster.
4. **The six-semester programme accumulates in parallel.** Relevant course selections become readable cards in a grid **two rows by three columns** (six semester panels, four courses each). The grid occupies the right side as the currently relevant cluster occupies the left. A card should show the **full course title** and, where helpful, its code. Course descriptions are *not* shown: the video is only a teaser, and the narrator should convey their essence.
5. **Make major cross-disciplinary transitions visible.** When the narration moves between distinct academic fields, briefly show how the new cluster connects to the previous one rather than letting courses accumulate as an uninterrupted stream. For the economics-to-politics change, return momentarily to the butterfly with BEN and GOS highlighted, then move into GOS. Keep the *same* six-semester grid visible and retain all earlier courses: the student is combining fields in one programme, not starting another. Apply this principle to other substantive cluster changes, but do not interrupt every minor shift of topic.
6. **Prefer understandable, minimal animation.** Course codes highlight in the cluster and cards travel/appear at their predetermined grid locations. It is desirable, though *optional for the pilot*, to keep newly selected courses fully prominent while older selections fade slightly but remain visible.
7. **Layout must serve readability.** The full butterfly cannot remain large alongside a readable 24-course grid. During selection, use the **relevant cluster crop/visual on the left**, not the entire butterfly squeezed into that space. Let the final completed grid use more or all screen space if needed. Avoid complex resizing unless it helps.
8. **Precompute the actual complete 24-course schedule.** The viewer sees it fill progressively, but course selections and semester positions come from a real, existing UCR Pathways programme record. No gaps or subsequent human-invented filler stage are needed. The ordering of selections is thematic for narration, **not** chronological by semester.
9. **Explain course relationships at selection time.** Groups of courses are the unit of explanation. The voice should convey their substantive content, why the subjects complement one another, and how they contribute to the student's interests. Do **not** read every card's course title. Once all 24 appear, there is **no second explanation** of the completed semester schedule.
10. **End with a visual payoff, then a short invitation.** Show the completed programme as the meaningful outcome of combining interests, then invite viewers to submit their own interests. Display the [UCR submission URL and its QR code](#33-interest-submission) together on the final screen. See the [next-iteration ending](#23-ending-direction-for-the-next-video).
11. **Public, third-person voice.** Narration should refer to “a student interested in ...”, not address the particular student as “you” throughout. The final invitation can address viewers directly.
12. **Calm, intellectually engaging tone.** Prefer specific, neutral and confident academic explanation over synthetic excitement, promotional superlatives or an advertising voice. Interest should emerge from the connections between ideas and the animation, not from artificial enthusiasm.

### 2.1 Opening direction for the next video

Use a **shared introduction** for student-interest videos, and potentially the counselor-comparison series. **Business & Entrepreneurship (BEN)** is the default example for explaining open courses, gateways and gateway-dependent courses because its conventional gateway structure is easy to demonstrate. Do **not** choose BEN merely as the academic focus of a particular student's programme; after the introduction, move to whatever clusters the approved record actually supports. There is no need to give every cluster its own introduction. For example, Media, Culture & Communication has no gateways.

**Provisional sequence and narration (not a locked final script):**

1. **Hook, about 0–18 seconds.** Show simple, clearly separated subject paths (such as economics, psychology and politics), not the UCR butterfly. Establish that choosing a degree often entails committing to a disciplinary focus, without claiming that conventional programmes have no electives. Then deliver the contrast: **“But what if your interests cross those boundaries?”** Show subject blocks beginning to combine. The follow-up thought is that students could explore before specializing or maintain several interests throughout their studies.
2. **Open-curriculum reveal, about 18–30 seconds.** Transition those abstract blocks into the full UCR curriculum butterfly. Explain that UCR's Liberal Arts and Sciences programme allows students to choose across six academic clusters. Make the cluster names readable as part of the video presentation; do not expect viewers to decipher tiny course codes on the full map.
3. **How course choice works, about 30–48 seconds.** Move to an enlarged **BEN** cluster, keep it on screen long enough to understand the structure, and visually distinguish courses without gateway requirements, gateway courses and courses that require a gateway. **Course level and gateway requirements are different:** 100-level courses are introductory; 300-level courses are advanced in academic demands and may include research, but a 300-level course does not necessarily require a gateway. **Provisional narration:** “Courses range from introductory to advanced levels. Some are open to students without a gateway, even at advanced levels. Others require particular knowledge or skills. Gateway courses provide that foundation, preparing students to take the courses that depend on them.” Briefly contrast an actual advanced course without a gateway with a gateway-dependent course, checking their classification against the current curriculum data. Where the visual uses “Locked”, explain it as **“Gateway required”**, not permanent inaccessibility. Demonstrate actual gateway-to-course relationships without implying that every advanced course is locked or that one gateway unlocks every course in the cluster.
4. **Transition to the example, about 48–58 seconds.** Introduce the approved student's original interest statement, place it legibly on the butterfly, then proceed to the existing **source cluster → highlighted courses → six-semester grid** construction and interest-specific narration.

**Visual and editorial principles:** Make the **“but”** a clear turning point, not a UCR promotional claim. Keep the opening graphic simple and animated; use the existing UCR brand assets when UCR enters. Preserve a readable, unhurried butterfly and gateway demonstration. This sequence is intended to be reusable; only the final handoff into the student or counselor example needs to change. Avoid duplicated interest statements during transitions.

**Open for the next review:** Exact voice-over wording, animation design, seconds per scene and total film length remain adjustable. These durations are planning estimates, not acceptance thresholds. Do not merely append the introduction if that makes the film unnecessarily long; review pacing across the whole video. Check specific gateway claims against the current course data and [UCR curriculum](https://ucr.nl/education/curriculum/) and [Business & Entrepreneurship](https://ucr.nl/education/courses/business-entrepreneurship/) explanations.

### 2.2 Cross-disciplinary transitions for the next video

The move from **economics (BEN) to politics (GOS)** should visibly demonstrate the open curriculum's ability to combine academic interests. After the economics selections finish, pause briefly while the semester grid remains on screen; zoom out from BEN to the full butterfly, highlight BEN and GOS to locate the two fields, then zoom into GOS and continue adding political courses to the existing grid. Aim for a concise transition (provisionally **5–7 seconds**), not an elaborate chapter break.

**Provisional narration:** “Economic questions lead us to political ones. Who sets the rules that shape markets? Who decides how resources are distributed? To explore those questions, we can bring politics into the programme.” Adapt the wording and timing to the actual narration and animations. The key is to explain the *intellectual connection*, not merely announce a change of cluster.

This is a reusable storytelling principle, not a fixed BEN-to-GOS sequence for every student. Do not require a transition for small changes within a discipline or invent academic connections unsupported by the approved record.

### 2.3 Ending direction for the next video

Replace the anticlimactic static completion with a short, restrained visual payoff and invitation (provisionally **15–20 seconds** in total):

1. **Completed-programme reveal (about 5 seconds).** The last course arrives and the six-semester grid expands to use the screen. Briefly emphasize the contributions of the different academic clusters with their existing colours; retain the real 24-course schedule. Avoid a long static hold.
2. **The payoff (about 5–7 seconds).** Connect the result back to the student's motivating interests. For the existing economics-and-politics pilot, provisional narration: “One question has taken us through economics, politics, history and sustainability. Together, they form a six-semester programme built around that student's interests.” A short on-screen summary may read: **“One question. Many disciplines. One programme.”** Adapt this to the actual record rather than imposing the same subjects or tagline on every video.
3. **The invitation (about 5–8 seconds).** Recede the curriculum to make room for **“What would you build?”** and the invitation to share interests. Use the existing UCR logo, branding and verified [submission URL and QR image](#33-interest-submission) together. Provisional narration: “That was one possibility. What would you build around your interests?”

These durations, copy and visual details are provisional. Preserve an academically restrained tone and make the combined-disciplinary programme feel like a result, without promotional exaggeration. Check that the QR code is readable and scannable from the final rendered frame. Review overall pacing rather than simply adding more runtime.

Do not introduce master's admission requirements into the initial pilot. They may be revisited for future versions.

## 3. Authoritative inputs and source inventory

### 3.1 Visual source images — uploaded on GitHub

The current authoritative video graphics are the seven **SVG files** in [`assets/video/`](../../assets/video/). Use these repository assets rather than the old PNG exports or compressed chat screenshots.

| File | Role |
| --- | --- |
| [`assets/video/curriculum.svg`](../../assets/video/curriculum.svg) | Full butterfly; shows six clusters and course codes |
| [`assets/video/BEN.svg`](../../assets/video/BEN.svg) | Business & Entrepreneurship close-up |
| [`assets/video/DIS.svg`](../../assets/video/DIS.svg) | Data Science & Intelligent Systems close-up |
| [`assets/video/ENS.svg`](../../assets/video/ENS.svg) | Environment & Sustainability close-up |
| [`assets/video/GOS.svg`](../../assets/video/GOS.svg) | Government & Society close-up |
| [`assets/video/HCB.svg`](../../assets/video/HCB.svg) | Human Health & Well-being close-up |
| [`assets/video/MCC.svg`](../../assets/video/MCC.svg) | Media, Culture & Communication close-up |

These SVGs contain identifiable course elements. The current Python renderer still assumes PNG files and hardcoded coordinates from their former dimensions: **adapt it for these SVG inputs in the next video iteration**. Use SVG course identifiers and actual geometry where practical; verify highlight alignment and readability after rendering. Do not assume the old PNG coordinates remain valid.

**UCR branding for the next video iteration:** Reuse the existing [UCR logo](../../assets/brand/ucr-primary-plum.png), [brand colours and font definitions](../../assets/css/brand.css), and available [`assets/fonts/`](../../assets/fonts/) files. Integrate these deliberately into the video's visual identity (for example, the opening, headings and closing) while keeping course content readable. Use the actual repository assets rather than recreating the logo or inventing branding. Keep project-internal `UCR Pathways` branding out of the public-facing video.

### 3.2 Real academic and schedule evidence

- **Public demonstration record:** [`data/examples/p-001.json`](../../data/examples/p-001.json). Use its interest statement, and for this pilot use the programme `ucr-depth`, labelled *Economics, Politics and Global Development*. This is an existing public example, not a private student.
- **Governing current course source:** [`data/reference/ucr_courses_enriched.xlsx`](../../data/reference/ucr_courses_enriched.xlsx); see [source description](../../data/reference/README.md). Confirm course titles and academic claims against the active database, not merely the images or old captions.
- **Existing presentation conventions:** [student Shiny pilot](../shiny/) and [counselor Shiny pilot](../counselor-shiny/). The six-semester grid and cards should resemble the comprehensible student-facing programme structure in those applications, not necessarily reproduce their technical UI verbatim.
- **Secondary, presentation-ready description reference:** [`pilot/shiny/data/courses/`](../shiny/data/courses/), including `BEN.json`, `GOS.json`, `ENS.json` and `ACC.json`. These are useful to interpret the prototype's earlier phrasing, but the enriched course workbook remains authoritative.
- **Academic governance:** [Master Specification](../../docs/UCR_Pathways_Master_Specification.md) and [Production Instructions](../../docs/UCR_Pathways_Production_Instructions.md). The video must reflect an actual validated programme rather than override its academic decisions.
- **Public use:** Follow the [Web/LinkedIn Workflow](../../docs/UCR_Pathways_Web_LinkedIn_Workflow.md) when publication or a real-student example becomes relevant. Student-specific records are private and **not automatically approved for public use**.

The public example's exact interest statement:

> Economics, politics, and why some countries become rich while others stay poor

The video shows one programme, not all UCR alternatives and not its external bachelor comparator. Do not imply that every viewer would receive this same curriculum. The programme's final six-semester course positions must come directly from the selected example and remain unchanged during storytelling.

### 3.3 Interest submission

- **On-screen URL** [https://ucr.nl/tell-us-about-your-interests/](https://ucr.nl/tell-us-about-your-interests/)
- **QR image** [`assets/video/qr-code.png`](../../assets/video/qr-code.png)

The QR code encodes the same URL. Show both together on the closing screen in the next render.

### 3.4 Source gaps and input still needed

- The existing narration voice was a very basic synthetic voice and was judged poor. A substantially more natural, restrained voice is required for an improved version. Free/offline tools are preferred, but tool selection is not yet settled.
- Recheck historical changes in titles/content before publishing, especially `GOSHIST312`: the older public example describes this as *History Research Seminar*, whereas the active reference may differ. Do not silently use an outdated academic claim.

## 4. First example: selection sequence and synchronized course groups

For `p-001 / ucr-depth`, the *existing* 24-course programme can be explained in seven groups. Add courses to their fixed semester positions as each group is discussed, without rereading all labels.

| Group and narration focus | Cluster display | Selected course codes | Number |
| --- | --- | --- | ---: |
| Economics: decisions, growth, policy, behaviour | BEN | `BENECON111`, `BENECON211`, `BENECON212`, `BENECON311`, `BENECON314` | 5 |
| Finance, entrepreneurship, business, AI | BEN | `BENGATE101`, `BENBUSI312`, `BENBUSI112`, `BENBUSI211`, `BENENTR312` | 5 |
| Statistics and econometric evidence | BEN | `BENGATE102`, `BENECON312` | 2 |
| Political philosophy, comparative and international politics, law and conflict | GOS | `GOSPOLI111`, `GOSPOLI212`, `GOSPOLI112`, `GOSPOLI311`, `GOSGATE102`, `GOSPOLI313` | 6 |
| Historical perspective and qualitative research | GOS | `GOSSOCI212`, `GOSHIST111`, `GOSHIST312`, `GOSHIST211` | 4 |
| Sustainability governance | ENS | `ENSDELT312` | 1 |
| Personal and professional development | PPD / ACC component | `ACCPPDE101` | 1 |
| **Total** | | | **24** |

This is **one proposed narrative grouping**, not a requirement to create the same seven groups for every student. Adapt each future video's group structure to its interests and actual curriculum. Make sure a course is highlighted in its real cluster; PPD may need a simple dedicated treatment rather than an invented cluster image.

## 5. Narration draft v1 — content baseline, not final audio script

The following version was positively received as worth testing in a video. It sets the intended academic tone and content; it was **not** approved as a final publication script. Revise with the visuals and verified current descriptions.

> Imagine a student interested in economics and politics, particularly one question: why do some countries become prosperous while others remain poor?
>
> At University College Roosevelt, we can start with the entire curriculum. It contains courses across six clusters, covering a wide range of disciplines. Let's see how we might construct a programme around this student's interests.
>
> We begin with economics.
>
> Some courses examine how individuals, businesses and markets make decisions. Others explore economic growth, inflation, international trade and the role of government. Public economics investigates how taxation and spending affect economic outcomes, while behavioural economics considers how people actually make decisions, rather than how economic models assume they do.
>
> But understanding prosperity also requires looking at businesses and financial institutions.
>
> Banks help channel savings into investment. Businesses make decisions about finance, production and international markets. Entrepreneurship introduces the process of developing new ventures, while the study of artificial intelligence raises questions about productivity, employment and inequality.
>
> These questions also require evidence. Research methods, statistics and econometrics provide tools for examining economic relationships and investigating whether one factor actually causes another.
>
> Now let's turn to politics.
>
> Political philosophy asks fundamental questions about justice, rights and authority. Comparative politics examines how political systems and institutions differ. International relations and European politics explore cooperation, competition and decision-making across borders.
>
> Law adds another perspective on how societies establish and enforce rules. The study of peace and conflict helps explain how political tensions develop and how societies attempt to resolve them.
>
> History contributes an essential dimension.
>
> Industrialisation, empires, wars and political transformations have shaped the economic and political institutions we see today. Studying these developments helps us understand why countries have followed different trajectories. Historical and qualitative research also offer ways to investigate questions that economic statistics alone cannot answer.
>
> We can extend the programme further by examining the governance of sustainability, where economic interests, political institutions and environmental concerns meet.
>
> And personal and professional development supports the academic skills and reflection that accompany the student's studies.
>
> We now have 24 courses, arranged across six semesters. The result is one possible programme that connects economics, politics, history and research around the student's original question.
>
> But this is just one example.
>
> What would a curriculum built around your interests look like?
>
> Tell us what you would like to explore. Scan the QR code or follow the link to see what you could study at UCR.

Editing principle: shorten or combine lines when needed to synchronize naturally with the animation. The narrator should substitute for long course descriptions only in the sense of **conveying their core ideas**, not by reading descriptions or codes aloud. Avoid promotional words and questionable generalizations. Update factual details from the current course database.

## 6. Prototypes and lessons learned — 18 November 2026

### What was produced

- An initial approximately 30-second **animated** economics-to-politics prototype demonstrated highlighting selected courses, moving cards into the grid, switching cluster panels and progressively accumulating earlier selections. The user confirmed that **the movement and basic animation matched the intended concept**.
- Two 1920×1080 layout mock-ups tested an intermediate split frame and a completed six-semester grid.
- A subsequent approximately 2 minute 38 second **static-scene** full-length video with synthetic narration was produced in ChatGPT as `ucr_pathways_video_static_v1.mp4`. Its static frames demonstrate the expanded sequence but are **not evidence that the full production-quality motion has been implemented**.
- An attempted animated full-length render was part of experimentation; do not treat it as a verified finished deliverable unless independently checked. A named file in a working directory is not proof of completion.

**Location/portability warning:** These prototype MP4 and mock-up outputs were generated in a ChatGPT session under a local `/mnt/data/pathways_video_test/` directory, **not committed to GitHub**. The session's sandbox URLs and temporary paths are not durable cross-session source assets. To use the actual MP4 as a reference in a later Work session, attach the file there or explicitly store an approved copy in persistent project storage. Do not claim the video itself is already in this repository.

### Verified conclusions and limitations

- The concept works technically using free programmatic graphics and video tools (for example, Python/Pillow/MoviePy/FFmpeg); generative cinematic video is unnecessary.
- A full-screen two-row, three-column, 24-course grid can display **codes and short-to-medium titles**. Readability is the critical constraint, especially with the left cluster panel still on screen.
- At a smaller screen size, a full butterfly displayed beside the grid is incomprehensible. Use an enlarged *active cluster* as the source during selection. The full butterfly is useful at the opening.
- The current synthetic voice sounds unnatural and is unacceptable as a final production choice. Script pacing and exact card appearance need better synchronization.
- The static-scene cut did not preserve the tested movement satisfactorily; **do not substitute static slides for the agreed animation** merely because they are easier to render.
- The static cut used a dummy QR-like image. It is **not a usable QR code** and should be replaced or removed.
- Initial mock-ups showed cramped/faded text in some course cards and rough layout. Revisit card typography, spacing, visual prominence and margins instead of assuming the prototype looks polished.
- Current visual tests do not amount to academic verification of all narrated course claims. Cross-check the enriched workbook and ensure every one of the 24 cards matches the approved record.

## 7. Next production assignment — executable from one sentence

**Invocation:** “Produce the next improved curriculum video following `pilot/curriculum-video/README.md` in `solmyr1980/ucr-pathways`.”

**Objective:** Produce one improved, genuinely animated full-length reference video from the existing public `p-001 / ucr-depth` record. **This README is the complete assignment:** do not require a second prompt specifying the storyboard changes, code modifications, rendering workflow, validation or deliverable. The existing scripts and GitHub Actions workflow reproduce the *old* pilot; implement the agreed next-iteration changes below as part of producing the new video, not as a separate prerequisite task.

**Execution and delivery:** Work directly on `main`. Modify and commit the existing Python renderer, narration/storyboard and GitHub Actions workflow only as needed, retaining working components and the validated academic data. Use the seven SVG assets listed in §3.1 and adapt the existing PNG-based renderer and verification as necessary. Do not request new graphic uploads or assume the old PNG coordinates apply. Run the revised GitHub Actions workflow, resolve technical failures, and verify the rendered MP4 against the acceptance criteria below. Return the **successful run URL** and instructions to download its **14-day artifact** for human review. Do **not** commit generated MP4s, upload to YouTube, publish anything or request routine intermediate approval. If an external blocker prevents completion, preserve tested progress and precise continuation instructions in GitHub and report the blocker.

1. Read this handoff and only the UCR Pathways authoritative documents needed for the particular implementation. Retrieve the current main-branch source record, enriched course reference and uploaded PNGs; check their actual content.
2. Implement the [reusable hook, butterfly overview and BEN gateway explanation](#21-opening-direction-for-the-next-video) before introducing the particular student. Then preserve the **source cluster → highlighted courses → six-semester grid** animation. Include a clearly visible, narrated [BEN-to-GOS transition](#22-cross-disciplinary-transitions-for-the-next-video) that briefly revisits the butterfly to show the two fields, while the same grid persists and continues filling.
3. Calculate precise tile/highlight positions from source image dimensions or underlying course elements. Do not rely blindly on coordinates from a previous screenshot; check each highlight against the corresponding code and the rendered frame.
4. Precompute all 24 destination cards and their fixed positions directly from `p-001`. Animate course selection by narrative group, with the source tile highlighted and the readable titled card appearing at its destination. Newly selected courses may be emphasized while earlier cards recede slightly.
5. Improve typography, card spacing, resizing, transitional motion and the full-frame final state. Retain readable codes plus titles, **no descriptions**. Avoid squeezing the whole butterfly and finished grid into one frame.
6. Refine the academically grounded narration and generate a natural, calm voice. Synchronize narration and visuals at the group level. Prefer free tools; if a paid/external service is truly necessary, describe the trade-off before using it.
7. Integrate the existing [UCR branding assets](#31-visual-source-images--uploaded-on-github) into the next video, using the official logo, colours and fonts where appropriate without cluttering the animation. Implement the [completed-programme payoff and invitation](#23-ending-direction-for-the-next-video), displaying the [submission URL and QR image](#33-interest-submission) together on the closing screen. Scan the QR code from the rendered frame to verify that it opens the displayed URL.
8. Render one reviewable 16:9 MP4. Inspect representative frames (opening, early selection, BEN→GOS transition, later full grid, closing), listen to the voice and check complete playback. Report issues candidly.
9. Keep the pilot separate from production publication. Store validated reusable **source code and instructions** in this sub-project when implementation is authorized. Do not overwrite the authoritative academic data or deploy/publish the example without separate authorization.

### Acceptance test for the next iteration

- The opening uses a clear **“but”** contrast before showing UCR; the six clusters and BEN gateway example are understandable and unhurried.
- The gateway explanation distinguishes **academic course level** from **gateway requirements**, including an advanced course that does not require a gateway.
- The move from the shared introduction to the particular student's interests is coherent, with no duplicate or overlapping text.
- The course titles and semester labels are legible at normal desktop video size.
- Selection highlighting identifies the correct code in the displayed cluster.
- Every one of the **24 unique courses** appears once in its **approved** semester.
- The grid persists across cluster changes and never resets.
- Narration explains why groups belong together *while* the group is being selected; there is no repeated explanation after completion.
- Movement is clear, smooth, and synchronized with the voice. The BEN-to-GOS transition visibly connects two disciplines without resetting or hiding the accumulating semester grid.
- Audio is intelligible and appropriately natural, and on-screen text is free from clipping or overlaps.
- The video can be generated without a required paid account; limitations are recorded.
- UCR's existing logo, colours and fonts are used appropriately and legibly; the branding supports rather than competes with the curriculum animation.
- The ending gives the completed curriculum a brief visual payoff, connects it to the student's interests, and avoids a prolonged static hold.
- The closing screen shows the submission URL and a scannable QR code that leads to the same page.
- No private student data appear, and no project-internal `UCR Pathways` product branding is presented to students.

## 8. Open decisions — do not silently treat these as settled

- The final synthesized voice (and whether it is achievable entirely with free tooling).
- Exact overall runtime and timing between narration groups.
- How much the full butterfly zoom and active-cluster panel should change size during the transition; judge by readability and simplicity.
- Whether earlier cards fade slightly in each scene; desirable but not essential for pilot feasibility.
- Whether images/visuals from the live Shiny renderer can be transformed into individually addressable vector elements instead of using PNG crops. This is an optimization, not a prerequisite.

**Working rule:** Treat this file as the specific, reusable **pilot handoff**, not as a new UCR Pathways production policy. Update it with demonstrated results and explicit user decisions as the video pilot progresses.
## 9. Review cut and reproduction

The original review cut runs **3:17** at 1920 × 1080 and 24 fps. It opens on Business & Entrepreneurship, reveals the full butterfly, then follows the narration through the seven groups. Each selected card moves from its highlighted tile to its semester. The academic core selection uses its actual tile in the full butterfly. The completed grid remains on screen for about twelve seconds. The final invitation asks viewers to submit their interests. The [submission URL and QR code](#33-interest-submission) are specified for the next render.

### Academic checks

The renderer reads the original interest, programme label and all semester and within-semester positions from the public example. It joins the 24 codes to the current official workbook names and checks for complete, unique storyboard coverage. GOSHIST312 now displays as *Researching the “American Century”*. Its narration describes historical source work using the official description.

The public example passed the structural example validator. The separate course feasibility validator found two discrepancies for the selected programme at input commit `a489fcd7960373ba1d627d7846e35faef075ceae`. BENBUSI211 is in spring 2028 in the example and BENECON314 in spring 2029. Neither term has a planned offering for that course in the current workbook. The pilot preserves the canonical positions and labels the final programme illustrative. Reconcile the two placements before presenting the film as a currently feasible schedule.

### Render with GitHub Actions

1. In the repository’s [Actions tab](https://github.com/solmyr1980/ucr-pathways/actions/workflows/render-curriculum-video.yml), select **Render curriculum video pilot**.
2. Select **Run workflow**, choose the **main** branch and select **Run workflow** again.
3. Open the completed run and look under **Artifacts**. Download **UCR-curriculum-pilot** in your browser (not through GitHub Desktop) and extract `UCR-curriculum-pilot.mp4` from the ZIP. GitHub requires sign-in. The artifact expires automatically after **14 days**.

The workflow uses the public `p-001 / ucr-depth` example and the same storyboard, Piper Alba voice and renderer as the archived review cut. It checks playback, narration cues, scene and motion frames, and all 24 course cards against their positions in the public example. The invitation matches the archived cut. The QR code and URL remain specified for a later revision.

The [initial GitHub Actions run](https://github.com/solmyr1980/ucr-pathways/actions/runs/44886275213) passed all checks on 21 November 2026. It rendered 196.500 seconds at 1920 × 1080 and 24 fps, with H.264 video and mono AAC narration. The archived cut runs 197.208 seconds. Fresh Piper synthesis can shift cue timing slightly.

### Review and YouTube publication

1. Download the MP4 from the GitHub Actions artifact and review it locally. If changes are needed, revise the storyboard or renderer and trigger another run.
2. Once approved, upload the downloaded MP4 **manually** through YouTube Studio and publish or schedule it there. There is no YouTube API integration or automatic upload.
3. Let the GitHub Actions artifact expire after **14 days**; no manual GitHub cleanup or permanent copy of the generated MP4 is required.

Keep source code, storyboard, academic inputs and reusable images in Git. Keep rendered MP4s outside the repository, including local review copies. Use Actions artifacts for temporary downloads. Deleting a committed video from the current branch leaves its bytes in Git history.

### Reproduce the film

Use a Linux checkout with FFmpeg (libx264 and AAC), Python 3.12, Open Sans and DejaVu Serif in the Debian system font locations. Run from the repository root. The model and package downloads require internet access once. Synthesis and rendering run locally without an account or service fee.

```bash
python -m venv /tmp/ucr-video-env
. /tmp/ucr-video-env/bin/activate
pip install piper-tts==1.8.0 openpyxl==3.1.5 Pillow==13.0.0
out=/tmp/ucr-curriculum-video
mkdir -p "$out"
model_url=https://huggingface.co/rhasspy/piper-voices/resolve/0ca208afc2a2ee102b1e961e72e0a7e4907be3d0/en/en_GB/alba/medium/en_GB-alba-medium.onnx
curl -fL "$model_url" -o "$out/alba.onnx"
curl -fL "$model_url.json" -o "$out/alba.onnx.json"

python pilot/curriculum-video/narrate.py "$out/alba.onnx" "$out"
python pilot/curriculum-video/render.py "$out"
python pilot/curriculum-video/verify.py "$out"
```

For an additional check against a local copy of the original review cut, pass `--reference /path/to/UCR-curriculum-pilot.mp4` to `verify.py`.

[Storyboard and narration](storyboard.json) associate each short passage with its course codes. [Narration synthesis](narrate.py) measures the audio for each passage and writes the voice track and timing file. [Animation and encoding](render.py) use those timestamps and native-resolution tile coordinates. To revise the layout alone, reuse the voice and timing files. To edit the script, regenerate both. Fresh neural synthesis can vary slightly in timing.

Voice credit: Alba (en_GB, medium), Piper voice collection. The voice model card credits the Alba dataset under CC BY 4.0 and describes the fine-tuning lineage. [Voice model card](https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_GB/alba/medium/MODEL_CARD)

### Review checks

- Checked all 24 tile rectangles against the source PNGs, including the tall gateways and the academic core tile.
- Inspected the opening, card selections, cluster change, final grid and invitation in rendered frames. The grid persists as the source changes.
- Decoded the entire MP4 without errors. Video and audio run 197.208 and 197.200 seconds respectively. Integrated loudness was −17.2 LUFS and true peak −1.3 dBFS.
- Checked the spoken sequence with offline speech recognition. Naturalness and pacing still need a listener’s judgment.
- Review file SHA-256: `95b45cc1132fc6ea6e778fbc080441af849dc738e0faa78a340c843f45ab43ad`. This checksum identifies the original review cut.
