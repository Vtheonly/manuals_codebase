"""
==================================================================================
ALGERIAN VOCATIONAL TRAINING SYSTEM (TAKWIN MEHANI) — SHARED MANUALS TEMPLATE
Unified Blueprint Engine for the 9 Specialty Manuals (Couture Dame & Modélisme)
Design: Emerald Deep & Warm Ochre — High-Fidelity Print CSS
==================================================================================
Author: Ouail Fati7a wa3il fati7a / وائل فتيحة
Version: 2.2 — Enhanced Centering, Anti-Header/Footer Print Rules, and Uniform Typography
==================================================================================
"""

# ==================================================================================
# PREMIUM COLOR PALETTE (Emerald Deep + Ochre Gold)
# ==================================================================================
PALETTE = {
    'emerald_deep':   '#022c22',
    'emerald':        '#064e3b',
    'emerald_light':  '#f0fdf4',
    'ochre':          '#b45309',
    'ochre_light':    '#fef3c7',
    'neutral_dark':   '#1e293b',
    'neutral_light':  '#f8fafc',
    'neutral_bg':     '#ffffff',
    'neutral_card':   '#f5f3ea',
    'text_primary':   '#1f2937',
    'text_secondary': '#4b5563',
    'text_muted':     '#6b7280',
    'border_color':   '#cbd5e1',
    'white':          '#ffffff',
}

# ==================================================================================
# HTML HEAD WITH UNIFORM FONTS
# ==================================================================================
def html_head(title_ar, title_fr):
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{title_ar} — {title_fr}</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Amiri:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
<style>
/* ================================================================ */
/* CSS CUSTOM PROPERTIES                                            */
/* ================================================================ */
:root {{
    --primary-deep:  {PALETTE['emerald_deep']};
    --primary:       {PALETTE['emerald']};
    --primary-light: {PALETTE['emerald_light']};
    --accent:        {PALETTE['ochre']};
    --accent-light:  {PALETTE['ochre_light']};
    --dark:          {PALETTE['neutral_dark']};
    --light:         {PALETTE['neutral_light']};
    --border:        {PALETTE['border_color']};
    --bg:            {PALETTE['neutral_bg']};
    --card:          {PALETTE['neutral_card']};
    --text:          {PALETTE['text_primary']};
    --text-2:        {PALETTE['text_secondary']};
    --text-muted:    {PALETTE['text_muted']};
    --white:         {PALETTE['white']};
    /* Harmonized Font Stacks */
    --font-fr:       'Inter', 'Segoe UI', sans-serif;
    --font-ar:       'Cairo', sans-serif;
    --font-display:  'Playfair Display', serif;
    --font-quote:    'Amiri', serif;
}}

/* ================================================================ */
/* PAGE SETUP & BROWSER PRINT HEADER/FOOTER REMOVAL                */
/* ================================================================ */
* {{ box-sizing: border-box; margin: 0; padding: 0; }}

@page {{
    size: A4;
    margin: 1.6cm 1.5cm; /* Native print margins */
}}

@media print {{
    @page {{
        margin: 1.6cm 1.5cm;
    }}
    /* Standard CSS rule to block browser-injected header/footer lines */
    html, body {{
        margin: 0;
        padding: 0;
        background: #fff;
    }}
}}

