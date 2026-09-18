"""
generators/html.py — Complete Document Assembly & CSS
"""
from core.design import DESIGN
from core.components import cover_page, table_of_contents, back_cover

def stylesheet() -> str:
    d = DESIGN; p = d.palette; ty = d.typography; s = d.spacing; b = d.borders
    return f"""
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:ital,wght@0,400;0,600;0,700;1,400&display=swap');
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    @page {{ size: A4 portrait; margin: 0; }}
    @media print {{
        body {{ background: transparent !important; margin: 0 !important; }}
        .document-page {{ box-shadow: none !important; margin: 0 !important; page-break-after: always !important; break-after: page !important; }}
    }}
    body {{ background: #e2e8f0; font-family: {ty.arabic}; color: {p.text}; direction: rtl; text-align: right; display: flex; flex-direction: column; align-items: center; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    .document-page {{ width: {d.page.width}; height: {d.page.height}; background: {p.surface}; padding: {s.page_y} {s.page_x}; box-shadow: 0 4px 20px rgba(0,0,0,0.08); position: relative; display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 20px; }}
    .cover-page-wrapper {{ padding: 10mm; }}
    .border-outer-frame {{ border: {b.frame_width} solid {p.primary}; border-radius: {b.radius_sm}; height: 100%; padding: 10mm 12mm; display: flex; flex-direction: column; justify-content: space-between; }}
    .admin-header-block {{ text-align: center; }}
    .gov-title {{ font-size: {ty.sizes["xl"]}; font-weight: {ty.weights["heavy"]}; color: {p.primary_deep}; margin-bottom: 2px; }}
    .ministry-title {{ font-size: {ty.sizes["lg"]}; font-weight: {ty.weights["bold"]}; color: {p.primary}; margin-bottom: 4px; }}
    .institute-line {{ font-size: {ty.sizes["base"]}; font-weight: {ty.weights["medium"]}; color: {p.muted}; }}
    .report-title-banner-area {{ text-align: center; margin: 8px 0; }}
    .purpose-title {{ font-size: {ty.sizes["md"]}; font-weight: {ty.weights["bold"]}; color: {p.text_dark}; margin-bottom: 6px; }}
    .rank-qualification-badge {{ display: inline-block; background: {p.surface_alt}; border: 1px dashed {p.primary}; padding: 4px 18px; border-radius: {b.pill}; font-size: {ty.sizes["sm"]}; font-weight: {ty.weights["bold"]}; color: {p.primary}; margin-bottom: 10px; }}
    .main-topic-gradient-card {{ background: linear-gradient(135deg, {p.banner_start} 0%, {p.banner_end} 100%); border: 1.5px solid {p.banner_border}; border-radius: {b.radius_lg}; padding: {s.card}; }}
    .topic-pre-title {{ font-size: {ty.sizes["md"]}; font-weight: {ty.weights["bold"]}; color: {p.banner_text}; margin-bottom: 4px; }}
    .topic-headline-ar {{ font-size: {ty.sizes["2xl"]}; font-weight: {ty.weights["black"]}; color: {p.banner_text}; line-height: 1.25; margin-bottom: 4px; }}
    .topic-subline-fr {{ font-family: {ty.latin}; font-size: {ty.sizes["sm"]}; font-style: italic; color: {p.primary}; direction: ltr; margin-bottom: 8px; }}
    .module-code-pill {{ display: inline-block; background: {p.surface}; color: {p.primary_deep}; padding: 3px 14px; border-radius: {b.pill}; font-size: {ty.sizes["xs"]}; font-weight: {ty.weights["bold"]}; }}
    .trainee-info-card {{ border: 1.5px solid {p.border}; border-radius: {b.radius_lg}; padding: 16px 22px; background: {p.surface}; display: flex; flex-direction: column; gap: 9px; }}
    .trainee-info-row {{ display: flex; align-items: baseline; font-size: {ty.sizes["base"]}; }}
    .field-label {{ width: 190px; font-weight: {ty.weights["bold"]}; color: {p.primary}; flex-shrink: 0; }}
    .field-separator {{ width: 20px; text-align: center; font-weight: {ty.weights["bold"]}; color: {p.primary}; }}
    .field-value {{ flex-grow: 1; font-weight: {ty.weights["medium"]}; }}
    .trainee-name {{ font-weight: {ty.weights["heavy"]}; color: {p.primary_deep}; font-size: {ty.sizes["md"]}; }}
    .cover-footer-block {{ text-align: center; }}
    .promo-batch-badge {{ display: inline-block; background: linear-gradient(135deg, {p.banner_start} 0%, {p.banner_end} 100%); border: 1px solid {p.banner_border}; padding: 5px 35px; border-radius: {b.radius_sm}; font-size: {ty.sizes["md"]}; font-weight: {ty.weights["heavy"]}; color: {p.banner_text}; margin-bottom: 6px; }}
    .season-text {{ font-size: {ty.sizes["xs"]}; font-weight: 600; color: {p.muted}; }}
    .toc-header-area {{ text-align: center; border-bottom: 2px solid {p.primary}; padding-bottom: 8px; margin-bottom: 16px; }}
    .toc-main-title {{ font-size: {ty.sizes["2xl"]}; font-weight: {ty.weights["black"]}; color: {p.primary_deep}; }}
    .toc-subtitle-fr {{ font-family: {ty.latin}; font-style: italic; font-size: {ty.sizes["sm"]}; color: {p.accent}; direction: ltr; }}
    .toc-list {{ list-style: none; display: flex; flex-direction: column; gap: 11px; }}
    .toc-entry {{ display: flex; align-items: center; font-size: {ty.sizes["base"]}; }}
    .toc-badge-num {{ background: {p.primary}; color: #fff; width: 22px; height: 22px; line-height: 22px; border-radius: 50%; text-align: center; font-family: {ty.latin}; font-weight: {ty.weights["bold"]}; font-size: {ty.sizes["xs"]}; margin-left: 10px; flex-shrink: 0; }}
    .appendix-badge {{ background: {p.accent}; }}
    .toc-text-wrap {{ display: flex; flex-direction: column; }}
    .toc-ar-title {{ font-weight: {ty.weights["bold"]}; color: {p.text_dark}; }}
    .toc-fr-title {{ font-family: {ty.latin}; font-style: italic; font-size: 7.5pt; color: {p.muted}; direction: ltr; text-align: right; }}
    .toc-dotted-leader {{ flex-grow: 1; border-bottom: 1px dotted {p.border}; margin: 0 10px; height: 1px; }}
    .toc-page-target {{ font-family: {ty.latin}; font-weight: {ty.weights["bold"]}; color: {p.primary}; font-size: {ty.sizes["base"]}; }}
    .toc-divider {{ height: 1px; background: {p.border_light}; margin: 12px 0; }}
    .running-footer {{ display: flex; justify-content: space-between; align-items: center; border-top: 1px solid {p.border_light}; padding-top: 6px; font-size: {ty.sizes["xs"]}; color: {p.muted}; font-family: {ty.latin}; direction: ltr; }}
    .footer-season {{ direction: rtl; font-family: {ty.arabic}; }}
    .footer-page {{ font-weight: {ty.weights["bold"]}; color: {p.text_dark}; }}
    .section-main-header {{ display: flex; align-items: center; margin-bottom: 12px; border-bottom: 2px solid {p.primary}; padding-bottom: 6px; }}
    .section-circle-badge {{ background: {p.primary}; color: #fff; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: {ty.weights["bold"]}; font-family: {ty.latin}; margin-left: 10px; }}
    .section-headline-ar {{ font-size: {ty.sizes["lg"]}; font-weight: {ty.weights["heavy"]}; color: {p.primary_deep}; }}
    .section-sub-fr {{ display: block; font-family: {ty.latin}; font-style: italic; font-size: {ty.sizes["xs"]}; color: {p.accent}; direction: ltr; text-align: right; }}
    .section-sub-header {{ display: flex; align-items: baseline; gap: 8px; border-right: 3.5px solid {p.accent}; padding-right: 8px; margin: 12px 0 8px 0; }}
    .sub-title-ar {{ font-size: {ty.sizes["md"]}; font-weight: {ty.weights["bold"]}; color: {p.primary_deep}; }}
    .sub-title-fr {{ font-family: {ty.latin}; font-style: italic; font-size: {ty.sizes["xs"]}; color: {p.muted}; direction: ltr; }}
    p.body-text {{ font-size: {ty.sizes["base"]}; line-height: {ty.line_height["normal"]}; text-align: justify; margin-bottom: 10px; }}
    table.standard-data-table {{ width: 100%; border-collapse: collapse; font-size: {ty.sizes["sm"]}; border: 1px solid {p.border}; margin: 8px 0; }}
    table.standard-data-table thead {{ background: {p.primary}; color: #fff; }}
    table.standard-data-table th {{ padding: {s.cell}; font-weight: {ty.weights["bold"]}; text-align: right; border: 1px solid {p.primary_deep}; }}
    table.standard-data-table th .th-sub {{ display: block; font-family: {ty.latin}; font-style: italic; font-size: 7pt; opacity: 0.85; direction: ltr; }}
    table.standard-data-table td {{ padding: {s.cell}; border: 1px solid {p.border_light}; line-height: 1.4; }}
    table.standard-data-table tbody tr:nth-child(even) {{ background: {p.surface_alt}; }}
    td.num-cell {{ text-align: center; font-family: {ty.latin}; font-weight: {ty.weights["bold"]}; color: {p.primary_deep}; direction: ltr; }}
    td .td-sub {{ display: block; font-family: {ty.latin}; font-size: 7.5pt; color: {p.muted}; direction: ltr; }}
    .callout-box {{ padding: 12px 16px; border-radius: {b.radius_md}; margin: 12px 0; border-right: 4px solid; }}
    .callout-accent {{ background: {p.accent_light}; border-color: {p.accent}; }}
    .callout-primary {{ background: {p.primary_light}; border-color: {p.primary}; }}
    .callout-badge-header {{ display: flex; align-items: center; gap: 8px; font-weight: {ty.weights["bold"]}; font-size: {ty.sizes["base"]}; margin-bottom: 6px; }}
    .callout-accent .callout-badge-header {{ color: {p.accent}; }}
    .callout-primary .callout-badge-header {{ color: {p.primary_deep}; }}
    .callout-body {{ font-size: {ty.sizes["sm"]}; line-height: {ty.line_height["normal"]}; }}
    .flowchart-container {{ margin: 12px 0; background: {p.surface_alt}; border: 1px solid {p.border_light}; padding: 14px; border-radius: {b.radius_md}; }}
    .flow-step-node {{ display: flex; align-items: center; gap: 12px; }}
    .step-circle {{ width: 24px; height: 24px; background: {p.primary}; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: {ty.latin}; font-weight: {ty.weights["bold"]}; font-size: {ty.sizes["xs"]}; flex-shrink: 0; }}
    .step-text-ar {{ font-size: {ty.sizes["sm"]}; font-weight: {ty.weights["bold"]}; color: {p.text_dark}; }}
    .step-text-fr {{ font-family: {ty.latin}; font-style: italic; font-size: 7.5pt; color: {p.muted}; direction: ltr; text-align: right; }}
    .flow-step-arrow {{ text-align: right; padding-right: 7px; color: {p.accent}; font-size: 9pt; margin: 2px 0; }}
    .stat-row-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin: 12px 0; }}
    .stat-card {{ background: {p.surface}; border: 1px solid {p.border_light}; border-top: 3px solid {p.accent}; padding: 10px; text-align: center; border-radius: {b.radius_sm}; }}
    .stat-number {{ font-size: {ty.sizes["xl"]}; font-weight: {ty.weights["black"]}; color: {p.primary_deep}; font-family: {ty.latin}; direction: ltr; }}
    .stat-label-ar {{ font-size: {ty.sizes["xs"]}; font-weight: {ty.weights["bold"]}; color: {p.text}; margin-top: 2px; }}
    .stat-label-fr {{ font-size: 6.5pt; font-family: {ty.latin}; font-style: italic; color: {p.muted}; direction: ltr; }}
    .chart-container {{ margin: 12px 0; padding: 10px; border: 1px solid {p.border_light}; border-radius: {b.radius_md}; background: {p.surface}; }}
    .chart-header {{ text-align: center; margin-bottom: 6px; }}
    .chart-title-ar {{ font-size: {ty.sizes["base"]}; font-weight: {ty.weights["bold"]}; color: {p.primary_deep}; }}
    .chart-title-fr {{ font-family: {ty.latin}; font-style: italic; font-size: {ty.sizes["xs"]}; color: {p.muted}; direction: ltr; }}
    .svg-viewport {{ width: 100%; max-height: 240px; display: block; margin: 0 auto; }}
    .chart-caption {{ text-align: center; font-size: 7.5pt; font-weight: {ty.weights["bold"]}; color: {p.primary}; margin-top: 6px; }}
    .chart-caption .fr {{ font-family: {ty.latin}; font-style: italic; font-weight: normal; color: {p.muted}; direction: ltr; }}
    .back-cover-page {{ background: {p.primary_deep}; color: #fff; padding: 18mm 16mm; display: flex; flex-direction: column; justify-content: space-between; text-align: center; }}
    .bc-header {{ border-bottom: 1.5px solid {p.accent}; padding-bottom: 12px; }}
    .bc-ministry-ar {{ font-size: {ty.sizes["xl"]}; font-weight: {ty.weights["heavy"]}; color: #fff; }}
    .bc-ministry-fr {{ font-family: {ty.latin}; font-size: 8pt; letter-spacing: 1.5px; color: {p.banner_start}; margin-top: 4px; direction: ltr; }}
    .bc-quote-block {{ max-width: 155mm; margin: 0 auto; }}
    .bc-gold-rule {{ width: 45mm; height: 2px; background: {p.accent}; margin: 16px auto; }}
    .bc-quote-ar {{ font-size: {ty.sizes["lg"]}; font-weight: {ty.weights["bold"]}; line-height: {ty.line_height["relaxed"]}; margin-bottom: 10px; color: #f8fafc; }}
    .bc-quote-fr {{ font-family: {ty.latin}; font-style: italic; font-size: {ty.sizes["sm"]}; color: #cbd5e1; direction: ltr; line-height: 1.5; }}
    .bc-meta-block {{ border-top: 1.5px solid {p.accent}; padding-top: 12px; font-size: {ty.sizes["xs"]}; color: #94a3b8; line-height: 1.6; }}
    .bc-meta-batch {{ color: {p.accent}; font-weight: {ty.weights["bold"]}; margin-top: 6px; }}
    """

