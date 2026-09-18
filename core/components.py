"""
core/components.py — Semantic HTML Component Renderer
"""
import html
from core.design import DESIGN

def esc(value: object) -> str:
    return html.escape(str(value), quote=True)

def cover_page(meta: dict) -> str:
    return f"""
    <div class="document-page cover-page-wrapper">
        <div class="border-outer-frame">
            <header class="admin-header-block">
                <h2 class="gov-title">{esc(meta.get("republic_ar", "الجمهورية الجزائرية الديمقراطية الشعبية"))}</h2>
                <h3 class="ministry-title">{esc(meta.get("ministry_ar", "وزارة التكــــوين والتعليـــم المهنـيين"))}</h3>
                <p class="institute-line">{esc(meta.get("center_1", ""))}</p>
                <p class="institute-line">{esc(meta.get("center_2", ""))}</p>
            </header>

            <div class="report-title-banner-area">
                <p class="purpose-title">{esc(meta.get("purpose", "- تقرير التربص للتكوين التكميلي ما قبل الترقية -"))}</p>
                <div class="rank-qualification-badge">{esc(meta.get("rank_title", "لرتبة: أستاذ متخصص في التكوين والتعليم المهنيين من الدرجة الأولى"))}</div>
                
                <div class="main-topic-gradient-card">
                    <p class="topic-pre-title">{esc(meta.get("topic_label", "تقرير التربص حول:"))}</p>
                    <h1 class="topic-headline-ar">{esc(meta.get("topic_title_ar", ""))}</h1>
                    <h2 class="topic-subline-fr">{esc(meta.get("topic_title_fr", ""))}</h2>
                    <div class="module-code-pill">الغلاف الساعي {esc(meta.get("volume_hours", ""))} — {esc(meta.get("module_code", ""))}</div>
                </div>
            </div>

            <div class="trainee-info-card">
                <div class="trainee-info-row"><span class="field-label">الاســــم واللقــــب</span><span class="field-separator">:</span><span class="field-value trainee-name">{esc(meta.get("trainee_name", ""))}</span></div>
                <div class="trainee-info-row"><span class="field-label">الشعـــــــــبة</span><span class="field-separator">:</span><span class="field-value">{esc(meta.get("branch", ""))}</span></div>
                <div class="trainee-info-row"><span class="field-label">التخصـــــــص</span><span class="field-separator">:</span><span class="field-value">{esc(meta.get("specialty", ""))}</span></div>
                <div class="trainee-info-row"><span class="field-label">المؤسســــــــة</span><span class="field-separator">:</span><span class="field-value">{esc(meta.get("institution", ""))} <small>({esc(meta.get("institution_sub", ""))})</small></span></div>
                <div class="trainee-info-row"><span class="field-label">الولايـــــــــة</span><span class="field-separator">:</span><span class="field-value">{esc(meta.get("wilaya", ""))}</span></div>
                <div class="trainee-info-row"><span class="field-label">المعهد صاحب الاختصاص</span><span class="field-separator">:</span><span class="field-value">{esc(meta.get("accredited_institute", ""))}</span></div>
            </div>

            <footer class="cover-footer-block">
                <div class="promo-batch-badge">الـدفـعـــــــــــــــة : {esc(meta.get("batch_number", "12"))}</div>
                <p class="season-text">الموسم التكويني: {esc(meta.get("training_season", "2025/2026"))}</p>
            </footer>
        </div>
    </div>
    """

def table_of_contents(toc_items: list, appendix_items: list, module_code: str, season: str) -> str:
    rows = []
    for it in toc_items:
        rows.append(f"""
        <li class="toc-entry">
            <span class="toc-badge-num">{it["num"]}</span>
            <div class="toc-text-wrap">
                <span class="toc-ar-title">{esc(it["title_ar"])}</span>
                <span class="toc-fr-title">{esc(it.get("title_fr", ""))}</span>
            </div>
            <span class="toc-dotted-leader"></span>
            <span class="toc-page-target">{it["page"]}</span>
        </li>
        """)
        
    appendix = []
    for it in appendix_items:
        appendix.append(f"""
        <li class="toc-entry appendix-entry">
            <span class="toc-badge-num appendix-badge">{esc(it["char"])}</span>
            <div class="toc-text-wrap">
                <span class="toc-ar-title">{esc(it["title_ar"])}</span>
                <span class="toc-fr-title">{esc(it.get("title_fr", ""))}</span>
            </div>
            <span class="toc-dotted-leader"></span>
            <span class="toc-page-target">{it["page"]}</span>
        </li>
        """)

    return f"""
    <div class="document-page content-page">
        <header class="toc-header-area">
            <h2 class="toc-main-title">فهرس المحتويات</h2>
            <p class="toc-subtitle-fr">Table des Matières</p>
        </header>
        <ul class="toc-list">{''.join(rows)}</ul>
        <div class="toc-divider"></div>
        <ul class="toc-list">{''.join(appendix)}</ul>
        <footer class="running-footer">
            <span class="footer-season">الموسم التكويني {esc(season)}</span>
            <span class="footer-page">2</span>
            <span class="footer-module">{esc(module_code)}</span>
        </footer>
    </div>
    """

