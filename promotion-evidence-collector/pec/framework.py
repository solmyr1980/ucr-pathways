"""UCR Teaching Career Framework constants used across the application.

Every rule in this module is a plain data structure so that it can be checked
against the current UCR framework text and edited without touching the
pipeline, the classifiers or the interface.
"""

from __future__ import annotations

DOMAINS: dict[int, str] = {
    1: "Teaching and supporting student learning",
    2: "Educational design, assessment, and feedback",
    3: "Tutoring and advising",
    4: "Teacher development and educational community",
    5: "Curriculum, program, and educational development",
    6: "Educational knowledge, evidence use, and inquiry",
}

SHORT_DOMAINS: dict[int, str] = {
    1: "Teaching",
    2: "Design and assessment",
    3: "Tutoring and advising",
    4: "Teacher development",
    5: "Curriculum and program",
    6: "Educational inquiry",
}

LEVELS = ["L1", "L2", "L3A", "L3B", "L4", "Not assigned"]
LEVEL_RANK = {"Not assigned": 0, "L1": 1, "L2": 2, "L3A": 3, "L3B": 3, "L4": 4}

LEVEL_DESCRIPTIONS = {
    "L1": "Competent practice in own teaching, tutoring or course work.",
    "L2": "Contribution beyond own courses, for example coordination of a course, track or programme component.",
    "L3A": "Institutional leader: shaped practice, structures, systems, decisions or educational arrangements across UCR or a significant institutional unit.",
    "L3B": "Scholarly teacher: systematic educational inquiry with a defined question, method, evidence, analysis, reported findings and use in practice.",
    "L4": "Educational leadership or scholarship beyond the institution.",
    "Not assigned": "No level is inferred from this item.",
}

EVIDENCE_TYPES = {
    "REFLECTIVE": "Reflective account explaining contribution, development, decisions, or learning.",
    "W": "Educational work or output.",
    "E": "Evaluation or review.",
    "U": "Use or influence.",
    "R": "External recognition.",
}

STATUSES = ["VERIFIED", "SUPPORTED", "POTENTIAL", "CONTEXT", "REJECT"]
STATUS_RANK = {"VERIFIED": 4, "SUPPORTED": 3, "POTENTIAL": 2, "CONTEXT": 1, "REJECT": 0}

STATUS_DESCRIPTIONS = {
    "VERIFIED": "The uploaded source directly supports both the factual claim and its classification.",
    "SUPPORTED": "The source supports the activity, but another source would strengthen the level, impact or implementation claim.",
    "POTENTIAL": "The activity might support the criterion, but necessary evidence is missing.",
    "CONTEXT": "Relevant to the academic career but does not itself establish the promotion criterion.",
    "REJECT": "Should not be used as promotion evidence.",
}

CONFIDENCES = ["High", "Medium", "Low"]

L3A_DOMAIN_RULES = {
    1: "Development or implementation of coordinated approaches that shaped teaching and student learning across UCR.",
    2: "Development or implementation of UCR-wide principles, systems, policies, templates, guidance, or coordinated approaches to design, assessment, or feedback.",
    3: "Development, coordination, or implementation of shared advising or tutoring approaches across UCR.",
    4: "Development or coordination of institutional systems for mentoring, peer learning, teacher development, professional learning, or collective reflection.",
    5: "Coordination of curriculum change beyond individual courses, work across clusters or programs, institutional curriculum planning, implementation, consensus-building, or shaping program priorities.",
    6: "Use of educational literature, evaluation evidence, or institutional data to guide decisions or change across UCR.",
}

L3B_DOMAIN_RULES = {
    1: "Systematic inquiry into teaching approaches or student learning, followed by reported findings used to improve practice.",
    2: "Systematic inquiry into course design, assessment, feedback, or related educational processes, followed by reported findings.",
    3: "Systematic inquiry into advising, tutoring, portfolio use, belonging, student development, or related areas, followed by reported findings.",
    4: "Systematic inquiry into mentoring, peer learning, teacher development, collegial culture, professional learning, or educational community.",
    5: "Systematic inquiry into curriculum design, student pathways, program structure, progression, or related educational structures.",
    6: "Higher education research whose primary purpose is to advance educational knowledge.",
}

L3B_COMPONENTS = {
    "question": "A defined educational question or problem",
    "method": "Systematic investigation (method)",
    "evidence": "Evidence or data gathered",
    "findings": "Analysis and reported findings",
    "use": "Use of findings to inform educational practice",
}

TARGET_POSITION = "UHD2"
PROMOTION_ROUTE = "UD1 to UHD2"
TARGET_FRAMEWORK_LEVEL = "L3"
L3_DOMAINS_REQUIRED = 2

# Promotion requirement rules for UHD2. These are the application's working
# reading of the procedure and are shown to the user verbatim in the interface.
# Confirm them against the current UCR procedure text before relying on them.
REQUIREMENT_RULES = {
    "L1": {
        "label": "L1 requirements",
        "rule": "At least one VERIFIED item at L1 or above in Domain 1 (teaching) and in Domain 2 (design, assessment, and feedback).",
        "domains": [1, 2],
        "min_level": "L1",
        "min_domains": 2,
    },
    "L2": {
        "label": "L2 requirements",
        "rule": "VERIFIED items at L2 or above in at least two domains.",
        "domains": [1, 2, 3, 4, 5, 6],
        "min_level": "L2",
        "min_domains": 2,
    },
    "L3": {
        "label": "At least two different domains at L3A or L3B",
        "rule": "VERIFIED L3A or L3B items in at least two different domains.",
        "domains": [1, 2, 3, 4, 5, 6],
        "min_level": "L3A",
        "min_domains": 2,
    },
}

REQUIREMENT_OUTCOMES = {
    "met": "Criterion appears evidenced",
    "partial": "Criterion partly evidenced",
    "none": "Insufficient evidence uploaded",
}

REVIEW_REASONS = {
    "low_confidence": "Low-confidence classification",
    "l3a_reach_unclear": "Possible L3A but institutional reach unclear",
    "l3b_incomplete": "Possible L3B but inquiry evidence incomplete",
    "conflicting_dates": "Conflicting dates",
    "possible_duplicate": "Possible duplicate",
    "unclear_authorship": "Unclear authorship",
    "uncorroborated_claim": "Claim found in CV but no corroborating source",
    "unreadable": "Document cannot be read",
    "domain_unclear": "Domain unclear",
}


def domain_label(number: int, short: bool = False) -> str:
    return f"{number}. {(SHORT_DOMAINS if short else DOMAINS)[number]}"


def level_at_least(level: str, minimum: str) -> bool:
    return LEVEL_RANK.get(level, 0) >= LEVEL_RANK.get(minimum, 0)
