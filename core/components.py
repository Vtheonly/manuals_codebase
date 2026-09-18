"""Generic semantic component renderers.

Components know visual semantics only. They never know the document domain.
"""
from __future__ import annotations

import html
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


def render_content(value: Any, mode: str = "text") -> str:
    content = str(value or "")
    return content if mode == "html" else esc(content)


def render_heading(block: Mapping[str, Any], design: DesignSystem) -> str:
    level = min(6, max(1, int(block.get("level", 2))))
    badge = f'<span class="circle-badge">{esc(block["badge"])}</span>' if "badge" in block else ""
    subtitle = f'<span class="sub-label">{esc(block["subtitle"])}</span>' if "subtitle" in block else ""
    return f'<div class="block-heading level-{level}">{badge}<div><h{level}>{esc(block["title"])}</h{level}>{subtitle}</div></div>'


def render_text(block: Mapping[str, Any], design: DesignSystem) -> str:
    role = esc(block.get("role", "body"))
    align = esc(block.get("align", "justify"))
    content = render_content(block.get("content", ""), block.get("format", "text"))
    return f'<div class="block-text role-{role} align-{align}">{content}</div>'


def render_badge(block: Mapping[str, Any], design: DesignSystem) -> str:
    variant = esc(block.get("variant", "default"))
    align = esc(block.get("align", "center"))
    return f'<div class="badge-wrapper align-{align}"><span class="badge badge-{variant}">{esc(block["text"])}</span></div>'


def render_card(block: Mapping[str, Any], design: DesignSystem) -> str:
    label = f'<div class="card-label">{esc(block["label"])}</div>' if "label" in block else ""
    subtitle = f'<div class="card-subtitle">{esc(block["subtitle"])}</div>' if "subtitle" in block else ""
    pill = f'<div class="card-pill">{esc(block["pill"])}</div>' if "pill" in block else ""
    content = f'<div class="card-content">{render_content(block["content"], block.get("format", "text"))}</div>' if "content" in block else ""
    return f'<section class="card">{label}<h2 class="card-title">{esc(block["title"])}</h2>{subtitle}{content}{pill}</section>'


def render_info_card(block: Mapping[str, Any], design: DesignSystem) -> str:
    rows = []
    for row in block.get("rows", []):
        if not isinstance(row, Mapping):
            raise ValueError("info_card rows must be objects")
        highlight = " highlight" if row.get("highlight") else ""
        rows.append(
            f'<div class="info-row{highlight}"><span class="info-label">{esc(row.get("label", ""))}</span>'
            f'<span class="info-sep">:</span><span class="info-value">{esc(row.get("value", ""))}</span></div>'
        )
    return f'<section class="info-card">{"".join(rows)}</section>'


def render_callout(block: Mapping[str, Any], design: DesignSystem) -> str:
    variant = esc(block.get("variant", "accent"))
    icon = f'<span class="callout-icon">{esc(block["icon"])}</span>' if "icon" in block else ""
    content = render_content(block.get("content", ""), block.get("format", "html"))
    return f'<aside class="callout callout-{variant}"><div class="callout-header">{icon}<strong>{esc(block["title"])}</strong></div><div class="callout-content">{content}</div></aside>'


def render_stats(block: Mapping[str, Any], design: DesignSystem) -> str:
    cards = []
    for item in block.get("items", []):
        if not isinstance(item, Mapping):
            raise ValueError("stats items must be objects")
        sub = f'<span class="stat-sub">{esc(item["sublabel"])}</span>' if "sublabel" in item else ""
        cards.append(f'<div class="stat-card"><div class="stat-value">{esc(item.get("value", ""))}</div><div class="stat-label">{esc(item.get("label", ""))}</div>{sub}</div>')
    columns = max(1, min(6, int(block.get("columns", len(cards) or 1))))
    return f'<div class="stats-grid cols-{columns}">{"".join(cards)}</div>'


