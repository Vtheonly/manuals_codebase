"""Tests for the text-integrity, BiDi isolation, and pagination layers."""
from __future__ import annotations

import pytest

from core.normalize import normalize_document_spec
from core.paginate import reflow, resolve_toc_page_refs
from core.text import arabic_integrity_problems, bidi_isolate, fmt, normalize_document
from core.validate import validate


# ---------------------------------------------------------------------------
# NFC normalization
# ---------------------------------------------------------------------------

def test_nfc_normalization_composes_all_strings():
    doc = {"title": "e\u0301", "pages": [{"id": "p", "blocks": []}],
           "artifacts": [], "meta": ["c\u0327"]}
    out = normalize_document(doc)
    assert out["title"] == "é"
    assert out["meta"][0] == "ç"


# ---------------------------------------------------------------------------
# Arabic integrity lint
# ---------------------------------------------------------------------------

def test_integrity_lint_flags_space_before_diacritic():
    text = "نص ُمكسور"
    assert arabic_integrity_problems(text), "space before diacritic must be flagged"


def test_integrity_lint_flags_bidi_control_characters():
    assert arabic_integrity_problems("نص\u200f مخفي")
    assert arabic_integrity_problems("a\u200bb")


def test_integrity_lint_accepts_clean_text():
    assert arabic_integrity_problems("يُعَدّ التدريج مهما في الصناعة") == []


