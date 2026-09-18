"""
core/svg.py — Deterministic, Domain-Agnostic Vector Graphics Engine (Pure SVG)
Generates high-fidelity vector charts and diagrams directly using DesignSystem tokens.

All geometry is expressed in PDF points (pt) inside a fixed viewBox so the
rendered output scales losslessly to any container width. Colors, fonts, and
label styling all come from design tokens; JSON artifacts may override the
series palette per chart and request interpolated `color_scale` ramps.
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


# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------

def _hex_to_rgb(color: str) -> tuple[int, int, int]:
    value = color.lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def _mix(a: str, b: str, ratio: float) -> str:
    ca, cb = _hex_to_rgb(a), _hex_to_rgb(b)
    mixed = [round(x + (y - x) * ratio) for x, y in zip(ca, cb)]
    return "#{:02x}{:02x}{:02x}".format(*mixed)


def color_ramp(count: int, start: str, end: str) -> list[str]:
    if count <= 1:
        return [start]
    return [_mix(start, end, i / (count - 1)) for i in range(count)]


def series_colors(spec: Mapping[str, Any], design: DesignSystem, count: int) -> list[str]:
    """Resolve the color list for a chart: explicit colors, a color_scale ramp,
    or the design-system series palette (cycled)."""
    palette = design.palette
    base = list(palette.series)

    explicit = spec.get("colors")
    if isinstance(explicit, list) and explicit:
        resolved = [str(c) for c in explicit]
        return [resolved[i % len(resolved)] for i in range(count)]

    scale = spec.get("color_scale")
    if isinstance(scale, list) and len(scale) >= 2:
        start, end = str(scale[0]), str(scale[-1])
        if count == 1:
            return [start]
        if len(scale) == 2:
            return color_ramp(count, start, end)
        # multi-stop ramp
        stops = [str(c) for c in scale]
        out = []
        for i in range(count):
            pos = i / (count - 1) * (len(stops) - 1)
            idx = min(int(pos), len(stops) - 2)
            out.append(_mix(stops[idx], stops[idx + 1], pos - idx))
        return out

    return [base[i % len(base)] for i in range(count)]


def axis_max_of(maximum: float, headroom: float = 1.2) -> float:
    """Axis maximum = data maximum scaled by headroom (reference behavior:
    110 -> 132, 240 -> 288) with 4 even intervals."""
    if maximum <= 0:
        return 4.0
    return maximum * headroom


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
           style="direction:ltr !important; unicode-bidi: isolate;"
           xmlns="http://www.w3.org/2000/svg" role="img"
           aria-label="{title}">{body}</svg>
      {caption_html}
    </section>
    """


# ---------------------------------------------------------------------------
# Charts
# ---------------------------------------------------------------------------