html, body {{
    background: var(--bg);
    color: var(--text);
    font-family: var(--font-ar);
    font-size: 10.5pt;
    line-height: 1.75;
    direction: rtl;
    text-align: right;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

@media screen {{
    html {{ background: #2a2a2a; display: flex; justify-content: center; }}
    body {{ width: 210mm; margin: 20px auto; box-shadow: 0 4px 30px rgba(0,0,0,0.5); padding: 1.6cm 1.5cm; }}
}}

/* ================================================================ */
/* COVER PAGE                                                       */
/* ================================================================ */
.cover {{
    width: 100%;
    min-height: 250mm;
    background: var(--bg);
    padding: 10mm;
    break-after: page;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
}}

.cover-inner {{
    border: 4px double var(--primary);
    height: 100%;
    width: 100%;
    padding: 10mm 15mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    text-align: center;
    box-sizing: border-box;
}}

/* ================================================================ */
/* TABLE OF CONTENTS                                                */
/* ================================================================ */
.toc-page {{
    width: 100%;
    min-height: 100%;
    background: var(--bg);
    padding: 10mm 5mm;
    break-after: page;
    page-break-after: always;
    box-sizing: border-box;
}}

/* ================================================================ */
/* BACK COVER                                                        */
/* ================================================================ */
.back-cover {{
    width: 100%;
    min-height: 240mm;
    background: var(--bg);
    padding: 10mm 5mm;
    break-before: page;
    page-break-before: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
}}

/* ================================================================ */
/* MAIN CONTENT                                                     */
/* ================================================================ */
.page {{
    background: #ffffff;
    width: 100%;
    padding: 5mm 0 8mm 0;
    box-sizing: border-box;
}}

.page:first-of-type {{
    padding-top: 0;
}}

/* ================================================================ */
/* HEADER BLOCK                                                     */
/* ================================================================ */
.cover-top-bar {{
    width: 100%;
    border-bottom: 2px solid var(--accent);
    padding-bottom: 6mm;
}}

.gov-txt-ar {{
    font-family: var(--font-ar);
    font-weight: 700;
    font-size: 12pt;
    color: var(--primary-deep);
    line-height: 1.5;
    margin: 0 0 1mm 0;
}}

.gov-txt-fr {{
    font-family: var(--font-fr);
    font-weight: 400;
    font-size: 9pt;
    color: #4b5563;
    direction: ltr;
    margin: 0 0 3mm 0;
    letter-spacing: 0.3px;
}}

/* ================================================================ */
/* COVER CENTER                                                     */
/* ================================================================ */
.cover-center {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 6mm 12mm;
}}

.cover-center .module-label {{
    font-family: var(--font-fr);
    font-weight: 500;
    font-size: 9pt;
    color: var(--text-muted);
    letter-spacing: 3px;
    direction: ltr;
    text-transform: uppercase;
    margin: 0 0 1mm 0;
}}

.cover-center .module-number {{
    font-family: var(--font-display);
    font-weight: 900;
    font-size: 48pt;
    color: var(--primary-deep);
    direction: ltr;
    line-height: 1;
    margin: 0 0 4mm 0;
}}

.cover-center .divider-ochre {{
    width: 50mm;
    height: 2px;
    background: var(--accent);
    margin: 2mm auto 4mm auto;
}}

.cover-center .title-ar {{
    font-family: var(--font-ar);
    font-weight: 800;
    font-size: 18pt;
    color: var(--primary-deep);
    line-height: 1.35;
    margin: 0 0 2mm 0;
    max-width: 160mm;
}}

.cover-center .title-fr {{
    font-family: var(--font-display);
    font-weight: 400;
    font-style: italic;
    font-size: 12pt;
    color: var(--accent);
    direction: ltr;
    margin: 0 0 6mm 0;
    max-width: 160mm;
}}

.cover-center .meta-block {{
    margin-top: 6mm;
    padding: 4mm 6mm;
    background: var(--primary-light);
    border-right: 3px solid var(--primary);
    border-radius: 1.5mm;
    font-family: var(--font-ar);
    font-size: 9.5pt;
    color: var(--text);
    line-height: 1.8;
    text-align: right;
    max-width: 165mm;
}}

.cover-center .meta-block .meta-row {{
    margin: 0.5mm 0;
}}

.cover-center .meta-block .meta-label {{
    color: var(--primary-deep);
    font-weight: 700;
    margin-left: 3mm;
}}

.cover-center .meta-block .meta-val {{
    color: var(--text);
    font-weight: 500;
}}

/* ================================================================ */
/* COVER BOTTOM                                                     */
/* ================================================================ */
.cover-bottom {{
    width: 100%;
    border-top: 2px solid var(--accent);
    padding-top: 6mm;
    text-align: center;
}}

.cover-bottom .author-label {{
    font-family: var(--font-ar);
    font-weight: 500;
    font-size: 9pt;
    color: var(--accent);
    margin: 0 0 1mm 0;
}}

.cover-bottom .author-name-ar {{
    font-family: var(--font-ar);
    font-weight: 700;
    font-size: 14pt;
    color: var(--primary-deep);
    margin: 0 0 0.5mm 0;
}}

.cover-bottom .author-name-fr {{
    font-family: var(--font-fr);
    font-weight: 500;
    font-size: 10pt;
    color: var(--dark);
    direction: ltr;
    margin: 0 0 1.5mm 0;
    letter-spacing: 0.5px;
}}

.cover-bottom .doc-type {{
    font-family: var(--font-fr);
    font-size: 8pt;
    color: var(--text-muted);
    direction: ltr;
    letter-spacing: 1.5px;
    margin: 0.5mm 0;
    text-transform: uppercase;
}}

.cover-bottom .year {{
    font-family: var(--font-display);
    font-size: 11pt;
    color: var(--accent);
    direction: ltr;
    margin: 0.5mm 0 0 0;
    letter-spacing: 1px;
}}

/* ================================================================ */
/* TABLE OF CONTENTS                                                */
/* ================================================================ */
.toc-header {{
    text-align: center;
    margin-bottom: 12mm;
    padding-bottom: 5mm;
    border-bottom: 2px solid var(--primary);
}}

.toc-header .toc-title-ar {{
    font-family: var(--font-ar);
    font-weight: 800;
    font-size: 20pt;
    color: var(--primary-deep);
    margin: 0 0 1.5mm 0;
}}

.toc-header .toc-title-fr {{
    font-family: var(--font-display);
    font-style: italic;
    font-size: 12pt;
    color: var(--accent);
    direction: ltr;
    margin: 0;
}}

.toc-list {{
    list-style: none;
    padding: 0;
    margin: 0;
}}

.toc-item {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 3mm 0;
    border-bottom: 1px dotted var(--border);
    font-family: var(--font-ar);
    font-size: 10.5pt;
}}

.toc-item .toc-num {{
    display: inline-block;
    width: 7mm;
    color: var(--accent);
    font-weight: 700;
    font-family: var(--font-display);
    font-size: 12pt;
    flex-shrink: 0;
}}

.toc-item .toc-text {{
    flex: 1;
    color: var(--text);
    margin: 0 3mm;
    line-height: 1.4;
}}

.toc-item .toc-text .toc-fr {{
    display: block;
    font-family: var(--font-fr);
    font-style: italic;
    font-size: 8.5pt;
    color: var(--text-muted);
    direction: ltr;
    text-align: left;
    margin-top: 0.5mm;
}}

.toc-item .toc-page-num {{
    color: var(--primary);
    font-weight: 700;
    font-family: var(--font-fr);
    font-size: 10pt;
    direction: ltr;
    flex-shrink: 0;
}}

/* ================================================================ */
/* SECTION HEADERS                                                  */
/* ================================================================ */
.section-header {{
    margin-top: 8mm;
    margin-bottom: 4mm;
    break-after: avoid;
    break-inside: avoid;
    padding-bottom: 2mm;
    border-bottom: 2px solid var(--primary);
}}

.section-header:first-of-type {{
    margin-top: 0;
}}

.section-header .sec-num {{
    display: inline-block;
    background: var(--primary);
    color: #fff;
    width: 7mm;
    height: 7mm;
    line-height: 7mm;
    text-align: center;
    border-radius: 50%;
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 10pt;
    margin-left: 2mm;
    direction: ltr;
    vertical-align: middle;
}}

.section-header .sec-title-ar {{
    font-family: var(--font-ar);
    font-weight: 800;
    font-size: 13pt;
    color: var(--primary-deep);
    line-height: 1.4;
    vertical-align: middle;
}}

.section-header .sec-title-fr {{
    display: block;
    font-family: var(--font-display);
    font-style: italic;
    font-size: 9pt;
    color: var(--accent);
    direction: ltr;
    text-align: left;
    margin-top: 1mm;
    margin-right: 9mm;
}}

/* ================================================================ */
/* SUBSECTION HEADERS                                               */
/* ================================================================ */
.subsection {{
    margin-top: 6mm;
    break-after: avoid;
}}

.subsection-title {{
    font-family: var(--font-ar);
    font-weight: 700;
    font-size: 11pt;
    color: var(--primary);
    margin: 0 0 2mm 0;
    padding-right: 3mm;
    border-right: 3px solid var(--accent);
    line-height: 1.4;
}}

.subsection-title .sub-fr {{
    font-family: var(--font-fr);
    font-weight: 500;
    font-style: italic;
    font-size: 9pt;
    color: var(--text-muted);
    direction: ltr;
    margin-right: 2mm;
}}

/* ================================================================ */
/* BODY TEXT                                                        */
/* ================================================================ */
p {{
    margin: 0 0 3mm 0;
    text-align: justify;
    font-family: var(--font-ar);
    font-size: 10.5pt;
    line-height: 1.8;
    color: var(--text);
}}

p .fr {{
    font-family: var(--font-fr);
    font-style: italic;
    color: var(--primary);
    font-weight: 500;
    direction: ltr;
    display: inline;
}}

strong, b {{
    font-weight: 700;
    color: var(--primary-deep);
}}

ul, ol {{
    margin: 2mm 0 3mm 0;
    padding-right: 7mm;
}}

ul li, ol li {{
    font-family: var(--font-ar);
    font-size: 10.5pt;
    line-height: 1.7;
    margin-bottom: 1.5mm;
    text-align: right;
    color: var(--text);
}}

ul li .fr, ol li .fr {{
    font-family: var(--font-fr);
    font-style: italic;
    color: var(--primary);
    direction: ltr;
    display: inline;
}}

/* ================================================================ */
/* TABLES                                                           */
/* ================================================================ */
.table-wrapper {{
    margin: 4mm auto;
    break-inside: avoid;
    direction: rtl;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}}

table.data-table {{
    width: 100%;
    border-collapse: collapse;
    font-family: var(--font-ar);
    font-size: 9pt;
    border: 1px solid var(--border);
    direction: rtl;
}}

table.data-table thead {{
    background: var(--primary);
    color: #fff;
}}

table.data-table thead th {{
    padding: 2mm 3mm;
    text-align: center;
    font-weight: 700;
    font-family: var(--font-ar);
    font-size: 9.5pt;
    border-bottom: 1.5px solid var(--primary-deep);
    color: #ffffff;
}}

table.data-table thead th .th-fr {{
    display: block;
    font-family: var(--font-fr);
    font-weight: 400;
    font-style: italic;
    font-size: 7.5pt;
    color: rgba(255,255,255,0.85);
    direction: ltr;
    margin-top: 0.3mm;
}}

table.data-table tbody tr:nth-child(even) {{
    background: var(--primary-light);
}}

table.data-table tbody tr:nth-child(odd) {{
    background: var(--white);
}}

table.data-table tbody td {{
    padding: 2mm 3mm;
    border-bottom: 1px solid var(--border);
    text-align: right;
    color: var(--text);
    font-size: 9pt;
    line-height: 1.4;
}}

table.data-table tbody td.center {{ text-align: center; }}

table.data-table tbody td.num {{
    text-align: center;
    font-family: var(--font-display);
    font-weight: 700;
    color: var(--primary-deep);
    direction: ltr;
}}

table.data-table tbody td .fr {{
    font-family: var(--font-fr);
    font-style: italic;
    color: var(--text-muted);
    font-size: 8pt;
    direction: ltr;
    display: inline;
}}

.table-caption {{
    text-align: center;
    font-family: var(--font-ar);
    font-size: 8.5pt;
    font-weight: 600;
    color: var(--primary);
    margin-top: 1.5mm;
    margin-bottom: 4mm;
}}

.table-caption .cap-fr {{
    font-family: var(--font-fr);
    font-style: italic;
    color: var(--text-muted);
    direction: ltr;
    display: block;
    font-size: 8pt;
    margin-top: 0.3mm;
}}

/* ================================================================ */
/* CALLOUT BOXES                                                    */
/* ================================================================ */
.callout {{
    margin: 4mm auto;
    padding: 4mm 5mm;
    border-radius: 1.5mm;
    break-inside: avoid;
    border-right: 3px solid var(--accent);
    background: var(--accent-light);
    font-family: var(--font-ar);
    font-size: 10pt;
    line-height: 1.6;
    color: var(--text);
    width: 100%;
}}

.callout-title {{
    font-family: var(--font-ar);
    font-weight: 700;
    font-size: 10.5pt;
    color: var(--accent);
    margin-bottom: 1.5mm;
    display: flex;
    align-items: center;
    gap: 2mm;
}}

.callout-title .icon {{
    display: inline-block;
    width: 6mm;
    height: 6mm;
    background: var(--accent);
    color: #fff;
    border-radius: 50%;
    text-align: center;
    line-height: 6mm;
    font-family: var(--font-display);
    font-weight: 900;
    font-size: 10pt;
    direction: ltr;
    flex-shrink: 0;
}}

.callout p {{
    margin-bottom: 1.5mm;
    font-size: 10pt;
    line-height: 1.6;
    color: var(--text);
}}

.callout-emerald {{
    border-right-color: var(--primary);
    background: var(--primary-light);
}}

.callout-emerald .callout-title {{
    color: var(--primary-deep);
}}

.callout-emerald .callout-title .icon {{
    background: var(--primary);
}}

/* ================================================================ */
/* DASHBOARD GRID — 3-column metric cards                           */
/* ================================================================ */
.dashboard-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin: 4mm auto;
    break-inside: avoid;
    width: 100%;
    justify-content: center;
}}