def back_cover(meta: dict) -> str:
    return f"""
    <div class="document-page back-cover-page">
        <header class="bc-header">
            <h2 class="bc-ministry-ar">{esc(meta.get("ministry_ar", "وزارة التكوين والتعليم المهنيين"))}</h2>
            <p class="bc-ministry-fr">MINISTÈRE DE LA FORMATION ET DE L'ENSEIGNEMENT PROFESSIONNELS</p>
        </header>
        <main class="bc-quote-block">
            <div class="bc-gold-rule"></div>
            <p class="bc-quote-ar">{esc(meta.get("closing_quote_ar", ""))}</p>
            <p class="bc-quote-fr">{esc(meta.get("closing_quote_fr", ""))}</p>
            <div class="bc-gold-rule"></div>
        </main>
        <footer class="bc-meta-block">
            <p class="bc-meta-statement">أُنجز هذا التقرير في إطار التربص للتكوين التكميلي ما قبل الترقية</p>
            <p class="bc-meta-details">الشعبة: {esc(meta.get("branch", ""))} — التخصص: {esc(meta.get("specialty", ""))} — المعهد صاحب الاختصاص: {esc(meta.get("accredited_institute", ""))}</p>
            <p class="bc-meta-legal">المرجعية: المعايير الجزائرية IANOR والقوانين المنشورة في الجريدة الرسمية JORADP ومرجعيات MFEP / INFEP</p>
            <p class="bc-meta-batch">الموسم التكويني: {esc(meta.get("training_season", "2025/2026"))} • الدفعة {esc(meta.get("batch_number", "12"))}</p>
        </footer>
    </div>
    """

def table(block: dict) -> str:
    head = "".join(f"<th>{esc(x[0])}<span class='th-sub'>{esc(x[1]) if len(x)>1 else ''}</span></th>" if isinstance(x, list) else f"<th>{esc(x)}</th>" for x in block["columns"])
    rows = []
    for r in block["rows"]:
        tds = []
        for cell in r:
            if isinstance(cell, dict):
                cls = "num-cell" if cell.get("numeric") else "text-cell"
                sub = f'<span class="td-sub">{esc(cell["sub"])}</span>' if "sub" in cell else ""
                tds.append(f'<td class="{cls}">{esc(cell.get("text", ""))} {sub}</td>')
            else:
                tds.append(f'<td>{esc(cell)}</td>')
        rows.append(f"<tr>{''.join(tds)}</tr>")
        
    sub_hdr = f"""<div class="section-sub-header"><h4 class="sub-title-ar">{esc(block["title"])}</h4><span class="sub-title-fr">— {esc(block.get("subtitle_fr", ""))}</span></div>""" if "title" in block else ""
    caption_html = f'<div class="chart-caption"><span>{esc(block.get("caption_ar", ""))}</span> — <span class="fr">{esc(block.get("caption_fr", ""))}</span></div>' if "caption_ar" in block else ""

    return f"""
    <section class="artifact table-artifact-container">
        {sub_hdr}
        <table class="standard-data-table">
            <thead><tr>{head}</tr></thead>
            <tbody>{''.join(rows)}</tbody>
        </table>
        {caption_html}
    </section>
    """

def callout(block: dict) -> str:
    variant = block.get("variant", "accent")
    icon = block.get("icon", "★")
    cls = "callout-primary" if variant == "primary" else "callout-accent"
    return f"""
    <aside class="artifact callout-box {cls}">
        <div class="callout-badge-header">
            <span class="callout-icon">{icon}</span>
            <span class="callout-title">{esc(block["title"])}</span>
        </div>
        <div class="callout-body">{block.get("content", "")}</div>
    </aside>
    """

def stat_row(block: dict) -> str:
    cards = []
    for it in block.get("items", []):
        cards.append(f"""
        <div class="stat-card">
            <div class="stat-number">{esc(it["number"])}</div>
            <div class="stat-label-ar">{esc(it["label_ar"])}</div>
            <div class="stat-label-fr">{esc(it.get("label_fr", ""))}</div>
        </div>
        """)
    return f'<div class="stat-row-grid">{"".join(cards)}</div>'

def text_block(block: dict) -> str:
    role = block.get("role", "body")
    if role == "subsection":
        return f'<div class="section-sub-header"><h4 class="sub-title-ar">{esc(block["text"])}</h4><span class="sub-title-fr">— {esc(block.get("subtitle_fr", ""))}</span></div>'
    if role == "quote":
        author = f'<span class="quote-author">— {esc(block["author"])}</span>' if "author" in block else ""
        return f'<blockquote class="quote-block-content">{esc(block["text"])}{author}</blockquote>'
    return f'<p class="body-text">{block.get("text", "")}</p>'

def render_block(block: dict) -> str:
    kind = block.get("type")
    if kind == "text": return text_block(block)
    if kind == "table": return table(block)
    if kind == "callout": return callout(block)
    if kind == "stats": return stat_row(block)
    raise ValueError(f"Unsupported block type: {kind}")