def render_table(block: Mapping[str, Any], design: DesignSystem) -> str:
    headers = []
    for column in block["columns"]:
        primary, secondary = label_parts(column)
        sub = f'<span class="th-sub">{esc(secondary)}</span>' if secondary else ""
        headers.append(f"<th>{esc(primary)}{sub}</th>")

    rows = []
    for row in block.get("rows", []):
        cells = []
        for cell in row:
            if isinstance(cell, Mapping):
                value = cell.get("text", "")
                secondary = cell.get("subtext")
                cls = "num" if cell.get("numeric") else "txt"
                sub = f'<span class="td-sub">{esc(secondary)}</span>' if secondary is not None else ""
            else:
                value, cls, sub = cell, "txt", ""
            cells.append(f'<td class="{cls}">{esc(value)}{sub}</td>')
        rows.append(f"<tr>{''.join(cells)}</tr>")

    title = f'<div class="table-header"><h4>{esc(block["title"])}</h4><span>{esc(block.get("subtitle", ""))}</span></div>' if "title" in block else ""
    caption = f'<div class="caption">{esc(block["caption"])}</div>' if "caption" in block else ""
    return f'<section class="table-wrapper">{title}<table class="standard-table"><thead><tr>{"".join(headers)}</tr></thead><tbody>{"".join(rows)}</tbody></table>{caption}</section>'


def render_flow_steps(block: Mapping[str, Any], design: DesignSystem) -> str:
    parts = []
    steps = block.get("steps", [])
    for index, step in enumerate(steps):
        if not isinstance(step, Mapping):
            raise ValueError("flow_steps entries must be objects")
        title, fallback_subtitle = label_parts(step.get("title", step.get("label", "")))
        subtitle = step.get("subtitle", fallback_subtitle)
        sub = f'<p class="step-sub">{esc(subtitle)}</p>' if subtitle else ""
        parts.append(f'<div class="step-node"><span class="step-num">{esc(step.get("badge", index + 1))}</span><div><p class="step-title">{esc(title)}</p>{sub}</div></div>')
        if index < len(steps) - 1:
            parts.append('<div class="step-arrow">▼</div>')
    title = f'<div class="flow-title">{esc(block["title"])}</div>' if "title" in block else ""
    return f'<section class="flow-steps">{title}{"".join(parts)}</section>'


def render_toc(block: Mapping[str, Any], design: DesignSystem) -> str:
    items = []
    for item in block.get("items", []):
        title, fallback_subtitle = label_parts(item.get("title", ""))
        subtitle = item.get("subtitle", fallback_subtitle)
        sub = f'<span class="toc-sub">{esc(subtitle)}</span>' if subtitle else ""
        items.append(f'<li class="toc-row"><span class="toc-badge">{esc(item.get("badge", ""))}</span><span class="toc-title"><strong>{esc(title)}</strong>{sub}</span><span class="toc-dots"></span><span class="toc-page">{esc(item.get("page", ""))}</span></li>')
    return f'<section class="toc"><h2>{esc(block["title"])}</h2><p class="toc-subtitle">{esc(block.get("subtitle", ""))}</p><ul>{"".join(items)}</ul></section>'


def render_quote(block: Mapping[str, Any], design: DesignSystem) -> str:
    author = f'<span class="quote-author">— {esc(block["author"])}</span>' if "author" in block else ""
    return f'<blockquote class="quote"><span class="quote-rule"></span><p>{esc(block["text"])}</p>{author}</blockquote>'


def render_list(block: Mapping[str, Any], design: DesignSystem) -> str:
    tag = "ol" if block.get("ordered") else "ul"
    mode = block.get("format", "text")
    items = "".join(f"<li>{render_content(item, mode)}</li>" for item in block.get("items", []))
    return f'<{tag} class="content-list">{items}</{tag}>'


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
    return f'<div class="content-group group-{layout} align-{align} justify-{justify} gap-{gap}">{"".join(rendered_children)}</div>'


def render_image(block: Mapping[str, Any], design: DesignSystem) -> str:
    src, alt = esc(block["src"]), esc(block.get("alt", ""))
    width = esc(block.get("width", "100%"))
    caption = f'<figcaption>{esc(block["caption"])}</figcaption>' if "caption" in block else ""
    return f'<figure class="image-block"><img src="{src}" alt="{alt}" style="max-width:{width};">{caption}</figure>'


RENDERERS = {
    "heading": render_heading,
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
