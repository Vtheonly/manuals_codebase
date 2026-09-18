"""
generators/html.py — Precision Document & Print Layout Engine
Produces exact, high-fidelity A4 pages matching the reference documents.
"""
from __future__ import annotations

import html
from collections.abc import Mapping
from typing import Any

from core.components import render_block
from core.design import DesignSystem


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def build_stylesheet(design: DesignSystem, direction: str) -> str:
    p = design.palette
    t = design.typography

    return f"""
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Inter:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      margin: 0;
      padding: 0;
    }}

    @page {{
      size: 210mm 297mm;
      margin: 0;
    }}

    @media print {{
      body {{
        background: transparent !important;
        margin: 0 !important;
      }}
      .page-sheet {{
        box-shadow: none !important;
        margin: 0 !important;
        break-after: page !important;
        page-break-after: always !important;
      }}
    }}

    body {{
      background: #475569;
      color: {p.text};
      font-family: 'Cairo', 'Segoe UI', Tahoma, sans-serif;
      direction: {esc(direction)};
      text-align: right;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    /* Standard A4 Container */
    .page-sheet {{
      width: 210mm;
      height: 297mm;
      max-height: 297mm;
      background: {p.surface};
      color: {p.text};
      padding: 13mm 15mm 10mm 15mm;
      margin-bottom: 24px;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 8px 24px rgba(0,0,0,0.18);
      overflow: hidden;
      box-sizing: border-box;
    }}

    .page-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    /* Cover Page Framing — Double Border Frame */
    .layout-framed {{
      padding: 8mm;
    }}

    .layout-framed .page-frame-outer {{
      height: 100%;
      border: 1px solid {p.primary};
      padding: 3.5mm;
      box-sizing: border-box;
    }}

    .layout-framed .page-frame {{
      height: 100%;
      border: 2px solid {p.primary};
      border-radius: 2px;
      padding: 10mm 12mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: stretch;
      box-sizing: border-box;
    }}

    /* Back Cover Dark Theme with Inner Gold Frame */
    .layout-dark {{
      background: {p.primary_deep};
      color: #ffffff;
      padding: 8mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-sizing: border-box;
    }}

    .layout-dark .dark-frame {{
      height: 100%;
      border: 1.5px solid {p.accent};
      padding: 14mm 16mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: stretch;
      text-align: center;
      box-sizing: border-box;
    }}

    .layout-dark .block-text,
    .layout-dark .quote {{ color: #ffffff; }}
    .layout-dark h1, .layout-dark h2, .layout-dark h3 {{ color: #ffffff; }}

    h1, h2, h3, h4, h5, h6, p, ul, ol, figure {{ margin: 0; }}

    /* Section Headings with Structured Sub-Label */
    .block-heading {{
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 6px;
    }}

    .block-heading .heading-content {{
      display: flex;
      flex-direction: column;
    }}

    .block-heading h2 {{
      font-size: 13pt;
      font-weight: 800;
      color: {p.primary_deep};
      margin: 0;
      line-height: 1.3;
    }}

    .circle-badge {{
      width: 25px;
      height: 25px;
      border-radius: 50%;
      background: {p.primary};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 8.5pt;
      font-family: 'Inter', sans-serif;
      flex-shrink: 0;
    }}

    .circle-badge.appendix-badge {{
      background: {p.accent} !important;
    }}

    .sub-label {{
      font-family: 'Inter', sans-serif;
      font-style: italic;
      font-size: 8pt;
      color: {p.muted};
      direction: ltr;
      text-align: right;
      margin-top: 1px;
    }}
    [dir="ltr"] .sub-label {{
      text-align: left;
    }}

    /* Subsections with Amber Vertical Accent Bar */
    .subsection-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      border-right: 4px solid {p.accent};
      padding-right: 8px;
      margin: 8px 0 4px 0;
    }}
    [dir="ltr"] .subsection-header {{
      border-right: none;
      border-left: 4px solid {p.accent};
      padding-right: 0;
      padding-left: 8px;
    }}
    .sub-title-primary {{
      font-size: 10.5pt;
      font-weight: 700;
      color: {p.primary_deep};
    }}
    .sub-title-secondary {{
      font-family: 'Inter', sans-serif;
      font-style: italic;
      font-size: 8pt;
      color: {p.muted};
      direction: ltr;
    }}

    /* Text Paragraphs */
    .block-text {{
      font-size: 9.5pt;
      line-height: 1.7;
      text-align: justify;
      color: {p.text};
      margin-bottom: 2px;
    }}
    .block-text p + p {{ margin-top: 6px; }}
    .align-left {{ text-align: left; }}
    .align-right {{ text-align: right; }}
    .align-center {{ text-align: center; }}
    .align-justify {{ text-align: justify; }}

    /* Badges */
    .badge-wrapper {{ margin: 5px 0; text-align: center; }}
    .badge {{
      display: inline-block;
      padding: 4px 18px;
      border-radius: 30px;
      font-size: 9pt;
      font-weight: 700;
    }}
    .badge-default, .badge-solid {{ background: {p.primary}; color: #ffffff; }}
    .badge-plain {{
      background: transparent;
      color: {p.text_dark};
      font-size: 11pt;
      font-weight: 700;
    }}
    .badge-dashed {{
      background: {p.surface_alt};
      color: {p.primary};
      border: 1.5px dashed {p.primary};
      border-radius: 20px;
      padding: 5px 22px;
      font-size: 9.5pt;
    }}
    .badge-gradient {{
      background: linear-gradient(135deg, {p.banner_start}, {p.banner_end});
      color: {p.banner_text};
      border: 1.5px solid {p.banner_border};
      padding: 6px 45px;
      border-radius: 6px;
      font-size: 11pt;
      font-weight: 800;
    }}

    /* Topic Gradient Card */
    .card {{
      border: 1.5px solid {p.banner_border};
      border-radius: 12px;
      padding: 16px 20px;
      margin: 8px 0;
      text-align: center;
      background: linear-gradient(135deg, {p.banner_start} 0%, {p.banner_end} 100%);
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }}
    .card-label {{ color: {p.banner_text}; font-weight: 700; font-size: 11pt; margin-bottom: 4px; }}
    .card-title {{ color: {p.banner_text}; font-size: 18pt; font-weight: 900; line-height: 1.3; margin-bottom: 4px; }}
    .card-subtitle {{ color: {p.primary}; font-style: italic; font-family: 'Inter', sans-serif; font-size: 9pt; margin-bottom: 8px; direction: ltr; }}
    .card-pill {{
      display: inline-block;
      margin-top: 4px;
      padding: 4px 18px;
      border-radius: 20px;
      background: #ffffff;
      color: {p.primary_deep};
      font-size: 8pt;
      font-weight: 700;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }}

    /* Trainee Info Card with 2-Column Exact Layout */
    .info-card {{
      border: 1.5px solid {p.border};
      border-radius: 12px;
      padding: 14px 22px;
      margin: 8px 0;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: {p.surface};
    }}
    .info-row {{
      display: flex;
      align-items: baseline;
      font-size: 10pt;
    }}
    .info-row.highlight .info-value {{
      color: {p.primary_deep};
      font-weight: 800;
    }}
    .info-label-cell {{
      display: flex;
      align-items: baseline;
      width: 190px;
      flex-shrink: 0;
      justify-content: space-between;
      padding-left: 12px;
    }}
    [dir="ltr"] .info-label-cell {{
      padding-left: 0;
      padding-right: 12px;
    }}
    .info-label {{
      font-weight: 700;
      color: {p.primary};
    }}
    .info-sep {{
      font-weight: 700;
      color: {p.primary};
      margin: 0 4px;
    }}
    .info-value {{
      flex: 1;
      font-weight: 500;
      color: {p.text};
      line-height: 1.4;
    }}

    /* Formula Block */
    .formula-box {{
      border-right: 4px solid {p.accent};
      border-radius: 4px;
      background: {p.accent_light};
      padding: 12px 18px;
      margin: 8px 0;
    }}
    [dir="ltr"] .formula-box {{
      border-right: none;
      border-left: 4px solid {p.accent};
    }}
    .formula-title {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 10pt;
      font-weight: 700;
      color: {p.accent};
      margin-bottom: 6px;
    }}
    .formula-icon-circle {{
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: {p.accent};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 8.5pt;
      font-family: {t.font_math};
    }}
    .formula-math {{
      text-align: center;
      font-family: {t.font_math};
      font-size: 15pt;
      font-weight: bold;
      color: {p.primary_deep};
      margin: 6px 0;
      direction: ltr;
      unicode-bidi: isolate;
    }}
    .formula-desc {{
      font-size: 8.5pt;
      line-height: 1.6;
      color: {p.text};
    }}

    /* Callouts */
    .callout {{
      border-right: 4px solid {p.accent};
      border-radius: 4px;
      background: {p.accent_light};
      padding: 10px 14px;
      margin: 8px 0;
    }}
    [dir="ltr"] .callout {{
      border-right: none;
      border-left: 4px solid {p.accent};
    }}
    .callout-primary {{
      border-color: {p.primary};
      background: {p.primary_light};
    }}
    .callout-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
      font-size: 10pt;
      margin-bottom: 4px;
      color: {p.accent};
    }}
    .callout-primary .callout-header {{ color: {p.primary_deep}; }}
    .callout-icon-circle {{
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: {p.accent};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 8pt;
      font-weight: 700;
      flex-shrink: 0;
    }}
    .callout-primary .callout-icon-circle {{ background: {p.primary}; }}
    .callout-content {{ font-size: 9pt; line-height: 1.6; }}

    /* Stat Cards */
    .stats-grid {{ display: grid; gap: 10px; margin: 10px 0; }}
    .cols-4 {{ grid-template-columns: repeat(4, 1fr); }}
    .cols-3 {{ grid-template-columns: repeat(3, 1fr); }}
    .cols-2 {{ grid-template-columns: repeat(2, 1fr); }}
    .stat-card {{
      border: 1px solid {p.border_light};
      border-radius: 6px;
      padding: 10px 8px;
      text-align: center;
      background: {p.surface};
    }}
    .stat-value {{
      font-size: 15pt;
      font-weight: 900;
      color: {p.primary_deep};
      font-family: {t.font_latin};
    }}
    .stat-label {{
      font-size: 8pt;
      font-weight: 700;
      color: {p.text};
      margin-top: 4px;
      line-height: 1.3;
    }}
    .stat-sub {{
      display: block;
      font-size: 6.5pt;
      color: {p.muted};
      font-style: italic;
      font-family: {t.font_latin};
      margin-top: 2px;
    }}

    /* Data Tables */
    .table-wrapper {{ margin: 8px 0; }}
    .standard-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 8.5pt;
      border: 1px solid {p.border};
    }}
    .standard-table th {{
      background: {p.primary};
      color: #ffffff;
      padding: 6px 10px;
      text-align: center;
      border: 1px solid {p.primary_deep};
      font-weight: 700;
    }}
    .standard-table th .th-sub {{
      display: block;
      color: #ffffff;
      font-style: italic;
      font-size: 7pt;
      font-weight: 400;
      opacity: 0.9;
    }}
    .standard-table td {{
      border: 1px solid {p.border_light};
      padding: 5px 10px;
      line-height: 1.4;
    }}
    .standard-table tbody tr:nth-child(even) {{ background: {p.surface_alt}; }}
    td.num {{ text-align: center; font-family: {t.font_latin}; font-weight: 700; }}
    td.txt {{ text-align: right; }}
    [dir="ltr"] td.txt {{ text-align: left; }}

    /* Two-Line Captions */
    .caption {{
      text-align: center;
      margin-top: 6px;
    }}
    .caption-main {{
      color: {p.primary};
      font-weight: 700;
      font-size: 8pt;
    }}
    .caption-sub {{
      font-family: {t.font_latin};
      font-style: italic;
      font-size: 7pt;
      color: {p.muted};
      margin-top: 1px;
    }}

    /* Flow Steps */
    .flow-steps {{
      border: 1px solid {p.border_light};
      background: {p.surface_alt};
      border-radius: 8px;
      padding: 12px 18px;
      margin: 8px 0;
    }}
    .step-node {{ display: flex; align-items: center; gap: 14px; }}
    .step-content {{ display: flex; flex-direction: column; }}
    .step-num {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: {p.primary};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 8.5pt;
      font-weight: 700;
      flex-shrink: 0;
      font-family: {t.font_latin};
    }}
    .step-title {{ font-weight: 700; font-size: 9pt; color: {p.text_dark}; }}
    .step-sub {{ color: {p.muted}; font-family: {t.font_latin}; font-style: italic; font-size: 7.5pt; margin-top: 1px; }}
    .step-arrow {{
      color: {p.accent};
      text-align: right;
      padding-right: 8px;
      font-size: 9pt;
      margin: 2px 0;
    }}
    [dir="ltr"] .step-arrow {{
      text-align: left;
      padding-right: 0;
      padding-left: 8px;
    }}

    /* Table of Contents - Spaced and Full Height */
    .toc {{
      display: flex;
      flex-direction: column;
      height: 100%;
    }}
    .toc h2 {{
      font-size: 20pt;
      font-weight: 900;
      text-align: center;
      color: {p.primary_deep};
      margin-bottom: 2px;
    }}
    .toc-subtitle {{
      text-align: center;
      font-family: {t.font_latin};
      font-style: italic;
      color: {p.accent};
      margin-bottom: 8px;
      font-size: 9pt;
    }}
    .toc-divider-line {{
      width: 100%;
      height: 2px;
      background: {p.primary};
      margin-bottom: 18px;
    }}
    .toc ul {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding: 0;
      flex: 1;
    }}
    .toc-row {{
      display: flex;
      align-items: center;
      font-size: 10pt;
    }}
    .toc-badge {{
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: {p.primary};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 8.5pt;
      font-weight: 700;
      flex-shrink: 0;
      margin-left: 10px;
      font-family: {t.font_latin};
    }}
    [dir="ltr"] .toc-badge {{
      margin-left: 0;
      margin-right: 10px;
    }}
    .appendix-badge {{ background: {p.accent} !important; }}
    .toc-title {{ display: flex; flex-direction: column; }}
    .toc-title strong {{ font-weight: 700; color: {p.text_dark}; }}
    .toc-sub {{ font-family: {t.font_latin}; font-size: 7.5pt; color: {p.muted}; font-style: italic; }}
    .toc-dots {{ flex: 1; border-bottom: 1px dotted {p.border}; margin: 0 10px; height: 1px; }}
    .toc-page {{ font-family: {t.font_latin}; font-weight: 700; color: {p.primary}; font-size: 10pt; }}

    /* Quotes */
    .quote {{ max-width: 160mm; margin: auto; text-align: center; }}
    .quote-rule {{ display: block; width: 45mm; height: 2px; background: {p.accent}; margin: 12px auto; }}
    .quote p {{ font-size: 12.5pt; font-weight: 700; line-height: 1.75; color: {p.text_dark}; }}
    .layout-dark .quote p {{ color: #f8fafc; }}
    .quote-sub {{ font-family: {t.font_latin}; font-style: italic; font-size: 8.5pt; color: {p.muted}; margin-top: 6px; }}
    .layout-dark .quote-sub {{ color: #cbd5e1; }}
    .quote-author {{ display: block; font-size: 8pt; color: {p.muted}; margin-top: 8px; }}

    /* Lists */
    .content-list {{ margin: 6px 0; padding-right: 22px; line-height: 1.65; font-size: 9pt; }}
    [dir="ltr"] .content-list {{ padding-right: 0; padding-left: 22px; }}

    /* Structured Card Lists */
    .list-cards {{
      list-style: none;
      padding: 0 !important;
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin: 6px 0;
    }}
    .list-item-card {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border: 1px solid {p.border_light};
      border-radius: 4px;
      background: {p.surface};
      padding: 6px 12px;
      gap: 10px;
    }}
    .list-item-badge {{
      font-size: 8.5pt;
      font-weight: 700;
      color: {p.muted};
      flex-shrink: 0;
      width: 16px;
      text-align: center;
    }}
    .list-item-content {{
      flex: 1;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }}
    .list-item-title {{
      font-size: 8pt;
      font-weight: 600;
      color: {p.text_dark};
      line-height: 1.35;
    }}
    .list-item-tag {{
      font-family: {t.font_latin};
      font-size: 7pt;
      color: {p.muted};
      white-space: nowrap;
      flex-shrink: 0;
    }}

    /* Layout Spacers */
    .spacer-sm {{ height: 8px; }}
    .spacer-md {{ height: 14px; }}
    .spacer-lg {{ height: 22px; }}

    /* Vector Chart Container */
    .chart-container {{
      margin: 8px 0;
      padding: 10px 14px;
      border: 1px solid {p.border_light};
      border-radius: 8px;
      background: #ffffff;
    }}
    .chart-header {{ text-align: center; margin-bottom: 6px; }}
    .chart-header h4 {{ font-size: 10.5pt; font-weight: 700; color: {p.primary_deep}; }}
    .chart-header .chart-subtitle {{ font-family: {t.font_latin}; font-style: italic; font-size: 8pt; color: {p.muted}; margin-top: 1px; }}
    .svg-viewport {{ width: 100%; max-height: 250px; display: block; margin: 0 auto; }}

    /* Running Footer: Left - Center - Right */
    .running-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid {p.border_light};
      padding-top: 6px;
      font-size: 8pt;
      color: {p.muted};
      font-family: {t.font_latin};
      direction: ltr !important;
      unicode-bidi: isolate;
    }}
    .footer-left {{ text-align: left; }}
    .footer-center {{ font-weight: 700; color: {p.text_dark}; font-size: 8.5pt; text-align: center; }}
    .footer-right {{ text-align: right; }}
    """


