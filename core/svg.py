# ========================================================================
# FILE: core/svg.py
# ========================================================================
"""
core/svg.py — Deterministic, Domain-Agnostic Vector Graphics Engine (Pure SVG)
Generates high-fidelity vector charts and diagrams directly using DesignSystem tokens.
"""
from __future__ import annotations

import html
import math
from collections.abc import Mapping, Sequence
from typing import Any

from core.design import DesignSystem


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def label_parts(value: Any) -> tuple[str, str]:
    if isinstance(value, Mapping):
        return str(value.get("text", "")), str(value.get("subtext", ""))
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        primary = str(value[0]) if value else ""
        secondary = str(value[1]) if len(value) > 1 else ""
        return primary, secondary
    return str(value), ""


def chart_frame(spec: Mapping[str, Any], body: str, design: DesignSystem, width: int, height: int) -> str:
    title = esc(spec.get("title", ""))
    subtitle = esc(spec.get("subtitle", spec.get("subtitle_fr", "")))
    subtitle_html = f'<p class="chart-subtitle">{subtitle}</p>' if subtitle else ""
    caption_html = ""
    if "caption" in spec:
        c_main, c_sub = label_parts(spec["caption"])
        sub_part = f'<div class="caption-sub">{esc(c_sub)}</div>' if c_sub else ""
        caption_html = f'<div class="caption"><div class="caption-main">{esc(c_main)}</div>{sub_part}</div>'

    return f"""
    <section class="artifact chart-container">
      <div class="chart-header">
        <h4>{title}</h4>
        {subtitle_html}
      </div>
      <svg viewBox="0 0 {width} {height}" class="svg-viewport"
           style="direction: ltr !important; unicode-bidi: isolate;"
           xmlns="http://www.w3.org/2000/svg" role="img"
           aria-label="{title}">{body}</svg>
      {caption_html}
    </section>
    """


def bar_chart(spec: Mapping[str, Any], design: DesignSystem) -> str:
    width, height = 640, 290
    ml, mr, mt, mb = 52, 22, 28, 52
    plot_w, plot_h = width - ml - mr, height - mt - mb
    values = [float(v) for v in spec["values"]]
    labels = spec["labels"]
    maximum = max((abs(v) for v in values), default=1.0) * 1.2 or 1.0
    count = max(1, len(values))
    bar_w = max(16.0, (plot_w / count) * 0.52)
    gap = (plot_w - bar_w * count) / (count + 1)
    axis = design.palette
    text_font = design.typography.font_arabic
    unit = esc(spec.get("unit", ""))

    parts: list[str] = []
    for i in range(5):
        y = mt + plot_h * i / 4
        val = maximum * (1 - i / 4)
        parts.append(
            f'<line x1="{ml}" y1="{y:.1f}" x2="{width - mr}" y2="{y:.1f}" '
            f'stroke="{axis.border_light}" stroke-dasharray="2,2"/>'
        )
        parts.append(
            f'<text x="{ml - 8}" y="{y + 4:.1f}" font-family="{esc(text_font)}" '
            f'font-size="8" fill="{axis.muted}" text-anchor="end">{val:.0f}</text>'
        )

    colors = axis.series or (axis.primary,)
    for index, (label, value) in enumerate(zip(labels, values)):
        x = ml + gap + index * (bar_w + gap)
        magnitude = abs(value)
        bar_h = (magnitude / maximum) * plot_h
        y = mt + plot_h - bar_h
        primary_label, secondary_label = label_parts(label)
        color = colors[index % len(colors)]

        val_display = f"{unit} {value:g}" if unit else f"{value:g}"
        parts.extend(
            [
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" '
                f'rx="2" fill="{esc(color)}"/>',
                f'<text x="{x + bar_w / 2:.1f}" y="{y - 5:.1f}" '
                f'font-family="{esc(text_font)}" font-size="8.5" font-weight="700" '
                f'fill="{axis.text_dark}" text-anchor="middle">{val_display}</text>',
                f'<text x="{x + bar_w / 2:.1f}" y="{mt + plot_h + 17:.1f}" '
                f'font-family="{esc(text_font)}" font-size="8" font-weight="600" '
                f'fill="{axis.text}" text-anchor="middle">{esc(primary_label)}</text>',
            ]
        )
        if secondary_label:
            parts.append(
                f'<text x="{x + bar_w / 2:.1f}" y="{mt + plot_h + 29:.1f}" '
                f'font-family="{esc(design.typography.font_latin)}" font-size="7" '
                f'font-style="italic" fill="{axis.muted}" text-anchor="middle">{esc(secondary_label)}</text>'
            )

    return chart_frame(spec, "".join(parts), design, width, height)