.dashboard-card {{
    background: var(--light);
    border-right: 3px solid var(--primary);
    border-radius: 3px;
    padding: 10px;
    text-align: center;
}}

.dashboard-value {{
    font-size: 1.3rem;
    font-weight: 900;
    color: var(--accent);
    line-height: 1.2;
    font-family: var(--font-display);
    direction: ltr;
}}

.dashboard-label {{
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--primary);
    margin-top: 1.5mm;
    font-family: var(--font-ar);
}}

.dashboard-label .fr {{
    display: block;
    font-family: var(--font-fr);
    font-style: italic;
    font-weight: 400;
    color: var(--text-muted);
    direction: ltr;
    font-size: 0.65rem;
    margin-top: 0.3mm;
}}

/* ================================================================ */
/* TIMELINE — vertical connected                                    */
/* ================================================================ */
.timeline-chain {{
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 4mm auto 15px auto;
    position: relative;
    break-inside: avoid;
    width: 100%;
    align-items: center;
}}

.timeline-node {{
    display: flex;
    gap: 10px;
    background: var(--light);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 8px 12px;
    page-break-inside: avoid;
    width: 100%;
}}

.node-index {{
    background: var(--primary);
    color: white;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-family: var(--font-display);
    font-size: 10pt;
    direction: ltr;
    flex-shrink: 0;
}}

