"""
==================================================================================
UNIFIED BLUEPRINT RUNTIME COMPILER
Compiles all 9 manuals using structured data inputs and modular design
==================================================================================
Author: Ouail Fati7a wa3il fati7a / وائل فتيحة
Version: 2.0 — Single-pass compilation, no more patch scripts
==================================================================================
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from manuals_template import build_manual_html
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart,
    timeline_chain, dashboard_grid
)

# Import all 9 manual content modules
from manual_01_couture_dame          import MANUAL_1, SECTIONS_HTML as S1
from manual_02_dossier_technique     import MANUAL_2, SECTIONS_HTML as S2
from manual_03_gradation             import MANUAL_3, SECTIONS_HTML as S3
from manual_04_moulage               import MANUAL_4, SECTIONS_HTML as S4
from manual_05_ost                   import MANUAL_5, SECTIONS_HTML as S5
from manual_06_technologie_machines  import MANUAL_6, SECTIONS_HTML as S6
from manual_07_technologie_textile   import MANUAL_7, SECTIONS_HTML as S7
from manual_08_protection_consommateur import MANUAL_8, SECTIONS_HTML as S8
from manual_09_entrepreneuriat       import MANUAL_9, SECTIONS_HTML as S9

MANUALS = [
    (MANUAL_1, S1, "01_couture_dame_tailleur_dames"),
    (MANUAL_2, S2, "02_dossier_technique"),
    (MANUAL_3, S3, "03_gradation"),
    (MANUAL_4, S4, "04_moulage"),
    (MANUAL_5, S5, "05_ost"),
    (MANUAL_6, S6, "06_technologie_machines"),
    (MANUAL_7, S7, "07_technologie_textile"),
    (MANUAL_8, S8, "08_protection_consommateur"),
    (MANUAL_9, S9, "09_entrepreneuriat"),
]

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output_builds")


# ==================================================================================
# REGISTRY-BASED COMPILATION (new single-pass approach)
# ==================================================================================
MANUAL_REGISTRY = {
    "01": {
        "title_ar": "الخياطة النسائية — Couture Dame",
        "title_fr": "Ladies Tailoring — Couture Dame",
        "code": "HTE1204/MQ1",
        "metrics": [("136 س", "الغلاف الساعي", "Volume Horaire"), ("38-40", "مقاس العينة", "Taille d'Échantillon"), ("مستوى IV", "الرتبة التأهيلية", "Niveau de Qualification")],
        "steps": [
            ("1", "تحليل البطاقة التقنية للموديل", "Analyse de la fiche technique"),
            ("2", "وضع واختيار الأنماط على الأقمشة", "Placement et coupe de tissu"),
            ("3", "تجميع وكي الأجزاء للحصول على المنتج النهائي", "Assemblage et finition"),
        ]
    },
    "02": {
        "title_ar": "إعداد الملف التقني — Dossier Technique",
        "title_fr": "Technical File — Dossier Technique",
        "code": "HTE1204/MQ2",
        "metrics": [("102 س", "الغلاف الساعي", "Volume Horaire"), ("±0.5 مم", "دقة التسامح المسموح بها", "Tolérance"), ("5 وثائق", "البنية النموذجية", "Structure Type")],
        "steps": [
            ("1", "توصيف نموذج المنتج الفني بدقة", "Fiche de style"),
            ("2", "بناء جدول القياسات التفصيلي للموديل", "Tableau de mesures"),
            ("3", "تحديد مراحل خط الإنتاج والتجميع", "Gamme de montage"),
        ]
    },
    "03": {
        "title_ar": "التدريج — الباترونات الصناعية",
        "title_fr": "Gradation / Scaling",
        "code": "HTE1204/MQ3",
        "metrics": [("112 س", "الغلاف الساعي", "Volume Horaire"), ("±0.1 مم", "دقة التدريج", "Précision"), ("6 مقاسات", "سلسلة الإنتاج", "Série de Tailles")],
        "steps": [
            ("1", "تحديد المقاس المرجعي ونظام المحاور", "Système d'axes cartésien"),
            ("2", "حساب قيم التطور لكل نقطة", "Calcul des valeurs d'évolution"),
            ("3", "رسم شبكة التدريج ومراقبة الجودة", "Tracé et contrôle qualité"),
        ]
    },
    "04": {
        "title_ar": "التفصيل بالقولبة — Moulage",
        "title_fr": "Moulage / Draping",
        "code": "HTE1204/MQ4",
        "metrics": [("136 س", "الغلاف الساعي", "Volume Horaire"), ("7 أدوات", "أساسيات القولبة", "Outils de Base"), ("3D → 2D", "الاستخراج المسطح", "Extraction à Plat")],
        "steps": [
            ("1", "تجهيز المانيكان بخطوط التشريح المرجعية", "Préparation du mannequin"),
            ("2", "تشكيل القماش وتثبيت البنسات", "Formage et épinglage"),
            ("3", "استخراج الباترون ونقله على الورق", "Extraction du patron"),
        ]
    },
    "05": {
        "title_ar": "التنظيم العلمي للعمل — OST",
        "title_fr": "Organisation Scientifique du Travail",
        "code": "HTE1204/MQ5",
        "metrics": [("77 س", "الغلاف الساعي", "Volume Horaire"), ("15-25%", "معامل الراحة", "Coefficient de Repos"), ("80%", "كفاءة خط الإنتاج", "Efficacité Ligne")],
        "steps": [
            ("1", "تحليل العمليات ودراسة الحركات", "Analyse des opérations"),
            ("2", "قياس الأزمنة بالكرونومتر (BTE)", "Chronométrage"),
            ("3", "موازنة الخط الإنتاجي وتحسين التدفق", "Équilibrage et optimisation"),
        ]
    },
    "06": {
        "title_ar": "تكنولوجيا الآلة — Machines",
        "title_fr": "Technologie des Machines",
        "code": "HTE1204/MQ6",
        "metrics": [("111 س", "الغلاف الساعي", "Volume Horaire"), ("301 ISO", "الغرزة المستقيمة", "Point Navette"), ("6 أنواع", "تصنيف الآلات", "Classification")],
        "steps": [
            ("1", "التعرف على أنواع آلات الخياطة الصناعية", "Identification des machines"),
            ("2", "تشخيص الأعطال الشائعة وإصلاحها", "Diagnostic des pannes"),
            ("3", "تنفيذ برنامج الصيانة الوقائية", "Maintenance préventive"),
        ]
    },
    "07": {
        "title_ar": "تكنولوجيا النسيج — Textile",
        "title_fr": "Technologie Textile",
        "code": "HTE1204/MQ7",
        "metrics": [("68 س", "الغلاف الساعي", "Volume Horaire"), ("3 أنواع", "الألياف النسيجية", "Fibres Textiles"), ("5 اختبارات", "مراقبة الجودة", "Contrôle Qualité")],
        "steps": [
            ("1", "التعرف على الألياف الطبيعية والصناعية", "Identification des fibres"),
            ("2", "تحليل بنية الأقمشة (السدى واللحمة)", "Analyse des armures"),
            ("3", "اختبارات الجودة الفيزيائية والكيميائية", "Tests de quality"),
        ]
    },
    "08": {
        "title_ar": "حماية المستهلك — Protection",
        "title_fr": "Protection du Consommateur",
        "code": "HTE1204/MQ8",
        "metrics": [("54 س", "الغلاف الساعي", "Volume Horaire"), ("5 قوانين", "الإطار التشريعي", "Cadre Législatif"), ("3 هيئات", "الرقابة وحماية المستهلك", "Organismes de Contrôle")],
        "steps": [
            ("1", "دراسة حقوق المستهلك في التشريع الجزائري", "Droits du consommateur"),
            ("2", "تحليل مواصفات الجودة والسلامة", "Normes de qualité"),
            ("3", "تقييم مطابقة المنتجات النسيجية", "Conformité des produits"),
        ]
    },
    "09": {
        "title_ar": "المقاولاتية — Entrepreneuriat",
        "title_fr": "Entrepreneuriat",
        "code": "HTE1204/MQ9",
        "metrics": [("77 س", "الغلاف الساعي", "Volume Horaire"), ("3 محاور", "مكونات المقاولاتية", "Axes Entrepreneuriat"), ("12 أسبوع", "مدة التربص", "Durée Stage")],
        "steps": [
            ("1", "تطوير الفكرة المقاولاتية ودراسة الجدوى", "Étude de faisabilité"),
            ("2", "بناء خطة العمل (Business Plan)", "Business Plan"),
            ("3", "إطلاق المشروع ومتابعة التسيير", "Lancement et gestion"),
        ]
    }
}


def compile_manual_registry(module_id, data):
    """
    New single-pass compiler — builds HTML from registry data + template components.
    """
    from manuals_template import (
        html_head, render_cover, render_toc, section_header, subsection,
        data_table, callout, flowchart, timeline_chain, dashboard_grid,
        stat_row, back_cover, main_content_open, main_content_close
    )

    css = """
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;700;900&family=Montserrat:ital,wght@0,300;0,400;0,600;0,700;1,400&display=swap');
    :root {
        --primary-deep: #022c22; --primary: #064e3b; --primary-light: #f0fdf4;
        --accent: #b45309; --accent-light: #fef3c7;
        --dark: #1e293b; --light: #f8fafc; --border: #cbd5e1;
        --font-ar: 'Cairo', sans-serif; --font-fr: 'Montserrat', sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    @page {
        size: A4;
        margin: 0; /* Fully blocks browser-injected header/footer print-lines */
    }
    
    html, body {
        margin: 0;
        padding: 0;
        width: 210mm;
        height: 297mm;
        background: #fff;
        color: var(--dark);
        line-height: 1.7;
        font-size: 11pt;
        font-family: var(--font-ar);
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
    
    .page {
        background: #fff;
        width: 210mm;
        height: 297mm;
        padding: 20mm 15mm;
        page-break-after: always;
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        position: relative;
    }
    
    @media screen {
        body { background: #e2e8f0; padding: 20px 0; }
        .page { margin: 0 auto 20px auto; box-shadow: 0 4px 15px rgba(0,0,0,0.06); }
    }
    
    .section-title-wrapper { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--primary); padding-bottom: 6px; margin-bottom: 20px; page-break-inside: avoid; }
    .section-title-ar { font-size: 1.4rem; font-weight: 800; color: var(--primary); }
    .section-title-fr { font-family: var(--font-fr); font-size: 0.85rem; font-weight: 700; color: var(--accent); text-transform: uppercase; }
    .dashboard-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0; }
    .dashboard-card { background: var(--light); border-right: 4px solid var(--primary); border-radius: 4px; padding: 15px; text-align: center; }
    .dashboard-value { font-size: 1.6rem; font-weight: 900; color: var(--accent); line-height: 1.2; }
    .dashboard-label { font-size: 0.85rem; font-weight: 700; color: var(--primary); }
    .timeline-chain { display: flex; flex-direction: column; gap: 15px; margin-bottom: 25px; position: relative; }
    .timeline-node { display: flex; gap: 15px; background: var(--light); border: 1px solid var(--border); border-radius: 6px; padding: 12px 18px; page-break-inside: avoid; }
    .node-index { background: var(--primary); color: white; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: var(--font-fr); }
    .node-content h4 { font-size: 0.95rem; font-weight: 700; color: var(--primary-deep); }
    .sub-section-title { font-size: 1.15rem; font-weight: 700; color: var(--primary-deep); border-right: 4px solid var(--accent); padding-right: 10px; margin: 20px 0 10px 0; page-break-inside: avoid; }
    .callout-box { background: var(--accent-light); border-right: 5px solid var(--accent); padding: 15px 20px; border-radius: 4px; margin-bottom: 20px; page-break-inside: avoid; }
    p { text-align: justify; color: var(--dark); margin-bottom: 12px; }
    .table-container { border: 1px solid var(--border); border-radius: 6px; overflow: hidden; margin-bottom: 25px; page-break-inside: avoid; }
    table { width: 100%; border-collapse: collapse; }
    th { background: var(--primary); color: white; font-weight: 700; font-size: 0.85rem; padding: 10px 14px; text-align: right; }
    td { padding: 10px 14px; font-size: 0.85rem; border-bottom: 1px solid var(--border); }
    tr:nth-child(even) { background-color: var(--light); }
    """

    html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<style>{css}</style>
</head>
<body>
"""

    # Cover
    html += f"""
    <div class="page">
        <div class="cover-container" style="border:4px double var(--primary);height:100%;padding:10mm;display:flex;flex-direction:column;justify-content:space-between;align-items:center;text-align:center;">
            <div class="header-block" style="width:100%;border-bottom:2px solid var(--accent);padding-bottom:8mm;">
                <p style="font-size:1.25rem;font-weight:700;color:var(--primary-deep);margin-bottom:3px;">الجمهورية الجزائرية الديمقراطية الشعبية</p>
                <p style="font-family:var(--font-fr);font-size:0.8rem;font-weight:600;letter-spacing:1px;color:var(--dark);direction:ltr;">République Algérienne Démocratique et Populaire</p>
                <p style="margin-top:5px;font-weight:700;">وزارة التكوين والتعليم المهنيين</p>
            </div>
            <div class="main-title-box" style="margin:30mm 0;">
                <span style="background:var(--accent);color:#fff;padding:6px 16px;font-size:0.9rem;font-weight:700;border-radius:30px;font-family:var(--font-fr);">N° {module_id} — {data['code']}</span>
                <h1 style="font-size:2.2rem;color:var(--primary);font-weight:900;margin:15px 0 8px 0;">{data['title_ar']}</h1>
                <h2 style="font-family:var(--font-fr);font-size:1.3rem;color:var(--accent);font-weight:400;">{data['title_fr']}</h2>
            </div>
            <div style="width:100%;text-align:right;">
                <p><strong>التخصص:</strong> نمذجة وتصميم الملابس (Modélisme et Design)</p>
                <p><strong>المستوى:</strong> تقني سامي — Technicien Supérieur</p>
                <p><strong>المتربص (ة):</strong> وعيل فتيحة / Wa3il Fatiha</p>
            </div>
        </div>
    </div>
    """

    # Main content page
    html += """
    <div class="page">
        <div class="section-title-wrapper">
            <div class="section-title-ar">01. أهداف الوحدة وبنية الكفاءة</div>
            <div class="section-title-fr">Objectifs & Compétences</div>
        </div>
        <p>تندرج هذه الوحدة ضمن البرنامج الوطني المعتمد من قبل <strong>وزارة التكوين والتعليم المهنيين</strong> لتأهيل تقنيين سامين لديهم القدرة الكاملة على العمل المباشر والمطابقة الفنية داخل الورشات الجزائرية.</p>
    """

    # Metrics dashboard
    html += '<div class="dashboard-grid">'
    for val, lbl_ar, lbl_fr in data['metrics']:
        html += f"""
            <div class="dashboard-card">
                <div class="dashboard-value">{val}</div>
                <div class="dashboard-label">{lbl_ar}<br><span style="font-family:var(--font-fr);font-size:0.75rem;color:#6b7280;font-style:italic;">{lbl_fr}</span></div>
            </div>
        """
    html += "</div>"

    # Steps timeline
    html += """
        <div class="sub-section-title">المسار العملي للإنجاز <span style="font-family:var(--font-fr);font-style:italic;font-size:0.95rem;color:var(--accent);">Séquence d'exécution</span></div>
        <div class="timeline-chain">
    """
    for num, ar, fr in data['steps']:
        html += f"""
            <div class="timeline-node">
                <div class="node-index">{num}</div>
                <div class="node-content">
                    <h4>{ar}</h4>
                    <p style="font-size:0.85rem;color:#475569;font-style:italic;">{fr}</p>
                </div>
            </div>
        """
    html += """
        </div>
    </div>
    </body>
    </html>
    """
    return html


def build_one(manual_meta, sections_html, filename):
    """Assemble one manual's HTML file (existing path)."""
    body = "\n".join(sections_html)
    html = build_manual_html(
        module_num       = manual_meta["module_num"],
        module_num_label = manual_meta["module_num_label"],
        title_ar         = manual_meta["title_ar"],
        title_fr         = manual_meta["title_fr"],
        toc_items        = manual_meta["toc_items"],
        body_sections_html = body,
        closing_ar       = manual_meta["closing_ar"],
        closing_fr       = manual_meta["closing_fr"],
        year             = "2025 / 2026",
    )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, filename + ".html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ Generated: {out_path}  ({len(html)//1024} KB)")
    return out_path


