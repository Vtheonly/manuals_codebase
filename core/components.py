"""
core/components.py — Generic Semantic Component Renderers
Pure domain-agnostic components mapping generic data models to presentation markup.

Every component reads its visual values from the DesignSystem tokens so that a
JSON theme override changes all documents at once. Components accept optional
generic style hints (variant names, token color references, sizes) but never
document-specific data.

Architectural guarantees implemented here:

* **Automated BiDi isolation** — every text surface is emitted through the
  `core.text` pipeline so Latin/digit runs inside RTL prose can never be
  reordered by the Unicode Bidirectional Algorithm.
* **Decoupled accent bars** — subsection accents are independent flex elements
  separated from the text node by an enforced gap, never container borders.
* **Vector icon primitives** — UI symbols (check, star, warning, …) render as
  inline SVG paths with geometric centering instead of font glyphs.
* **Defensive template guarding** — optional accessories (TOC badges, page
  numbers, icons) are omitted entirely when absent rather than rendering empty
  placeholder shapes.
"""
from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

from core.design import DesignSystem
from core.text import bidi_isolate, fmt


def esc(value: object) -> str:
    """Escape a value for attribute/URL contexts (no BiDi processing)."""
    import html

    return html.escape(str(value), quote=True)


def label_parts(value: Any) -> tuple[str, str]:
    if isinstance(value, Mapping):
        return str(value.get("text", "")), str(value.get("subtext", ""))
    if isinstance(value, (list, tuple)):
        return (str(value[0]) if value else "", str(value[1]) if len(value) > 1 else "")
    return str(value), ""


def clean_html(value: Any, mode: str = "auto") -> str:
    """Render a text value with automated bidirectional isolation.

    mode "text"  — plain text: escaped + BiDi isolated (default for most data).
    mode "html"  — trusted author markup: tags/entities pass through, text
                   nodes are BiDi isolated.
    mode "auto"  — html when the value already contains markup, else text.
    """
    content = str(value or "")
    # Generic cleanup of any pagination sentinels
    content = re.sub(r"PGB[SA][a-zA-Z0-9]+", "", content)
    if mode == "text":
        return bidi_isolate(content, escape=True)
    if mode == "html":
        return bidi_isolate(content, escape=False)
    if "<" in content and ">" in content:
        return bidi_isolate(content, escape=False)
    return bidi_isolate(content, escape=True)


PALETTE_TOKENS = (
    "primary", "primary_deep", "primary_light", "accent", "accent_text", "accent_light",
    "banner_start", "banner_end", "banner_border", "banner_text", "text_dark", "text",
    "muted", "muted_light", "surface", "surface_alt", "surface_warm", "border",
    "border_light", "border_table", "border_table_strong", "dots", "divider_strong",
    "frame_inner", "back_cover", "back_frame", "chart_axis", "chart_track",
    "chart_track_border", "gold",
)


def resolve_color(value: Any, design: DesignSystem, default: str | None = None) -> str | None:
    """Resolve a color hint: a palette token name, a 'series.N' reference, or a literal."""
    if value is None:
        return default
    p = design.palette
    name = str(value).strip()
    if name == "gold":
        return p.accent
    if hasattr(p, name) and name in PALETTE_TOKENS:
        return getattr(p, name)
    if name.startswith("series."):
        try:
            index = int(name.split(".", 1)[1])
            return p.series[index % len(p.series)]
        except (ValueError, IndexError):
            pass
    return name


# ---------------------------------------------------------------------------
# Vector icon primitives — geometrically centered UI symbols (SVG paths)
# ---------------------------------------------------------------------------