.node-content {{
    flex: 1;
}}

.node-content h4 {{
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--primary-deep);
    font-family: var(--font-ar);
    margin: 0 0 1mm 0;
}}

.node-content p {{
    margin: 0;
    font-size: 0.8rem;
    color: var(--text-2);
    font-style: italic;
    font-family: var(--font-fr);
    direction: ltr;
    text-align: left;
}}

/* ================================================================ */
/* FLOWCHART / PROCESS                                              */
/* ================================================================ */
.flowchart {{
    margin: 4mm auto;
    break-inside: avoid;
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 1.5mm;
    padding: 4mm;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}}

.flow-step {{
    display: flex;
    align-items: center;
    margin-bottom: 2mm;
    break-inside: avoid;
    width: 100%;
    justify-content: flex-start;
}}

.flow-step .step-num {{
    flex-shrink: 0;
    width: 8mm;
    height: 8mm;
    border-radius: 50%;
    background: var(--primary);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 10pt;
    direction: ltr;
    margin-left: 3mm;
}}

.flow-step .step-text {{
    flex: 1;
    font-family: var(--font-ar);
    font-size: 9.5pt;
    line-height: 1.6;
    color: var(--text);
}}

.flow-step .step-text .step-fr {{
    display: block;
    font-family: var(--font-fr);
    font-style: italic;
    color: var(--text-muted);
    font-size: 8pt;
    direction: ltr;
    margin-top: 0.3mm;
}}

.flow-arrow {{
    text-align: right;
    padding-right: 3.5mm; /* Centers the down-arrow perfectly under the 8mm step-circle */
    color: var(--accent);
    font-size: 11pt;
    margin: 1mm 0;
    line-height: 1;
    width: 100%;
}}

/* ================================================================ */
/* STAT ROW                                                         */
/* ================================================================ */
.stat-row {{
    display: flex;
    gap: 3mm;
    margin: 4mm auto;
    break-inside: avoid;
    width: 100%;
    justify-content: center;
}}

.stat-card {{
    flex: 1;
    background: var(--white);
    border: 1px solid var(--border);
    border-top: 2.5px solid var(--accent);
    border-radius: 1.5mm;
    padding: 3mm 2mm;
    text-align: center;
}}

.stat-card .stat-num {{
    font-family: var(--font-display);
    font-weight: 900;
    font-size: 17pt;
    color: var(--primary-deep);
    direction: ltr;
    line-height: 1.1;
}}

.stat-card .stat-label {{
    font-family: var(--font-ar);
    font-size: 8pt;
    color: var(--text-2);
    margin-top: 1.5mm;
    line-height: 1.3;
}}

.stat-card .stat-label .fr {{
    display: block;
    font-family: var(--font-fr);
    font-style: italic;
    color: var(--text-muted);
    direction: ltr;
    font-size: 7pt;
    margin-top: 0.3mm;
}}

/* ================================================================ */
/* QUOTE BLOCK                                                      */
/* ================================================================ */
.quote-block {{
    margin: 5mm auto;
    padding: 4mm 6mm;
    border-right: 3px solid var(--primary);
    background: var(--card);
    font-family: var(--font-quote);
    font-style: italic;
    font-size: 10.5pt;
    line-height: 1.7;
    color: var(--primary-deep);
    break-inside: avoid;
    width: 100%;
}}

.quote-block .quote-author {{
    display: block;
    text-align: left;
    margin-top: 1.5mm;
    font-family: var(--font-fr);
    font-style: normal;
    font-size: 8.5pt;
    color: var(--text-muted);
    direction: ltr;
}}

/* ================================================================ */
/* SVG CHART CARD (Centered container & centered graphs)             */
/* ================================================================ */
.chart-card {{
    margin: 5mm auto;
    padding: 4mm;
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 1.5mm;
    break-inside: avoid;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}}

.chart-title {{
    font-family: var(--font-ar);
    font-weight: 700;
    font-size: 11pt;
    color: var(--primary-deep);
    text-align: center;
    margin: 0 0 0.5mm 0;
    width: 100%;
}}

.chart-subtitle {{
    font-family: var(--font-fr);
    font-style: italic;
    font-size: 8.5pt;
    color: var(--text-muted);
    text-align: center;
    direction: ltr;
    margin: 0 0 3mm 0;
    width: 100%;
}}

.chart-svg {{
    display: block;
    margin: 0 auto;
    max-width: 100%;
    height: auto;
}}

.chart-caption {{
    text-align: center;
    font-family: var(--font-ar);
    font-size: 8.5pt;
    font-weight: 600;
    color: var(--primary);
    margin-top: 2mm;
    width: 100%;
}}

.chart-caption .cap-fr {{
    font-family: var(--font-fr);
    font-style: italic;
    color: var(--text-muted);
    direction: ltr;
    display: block;
    font-size: 8pt;
    margin-top: 0.3mm;
}}

/* ================================================================ */
/* BACK COVER                                                        */
/* ================================================================ */
.back-cover .bc-top {{
    background: var(--primary-deep);
    color: var(--white);
    padding: 10mm 16mm;
    text-align: center;
    position: relative;
}}

.back-cover .bc-top::after {{
    content: "";
    position: absolute;
    bottom: -2mm;
    left: 50%;
    transform: translateX(-50%);
    width: 40mm;
    height: 2.5mm;
    background: var(--accent);
}}

.back-cover .insfp-mark {{
    font-family: var(--font-display);
    font-weight: 900;
    font-size: 32pt;
    color: var(--accent);
    direction: ltr;
    letter-spacing: 6px;
    margin: 0;
}}