def line_chart(spec: Mapping[str, Any], design: DesignSystem) -> str:
    p = design.palette
    fonts = design.typography.families
    width, height = 510, 262
    ml, mr, mt, mb = 42, 12, 16, 48
    plot_w, plot_h = width - ml - mr, height - mt - mb
    labels = spec["labels"]
    series_data = spec.get("series", [])
    unit = str(spec.get("unit", "")).strip()

    values = [float(v) for s in series_data for v in s["values"]] or [1.0]
    axis_max = axis_max_of(max(values))
    colors = series_colors(spec, design, max(1, len(series_data)))

    parts: list[str] = []
    legend_items: list[str] = []

    # horizontal gridlines + y labels (0, 25, 50, 75 % of axis)
    for i in range(5):
        tick_val = axis_max * i / 4
        y = mt + plot_h - (tick_val / axis_max) * plot_h
        parts.append(
            f'<line x1="{ml}" y1="{y:.1f}" x2="{width - mr}" y2="{y:.1f}" '
            f'stroke="{p.border_light}" stroke-width="0.75"/>'
        )
        label_parts_list = []
        number = f"{tick_val:g}"
        if unit:
            label_parts_list.append(
                f'<tspan font-family="{esc(fonts["chart_latin"])}">{number} </tspan>'
                f'<tspan font-family="{esc(fonts["chart_arabic"])}">{esc(unit)}</tspan>'
            )
            label_text = "".join(label_parts_list)
        else:
            label_text = number
        parts.append(
            f'<text x="{ml - 6}" y="{y + 2.3:.1f}" font-size="6.5" fill="{p.chart_axis}" '
            f'text-anchor="end">{label_text}</text>'
        )

    count = len(labels)

    # x labels (primary + optional secondary)
    for index, label in enumerate(labels):
        x = ml + (plot_w / max(1, count - 1)) * index
        primary_label, secondary_label = label_parts(label)
        parts.append(
            f'<line x1="{x:.1f}" y1="{mt}" x2="{x:.1f}" y2="{mt + plot_h}" '
            f'stroke="{p.border_light}" stroke-width="0.5" opacity="0.6"/>'
        )
        parts.append(
            f'<text x="{x:.1f}" y="{mt + plot_h + 12:.1f}" font-size="6.5" font-weight="700" '
            f'fill="{p.chart_axis}" text-anchor="middle" '
            f'font-family="{esc(fonts["chart_arabic"])}">{esc(primary_label)}</text>'
        )
        if secondary_label:
            parts.append(
                f'<text x="{x:.1f}" y="{mt + plot_h + 21:.1f}" font-size="5.3" font-style="italic" '
                f'fill="{p.muted}" text-anchor="middle" '
                f'font-family="{esc(fonts["chart_latin"])}">{esc(secondary_label)}</text>'
            )

    def point_xy(idx: int, val: float) -> tuple[float, float]:
        px = ml + (plot_w / max(1, count - 1)) * idx
        py = mt + plot_h - (val / axis_max) * plot_h
        return px, py

    show_values = bool(spec.get("show_values", False))

    for series_index, series in enumerate(series_data):
        vals = [float(v) for v in series["values"]]
        color = esc(series.get("color") or colors[series_index % len(colors)])
        points = [point_xy(i, v) for i, v in enumerate(vals)]

        if len(points) >= 2:
            polyline = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
            parts.append(
                f'<polyline points="{polyline}" fill="none" stroke="{color}" '
                f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
            )

        for i, (x, y) in enumerate(points):
            parts.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="{color}" '
                f'stroke="{p.surface}" stroke-width="1.4"/>'
            )
            if show_values:
                parts.append(
                    f'<text x="{x:.1f}" y="{y - 5:.1f}" font-size="6.5" font-weight="700" '
                    f'fill="{color}" text-anchor="middle" '
                    f'font-family="{esc(fonts["chart_latin"])}">{vals[i]:g}</text>'
                )

        label = str(series.get("label", "")).strip()
        if label:
            legend_items.append((color, label))

    if legend_items:
        n = len(legend_items)
        spacing = plot_w / n
        for i, (color, label) in enumerate(legend_items):
            # RTL order: the first series is the rightmost legend entry.
            cx = ml + plot_w - (i + 0.5) * spacing
            cy = height - 8
            parts.append(
                f'<circle cx="{cx:.1f}" cy="{cy}" r="3.5" fill="{color}"/>'
                f'<text x="{cx + 8:.1f}" y="{cy + 2.6:.1f}" font-size="7.3" font-weight="400" '
                f'fill="{p.chart_axis}" text-anchor="start" '
                f'font-family="{esc(fonts["chart_arabic"])}">{esc(label)}</text>'
            )

    return chart_frame(spec, "".join(parts), design, width, height)