def line_chart(spec: Mapping[str, Any], design: DesignSystem) -> str:
    width, height = 640, 280
    ml, mr, mt, mb = 60, 28, 30, 54
    plot_w, plot_h = width - ml - mr, height - mt - mb
    labels = spec["labels"]
    axis = design.palette
    colors = axis.series or (axis.primary,)
    series_data = spec.get("series")
    if not series_data:
        series_data = [{
            "label": "",
            "values": spec.get("values", []),
            "color": axis.primary,
        }]

    unit = str(spec.get("unit", "")).strip()
    unit_prefix = f"{unit} " if unit else ""

    all_values = [float(v) for s in series_data for v in s["values"]]
    maximum = max(all_values, default=1.0) * 1.2 or 1.0
    minimum = min(0.0, min(all_values, default=0.0))
    span = max(maximum - minimum, 1.0)
    count = len(labels)

    parts: list[str] = []

    for i in range(5):
        ratio = i / 4
        y = mt + plot_h * ratio
        val = maximum - span * ratio
        parts.append(
            f'<line x1="{ml}" y1="{y:.1f}" x2="{width - mr}" y2="{y:.1f}" '
            f'stroke="{axis.border_light}" stroke-dasharray="2,2"/>'
        )
        parts.append(
            f'<text x="{ml - 8}" y="{y + 4:.1f}" font-size="8" fill="{axis.muted}" '
            f'text-anchor="end">{unit_prefix}{val:g}</text>'
        )

    def point_xy(idx: int, val: float) -> tuple[float, float]:
        px = ml + (plot_w / max(1, count - 1)) * idx
        py = mt + (maximum - val) / span * plot_h
        return px, py

    for index, label in enumerate(labels):
        x = ml + (plot_w / max(1, count - 1)) * index
        primary_label, secondary_label = label_parts(label)
        parts.append(
            f'<text x="{x:.1f}" y="{mt + plot_h + 18:.1f}" font-size="8.5" '
            f'font-weight="600" fill="{axis.text}" text-anchor="middle">'
            f'{esc(primary_label)}</text>'
        )
        if secondary_label:
            parts.append(
                f'<text x="{x:.1f}" y="{mt + plot_h + 30:.1f}" font-size="7" '
                f'font-style="italic" fill="{axis.muted}" text-anchor="middle">'
                f'{esc(secondary_label)}</text>'
            )

    legend_items: list[str] = []
    annotations: list[str] = []

    for series_index, series in enumerate(series_data):
        vals = [float(v) for v in series["values"]]
        color = esc(series.get("color", colors[series_index % len(colors)]))
        points = [point_xy(i, v) for i, v in enumerate(vals)]

        if len(points) >= 2:
            polyline = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
            parts.append(
                f'<polyline points="{polyline}" fill="none" stroke="{color}" '
                f'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
            )

        for i, (x, y) in enumerate(points):
            parts.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{color}" '
                f'stroke="{axis.surface}" stroke-width="1.5"/>'
            )
            annotations.append(
                f'<text x="{x:.1f}" y="{y - 8:.1f}" font-size="7.5" font-weight="700" '
                f'fill="{color}" text-anchor="middle">{vals[i]:g}</text>'
            )

        label = str(series.get("label", "")).strip()
        if label:
            lx = 150 + series_index * 145
            ly = height - 10
            legend_items.append(
                f'<circle cx="{lx}" cy="{ly - 3}" r="4" fill="{color}"/>'
                f'<text x="{lx + 10}" y="{ly}" font-size="8" fill="{axis.text}" '
                f'text-anchor="start">{esc(label)}</text>'
            )

    return chart_frame(
        spec,
        "".join(parts) + "".join(annotations) + "".join(legend_items),
        design,
        width,
        height,
    )