.back-cover .bc-center {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 12mm 18mm;
}}

.back-cover .closing-ar {{
    font-family: var(--font-ar);
    font-weight: 700;
    font-size: 13pt;
    color: var(--primary-deep);
    line-height: 1.7;
    margin: 4mm 0;
    max-width: 160mm;
}}

.back-cover .closing-fr {{
    font-family: var(--font-fr);
    font-weight: 300;
    font-style: italic;
    font-size: 10pt;
    color: var(--text-2);
    direction: ltr;
    line-height: 1.6;
    max-width: 160mm;
    margin: 0 0 8mm 0;
}}

.back-cover .closing-divider {{
    width: 25mm;
    height: 2px;
    background: var(--accent);
    margin: 3mm auto;
}}

.back-cover .bc-bottom {{
    background: var(--primary-deep);
    color: var(--white);
    text-align: center;
    padding: 6mm 16mm 10mm 16mm;
    position: relative;
}}

.back-cover .bc-bottom::before {{
    content: "";
    position: absolute;
    top: -2mm;
    left: 50%;
    transform: translateX(-50%);
    width: 40mm;
    height: 2.5mm;
    background: var(--accent);
}}

.back-cover .closing-meta {{
    font-family: var(--font-ar);
    font-size: 9pt;
    color: rgba(255,255,255,0.78);
    line-height: 1.7;
    margin: 0;
}}

.back-cover .closing-meta .meta-year {{
    font-family: var(--font-display);
    color: var(--accent);
    font-size: 10pt;
    direction: ltr;
    display: block;
    margin-top: 1.5mm;
}}

</style>
</head>
<body>
"""

# ==================================================================================
# COVER PAGE
# ==================================================================================
def render_cover(module_num, module_num_label, title_ar, title_fr, code_module="HTE1204", year="2025 / 2026"):
    return f"""
<!-- ============================ COVER PAGE ============================ -->
<div class="cover">
    <div class="cover-inner">
        <div class="cover-top-bar">
            <div class="gov-txt-ar">الجمهورية الجزائرية الديمقراطية الشعبية</div>
            <div class="gov-txt-fr">République Algérienne Démocratique et Populaire</div>
            <p style="margin-top: 4px; font-weight:700; font-family:var(--font-ar); color:var(--primary-deep);">وزارة التكوين والتعليم المهنيين</p>
        </div>

        <div class="cover-center">
            <div class="module-label">{module_num_label}</div>
            <div class="module-number">{module_num}</div>
            <div class="divider-ochre"></div>
            <div class="title-ar">{title_ar}</div>
            <div class="title-fr">{title_fr}</div>

            <div class="meta-block">
                <div class="meta-row"><span class="meta-label">التخصص :</span><span class="meta-val">التقني السامي في تصميم و صناعة الملابس — Tailleur Dames</span></div>
                <div class="meta-row"><span class="meta-label">المستوى :</span><span class="meta-val">التقني السامي — Technicien Supérieur (Niveau IV)</span></div>
                <div class="meta-row"><span class="meta-label">رمز التخصص :</span><span class="meta-val" style="direction:ltr;">{code_module}</span></div>
                <div class="meta-row"><span class="meta-label">الإطار البيداغوجي :</span><span class="meta-val">المنهجية المبنية على الكفاءات — Approche Par Compétences (APC)</span></div>
            </div>
        </div>

        <div class="cover-bottom">
            <div class="author-label">إعداد الطالب</div>
            <div class="author-name-ar">وعيل فتيحة</div>
            <div class="author-name-fr">Ouail Fatiha</div>
            <div class="doc-type">Rapport Pédagogique — تقرير بيداغوجي</div>
            <div class="year">{year}</div>
        </div>
    </div>
</div>
"""

# ==================================================================================
# TABLE OF CONTENTS
# ==================================================================================
def render_toc(toc_items):
    """toc_items: list of (number, title_ar, title_fr, page_num)"""
    items_html = ""
    for num, t_ar, t_fr, pg in toc_items:
        items_html += f"""
        <li class="toc-item">
            <span class="toc-num">{num}</span>
            <span class="toc-text">{t_ar}<span class="toc-fr">{t_fr}</span></span>
            <span class="toc-page-num">{pg}</span>
        </li>"""
    return f"""
<!-- ============================ TABLE OF CONTENTS ============================ -->
<div class="toc-page">
    <div class="toc-header">
        <div class="toc-title-ar">فهرس المحتويات</div>
        <div class="toc-title-fr">Table des Matières</div>
    </div>
    <ul class="toc-list">
        {items_html}
    </ul>
</div>
"""

# ==================================================================================
# SECTION HEADER
# ==================================================================================
def section_header(num, title_ar, title_fr):
    return f"""
<div class="section-header">
    <span class="sec-num">{num}</span><span class="sec-title-ar">{title_ar}</span>
    <span class="sec-title-fr">{title_fr}</span>
</div>
"""

# ==================================================================================
# SUBSECTION HEADER
# ==================================================================================
def subsection(title_ar, title_fr=""):
    fr_html = f'<span class="sub-fr">— {title_fr}</span>' if title_fr else ""
    return f"""
<div class="subsection">
    <div class="subsection-title">{title_ar} {fr_html}</div>
</div>
"""

# ==================================================================================
# DATA TABLE
# ==================================================================================
def data_table(headers, rows, caption_ar="", caption_fr=""):
    thead = ""
    for h_ar, h_fr in headers:
        thead += f'<th>{h_ar}<span class="th-fr">{h_fr}</span></th>'

    tbody = ""
    for row in rows:
        tbody += "<tr>"
        for cell in row:
            if isinstance(cell, dict):
                text = cell.get('text', '')
                fr = cell.get('fr', '')
                ctype = cell.get('type', '')
                cls = f' class="{ctype}"' if ctype else ''
                fr_html = f' <span class="fr">{fr}</span>' if fr else ''
                tbody += f'<td{cls}>{text}{fr_html}</td>'
            else:
                tbody += f'<td>{cell}</td>'
        tbody += "</tr>"

    cap_html = ""
    if caption_ar or caption_fr:
        cap_fr_html = f'<span class="cap-fr">{caption_fr}</span>' if caption_fr else ""
        cap_html = f'<div class="table-caption">{caption_ar} {cap_fr_html}</div>'

    return f"""