def bar_chart(spec: Mapping[str, Any], design: DesignSystem) -> str:
    p = design.palette
    fonts = design.typography.families
    width, height = 510, 240
    ml, mr, mt, mb = 40, 12, 20, 46
    plot_w, plot_h = width - ml - mr, height - mt - mb
    values = [float(v) for v in spec["values"]]
    labels = spec["labels"]
    unit = str(spec.get("unit", "")).strip()
    axis_max = axis_max_of(max(values, default=0.0))
    colors = series_colors(spec, design, max(1, len(values)))
    count = max(1, len(values))
    bar_w = min(46.0, plot_w / count * 0.52)
    gap = (plot_w - bar_w * count) / (count + 1)

    parts: list[str] = []

    for i in range(5):
        tick_val = axis_max * i / 4
        y = mt + plot_h - (tick_val / axis_max) * plot_h
        parts.append(
            f'<line x1="{ml}" y1="{y:.1f}" x2="{width - mr}" y2="{y:.1f}" '
            f'stroke="{p.border_light}" stroke-width="0.75"/>'
        )
        parts.append(
            f'<text x="{ml - 6}" y="{y + 2.3:.1f}" font-size="6.5" fill="{p.chart_axis}" '
            f'text-anchor="end" font-family="{esc(fonts["chart_latin"])}">{tick_val:g}</text>'
        )

    for index, (label, value) in enumerate(zip(labels, values)):
        x = ml + gap + index * (bar_w + gap)
        bar_h = (value / axis_max) * plot_h
        y = mt + plot_h - bar_h
        primary_label, secondary_label = label_parts(label)
        color = colors[index % len(colors)]

        val_display = f"{value:g} {unit}" if unit else f"{value:g}"
        parts.extend(
            [
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" '
                f'rx="3" fill="{esc(color)}"/>',
                f'<text x="{x + bar_w / 2:.1f}" y="{y - 4:.1f}" '
                f'font-family="{esc(fonts["chart_arabic"])}" font-size="7.3" font-weight="700" '
                f'fill="{p.text_dark}" text-anchor="middle">{esc(val_display)}</text>',
                f'<text x="{x + bar_w / 2:.1f}" y="{mt + plot_h + 11:.1f}" '
                f'font-family="{esc(fonts["chart_arabic"])}" font-size="6.5" font-weight="700" '
                f'fill="{p.chart_axis}" text-anchor="middle">{esc(primary_label)}</text>',
            ]
        )
        if secondary_label:
            parts.append(
                f'<text x="{x + bar_w / 2:.1f}" y="{mt + plot_h + 19.5:.1f}" '
                f'font-family="{esc(fonts["chart_latin"])}" font-size="5.3" '
                f'font-style="italic" fill="{p.muted}" text-anchor="middle">{esc(secondary_label)}</text>'
            )

    # axis lines
    parts.append(
        f'<line x1="{ml}" y1="{mt + plot_h}" x2="{width - mr}" y2="{mt + plot_h}" '
        f'stroke="{p.chart_axis}" stroke-width="0.65"/>'
    )
    parts.append(
        f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{mt + plot_h}" '
        f'stroke="{p.chart_axis}" stroke-width="0.65"/>'
    )

    return chart_frame(spec, "".join(parts), design, width, height)


