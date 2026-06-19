from __future__ import annotations

import re

TRAILING_PUNCTUATION = " .;:,"


def clean_fragment(value: str) -> str:
    text = _clean_spacing(str(value).strip())
    text = text.rstrip(TRAILING_PUNCTUATION)
    return _clean_spacing(text)


def clean_sentence(value: str) -> str:
    text = _clean_spacing(str(value).strip())
    text = re.sub(r"([.;:,])\s*([.;:,])+", r"\1", text)
    text = re.sub(r"\.;", ";", text)
    text = re.sub(r";\.", ".", text)
    text = re.sub(r"\.{2,}", ".", text)
    return _clean_spacing(text)


def ensure_period(value: str) -> str:
    text = clean_sentence(value).rstrip(TRAILING_PUNCTUATION)
    return f"{text}." if text else text


def capitalize_first(value: str) -> str:
    text = clean_sentence(value)
    return f"{text[:1].upper()}{text[1:]}" if text else text


def clean_items(items: list[str]) -> list[str]:
    return [clean_fragment(item) for item in items if clean_fragment(item)]


def _clean_spacing(value: str) -> str:
    text = re.sub(r"\s+", " ", value)
    text = re.sub(r"\s+([.;:,])", r"\1", text)
    text = re.sub(r"([.;:,])([A-Za-z])", r"\1 \2", text)
    return text.strip()
