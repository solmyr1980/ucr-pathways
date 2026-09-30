"""Local rule-based extraction engine.

The engine works passage by passage and never sends text anywhere. It is
deliberately conservative: it only proposes L3A when a passage describes
institutional action with institutional reach, and only proposes L3B when a
passage contains the components of systematic educational inquiry.
"""

from __future__ import annotations

import re

from .. import signals as sg
from ..framework import L3B_COMPONENTS
from .base import DocumentContext, Draft

MISSING_ROLE_ACTION = "Evidence of what the candidate did in the role, such as responsibilities carried out, decisions, structures or systems developed, and their reach across UCR or the unit."
MISSING_REACH = "Evidence that the work reached beyond a single course or group, for example adoption across UCR, a department, or a programme."
MISSING_CORROBORATION = "An independent source (handbook, minutes, report, policy, appointment letter, or evaluation) that corroborates the institutional action."
MISSING_GRANT_OUTCOME = "Project outputs, an evaluation method, gathered evidence, reported findings, and evidence that the findings informed practice."
MISSING_MEMBERSHIP = "Evidence of specific contributions or decisions the candidate shaped through this body."


def _condense(text: str, limit: int = 400) -> str:
    flat = re.sub(r"\s+", " ", text).strip()
    if len(flat) <= limit:
        return flat
    cut = flat[:limit]
    stop = max(cut.rfind(". "), cut.rfind("; "))
    return (cut[: stop + 1] if stop > limit * 0.5 else cut.rsplit(" ", 1)[0]) + " [...]"


def _title(text: str, entity: sg.Entity | None, generic: str, l3a: bool = False) -> str:
    if entity:
        return entity.l3a_title if l3a else entity.title
    if generic:
        return generic
    body = re.sub(r"^(\W+|\d+[.)]\s+|sheet:[^\n]*\n)", "", text.strip(), flags=re.I)
    first = re.split(r"(?<=[.;:])\s|\n", body, maxsplit=1)[0]
    first = re.sub(r"\s+", " ", first).strip(" .;:")
    return first if len(first) <= 110 else first[:107].rsplit(" ", 1)[0] + " [...]"


def _types(s: sg.Signals, *extra: str) -> list[str]:
    order = ["REFLECTIVE", "W", "E", "U", "R"]
    found = set(s.types) | set(extra)
    return [t for t in order if t in found]


def is_relevant(text: str, s: sg.Signals, entity: sg.Entity | None) -> bool:
    if len(text) < 30 and not sg.YEAR_RE.search(text):
        return False  # fragments
    if s.heading:
        return False  # section headings such as "Teaching-Related Grants"
    if entity:
        return True
    top = max(s.domain_scores.values() or [0])
    if s.qualification and re.search(r"teaching", text, re.I):
        return True
    if s.publication or s.presentation or s.peer_review or s.award or s.grant:
        return top >= 1 or s.disciplinary
    if s.action and s.scope and (s.edu_object or top >= 2):
        return True
    if len(text) < 40 and not sg.YEAR_RE.search(text):
        return False
    return s.total_domain_score >= 3 and top >= 2


PLAN_GENRES = {"application", "proposal"}