def render_page(
    page: Mapping[str, Any],
    page_number: int,
    page_count: int,
    block_html: Mapping[str, str],
    artifact_html: Mapping[str, str],
) -> str:
    page_token = str(page.get("id", page_number))
    content_parts = []
    for index, block in enumerate(page.get("blocks", []), start=1):
        if block.get("type") == "artifact_ref":
            content_parts.append(artifact_html[block["artifact_id"]])
        else:
            content_parts.append(block_html[f"page-{page_token}-block-{index}"])

    footer_html = ""
    footer = page.get("footer")
    if isinstance(footer, Mapping):
        left = str(footer.get("left", "")).replace("{page}", str(page_number)).replace("{pages}", str(page_count))
        center = str(footer.get("center", "")).replace("{page}", str(page_number)).replace("{pages}", str(page_count))
        right = str(footer.get("right", "")).replace("{page}", str(page_number)).replace("{pages}", str(page_count))
        footer_html = (
            f'<footer class="running-footer">'
            f'<span class="footer-left">{esc(left)}</span>'
            f'<span class="footer-center">{esc(center)}</span>'
            f'<span class="footer-right">{esc(right)}</span>'
            f'</footer>'
        )

    layout = page.get("layout", "standard")
    content = "".join(content_parts)

    if layout == "framed":
        return (
            f'<main class="page-sheet layout-framed">'
            f'<div class="page-frame-outer"><div class="page-frame">{content}</div></div>'
            f'</main>'
        )
    if layout == "dark":
        return (
            f'<main class="page-sheet layout-dark">'
            f'<div class="dark-frame">{content}</div>'
            f'</main>'
        )
    return (
        f'<main class="page-sheet layout-{layout}">'
        f'<div class="page-content">{content}</div>{footer_html}'
        f'</main>'
    )


def render(
    document: Mapping[str, Any],
    artifact_html: Mapping[str, str],
    block_html: Mapping[str, str],
    design: DesignSystem,
) -> str:
    direction = str(document.get("direction", "rtl"))
    language = esc(document.get("language", "ar"))
    title = esc(document.get("title", "Document"))
    pages = document["pages"]
    rendered_pages = [
        render_page(page, index, len(pages), block_html, artifact_html)
        for index, page in enumerate(pages, start=1)
    ]
    return (
        f'<!doctype html><html lang="{language}" dir="{direction}">'
        f'<head><meta charset="utf-8"><title>{title}</title>'
        f'<style>{build_stylesheet(design, direction)}</style></head>'
        f'<body>{"".join(rendered_pages)}</body></html>'
    )