<div class="table-wrapper">
    <table class="data-table">
        <thead><tr>{thead}</tr></thead>
        <tbody>{tbody}</tbody>
    </table>
    {cap_html}
</div>
"""

# ==================================================================================
# CALLOUT BOX
# ==================================================================================
def callout(title, body_html, variant="ochre", icon="★"):
    cls = "callout-emerald" if variant == "emerald" else ""
    return f"""
<div class="callout {cls}">
    <div class="callout-title"><span class="icon">{icon}</span>{title}</div>
    {body_html}
</div>
"""

# ==================================================================================
# FLOWCHART
# ==================================================================================
def flowchart(steps, title=""):
    steps_html = ""
    for i, (num, t_ar, t_fr) in enumerate(steps):
        steps_html += f"""
        <div class="flow-step">
            <div class="step-num">{num}</div>
            <div class="step-text">{t_ar}<span class="step-fr">{t_fr}</span></div>
        </div>"""
        if i < len(steps) - 1:
            steps_html += '<div class="flow-arrow">▼</div>'
    title_html = f'<div style="text-align:center;font-weight:700;margin-bottom:2mm;color:var(--primary-deep);font-family:var(--font-ar);">{title}</div>' if title else ""
    return f"""
<div class="flowchart">
    {title_html}
    {steps_html}
</div>
"""

# ==================================================================================
# TIMELINE CHAIN
# ==================================================================================
def timeline_chain(nodes):
    nodes_html = ""
    for num, t_ar, desc_fr in nodes:
        nodes_html += f"""
        <div class="timeline-node">
            <div class="node-index">{num}</div>
            <div class="node-content">
                <h4>{t_ar}</h4>
                <p>{desc_fr}</p>
            </div>
        </div>"""
    return f"""
<div class="timeline-chain">
    {nodes_html}
</div>
"""

# ==================================================================================
# STAT ROW
# ==================================================================================
def stat_row(stats):
    cards = ""
    for num, lab_ar, lab_fr in stats:
        cards += f"""
        <div class="stat-card">
            <div class="stat-num">{num}</div>
            <div class="stat-label">{lab_ar}<span class="fr">{lab_fr}</span></div>
        </div>"""
    return f'<div class="stat-row">{cards}</div>'

# ==================================================================================
# QUOTE BLOCK
# ==================================================================================
def quote_block(text, author=""):
    author_html = f'<span class="quote-author">— {author}</span>' if author else ""
    return f"""
<div class="quote-block">{text}{author_html}</div>
"""

# ==================================================================================
# CHART: Vertical BAR CHART (SVG)
# ==================================================================================
def bar_chart(title_ar, title_fr, categories, values, unit="", caption_ar="", caption_fr="",
              max_val=None, color="#064e3b", accent_color="#b45309"):
    if max_val is None:
        max_val = max(values) * 1.2 if values else 100

    n = len(categories)
    chart_w = 600
    chart_h = 320
    margin_l = 55
    margin_r = 15
    margin_t = 25
    margin_b = 35
    bar_area_w = chart_w - margin_l - margin_r
    bar_area_h = chart_h - margin_t - margin_b

    bar_w = max(12, min(50, (bar_area_w / n) * 0.6))
    gap = (bar_area_w - (bar_w * n)) / (n + 1) if n > 0 else 10
    start_x = margin_l + gap

    bars_svg = ""
    grid_svg = ""
    labels_svg = ""
    values_svg = ""

    for i in range(5):
        y = margin_t + (bar_area_h / 4) * i
        val = max_val - (max_val / 4) * i
        grid_svg += f'<line x1="{margin_l}" y1="{y}" x2="{chart_w - margin_r}" y2="{y}" stroke="#E5E7EB" stroke-width="0.5" stroke-dasharray="2,2"/>'
        grid_svg += f'<text x="{margin_l - 6}" y="{y + 3}" font-family="Inter" font-size="8" fill="#6B7280" text-anchor="end">{val:.0f}</text>'

    for i, ((lab_ar, lab_fr), v) in enumerate(zip(categories, values)):
        x = start_x + i * (bar_w + gap)
        bar_h = (v / max_val) * bar_area_h if max_val > 0 else 0
        y = margin_t + (bar_area_h - bar_h)
        fill = color if i % 2 == 0 else accent_color
        bars_svg += f'<rect x="{x}" y="{y}" width="{bar_w}" height="{bar_h}" fill="{fill}" rx="1.5"/>'
        values_svg += f'<text x="{x + bar_w/2}" y="{y-4}" font-family="Inter" font-size="9" font-weight="700" fill="#022c22" text-anchor="middle">{v}{unit}</text>'
        labels_svg += f'<text x="{x + bar_w/2}" y="{margin_t + bar_area_h + 12}" font-family="Cairo" font-size="7.5" fill="#1F2937" text-anchor="middle">{lab_ar}</text>'
        if lab_fr:
            labels_svg += f'<text x="{x + bar_w/2}" y="{margin_t + bar_area_h + 22}" font-family="Inter" font-size="6.5" font-style="italic" fill="#6B7280" text-anchor="middle">{lab_fr}</text>'

    axes = f'<line x1="{margin_l}" y1="{margin_t}" x2="{margin_l}" y2="{margin_t + bar_area_h}" stroke="#1F2937" stroke-width="0.8"/>'
    axes += f'<line x1="{margin_l}" y1="{margin_t + bar_area_h}" x2="{chart_w - margin_r}" y2="{margin_t + bar_area_h}" stroke="#1F2937" stroke-width="0.8"/>'

    cap_html = ""
    if caption_ar or caption_fr:
        cap_fr_html = f'<span class="cap-fr">{caption_fr}</span>' if caption_fr else ""
        cap_html = f'<div class="chart-caption">{caption_ar} {cap_fr_html}</div>'

    return f"""
