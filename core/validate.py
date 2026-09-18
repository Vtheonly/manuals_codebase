"""
core/validate.py — Generic Document Schema & Semantic Contract Validation
Ensures incoming JSON documents conform to generic component and artifact specifications.
"""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

BLOCK_TYPES = {
    "heading",
    "subsection",
    "formula",
    "text",
    "badge",
    "card",
    "info_card",
    "callout",
    "stats",
    "table",
    "flow_steps",
    "toc",
    "quote",
    "list",
    "spacer",
    "group",
    "image",
    "divider",
    "artifact_ref",
}
CHART_KINDS = {"bar", "line", "donut", "progress"}
DIAGRAM_KINDS = {"flow", "graph"}


def validate(document: Mapping[str, Any]) -> None:
    required = ("id", "title", "pages", "artifacts")
    missing = [key for key in required if key not in document]
    if missing:
        raise ValueError(f"Missing document fields: {', '.join(missing)}")

    if not isinstance(document["pages"], list) or not document["pages"]:
        raise ValueError("'pages' must be a non-empty array")
    if not isinstance(document["artifacts"], list):
        raise ValueError("'artifacts' must be an array")

    artifact_ids: set[str] = set()
    for artifact in document["artifacts"]:
        _require_mapping(artifact, "artifact")
        artifact_id = _require_string(artifact, "id", "artifact")
        if artifact_id in artifact_ids:
            raise ValueError(f"Duplicate artifact id: {artifact_id}")
        artifact_ids.add(artifact_id)
        _validate_artifact(artifact)

    page_ids: set[str] = set()
    references: list[str] = []
    for index, page in enumerate(document["pages"], start=1):
        _require_mapping(page, f"page {index}")
        page_id = page.get("id")
        if page_id is not None:
            if not isinstance(page_id, str) or not page_id:
                raise ValueError(f"page {index}: 'id' must be a non-empty string")
            if page_id in page_ids:
                raise ValueError(f"Duplicate page id: {page_id}")
            page_ids.add(page_id)

        blocks = page.get("blocks", [])
        if not isinstance(blocks, list):
            raise ValueError(f"page {index}: 'blocks' must be an array")
        for block_index, block in enumerate(blocks, start=1):
            references.extend(_validate_block(block, f"page {index} block {block_index}"))

    missing_refs = sorted(set(references) - artifact_ids)
    if missing_refs:
        raise ValueError(f"Unknown artifact reference(s): {', '.join(missing_refs)}")


def _validate_artifact(artifact: Mapping[str, Any]) -> None:
    artifact_type = artifact.get("type")
    if artifact_type == "chart":
        _require_string(artifact, "kind", "chart")
        kind = artifact["kind"]
        if kind not in CHART_KINDS:
            raise ValueError(f"Unsupported chart kind: {kind}")

        if kind == "progress":
            _require_list(artifact, "items", "chart")
            return

        _require_list(artifact, "labels", "chart")
        if kind == "line" and artifact.get("series") is not None:
            series = _require_list(artifact, "series", "chart")
            for index, item in enumerate(series, start=1):
                if not isinstance(item, Mapping):
                    raise ValueError(f"chart series item {index} must be an object")
                _require_list(item, "values", f"chart series item {index}")
            lengths = {len(item["values"]) for item in series}
            if len(lengths) > 1:
                raise ValueError("All line chart series must have the same number of values")
            if lengths and next(iter(lengths)) != len(artifact["labels"]):
                raise ValueError("Line chart series values must match the labels length")
            return

        _require_list(artifact, "values", "chart")
        if len(artifact["labels"]) != len(artifact["values"]):
            raise ValueError("Chart labels and values must have the same length")
    elif artifact_type == "diagram":
        _require_string(artifact, "kind", "diagram")
        if artifact["kind"] not in DIAGRAM_KINDS:
            raise ValueError(f"Unsupported diagram kind: {artifact['kind']}")
        if artifact["kind"] == "flow":
            _require_list(artifact, "steps", "diagram")
        else:
            _require_list(artifact, "nodes", "diagram")
            _require_list(artifact, "edges", "diagram")
    else:
        raise ValueError(f"Unsupported artifact type: {artifact_type}")


def _validate_block(block: Any, context: str) -> list[str]:
    _require_mapping(block, context)
    kind = block.get("type")
    if kind not in BLOCK_TYPES:
        raise ValueError(f"{context}: unsupported block type: {kind}")

    if kind == "artifact_ref":
        return [_require_string(block, "artifact_id", context)]

    if kind in {"heading", "card", "callout", "quote", "toc", "subsection"}:
        _require_string(block, "title" if kind != "quote" else "text", context)
    if kind == "badge":
        _require_string(block, "text", context)
    if kind == "formula":
        if "expression" not in block and "html_expression" not in block:
            raise ValueError(f"{context}: missing 'expression' or 'html_expression'")
    if kind == "text":
        if "content" not in block and "text" not in block:
            raise ValueError(f"{context}: missing 'content' or 'text'")
    if kind == "table":
        _require_list(block, "columns", context)
        _require_list(block, "rows", context)
    if kind == "info_card":
        _require_list(block, "rows", context)
    if kind == "stats":
        _require_list(block, "items", context)
    if kind == "flow_steps":
        _require_list(block, "steps", context)
    if kind == "group":
        children = _require_list(block, "children", context)
        for index, child in enumerate(children, start=1):
            _validate_block(child, f"{context} child {index}")
    if kind == "image":
        _require_string(block, "src", context)
    if kind == "list":
        _require_list(block, "items", context)

    return []


def _require_mapping(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{context} must be an object")
    return value


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise ValueError(f"{context}: '{key}' must be an array")
    return value


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{context}: '{key}' must be a non-empty string")
    return value