# name -> (inner markup, stroke-based?) rendered inside a 24x24 viewBox.
ICON_PATHS: dict[str, tuple[str, bool]] = {
    "check": ('<path d="M20 6 9 17l-5-5"/>', True),
    "star": ('<path d="M12 2.5l2.95 6.3 6.55.62-4.95 4.35 1.45 6.43L12 16.9l-6 3.3 1.45-6.43L2.5 9.42l6.55-.62z"/>', False),
    "warning": ('<path d="M12 3.5 21.5 20H2.5z"/><path d="M12 10v4.2"/><circle cx="12" cy="17.1" r="0.4"/>', True),
    "info": ('<circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><circle cx="12" cy="8" r="0.5"/>', True),
    "sigma": ('<path d="M18 6H8.5l5.5 6-5.5 6H18"/>', True),
    "target": ('<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2.2"/>', True),
    "flag": ('<path d="M6 21V4"/><path d="M6 4h11l-2.5 3.5L17 11H6"/>', True),
    "bulb": ('<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.8.6 1.2 1.3 1.4 2.1h4.2c.2-.8.6-1.5 1.4-2.1A6 6 0 0 0 12 3z"/>', True),
    "book": ('<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M20 19H6.5A2.5 2.5 0 0 0 4 21.5"/>', True),
    "arrow_down": ('<path d="M12 4v13"/><path d="m6.5 12.5 5.5 5.5 5.5-5.5"/>', True),
}

# Legacy glyph characters accepted in JSON `icon` fields, mapped to vector icons.
ICON_GLYPH_ALIASES = {
    "✓": "check", "✔": "check", "√": "check",
    "★": "star", "☆": "star",
    "⚠": "warning", "⚠️": "warning", "!": "warning",
    "ⓘ": "info", "ℹ": "info", "i": "info",
    "∑": "sigma", "Σ": "sigma",
    "◎": "target", "◉": "target", "⊙": "target",
    "⚑": "flag", "⚐": "flag",
    "▼": "arrow_down", "▽": "arrow_down",
}


def render_icon(name: str, size_pt: float = 9.5) -> str:
    """Render a UI symbol as an inline, geometrically centered SVG icon."""
    key = str(name).strip()
    key = ICON_GLYPH_ALIASES.get(key, key)
    entry = ICON_PATHS.get(key)
    if entry is None:
        return ""
    inner, stroke_based = entry
    if stroke_based:
        body = (
            f'{inner}'
        )
        return (
            f'<svg class="ui-icon" viewBox="0 0 24 24" width="{size_pt}pt" height="{size_pt}pt" '
            f'fill="none" stroke="currentColor" stroke-width="2.4" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'
        )
    return (
        f'<svg class="ui-icon" viewBox="0 0 24 24" width="{size_pt}pt" height="{size_pt}pt" '
        f'fill="currentColor" aria-hidden="true">{inner}</svg>'
    )


def icon_or_text(value: Any, size_pt: float = 9.5) -> str:
    """Vector icon when a known symbol is requested, escaped text otherwise."""
    raw = str(value or "").strip()
    svg = render_icon(raw, size_pt)
    if svg:
        return svg
    return fmt(raw) if raw else ""


# Block types that introduce a section and must never be stranded at the very
# bottom of a page without at least one following block (used by the paginator).
KEEP_WITH_NEXT_TYPES = frozenset({"heading", "subsection"})


# ---------------------------------------------------------------------------
# Component renderers
# ---------------------------------------------------------------------------

def render_divider(block: Mapping[str, Any], design: DesignSystem) -> str:
    """Generic decorative rule component.

    Variants: solid | dotted | double | gradient | section
    Options: color (token/hex), thickness, width (full|content|<len>), margin (sm|md|lg)
    """
    variant = esc(block.get("variant", "solid"))
    color = resolve_color(block.get("color"), design, design.palette.primary)
    thickness = esc(block.get("thickness", "thick"))
    width = esc(block.get("width", "full"))
    margin = esc(block.get("margin", "md"))
    extra_style = ""
    if variant == "gradient":
        base = resolve_color(block.get("start"), design, color) or color
        end = resolve_color(block.get("end"), design, design.palette.accent)
        extra_style = (
            f"background: linear-gradient(90deg, {base}, {end});"
            if design and base and end
            else ""
        )
    return (
        f'<hr class="divider divider-{variant} thickness-{thickness} width-{width} '
        f'margin-{margin}" style="{extra_style}" aria-hidden="true">'
    )


