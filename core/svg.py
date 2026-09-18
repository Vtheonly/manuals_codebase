"""
core/svg.py — Deterministic Vector Graphics Generator (Pure SVG)
"""
import html
import math
from core.design import DESIGN

def esc(v: object) -> str:
    return html.escape(str(v), quote=True)

def bar_chart(a: dict) -> str:
    p = DESIGN.palette; ty = DESIGN.typography
    w, h = 620, 280
    ml, mr, mt, mb = 50, 20, 30, 45
    pw, ph = w - ml - mr, h - mt - mb
    
    vals = [float(x) for x in a["values"]]
    mx = max(vals, default=1.0) * 1.2 or 1.0
    n = max(1, len(vals))
    bw = max(16.0, (pw / n) * 0.48)
    gap = (pw - (bw * n)) / (n + 1)
    unit = a.get("unit", "")
    
    parts = []
    # خطوط الشبكة والمحور
    for i in range(5):
        y = mt + ph * i / 4
        val = mx * (1 - i / 4)
        parts.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{w - mr}" y2="{y:.1f}" stroke="{p.border_light}" stroke-dasharray="2,2"/>')
        parts.append(f'<text x="{ml - 8}" y="{y + 4:.1f}" font-family="{ty.latin}" font-size="8.5" fill="{p.muted}" text-anchor="end">{int(val)}</text>')
        
    for i, (lbl, val) in enumerate(zip(a["labels"], vals)):
        x = ml + gap + i * (bw + gap)
        bh = (val / mx) * ph
        y = mt + ph - bh
        color = p.primary if i % 2 == 0 else p.accent
        
        lbl_ar = lbl[0] if isinstance(lbl, list) else str(lbl)
        lbl_fr = lbl[1] if isinstance(lbl, list) and len(lbl) > 1 else ""
        
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="2" fill="{color}"/>')
        parts.append(f'<text x="{x + bw/2:.1f}" y="{y - 5:.1f}" font-family="{ty.arabic}" font-size="9" font-weight="700" fill="{p.text_dark}" text-anchor="middle">{unit} {int(val)}</text>')
        parts.append(f'<text x="{x + bw/2:.1f}" y="{mt + ph + 16:.1f}" font-family="{ty.arabic}" font-size="8.5" font-weight="600" fill="{p.text}" text-anchor="middle">{esc(lbl_ar)}</text>')
        if lbl_fr:
            parts.append(f'<text x="{x + bw/2:.1f}" y="{mt + ph + 28:.1f}" font-family="{ty.latin}" font-style="italic" font-size="7" fill="{p.muted}" text-anchor="middle">{esc(lbl_fr)}</text>')

    caption_html = f'<div class="chart-caption"><span>{esc(a.get("caption_ar", ""))}</span> — <span class="fr">{esc(a.get("caption_fr", ""))}</span></div>' if "caption_ar" in a else ""
    return f"""
    <div class="artifact chart-container">
        <div class="chart-header">
            <h4 class="chart-title-ar">{esc(a["title"])}</h4>
            <p class="chart-title-fr">{esc(a.get("subtitle_fr", ""))}</p>
        </div>
        <svg viewBox="0 0 {w} {h}" class="svg-viewport" xmlns="http://www.w3.org/2000/svg">{''.join(parts)}</svg>
        {caption_html}
    </div>
    """

