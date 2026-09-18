"""HTML document renderer driven by the JSON document and design tokens."""
from __future__ import annotations

import html
from collections.abc import Mapping
from typing import Any

from core.design import DesignSystem


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def build_stylesheet(design: DesignSystem, direction: str) -> str:
    p, t, s, b = design.palette, design.typography, design.spacing, design.borders
    align_default = "right" if direction == "rtl" else "left"
    return f"""
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:ital,wght@0,400;0,600;0,700;1,400&display=swap');

    *, *::before, *::after {{ box-sizing:border-box; margin:0; padding:0; }}
    html, body {{ margin:0; padding:0; }}
    @page {{ size:{design.page.width} {design.page.height}; margin:0; }}

    @media print {{
      body {{ background:transparent !important; }}
      .page-sheet {{ box-shadow:none !important; margin:0 !important; break-after:page !important; page-break-after:always !important; }}
    }}

    body {{
      background:#cbd5e1;
      color:{p.text};
      font-family:{t.font_arabic};
      direction:{esc(direction)};
      text-align:{align_default};
      -webkit-print-color-adjust:exact;
      print-color-adjust:exact;
      display:flex;
      flex-direction:column;
      align-items:center;
    }}

    .page-sheet {{
      width:{design.page.width};
      height:{design.page.height};
      max-height:{design.page.height};
      background:{p.surface};
      color:{p.text};
      padding:{s.page_y} {s.page_x};
      margin-bottom:20px;
      position:relative;
      display:flex;
      flex-direction:column;
      justify-content:space-between;
      gap:{s.md};
      box-shadow:0 4px 18px rgba(0,0,0,.08);
      overflow:hidden;
    }}

    .page-content {{ flex:1; min-height:0; display:flex; flex-direction:column; gap:8px; }}

    .layout-framed {{ padding:10mm; }}
    .layout-framed .page-frame {{
      height:100%;
      border:{b.thick} solid {p.primary};
      border-radius:{b.radius_sm};
      padding:{s.frame_padding};
      display:flex;
      flex-direction:column;
      justify-content:space-between;
      overflow:hidden;
    }}

    .layout-dark {{
      background:{p.primary_deep};
      color:{p.surface};
      padding:18mm 16mm;
      justify-content:space-between;
    }}
    .layout-dark .block-text, .layout-dark .quote {{ color:{p.surface}; }}
    .layout-dark .block-heading h1, .layout-dark .block-heading h2, .layout-dark .block-heading h3,
    .layout-dark .block-heading h4, .layout-dark .block-heading h5, .layout-dark .block-heading h6 {{ color:{p.surface}; }}

    h1,h2,h3,h4,h5,h6,p,ul,ol,figure {{ margin:0; }}

    /* Semantic headings */
    .block-heading {{
      display:flex;
      align-items:center;
      gap:8px;
      border-bottom:2px solid {p.primary};
      padding-bottom:4px;
      margin-bottom:4px;
    }}
    .block-heading h1 {{ font-size:{t.sizes["3xl"]}; font-weight:{t.weights["heavy"]}; }}
    .block-heading h2 {{ font-size:{t.sizes["2xl"]}; font-weight:{t.weights["heavy"]}; }}
    .block-heading h3 {{ font-size:{t.sizes["xl"]}; font-weight:{t.weights["bold"]}; }}
    .block-heading h4 {{ font-size:{t.sizes["lg"]}; font-weight:{t.weights["bold"]}; }}
    .block-heading h5,.block-heading h6 {{ font-size:{t.sizes["md"]}; font-weight:{t.weights["bold"]}; }}

    .circle-badge {{
      width:24px;
      height:24px;
      border-radius:50%;
      background:{p.primary};
      color:{p.surface};
      display:inline-flex;
      align-items:center;
      justify-content:center;
      font-weight:{t.weights["bold"]};
      font-size:{t.sizes["xs"]};
      flex-shrink:0;
    }}
    .sub-label {{
      display:block;
      color:{p.accent};
      font-family:{t.font_latin};
      font-style:italic;
      font-size:{t.sizes["xs"]};
      margin-top:2px;
    }}

    /* Subsections */
    .subsection-header {{
      display:flex;
      align-items:baseline;
      gap:8px;
      border-inline-end:3.5px solid {p.accent};
      padding-inline-end:8px;
      margin:8px 0 4px 0;
    }}
    .sub-title-ar {{ font-size:10.5pt; font-weight:{t.weights["bold"]}; color:{p.primary_deep}; }}
    .sub-title-fr {{ font-family:{t.font_latin}; font-style:italic; font-size:{t.sizes["xs"]}; color:{p.muted}; direction:ltr; }}

    /* Text */
    .block-text {{ font-size:{t.sizes["base"]}; line-height:1.6; text-align:justify; margin-bottom:4px; }}
    .block-text p + p {{ margin-top:4px; }}
    .align-left {{ text-align:left; }}
    .align-right {{ text-align:right; }}
    .align-center {{ text-align:center; }}
    .align-justify {{ text-align:justify; }}

    /* Badges and cards */
    .badge-wrapper {{ margin:8px 0; }}
    .badge {{
      display:inline-block;
      padding:4px 18px;
      border-radius:30px;
      font-size:{t.sizes["sm"]};
      font-weight:{t.weights["bold"]};
    }}
    .badge-default,.badge-solid {{ background:{p.primary}; color:{p.surface}; }}
    .badge-plain {{ background:transparent; color:{p.primary_deep}; }}
    .badge-dashed {{ background:{p.surface_alt}; color:{p.primary}; border:1.5px dashed {p.primary}; border-radius:20px; }}
    .badge-gradient {{ background:linear-gradient(135deg,{p.banner_start},{p.banner_end}); color:{p.banner_text}; border:1px solid {p.banner_border}; padding:5px 35px; border-radius:6px; }}

    .card {{
      border:1.5px solid {p.banner_border};
      border-radius:12px;
      padding:12px 18px;
      margin:8px 0;
      text-align:center;
      background:linear-gradient(135deg,{p.banner_start},{p.banner_end});
    }}
    .card-label {{ color:{p.banner_text}; font-weight:{t.weights["bold"]}; font-size:9pt; }}
    .card-title {{ color:{p.banner_text}; font-size:{t.sizes["2xl"]}; font-weight:{t.weights["black"]}; margin:2px 0; }}
    .card-subtitle {{ color:{p.primary}; font-style:italic; font-family:{t.font_latin}; font-size:8pt; }}
    .card-content {{ margin-top:8px; }}
    .card-pill {{
      display:inline-block;
      margin-top:6px;
      padding:3px 14px;
      border-radius:20px;
      background:{p.surface};
      color:{p.primary_deep};
      border:1px solid {p.border_light};
      font-size:{t.sizes["xs"]};
      font-weight:{t.weights["bold"]};
    }}

    .info-card {{ border:1.5px solid {p.border}; border-radius:12px; padding:14px 20px; margin:8px 0; display:flex; flex-direction:column; gap:8px; }}
    .info-row {{ display:flex; align-items:baseline; font-size:{t.sizes["base"]}; }}
    .info-row.highlight .info-value {{ color:{p.primary_deep}; font-weight:{t.weights["heavy"]}; font-size:{t.sizes["md"]}; }}
    .info-label {{ width:170px; font-weight:{t.weights["bold"]}; color:{p.primary}; flex-shrink:0; }}
    .info-sep {{ width:16px; text-align:center; font-weight:{t.weights["bold"]}; color:{p.primary}; }}
    .info-value {{ flex:1; }}

    /* Formula */
    .formula-box {{
      border-inline-end:4px solid {p.accent};
      border-radius:6px;
      background:{p.accent_light};
      padding:10px 16px;
      margin:8px 0;
    }}
    .formula-title {{
      display:flex;
      align-items:center;
      gap:6px;
      font-size:9.5pt;
      font-weight:{t.weights["bold"]};
      color:{p.accent};
      margin-bottom:4px;
    }}
    .formula-icon {{ font-family:{t.font_math}; font-size:12pt; }}
    .formula-math {{
      text-align:center;
      font-family:{t.font_math};
      font-size:14pt;
      font-weight:{t.weights["bold"]};
      margin:4px 0;
      direction:ltr;
      unicode-bidi:isolate;
    }}
    .formula-desc {{ font-size:{t.sizes["sm"]}; line-height:1.5; }}

    /* Callouts and stats */
    .callout {{
      border-inline-end:4px solid {p.accent};
      border-radius:6px;
      background:{p.accent_light};
      padding:10px 14px;
      margin:6px 0;
    }}
    .callout-primary {{ border-color:{p.primary}; background:{p.primary_light}; }}
    .callout-header {{
      display:flex;
      align-items:center;
      gap:6px;
      font-weight:{t.weights["bold"]};
      font-size:9.5pt;
      margin-bottom:3px;
      color:{p.accent};
    }}
    .callout-primary .callout-header {{ color:{p.primary_deep}; }}
    .callout-icon {{ font-family:{t.font_math}; }}
    .callout-content {{ font-size:{t.sizes["sm"]}; line-height:1.55; }}

    .stats-grid {{ display:grid; gap:8px; margin:8px 0; }}
    .cols-1 {{ grid-template-columns:repeat(1,1fr); }}
    .cols-2 {{ grid-template-columns:repeat(2,1fr); }}
    .cols-3 {{ grid-template-columns:repeat(3,1fr); }}
    .cols-4 {{ grid-template-columns:repeat(4,1fr); }}
    .cols-5 {{ grid-template-columns:repeat(5,1fr); }}
    .cols-6 {{ grid-template-columns:repeat(6,1fr); }}
    .stat-card {{
      border:1px solid {p.border_light};
      border-top:3px solid {p.accent};
      border-radius:4px;
      padding:8px;
      text-align:center;
      background:{p.surface};
    }}
    .stat-value {{ font-size:14pt; font-weight:{t.weights["black"]}; color:{p.primary_deep}; font-family:{t.font_latin}; }}
    .stat-label {{ font-size:{t.sizes["xs"]}; font-weight:{t.weights["bold"]}; margin-top:2px; }}
    .stat-sub {{ display:block; font-size:6.5pt; color:{p.muted}; font-style:italic; }}

    /* Tables */
    .table-wrapper {{ margin:6px 0; }}
    .table-header {{
      display:flex;
      align-items:baseline;
      gap:8px;
      border-inline-end:4px solid {p.accent};
      padding-inline-end:8px;
      margin-bottom:4px;
    }}
    .table-header h4 {{ color:{p.primary_deep}; }}
    .table-header span {{ color:{p.muted}; font-size:{t.sizes["xs"]}; font-family:{t.font_latin}; font-style:italic; }}
    .standard-table {{ width:100%; border-collapse:collapse; font-size:8pt; border:1px solid {p.border}; }}
    .standard-table th {{ background:{p.primary}; color:{p.surface}; padding:5px 8px; text-align:inherit; border:1px solid {p.primary_deep}; }}
    .standard-table td {{ border:1px solid {p.border_light}; padding:5px 8px; }}
    .standard-table tbody tr:nth-child(even) {{ background:{p.surface_alt}; }}
    td.num {{ text-align:center; font-family:{t.font_latin}; font-weight:{t.weights["bold"]}; }}
    .th-sub, .td-sub {{ display:block; color:{p.muted}; font-style:italic; font-size:6.5pt; }}
    .caption {{ text-align:center; color:{p.primary}; font-weight:{t.weights["bold"]}; font-size:{t.sizes["xs"]}; margin-top:4px; }}

    /* Flow */
    .flow-steps {{ border:1px solid {p.border_light}; background:{p.surface_alt}; border-radius:8px; padding:10px 14px; }}
    .flow-title {{ font-weight:{t.weights["bold"]}; color:{p.primary_deep}; margin-bottom:8px; }}
    .step-node {{ display:flex; align-items:center; gap:10px; }}
    .step-num {{ width:22px; height:22px; border-radius:50%; background:{p.primary}; color:{p.surface}; display:inline-flex; align-items:center; justify-content:center; font-size:{t.sizes["xs"]}; font-weight:{t.weights["bold"]}; flex-shrink:0; }}
    .step-title {{ font-weight:{t.weights["bold"]}; font-size:{t.sizes["sm"]}; }}
    .step-sub {{ color:{p.muted}; font-family:{t.font_latin}; font-style:italic; font-size:7pt; }}
    .step-arrow {{ color:{p.accent}; margin:1px 0; text-align:right; padding-right:6px; font-size:8pt; }}

    /* ToC */
    .toc h2 {{ font-size:18pt; font-weight:{t.weights["black"]}; text-align:center; color:{p.primary_deep}; border-bottom:2px solid {p.primary}; padding-bottom:4px; }}
    .toc-subtitle {{ text-align:center; font-family:{t.font_latin}; font-style:italic; color:{p.accent}; margin-bottom:12px; font-size:{t.sizes["sm"]}; }}
    .toc ul {{ list-style:none; display:flex; flex-direction:column; gap:8px; padding:0; }}
    .toc-row {{ display:flex; align-items:center; gap:4px; font-size:{t.sizes["base"]}; }}
    .toc-badge {{ width:20px; height:20px; border-radius:50%; background:{p.primary}; color:{p.surface}; display:inline-flex; align-items:center; justify-content:center; font-size:{t.sizes["xs"]}; font-weight:{t.weights["bold"]}; flex-shrink:0; margin-inline-end:8px; }}
    .toc-title {{ display:flex; flex-direction:column; }}
    .toc-sub {{ font-family:{t.font_latin}; font-size:7pt; color:{p.muted}; font-style:italic; }}
    .toc-dots {{ flex:1; border-bottom:1px dotted {p.border}; margin:0 8px; height:1px; }}
    .toc-page {{ font-family:{t.font_latin}; font-weight:{t.weights["bold"]}; color:{p.primary}; }}

    /* Quotes */
    .quote {{ max-width:155mm; margin:auto; text-align:center; }}
    .quote-rule {{ display:block; width:45mm; height:2px; background:{p.accent}; margin:12px auto; }}
    .quote p {{ font-size:12pt; font-weight:{t.weights["bold"]}; line-height:1.7; }}
    .quote-sub {{ font-family:{t.font_latin}; font-style:italic; font-size:8pt; color:#cbd5e1; margin-top:6px; }}
    .quote-author {{ display:block; font-size:7.5pt; color:{p.muted}; margin-top:6px; }}

    .content-list {{ margin:4px 0; padding-inline-start:20px; line-height:1.6; font-size:{t.sizes["sm"]}; }}
    .content-group {{ display:flex; }}
    .group-column {{ flex-direction:column; }}
    .group-row {{ flex-direction:row; }}
    .group-row > * {{ flex:1; min-width:0; }}

    .justify-flex-start {{ justify-content:flex-start; }}
    .justify-center {{ justify-content:center; }}
    .justify-space-between {{ justify-content:space-between; }}
    .align-stretch {{ align-items:stretch; }}
    .align-start {{ align-items:flex-start; }}
    .align-end {{ align-items:flex-end; }}
    .align-center {{ align-items:center; }}

    .gap-xs {{ gap:{s.xs}; }}
    .gap-sm {{ gap:{s.sm}; }}
    .gap-md {{ gap:{s.md}; }}
    .gap-lg {{ gap:{s.lg}; }}

    .image-block {{ text-align:center; margin:{s.sm} 0; }}
    .image-block img {{ display:inline-block; height:auto; }}
    .image-block figcaption {{ color:{p.muted}; font-size:{t.sizes["xs"]}; margin-top:{s.xs}; }}

    .spacer-xs {{ height:{s.xs}; }}
    .spacer-sm {{ height:{s.sm}; }}
    .spacer-md {{ height:{s.md}; }}
    .spacer-lg {{ height:{s.lg}; }}
    .spacer-xl {{ height:{s.xl}; }}

    .running-footer {{
      display:flex;
      justify-content:space-between;
      gap:{s.sm};
      border-top:1px solid {p.border_light};
      padding-top:{s.xs};
      color:{p.muted};
      font-size:{t.sizes["xs"]};
      font-family:{t.font_latin};
      direction:ltr;
    }}
    .layout-dark .running-footer {{ border-color:rgba(255,255,255,.18); color:#cbd5e1; }}
    """


