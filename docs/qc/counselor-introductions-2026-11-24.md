# Counselor comparison introductions

24 November 2026 · 438 indexed programmes

The counselor now reads one paragraph before the table. Ordinary and caution comparisons end with the last course row and the Program Builder link. Qualified comparisons also provide a link to the full assessed and excluded scope.

[Desktop and mobile before-and-after screenshots (PDF)](evidence/counselor-introductions-2026-11-24/counselor-before-and-after.pdf)

## Editorial decision

The [September table-first renderer](https://github.com/solmyr1980/ucr-pathways/blob/8830b60a/pilot/counselor-shiny/app.R) placed the table directly after a short introduction. The [23 November renderer](https://github.com/solmyr1980/ucr-pathways/blob/2075bfc6e726487451ad47d2f58e108e1c07d335/pilot/counselor-shiny/app.R) restored that prominence but displayed reviewed narratives in as many as four topic disclosures, plus a scope disclosure on qualified pages. Different source fields often described the same distinction.

For each visible comparison, the editorial review considered the external description, comparison explanation, selected notes, alternative concepts and curriculum limitations together. It also checked any formal scope restriction. The deciding question was whether the table and common paragraph could leave a counselor with a materially wrong impression. Examples included mistaking biomedical overlap for clinical preparation, workload figures for separate course awards, or a documented third-year outline for assessed third-year teaching. Lists of differing electives, summaries of clearly labelled options and routine descriptions of a thesis generally added little.

The common wording identifies the closest feasible option and explains shared and blank rows. A case entry with a material qualification replaces the whole paragraph. Each such paragraph was checked against its case evidence. The ordinary and caution custom paragraphs range from 50 to 70 words. On qualified pages the longest paragraph is 80 words before the scope link. The two longer explanations of assessed and excluded scope remain available in their original approved wording.

## Corpus disposition

| Reader experience | Common paragraph | Case-specific paragraph | Scope disclosure |
|---|---:|---:|---:|
| Ordinary comparisons | 86 | 168 | 0 |
| Caution comparisons without a formal scope restriction | 0 | 51 | 0 |
| Qualified comparisons, including those also marked caution | 0 | 38 | 38 |
| **All 343 visible comparisons** | **86** | **257** | **38** |

The other 95 records open an external-programme page. They comprise 74 established no-matches, 15 unresolved external curricula, one registry exception and five comparisons withheld by an external-only setting. No new academic question required a decision.

## Fifteen-case pilot

The pilot used current production records with one, two and three UCR alternatives. The table records the editorial judgment for each. The full final wording is in the [presentation settings](../../data/counselor/presentation-overrides.json). The [academic records](../../data/counselor/comparisons/) retain the source narratives.

| Record | What the previous presentation did | What the counselor now reads |
|---|---|---|
| CP001 · Public Administration | The explanation, specialist note and two concepts repeated the governance comparison. | The introduction distinguishes the policy and sustainability options from Erasmus’s internship and bachelor project. |
| CP002 · Management of International Social Challenges | The global governance, climate and AI approaches appeared in the overview and again in the individual concepts. | One paragraph locates the options and names the dedicated migration and development teaching and required project. |
| CP377 · Actuarial Science | The comparison described shared financial methods. A separate note explained their different applications. | Shared quantitative methods are interpreted alongside Amsterdam’s dedicated insurance and pensions training and actuarial thesis. |
| CP150 · Business Administration | Several fields described business functions, electives and the emphases of the three schedules. | The common paragraph suffices. The headings and rows identify the business options and specialist subjects. |
| CP019 · Arts and Culture Studies | The specialist cultural-sector sequence and placement appeared in multiple fields. | The introduction distinguishes interdisciplinary arts study from specialist cultural-sector teaching and the required internship and project. |
| CP035 · Biology | The explanation and note both listed specialist subjects and described the research placement. | Plant physiology, microbiology and the compulsory placement explain why UCR coursework and optional research have different implications. |
| CP269 · Psychology & Technology | The note and comparison explanation used identical wording about the Living route. | The introduction identifies the illustrated route and its 30 EC technical specialisation. |
| CP043 · English Language and Culture | A general caution appeared before the table and linguistic detail after it. | The paragraph identifies which literary and linguistic training the UCR option addresses and where it has less depth. |
| CP097 · Medicine | The page placed clinical training in a separate warning and biomedical alternatives in the detail sections. | One paragraph connects shared biomedical content with the difference in supervised clinical practice. |
| CP041 · Economics and Business Economics | A separate scope statement reported 180 EC and other fields explained the thesis-entry uncertainty. | The paragraph states that all credits are listed and that thesis entry remains unconfirmed. The full scope stays accessible. |
| CP250 · Clinical Technology | The scope banner and academic detail described the disputed placement separately. | The introduction identifies the 176.5 EC shown, the excluded placement and the limit on clinical correspondence. |
| CP397 · Fiscal Economics | A combined caution and scope banner preceded several explanations of public finance, tax law and access. | The paragraph explains both the narrower tax-law training and the reason for showing 177 of 180 EC. |
| CP003 · Pedagogical Sciences | A no-match page showed the external curriculum and explained the limits of related UCR study. | The separate no-match presentation remains appropriate. |
| CP396 · Tax Law | A no-match page distinguished a substantive tax-law shortfall from a 3 EC access uncertainty. | The page retains its no-match judgment and the qualification that it rests on the established core. |
| CP311 · Notarial Law | The external-only setting withheld an internally qualified comparison. | The counselor still sees the external programme and verified components without a UCR comparison or scope disclosure. |

The pilot established two rules for the wider review. A complete external credit total can coexist with uncertain access. A displayed component can also fall outside the academic claim. For example, CP410 shows 156 EC but compares only the 60 EC first year. A third distinction emerged in CP373, where the left column describes UCR’s own degree and the three other columns illustrate ways to fulfil it.

## Verification

The static corpus check runs on data-only changes and requires reviewed copy for visible caution and qualified cases. The R tests check paragraph coverage, credit substitution, fallback behaviour, and exclusion of historical free text. The browser suite opens the actual Shiny application at 1440 × 1000 and 390 × 844, checks the order of page elements, and compares rendered courses, EC, links, blocks and blank cells with the academic records. It also exercises course popups, scope links, search navigation and mobile column controls. The before-and-after screenshots were captured through the search interface at the same widths.

Only the display policy adds case prose. The comparison files, decision files, presentation modes and historical caution messages are unchanged. The deployment bundle was checked locally. Public deployment requires a separate decision.
