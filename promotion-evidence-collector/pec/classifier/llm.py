"""Optional LLM extraction engine.

``LLMEngine`` is provider-neutral. It needs only a ``JSONProvider`` that takes
a system prompt, a user message and a JSON schema and returns parsed JSON.
Add a provider by implementing ``complete_json`` and registering it in
``registry.py``.

Using an LLM engine sends extracted document text to the provider. Original
files never leave the machine, but their text does. The interface states this
before the engine can be selected.
"""

from __future__ import annotations

import json
import os
from typing import Protocol

from .. import framework as fw
from .base import DocumentContext, Draft

CHUNK_CHARS = 40_000

ITEM_SCHEMA = {
    "type": "object",
    "properties": {
        "quote": {"type": "string"},
        "page": {"type": "integer"},
        "title": {"type": "string"},
        "claim": {"type": "string"},
        "domains": {"type": "array", "items": {"type": "integer"}},
        "level": {"type": "string", "enum": fw.LEVELS},
        "level_reason": {"type": "string"},
        "evidence_types": {"type": "array", "items": {"type": "string", "enum": list(fw.EVIDENCE_TYPES)}},
        "status": {"type": "string", "enum": fw.STATUSES},
        "confidence": {"type": "string", "enum": fw.CONFIDENCES},
        "missing_evidence": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["quote", "page", "title", "claim", "domains", "level", "level_reason",
                 "evidence_types", "status", "confidence", "missing_evidence"],
    "additionalProperties": False,
}

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {"items": {"type": "array", "items": ITEM_SCHEMA}},
    "required": ["items"],
    "additionalProperties": False,
}


def system_prompt() -> str:
    domains = "\n".join(f"{n}. {name}" for n, name in fw.DOMAINS.items())
    l3a = "\n".join(f"Domain {n}: {rule}" for n, rule in fw.L3A_DOMAIN_RULES.items())
    l3b = "\n".join(f"Domain {n}: {rule}" for n, rule in fw.L3B_DOMAIN_RULES.items())
    types = "\n".join(f"{k}: {v}" for k, v in fw.EVIDENCE_TYPES.items())
    statuses = "\n".join(f"{k}: {v}" for k, v in fw.STATUS_DESCRIPTIONS.items())
    return f"""You extract promotion evidence for an academic under the University College Roosevelt (UCR) Teaching Career Framework. Extract only statements about the candidate's educational activities, roles, outputs, evaluations, use, or recognition. Classify conservatively.

Domains:
{domains}

Levels: L1, L2, L3A (institutional leader), L3B (scholarly teacher), L4, or "Not assigned".

L3A requires evidence that the person shaped practice, structures, systems, decisions, or educational arrangements across UCR or a significant institutional unit. A title alone never establishes L3A. Committee membership is not leadership.
{l3a}

L3B requires a defined educational question, systematic investigation, evidence or data, analysis, reported findings, and use of the findings in educational practice. Disciplinary scholarship (literature, film, environmental humanities, media, and other subjects) is CONTEXT, even when the author teaches the subject or co-authored with a student.
{l3b}

Evidence types:
{types}

Statuses:
{statuses}

Rules:
- "quote" must be copied exactly, character for character, from the document text. Items whose quote cannot be found are discarded.
- Self-descriptions in a CV or reflective statement are claims. Mark them SUPPORTED or POTENTIAL, never VERIFIED.
- Do not infer impact, authorship, motives, or outcomes that the quote does not state.
- An award, a course, a job title, or research-led teaching does not establish L3A or L3B.
- Keep lower-level evidence (L1, L2). The framework is cumulative.
- level_reason: one or two sentences. missing_evidence: what exact additional evidence would strengthen the claim.
- Confidence is confidence in the classification, not the importance of the activity."""


class JSONProvider(Protocol):
    name: str

    def complete_json(self, system: str, user: str, schema: dict) -> dict:
        ...


class AnthropicProvider:
    """Claude via the official Anthropic Python SDK (``pip install anthropic``).

    Credentials come from ANTHROPIC_API_KEY or an ``ant auth login`` profile.
    The model can be changed with PEC_ANTHROPIC_MODEL.
    """

    name = "anthropic"

    def __init__(self, model: str | None = None):
        import anthropic

        self.client = anthropic.Anthropic()
        self.model = model or os.environ.get("PEC_ANTHROPIC_MODEL", "claude-opus-5-5")

    def complete_json(self, system: str, user: str, schema: dict) -> dict:
        response = self.client.beta.messages.create(
            model=self.model,
            max_tokens=16000,
            system=system,
            messages=[{"role": "user", "content": user}],
            output_config={"effort": "medium", "format": {"type": "json_schema", "schema": schema}},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )
        if response.stop_reason == "refusal":
            raise RuntimeError("The model declined this document. Classify it with the local rule engine.")
        if response.stop_reason == "max_tokens":
            raise RuntimeError("The model response was truncated. Reduce PEC chunk size or use the rule engine.")
        text = next(block.text for block in response.content if block.type == "text")
        return json.loads(text)


class LLMEngine:
    sends_text_externally = True

    def __init__(self, provider: JSONProvider):
        self.provider = provider
        self.name = f"llm:{provider.name}"

    def _chunks(self, doc: DocumentContext):
        buf, start = [], 1
        size = 0
        for page_no, page in enumerate(doc.pages, start=1):
            block = f"[{doc.page_label} {page_no}]\n{page}"
            if buf and size + len(block) > CHUNK_CHARS:
                yield start, "\n\n".join(buf)
                buf, size, start = [], 0, page_no
            buf.append(block)
            size += len(block)
        if buf:
            yield start, "\n\n".join(buf)

    def extract(self, doc: DocumentContext) -> list[Draft]:
        drafts: list[Draft] = []
        for _, chunk in self._chunks(doc):
            user = (
                f"Document filename: {doc.filename}\nDetected genre: {doc.genre}\n"
                f"Page markers appear as [{doc.page_label} N].\n\n<document>\n{chunk}\n</document>\n\n"
                "Return every candidate evidence item in this document."
            )
            result = self.provider.complete_json(system_prompt(), user, RESPONSE_SCHEMA)
            for item in result.get("items", []):
                drafts.append(Draft(
                    passage=item.get("quote", ""), page_no=int(item.get("page") or 1),
                    title=item.get("title", "")[:120], claim=item.get("claim", ""),
                    domains=item.get("domains", []), level=item.get("level", "Not assigned"),
                    level_reason=item.get("level_reason", ""), evidence_types=item.get("evidence_types", []),
                    status=item.get("status", "POTENTIAL"), confidence=item.get("confidence", "Low"),
                    missing_evidence=item.get("missing_evidence", []),
                ))
        return drafts