def render_heading(block: Mapping[str, Any], design: DesignSystem) -> str:
    level = min(6, max(1, int(block.get("level", 2))))
    badge_val = str(block.get("badge", "")).strip()
    badge_html = ""
    if badge_val:
        is_appendix = block.get("badge_variant") == "accent"
        badge_cls = "circle-badge appendix-badge" if is_appendix else "circle-badge"
        badge_html = f'<span class="{badge_cls}">{fmt(badge_val)}</span>'

    subtitle_html = (
        f'<span class="sub-label">{clean_html(block["subtitle"])}</span>'
        if "subtitle" in block
        else ""
    )
    rule = block.get("rule", True)
    rule_html = ""
    if rule:
        if isinstance(rule, Mapping):
            rule_block = {"type": "divider", **rule}
        else:
            rule_block = {"type": "divider", "variant": "section"}
        rule_html = render_divider(rule_block, design)
    title = clean_html(block["title"])
    # Heading + rule are wrapped in a single container so one block always
    # maps to exactly one layout child (atomic for pagination measurement).
    return (
        f'<div class="heading-block"><div class="block-heading level-{level}">{badge_html}'
        f'<div class="heading-content"><h{level}>{title}</h{level}>{subtitle_html}</div></div>'
        f'{rule_html}</div>'
    )


def render_subsection(block: Mapping[str, Any], design: DesignSystem) -> str:
    """Subsection header with a decoupled accent bar.

    The accent bar is an independent flex element separated from the text by
    the header's `gap`, so text ink and the bar can never share coordinate
    space regardless of the script's sidebearings.
    """
    subtitle = (
        f'<span class="sub-title-secondary">{clean_html(block["subtitle"])}</span>'
        if "subtitle" in block
        else ""
    )
    accent = esc(block.get("accent", "bar"))
    accent_color = resolve_color(block.get("accent_color"), design, design.palette.accent)
    style = f' style="--subsection-accent:{accent_color}"' if accent_color else ""
    bar = '<span class="subsection-bar" aria-hidden="true"></span>' if accent == "bar" else ""
    # The dash lives inside the RTL title element so it stays adjacent to the
    # Arabic text regardless of document direction.
    dash = '<span class="sub-dash">—</span>' if subtitle else ""
    return (
        f'<div class="subsection-header sub-accent-{accent}"{style}>{bar}'
        f'<h4 class="sub-title-primary">'
        f'{clean_html(block["title"])}{dash}</h4>{subtitle}</div>'
    )


def render_formula(block: Mapping[str, Any], design: DesignSystem) -> str:
    icon_char = str(block.get("icon", "∑") or "")
    icon_html = icon_or_text(icon_char, size_pt=10)
    icon_span = f'<span class="formula-icon-circle">{icon_html}</span>' if icon_html else ""
    title_text = clean_html(block.get("title", ""))
    badge_html = (
        f'<div class="formula-badge">{icon_span}'
        f'<strong>{title_text}</strong></div>'
        if title_text
        else ""
    )
    description = (
        f'<div class="formula-desc">{clean_html(block["description"])}</div>'
        if "description" in block
        else ""
    )
    expression = block.get("html_expression", block.get("expression", ""))
    # The math body is a dedicated, isolated LTR block: operators, sub/superscripts
    # and variable names can never be influenced by ambient RTL flow.
    math_html = (
        f'<div class="formula-math" dir="ltr" isolation="isolate">{bidi_isolate(str(expression), escape=False)}</div>'
    )
    return (
        f'<aside class="formula-container">{badge_html}'
        f'{math_html}'
        f'{description}</aside>'
    )


def render_text(block: Mapping[str, Any], design: DesignSystem) -> str:
    role = esc(block.get("role", "body"))
    align = esc(block.get("align", "justify"))
    lead = esc(block.get("lead", "loose"))
    content = clean_html(block.get("content", block.get("text", "")), block.get("format", "auto"))
    return f'<div class="block-text role-{role} align-{align} lead-{lead}">{content}</div>'


def render_badge(block: Mapping[str, Any], design: DesignSystem) -> str:
    variant = esc(block.get("variant", "default"))
    align = esc(block.get("align", "center"))
    size = esc(block.get("size", "md"))
    return (
        f'<div class="badge-wrapper align-{align}">'
        f'<span class="badge badge-{variant} size-{size}">{clean_html(block["text"])}</span></div>'
    )


