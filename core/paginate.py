"""
core/paginate.py — Measured, Overflow-Safe Page Assembly

Root-cause fix for the whole class of footer collisions, clipped headings,
"page number stamped over the chart" and orphaned blank pages:

Instead of trusting that hand-authored page definitions fit an A4 sheet, the
engine measures the *actually rendered* height of every block (via the
Playwright/Chromium measurement pass in ``generators.pdf``) and reflows pages
that overflow:

* A page whose blocks exceed the content budget keeps the largest prefix that
  fits; the remaining blocks move to an auto-created **continuation sheet**
  that inherits the page's footer template (with an auto page number).
* ``keep_with_next`` semantics: section headings / subsections are never
  stranded at the very bottom of a page — they move together with their first
  follower.
* A single block taller than a whole empty page is an authoring error and
  fails fast with an actionable message (never silently clipped).
* Table-of-contents ``page_ref`` values are resolved against the *final*
  pagination, so TOC numbers stay correct after any spill.

The reflow is content-agnostic: it never inspects document text, only block
types, measured geometry, and page tokens.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any

from core.components import KEEP_WITH_NEXT_TYPES

__all__ = ["reflow", "resolve_toc_page_refs", "remaining_overflow"]

# Chromium rounding noise tolerance in CSS pixels.
TOLERANCE_PX = 2.0

# Minimum rows a table fragment must retain to justify a row-boundary split
# (below this the whole block moves, mirroring print engines' keep rules).
MIN_SPLIT_ROWS = 2


class BlockTooTallError(ValueError):
    """A single block exceeds the content area of an empty page."""


def _token_of(page: Mapping[str, Any], ordinal: int) -> str:
    return str(page.get("id", ordinal))


def _continuation_suffix_taken(pages: list[Mapping[str, Any]], token: str) -> int:
    taken = 0
    prefix = f"{token}~"
    for page in pages:
        page_id = page.get("id")
        if isinstance(page_id, str) and page_id.startswith(prefix):
            tail = page_id[len(prefix) :]
            if tail.isdigit():
                taken = max(taken, int(tail))
    return taken


def _continuation_footer(page: Mapping[str, Any]) -> Any:
    footer = page.get("footer")
    if not isinstance(footer, Mapping):
        return None
    inherited = {key: value for key, value in footer.items() if key != "center"}
    inherited["center"] = "{page}"
    return inherited


def _split_table(
    block: dict[str, Any],
    detail: Mapping[str, Any],
    space: float,
) -> tuple[dict[str, Any], dict[str, Any]] | None:
    """Split a table block at a row boundary to fit ``space`` px.

    Returns (head_part, tail_part) or None when a clean split is impossible.
    The head keeps the table title; the tail repeats the column header (the
    renderer always emits ``thead``), carries the caption when it holds the
    final rows, and preserves zebra parity via ``_zebra_offset``.
    """
    rows = block.get("rows", [])
    row_heights = detail.get("rowHeights") or []
    if len(row_heights) != len(rows) or len(rows) < MIN_SPLIT_ROWS + 1:
        return None
    if not isinstance(rows[0], list):
        return None

    fixed = (
        float(detail.get("marginTop", 0) or 0)
        + float(detail.get("titleHeight", 0) or 0)
        + float(detail.get("headerHeight", 0) or 0)
        + float(detail.get("marginBottom", 0) or 0)
    )
    avail = space - fixed
    if avail <= 0:
        return None

    used = 0.0
    m = 0
    for height in row_heights:
        if used + float(height) <= avail:
            used += float(height)
            m += 1
        else:
            break
    if m < MIN_SPLIT_ROWS or m >= len(rows):
        # All rows fit: consider splitting only when the caption would clip.
        caption = float(detail.get("captionHeight", 0) or 0)
        if m == len(rows) and caption > 0 and used + caption > avail:
            m -= 1
        if m < MIN_SPLIT_ROWS or m >= len(rows):
            return None

    head = dict(block)
    head["rows"] = rows[:m]
    head.pop("caption", None)
    tail = dict(block)
    tail["rows"] = rows[m:]
    tail.pop("title", None)
    tail.pop("subtitle", None)
    tail["_zebra_offset"] = int(block.get("_zebra_offset", 0)) + m
    return head, tail


def _place_tail(
    pages: list[dict[str, Any]],
    index: int,
    page: Mapping[str, Any],
    token: str,
    moved: list[dict[str, Any]],
    table_split: bool,
    report: dict[str, Any],
) -> int:
    """Place overflowing blocks: flow into the next page when it accepts
    content (natural document flow), otherwise create a continuation sheet.

    The next declared page accepts flow when it uses the standard layout and
    does not declare ``"break": true``. Pages carrying ``"break": true`` always
    start fresh — that is the declarative section-break mechanism.
    """
    nxt = pages[index + 1] if index + 1 < len(pages) else None
    if (
        nxt is not None
        and nxt.get("layout", "standard") == "standard"
        and not nxt.get("break")
    ):
        nxt["blocks"] = list(moved) + list(nxt.get("blocks", []))
        report["changed"] = True
        report["spills"].append(
            {
                "source": token,
                "flowed_into": str(nxt.get("id", index + 2)),
                "moved_blocks": len(moved),
                "table_split": table_split,
            }
        )
        # The receiving page's measurement is now stale; skip it this pass.
        return index + 2

    suffix = _continuation_suffix_taken(pages, token) + 1
    continuation = {
        "id": f"{token}~{suffix}",
        "layout": "standard",
        "_continuation": True,
        "footer": _continuation_footer(page),
        "blocks": moved,
    }
    pages.insert(index + 1, continuation)
    report["changed"] = True
    report["spills"].append(
        {
            "source": token,
            "continuation": continuation["id"],
            "moved_blocks": len(moved),
            "table_split": table_split,
        }
    )
    return index + 2


def reflow(
    document: dict[str, Any],
    measurements: list[Mapping[str, Any]],
    tolerance: float = TOLERANCE_PX,
) -> dict[str, Any]:
    """Move overflowing trailing blocks onto the next accepting page or a
    continuation sheet.

    Long tables split at row boundaries (repeating their header) before the
    engine falls back to moving the whole block.

    Mutates ``document['pages']`` in place and returns a report::
        {"changed": bool, "spills": [...], "warnings": [...]}
    """
    report: dict[str, Any] = {"changed": False, "spills": [], "warnings": []}
    by_token: dict[str, Mapping[str, Any]] = {}
    for entry in measurements:
        token = entry.get("token")
        if token:
            by_token[str(token)] = entry

    pages: list[dict[str, Any]] = document["pages"]
    index = 0
    while index < len(pages):
        page = pages[index]
        token = _token_of(page, index + 1)
        entry = by_token.get(token)
        if entry is None or not entry.get("measured"):
            index += 1
            continue

        content_client = float(entry.get("contentClient", 0) or 0)
        content_scroll = float(entry.get("contentScroll", 0) or 0)
        if content_scroll <= content_client + tolerance:
            index += 1
            continue

        blocks = page.get("blocks", [])
        heights = entry.get("blockHeights") or []
        details = entry.get("tableDetails") or []
        gap = float(entry.get("gap", 0) or 0)
        if len(heights) != len(blocks):
            report["warnings"].append(
                f"page '{token}': measurement mismatch "
                f"({len(blocks)} blocks vs {len(heights)} measured); overflow not reflowed"
            )
            index += 1
            continue

        budget = content_client + tolerance
        # Largest prefix of blocks that fits the content area.
        cumulative = 0.0
        k = 0
        for height in heights:
            needed = height if k == 0 else height + gap
            if cumulative + needed <= budget:
                cumulative += needed
                k += 1
            else:
                break

        if k == 0:
            # A block alone taller than the page: split tables, reject others.
            first = blocks[0] if blocks else {}
            if first.get("type") == "table" and details:
                split = _split_table(first, details[0] or {}, budget)
                if split:
                    head, tail = split
                    blocks[0] = head
                    moved = [tail, *blocks[1:]]
                    del blocks[1:]
                    index = _place_tail(pages, index, page, token, moved, True, report)
                    continue
            raise BlockTooTallError(
                f"page '{token}': first block (type '{first.get('type', '?')}') measures "
                f"{heights[0] if heights else 0:.0f}px but the content area only provides "
                f"{content_client:.0f}px. Reduce the block height (e.g. fewer rows, smaller "
                f"chart height) or move it to its own page."
            )

        if k >= len(blocks):
            # Everything fits within tolerance yet scrollHeight disagrees
            # (sub-pixel rounding): accept and warn.
            report["warnings"].append(
                f"page '{token}': overflow within measurement tolerance "
                f"({content_scroll:.0f}px vs {content_client:.0f}px)"
            )
            index += 1
            continue

        # Preferred: split a boundary table at a row boundary (keeps the page
        # filled like a real print engine) before demoting headings.
        boundary_block = blocks[k]
        if boundary_block.get("type") == "table" and details:
            space = budget - cumulative - gap
            split = _split_table(boundary_block, details[k] or {}, space)
            if split is not None:
                head, tail = split
                blocks[k] = head
                moved = [tail, *blocks[k + 1 :]]
                del blocks[k + 1 :]
                index = _place_tail(pages, index, page, token, moved, True, report)
                continue

        # keep_with_next: never strand a section introduction at the bottom.
        while k > 1 and str(blocks[k - 1].get("type", "")) in KEEP_WITH_NEXT_TYPES:
            k -= 1

        moved = blocks[k:]
        del blocks[k:]
        index = _place_tail(pages, index, page, token, moved, False, report)

    return report


def resolve_toc_page_refs(document: dict[str, Any]) -> bool:
    """Replace TOC ``page_ref`` tokens with the final page ordinals.

    A ``page_ref`` may reference either a page id or a block id (``anchor``):
    any block (including nested group children) carrying ``"id" == ref`` maps
    to the ordinal of the page that finally contains it after reflow.

    Returns True when at least one page number changed (so callers can
    re-render).
    """
    pages = document.get("pages", [])
    token_to_ordinal = {
        str(page.get("id", index)): index for index, page in enumerate(pages, start=1)
    }
    # Block anchors (any block with an explicit id, including group children).
    anchor_to_ordinal: dict[str, int] = {}

    def index_anchors(block: Any, ordinal: int) -> None:
        if isinstance(block, Mapping):
            block_id = block.get("id")
            if isinstance(block_id, str) and block_id and block_id not in anchor_to_ordinal:
                anchor_to_ordinal[block_id] = ordinal
            for child in block.get("children", []) or []:
                index_anchors(child, ordinal)

    for index, page in enumerate(pages, start=1):
        for block in page.get("blocks", []):
            index_anchors(block, index)

    def resolve(ref: str) -> int | None:
        if ref in token_to_ordinal:
            return token_to_ordinal[ref]
        return anchor_to_ordinal.get(ref)

    changed = False

    def visit(block: Any) -> None:
        nonlocal changed
        if isinstance(block, Mapping):
            if block.get("type") == "toc":
                for item in block.get("items", []):
                    if isinstance(item, Mapping) and "page_ref" in item:
                        ref = str(item["page_ref"])
                        ordinal = resolve(ref)
                        if ordinal is None:
                            raise ValueError(f"TOC page_ref target not found: {ref}")
                        new_value = str(ordinal)
                        if str(item.get("page", "")) != new_value:
                            changed = True
                        item["page"] = new_value
            for child in block.get("children", []) or []:
                visit(child)

    for page in pages:
        for block in page.get("blocks", []):
            visit(block)
    return changed


def remaining_overflow(measurements: list[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Report any page that still overflows after the final render."""
    issues = []
    for entry in measurements:
        if not entry.get("measured"):
            continue
        client = float(entry.get("contentClient", 0) or 0)
        scroll = float(entry.get("contentScroll", 0) or 0)
        if scroll > client + TOLERANCE_PX:
            issues.append(
                {
                    "page": entry.get("token"),
                    "content_client_px": round(client, 1),
                    "content_scroll_px": round(scroll, 1),
                }
            )
    return issues
