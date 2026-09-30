"""Build a fictional sample corpus from the known test cases.

The candidate is fictional ("Sam Verhoeven"). Run
``python -m pec.cli samples ./sample_docs`` to create the files.
"""

from __future__ import annotations

from pathlib import Path

CANDIDATE = "Sam Verhoeven"

CV_TEXT = """Curriculum Vitae
Dr. Sam Verhoeven
University College Roosevelt, Middelburg

Academic and administrative positions

Head Tutor, 2021-2023
- Managed academic advising, ensured teaching quality, and oversaw 17 faculty advisors.

Interim Head of Social Sciences, 2019-2020

Extended Executive Board Member, 2020-2022

Member of the Board of Studies, 2017-2020

Chair, Works Council, 2016-2018. Vice-Chair, Works Council, 2014-2016.

Member, Program Committee, 2015-2017

Coordinator, Film and Media Studies Track, 2014-present

Coordinator of the First-Year English Programme, 2012-2018

Teaching and tutoring

Academic tutor for about 25 students per year, 2011-present.

Taught courses in environmental humanities, literature, and film at all levels of the curriculum, 2011-present.

Supervised faculty and tutors as Head Tutor, 2021-2023.

Led transformation of the advising system.

Developed international exchange agreements with three partner universities, 2018-2020.

Grants and qualifications

Salvaged Semiotics, educational innovation grant (Comenius Teaching Fellow), 2022.

Professional development grant for a pedagogy summer school, 2018.

Senior Teaching Qualification (STQ), 2020.

Research

Verhoeven, S. and Jansen, A. (2021). Diane di Prima and the Beat archive. Journal of Beat Studies 9: 45-67. Co-authored with a former student.

Paper presented at the European Beat Studies Network conference, 2019: Kerouac and ecology.

Peer reviewer for the Journal of Beat Studies and ISLE.

JRF student archival research project: supervised four students in archival research on Beat Generation materials, 2019.
"""

HANDBOOK_TEXT = """UCR Tutoring and Advising Handbook
University College Roosevelt, edition 2021

The tutoring system

Every UCR student is assigned an academic tutor who advises on course choice, degree planning, and academic progress.

The Head Tutor

The Head Tutor helps oversee the tutoring system, coordinates training and professional development of tutors, participates in evaluation, appraises tutors, and reports findings to the Board of Studies.

The Head Tutor chairs the tutor meetings each semester and maintains the advising guidelines used by all tutors.
"""

MINUTES_TEXT = """Minutes of the Board of Studies
University College Roosevelt
14 March 2022

Present: Board of Studies members; Dr. S. Verhoeven (Head Tutor) for item 3.

3. Advising structure. Dr. Verhoeven presented the revised advising structure and the new tutor training programme. The revised structure was implemented across UCR from September 2022, and all tutors now use the new advising guidelines.
"""

PROPOSAL_TEXT = """Proposal: Interdisciplinary Education Programme intervention
Applicant: Dr. Sam Verhoeven

Research question: To what extent can an interdisciplinary educational intervention bridge the disciplines at UCR?

The Interdisciplinary Education Programme will pilot two joint modules taught by staff from different departments. We plan to evaluate the intervention with student surveys and focus groups.
"""

STUDY_TEXT = """Portfolio advising and student belonging at UCR: evaluation report
Sam Verhoeven, Educational Innovation Office, University College Roosevelt, 3 June 2023

Research question: to what extent does portfolio-based advising improve student belonging among first-year students?

Method: we surveyed 120 first-year students with a validated belonging questionnaire before and after the pilot (n = 120) and held three focus groups with tutors.

Findings: results showed that belonging scores increased significantly in the pilot group compared with the previous cohort.

Use: as a result, the advising handbook was revised and portfolio-based advising was adopted across UCR in 2023-2024.
"""

CERT_TEXT = """Certificate
This is to certify that Sam Verhoeven has successfully completed the Senior Teaching Qualification (STQ).
Utrecht, 12 May 2020
"""

ARTICLE_TEXT = """Diane di Prima and the Beat archive
Sam Verhoeven and Anna Jansen
Journal of Beat Studies 9 (2021): 45-67

Abstract. This article reads Diane di Prima's letters and the archive of the Beat Generation to show how poetry circulated through small presses.
Keywords: Beat Generation, di Prima, poetry, archive
"""