def donut_chart(a: dict) -> str:
    p = DESIGN.palette; ty = DESIGN.typography
    w, h = 580, 250
    cx, cy, r_out, r_in = 160, 125, 90, 52
    
    vals = [float(x) for x in a["values"]]
    total = sum(vals) or 1.0
    start = -math.pi / 2
    parts, legends = [], []
    
    for i, (lbl, val) in enumerate(zip(a["labels"], vals)):
        sweep = 2 * math.pi * val / total
        end = start + sweep
        large = int(sweep > math.pi)
        
        x1, y1 = cx + r_out * math.cos(start), cy + r_out * math.sin(start)
        x2, y2 = cx + r_out * math.cos(end), cy + r_out * math.sin(end)
        x3, y3 = cx + r_in * math.cos(end), cy + r_in * math.sin(end)
        x4, y4 = cx + r_in * math.cos(start), cy + r_in * math.sin(start)
        color = p.series[i % len(p.series)]
        
        d = f"M {x1:.2f} {y1:.2f} A {r_out} {r_out} 0 {large} 1 {x2:.2f} {y2:.2f} L {x3:.2f} {y3:.2f} A {r_in} {r_in} 0 {large} 0 {x4:.2f} {y4:.2f} Z"
        parts.append(f'<path d="{d}" fill="{color}" stroke="#fff" stroke-width="1.5"/>')
        
        pct = val / total * 100
        ly = 45 + i * 36
        lbl_ar = lbl[0] if isinstance(lbl, list) else str(lbl)
        lbl_fr = lbl[1] if isinstance(lbl, list) and len(lbl) > 1 else ""
        
        legends.append(f'<rect x="310" y="{ly}" width="12" height="12" rx="2" fill="{color}"/>')
        legends.append(f'<text x="330" y="{ly + 10}" font-family="{ty.arabic}" font-size="9" font-weight="700" fill="{p.text_dark}">{esc(lbl_ar)} — {pct:.1f}%</text>')
        if lbl_fr:
            legends.append(f'<text x="330" y="{ly + 22}" font-family="{ty.latin}" font-style="italic" font-size="7.5" fill="{p.muted}">{esc(lbl_fr)}</text>')
        start = end

    center_badge = f"""
    <text x="{cx}" y="{cy - 2}" font-family="{ty.latin}" font-size="16" font-weight="900" fill="{p.primary_deep}" text-anchor="middle">{esc(a.get("center_val", "100%"))}</text>
    <text x="{cx}" y="{cy + 14}" font-family="{ty.latin}" font-size="8" fill="{p.muted}" text-anchor="middle">{esc(a.get("center_lbl", "CAD/FAO"))}</text>
    """
    caption_html = f'<div class="chart-caption"><span>{esc(a.get("caption_ar", ""))}</span> — <span class="fr">{esc(a.get("caption_fr", ""))}</span></div>' if "caption_ar" in a else ""

    return f"""
    <div class="artifact chart-container">
        <div class="chart-header">
            <h4 class="chart-title-ar">{esc(a["title"])}</h4>
            <p class="chart-title-fr">{esc(a.get("subtitle_fr", ""))}</p>
        </div>
        <svg viewBox="0 0 {w} {h}" class="svg-viewport" xmlns="http://www.w3.org/2000/svg">{''.join(parts)}{center_badge}{''.join(legends)}</svg>
        {caption_html}
    </div>
    """

def line_chart(a: dict) -> str:
    p = DESIGN.palette; ty = DESIGN.typography
    w, h = 620, 270
    ml, mr, mt, mb = 55, 25, 30, 40
    pw, ph = w - ml - mr, h - mt - mb
    
    vals = [float(x) for x in a["values"]]
    mx = max(vals, default=1.0) * 1.2 or 1.0
    n = len(vals)
    unit = a.get("unit", "")
    
    parts = []
    for i in range(5):
        y = mt + ph * i / 4
        val = mx * (1 - i / 4)
        parts.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{w - mr}" y2="{y:.1f}" stroke="{p.border_light}" stroke-dasharray="2,2"/>')
        parts.append(f'<text x="{ml - 8}" y="{y + 4:.1f}" font-family="{ty.latin}" font-size="8.5" fill="{p.muted}" text-anchor="end">{int(val)} {unit}</text>')
        
    for i, lbl in enumerate(a["labels"]):
        x = ml + (pw / max(1, n - 1)) * i
        parts.append(f'<text x="{x:.1f}" y="{mt + ph + 18:.1f}" font-family="{ty.arabic}" font-size="8.5" fill="{p.text}" text-anchor="middle">{esc(lbl)}</text>')
        
    pts = []
    for i, val in enumerate(vals):
        x = ml + (pw / max(1, n - 1)) * i
        y = mt + ph - (val / mx) * ph
        pts.append((x, y))
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{p.accent}" stroke="#fff" stroke-width="1.5"/>')
        parts.append(f'<text x="{x:.1f}" y="{y - 8:.1f}" font-family="{ty.latin}" font-size="8.5" font-weight="700" fill="{p.primary}" text-anchor="middle">{int(val)}</text>')
        
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    parts.insert(0, f'<polyline points="{poly}" fill="none" stroke="{p.primary}" stroke-width="2.5"/>')
    caption_html = f'<div class="chart-caption"><span>{esc(a.get("caption_ar", ""))}</span> — <span class="fr">{esc(a.get("caption_fr", ""))}</span></div>' if "caption_ar" in a else ""

    return f"""
    <div class="artifact chart-container">
        <div class="chart-header">
            <h4 class="chart-title-ar">{esc(a["title"])}</h4>
            <p class="chart-title-fr">{esc(a.get("subtitle_fr", ""))}</p>
        </div>
        <svg viewBox="0 0 {w} {h}" class="svg-viewport" xmlns="http://www.w3.org/2000/svg">{''.join(parts)}</svg>
        {caption_html}
    </div>
    """

