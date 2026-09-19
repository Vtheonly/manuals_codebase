"""
core/validate.py — Generic Document Schema & Semantic Contract Validation
Ensures incoming JSON documents conform to generic component and artifact
specifications.

The contract is strict and fails fast:

* Charts must carry non-empty, numeric data — a chart generator must never
  silently emit an empty coordinate box (ghost chart) because a data array was
  missing or empty.
* Table-of-contents items must declare a title plus a page reference
  (``page`` or ``page_ref``) — missing accessories are omitted by the template,
  but a TOC row without a page target is a contract violation.
* Unknown artifact references, unknown page_ref targets and malformed block
  shapes are rejected with precise context.

A ``page_ref`` may reference either a **page id** or a **block anchor** — any
block (including nested group children) carrying an ``"id"`` field. This
mirrors exactly what ``core.paginate.resolve_toc_page_refs`` resolves against
after reflow, so the validator accepts precisely the references the runtime
can honour.
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
        _validate_artifact(artifact, f"artifact '{artifact_id}'")

    page_ids: set[str] = set()
    references: list[str] = []
    block_anchor_ids: set[str] = set()
    toc_page_refs: set[str] = set()
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
            context = f"page {index} block {block_index}"
            references.extend(
                _validate_block(block, context, toc_page_refs, block_anchor_ids)
            )

    missing_refs = sorted(set(references) - artifact_ids)
    if missing_refs:
        raise ValueError(f"Unknown artifact reference(s): {', '.join(missing_refs)}")

    # A page_ref resolves against page ids ∪ block anchor ids (the same
    # resolution space the runtime uses after reflow).
    page_ref_targets = page_ids | block_anchor_ids
    unresolved_refs = sorted(toc_page_refs - page_ref_targets)
    if unresolved_refs:
        raise ValueError(
            "TOC page_ref target(s) not found among page ids or block anchors: "
            + ", ".join(unresolved_refs)
        )
    # A page id and a block anchor must not share a token: resolution order
    # would silently prefer the page and hide an authoring mistake.
    ambiguous = sorted(page_ids & block_anchor_ids)
    if ambiguous:
        raise ValueError(
            "id(s) used both as a page id and a block anchor are ambiguous: "
            + ", ".join(ambiguous)
        )


def _validate_artifact(artifact: Mapping[str, Any], context: str) -> None:
    artifact_type = artifact.get("type")
    if artifact_type == "chart":
        _require_string(artifact, "kind", context)
        kind = artifact["kind"]
        if kind not in CHART_KINDS:
            raise ValueError(f"{context}: unsupported chart kind: {kind}")

        if kind == "progress":
            items = _require_list(artifact, "items", context)
            if not items:
                raise ValueError(f"{context}: 'items' must not be empty")
            for index, item in enumerate(items, start=1):
                if not isinstance(item, Mapping):
                    raise ValueError(f"{context} progress item {index} must be an object")
                _require_number(item, "value", f"{context} progress item {index}")
                if "max" in item:
                    _require_number(item, "max", f"{context} progress item {index}")
            return

        labels = _require_list(artifact, "labels", context)
        if not labels:
            raise ValueError(f"{context}: 'labels' must not be empty (ghost chart guard)")

        if kind == "line":
            series = artifact.get("series")
            if series is None:
                # single-series form: top-level `values`
                values = _require_numbers(artifact, "values", context)
                if len(values) != len(labels):
                    raise ValueError(f"{context}: line chart values must match the labels length")
                return
            if not isinstance(series, list) or not series:
                raise ValueError(f"{context}: 'series' must be a non-empty array")
            lengths: set[int] = set()
            for index, item in enumerate(series, start=1):
                if not isinstance(item, Mapping):
                    raise ValueError(f"{context} series item {index} must be an object")
                item_values = _require_numbers(item, "values", f"{context} series item {index}")
                lengths.add(len(item_values))
            if len(lengths) > 1:
                raise ValueError(f"{context}: all line chart series must have the same number of values")
            if lengths and next(iter(lengths)) != len(labels):
                raise ValueError(f"{context}: line chart series values must match the labels length")
            return

        values = _require_numbers(artifact, "values", context)
        if len(values) != len(labels):
            raise ValueError(f"{context}: chart labels and values must have the same length")
        if kind == "donut":
            total = sum(values)
            if total <= 0:
                raise ValueError(f"{context}: donut chart values must sum to a positive number")
            if any(v < 0 for v in values):
                raise ValueError(f"{context}: donut chart values must be non-negative")
        return

    if artifact_type == "diagram":
        _require_string(artifact, "kind", context)
        if artifact["kind"] not in DIAGRAM_KINDS:
            raise ValueError(f"{context}: unsupported diagram kind: {artifact['kind']}")
        if artifact["kind"] == "flow":
            steps = _require_list(artifact, "steps", context)
            if not steps:
                raise ValueError(f"{context}: 'steps' must not be empty")
        else:
            nodes = _require_list(artifact, "nodes", context)
            if not nodes:
                raise ValueError(f"{context}: 'nodes' must not be empty")
            _require_list(artifact, "edges", context)
        return

    raise ValueError(f"{context}: unsupported artifact type: {artifact_type}")


def _validate_block(
    block: Any,
    context: str,
    toc_page_refs: set[str] | None = None,
    anchor_ids: set[str] | None = None,
) -> list[str]:
    _require_mapping(block, context)
    kind = block.get("type")
    if kind not in BLOCK_TYPES:
        raise ValueError(f"{context}: unsupported block type: {kind}")

    # Any block carrying an explicit string id becomes a resolvable TOC
    # anchor (mirrors core.paginate.resolve_toc_page_refs).
    block_id = block.get("id")
    if block_id is not None:
        if not isinstance(block_id, str) or not block_id:
            raise ValueError(f"{context}: 'id' must be a non-empty string")
        if anchor_ids is not None:
            anchor_ids.add(block_id)

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
        columns = _require_list(block, "columns", context)
        if not columns:
            raise ValueError(f"{context}: 'columns' must not be empty")
        _require_list(block, "rows", context)
    if kind == "info_card":
        rows = _require_list(block, "rows", context)
        if not rows:
            raise ValueError(f"{context}: 'rows' must not be empty")
    if kind == "stats":
        items = _require_list(block, "items", context)
        if not items:
            raise ValueError(f"{context}: 'items' must not be empty")
    if kind == "flow_steps":
        steps = _require_list(block, "steps", context)
        if not steps:
            raise ValueError(f"{context}: 'steps' must not be empty")
    if kind == "group":
        children = _require_list(block, "children", context)
        for index, child in enumerate(children, start=1):
            _validate_block(child, f"{context} child {index}", toc_page_refs, anchor_ids)
    if kind == "image":
        _require_string(block, "src", context)
    if kind == "list":
        items = _require_list(block, "items", context)
        if not items:
            raise ValueError(f"{context}: 'items' must not be empty")
    if kind == "toc":
        _validate_toc(block, context, toc_page_refs if toc_page_refs is not None else set())

    return []


def _validate_toc(block: Mapping[str, Any], context: str, toc_page_refs: set[str]) -> None:
    items = block.get("items")
    if not isinstance(items, list) or not items:
        raise ValueError(f"{context}: 'items' must be a non-empty array")
    for index, item in enumerate(items, start=1):
        item_context = f"{context} item {index}"
        if not isinstance(item, Mapping):
            raise ValueError(f"{item_context} must be an object")
        title = item.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"{item_context}: 'title' must be a non-empty string")
        has_page = "page" in item
        has_ref = "page_ref" in item
        if has_page and has_ref:
            raise ValueError(f"{item_context}: 'page' and 'page_ref' are mutually exclusive")
        if not has_page and not has_ref:
            raise ValueError(
                f"{item_context}: requires 'page' or 'page_ref' (TOC starvation guard)"
            )
        if has_page and not str(item["page"]).strip():
            raise ValueError(f"{item_context}: 'page' must be a non-empty value")
        if has_ref:
            ref = item["page_ref"]
            if not isinstance(ref, str) or not ref:
                raise ValueError(f"{item_context}: 'page_ref' must be a non-empty string")
            toc_page_refs.add(ref)


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


def _require_number(mapping: Mapping[str, Any], key: str, context: str) -> float:
    value = mapping.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{context}: '{key}' must be a number")
    return float(value)


def _require_numbers(mapping: Mapping[str, Any], key: str, context: str) -> list[float]:
    values = _require_list(mapping, key, context)
    if not values:
        raise ValueError(f"{context}: '{key}' must not be empty (ghost chart guard)")
    for index, value in enumerate(values):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{context}: '{key}[{index}]' must be a number")
    return [float(v) for v in values]
