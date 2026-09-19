"""
core/text.py — Text Integrity & Bidirectional Isolation Layer

Root-cause fixes implemented here (no per-document logic, purely generic):

1. **Unicode NFC normalization** applied to every string of the ingested JSON so
   decomposed Arabic (or Latin) sequences compose deterministically before any
   rendering decision is made.

2. **Arabic joining-integrity lint** that flags *unambiguous* corruption only
   (whitespace in front of a diacritic, invisible BiDi control characters, …).
   The engine never *guesses* how to rejoin broken letters at render time — it
   fails fast so the source data can be repaired at the source.

3. **Automated bidirectional isolation** (`bidi_isolate` / `fmt`): any run of
   Latin letters, European digits, signed numbers, codes, dates, slash
   expressions, or mixed French/Latin phrases embedded in RTL prose is wrapped
   in `<bdi dir="ltr">…</bdi>` before escaping. This removes the entire class of
   UBA (Unicode Bidirectional Algorithm) inversions: flipped parentheses,
   mirrored slashes, signs detached from numbers (`+4.0` rendering as `4.0+`),
   and scrambled codes or dates embedded in RTL prose.

The scanner is tag-aware: markup is preserved untouched and only text nodes
are processed, so it can safely run over both plain values and author-supplied
HTML fragments.
"""
from __future__ import annotations

import html as _html
import re
import unicodedata
from collections.abc import Mapping
from typing import Any

__all__ = [
    "normalize_document",
    "bidi_isolate",
    "fmt",
    "arabic_integrity_problems",
    "document_integrity_report",
]

# ---------------------------------------------------------------------------
# 1. Unicode normalization
# ---------------------------------------------------------------------------


def normalize_document(document: Any) -> Any:
    """Recursively apply NFC normalization to every string in a JSON document.

    This composes decomposed code points (Arabic hamza carriers, Latin
    accents) into their canonical forms and is a strict no-op for text that is
    already normalized — which is the common case.
    """
    if isinstance(document, str):
        return unicodedata.normalize("NFC", document)
    if isinstance(document, Mapping):
        return {key: normalize_document(value) for key, value in document.items()}
    if isinstance(document, list):
        return [normalize_document(value) for value in document]
    return document


# ---------------------------------------------------------------------------
# 2. Arabic joining-integrity lint (unambiguous failures only)
# ---------------------------------------------------------------------------

# Invisible / control characters that must never appear in source content.
_INVISIBLE = re.compile(r"[\u200b\u200e\u200f\u202a-\u202e\u2066-\u2069\ufffe\uffff]")
# Whitespace directly in front of a combining diacritic (tashkeel) or a
# superscript/subscript alef — always a corruption of Arabic joining.
_SPACE_BEFORE_DIACRITIC = re.compile(r"[\s\u00a0][\u064b-\u0652\u0670]")
# A diacritic followed by whitespace followed by a letter that joins to the
# left is ambiguous (legitimate word boundary), so it is NOT flagged here.


def arabic_integrity_problems(text: str) -> list[str]:
    """Return human-readable descriptions of unambiguous Arabic corruption."""
    problems: list[str] = []
    for match in _SPACE_BEFORE_DIACRITIC.finditer(text):
        problems.append(f"whitespace before combining mark at offset {match.start()}: {text[max(0, match.start() - 8):match.end() + 8]!r}")
    if _INVISIBLE.search(text):
        problems.append("contains invisible/control characters (zero-width or BiDi controls)")
    return problems