def donut_chart(spec: Mapping[str, Any], design: DesignSystem) -> str:
    width, height = 600, 260
    cx, cy, outer, inner = 160, 130, 92, 53
    values = [max(0.0, float(v)) for v in spec["values"]]
    total = sum(values) or 1.0
    axis = design.palette
    start = -math.pi / 2
    parts: list[str] = []
    legends: list[str] = []
    colors = axis.series or (axis.primary,)

    for index, (label, value) in enumerate(zip(spec["labels"], values)):
        sweep = 2 * math.pi * value / total
        end = start + sweep
        large = 1 if sweep > math.pi else 0
        x1, y1 = cx + outer * math.cos(start), cy + outer * math.sin(start)
        x2, y2 = cx + outer * math.cos(end), cy + outer * math.sin(end)
        x3, y3 = cx + inner * math.cos(end), cy + inner * math.sin(end)
        x4, y4 = cx + inner * math.cos(start), cy + inner * math.sin(start)
        color = colors[index % len(colors)]
        path = (
            f"M {x1:.2f} {y1:.2f} A {outer} {outer} 0 {large} 1 {x2:.2f} {y2:.2f} "
            f"L {x3:.2f} {y3:.2f} A {inner} {inner} 0 {large} 0 {x4:.2f} {y4:.2f} Z"
        )
        parts.append(
            f'<path d="{path}" fill="{esc(color)}" stroke="{axis.surface}" stroke-width="1.5"/>'
        )

        primary_label, secondary_label = label_parts(label)
        y = 42 + index * 38
        percentage = value / total * 100
        legends.append(
            f'<rect x="312" y="{y}" width="12" height="12" rx="2" fill="{esc(color)}"/>'
            f'<text x="332" y="{y + 10}" font-size="8.5" font-weight="700" '
            f'fill="{axis.text_dark}">{esc(primary_label)} — {percentage:.1f}%</text>'
        )
        if secondary_label:
            legends.append(
                f'<text x="332" y="{y + 22}" font-size="7" font-style="italic" '
                f'fill="{axis.muted}">{esc(secondary_label)}</text>'
            )
        start = end

    center_val = esc(spec.get("center_val", spec.get("center_value", "100%")))
    center_lbl = esc(spec.get("center_lbl", spec.get("center_label", "")))
    center = (
        f'<text x="{cx}" y="{cy - 2}" font-size="16" font-weight="900" '
        f'fill="{axis.primary_deep}" text-anchor="middle">{center_val}</text>'
        f'<text x="{cx}" y="{cy + 14}" font-size="8.5" fill="{axis.muted}" '
        f'text-anchor="middle">{center_lbl}</text>'
    )
    return chart_frame(spec, "".join(parts) + center + "".join(legends), design, width, height)


def progress_chart(spec: Mapping[str, Any], design: DesignSystem) -> str:
    items = spec["items"]
    width = 620
    height = max(70, 34 + len(items) * 38)
    axis = design.palette
    parts: list[str] = []
    series_colors = axis.series or (axis.primary,)
    spec_color = spec.get("color")

    for index, item in enumerate(items):
        label_val = item.get("label", "")
        sub_val = item.get("sublabel", "")
        if sub_val:
            label = str(label_val)
            secondary = str(sub_val)
        else:
            label, secondary = label_parts(label_val)

        y = 20 + index * 38
        value = float(item["value"])
        maximum = float(item.get("max", 1.0)) or 1.0
        fill_w = max(0.0, min(1.0, value / maximum)) * 320
        color = item.get("color") or spec_color or series_colors[index % len(series_colors)]

        parts.append(
            f'<text x="25" y="{y + 9}" font-size="8.5" font-weight="700" '
            f'fill="{axis.text_dark}" text-anchor="start">{esc(label)}</text>'
        )
        if secondary:
            parts.append(
                f'<text x="25" y="{y + 21}" font-size="7" font-style="italic" '
                f'fill="{axis.muted}" text-anchor="start">{esc(secondary)}</text>'
            )
        parts.extend(
            [
                f'<rect x="180" y="{y}" width="320" height="14" rx="4" '
                f'fill="{axis.surface_alt}" stroke="{axis.border_light}"/>',
                f'<rect x="180" y="{y}" width="{fill_w:.1f}" height="14" rx="4" '
                f'fill="{esc(color)}"/>',
                f'<text x="515" y="{y + 11}" font-size="9.5" font-weight="800" '
                f'fill="{axis.text_dark}">{value:g}</text>',
            ]
        )

    return chart_frame(spec, "".join(parts), design, width, height)


