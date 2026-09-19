"""
generators/html.py — Precision Document & Print Layout Engine
Produces exact, high-fidelity A4 pages driven entirely by DesignSystem tokens.

Fonts are resolved through local @font-face declarations pointing at the
bundled `assets/fonts` directory (copied next to the output by the compiler),
so rendering is deterministic and identical across machines and PDF backends.
"""
from __future__ import annotations

import html
from collections.abc import Mapping
from typing import Any

from core.components import render_block
from core.design import DesignSystem
from core.text import fmt


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


# Bundled font faces: family -> list of (weight, style, filename)
FONT_FACES: dict[str, list[tuple[str, str, str]]] = {
    "Noto Kufi Arabic": [
        ("400", "normal", "NotoKufiArabic-400.ttf"),
        ("600", "normal", "NotoKufiArabic-600.ttf"),
        ("700", "normal", "NotoKufiArabic-700.ttf"),
        ("800", "normal", "NotoKufiArabic-800.ttf"),
        ("900", "normal", "NotoKufiArabic-900.ttf"),
    ],
    "Arimo": [
        ("400", "normal", "Arimo-400.ttf"),
        ("700", "normal", "Arimo-700.ttf"),
        ("400", "italic", "Arimo-Italic-400.ttf"),
        ("700", "italic", "Arimo-Italic-700.ttf"),
    ],
    "Amiri": [
        ("400", "normal", "Amiri-400.ttf"),
        ("700", "normal", "Amiri-700.ttf"),
    ],
    "Tinos": [
        ("400", "normal", "Tinos-400.ttf"),
        ("700", "normal", "Tinos-700.ttf"),
        ("400", "italic", "Tinos-Italic-400.ttf"),
        ("700", "italic", "Tinos-Italic-700.ttf"),
    ],
    "Noto Sans Arabic UI": [
        ("400", "normal", "NotoSansArabicUI-400.ttf"),
        ("700", "normal", "NotoSansArabicUI-700.ttf"),
    ],
}


def build_font_faces(base_path: str = "fonts") -> str:
    """Emit @font-face rules for every bundled font."""
    rules = []
    for family, faces in FONT_FACES.items():
        for weight, style, filename in faces:
            rules.append(
                f"@font-face {{ font-family: '{family}'; font-style: {style}; "
                f"font-weight: {weight}; font-display: block; "
                f"src: local('{family}'), url('{base_path}/{filename}') format('truetype'); }}"
            )
    return "\n    ".join(rules)