TEACHING_STATEMENT_TEXT = """Teaching Statement
Sam Verhoeven

I came to UCR as a lecturer in literature and film, and my approach to teaching has changed since then. I learned that students write more precisely when feedback arrives early and in conversation, so I now build draft conferences into every course.

As a tutor I realised that course choice is only part of advising. My approach now links advising conversations to the student's portfolio and to their sense of belonging at the college.
"""

ANNUAL_REPORT_TEXT = """Social Sciences Department Annual Report 2019-2020
University College Roosevelt, 30 September 2020

Curriculum. Under the Interim Head of Social Sciences, Dr. Sam Verhoeven, the department coordinated a revision of the Social Sciences curriculum across the department, introduced shared learning outcomes for all 100-level courses, and implemented a new course review procedure used by all Social Sciences staff.
"""


def _pdf(path: Path, text: str, image_only: bool = False) -> None:
    import pymupdf

    doc = pymupdf.open()
    page = doc.new_page()
    if image_only:
        page.draw_rect(pymupdf.Rect(72, 72, 400, 300), color=(0, 0, 0), fill=(0.8, 0.8, 0.8))
    else:
        page.insert_textbox(pymupdf.Rect(50, 50, 545, 800), text, fontsize=10)
    doc.save(str(path))
    doc.close()


def _docx(path: Path, text: str) -> None:
    import docx

    document = docx.Document()
    for block in text.split("\n"):
        if block.startswith("- "):
            document.add_paragraph(block[2:], style="List Bullet")
        else:
            document.add_paragraph(block)
    document.save(str(path))


def build(folder: str | Path) -> Path:
    import openpyxl
    from pptx import Presentation

    out = Path(folder)
    out.mkdir(parents=True, exist_ok=True)
    _docx(out / "Verhoeven_CV_2024.docx", CV_TEXT)
    (out / "Verhoeven_CV_2024 (copy).docx").write_bytes((out / "Verhoeven_CV_2024.docx").read_bytes())
    _pdf(out / "UCR_Tutoring_and_Advising_Handbook.pdf", HANDBOOK_TEXT)
    (out / "Tutoring Handbook final.pdf").write_bytes((out / "UCR_Tutoring_and_Advising_Handbook.pdf").read_bytes())
    _docx(out / "Tutoring_and_Advising_Handbook_2021.docx", HANDBOOK_TEXT)
    (out / "BoS_minutes_2022-03-14.txt").write_text(MINUTES_TEXT, encoding="utf-8")
    _docx(out / "Interdisciplinary_proposal.docx", PROPOSAL_TEXT)
    _pdf(out / "Portfolio_advising_evaluation_report.pdf", STUDY_TEXT)
    _pdf(out / "SUTQ_certificate.pdf", CERT_TEXT)
    (out / "di_Prima_article.txt").write_text(ARTICLE_TEXT, encoding="utf-8")
    _pdf(out / "scanned_appointment_letter.pdf", "", image_only=True)

    _docx(out / "Teaching_Statement_2024.docx", TEACHING_STATEMENT_TEXT)
    _pdf(out / "Social_Sciences_Annual_Report_2020.pdf", ANNUAL_REPORT_TEXT)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "LIT201 2023"
    ws.append(["Course", "Teacher", "Question", "Mean score"])
    ws.append(["LIT201 Environmental Literature", "S. Verhoeven", "Overall teaching quality", 4.6])
    ws.append(["LIT201 Environmental Literature", "S. Verhoeven", "Feedback on assignments was useful", 4.4])
    ws.append(["LIT201 Environmental Literature", "S. Verhoeven", "The teacher supported my learning", 4.7])
    wb.save(out / "Course_evaluation_LIT201_2023.xlsx")

    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Tutor training workshop"
    slide.placeholders[1].text = (
        "Training for new tutors, September 2022. Facilitated by Dr. Sam Verhoeven, Head Tutor. "
        "Topics: advising guidelines, student belonging, feedback conversations with tutees."
    )
    prs.save(out / "Tutor_training_workshop.pptx")
    return out