def render(report: dict, artifact_html: dict) -> str:
    meta = report.get("metadata", {})
    code = meta.get("module_code", "")
    season = meta.get("training_season", "")

    pages = [cover_page(meta)]
    pages.append(table_of_contents(report.get("toc", []), report.get("appendix_toc", []), code, season))

    page_counter = 3
    for s in report["sections"]:
        body = []
        # ترويسة القسم الرئيسي
        body.append(f"""
        <div class="section-main-header">
            <div class="section-circle-badge">{s.get("num", "")}</div>
            <div>
                <h3 class="section-headline-ar">{s["title"]}</h3>
                <span class="section-sub-fr">{s.get("subtitle_fr", "")}</span>
            </div>
        </div>
        """)

        for index, block in enumerate(s.get("blocks", []), 1):
            if block.get("type") == "artifact_ref":
                body.append(artifact_html[block["artifact_id"]])
            else:
                body.append(artifact_html[f'{s["id"]}-block-{index}'])

        footer = f"""
        <footer class="running-footer">
            <span class="footer-season">الموسم التكويني {season}</span>
            <span class="footer-page">{page_counter}</span>
            <span class="footer-module">{code}</span>
        </footer>
        """
        page_counter += 1

        pages.append(f"""
        <main class="document-page content-page">
            <div class="page-content-wrapper">{''.join(body)}</div>
            {footer}
        </main>
        """)

    pages.append(back_cover(meta))
    return f"""<!doctype html>
<html lang="{report.get('language', 'ar')}" dir="rtl">
<head>
    <meta charset="utf-8">
    <title>{report['title']}</title>
    <style>{stylesheet()}</style>
</head>
<body>
    {''.join(pages)}
</body>
</html>
"""