def progress_chart(a: dict) -> str:
    p = DESIGN.palette; ty = DESIGN.typography
    items = a["items"]
    bar_h, row_h = 14, 38
    w, h = 600, 25 + len(items) * row_h
    parts = []
    
    for i, item in enumerate(items):
        y = 20 + i * row_h
        lbl_ar = item["label_ar"]
        lbl_fr = item.get("label_fr", "")
        val, mx = float(item["value"]), float(item.get("max", 5.0))
        color = p.primary if i % 2 == 0 else p.accent
        
        parts.append(f'<text x="10" y="{y + 8}" font-family="{ty.arabic}" font-size="9" font-weight="700" fill="{p.text_dark}">{esc(lbl_ar)}</text>')
        if lbl_fr:
            parts.append(f'<text x="10" y="{y + 19}" font-family="{ty.latin}" font-style="italic" font-size="7.5" fill="{p.muted}">{esc(lbl_fr)}</text>')
            
        bx, max_bw = 210, 320
        fw = (val / mx) * max_bw if mx else 0
        parts.append(f'<rect x="{bx}" y="{y}" width="{max_bw}" height="{bar_h}" rx="3" fill="{p.surface_alt}" stroke="{p.border_light}"/>')
        parts.append(f'<rect x="{bx}" y="{y}" width="{fw:.1f}" height="{bar_h}" rx="3" fill="{color}"/>')
        parts.append(f'<text x="{bx + max_bw + 14}" y="{y + 11}" font-family="{ty.latin}" font-size="9.5" font-weight="800" fill="{p.text_dark}">{val:g}</text>')

    caption_html = f'<div class="chart-caption"><span>{esc(a.get("caption_ar", ""))}</span> — <span class="fr">{esc(a.get("caption_fr", ""))}</span></div>' if "caption_ar" in a else ""
    return f"""
    <div class="artifact chart-container">
        <div class="chart-header">
            <h4 class="chart-title-ar">{esc(a["title"])}</h4>
            <p class="chart-title-fr">{esc(a.get("subtitle_fr", ""))}</p>
        </div>
        <svg viewBox="0 0 {w} {h}" class="svg-viewport" xmlns="http://www.w3.org/2000/svg">{''.join(parts)}</svg>
        {caption_html}
    </div>
    """

def diagram(a: dict) -> str:
    # مخطط المسار الرأسي للعمليات (Vertical Step Flowchart)
    steps = a.get("steps", [])
    parts = []
    for i, step in enumerate(steps):
        parts.append(f"""
        <div class="flow-step-node">
            <div class="step-circle">{step["index"]}</div>
            <div class="step-desc">
                <p class="step-text-ar">{esc(step["title_ar"])}</p>
                <p class="step-text-fr">{esc(step.get("subtitle_fr", ""))}</p>
            </div>
        </div>
        """)
        if i < len(steps) - 1:
            parts.append('<div class="flow-step-arrow">▼</div>')
            
    header_html = f"""
    <div class="section-sub-header">
        <h4 class="sub-title-ar">{esc(a["title"])}</h4>
        <span class="sub-title-fr">— {esc(a.get("subtitle_fr", ""))}</span>
    </div>
    """ if "title" in a else ""

    return f"""
    <div class="artifact flowchart-container">
        {header_html}
        <div class="flow-sequence">{''.join(parts)}</div>
    </div>
    """