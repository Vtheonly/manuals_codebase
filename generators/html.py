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
    *, *::before, *::after {{ box-sizing:border-box; }}
    html, body {{ margin:0; padding:0; }}
    @page {{ size:{design.page.width} {design.page.height}; margin:0; }}
    @media print {{
      body {{ background:transparent !important; }}
      .page-sheet {{ box-shadow:none !important; margin:0 !important; break-after:page; page-break-after:always; }}
    }}
    body {{
      background:{p.surface_alt}; color:{p.text}; font-family:{t.primary};
      direction:{esc(direction)}; text-align:{align_default};
      -webkit-print-color-adjust:exact; print-color-adjust:exact;
      display:flex; flex-direction:column; align-items:center;
    }}
    .page-sheet {{
      width:{design.page.width}; height:{design.page.height};
      background:{p.surface}; color:{p.text}; padding:{s.page_y} {s.page_x};
      margin-bottom:20px; position:relative; display:flex; flex-direction:column;
      gap:{s.md}; box-shadow:0 4px 18px rgba(0,0,0,.08); overflow:hidden;
    }}
    .page-content {{ flex:1; min-height:0; }}
    .layout-framed {{ padding:8mm; }}
    .layout-framed .page-frame {{
      height:100%; border:{b.thick} solid {p.primary}; border-radius:{b.radius_sm};
      padding:{s.frame_padding}; overflow:hidden; display:flex; flex-direction:column; gap:{s.md};
    }}
    .layout-dark {{ background:{p.primary_deep}; color:{p.surface}; }}
    .layout-dark .block-text, .layout-dark .quote {{ color:{p.surface}; }}
    .layout-dark .block-heading h1, .layout-dark .block-heading h2, .layout-dark .block-heading h3,
    .layout-dark .block-heading h4, .layout-dark .block-heading h5, .layout-dark .block-heading h6 {{ color:{p.surface}; }}
    h1,h2,h3,h4,h5,h6,p,ul,ol,figure {{ margin:0; }}
    .block-heading {{ display:flex; align-items:center; gap:{s.sm}; border-bottom:2px solid {p.primary}; padding-bottom:{s.xs}; margin-bottom:{s.sm}; }}
    .block-heading h1 {{ font-size:{t.sizes["3xl"]}; }} .block-heading h2 {{ font-size:{t.sizes["2xl"]}; }}
    .block-heading h3 {{ font-size:{t.sizes["xl"]}; }} .block-heading h4 {{ font-size:{t.sizes["lg"]}; }}
    .block-heading h5,.block-heading h6 {{ font-size:{t.sizes["md"]}; }}
    .circle-badge {{ width:26px; height:26px; flex:0 0 26px; border-radius:50%; background:{p.primary}; color:{p.surface}; display:inline-flex; align-items:center; justify-content:center; font-weight:{t.weights["bold"]}; }}
    .sub-label {{ display:block; color:{p.accent}; font-family:{t.secondary}; font-style:italic; font-size:{t.sizes["xs"]}; margin-top:2px; }}
    .block-text {{ font-size:{t.sizes["base"]}; line-height:{t.line_height["normal"]}; margin-bottom:{s.sm}; }}
    .align-left {{ text-align:left; }} .align-right {{ text-align:right; }} .align-center {{ text-align:center; }} .align-justify {{ text-align:justify; }}
    .badge-wrapper {{ margin:{s.sm} 0; }} .badge {{ display:inline-block; padding:4px 16px; border-radius:{b.pill}; font-size:{t.sizes["sm"]}; font-weight:{t.weights["bold"]}; }}
    .badge-default,.badge-solid {{ background:{p.primary}; color:{p.surface}; }} .badge-dashed {{ background:{p.surface_alt}; color:{p.primary}; border:1px dashed {p.primary}; }}
    .badge-gradient {{ background:linear-gradient(135deg,{p.banner_start},{p.banner_end}); color:{p.banner_text}; border:1px solid {p.banner_border}; }}
    .card {{ border:1px solid {p.border}; border-radius:{b.radius_lg}; padding:{s.card}; margin:{s.sm} 0; background:linear-gradient(135deg,{p.primary_light},{p.surface}); }}
    .card-label {{ color:{p.accent}; font-weight:{t.weights["bold"]}; font-size:{t.sizes["sm"]}; }} .card-title {{ color:{p.primary_deep}; font-size:{t.sizes["2xl"]}; font-weight:{t.weights["black"]}; }}
    .card-subtitle {{ color:{p.muted}; font-style:italic; font-family:{t.secondary}; font-size:{t.sizes["sm"]}; }} .card-content {{ margin-top:{s.sm}; line-height:{t.line_height["normal"]}; }}
    .card-pill {{ display:inline-block; margin-top:{s.sm}; padding:3px 12px; border-radius:{b.pill}; background:{p.surface}; color:{p.primary_deep}; border:1px solid {p.border_light}; font-size:{t.sizes["xs"]}; }}
    .info-card {{ border:1px solid {p.border}; border-radius:{b.radius_lg}; padding:{s.md}; margin:{s.sm} 0; }} .info-row {{ display:flex; gap:{s.xs}; align-items:baseline; padding:4px 0; font-size:{t.sizes["base"]}; }}
    .info-label {{ min-width:28%; font-weight:{t.weights["bold"]}; color:{p.primary}; }} .info-sep {{ color:{p.primary}; font-weight:{t.weights["bold"]}; }} .info-value {{ flex:1; }} .info-row.highlight .info-value {{ color:{p.primary_deep}; font-weight:{t.weights["heavy"]}; }}
    .callout {{ border-inline-end:4px solid {p.accent}; border-radius:{b.radius_md}; background:{p.accent_light}; padding:{s.sm} {s.md}; margin:{s.sm} 0; }} .callout-primary {{ border-color:{p.primary}; background:{p.primary_light}; }} .callout-warning {{ border-color:{p.accent}; }} .callout-neutral {{ border-color:{p.border}; background:{p.surface_alt}; }}
    .callout-header {{ display:flex; align-items:center; gap:{s.xs}; margin-bottom:{s.xs}; }} .callout-icon {{ color:{p.accent}; }} .callout-content {{ line-height:{t.line_height["normal"]}; font-size:{t.sizes["sm"]}; }}
    .stats-grid {{ display:grid; gap:{s.gap}; margin:{s.sm} 0; }} .cols-1 {{ grid-template-columns:repeat(1,1fr); }} .cols-2 {{ grid-template-columns:repeat(2,1fr); }} .cols-3 {{ grid-template-columns:repeat(3,1fr); }} .cols-4 {{ grid-template-columns:repeat(4,1fr); }} .cols-5 {{ grid-template-columns:repeat(5,1fr); }} .cols-6 {{ grid-template-columns:repeat(6,1fr); }}
    .stat-card {{ border:1px solid {p.border_light}; border-top:3px solid {p.accent}; border-radius:{b.radius_sm}; padding:{s.sm}; text-align:center; background:{p.surface}; }} .stat-value {{ font-size:{t.sizes["xl"]}; font-weight:{t.weights["black"]}; color:{p.primary_deep}; font-family:{t.secondary}; }} .stat-label {{ font-size:{t.sizes["xs"]}; font-weight:{t.weights["bold"]}; }} .stat-sub {{ display:block; margin-top:2px; font-size:6.5pt; color:{p.muted}; font-style:italic; }}
    .table-wrapper {{ margin:{s.sm} 0; }} .table-header {{ display:flex; gap:{s.xs}; align-items:baseline; border-inline-end:4px solid {p.accent}; padding-inline-end:{s.xs}; margin-bottom:{s.xs}; }} .table-header h4 {{ color:{p.primary_deep}; }} .table-header span {{ color:{p.muted}; font-size:{t.sizes["xs"]}; }}
    .standard-table {{ width:100%; border-collapse:collapse; font-size:{t.sizes["sm"]}; }} .standard-table th {{ background:{p.primary}; color:{p.surface}; border:1px solid {p.primary_deep}; padding:{s.cell}; text-align:inherit; }} .standard-table td {{ border:1px solid {p.border_light}; padding:{s.cell}; }} .standard-table tbody tr:nth-child(even) {{ background:{p.surface_alt}; }}
    .standard-table td.num {{ text-align:center; font-family:{t.secondary}; font-weight:{t.weights["bold"]}; }} .th-sub,.td-sub {{ display:block; color:{p.muted}; font-style:italic; font-size:7pt; }} .caption {{ text-align:center; color:{p.muted}; font-size:{t.sizes["xs"]}; margin-top:{s.xs}; }}
    .flow-steps {{ border:1px solid {p.border_light}; background:{p.surface_alt}; border-radius:{b.radius_md}; padding:{s.md}; }} .flow-title {{ font-weight:{t.weights["bold"]}; color:{p.primary_deep}; margin-bottom:{s.sm}; }}
    .step-node {{ display:flex; align-items:center; gap:{s.sm}; }} .step-num {{ width:24px; height:24px; border-radius:50%; background:{p.primary}; color:{p.surface}; display:inline-flex; align-items:center; justify-content:center; font-size:{t.sizes["xs"]}; font-weight:{t.weights["bold"]}; flex:0 0 24px; }} .step-title {{ font-weight:{t.weights["bold"]}; font-size:{t.sizes["sm"]}; }} .step-sub {{ color:{p.muted}; font-family:{t.secondary}; font-style:italic; font-size:7.5pt; }} .step-arrow {{ color:{p.accent}; margin:2px 0; }}
    .toc {{ margin:{s.md} 0; }} .toc h2 {{ color:{p.primary_deep}; text-align:center; font-size:{t.sizes["2xl"]}; }} .toc-subtitle {{ text-align:center; color:{p.accent}; font-style:italic; margin-bottom:{s.md}; }} .toc ul {{ list-style:none; padding:0; display:flex; flex-direction:column; gap:{s.sm}; }} .toc-row {{ display:flex; align-items:center; gap:{s.xs}; }} .toc-badge {{ width:22px; height:22px; flex:0 0 22px; border-radius:50%; background:{p.primary}; color:{p.surface}; display:inline-flex; align-items:center; justify-content:center; font-size:{t.sizes["xs"]}; font-weight:{t.weights["bold"]}; }} .toc-title {{ display:flex; flex-direction:column; }} .toc-sub {{ color:{p.muted}; font-size:7.5pt; font-style:italic; }} .toc-dots {{ flex:1; border-bottom:1px dotted {p.border}; }} .toc-page {{ font-family:{t.secondary}; font-weight:{t.weights["bold"]}; color:{p.primary}; }}
    .quote {{ max-width:165mm; margin:{s.xl} auto; text-align:center; }} .quote-rule {{ display:block; width:45mm; height:2px; background:{p.accent}; margin:{s.md} auto; }} .quote p {{ font-size:{t.sizes["lg"]}; font-weight:{t.weights["bold"]}; line-height:{t.line_height["relaxed"]}; }} .quote-author {{ display:block; margin-top:{s.sm}; color:{p.muted}; font-size:{t.sizes["xs"]}; }}
    .content-list {{ margin:{s.sm} 0; padding-inline-start:1.5em; line-height:{t.line_height["normal"]}; }} .content-group {{ display:flex; }} .group-column {{ flex-direction:column; }} .group-row {{ flex-direction:row; }} .group-row > * {{ flex:1; min-width:0; }}
    .justify-flex-start {{ justify-content:flex-start; }} .justify-center {{ justify-content:center; }} .justify-space-between {{ justify-content:space-between; }} .align-stretch {{ align-items:stretch; }} .align-start {{ align-items:flex-start; }} .align-end {{ align-items:flex-end; }} .align-center {{ align-items:center; }}
    .gap-xs {{ gap:{s.xs}; }} .gap-sm {{ gap:{s.sm}; }} .gap-md {{ gap:{s.md}; }} .gap-lg {{ gap:{s.lg}; }} .image-block {{ text-align:center; margin:{s.sm} 0; }} .image-block img {{ display:inline-block; height:auto; }} .image-block figcaption {{ color:{p.muted}; font-size:{t.sizes["xs"]}; margin-top:{s.xs}; }}
    .spacer-xs {{ height:{s.xs}; }} .spacer-sm {{ height:{s.sm}; }} .spacer-md {{ height:{s.md}; }} .spacer-lg {{ height:{s.lg}; }} .spacer-xl {{ height:{s.xl}; }}
    .running-footer {{ display:flex; justify-content:space-between; gap:{s.sm}; border-top:1px solid {p.border_light}; padding-top:{s.xs}; color:{p.muted}; font-size:{t.sizes["xs"]}; }}
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