def donut_chart(spec: Mapping[str, Any], design: DesignSystem) -> str:
    p = design.palette
    fonts = design.typography.families
    width, height = 510, 205
    cx, cy, outer, inner = 132, 102, 62, 38
    values = [max(0.0, float(v)) for v in spec["values"]]
    total = sum(values) or 1.0
    start = -math.pi / 2
    parts: list[str] = []
    legends: list[str] = []
    colors = series_colors(spec, design, max(1, len(values)))

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
            f'<path d="{path}" fill="{esc(color)}" stroke="{p.surface}" stroke-width="1"/>'
        )

        primary_label, secondary_label = label_parts(label)
        y = 38 + index * 36
        percentage = value / total * 100
        swatch_x = 254
        # Legend row reads LTR: swatch, then "XX.X% — " in latin, then the
        # Arabic label at the right end (reference composite layout).
        legends.append(
            f'<rect x="{swatch_x}" y="{y - 9}" width="10" height="10" rx="2" fill="{esc(color)}"/>'
            f'<text x="{swatch_x + 16}" y="{y}" font-size="7.5" font-weight="700" '
            f'fill="{p.chart_axis}" direction="ltr" text-anchor="start" '
            f'font-family="{esc(fonts["chart_latin"])}">'
            f'<tspan>{percentage:.1f}% — </tspan>'
            f'<tspan font-family="{esc(fonts["chart_arabic"])}">{esc(primary_label)}</tspan></text>'
        )
        if secondary_label:
            legends.append(
                f'<text x="{swatch_x + 16}" y="{y + 10.5}" font-size="5.9" font-style="italic" '
                f'fill="{p.muted}" direction="ltr" text-anchor="start" '
                f'font-family="{esc(fonts["chart_latin"])}">{esc(secondary_label)}</text>'
            )
        start = end

    center_val = esc(spec.get("center_val", spec.get("center_value", "100%")))
    center_lbl = esc(spec.get("center_lbl", spec.get("center_label", "")))
    center = (
        f'<text x="{cx}" y="{cy - 2}" font-size="15" font-weight="700" '
        f'fill="{p.text_dark}" text-anchor="middle" '
        f'font-family="{esc(fonts["chart_latin"])}">{center_val}</text>'
        f'<text x="{cx}" y="{cy + 13}" font-size="8" fill="{p.muted}" '
        f'text-anchor="middle" font-family="{esc(fonts["chart_arabic"])}">{center_lbl}</text>'
    )
    return chart_frame(spec, "".join(parts) + center + "".join(legends), design, width, height)


def progress_chart(spec: Mapping[str, Any], design: DesignSystem) -> str:
    p = design.palette
    fonts = design.typography.families
    items = spec["items"]
    width = 510
    row_pitch = 36.9
    height = max(56, 14 + len(items) * row_pitch)
    colors = series_colors(spec, design, max(1, len(items)))
    spec_color = spec.get("color")

    label_x = 58
    track_x = 196
    track_w = 260
    track_h = 13.4
    parts: list[str] = []

    for index, item in enumerate(items):
        label_val = item.get("label", "")
        sub_val = item.get("sublabel", "")
        if sub_val:
            label = str(label_val)
            secondary = str(sub_val)
        else:
            label, secondary = label_parts(label_val)

        y = 8 + index * row_pitch
        value = float(item["value"])
        maximum = float(item.get("max", 1.0)) or 1.0
        fill_w = max(0.0, min(1.0, value / maximum)) * track_w
        color = item.get("color") or spec_color or colors[index % len(colors)]

        # label block on the left, right-aligned
        parts.append(
            f'<text x="{label_x}" y="{y + 8.5:.1f}" font-size="7.5" font-weight="400" '
            f'fill="{p.chart_axis}" text-anchor="start" direction="rtl" '
            f'font-family="{esc(fonts["chart_arabic"])}">{esc(label)}</text>'
        )
        if secondary:
            parts.append(
                f'<text x="{label_x}" y="{y + 17.5:.1f}" font-size="5.9" font-style="italic" '
                f'fill="{p.muted}" text-anchor="end" direction="ltr" '
                f'font-family="{esc(fonts["chart_latin"])}">{esc(secondary)}</text>'
            )
        # track (light) + right-anchored fill (grows leftward for RTL reading)
        parts.extend(
            [
                f'<rect x="{track_x}" y="{y + 1:.1f}" width="{track_w}" height="{track_h}" rx="2" '
                f'fill="{p.chart_track}" stroke="{p.chart_track_border}" stroke-width="0.75"/>',
                f'<rect x="{track_x + track_w - fill_w:.1f}" y="{y + 1:.1f}" width="{fill_w:.1f}" '
                f'height="{track_h}" rx="2" fill="{esc(color)}"/>',
                f'<text x="{track_x + track_w + 8:.1f}" y="{y + 11.5:.1f}" font-size="8.4" '
                f'font-weight="700" fill="{p.text_dark}" '
                f'font-family="{esc(fonts["chart_latin"])}">{value:g}</text>',
            ]
        )

    return chart_frame(spec, "".join(parts), design, width, height)