def footer_value(value: Any, page_number: int, page_count: int) -> str:
    return str(value).replace("{page}", str(page_number)).replace("{pages}", str(page_count))


def render_page(page: Mapping[str, Any], page_number: int, page_count: int, block_html: Mapping[str, str], artifact_html: Mapping[str, str]) -> str:
    page_token = str(page.get("id", page_number))
    content_parts: list[str] = []
    for index, block in enumerate(page.get("blocks", []), start=1):
        if block.get("type") == "artifact_ref":
            content_parts.append(artifact_html[block["artifact_id"]])
        else:
            content_parts.append(block_html[f"page-{page_token}-block-{index}"])

    footer_html = ""
    footer = page.get("footer")
    if isinstance(footer, Mapping):
        values = [footer_value(footer.get(key, ""), page_number, page_count) for key in ("left", "center", "right")]
        footer_html = '<footer class="running-footer">' + "".join(f"<span>{esc(value)}</span>" for value in values) + "</footer>"

    layout = esc(page.get("layout", "standard"))
    content = "".join(content_parts)
    if layout == "framed":
        return f'<main class="page-sheet layout-framed"><div class="page-frame"><div class="page-content">{content}</div>{footer_html}</div></main>'
    return f'<main class="page-sheet layout-{layout}"><div class="page-content">{content}</div>{footer_html}</main>'


def render(document: Mapping[str, Any], artifact_html: Mapping[str, str], block_html: Mapping[str, str], design: DesignSystem) -> str:
    direction = str(document.get("direction", "ltr"))
    language = esc(document.get("language", ""))
    title = esc(document.get("title", "Document"))
    pages = document["pages"]
    rendered_pages = [render_page(page, index, len(pages), block_html, artifact_html) for index, page in enumerate(pages, start=1)]
    return "<!doctype html>" + f'<html lang="{language}" dir="{esc(direction)}"><head><meta charset="utf-8"><title>{title}</title><style>{build_stylesheet(design, direction)}</style></head><body>{"".join(rendered_pages)}</body></html>'
