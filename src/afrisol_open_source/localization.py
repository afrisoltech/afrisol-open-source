"""Small dependency-free helpers for locale-aware application interfaces."""

import re

_LANGUAGE_TAG = re.compile(r"^[A-Za-z]{2,3}(?:-[A-Za-z]{2}|-[0-9]{3})?$")
SUPPORTED_LANGUAGES = frozenset({"en", "sw", "fr", "ar", "pt"})


def normalize_language_tag(value: str) -> str:
    """Normalize a simple BCP-47 language tag; reject malformed input."""
    if not isinstance(value, str) or not _LANGUAGE_TAG.fullmatch(value):
        raise ValueError("Invalid language tag")
    parts = value.split("-")
    return parts[0].lower() + ("-" + parts[1].upper() if len(parts) == 2 else "")


def supported_language(value: str, fallback: str = "en") -> str:
    """Return a supported base language, or a validated fallback."""
    normalized = normalize_language_tag(value)
    default = normalize_language_tag(fallback).split("-")[0]
    if default not in SUPPORTED_LANGUAGES:
        raise ValueError("Unsupported fallback language")
    base = normalized.split("-")[0]
    return base if base in SUPPORTED_LANGUAGES else default
