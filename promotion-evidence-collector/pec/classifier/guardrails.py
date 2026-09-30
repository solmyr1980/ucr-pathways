"""Conservative constraints applied to every draft, whichever engine made it.

The guardrails can lower a level or status. They never raise one.
"""

from __future__ import annotations

from .. import signals as sg
from ..framework import DOMAINS, EVIDENCE_TYPES, L3B_COMPONENTS, LEVELS, STATUSES
from .base import Draft


def _add_missing(draft: Draft, text: str) -> None:
    if text not in draft.missing_evidence:
        draft.missing_evidence.append(text)


def sanitize(draft: Draft) -> Draft:
    """Coerce engine output to the allowed vocabularies."""
    draft.domains = [int(d) for d in draft.domains if str(d).isdigit() and int(d) in DOMAINS][:3]
    if draft.level not in LEVELS:
        draft.level = "Not assigned"
    if draft.status not in STATUSES:
        draft.status = "POTENTIAL"
    if draft.confidence not in ("High", "Medium", "Low"):
        draft.confidence = "Low"
    draft.evidence_types = [t for t in draft.evidence_types if t in EVIDENCE_TYPES]
    if isinstance(draft.missing_evidence, str):
        draft.missing_evidence = [draft.missing_evidence] if draft.missing_evidence else []
    if not draft.domains:
        draft.domains = sg.pick_domains(sg.domain_scores(draft.passage)) or [6]
        draft.confidence = "Low"
    return draft


def apply(draft: Draft) -> Draft:
    draft = sanitize(draft)
    s = sg.compute(draft.passage)
    active = draft.status in ("VERIFIED", "SUPPORTED")

    if s.intent_only and draft.level in ("L2", "L3A", "L3B", "L4") and active:
        draft.status = "POTENTIAL"
        draft.level_reason = "The passage states intended or planned work, not completed work. " + draft.level_reason
        _add_missing(draft, "A source showing that the intended work was carried out.")
        active = False

    if draft.level == "L3A":
        if s.membership_only:
            draft.level = "L2"
            draft.level_reason = "Membership does not by itself establish leadership. " + draft.level_reason
        elif not (s.action and s.scope) and active:
            draft.status = "POTENTIAL"
            _add_missing(draft, "Evidence of institutional action and its reach across UCR or a significant unit.")
            draft.level_reason = "The source does not show both institutional action and institutional reach. " + draft.level_reason

    if draft.level == "L3B":
        if not s.edu_object:
            draft.level = "Not assigned"
            draft.status = "CONTEXT" if draft.status != "REJECT" else "REJECT"
            draft.level_reason = "The passage does not concern teaching or learning, so it cannot support L3B. " + draft.level_reason
        elif not set(L3B_COMPONENTS) <= s.inquiry and active:
            draft.status = "POTENTIAL"
            for key, label in L3B_COMPONENTS.items():
                if key not in s.inquiry:
                    _add_missing(draft, label)

    if draft.level == "L4" and active and not (s.external and s.action):
        draft.status = "POTENTIAL"
        _add_missing(draft, "A source showing educational leadership or influence beyond UCR.")

    if s.award and draft.level in ("L3A", "L3B", "L4") and not (s.action and s.scope) and active:
        draft.status = "POTENTIAL"

    if s.qualification and draft.level in ("L3A", "L3B") and not s.action:
        draft.level, draft.status = "Not assigned", "CONTEXT"

    return draft