def render_card(block: Mapping[str, Any], design: DesignSystem) -> str:
    label = f'<div class="card-label">{clean_html(block["label"])}</div>' if "label" in block else ""
    subtitle = (
        f'<div class="card-subtitle">{clean_html(block["subtitle"])}</div>'
        if "subtitle" in block
        else ""
    )
    pill = f'<div class="card-pill">{clean_html(block["pill"])}</div>' if "pill" in block else ""
    content = (
        f'<div class="card-content">{clean_html(block["content"])}</div>'
        if "content" in block
        else ""
    )
    return (
        f'<section class="card">{label}'
        f'<h2 class="card-title">{clean_html(block["title"])}</h2>'
        f'{subtitle}{content}{pill}</section>'
    )


def render_info_card(block: Mapping[str, Any], design: DesignSystem) -> str:
    """Key/value metadata card with intrinsically sized label column.

    The label column uses ``width: 1%; white-space: nowrap`` shrink-to-fit
    sizing so labels of any length stay on one line and never split across
    cells; the value column absorbs the remaining width.
    """
    rows = []
    for row in block.get("rows", []):
        if not isinstance(row, Mapping):
            raise ValueError("info_card rows must be objects")
        highlight = " highlight" if row.get("highlight") else ""
        label = clean_html(row.get("label", ""))
        val = clean_html(row.get("value", ""))
        sep = esc(row.get("separator", ":"))
        rows.append(
            f'<tr class="info-row{highlight}">'
            f'<td class="info-label">{label}</td>'
            f'<td class="info-sep">{sep}</td>'
            f'<td class="info-value">{val}</td>'
            f'</tr>'
        )
    return f'<section class="info-card"><table class="info-table">{"".join(rows)}</table></section>'


def render_callout(block: Mapping[str, Any], design: DesignSystem) -> str:
    variant = esc(block.get("variant", "accent"))
    icon_char = block.get("icon")
    icon_html = icon_or_text(icon_char, size_pt=9) if icon_char else ""
    icon_span = f'<span class="callout-icon-circle">{icon_html}</span>' if icon_html else ""
    content = clean_html(block.get("content", ""), block.get("format", "auto"))
    return (
        f'<aside class="callout callout-{variant}">'
        f'<div class="callout-header">{icon_span}<strong>{clean_html(block["title"])}</strong></div>'
        f'<div class="callout-content">{content}</div>'
        f'</aside>'
    )


def render_stats(block: Mapping[str, Any], design: DesignSystem) -> str:
    cards = []
    for item in block.get("items", []):
        if not isinstance(item, Mapping):
            raise ValueError("stats items must be objects")
        sub = f'<span class="stat-sub">{clean_html(item["sublabel"])}</span>' if "sublabel" in item else ""
        cards.append(
            f'<div class="stat-card">'
            f'<div class="stat-value">{clean_html(item.get("value", ""))}</div>'
            f'<div class="stat-label">{clean_html(item.get("label", ""))}</div>'
            f'{sub}</div>'
        )
    columns = max(1, min(6, int(block.get("columns", len(cards) or 1))))
    return f'<div class="stats-grid cols-{columns}">{"".join(cards)}</div>'


def render_table(block: Mapping[str, Any], design: DesignSystem) -> str:
    headers = []
    for column in block["columns"]:
        primary, secondary = label_parts(column)
        sub = f'<span class="th-sub">{clean_html(secondary)}</span>' if secondary else ""
        headers.append(f"<th>{clean_html(primary)}{sub}</th>")

    # Zebra parity survives table splits across pages: the continuation
    # carries ``_zebra_offset`` so striping continues seamlessly.
    zebra_offset = int(block.get("_zebra_offset", 0) or 0)
    rows = []
    for row_index, row in enumerate(block.get("rows", []), start=1):
        cells = []
        for cell in row:
            if isinstance(cell, Mapping):
                value = cell.get("text", "")
                secondary = cell.get("subtext")
                cls = "num" if cell.get("numeric") else "txt"
                sub = f'<span class="td-sub">{clean_html(secondary)}</span>' if secondary is not None else ""
                if cell.get("strong"):
                    cls += " strong"
            else:
                value, cls, sub = cell, "txt", ""
            cells.append(f'<td class="{cls}">{clean_html(value)}{sub}</td>')
        parity = row_index + zebra_offset
        row_class = ' class="alt"' if parity % 2 == 0 else ""
        rows.append(f"<tr{row_class}>{''.join(cells)}</tr>")

    caption_html = ""
    if "caption" in block:
        c_main, c_sub = label_parts(block["caption"])
        sub_part = f'<div class="caption-sub">{clean_html(c_sub)}</div>' if c_sub else ""
        caption_html = f'<div class="caption"><div class="caption-main">{clean_html(c_main)}</div>{sub_part}</div>'

    title = (
        f'<div class="table-header"><h4>{clean_html(block["title"])}</h4>'
        f'<span>— {clean_html(block.get("subtitle", ""))}</span></div>'
        if "title" in block
        else ""
    )
    return (
        f'<section class="table-wrapper">{title}'
        f'<table class="standard-table"><thead><tr>{"".join(headers)}</tr></thead>'
        f'<tbody>{"".join(rows)}</tbody></table>{caption_html}</section>'
    )