<div class="chart-card">
    <div class="chart-title">{title_ar}</div>
    <div class="chart-subtitle">{title_fr}</div>
    <svg class="chart-svg" style="direction: ltr;" viewBox="0 0 {chart_w} {chart_h}" xmlns="http://www.w3.org/2000/svg">
        {grid_svg}
        {axes}
        {bars_svg}
        {values_svg}
        {labels_svg}
    </svg>
    {cap_html}
</div>
"""

# ==================================================================================
# CHART: PIE / DONUT CHART (SVG)
# ==================================================================================
def pie_chart(title_ar, title_fr, segments, caption_ar="", caption_fr="",
              donut=True, center_label="", center_value=""):
    total = sum(s[2] for s in segments) if segments else 1
    chart_w = 580
    chart_h = 300
    cx, cy = 160, 145
    r_out = 100
    r_in = 55 if donut else 0

    import math
    slices_svg = ""
    legend_svg = ""
    legend_x = 290
    legend_y = 20

    start_angle = -90
    for i, (lab_ar, lab_fr, val, color) in enumerate(segments):
        sweep_angle = (val / total) * 360
        end_angle = start_angle + sweep_angle

        sa = start_angle * math.pi / 180
        ea = end_angle * math.pi / 180

        x1 = cx + r_out * math.cos(sa)
        y1 = cy + r_out * math.sin(sa)
        x2 = cx + r_out * math.cos(ea)
        y2 = cy + r_out * math.sin(ea)

        large_arc = 1 if sweep_angle > 180 else 0

        if donut:
            x3 = cx + r_in * math.cos(ea)
            y3 = cy + r_in * math.sin(ea)
            x4 = cx + r_in * math.cos(sa)
            y4 = cy + r_in * math.sin(sa)
            path = f'M {x1} {y1} A {r_out} {r_out} 0 {large_arc} 1 {x2} {y2} L {x3} {y3} A {r_in} {r_in} 0 {large_arc} 0 {x4} {y4} Z'
        else:
            path = f'M {cx} {cy} L {x1} {y1} A {r_out} {r_out} 0 {large_arc} 1 {x2} {y2} Z'

        slices_svg += f'<path d="{path}" fill="{color}" stroke="#FFFFFF" stroke-width="1.2"/>'

        pct = (val / total) * 100
        ly = legend_y + i * 20
        legend_svg += f'<rect x="{legend_x}" y="{ly}" width="12" height="12" fill="{color}" rx="1.5"/>'
        legend_svg += f'<text x="{legend_x + 18}" y="{ly + 10}" font-family="Cairo" font-size="9" fill="#1F2937">{lab_ar} — {pct:.1f}%</text>'
        if lab_fr:
            legend_svg += f'<text x="{legend_x + 18}" y="{ly + 20}" font-family="Inter" font-size="7" font-style="italic" fill="#6B7280">{lab_fr}</text>'

        start_angle = end_angle

    center_svg = ""
    if donut and (center_label or center_value):
        if center_value:
            center_svg += f'<text x="{cx}" y="{cy-2}" font-family="Inter" font-size="20" font-weight="900" fill="#022c22" text-anchor="middle">{center_value}</text>'
        if center_label:
            center_svg += f'<text x="{cx}" y="{cy+14}" font-family="Cairo" font-size="9" fill="#6B7280" text-anchor="middle">{center_label}</text>'

    cap_html = ""
    if caption_ar or caption_fr:
        cap_fr_html = f'<span class="cap-fr">{caption_fr}</span>' if caption_fr else ""
        cap_html = f'<div class="chart-caption">{caption_ar} {cap_fr_html}</div>'

    return f"""
<div class="chart-card">
    <div class="chart-title">{title_ar}</div>
    <div class="chart-subtitle">{title_fr}</div>
    <svg class="chart-svg" style="direction: ltr;" viewBox="0 0 {chart_w} {chart_h}" xmlns="http://www.w3.org/2000/svg">
        {slices_svg}
        {center_svg}
        {legend_svg}
    </svg>
    {cap_html}
</div>
"""

# ==================================================================================
# CHART: LINE CHART (SVG)
# ==================================================================================
def line_chart(title_ar, title_fr, x_labels, series, caption_ar="", caption_fr="",
               y_max=None, y_unit=""):
    chart_w = 600
    chart_h = 320
    margin_l = 55
    margin_r = 15
    margin_t = 25
    margin_b = 30
    plot_w = chart_w - margin_l - margin_r
    plot_h = chart_h - margin_t - margin_b

    n = len(x_labels)
    all_vals = [v for s in series for v in s[2]] if series else []
    if y_max is None:
        y_max = max(all_vals) * 1.2 if all_vals else 100

    grid_svg = ""
    for i in range(5):
        y = margin_t + (plot_h / 4) * i
        val = y_max - (y_max / 4) * i
        grid_svg += f'<line x1="{margin_l}" y1="{y}" x2="{margin_l + plot_w}" y2="{y}" stroke="#E5E7EB" stroke-width="0.5" stroke-dasharray="2,2"/>'
        grid_svg += f'<text x="{margin_l - 6}" y="{y + 3}" font-family="Inter" font-size="8" fill="#6B7280" text-anchor="end">{val:.0f}{y_unit}</text>'

    x_labels_svg = ""
    for i, lab in enumerate(x_labels):
        x = margin_l + (plot_w / (n - 1)) * i if n > 1 else margin_l + plot_w / 2
        x_labels_svg += f'<text x="{x}" y="{margin_t + plot_h + 14}" font-family="Cairo" font-size="8" fill="#1F2937" text-anchor="middle">{lab}</text>'

    series_svg = ""
    for lab_ar, lab_fr, values, color in series:
        points = []
        for i, v in enumerate(values):
            x = margin_l + (plot_w / (n - 1)) * i if n > 1 else margin_l + plot_w / 2
            y = margin_t + plot_h - (v / y_max) * plot_h if y_max > 0 else margin_t + plot_h
            points.append(f"{x},{y}")
            series_svg += f'<circle cx="{x}" cy="{y}" r="3" fill="{color}" stroke="#FFFFFF" stroke-width="1"/>'
        polyline = " ".join(points)
        series_svg += f'<polyline points="{polyline}" fill="none" stroke="{color}" stroke-width="2"/>'

    legend_svg = ""
    lx = margin_l
    ly = margin_t + plot_h + 28
    for i, (lab_ar, lab_fr, _, color) in enumerate(series):
        x = lx + i * 150
        legend_svg += f'<line x1="{x}" y1="{ly}" x2="{x + 18}" y2="{ly}" stroke="{color}" stroke-width="2.5"/>'
        legend_svg += f'<circle cx="{x + 9}" cy="{ly}" r="2.5" fill="{color}"/>'
        legend_svg += f'<text x="{x + 22}" y="{ly + 3}" font-family="Cairo" font-size="9" fill="#1F2937">{lab_ar}</text>'

    axes = f'<line x1="{margin_l}" y1="{margin_t}" x2="{margin_l}" y2="{margin_t + plot_h}" stroke="#1F2937" stroke-width="0.8"/>'
    axes += f'<line x1="{margin_l}" y1="{margin_t + plot_h}" x2="{margin_l + plot_w}" y2="{margin_t + plot_h}" stroke="#1F2937" stroke-width="0.8"/>'

    cap_html = ""
    if caption_ar or caption_fr:
        cap_fr_html = f'<span class="cap-fr">{caption_fr}</span>' if caption_fr else ""
        cap_html = f'<div class="chart-caption">{caption_ar} {cap_fr_html}</div>'

    return f"""