def flow_diagram(spec: Mapping[str, Any], design: DesignSystem) -> str:
    steps = spec.get("steps", [])
    node_w, node_h, gap = 460, 46, 22
    width = 520
    height = max(100, 26 + len(steps) * (node_h + gap))
    axis = design.palette
    parts: list[str] = []

    for index, step in enumerate(steps):
        label, secondary = label_parts(step.get("label", step.get("title", "")))
        y = 18 + index * (node_h + gap)
        parts.append(
            f'<rect x="30" y="{y}" width="{node_w}" height="{node_h}" rx="8" '
            f'fill="{axis.surface}" stroke="{axis.border}" stroke-width="1.2"/>'
            f'<circle cx="54" cy="{y + 23}" r="13" fill="{axis.primary}"/>'
            f'<text x="54" y="{y + 27}" text-anchor="middle" font-size="8" '
            f'font-weight="700" fill="{axis.surface}">{esc(step.get("badge", index + 1))}</text>'
            f'<text x="78" y="{y + 21}" font-size="9" font-weight="700" '
            f'fill="{axis.text_dark}">{esc(label)}</text>'
        )
        if secondary:
            parts.append(
                f'<text x="78" y="{y + 34}" font-size="7" font-style="italic" '
                f'fill="{axis.muted}">{esc(secondary)}</text>'
            )
        if index < len(steps) - 1:
            parts.append(
                f'<line x1="50" y1="{y + node_h}" x2="50" y2="{y + node_h + gap - 4}" '
                f'stroke="{axis.accent}" stroke-width="2"/>'
            )
            parts.append(
                f'<polygon points="44,{y + node_h + gap - 7} 56,{y + node_h + gap - 7} '
                f'50,{y + node_h + gap - 1}" fill="{axis.accent}"/>'
            )

    return chart_frame(spec, "".join(parts), design, width, height)


def graph_diagram(spec: Mapping[str, Any], design: DesignSystem) -> str:
    nodes = spec.get("nodes", [])
    edges = spec.get("edges", [])
    width, height = 680, 360
    axis = design.palette
    node_w, node_h = 150, 52
    positions: dict[str, tuple[float, float]] = {}

    for index, node in enumerate(nodes):
        if isinstance(node, Mapping):
            node_id = str(node.get("id", index))
            x = float(node.get("x", 40 + (index % 4) * 165))
            y = float(node.get("y", 40 + (index // 4) * 110))
        else:
            node_id = str(index)
            x = 40 + (index % 4) * 165
            y = 40 + (index // 4) * 110
        positions[node_id] = (x, y)

    parts: list[str] = []
    for edge in edges:
        if not isinstance(edge, (list, tuple)) or len(edge) != 2:
            continue
        source, target = str(edge[0]), str(edge[1])
        if source not in positions or target not in positions:
            continue
        sx, sy = positions[source]
        tx, ty = positions[target]
        parts.append(
            f'<line x1="{sx + node_w}" y1="{sy + node_h / 2}" x2="{tx}" y2="{ty + node_h / 2}" '
            f'stroke="{axis.border}" stroke-width="1.5" marker-end="url(#arrow)"/>'
        )

    for index, node in enumerate(nodes):
        if isinstance(node, Mapping):
            node_id = str(node.get("id", index))
            label, secondary = label_parts(node.get("label", node.get("title", "")))
        else:
            node_id = str(index)
            label, secondary = label_parts(node)
        x, y = positions[node_id]
        parts.append(
            f'<rect x="{x}" y="{y}" width="{node_w}" height="{node_h}" rx="8" '
            f'fill="{axis.surface}" stroke="{axis.primary}" stroke-width="1.2"/>'
            f'<text x="{x + node_w / 2}" y="{y + 22}" text-anchor="middle" '
            f'font-size="8.5" font-weight="700" fill="{axis.text_dark}">{esc(label)}</text>'
        )
        if secondary:
            parts.append(
                f'<text x="{x + node_w / 2}" y="{y + 37}" text-anchor="middle" '
                f'font-size="7" font-style="italic" fill="{axis.muted}">{esc(secondary)}</text>'
            )

    defs = (
        f'<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3.5" '
        f'orient="auto"><polygon points="0 0, 8 3.5, 0 7" fill="{axis.border}"/></marker></defs>'
    )
    return chart_frame(spec, defs + "".join(parts), design, width, height)


def diagram(spec: Mapping[str, Any], design: DesignSystem) -> str:
    kind = spec.get("kind", "flow")
    if kind == "flow":
        return flow_diagram(spec, design)
    if kind == "graph":
        return graph_diagram(spec, design)
    raise ValueError(f"Unsupported diagram kind: {kind}")