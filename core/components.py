"""
core/components.py — Generic Semantic Component Renderers
Pure domain-agnostic components mapping generic data models to presentation markup.
"""
from __future__ import annotations

import html
import re
from collections.abc import Mapping
from typing import Any

from core.design import DesignSystem


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def label_parts(value: Any) -> tuple[str, str]:
    if isinstance(value, Mapping):
        return str(value.get("text", "")), str(value.get("subtext", ""))
    if isinstance(value, (list, tuple)):
        return (str(value[0]) if value else "", str(value[1]) if len(value) > 1 else "")
    return str(value), ""


def clean_html(value: Any, mode: str = "auto") -> str:
    content = str(value or "")
    # Generic cleanup of any pagination sentinels
    content = re.sub(r'PGB[SA][a-zA-Z0-9]+', '', content)
    if mode == "html":
        return content
    if mode == "text":
        return esc(content)
    if "<" in content and ">" in content:
        return content
    return esc(content)


def render_heading(block: Mapping[str, Any], design: DesignSystem) -> str:
    level = min(6, max(1, int(block.get("level", 2))))
    badge_val = clean_html(str(block.get("badge", "")).strip())
    badge_html = ""
    if badge_val:
        is_appendix = (
            block.get("badge_variant") == "accent"
            or badge_val in ["أ", "ب", "ج", "د", "A", "B", "C", "D"]
        )
        badge_cls = "circle-badge appendix-badge" if is_appendix else "circle-badge"
        badge_html = f'<span class="{badge_cls}">{esc(badge_val)}</span>'

    subtitle_html = (
        f'<span class="sub-label">{clean_html(block["subtitle"])}</span>'
        if "subtitle" in block
        else ""
    )
    title = clean_html(block["title"])
    return (
        f'<div class="block-heading level-{level}">{badge_html}'
        f'<div class="heading-content"><h{level}>{title}</h{level}>{subtitle_html}</div></div>'
    )


def render_subsection(block: Mapping[str, Any], design: DesignSystem) -> str:
    subtitle = (
        f'<span class="sub-title-secondary">— {clean_html(block["subtitle"])}</span>'
        if "subtitle" in block
        else ""
    )
    return (
        f'<div class="subsection-header"><h4 class="sub-title-primary">'
        f'{clean_html(block["title"])}</h4>{subtitle}</div>'
    )


