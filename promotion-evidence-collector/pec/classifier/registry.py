"""Engine registry. Add new engines or LLM providers here."""

from __future__ import annotations

from .base import ExtractionEngine
from .rules import RuleEngine

ENGINES = {
    "rules": "Local rules (no text leaves this computer)",
    "anthropic": "Claude via Anthropic API (sends extracted text to Anthropic)",
}


def get_engine(name: str = "rules") -> ExtractionEngine:
    if name == "rules":
        return RuleEngine()
    if name == "anthropic":
        from .llm import AnthropicProvider, LLMEngine

        return LLMEngine(AnthropicProvider())
    raise ValueError(f"Unknown engine: {name}")