def document_integrity_report(document: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Walk a document and collect every string with integrity problems.

    Returns a list of ``{"path": str, "problems": [str, ...]}`` entries so
    callers can fail fast with precise, actionable error messages.
    """
    report: list[dict[str, Any]] = []

    def visit(node: Any, path: str) -> None:
        if isinstance(node, str):
            problems = arabic_integrity_problems(node)
            if problems:
                report.append({"path": path, "problems": problems})
        elif isinstance(node, Mapping):
            for key, value in node.items():
                visit(value, f"{path}.{key}")
        elif isinstance(node, list):
            for index, value in enumerate(node):
                visit(value, f"{path}[{index}]")

    visit(document, "$")
    return report


# ---------------------------------------------------------------------------
# 3. Bidirectional isolation engine
# ---------------------------------------------------------------------------

# Neutrals that may *bridge* two strong-LTR/number tokens inside a single
# isolated run (so “BTS Modélisme et CAO” or a slashed code pair stays in one
# piece). Trailing/leading neutrals are trimmed so surrounding Arabic text
# keeps its natural spacing.
_BRIDGE_CHARS = set(
    " \t\n\r"
    ".,:;/"          # punctuation
    "()[]{}"          # grouping
    "'\"‘’«»"         # quotes & apostrophes
    "+<=>"            # relational / arithmetic
    "%" "°" "×" "÷"   # units & operators
    "·" "•"           # separators
    "→" "↔" "←"       # arrows
    "\u00a0"          # no-break space
    "\u2019"          # right single quotation mark (French apostrophe)
    "\u2013"          # en dash
)

_TAG_RE = re.compile(r"(<[^>]*>)", re.S)
# Markup tokens (tags + character entities) that must pass through untouched
# when processing trusted author HTML.
_MARKUP_TOKEN_RE = re.compile(
    r"<[^>]*>|&(?:[a-zA-Z][a-zA-Z0-9]*|#[0-9]+|#[xX][0-9a-fA-F]+);", re.S
)


def _class_of(ch: str) -> str:
    code = ord(ch)
    if (
        0x0600 <= code <= 0x06FF
        or 0x0750 <= code <= 0x077F
        or 0x08A0 <= code <= 0x08FF
        or 0xFB50 <= code <= 0xFDFF
        or 0xFE70 <= code <= 0xFEFF
    ):
        return "R"  # Arabic script block (letters, diacritics, AN digits)
    if ch.isalpha():
        return "L"  # strong LTR letters (Latin, Greek, Cyrillic, …)
    if ch.isdigit():
        return "D"  # European digits
    if ch in _BRIDGE_CHARS:
        return "N"  # bridgeable neutral
    return "X"      # unbridgeable neutral (em dash, #, @, …)


def _isolate_segment(segment: str, escape: bool) -> str:
    """Isolate LTR runs inside one plain-text segment.

    ``escape`` controls whether the non-markup text is HTML-escaped here (it
    must happen *after* run detection because escaping would inject entity
    letters that confuse the scanner).
    """
    if not segment:
        return segment
    classes = [_class_of(ch) for ch in segment]
    length = len(segment)

    def esc(part: str) -> str:
        return _html.escape(part, quote=False) if escape else part

    out: list[str] = []
    cursor = 0  # start of unprocessed region

    def find_seed(start: int) -> int | None:
        for pos in range(start, length):
            if classes[pos] in ("L", "D"):
                return pos
        return None

    while True:
        seed = find_seed(cursor)
        if seed is None:
            break
        # Grow right: include L/D and bridged neutrals (neutrals only when a
        # further L/D token follows them before any Arabic character).
        end = seed + 1
        while end < length:
            kind = classes[end]
            if kind in ("L", "D"):
                end += 1
                continue
            if kind == "N":
                probe = end + 1
                while probe < length and classes[probe] == "N":
                    probe += 1
                if probe < length and classes[probe] in ("L", "D"):
                    end = probe + 1
                    continue
            break
        # Trim trailing bridged neutrals.
        while end > seed and classes[end - 1] == "N":
            end -= 1
        # Grow left (signs, digits preceding letters are already seeded by
        # find_seed, so this only extends over leading bridgeable neutrals
        # when more L/D material sits on the other side).
        start = seed
        while start > 0:
            kind = classes[start - 1]
            if kind in ("L", "D"):
                start -= 1
                continue
            if kind == "N":
                probe = start - 1
                while probe > 0 and classes[probe - 1] == "N":
                    probe -= 1
                if probe > 0 and classes[probe - 1] in ("L", "D"):
                    start = probe
                    continue
            break
        # Absorb one level of directly enclosing parentheses/brackets.
        if (
            start > 0
            and end < length
            and segment[start - 1] in "([{"
            and segment[end] in ")]}"
            and _matches_bracket(segment[start - 1], segment[end])
        ):
            start -= 1
            end += 1
        # Absorb a leading sign glued to a numeric run (+4.0, -3.5, ±1) so the
        # neutral sign can never be captured by the surrounding RTL flow.
        if classes[start] == "D" and start > 0 and segment[start - 1] in "+-±\u2212":
            start -= 1
        # Absorb a unit suffix glued to the numeric run (75%, 90°) for the
        # same reason.
        if classes[end - 1] == "D" and end < length and segment[end] in "%°":
            end += 1

        run_classes = classes[start:end]
        has_letter = any(c == "L" for c in run_classes)
        has_digit = any(c == "D" for c in run_classes)
        structural = any(c == "N" for c in run_classes)
        if not (has_letter or (has_digit and structural)):
            # Plain number without structure: leave to the native bidi
            # algorithm (visually identical, avoids churn).
            out.append(esc(segment[cursor : end]))
            cursor = end
            continue

        run_text = segment[start:end]
        out.append(esc(segment[cursor:start]))
        out.append(f'<bdi dir="ltr">{esc(run_text)}</bdi>')
        cursor = end

    out.append(esc(segment[cursor:]))
    return "".join(out)


def _matches_bracket(open_ch: str, close_ch: str) -> bool:
    pairs = {"(": ")", "[": "]", "{": "}"}
    return pairs.get(open_ch) == close_ch


def bidi_isolate(markup: str, escape: bool = True) -> str:
    """Tag-aware bidirectional isolation for a text or HTML fragment.

    With ``escape=True`` the value is treated as plain text: no markup is
    recognized (anything that looks like a tag is escaped) and Latin/digit runs
    are wrapped in ``<bdi dir="ltr">``.

    With ``escape=False`` the value is treated as trusted author HTML: real
    markup tags pass through untouched and only their text nodes are processed.
    """
    if not markup:
        return markup
    if escape:
        # Plain-text contract: process the whole string as a single segment,
        # escaping every reserved character (no tag passthrough).
        if not any(_class_of(ch) in ("L", "D") for ch in markup):
            return _html.escape(markup, quote=False)
        return _isolate_segment(markup, escape=True)
    # Trusted-markup contract: split on tags/entities, isolate text nodes only.
    rendered: list[str] = []
    cursor = 0
    for match in _MARKUP_TOKEN_RE.finditer(markup):
        rendered.append(_isolate_segment(markup[cursor : match.start()], escape=False))
        rendered.append(match.group(0))
        cursor = match.end()
    rendered.append(_isolate_segment(markup[cursor:], escape=False))
    return "".join(rendered)


def fmt(value: Any) -> str:
    """Escape + isolate a plain text value in one call."""
    return bidi_isolate(str(value), escape=True)
