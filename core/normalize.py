"""
core/normalize.py — Ingestion Normalization Layer

Runs before validation so every downstream consumer (validators, SVG
generators, component renderers) sees one canonical data contract:

* Unicode NFC normalization of every string (see ``core.text``).
* Chart field aliases: common synonyms (``data`` -> ``values``,
  ``categories`` -> ``labels``, ``points`` -> ``values`` …) are mapped to the
  canonical contract instead of silently producing ghost charts.
* Numeric coercion: numeric strings ("4.5") become floats so the strict
  numeric validation can rely on real numbers.

The layer is generic and content-agnostic: it never invents or repairs
document data, it only canonicalizes equivalent spellings of the same contract.
"""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from core.text import normalize_document

__all__ = ["normalize_document_spec"]

# chart kind -> alias map applied to the artifact spec itself
_CHART_ALIASES = {
    "values": ("data", "points", "amounts"),
    "labels": ("categories", "category_labels", "x_labels"),
}
_SERIES_ALIASES = {
    "values": ("data", "points"),
    "label": ("name", "title"),
}


def _coerce_number(value: Any) -> Any:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        stripped = value.strip()
        try:
            return float(stripped)
        except ValueError:
            return value
    return value


def _normalize_chart(artifact: dict[str, Any]) -> dict[str, Any]:
    kind = artifact.get("kind")

    # Resolve top-level aliases (never overwrite canonical keys).
    for canonical, aliases in _CHART_ALIASES.items():
        if canonical in artifact:
            continue
        for alias in aliases:
            if alias in artifact:
                artifact[canonical] = artifact.pop(alias)
                break

    if kind == "progress":
        items = artifact.get("items")
        if isinstance(items, list):
            for item in items:
                if isinstance(item, Mapping):
                    if "label" not in item and "name" in item:
                        item["label"] = item.pop("name")
                    for numeric_key in ("value", "max"):
                        if numeric_key in item:
                            item[numeric_key] = _coerce_number(item[numeric_key])
        return artifact

    if kind == "line":
        series = artifact.get("series")
        if isinstance(series, list):
            for item in series:
                if isinstance(item, Mapping):
                    for canonical, aliases in _SERIES_ALIASES.items():
                        if canonical in item:
                            continue
                        for alias in aliases:
                            if alias in item:
                                item[canonical] = item.pop(alias)
                                break
                    if "values" in item and isinstance(item["values"], list):
                        item["values"] = [_coerce_number(v) for v in item["values"]]
        return artifact

    if "values" in artifact and isinstance(artifact["values"], list):
        artifact["values"] = [_coerce_number(v) for v in artifact["values"]]
    return artifact


def _normalize_document(document: Any) -> Any:
    if isinstance(document, Mapping):
        normalized = {key: _normalize_document(value) for key, value in document.items()}
        if (
            normalized.get("type") == "chart"
            and isinstance(normalized.get("kind"), str)
        ):
            return _normalize_chart(dict(normalized))
        return normalized
    if isinstance(document, list):
        return [_normalize_document(value) for value in document]
    return document


def normalize_document_spec(document: Any) -> Any:
    """NFC-normalize + contract-canonicalize a freshly loaded JSON document."""
    return _normalize_document(normalize_document(document))