<div class="chart-card">
    <div class="chart-title">{title_ar}</div>
    <div class="chart-subtitle">{title_fr}</div>
    <svg class="chart-svg" style="direction: ltr;" viewBox="0 0 {chart_w} {chart_h}" xmlns="http://www.w3.org/2000/svg">
        {grid_svg}
        {axes}
        {x_labels_svg}
        {series_svg}
        {legend_svg}
    </svg>
    {cap_html}
</div>
"""

# ==================================================================================
# CHART: HORIZONTAL PROGRESS BARS
# ==================================================================================
def progress_chart(title_ar, title_fr, items, caption_ar="", caption_fr=""):
    bar_h = 16
    gap = 6
    label_h = 22
    chart_w = 580
    n = len(items)
    chart_h = 25 + n * (bar_h + gap + label_h) + 15

    bars_svg = ""
    for i, (lab_ar, lab_fr, val, mx, color) in enumerate(items):
        y = 18 + i * (bar_h + gap + label_h)
        bars_svg += f'<text x="10" y="{y + 10}" font-family="Cairo" font-size="9" fill="#1F2937">{lab_ar}</text>'
        if lab_fr:
            bars_svg += f'<text x="10" y="{y + 20}" font-family="Inter" font-size="7" font-style="italic" fill="#6B7280">{lab_fr}</text>'
        bx = 220
        bw = 310
        bars_svg += f'<rect x="{bx}" y="{y + 6}" width="{bw}" height="{bar_h}" fill="#F3F4F6" rx="2.5"/>'
        fill_w = (val / mx) * bw if mx > 0 else 0
        bars_svg += f'<rect x="{bx}" y="{y + 6}" width="{fill_w}" height="{bar_h}" fill="{color}" rx="2.5"/>'
        bars_svg += f'<text x="{bx + bw + 8}" y="{y + 18}" font-family="Inter" font-size="10" font-weight="700" fill="#022c22">{val}</text>'

    cap_html = ""
    if caption_ar or caption_fr:
        cap_fr_html = f'<span class="cap-fr">{caption_fr}</span>' if caption_fr else ""
        cap_html = f'<div class="chart-caption">{caption_ar} {cap_fr_html}</div>'

    return f"""
<div class="chart-card">
    <div class="chart-title">{title_ar}</div>
    <div class="chart-subtitle">{title_fr}</div>
    <svg class="chart-svg" style="direction: ltr;" viewBox="0 0 {chart_w} {chart_h}" xmlns="http://www.w3.org/2000/svg">
        {bars_svg}
    </svg>
    {cap_html}
</div>
"""

# ==================================================================================
# DASHBOARD GRID
# ==================================================================================
def dashboard_grid(metrics):
    cards = ""
    for val, lab_ar, lab_fr in metrics:
        fr_html = f'<span class="fr">{lab_fr}</span>' if lab_fr else ""
        cards += f"""
        <div class="dashboard-card">
            <p class="dashboard-value">{val}</p>
            <p class="dashboard-label">{lab_ar}{fr_html}</p>
        </div>"""
    return f'<div class="dashboard-grid">{cards}</div>'

# ==================================================================================
# BACK COVER
# ==================================================================================
def back_cover(closing_ar, closing_fr, year="2025 / 2026"):
    return f"""
<!-- ============================ BACK COVER ============================ -->
<div class="back-cover">
    <div class="bc-top">
        <div class="insfp-mark">INSFP</div>
    </div>
    <div class="bc-center">
        <div class="closing-divider"></div>
        <div class="closing-ar">{closing_ar}</div>
        <div class="closing-fr">{closing_fr}</div>
        <div class="closing-divider"></div>
    </div>
    <div class="bc-bottom">
        <div class="closing-meta">
            تم إعداد هذا التقرير وفق المنهاج المعتمد في معاهد التكوين المهني الجزائرية<br>
            تحت رقم التخصص : التقني السامي في تصميم و صناعة الملابس — Tailleur Dames<br>
            <span class="meta-year">{year} • الجمهورية الجزائرية الديمقراطية الشعبية</span>
        </div>
    </div>
</div>
</body>
</html>
"""

# ==================================================================================
# MAIN CONTENT WRAPPER
# ==================================================================================
def main_content_open():
    return '<div class="page">'

def main_content_close():
    return '</div>'

# ==================================================================================
# BUILD COMPLETE MANUAL HTML
# ==================================================================================
def build_manual_html(module_num, module_num_label, title_ar, title_fr,
                      toc_items, body_sections_html,
                      closing_ar, closing_fr, year="2025 / 2026"):
    html = html_head(title_ar, title_fr)
    html += render_cover(module_num, module_num_label, title_ar, title_fr, year=year)
    html += render_toc(toc_items)
    html += main_content_open()
    html += body_sections_html
    html += main_content_close()
    html += back_cover(closing_ar, closing_fr, year=year)
    return html