def classify_passage(text: str, page_no: int = 1, genre: str = "") -> Draft | None:
    s = sg.compute(text)
    entity = sg.match_entity(text)
    if not is_relevant(text, s, entity):
        return None
    generic = "" if entity else sg.generic_entity(text)
    entity_key = entity.key if entity else (f"generic:{sg.normalize(generic)}" if generic else "")
    hint = entity.domains if entity else ()
    domains = sg.pick_domains(s.domain_scores, hint)
    top = max(s.domain_scores.values() or [0])
    base_conf = "Low" if top <= 1 and not entity else "Medium"
    claim = _condense(text)

    def draft(**kw) -> Draft:
        values = dict(
            passage=text, page_no=page_no, title=_title(text, entity, generic), claim=claim,
            domains=domains or [6], level="Not assigned", level_reason="", evidence_types=_types(s),
            status="CONTEXT", confidence=base_conf, missing_evidence=[], entity_key=entity_key, notes="",
        )
        values.update(kw)
        return Draft(**values)

    kind = entity.kind if entity else ""

    # 0. Self-assessment against the framework and stated intentions.
    if s.self_assessment and not s.action:
        return draft(
            status="CONTEXT", confidence="High", evidence_types=_types(s),
            level_reason="A statement of the level the candidate claims. It is not evidence of that level.",
        )
    edu_inquiry = sg.educational_inquiry(s) or (kind == "project" and s.edu_object and len(s.inquiry) >= 2)
    if s.intent_only and not edu_inquiry:
        return draft(
            status="CONTEXT", confidence="High", evidence_types=_types(s),
            level_reason="The passage states intended or planned work, not completed work.",
            missing_evidence=["A source showing that the intended work was carried out."],
        )

    # 1. Teaching qualifications.
    if kind == "qualification" or (s.qualification and re.search(r"teaching qualification|\b(SU?TQ|UTQ)\b|SKO|BKO", text, re.I)):
        return draft(
            domains=[4], evidence_types=_types(s, "R"), status="CONTEXT", confidence="High",
            level_reason="The qualification supports educational expertise but does not by itself demonstrate institutional leadership or systematic educational inquiry.",
        )

    # 2. Staff representation and governance outside the framework domains.
    if kind == "governance" or (s.governance and not s.edu_object):
        return draft(
            domains=[4], status="CONTEXT", confidence="Medium",
            level_reason="Staff representation documents institutional service. It does not by itself show educational leadership under the framework.",
            notes="Educational relevance would need a source showing work on teaching, curriculum, or educational policy.",
        )

    # 3. Disciplinary scholarship, presentations and peer review. A
    # publication or presentation on an educational topic without documented
    # inquiry is also context. Supervising students whose work was published
    # is teaching and is handled below.
    supervision = bool(re.search(r"\bsupervis", text, re.I))
    if (s.peer_review and not edu_inquiry) or (
            (s.publication or s.presentation) and not edu_inquiry and not supervision):
        if s.student_coauthor:
            return draft(
                title=_title(text, entity, generic) if (entity or generic) else "Co-authored disciplinary research with former student",
                domains=[1], evidence_types=_types(s, "W"), status="CONTEXT", confidence="High",
                level_reason="The output shows research collaboration with a student and may support undergraduate research mentoring. Its subject is disciplinary scholarship, not systematic inquiry into higher education.",
                missing_evidence=["For L3B: a source documenting an educational research question, method, findings, and use in educational practice."],
            )
        if s.peer_review:
            return draft(
                domains=[6], evidence_types=_types(s, "R"), status="CONTEXT", confidence="High" if s.disciplinary else "Medium",
                level_reason="External academic service in the discipline. It is relevant context but not evidence of educational leadership or educational inquiry.",
            )
        if s.edu_object and not s.disciplinary:
            return draft(
                domains=[6], evidence_types=_types(s, "W"), status="CONTEXT", confidence="Medium",
                level_reason="A presentation or publication on an educational topic. Without a documented inquiry question, method, and findings it is context, not L3B.",
                missing_evidence=["For L3B: the educational question, method, evidence, findings, and use in practice."],
            )
        return draft(
            domains=[6], evidence_types=_types(s, "W"), status="CONTEXT", confidence="High" if s.disciplinary else "Medium",
            level_reason="Disciplinary scholarship. It is recorded as context and not as L3B because it is not systematic inquiry into teaching or learning.",
        )

    # 4. Systematic educational inquiry.
    if edu_inquiry:
        comps = s.inquiry
        doms = list(dict.fromkeys(domains + [6]))[:3]
        if set(L3B_COMPONENTS) <= comps:
            return draft(
                domains=doms, level="L3B", status="VERIFIED", evidence_types=_types(s, "W"),
                confidence="High" if s.edu_object and not s.disciplinary else "Medium",
                level_reason="The source reports an educational question, method, evidence, findings, and use of the findings in practice.",
            )
        missing = [L3B_COMPONENTS[c] for c in L3B_COMPONENTS if c not in comps]
        return draft(
            domains=doms, level="L3B", status="POTENTIAL", evidence_types=_types(s, "W"), confidence="Medium",
            level_reason="The source establishes an educational inquiry question or intervention but does not by itself show that systematic inquiry was completed.",
            missing_evidence=missing,
        )

    # 5. Grants and awards.
    if s.grant and (s.edu_grant or kind == "project") and not s.pd_grant:
        return draft(
            evidence_types=_types(s, "R"), status="SUPPORTED", confidence="Medium",
            level_reason="A competitive educational grant is recognition of a proposed project. It does not by itself show completed inquiry or institutional impact.",
            missing_evidence=[MISSING_GRANT_OUTCOME],
        )
    if s.grant and s.pd_grant:
        return draft(
            domains=[4], evidence_types=["R"], status="CONTEXT", confidence="High",
            level_reason="A professional-development grant supports the candidate's own development. It does not by itself establish a framework level.",
        )
    if s.grant and not s.edu_object:
        return draft(
            domains=[6], evidence_types=_types(s, "R"), status="CONTEXT", confidence="Medium",
            level_reason="Research funding outside education. Relevant context only.",
        )
    if s.award and not (s.action and s.scope):
        disciplinary = s.disciplinary and not s.edu_object
        return draft(
            evidence_types=_types(s, "R"), status="CONTEXT" if disciplinary else "SUPPORTED",
            confidence="Medium",
            level_reason="An award is recognition. It does not by itself demonstrate institutional impact.",
        )

    # 6. Institutional leadership. In the candidate's own first-person account
    # only completed actions count. Course development counts only with
    # explicit reach across UCR or the curriculum.
    if s.course_development and not s.broad_reach:
        return draft(
            level="L2", status="VERIFIED", confidence="Medium",
            level_reason="Course development beyond own teaching. Developing courses does not by itself establish curriculum leadership.",
            missing_evidence=["Evidence that the courses changed curriculum or practice beyond the candidate's own teaching, for example programme documents or adoption records."],
        )
    if s.action and s.scope and not s.membership_only and (s.completed_action or not s.first_person):
        return draft(
            title=_title(text, entity, generic, l3a=True), level="L3A", status="VERIFIED",
            confidence="High" if s.action_count >= 2 else "Medium",
            level_reason="The passage describes institutional action with reach across UCR or a significant unit, not only a title.",
        )
    if kind == "membership" or s.membership_only:
        return draft(
            level="L2", status="VERIFIED", confidence="Medium",
            level_reason="Membership documents participation beyond own teaching. Committee membership does not by itself establish leadership.",
            missing_evidence=[MISSING_MEMBERSHIP],
        )
    if kind == "senior_role" or s.senior_title:
        if s.action:
            return draft(
                title=_title(text, entity, generic, l3a=False), level="L3A", status="POTENTIAL", confidence="Medium",
                level_reason="The passage describes actions in a senior role, but the institutional reach of those actions is not shown.",
                missing_evidence=[MISSING_REACH],
            )
        return draft(
            level="L3A", status="POTENTIAL", confidence="High",
            level_reason="The role title establishes the appointment only. A title does not by itself establish L3A.",
            missing_evidence=[MISSING_ROLE_ACTION],
        )
    if kind == "coordination" or s.coordination:
        return draft(
            level="L2", status="VERIFIED", confidence="Medium",
            level_reason="Coordination beyond a single course. Institutional reach is not shown in this passage.",
            missing_evidence=[MISSING_REACH] if s.action else [],
        )
    if kind == "project" and s.action and domains[:1] != [1]:
        return draft(
            level="L2", status="VERIFIED", confidence="Medium",
            level_reason="Development work beyond own teaching. Institutional reach is not shown in this passage.",
            missing_evidence=[MISSING_REACH],
        )

    # 7. Contributions beyond own courses.
    colleague_work = s.domain_scores.get(4, 0) >= 3 and s.action
    curriculum_work = domains[:1] == [5] and s.action
    if colleague_work or curriculum_work:
        return draft(
            level="L2", status="VERIFIED", confidence=base_conf,
            level_reason="Contribution beyond own teaching, for example work with colleagues or on curriculum beyond one course. Institutional reach is not shown.",
        )

    # 8. Own teaching, design, tutoring and evaluations. Argument or background
    # prose without a described activity is not evidence.
    if not (s.activity or "E" in s.types or "REFLECTIVE" in s.types or entity):
        return None
    if genre in PLAN_GENRES and not entity:
        return None  # background or argument in an application or proposal
    reason = "Documents the candidate's own teaching, course design, or tutoring practice."
    if "E" in s.types:
        reason = "Evaluation of the candidate's own teaching or tutoring."
    return draft(level="L1", status="VERIFIED", level_reason=reason)


class RuleEngine:
    name = "rules"
    sends_text_externally = False

    def extract(self, doc: DocumentContext) -> list[Draft]:
        drafts: list[Draft] = []
        for page_no, page in enumerate(doc.pages, start=1):
            for passage in sg.segment(page):
                result = classify_passage(passage, page_no, doc.genre)
                if result is not None:
                    drafts.append(result)
        return drafts