def build_stylesheet(design: DesignSystem, direction: str) -> str:
    p = design.palette
    t = design.typography
    s = design.spacing
    b = design.borders
    fonts = t.families

    return f"""
    {build_font_faces()}

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
      size: {design.page.width} {design.page.height};
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
      /* The final sheet must not spill an empty trailing page. */
      .page-sheet:last-child {{
        break-after: auto !important;
        page-break-after: auto !important;
      }}
      /* Atomic components never split across PDF page boundaries. */
      .card, .callout, .formula-container, .info-card, .table-wrapper,
      .chart-container, .flow-steps, .stats-grid, .quote, .toc,
      .content-list, .artifact {{ break-inside: avoid; }}
      /* Section introductions stay with at least one following block. */
      .heading-block, .subsection-header {{
        break-inside: avoid;
        break-after: avoid;
      }}
    }}

    body {{
      background: #475569;
      color: {p.text};
      font-family: {fonts['arabic']};
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
      width: {design.page.width};
      height: {design.page.height};
      min-height: {design.page.height};
      max-height: {design.page.height};
      background: {p.surface};
      color: {p.text};
      padding: {s.page_y} {s.page_x} 9mm {s.page_x};
      margin-bottom: 24px;
      position: relative;
      display: flex;
      flex-direction: column;
      box-shadow: 0 8px 24px rgba(0,0,0,0.18);
      overflow: hidden;
    }}

    .page-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 9.5pt;
      min-height: 0;
    }}

    /* ============ Decorative Dividers (generic rule component) ============ */
    .divider {{
      border: none;
      background: none;
      height: 0;
    }}
    .divider-margin-sm {{ margin: 3pt 0; }}
    .divider-margin-md {{ margin: 5pt 0 7pt 0; }}
    .divider-margin-lg {{ margin: 10pt 0 12pt 0; }}
    .divider-width-full {{ width: 100%; align-self: stretch; }}
    .divider-width-content {{ width: 100%; }}
    .divider-width-sub {{ width: 96pt; }}
    .divider-thickness-thin {{ --rule: 0.75pt; }}
    .divider-thickness-medium {{ --rule: 1pt; }}
    .divider-thickness-thick {{ --rule: 1.5pt; }}
    .divider-thickness-heavy {{ --rule: 2.25pt; }}
    .divider-solid {{ border-top: var(--rule) solid currentColor; }}
    .divider-dotted {{ border-top: 2pt dotted currentColor; }}
    .divider-double {{ border-top: var(--rule) double currentColor; }}
    .divider-gradient {{ height: var(--rule, 1.5pt); border: none; }}
    /* Compound section rule: full-width primary line with a gold segment at
       the logical start side (used under section headings). */
    .divider-section {{
      border: none;
      height: 1.5pt;
      background: {p.primary};
      position: relative;
    }}
    .divider-section::after {{
      content: '';
      position: absolute;
      top: 0;
      inset-inline-start: 0;
      width: {b.rule_overlay};
      height: 1.5pt;
      background: {p.accent};
    }}

    /* Cover Page Framing — Heavy Outer + Light Inner Frame */
    .layout-framed {{
      padding: 11.5mm;
    }}

    .layout-framed .page-frame-outer {{
      height: 100%;
      border: 2.25pt solid {p.primary};
      padding: 2.9mm;
      box-sizing: border-box;
    }}

    .layout-framed .page-frame {{
      height: 100%;
      border: 0.75pt solid {p.frame_inner};
      padding: 5.65mm;
      display: flex;
      flex-direction: column;
      align-items: stretch;
      box-sizing: border-box;
      text-align: center;
    }}

    /* Back Cover Dark Theme with Inner Gold Frame */
    .layout-dark {{
      background: {p.back_cover};
      color: #ffffff;
      padding: 9mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-sizing: border-box;
    }}

    .layout-dark .dark-frame {{
      height: 100%;
      border: 0.75pt solid {p.back_frame};
      padding: 18mm 16mm;
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

    /* ============ Section Headings with Gold Sub-Label and Rule ============ */
    /* Wrapper keeps heading + rule as one atomic layout child for measured
       pagination. */
    .heading-block {{ display: block; }}
    .block-heading {{
      display: flex;
      align-items: flex-start;
      gap: 8pt;
      margin-bottom: 4pt;
      margin-top: 2pt;
    }}

    .block-heading .heading-content {{
      display: flex;
      flex-direction: column;
      flex: 1;
    }}

    .block-heading h2 {{
      font-size: 13.5pt;
      font-weight: 800;
      color: {p.text_dark};
      margin: 0;
      line-height: 1.32;
    }}

    /* Circular glyph badges: leading neutralized, script-primary font stack,
       flex-centered so ascenders/descenders optically center in the circle. */
    .circle-badge {{
      width: 22.5pt;
      height: 22.5pt;
      border-radius: 50%;
      background: {p.primary};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 10.5pt;
      line-height: 1;
      padding: 0;
      font-family: {fonts['badge']};
      flex-shrink: 0;
    }}

    .circle-badge.appendix-badge {{
      background: {p.accent} !important;
    }}

    .sub-label {{
      font-family: {fonts['latin']};
      font-style: italic;
      font-size: 9pt;
      color: {p.accent_text};
      unicode-bidi: isolate;
      text-align: start;
      display: block;
      margin-top: 2.5pt;
    }}

    .block-heading + .divider-section {{
      margin-top: 4pt;
    }}

    /* ============ Subsections with configurable accent ============ */
    .subsection-header {{
      display: flex;
      align-items: center;
      gap: 8pt;
      position: relative;
      margin: 8pt 0 5pt 0;
      min-height: 17pt;
    }}
    /* The accent bar is an independent flex element separated from the text
       node by the enforced header gap: bar ink and glyph ink can never share
       coordinate space, whatever the script's sidebearings. */
    .subsection-bar {{
      display: block;
      width: 2.25pt;
      height: 16.5pt;
      min-width: 2.25pt;
      border-radius: 1.125pt;
      background: var(--subsection-accent, {p.accent});
      flex-shrink: 0;
      align-self: center;
    }}
    .subsection-header.sub-accent-rule {{
      border-bottom: 0.75pt solid {p.divider_strong};
      padding-bottom: 5.5pt;
    }}
    .sub-title-primary {{
      font-size: 11.5pt;
      font-weight: 700;
      color: {p.primary};
      line-height: 1.4;
    }}
    .sub-title-secondary {{
      font-family: {fonts['latin']};
      font-style: italic;
      font-size: 9pt;
      color: {p.muted};
      unicode-bidi: isolate;
      white-space: nowrap;
    }}
    .sub-dash {{
      font-family: {fonts['latin']};
      font-weight: 400;
      color: {p.muted};
      margin-inline: 5pt 4pt;
    }}

    /* ============ Text Paragraphs ============ */
    .block-text {{
      font-size: 10.5pt;
      line-height: 1.88;
      text-align: justify;
      color: {p.text};
      margin-bottom: 2pt;
    }}
    .block-text.lead-normal {{ line-height: 1.65; }}
    .block-text.lead-relaxed {{ line-height: 1.75; }}
    .block-text p + p {{ margin-top: 5pt; }}
    .block-text strong {{ color: {p.text_dark}; font-weight: 700; }}
    /* Inline pill badge used inside flowing text */
    .inline-pill {{
      display: inline-block;
      background: {p.primary_light};
      border: 0.75pt solid {p.divider_strong};
      border-radius: 8pt;
      padding: 0.5pt 6pt;
      font-size: 8pt;
      font-weight: 700;
      color: {p.text_dark};
      font-family: {fonts['latin']};
      white-space: nowrap;
      vertical-align: baseline;
    }}
    .align-left {{ text-align: left; }}
    .align-right {{ text-align: right; }}
    .align-center {{ text-align: center; }}
    .align-justify {{ text-align: justify; }}

    /* ============ Badges ============ */
    .badge-wrapper {{ margin: 5pt 0; text-align: center; }}
    .badge {{
      display: inline-block;
      padding: 4pt 18pt;
      border-radius: 30pt;
      font-size: 9pt;
      font-weight: 700;
      line-height: 1.5;
    }}
    .badge.size-lg {{ font-size: 11.5pt; padding: 5pt 22pt; }}
    .badge-default, .badge-solid {{ background: {p.primary}; color: #ffffff; }}
    .badge-plain {{
      background: transparent;
      color: {p.text_dark};
      font-size: 12.5pt;
      font-weight: 700;
    }}
    .badge-dashed {{
      background: #f8fafc;
      color: {p.primary};
      border: 1pt dashed {p.banner_border};
      border-radius: 14pt;
      padding: 5pt 20pt;
      font-size: 10pt;
    }}
    .badge-gradient {{
      background: linear-gradient(135deg, {p.banner_start} 0%, {p.banner_end} 100%);
      color: {p.banner_text};
      padding: 6pt 26pt;
      border-radius: 6pt;
      font-size: 10pt;
      font-weight: 800;
    }}
    .badge-pill {{
      background: linear-gradient(135deg, {p.banner_start} 0%, {p.banner_end} 100%);
      color: {p.banner_text};
      padding: 5pt 22pt;
      border-radius: 999pt;
      border: 0.75pt solid {p.frame_inner};
      font-size: 12pt;
      font-weight: 800;
    }}

    /* ============ Topic Banner Card (light gradient, dark text) ============ */
    .card {{
      border-radius: 8pt;
      padding: 14pt 18pt;
      margin: 8pt auto;
      width: 100%;
      text-align: center;
      background: linear-gradient(135deg, {p.banner_start} 0%, {p.banner_end} 100%);
      box-shadow: 0 2pt 6pt rgba(0,0,0,0.06);
      color: {p.banner_text};
    }}
    .card-label {{ color: {p.banner_text}; font-weight: 700; font-size: 11.5pt; margin-bottom: 3pt; }}
    .card-title {{ color: {p.banner_text}; font-size: 15.5pt; font-weight: 900; line-height: 1.5; margin-bottom: 2pt; }}
    .card-subtitle {{ color: {p.primary_deep}; font-style: italic; font-family: {fonts['latin']}; font-size: 10pt; margin-bottom: 8pt; direction: ltr; }}
    .card-pill {{
      display: inline-block;
      padding: 3pt 14pt;
      border-radius: 999pt;
      background: #ffffff;
      border: 0.75pt solid {p.banner_border};
      color: {p.text_dark};
      font-size: 8.5pt;
      font-weight: 700;
      font-family: {fonts['latin']};
      box-shadow: 0 1pt 2pt rgba(0,0,0,0.05);
    }}
    .card-content {{ color: {p.banner_text}; font-size: 9.5pt; margin-top: 4pt; }}

    /* ============ Info Card ============ */
    .info-card {{
      border: 0.75pt solid {p.muted_light};
      border-radius: 10pt;
      padding: 12pt 16pt;
      margin: 8pt auto;
      width: 100%;
      background: {p.surface};
    }}
    .info-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: start;
    }}
    .info-row td {{
      padding: 4.5pt 0;
      font-size: 11pt;
      vertical-align: baseline;
    }}
    /* Intrinsic sizing: the label column shrink-wraps to its content so a
       label of any length stays on one line and never splits across cells. */
    .info-label {{
      width: 1%;
      white-space: nowrap;
      font-weight: 700;
      color: {p.text_dark};
    }}
    .info-sep {{
      width: 1%;
      white-space: nowrap;
      text-align: center;
      font-weight: 700;
      color: {p.primary};
      font-family: {fonts['latin']};
      padding: 0 2pt;
    }}
    .info-value {{
      font-weight: 600;
      color: {p.text};
      line-height: 1.75;
      padding-inline-start: 6pt;
    }}
    .info-row.highlight .info-value {{
      color: {p.text_dark};
      font-weight: 800;
    }}

    /* ============ Formula Block (gold theme) ============ */
    .formula-container {{
      border: none;
      border-inline-start: 4.5pt solid {p.accent};
      border-radius: 0;
      background: {p.accent_light};
      padding: 10pt 12pt;
      margin: 10pt 0;
      text-align: center;
    }}
    .formula-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6pt;
      color: {p.accent_text};
      font-size: 10.5pt;
      font-weight: 700;
      margin-bottom: 6pt;
    }}
    .formula-icon-circle {{
      width: 17.25pt;
      height: 17.25pt;
      border-radius: 50%;
      background: {p.accent};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
      padding: 0;
      flex-shrink: 0;
    }}
    .formula-math {{
      text-align: center;
      font-family: {fonts['math']};
      font-size: 13pt;
      font-weight: 700;
      color: {p.text_dark};
      margin: 6pt 0;
      direction: ltr;
      unicode-bidi: isolate;
    }}
    .formula-math sub, .formula-math sup {{ font-size: 68%; }}
    .formula-desc {{
      font-size: 10pt;
      line-height: 1.85;
      color: {p.text};
      text-align: justify;
    }}

    /* ============ Callouts (gold theme) ============ */
    .callout {{
      background: {p.accent_light};
      border: none;
      border-inline-start: 4.5pt solid {p.accent};
      padding: 10pt 12pt;
      margin: 10pt 0;
      font-size: 10pt;
      line-height: 1.85;
    }}
    .callout-primary {{
      background: {p.primary_light};
      border-inline-start-color: {p.primary};
    }}
    .callout-primary .callout-header {{ color: {p.text_dark}; }}
    .callout-header {{
      display: flex;
      align-items: center;
      gap: 6pt;
      font-weight: 700;
      font-size: 10.5pt;
      margin-bottom: 4pt;
      color: {p.accent_text};
    }}
    .callout-icon-circle {{
      width: 17.25pt;
      height: 17.25pt;
      border-radius: 50%;
      background: {p.accent};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
      padding: 0;
      flex-shrink: 0;
    }}
    .ui-icon {{ display: block; }}
    .callout-primary .callout-icon-circle {{ background: {p.primary}; }}
    .callout-content {{ font-size: 10pt; line-height: 1.85; color: {p.text}; }}

    /* ============ Stat Cards (gold top accent) ============ */
    .stats-grid {{
      display: flex;
      justify-content: space-between;
      gap: 8pt;
      margin: 12pt 0;
    }}
    .stat-card {{
      flex: 1 1 0;
      background: {p.surface};
      border: 0.75pt solid {p.border};
      border-top: 2.25pt solid {p.accent};
      border-radius: 6pt;
      padding: 9pt 8pt;
      text-align: center;
    }}
    .stat-value {{
      font-size: 15.5pt;
      font-weight: 700;
      color: {p.text_dark};
      font-family: {fonts['latin']};
      direction: ltr;
      line-height: 1.1;
    }}
    .stat-label {{
      font-size: 8pt;
      font-weight: 400;
      color: #4b5563;
      margin-top: 3pt;
      line-height: 1.45;
    }}
    .stat-sub {{
      display: block;
      font-size: 7pt;
      color: {p.muted};
      font-style: italic;
      font-family: {fonts['latin']};
      margin-top: 2pt;
      direction: ltr;
      line-height: 1.35;
    }}

    /* ============ Data Tables ============ */
    .table-wrapper {{ margin: 8pt 0; }}
    .table-header {{
      margin-bottom: 4pt;
    }}
    .table-header h4 {{
      font-size: 11pt;
      font-weight: 700;
      color: {p.text_dark};
      display: inline;
    }}
    .table-header span {{
      font-family: {fonts['latin']};
      font-style: italic;
      font-size: 8.5pt;
      color: {p.muted};
      direction: ltr;
      unicode-bidi: isolate;
    }}
    .standard-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 9pt;
      border: 0.75pt solid {p.border_table_strong};
    }}
    .standard-table th {{
      background: {p.primary};
      color: #ffffff;
      padding: 8pt 8pt;
      text-align: center;
      border: 0.75pt solid {p.border_table};
      font-weight: 700;
      font-size: 9.5pt;
      line-height: 1.35;
      vertical-align: middle;
    }}
    .standard-table th .th-sub {{
      display: block;
      color: rgba(255,255,255,0.85);
      font-style: italic;
      font-size: 7.5pt;
      font-weight: 400;
      font-family: {fonts['latin']};
      direction: ltr;
    }}
    .standard-table td {{
      border: 0.75pt solid {p.border_table};
      padding: 6pt 8pt;
      line-height: 1.55;
      vertical-align: middle;
    }}
    .standard-table tbody tr.alt {{ background: {p.surface_alt}; }}
    td.num {{ text-align: center; font-family: {fonts['latin']}; font-weight: 700; direction: ltr; unicode-bidi: isolate; color: {p.text_dark}; }}
    td.txt {{ text-align: start; }}
    td.strong {{ font-weight: 700; color: {p.text_dark}; }}
    .td-sub {{
      display: inline;
      font-size: 8pt;
      color: {p.muted};
      font-weight: 400;
      font-family: {fonts['latin']};
      font-style: italic;
      unicode-bidi: isolate;
    }}

    /* ============ Captions ============ */
    .caption {{
      text-align: center;
      margin-top: 5pt;
    }}
    .caption-main {{
      color: {p.primary};
      font-weight: 600;
      font-size: 8.5pt;
    }}
    .caption-sub {{
      font-family: {fonts['latin']};
      font-style: italic;
      font-size: 7.5pt;
      color: {p.muted};
      direction: ltr;
      margin-top: 1pt;
    }}

    /* ============ Flow Steps (unified card, gold arrows) ============ */
    .flow-steps {{
      background: {p.surface};
      border: 0.75pt solid {p.border};
      border-radius: 8pt;
      padding: 10pt 16pt;
      margin: 10pt 0;
    }}
    .flow-title {{
      font-size: 11pt;
      font-weight: 700;
      color: {p.text_dark};
      margin-bottom: 6pt;
    }}
    .step-node {{ display: flex; align-items: flex-start; gap: 10pt; }}
    .step-content {{ flex: 1; }}
    .step-num {{
      width: 22.5pt;
      height: 22.5pt;
      border-radius: 50%;
      background: {p.primary};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 10pt;
      font-weight: 700;
      line-height: 1;
      padding: 0;
      flex-shrink: 0;
      font-family: {fonts['badge']};
    }}
    .step-title {{ font-weight: 400; font-size: 9.5pt; color: {p.text}; line-height: 1.5; margin-top: 1.5pt; }}
    .step-title strong {{ color: {p.text_dark}; }}
    .step-sub {{ color: {p.muted}; font-family: {fonts['latin']}; font-style: italic; font-size: 8pt; margin-top: 0; unicode-bidi: isolate; text-align: start; }}
    .step-arrow {{
      color: {p.accent};
      display: flex;
      align-items: center;
      justify-content: center;
      padding-inline-start: 24pt;
      margin: 5pt 0;
    }}
    .step-arrow svg {{ display: block; }}

    /* ============ Table of Contents ============ */
    .toc {{
      display: flex;
      flex-direction: column;
      height: 100%;
    }}
    .toc h2 {{
      font-size: 17pt;
      font-weight: 900;
      text-align: center;
      color: {p.text_dark};
      margin-bottom: 1pt;
    }}
    .toc-subtitle {{
      text-align: center;
      font-family: {fonts['latin']};
      font-style: italic;
      color: {p.accent_text};
      margin-bottom: 6pt;
      font-size: 11pt;
      direction: ltr;
    }}
    .toc-divider-line {{
      width: 100%;
      height: 1.5pt;
      background: {p.primary};
      margin: 4pt 0 18pt 0;
    }}
    .toc ul {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 16pt;
      padding: 0;
      flex: 1;
    }}
    .toc-row {{
      display: flex;
      align-items: center;
      font-size: 10.5pt;
    }}
    .toc-badge {{
      width: 22.5pt;
      height: 22.5pt;
      border-radius: 50%;
      background: {p.primary};
      color: #ffffff;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 10pt;
      font-weight: 700;
      line-height: 1;
      padding: 0;
      flex-shrink: 0;
      margin-inline-end: 9pt;
      font-family: {fonts['badge']};
    }}
    .appendix-badge {{ background: {p.accent_text} !important; }}
    .toc-title {{ display: flex; flex-direction: column; font-weight: 400; }}
    .toc-title strong {{ font-weight: 400; color: {p.text}; }}
    .toc-sub {{ font-family: {fonts['latin']}; font-size: 8pt; color: {p.muted}; font-style: italic; unicode-bidi: isolate; text-align: start; }}
    .toc-dots {{
      flex: 1;
      margin: 0 13pt 0 9pt;
      height: 5pt;
      background-image: radial-gradient(circle, {p.dots} 0.75pt, transparent 0.85pt);
      background-size: 5pt 5pt;
      background-repeat: repeat-x;
      background-position: bottom center;
    }}
    .toc-page {{
      font-family: {fonts['latin']};
      font-weight: 700;
      color: {p.primary};
      font-size: 10.5pt;
      min-width: 16pt;
      text-align: end;
    }}

    /* ============ Quotes (serif, boxed) ============ */
    .quote-box {{
      background: {p.surface_warm};
      border: none;
      border-inline-start: 3.5pt solid {p.primary};
      padding: 12pt 18pt;
      border-radius: 0;
      max-width: none;
      margin: 10pt 0;
    }}
    .layout-dark .quote-box {{
      background: transparent;
      border-color: {p.back_frame};
    }}
    .quote-rule {{ display: block; width: 60pt; height: 1.5pt; background: {p.accent}; margin: 12pt auto; }}
    .quote {{
      max-width: 490pt;
      margin: 10pt auto;
      text-align: center;
      padding: 0 22pt;
    }}
    .quote p {{
      font-size: 11.5pt;
      font-weight: 400;
      line-height: 1.75;
      color: {p.text_dark};
      font-family: {fonts['quote']};
    }}
    .layout-dark .quote p {{ color: #ffffff; line-height: 2.05; }}
    .layout-dark .quote {{ margin: 26pt auto; padding: 0 30pt; }}
    .quote-sub {{
      font-family: {fonts['latin']};
      font-style: italic;
      font-size: 8.5pt;
      color: {p.muted};
      margin-top: 7pt;
      unicode-bidi: isolate;
      line-height: 1.6;
    }}
    .layout-dark .quote-sub {{ color: #e2e8f0; }}
    .quote-author {{
      display: block;
      font-size: 8.5pt;
      color: {p.muted};
      margin-top: 7pt;
      text-align: end;
      unicode-bidi: isolate;
      font-family: {fonts['latin']};
    }}

    /* ============ Lists ============ */
    .content-list {{ margin: 5pt 0; padding-inline-start: 20pt; line-height: 1.7; font-size: 10.5pt; }}

    /* Card-variant lists */
    .list-cards {{
      list-style: none;
      padding: 0 !important;
      display: flex;
      flex-direction: column;
      gap: 6pt;
      margin: 7pt 0;
    }}
    .list-item-card {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border: 0.75pt solid {p.border_light};
      border-radius: 5pt;
      background: {p.surface};
      padding: 6pt 10pt;
      gap: 10pt;
    }}
    .list-item-badge {{
      font-size: 8.5pt;
      font-weight: 700;
      color: {p.muted};
      flex-shrink: 0;
      width: 16pt;
      text-align: center;
      font-family: {fonts['badge']};
    }}
    .list-item-content {{
      flex: 1;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 9pt;
    }}
    .list-item-title {{
      font-size: 9.5pt;
      font-weight: 700;
      color: {p.text_dark};
      line-height: 1.45;
    }}
    .list-item-tag {{
      font-family: {fonts['arabic']};
      font-size: 7.5pt;
      color: {p.muted};
      white-space: nowrap;
      flex-shrink: 0;
      background: {p.surface_alt};
      border: 0.75pt solid {p.border_light};
      padding: 1.5pt 7pt;
      border-radius: 4pt;
    }}
    .list-item-sub {{
      display: block;
      font-size: 8pt;
      color: {p.muted};
      font-weight: 400;
      line-height: 1.5;
    }}

    /* Row-variant lists (dotted dividers, light badges) */
    .list-rows {{
      list-style: none;
      padding: 0 !important;
      margin: 4pt 0;
    }}
    .list-row {{
      display: flex;
      align-items: flex-start;
      gap: 9pt;
      padding: 6pt 0;
      border-bottom: 1.5pt dotted {p.dots};
    }}
    .list-rows .list-row:last-child {{ border-bottom: none; }}
    .list-rows .list-item-badge {{
      width: 18pt;
      height: 18pt;
      border-radius: 50%;
      background: {p.surface_alt};
      color: {p.primary};
      font-family: {fonts['badge']};
      font-size: 9.5pt;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
      padding: 0;
      flex-shrink: 0;
      margin-top: 1pt;
    }}
    .list-row-content {{ flex: 1; }}
    .list-rows .list-item-title {{ font-size: 9.5pt; font-weight: 700; }}
    .list-rows .list-item-sub {{
      font-size: 8pt;
      color: {p.muted};
      margin-top: 1.5pt;
    }}

    /* ============ Image Blocks ============ */
    .image-block {
      margin: 6pt auto;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      break-inside: avoid;
    }
    .image-block.align-left { align-items: flex-start; text-align: left; }
    .image-block.align-right { align-items: flex-end; text-align: right; }
    .image-block.align-center { align-items: center; text-align: center; }
    .image-block img {
      display: block;
      height: auto;
      object-fit: contain;
      border-radius: 4pt;
    }
    .image-block.bordered img {
      border: 0.75pt solid {p.border};
      box-shadow: 0 1pt 3pt rgba(0,0,0,0.06);
      padding: 3pt;
      background: #ffffff;
    }
    .image-block figcaption {
      margin-top: 4pt;
    }

    /* ============ Layout Spacers ============ */
    .spacer-xs {{ height: 4pt; }}
    .spacer-sm {{ height: 8pt; }}
    .spacer-md {{ height: 14pt; }}
    .spacer-lg {{ height: 22pt; }}
    .spacer-xl {{ height: 32pt; }}
    .spacer-2xl {{ height: 48pt; }}

    /* ============ Vector Chart Container Card ============ */
    .chart-container {{
      margin: 9pt 0;
      padding: 9pt 12pt 7pt 12pt;
      border: 0.75pt solid {p.border};
      border-radius: 8pt;
      background: {p.surface};
      text-align: center;
    }}
    .chart-header {{ text-align: center; margin-bottom: 5pt; }}
    .chart-header h4 {{ font-size: 11pt; font-weight: 700; color: {p.text_dark}; line-height: 1.6; }}
    .chart-header .chart-subtitle {{
      font-family: {fonts['latin']};
      font-style: italic;
      font-size: 8.5pt;
      color: {p.muted};
      margin-top: 1pt;
      direction: ltr;
    }}
    .svg-viewport {{ width: 100%; max-height: 250pt; display: block; margin: 0 auto; }}

    /* ============ Running Footer (no rule, navy page number) ============ */
    .running-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 14pt;
      font-size: 7.5pt;
      color: {p.muted_light};
      font-family: {fonts['chart_arabic']};
      direction: ltr !important;
      unicode-bidi: isolate;
      line-height: 1.3;
    }}
    .footer-left {{ text-align: left; direction: rtl; unicode-bidi: isolate; }}
    .footer-right {{ text-align: right; direction: ltr; font-family: {fonts['latin']}; }}
    .footer-center {{
      background: {p.primary};
      color: #ffffff;
      font-family: {fonts['latin']};
      font-weight: 700;
      font-size: 9pt;
      line-height: 1;
      padding: 2.2pt 5pt;
      border-radius: 3pt;
      min-width: 14pt;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-align: center;
    }}
    /* Plain page number: primary-colored bold digits, no pill background
       (the reference design's default footer treatment). */
    .footer-center.footer-center-plain {{
      background: transparent;
      color: {p.primary};
      padding: 0;
      border-radius: 0;
      min-width: 0;
    }}
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
        center_style = str(footer.get("center_style", "plain"))
        center_cls = f"footer-center footer-center-{center_style}"
        if center_style not in ("pill", "plain"):
            center_cls = "footer-center footer-center-plain"
        footer_html = (
            f'<footer class="running-footer">'
            f'<span class="footer-left">{fmt(left)}</span>'
            f'<span class="{center_cls}">{fmt(center)}</span>'
            f'<span class="footer-right">{fmt(right)}</span>'
            f'</footer>'
        )

    layout = page.get("layout", "standard")
    content = "".join(content_parts)
    continuation = ' data-continuation="true"' if page.get("_continuation") else ""
    data_attrs = f' data-page-token="{esc(page_token)}"{continuation}'

    if layout == "framed":
        return (
            f'<main class="page-sheet layout-framed"{data_attrs}>'
            f'<div class="page-frame-outer"><div class="page-frame">{content}</div></div>'
            f'</main>'
        )
    if layout == "dark":
        return (
            f'<main class="page-sheet layout-dark"{data_attrs}>'
            f'<div class="dark-frame">{content}</div>'
            f'</main>'
        )
    return (
        f'<main class="page-sheet layout-{esc(layout)}"{data_attrs}>'
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