def test_compiler_rejects_broken_arabic(tmp_path, monkeypatch):
    import compiler
    source = tmp_path / "broken.json"
    source.write_text(
        '{"id": "x", "title": "t", "pages": [{"id": "p", "blocks": ['
        '{"type": "text", "content": "نص ُمكسور هنا"}]}], "artifacts": []}',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Arabic text integrity"):
        compiler.load_source(source)


# ---------------------------------------------------------------------------
# Bidirectional isolation
# ---------------------------------------------------------------------------

def test_bidi_isolates_codes_and_dates():
    assert fmt("الموسم التكويني: 2026") == (
        'الموسم التكويني: <bdi dir="ltr">2026</bdi>'
    )


def test_bidi_isolates_signed_numbers_with_units():
    out = fmt("زيادة +4.0 سم ودقة 95%")
    assert '<bdi dir="ltr">+4.0</bdi>' in out
    assert '<bdi dir="ltr">95%</bdi>' in out


def test_bidi_keeps_french_phrases_together():
    assert '<bdi dir="ltr">Point d\'Évolution</bdi>' in fmt("Point d'Évolution")


def test_bidi_leaves_pure_arabic_untouched():
    assert fmt("الجزائر النسائية") == "الجزائر النسائية"


def test_bidi_plain_text_mode_escapes_markup():
    out = fmt("<script>alert(1)</script>")
    assert "<script>" not in out
    assert "&lt;" in out


def test_bidi_trusted_markup_preserves_tags_and_isolates_text_nodes():
    out = bidi_isolate("<b>المعيار</b> NA EN 13402", escape=False)
    assert out.startswith("<b>")
    assert '<bdi dir="ltr">NA EN 13402</bdi>' in out


def test_bidi_entities_pass_through_in_trusted_mode():
    out = bidi_isolate("القيمة &amp; المرجع NA 5", escape=False)
    assert "&amp;" in out


# ---------------------------------------------------------------------------
# Strict chart contract (ghost-chart guard)
# ---------------------------------------------------------------------------

def _doc_with_chart(chart):
    return {
        "id": "d", "title": "t",
        "pages": [{"id": "p", "blocks": [
            {"type": "artifact_ref", "artifact_id": "c"}]}],
        "artifacts": [dict({"id": "c", "type": "chart"}, **chart)],
    }


def test_empty_chart_series_fails_fast():
    with pytest.raises(ValueError, match="series"):
        validate(_doc_with_chart({"kind": "line", "labels": ["1", "2", "3"], "series": []}))


def test_empty_chart_values_fail_fast():
    with pytest.raises(ValueError, match="ghost chart guard"):
        validate(_doc_with_chart({"kind": "bar", "labels": [], "values": []}))


def test_non_numeric_chart_values_fail_fast():
    with pytest.raises(ValueError, match="number"):
        validate(_doc_with_chart({"kind": "bar", "labels": ["a"], "values": ["x"]}))


def test_chart_aliases_normalize_before_validation():
    doc = _doc_with_chart({"kind": "bar", "categories": ["a", "b"], "data": [1, 2]})
    validate(normalize_document_spec(doc))  # aliases resolve; no error


# ---------------------------------------------------------------------------
# TOC contract
# ---------------------------------------------------------------------------

def test_toc_item_without_page_fails_fast():
    doc = {
        "id": "d", "title": "t",
        "pages": [{"id": "p", "blocks": [
            {"type": "toc", "title": "فهرس",
             "items": [{"badge": "1", "title": "قسم"}]}]}],
        "artifacts": [],
    }
    with pytest.raises(ValueError, match="TOC starvation guard"):
        validate(doc)


def test_toc_page_ref_must_reference_known_page():
    doc = {
        "id": "d", "title": "t",
        "pages": [{"id": "p", "blocks": [
            {"type": "toc", "title": "فهرس",
             "items": [{"badge": "1", "title": "قسم", "page_ref": "ghost"}]}]}],
        "artifacts": [],
    }
    with pytest.raises(ValueError, match="page_ref"):
        validate(doc)


# ---------------------------------------------------------------------------
# Pagination: row-boundary table splitting + flow
# ---------------------------------------------------------------------------

def _measurement(token, client, heights, rows=None, gap=12.0, details=None):
    rows = rows or []
    return {
        "token": token,
        "measured": True,
        "contentClient": client,
        "contentScroll": client + 500,
        "blockHeights": heights,
        "tableDetails": details or [None] * len(heights),
        "gap": gap,
    }


def test_table_splits_at_row_boundary_and_flows_into_next_page():
    document = {
        "pages": [
            {"id": "page-1", "layout": "standard", "footer": {"center": "{page}"},
             "blocks": [
                 {"type": "text", "content": "lead"},
                 {"type": "table",
                  "columns": [["h1", ""], ["h2", ""]],
                  "rows": [["r1a", "r1b"], ["r2a", "r2b"], ["r3a", "r3b"],
                           ["r4a", "r4b"]]},
             ]},
            {"id": "page-2", "layout": "standard", "footer": {"center": "{page}"},
             "blocks": [{"type": "text", "content": "next page"}]},
        ]
    }
    detail = {"marginTop": 8, "marginBottom": 8, "titleHeight": 0,
              "headerHeight": 30, "captionHeight": 0,
              "rowHeights": [100, 100, 100, 100]}
    # Budget fits lead + title + header + 2 rows only.
    measurement = _measurement("page-1", 400, [50, 438], details=[None, detail])
    report = reflow(document, [measurement])
    assert report["changed"]
    table = document["pages"][0]["blocks"][1]
    assert len(table["rows"]) == 2
    assert document["pages"][1]["blocks"][0]["type"] == "table"
    assert document["pages"][1]["blocks"][0]["_zebra_offset"] == 2
    assert document["pages"][1]["blocks"][-1]["content"] == "next page"


def test_keep_with_next_demotes_stranded_heading():
    document = {
        "pages": [
            {"id": "page-1", "layout": "standard",
             "blocks": [
                 {"type": "text", "content": "a"},
                 {"type": "subsection", "title": "head"},
                 {"type": "text", "content": "tail"},
             ]},
            {"id": "page-2", "layout": "standard",
             "blocks": [{"type": "text", "content": "next"}]},
        ]
    }
    measurement = _measurement("page-1", 210, [100, 100, 100])
    report = reflow(document, [measurement])
    assert report["changed"]
    moved = document["pages"][1]["blocks"]
    assert moved[0]["type"] == "subsection"
    assert moved[1]["content"] == "tail"


def test_break_page_rejects_flow_and_gets_continuation():
    document = {
        "pages": [
            {"id": "page-1", "layout": "standard",
             "blocks": [{"type": "text", "content": "a"},
                        {"type": "text", "content": "b"}]},
            {"id": "page-2", "layout": "standard", "break": True,
             "blocks": [{"type": "text", "content": "fresh"}]},
        ]
    }
    measurement = _measurement("page-1", 150, [100, 100])
    report = reflow(document, [measurement])
    assert report["changed"]
    assert len(document["pages"]) == 3
    assert document["pages"][1]["id"] == "page-1~1"
    assert document["pages"][2]["blocks"][0]["content"] == "fresh"


def test_resolve_toc_page_refs_uses_final_ordinals():
    document = {
        "pages": [
            {"id": "p1", "blocks": [
                {"type": "toc", "title": "t",
                 "items": [{"badge": "1", "title": "x", "page_ref": "p3"},
                           {"badge": "2", "title": "y", "page_ref": "sec"}]}]},
            {"id": "p2", "blocks": []},
            {"id": "p3", "blocks": [{"type": "heading", "id": "sec", "title": "h"}]},
        ]
    }
    changed = resolve_toc_page_refs(document)
    assert changed
    assert document["pages"][0]["blocks"][0]["items"][0]["page"] == "3"
    assert document["pages"][0]["blocks"][0]["items"][1]["page"] == "3"


# ---------------------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------------------

def test_badge_typography_token_exists():
    from core.design import DesignSystem
    design = DesignSystem()
    assert design.typography.families["badge"].startswith("'Noto Kufi Arabic'")