# ---------------------------------------------------------------------------
# Diagrams
# ---------------------------------------------------------------------------

def flow_diagram(spec: Mapping[str, Any], design: DesignSystem) -> str:
    p = design.palette
    fonts = design.typography.families
    steps = spec.get("steps", [])
    node_w, node_h, gap = 460, 46, 22
    width = 510
    height = max(100, 26 + len(steps) * (node_h + gap))
    parts: list[str] = []

    for index, step in enumerate(steps):
        label, secondary = label_parts(step.get("label", step.get("title", "")))
        y = 18 + index * (node_h + gap)
        parts.append(
            f'<rect x="25" y="{y}" width="{node_w}" height="{node_h}" rx="8" '
            f'fill="{p.surface}" stroke="{p.border}" stroke-width="1.2"/>'
            f'<circle cx="49" cy="{y + 23}" r="11.25" fill="{p.primary}"/>'
            f'<text x="49" y="{y + 26.5}" text-anchor="middle" font-size="8" '
            f'font-weight="700" fill="{p.surface}">{esc(step.get("badge", index + 1))}</text>'
            f'<text x="70" y="{y + 21}" font-size="9" font-weight="700" '
            f'fill="{p.text_dark}">{esc(label)}</text>'
        )
        if secondary:
            parts.append(
                f'<text x="70" y="{y + 34}" font-size="7" font-style="italic" '
                f'fill="{p.muted}">{esc(secondary)}</text>'
            )
        if index < len(steps) - 1:
            parts.append(
                f'<line x1="45" y1="{y + node_h}" x2="45" y2="{y + node_h + gap - 4}" '
                f'stroke="{p.accent}" stroke-width="2"/>'
            )
            parts.append(
                f'<polygon points="39,{y + node_h + gap - 7} 51,{y + node_h + gap - 7} '
                f'45,{y + node_h + gap - 1}" fill="{p.accent}"/>'
            )

    return chart_frame(spec, "".join(parts), design, width, height)


def graph_diagram(spec: Mapping[str, Any], design: DesignSystem) -> str:
    p = design.palette
    nodes = spec.get("nodes", [])
    edges = spec.get("edges", [])
    width, height = 510, 360
    node_w, node_h = 150, 52
    positions: dict[str, tuple[float, float]] = {}

    for index, node in enumerate(nodes):
        if isinstance(node, Mapping):
            node_id = str(node.get("id", index))
            x = float(node.get("x", 40 + (index % 3) * 165))
            y = float(node.get("y", 40 + (index // 3) * 110))
        else:
            node_id = str(index)
            x = 40 + (index % 3) * 165
            y = 40 + (index // 3) * 110
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
            f'stroke="{p.border}" stroke-width="1.5" marker-end="url(#arrow)"/>'
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
            f'fill="{p.surface}" stroke="{p.primary}" stroke-width="1.2"/>'
            f'<text x="{x + node_w / 2}" y="{y + 22}" text-anchor="middle" '
            f'font-size="8.5" font-weight="700" fill="{p.text_dark}">{esc(label)}</text>'
        )
        if secondary:
            parts.append(
                f'<text x="{x + node_w / 2}" y="{y + 37}" text-anchor="middle" '
                f'font-size="7" font-style="italic" fill="{p.muted}">{esc(secondary)}</text>'
            )

    defs = (
        f'<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3.5" '
        f'orient="auto"><polygon points="0 0, 8 3.5, 0 7" fill="{p.border}"/></marker></defs>'
    )
    return chart_frame(spec, defs + "".join(parts), design, width, height)


def diagram(spec: Mapping[str, Any], design: DesignSystem) -> str:
    kind = spec.get("kind", "flow")
    if kind == "flow":
        return flow_diagram(spec, design)
    if kind == "graph":
        return graph_diagram(spec, design)
    raise ValueError(f"Unsupported diagram kind: {kind}")
