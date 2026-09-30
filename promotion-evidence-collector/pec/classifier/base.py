"""Engine interface for evidence extraction.

An engine reads one document and returns ``Draft`` records. Every draft must
carry a passage copied from the document text. The pipeline discards drafts
whose passage cannot be found in the source, applies the conservative
guardrails, merges drafts across documents and assigns final statuses.

To add or change an LLM provider, implement ``ExtractionEngine`` (or a
``JSONProvider`` for ``LLMEngine``) and register it in ``registry.py``. No
other module needs to change.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Protocol


@dataclass
class DocumentContext:
    filename: str
    genre: str
    pages: list[str]
    page_label: str = "page"


@dataclass
class Draft:
    passage: str
    page_no: int
    title: str
    claim: str
    domains: list[int]
    level: str
    level_reason: str
    evidence_types: list[str]
    status: str
    confidence: str
    missing_evidence: list[str] = field(default_factory=list)
    entity_key: str = ""
    notes: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Draft":
        known = {k: data[k] for k in cls.__dataclass_fields__ if k in data}
        return cls(**known)


class ExtractionEngine(Protocol):
    name: str
    sends_text_externally: bool

    def extract(self, doc: DocumentContext) -> list[Draft]:
        ...