def render_flow_steps(block: Mapping[str, Any], design: DesignSystem) -> str:
    parts = []
    steps = block.get("steps", [])
    for index, step in enumerate(steps):
        if not isinstance(step, Mapping):
            raise ValueError("flow_steps entries must be objects")
        title, fallback_subtitle = label_parts(step.get("title", step.get("label", "")))
        subtitle = step.get("subtitle", fallback_subtitle)
        sub = f'<p class="step-sub">{clean_html(subtitle)}</p>' if subtitle else ""
        badge_val = str(step.get("badge", index + 1))
        parts.append(
            f'<div class="step-node"><span class="step-num">{fmt(badge_val)}</span>'
            f'<div class="step-content"><p class="step-title">{clean_html(title)}</p>{sub}</div></div>'
        )
        if index < len(steps) - 1:
            parts.append(f'<div class="step-arrow">{render_icon("arrow_down", 8)}</div>')
    title = f'<div class="flow-title">{clean_html(block["title"])}</div>' if "title" in block else ""
    return f'<section class="flow-steps">{title}{"".join(parts)}</section>'


def render_toc(block: Mapping[str, Any], design: DesignSystem) -> str:
    """Table of contents with canonical logical DOM ordering.

    DOM order always matches logical reading order:
    leading accessory (badge) -> primary title -> flexible spacer (dots) ->
    trailing accessory (page number). Missing accessories are omitted
    entirely instead of rendering empty placeholder shapes.
    """
    items = []
    for item in block.get("items", []):
        title, fallback_subtitle = label_parts(item.get("title", ""))
        subtitle = item.get("subtitle", fallback_subtitle)
        sub = f'<span class="toc-sub">{clean_html(subtitle)}</span>' if subtitle else ""
        badge_val = str(item.get("badge", "")).strip()
        page_val = str(item.get("page", "")).strip()
        is_appendix = item.get("appendix", False) or item.get("badge_variant") == "accent"
        badge_cls = " appendix-badge" if is_appendix else ""
        badge_html = (
            f'<span class="toc-badge{badge_cls}">{fmt(badge_val)}</span>' if badge_val else ""
        )
        page_html = (
            f'<span class="toc-page" dir="ltr">{fmt(page_val)}</span>' if page_val else ""
        )
        items.append(
            f'<li class="toc-row">'
            f'{badge_html}'
            f'<span class="toc-title"><strong>{clean_html(title)}</strong>{sub}</span>'
            f'<span class="toc-dots" aria-hidden="true"></span>'
            f'{page_html}'
            f'</li>'
        )
    subtitle_html = (
        f'<p class="toc-subtitle">{clean_html(block["subtitle"])}</p>'
        if "subtitle" in block
        else ""
    )
    return (
        f'<section class="toc"><h2>{clean_html(block["title"])}</h2>{subtitle_html}'
        f'<div class="toc-divider-line"></div>'
        f'<ul>{"".join(items)}</ul></section>'
    )


def render_quote(block: Mapping[str, Any], design: DesignSystem) -> str:
    subtext = f'<p class="quote-sub">{clean_html(block["subtext"])}</p>' if "subtext" in block else ""
    author = f'<span class="quote-author">— {clean_html(block["author"])}</span>' if "author" in block else ""
    box_cls = " quote-box" if block.get("box", True) else ""
    return (
        f'<blockquote class="quote{box_cls}"><span class="quote-rule"></span>'
        f'<p>{clean_html(block["text"])}</p>{subtext}{author}'
        f'<span class="quote-rule"></span></blockquote>'
    )