def main():
    print("=" * 70)
    print("  UNIFIED BLUEPRINT COMPILER — ALGERIAN VOCATIONAL MANUALS")
    print("  Author: Wa3il Fatiha / وائل فتيحة")
    print("=" * 70)

    # Path 1: Legacy module-based compilation (all 9 manuals)
    print("\n[1/2] Compiling 9 manuals from content modules...")
    paths = []
    for meta, secs, fname in MANUALS:
        p = build_one(meta, secs, fname)
        paths.append(p)

    # Path 2: New registry-based compilation (demonstration)
    print("\n[2/2] Compiling registry-based manuals (new single-pass)...")
    reg_paths = []
    for m_id in sorted(MANUAL_REGISTRY.keys()):
        data = MANUAL_REGISTRY[m_id]
        doc = compile_manual_registry(m_id, data)
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        out_path = os.path.join(OUTPUT_DIR, f"manual_{m_id}_registry.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(doc)
        print(f"  ✓ Generated: {out_path}  ({len(doc)//1024} KB)")
        reg_paths.append(out_path)

    print("\n" + "=" * 70)
    print(f"  ✓ ALL {len(paths)} MODULE-BASED + {len(reg_paths)} REGISTRY-BASED COMPILED")
    print(f"  → Output directory: {OUTPUT_DIR}")
    print("=" * 70)
    return paths + reg_paths


if __name__ == "__main__":
    main()