def render_formula(block: Mapping[str, Any], design: DesignSystem) -> str:
    icon_char = esc(block.get("icon", "∑"))
    title_text = clean_html(block.get("title", ""))
    badge_html = (
        f'<div class="formula-badge"><span class="formula-icon-circle">{icon_char}</span>'
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
    return (
        f'<aside class="formula-container">{badge_html}'
        f'<div class="formula-math" dir="ltr">{clean_html(expression)}</div>'
        f'{description}</aside>'
    )


def render_text(block: Mapping[str, Any], design: DesignSystem) -> str:
    role = esc(block.get("role", "body"))
    align = esc(block.get("align", "justify"))
    content = clean_html(block.get("content", block.get("text", "")), block.get("format", "auto"))
    return f'<div class="block-text role-{role} align-{align}">{content}</div>'


def render_badge(block: Mapping[str, Any], design: DesignSystem) -> str:
    variant = esc(block.get("variant", "default"))
    align = esc(block.get("align", "center"))
    return (
        f'<div class="badge-wrapper align-{align}">'
        f'<span class="badge badge-{variant}">{clean_html(block["text"])}</span></div>'
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
    icon_html = f'<span class="callout-icon-circle">{esc(icon_char)}</span>' if icon_char else ""
    content = clean_html(block.get("content", ""), block.get("format", "auto"))
    return (
        f'<aside class="callout callout-{variant}">'
        f'<div class="callout-header">{icon_html}<strong>{clean_html(block["title"])}</strong></div>'
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

    rows = []
    for row in block.get("rows", []):
        cells = []
        for cell in row:
            if isinstance(cell, Mapping):
                value = cell.get("text", "")
                secondary = cell.get("subtext")
                cls = "num" if cell.get("numeric") else "txt"
                sub = f'<span class="td-sub">{clean_html(secondary)}</span>' if secondary is not None else ""
            else:
                value, cls, sub = cell, "txt", ""
            cells.append(f'<td class="{cls}">{clean_html(value)}{sub}</td>')
        rows.append(f"<tr>{''.join(cells)}</tr>")

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
        badge_val = esc(step.get("badge", index + 1))
        parts.append(
            f'<div class="step-node"><span class="step-num">{badge_val}</span>'
            f'<div class="step-content"><p class="step-title">{clean_html(title)}</p>{sub}</div></div>'
        )
        if index < len(steps) - 1:
            parts.append('<div class="step-arrow">▼</div>')
    title = f'<div class="flow-title">{clean_html(block["title"])}</div>' if "title" in block else ""
    return f'<section class="flow-steps">{title}{"".join(parts)}</section>'


def render_toc(block: Mapping[str, Any], design: DesignSystem) -> str:
    items = []
    for item in block.get("items", []):
        title, fallback_subtitle = label_parts(item.get("title", ""))
        subtitle = item.get("subtitle", fallback_subtitle)
        sub = f'<span class="toc-sub">{clean_html(subtitle)}</span>' if subtitle else ""
        badge_val = str(item.get("badge", "")).strip()
        is_appendix = item.get("appendix", False) or badge_val in [
            "أ", "ب", "ج", "د", "A", "B", "C", "D"
        ]
        badge_cls = " appendix-badge" if is_appendix else ""
        # Correct RTL order: Badge on the right, title next to it, dots in middle, page on left
        items.append(
            f'<li class="toc-row">'
            f'<span class="toc-badge{badge_cls}">{esc(badge_val)}</span>'
            f'<span class="toc-title"><strong>{clean_html(title)}</strong>{sub}</span>'
            f'<span class="toc-dots"></span>'
            f'<span class="toc-page">{esc(item.get("page", ""))}</span>'
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
    return (
        f'<blockquote class="quote"><span class="quote-rule"></span>'
        f'<p>{clean_html(block["text"])}</p>{subtext}{author}'
        f'<span class="quote-rule"></span></blockquote>'
    )


def render_list(block: Mapping[str, Any], design: DesignSystem) -> str:
    tag = "ol" if block.get("ordered") else "ul"
    variant = esc(block.get("variant", "default"))
    mode = block.get("format", "auto")
    items = []
    for index, item in enumerate(block.get("items", []), start=1):
        if isinstance(item, Mapping):
            badge = item.get("badge", str(index) if block.get("ordered") else "")
            title = clean_html(item.get("title", item.get("text", "")), mode)
            subtitle = clean_html(item.get("subtitle", ""))
            tag_txt = clean_html(item.get("tag", ""))
            badge_html = f'<span class="list-item-badge">{esc(badge)}</span>' if badge else ""
            tag_html = f'<span class="list-item-tag">{tag_txt}</span>' if tag_txt else ""
            sub_html = f'<span class="list-item-sub">{subtitle}</span>' if subtitle else ""
            items.append(
                f'<li class="list-item-card">{badge_html}<div class="list-item-content">'
                f'<div class="list-item-title">{title}</div>{sub_html}{tag_html}</div></li>'
            )
        else:
            items.append(f"<li>{clean_html(item, mode)}</li>")
    return f'<{tag} class="content-list list-{variant}">{"".join(items)}</{tag}>'


def render_spacer(block: Mapping[str, Any], design: DesignSystem) -> str:
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
}


def render_block(block: Mapping[str, Any], design: DesignSystem) -> str:
    kind = block.get("type")
    if kind == "artifact_ref":
        raise ValueError("artifact_ref must be resolved by the compiler")
    renderer = RENDERERS.get(kind)
    if renderer is None:
        raise ValueError(f"Unsupported component type: {kind}")
    return renderer(block, design)