def render_list(block: Mapping[str, Any], design: DesignSystem) -> str:
    variant = esc(block.get("variant", "cards"))
    ordered = bool(block.get("ordered"))
    tag = "ol" if ordered else "ul"
    mode = block.get("format", "auto")
    items = []
    for index, item in enumerate(block.get("items", []), start=1):
        if isinstance(item, Mapping):
            badge = item.get("badge", str(index) if ordered else "")
            title = clean_html(item.get("title", item.get("text", "")), mode)
            subtitle = clean_html(item.get("subtitle", ""))
            tag_txt = clean_html(item.get("tag", ""))
            badge_html = f'<span class="list-item-badge">{fmt(badge)}</span>' if str(badge).strip() else ""
            tag_html = f'<span class="list-item-tag">{tag_txt}</span>' if tag_txt else ""
            sub_html = f'<span class="list-item-sub">{subtitle}</span>' if subtitle else ""
            if variant == "rows":
                items.append(
                    f'<li class="list-row">{badge_html}<div class="list-row-content">'
                    f'<div class="list-item-title">{title}</div>{sub_html}{tag_html}</div></li>'
                )
            else:
                items.append(
                    f'<li class="list-item-card">{badge_html}<div class="list-item-content">'
                    f'<div class="list-item-title">{title}</div>{sub_html}{tag_html}</div></li>'
                )
        else:
            if variant == "rows":
                items.append(
                    f'<li class="list-row"><span class="list-item-badge">{index}</span>'
                    f'<div class="list-row-content"><div class="list-item-title">'
                    f'{clean_html(item, mode)}</div></div></li>'
                )
            else:
                items.append(f"<li>{clean_html(item, mode)}</li>")
    return f'<{tag} class="content-list list-{variant}">{"".join(items)}</{tag}>'


def render_spacer(block: Mapping[str, Any], design: DesignSystem) -> str:
    height = block.get("height")
    if height:
        return f'<div class="spacer spacer-custom" style="height:{esc(height)}" aria-hidden="true"></div>'
    return f'<div class="spacer spacer-{esc(block.get("size", "md"))}" aria-hidden="true"></div>'


def render_group(block: Mapping[str, Any], design: DesignSystem) -> str:
    rendered_children = block.get("_rendered_children")
    if rendered_children is None:
        rendered_children = [render_block(child, design) for child in block.get("children", [])]
    layout = "row" if block.get("layout") == "row" else "column"
    align = esc(block.get("align", "stretch"))
    justify = esc(block.get("justify", "flex-start"))
    gap = esc(block.get("gap", "md"))
    return (
        f'<div class="content-group group-{layout} align-{align} justify-{justify} gap-{gap}">'
        f'{"".join(rendered_children)}</div>'
    )


def render_image(block: Mapping[str, Any], design: DesignSystem) -> str:
    src, alt = esc(block["src"]), esc(block.get("alt", ""))
    width = esc(block.get("width", "100%"))
    caption = f'<figcaption>{clean_html(block["caption"])}</figcaption>' if "caption" in block else ""
    return f'<figure class="image-block"><img src="{src}" alt="{alt}" style="max-width:{width};">{caption}</figure>'


RENDERERS = {
    "heading": render_heading,
    "subsection": render_subsection,
    "formula": render_formula,
    "text": render_text,
    "badge": render_badge,
    "card": render_card,
    "info_card": render_info_card,
    "callout": render_callout,
    "stats": render_stats,
    "table": render_table,
    "flow_steps": render_flow_steps,
    "toc": render_toc,
    "quote": render_quote,
    "list": render_list,
    "spacer": render_spacer,
    "group": render_group,
    "image": render_image,
    "divider": render_divider,
}


def render_block(block: Mapping[str, Any], design: DesignSystem) -> str:
    kind = block.get("type")
    if kind == "artifact_ref":
        raise ValueError("artifact_ref must be resolved by the compiler")
    renderer = RENDERERS.get(kind)
    if renderer is None:
        raise ValueError(f"Unsupported component type: {kind}")
    return renderer(block, design)
