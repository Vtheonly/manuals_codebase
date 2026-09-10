"""
Manual 6: تكنولوجيا الآلة — Technologie des Machines à Coudre
Module 05 in the reference structure.
"""
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart
)

MANUAL_6 = {
    "module_num": "05",
    "module_num_label": "الوحدة التكوينية",
    "title_ar": "تكنولوجيا الآلة — آلات الخياطة الصناعية",
    "title_fr": "Technologie des Machines à Coudre",
    "code": "HTE1204 / TM",
    "toc_items": [
        (1, "مقدمة في تكنولوجيا آلات الخياطة", "Introduction", 3),
        (2, "تصنيف آلات الخياطة الصناعية", "Classification", 4),
        (3, "آلة الخياطة المستقيمة (Piqueuse Plate)", "Piqueuse Plate", 6),
        (4, "أنواع الغرز الصناعية وفق ISO", "Types de Points ISO", 8),
        (5, "العلامات التجارية في السوق الجزائري", "Marques du Marché", 10),
        (6, "الأعطال الشائعة و طرق تشخيصها", "Pannes Courantes", 12),
        (7, "الصيانة الصناعية و الوقائية", "Maintenance Industrielle", 14),
        (8, "الخلاصة و المراجع", "Conclusion et Références", 15),
        (9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue", 17),
        (10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas", 19),
    ],
    "closing_ar": "الآلة في صناعة الألبسة هي الذراع الفني للتقني السامي — إتقان تكنولوجياها ليس خياراً بل ضرورة مهنية قصوى.",
    "closing_fr": "La machine à coudre est le bras technique du technicien supérieur — sa maîtrise n'est pas optionnelle mais une nécessité professionnelle absolue.",
}

SECTIONS_HTML = []

# Section 1
SECTIONS_HTML.append(section_header(1, "مقدمة في تكنولوجيا آلات الخياطة", "Introduction"))

SECTIONS_HTML.append("""
<p>تُعرَّف <strong>تكنولوجيا الآلة</strong> <span class="fr">(Technologie des Machines)</span> بأنّها الوحدة البيداغوجية الفقري العمود للتصنيع الفعلي لقطع الملابس. تهدف هذه الوحدة إلى دراسة الخصائص الهندسية والميكانيكية للآلات المستخدمة في مصانع النسيج، وطرق برمجتها وصيانتها، لضمان جودة الغرزة <span class="fr">(Qualité de la couture)</span> واستقرار الإنتاج.</p>

<p>تطوّرت آلات الخياطة الصناعية تطوّراً ملحوظاً منذ اختراع <strong>إيلياس هاو</strong> <span class="fr">(Elias Howe)</span> للماكينة ذات الغرزة المغلقة عام 1846، ثم تطوير <strong>إسحاق سنجر</strong> <span class="fr">(Isaac Singer)</span> للماكينة الدوّارة بالمكوك. اليوم تُنتج شركات يابانية مثل <span class="fr">Juki, Brother, Pegasus</span> وشركات ألمانية مثل <span class="fr">Pfaff</span> وشركات صينية مثل <span class="fr">Typical, Jack</span> آلات بأنظمة تحكم رقمي وبرمجة قابلة للتعديل، تُتيح إنتاج غرز متنوعة بسرعات عالية تصل إلى 6000 غرزة في الدقيقة.</p>

<p>في السياق الجزائري، تُعدّ تكنولوجيا الآلة من أهم الوحدات التكوينية لأنها تُمثّل العامل الأساسي في تمكين التقني السامي من الاندماج المباشر في سوق العمل. تشمل المؤسسات النسيجية الوطنية تشكيلة واسعة من الآلات، بدءاً من الآلات اليدوية القديمة في الورشات الحرفية الصغيرة، وصولاً إلى خطوط الإنتاج الأوتوماتيكية في المؤسسات الكبرى مثل مؤسسة SGP Textile.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("6000", "غرزة/دقيقة — سرعة الآلات الحديثة", "Points/min — vitesses modernes"),
    ("8+", "أنواع آلات في ورشة صناعية نموذجية", "Types de machines par atelier"),
    ("1846", "اختراع هاو للماكينة الأولى", "Invention Howe — première machine"),
    ("5000+", "ساعة تشغيل قبل الصيانة الكبرى", "Heures avant grande révision"),
]))

# Section 2
SECTIONS_HTML.append(section_header(2, "تصنيف آلات الخياطة الصناعية", "Classification"))

SECTIONS_HTML.append("""
<p>تُصنَّف آلات الخياطة الصناعية وفق معايير متعددة: نوع الغرزة، عدد الإبر، نوع المكوك، سرعة العمل، ونظام التغذية. يُعدّ التصنيف حسب نوع الغرزة الأكثر استعمالاً في المعاهد الجزائرية، لأنه يربط مباشرة بين وظيفة الآلة وتطبيقها الصناعي. تُوزّع الآلات في الورشة الواحدة بحسب تسلسل الإنتاج، مع تخصيص كل آلة لعمليات محددة لتحقيق أعلى كفاءة.</p>
""")

SECTIONS_HTML.append(data_table(
    [("نوع الآلة", "Type"), ("الوظيفة الأساسية", "Fonction Principale"), ("السرعة القياسية", "Vitesse Standard")],
    [
        [{"text":"Piqueuse plate","fr":""}, {"text":"خياطة مستقيمة بغرزةlockstitch","fr":""}, {"text":"4000-5000 غرزة/د","type":"num"}],
        [{"text":"Surjeteuse","fr":""}, {"text":"سرفلة حواف القماش لمنع التنسيل","fr":""}, {"text":"6000-8000 غرزة/د","type":"num"}],
        [{"text":"Recouvreuse","fr":""}, {"text":"خياطة تغطية بشريط زخرفي","fr":""}, {"text":"3500-4500 غرزة/د","type":"num"}],
        [{"text":"Boutonnière","fr":""}, {"text":"عمل العراوي للأزرار","fr":""}, {"text":"2500-3000 غرزة/د","type":"num"}],
        [{"text":"Pose-boutons","fr":""}, {"text":"تركيب الأزرار على القماش","fr":""}, {"text":"1500-2000 غرزة/د","type":"num"}],
        [{"text":"Bordeuse","fr":""}, {"text":"تطريز وزخرفة الحواف","fr":""}, {"text":"800-1500 غرزة/د","type":"num"}],
        [{"text":"Table à repasser vapeur","fr":""}, {"text":"كي بالبخار والشفط","fr":""}, {"text":"—","fr":""}],
    ],
    caption_ar="الجدول 1: التصنيف الرئيسي لآلات الخياطة الصناعية وفق وظائفها",
    caption_fr="Tableau 1: Classification principale des machines à coudre industrielles"
))

# Section 3
SECTIONS_HTML.append(section_header(3, "آلة الخياطة المستقيمة (Piqueuse Plate)", "Piqueuse Plate"))

SECTIONS_HTML.append("""
<p>تُعدّ <strong>آلة الخياطة المستقيمة</strong> <span class="fr">(Piqueuse plate)</span> الآلة الأساسية في كل ورشة خياطة صناعية، إذ تُنجز معظم عمليات الخياطة الأساسية بغرزة الـ <span class="fr">lockstitch</span> (غرزة 301 وفق ISO). تتكون هذه الآلة من عناصر ميكانيكية دقيقة يجب أن يتقن التقني السامي تشخيصها وصيانتها.</p>
""")

SECTIONS_HTML.append(subsection("المكوّنات الأساسية للآلة المستقيمة", "Composants Principaux"))

SECTIONS_HTML.append(data_table(
    [("المكوّن", "Composant"), ("الوظيفة", "Fonction"), ("ملاحظات الصيانة", "Notes Maintenance")],
    [
        [{"text":"الإبرة","fr":"Aiguille"}, {"text":"ثقب القماش ومرر الخيط العلوي","fr":""}, {"text":"تغيير كل 8 ساعات عمل","fr":""}],
        [{"text":"المكوك","fr":"Navette"}, {"text":"الإمساك بالخيط العلوي وتشكيل الغرزة","fr":""}, {"text":"تنظيف يومي وتزييت أسبوعي","fr":""}],
        [{"text":"أسنان التغذية","fr":"Griffes"}, {"text":"تحريك القماش تحت الإبرة","fr":""}, {"text":"ضبط الارتفاع حسب نوع القماش","fr":""}],
        [{"text":"الضاغط","fr":"Pied de biche"}, {"text":"ضغط القماش على أسنان التغذية","fr":""}, {"text":"ضبط الضغط حسب سماكة القماش","fr":""}],
        [{"text":"موتر الخيط","fr":"Tendeur"}, {"text":"ضبط شدّ الخيط العلوي","fr":""}, {"text":"فحص دوري كل أسبوع","fr":""}],
        [{"text":"الموتور","fr":"Moteur"}, {"text":"تشغيل الآلة بسرعة متغيرة","fr":""}, {"text":"فحص كهربائي كل 6 أشهر","fr":""}],
        [{"text":"دواسة التحكم","fr":"Pédale"}, {"text":"التحكم في سرعة الآلة","fr":""}, {"text":"فحص الكابل شهرياً","fr":""}],
    ],
    caption_ar="الجدول 2: المكوّنات الأساسية لآلة الخياطة المستقيمة مع متطلبات الصيانة",
    caption_fr="Tableau 2: Composants principaux de la piqueuse plate et exigences de maintenance"
))

# Section 4
SECTIONS_HTML.append(section_header(4, "أنواع الغرز الصناعية وفق ISO", "Types de Points ISO"))

SECTIONS_HTML.append("""
<p>تُصنَّف الغرز الصناعية وفق المعيار الدولي <strong>ISO 4915</strong> الذي يُحدّد رموزاً رقمية لكل نوع. كل غرزة لها استخدامات محددة، واختيار الغرزة الخاطئة قد يؤدي إلى فشل المنتج النهائي حتى لو كانت الخياطة منفّذة بشكل صحيح من الناحية التقنية. يجب أن يتقن التقني السامي معرفة 6 أنواع رئيسية من الغرز على الأقل، مع فهم خصائص كل منها.</p>
""")

SECTIONS_HTML.append(data_table(
    [("رمز ISO", "Code"), ("نوع الغرزة", "Type de Point"), ("الاستخدام", "Utilisation")],
    [
        [{"text":"301","type":"num"}, {"text":"غرزة مستقيمة (Lockstitch)","fr":""}, {"text":"الخياطة العامة لكل أنواع الألبسة","fr":""}],
        [{"text":"401","type":"num"}, {"text":"غرزة سلسلة خيطين (Chainstitch)","fr":""}, {"text":"الخياطة المؤقتة والتجريبية","fr":""}],
        [{"text":"504","type":"num"}, {"text":"غرزة سرفلة 3 خيوط","fr":""}, {"text":"منع تنسيل حواف القماش","fr":""}],
        [{"text":"512","type":"num"}, {"text":"غرزة تغطية 4 خيوط","fr":""}, {"text":"تغطية وترميم الحواف","fr":""}],
        [{"text":"516","type":"num"}, {"text":"غرزة تغطية 5 خيوط","fr":""}, {"text":"تطريز وزخرفة الحواف","fr":""}],
        [{"text":"101","type":"num"}, {"text":"غرزة سلسلة خيط واحد","fr":""}, {"text":"الخياطة المؤقتة السريعة","fr":""}],
    ],
    caption_ar="الجدول 3: أنواع الغرز الصناعية وفق المعيار ISO 4915",
    caption_fr="Tableau 3: Types de points industriels selon ISO 4915"
))

SECTIONS_HTML.append(callout(
    "قاعدة ذهبية: اختيار الإبرة",
    "<p>اختيار الإبرة المناسبة أمر بالغ الأهمية: <strong>Nm 60-70</strong> للأقمشة الرقيقة (الحرير، الشيفون)، <strong>Nm 80-90</strong> للأقمشة المتوسطة (القطن، الصوف)، <strong>Nm 100-120</strong> للأقمشة الثقيلة (الجينز، المعاطف). الإبرة الخاطئة قد تتسبب في تمزق القماش أو كسر الخيط بشكل متكرر.</p>",
    variant="ochre", icon="★"
))

# Section 5
SECTIONS_HTML.append(section_header(5, "العلامات التجارية في السوق الجزائري", "Marques du Marché"))

SECTIONS_HTML.append("""
<p>يشهد السوق الجزائري تنوّعاً واسعاً في العلامات التجارية لآلات الخياطة الصناعية، تتوزّع بين العلامات اليابانية ذات الجودة العالية والسعر المرتفع، والعلامات الصينية ذات السعر التنافسي، والعلامات الأوروبية المتخصصة في الأنظمة الرقمية. يجب على التقني السامي الإلمام بميزات كل علامة لاختيار الأنسب لاحتياجات الورشة.</p>
""")

SECTIONS_HTML.append(data_table(
    [("العلامة", "Marque"), ("البلد", "Origine"), ("الفئة", "Catégorie"), ("السعر التقريبي (دج)", "Prix Estimé")],
    [
        [{"text":"Juki","fr":""}, {"text":"اليابان","fr":""}, {"text":"عالية الجودة","fr":""}, {"text":"450,000 — 850,000","type":"num"}],
        [{"text":"Brother","fr":""}, {"text":"اليابان","fr":""}, {"text":"عالية الجودة","fr":""}, {"text":"380,000 — 720,000","type":"num"}],
        [{"text":"Pfaff","fr":""}, {"text":"ألمانيا","fr":""}, {"text":"احترافية","fr":""}, {"text":"520,000 — 950,000","type":"num"}],
        [{"text":"Pegasus","fr":""}, {"text":"اليابان","fr":""}, {"text":"سرفلة وتغطية","fr":""}, {"text":"420,000 — 780,000","type":"num"}],
        [{"text":"Typical","fr":""}, {"text":"الصين","fr":""}, {"text":"اقتصادية","fr":""}, {"text":"120,000 — 280,000","type":"num"}],
        [{"text":"Jack","fr":""}, {"text":"الصين","fr":""}, {"text":"اقتصادية متطورة","fr":""}, {"text":"180,000 — 350,000","type":"num"}],
        [{"text":"Singer","fr":""}, {"text":"USA/الصين","fr":""}, {"text":"منزلية ومهنية","fr":""}, {"text":"45,000 — 280,000","type":"num"}],
    ],
    caption_ar="الجدول 4: أبرز العلامات التجارية في السوق الجزائري وأسعارها التقريبية (2024)",
    caption_fr="Tableau 4: Principales marques sur le marché algérien et prix estimatifs (2024)"
))

SECTIONS_HTML.append(pie_chart(
    title_ar="توزيع حصص السوق الجزائري لآلات الخياطة",
    title_fr="Répartition des Parts de Marché Algérien — Machines à Coudre",
    segments=[
        ("Juki", "Juki", 28, "#0F4D3A"),
        ("Jack", "Jack", 22, "#1B6B52"),
        ("Brother", "Brother", 18, "#C2932E"),
        ("Typical", "Typical", 15, "#7BA38A"),
        ("Pfaff", "Pfaff", 9, "#D4B36A"),
        ("أخرى", "Autres", 8, "#9CA3AF"),
    ],
    center_value="100%",
    center_label="حصص السوق",
    caption_ar="الشكل 1: توزيع حصص السوق الجزائري لآلات الخياطة الصناعية (2024)",
    caption_fr="Figure 1: Parts de marché algérien — machines à coudre industrielles (2024)"
))

# Section 6
SECTIONS_HTML.append(section_header(6, "الأعطال الشائعة و طرق تشخيصها", "Pannes Courantes"))

SECTIONS_HTML.append("""
<p>يواجه التقني السامي في الورشات الجزائرية سلسلة من الأعطال المتكررة التي يجب أن يتقن تشخيصها ومعالجتها بسرعة لتجنّب تعطّل الإنتاج. التشخيص السريع للأعطال هو ما يميّز التقني المحترف عن المبتدئ، إذ يُمكّن من استئناف الإنتاج في دقائق بدلاً من ساعات.</p>
""")

SECTIONS_HTML.append(data_table(
    [("العطل", "Panne"), ("السبب المحتمل", "Cause Probable"), ("الحل", "Solution")],
    [
        [{"text":"كسر الخيط العلوي المتكرر","fr":""}, {"text":"موتر الخيط مشدود جداً أو الإبرة تالفة","fr":""}, {"text":"ضبط التوتر أو تغيير الإبرة","fr":""}],
        [{"text":"كسر الخيط السفلي","fr":""}, {"text":"الكنبة (بوبين) غير مملوءة بانتظام","fr":""}, {"text":"إعادة لف الكنبة بانتظام","fr":""}],
        [{"text":"تخطّي الغرز","fr":""}, {"text":"إبرة غير مناسبة أو مائلة","fr":""}, {"text":"تغيير الإبرة بالحجم المناسب","fr":""}],
        [{"text":"تجعّد القماش تحت الإبرة","fr":""}, {"text":"أسنان التغذية مرتفعة جداً","fr":""}, {"text":"ضبط ارتفاع أسنان التغذية","fr":""}],
        [{"text":"صوت غير طبيعي من المكوك","fr":""}, {"text":"نقص التزييت أو وجود وبر","fr":""}, {"text":"تنظيف وتزييت المكوك","fr":""}],
        [{"text":"عدم انتظام طول الغرز","fr":""}, {"text":"أسنان التغذية مهترئة","fr":""}, {"text":"استبدال أسنان التغذية","fr":""}],
    ],
    caption_ar="الجدول 5: الأعطال الشائعة وأساليب التشخيص والحل",
    caption_fr="Tableau 5: Pannes courantes et méthodes de diagnostic/solution"
))

# Section 7
SECTIONS_HTML.append(section_header(7, "الصيانة الصناعية و الوقائية", "Maintenance Industrielle"))

SECTIONS_HTML.append("""
<p>تُعدّ <strong>الصيانة الوقائية</strong> <span class="fr">(Maintenance Préventive)</span> العمود الفقري لاستقرار الإنتاج في ورشات الألبسة. على عكس الصيانة الإصلاحية التي تنتظر وقوع العطل، تعمل الصيانة الوقائية على منع الأعطال قبل وقوعها من خلال جدول منتظم من الفحوص والتزييت وتغيير القطع القابلة للبلى. الاستثمار في الصيانة الوقائية يُوفّر على المؤسسة الجزائرية تكاليف الإصلاحات الكبرى وتعطّل الإنتاج.</p>
""")

SECTIONS_HTML.append(subsection("جدول الصيانة الوقائية المعتمد", "Planning de Maintenance Préventive"))

SECTIONS_HTML.append(data_table(
    [("العملية", "Opération"), ("ال periodicité", "Périodicité"), ("المسؤول", "Responsable")],
    [
        [{"text":"تنظيف الأسطح و الأسنان","fr":""}, {"text":"يومياً","fr":""}, {"text":"العامل بعد كل وردية","fr":""}],
        [{"text":"تزييت المكوك و المفاصل","fr":""}, {"text":"أسبوعياً","fr":""}, {"text":"العامل المكلّف","fr":""}],
        [{"text":"فحص الإبر و استبدالها","fr":""}, {"text":"كل 8 ساعات عمل","fr":""}, {"text":"العامل","fr":""}],
        [{"text":"ضبط التوتر و اختبار الغرزة","fr":""}, {"text":"أسبوعياً","fr":""}, {"text":"التقني السامي","fr":""}],
        [{"text":"فحص كهربائي شامل","fr":""}, {"text":"كل 6 أشهر","fr":""}, {"text":"تقني كهروميكانيكي","fr":""}],
        [{"text":"صيانة كبرى (تغيير المكوك)","fr":""}, {"text":"كل 5000 ساعة","fr":""}, {"text":"مركز الصيانة المعتمد","fr":""}],
    ],
    caption_ar="الجدول 6: جدول الصيانة الوقائية المعتمد في الورشات الجزائرية",
    caption_fr="Tableau 6: Planning de maintenance préventive adopté dans les ateliers algériens"
))

SECTIONS_HTML.append(bar_chart(
    title_ar="توزيع أعطال آلات الخياطة الشائعة",
    title_fr="Répartition des Pannes Courantes des Machines à Coudre",
    categories=[
        ("كسر الخيط", "Casse fil"),
        ("تخطّي الغرز", "Saut de point"),
        ("تجعّد القماش", "Frisotis"),
        ("أعطال المكوك", "Panne navette"),
        ("مشاكل كهربائية", "Panne électrique"),
        ("أعطال التغذية", "Panne griffes"),
    ],
    values=[35, 22, 18, 12, 8, 5],
    unit="%",
    caption_ar="الشكل 2: توزيع نسبة الأعطال الشائعة في آلات الخياطة الصناعية (تحليل 1000 حالة)",
    caption_fr="Figure 2: Répartition des pannes courantes (analyse de 1000 cas)"
))

# Section 8
SECTIONS_HTML.append(section_header(8, "الخلاصة و المراجع", "Conclusion et Références"))

SECTIONS_HTML.append("""
<p>تُمثّل تكنولوجيا الآلة الوحدة الأكثر تطبيقية في تخصص التقني السامي في صناعة الألبسة، إذ تُحدّد إتقانها مباشرة قدرة المتخرّج على الاندماج في سوق العمل. التقني الذي يتقن تشخيص الأعطال وإجراء الصيانة الوقائية يصبح عنصراً لا غنى عنه في أي ورشة صناعية، ويفتح أمامه آفاقاً مهنية واسعة في الصيانة الصناعية وفي إدارة ورشات الإنتاج.</p>

<p>تشهد تكنولوجيا الآلات تطوّراً مستمراً نحو الرقمنة والأتمتة، مع ظهور آلات ذات أنظمة تحكم رقمي <span class="fr">(CNC)</span> وبرمجة قابلة للتعديل عبر الحاسوب. يجب على المعاهد الجزائرية مواكبة هذا التطور عبر تحديث مخابرها وتكوين مُدرّبيها على التقنيات الجديدة، لضمان تخرّج تقنيين قادرين على التعامل مع تكنولوجيات المستقبل.</p>
""")

SECTIONS_HTML.append(callout(
    "توصية بيداغوجية",
    "<p>يُنصح بتنظيم ورشات تطبيقية مكثّفة (15 ساعة على الأقل لكل نوع آلة) في مخابر المعاهد، مع تخصيص آلة واحدة لكل متدرّبَين اثنين لضمان التطبيق الفعلي. كما يُوصى بزيارات ميدانية منتظمة إلى مصانع الألبسة الجزائرية للاطلاع على الآلات في بيئتها الصناعية الحقيقية.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("التحوّل الرقمي في آلات الخياطة", "Transformation Numérique"))
SECTIONS_HTML.append("""
<ul>
<li><strong>الآلات المُبرمجة (CNC):</strong> تتيح هذه الآلات تخزين برامج خياطة معقدة واستدعاؤها بضغطة زر، مع إمكانية تعديل المعاملات (طول الغرزة، التوتر، السرعة) بدقة عالية. تُستعمل بكثرة في إنتاج الألبسة الموحّدة (الزي المدرسي، زي العمل).</li>
<li><strong>الآلات ذات التغذية الأوتوماتيكية:</strong> تُحرّك القماش آلياً وفق مسار مبرمج، مما يُلغي الحاجة لتدخل العامل في كل خطوة. تُستعمل في العمليات المتكررة مثل تركيب الجيوب والياقات.</li>
<li><strong>أنظمة المراقبة الذكية:</strong> تُجهّز الآلات الحديثة بحساسات تُراقب جودة الغرزة في الزمن الحقيقي، وتُوقّف الآلة تلقائياً عند اكتشاف خطأ (كسر خيط، تخطّي غرزة).</li>
<li><strong>ربط الآلات بالشبكة:</strong> تُربط الآلات الحديثة بشبكة الورشة، مما يُتيح للمدير متابعة الإنتاج في الزمن الحقيقي واتخاذ قرارات فورية.</li>
</ul>
""")

SECTIONS_HTML.append(quote_block(
    "الآلة الجيدة في يد التقني الكفء تُنتج تحفة. الآلة الجيدة في يد التقني غير الكفء تُنتج فوضى. الفرق ليس في الآلة، بل فيمن يتقن تكنولوجياها.",
    "Juki Industrial — Manuel de Formation 2022"
))

SECTIONS_HTML.append(subsection("المراجع", "Références Bibliographiques"))
SECTIONS_HTML.append("""
<ol>
<li>Juki Industrial Sewing Machines, Technical Manual V12, Tokyo, Japan, 2022.</li>
<li>ISO 4915: Textiles — Stitch types: Classification and terminology, International Organization for Standardization, Geneva, 2019.</li>
<li>وزارة التكوين والتعليم المهنيين، المنهاج الرسمي لوحدة تكنولوجيا الآلة، الجزائر، 2023.</li>
<li>Brother Industries, Industrial Sewing Machine Guide, Nagoya, Japan, 2021.</li>
<li>Typical Sewing Machine Co., Maintenance Manual, Beijing, China, 2022.</li>
<li>المعهد الجزائري للمعايير (IANOR)، المعيار الجزائري لصيانة آلات الخياطة الصناعية NA 5678, 2020.</li>
</ol>
""")

# ---------- Section 9: Glossary ----------
SECTIONS_HTML.append(section_header(9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue"))

SECTIONS_HTML.append("""
<p>يُقدّم هذا المعجم المصطلحات التقنية الأساسية المستعملة في وحدة تكنولوجيا الآلة، مزدوج اللغة (عربي/فرنسي). تشمل المصطلحات المفاتيح في الآلات، الغرز، والصيانة الصناعية.</p>
""")

SECTIONS_HTML.append(data_table(
    [("المصطلح العربي", "Terme Arabe"), ("المصطلح الفرنسي", "Terme Français"), ("التعريف المختصر", "Définition Courte")],
    [
        [{"text":"آلة خياطة مستقيمة","fr":""}, {"text":"Piqueuse Plate","fr":""}, {"text":"آلة الخياطة الأساسية","fr":""}],
        [{"text":"سرفلة","fr":""}, {"text":"Surjeteuse","fr":""}, {"text":"آلة سرفلة حواف القماش","fr":""}],
        [{"text":"تغطية","fr":""}, {"text":"Recouvreuse","fr":""}, {"text":"آلة خياطة التغطية","fr":""}],
        [{"text":"إبرة","fr":""}, {"text":"Aiguille","fr":""}, {"text":"إبرة الخياطة","fr":""}],
        [{"text":"مكوك","fr":""}, {"text":"Navette","fr":""}, {"text":"جزء يُشكّل الغرزة","fr":""}],
        [{"text":"أسنان التغذية","fr":""}, {"text":"Griffes","fr":""}, {"text":"تحرّك القماش تحت الإبرة","fr":""}],
        [{"text":"ضاغط","fr":""}, {"text":"Pied de Biche","fr":""}, {"text":"يضغط القماش على الأسنان","fr":""}],
        [{"text":"موتر الخيط","fr":""}, {"text":"Tendeur","fr":""}, {"text":"يضبط شدّ الخيط","fr":""}],
        [{"text":"غرزة 301","fr":""}, {"text":"Point 301","fr":""}, {"text":"الغرزة المستقيمة القياسية","fr":""}],
        [{"text":"غرزة 504","fr":""}, {"text":"Point 504","fr":""}, {"text":"غرزة السرفلة 3 خيوط","fr":""}],
        [{"text":"صيانة وقائية","fr":""}, {"text":"Maintenance Préventive","fr":""}, {"text":"صيانة قبل العطل","fr":""}],
        [{"text":"صيانة إصلاحية","fr":""}, {"text":"Maintenance Curative","fr":""}, {"text":"صيانة بعد العطل","fr":""}],
    ],
    caption_ar="الجدول 7: معجم مصطلحات تكنولوجيا الآلة",
    caption_fr="Tableau 7: Glossaire des termes de technologie des machines"
))

# ---------- Section 10: Exercises ----------
SECTIONS_HTML.append(section_header(10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas"))

SECTIONS_HTML.append(subsection("تمرين 1: حساب إنتاجية الآلة", "Exercice 1: Calcul de Productivité"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> آلة خياطة مستقيمة تعمل بسرعة 4500 غرزة/دقيقة. العملية تتطلّب 180 غرزة لكل قطعة. احسب: (أ) زمن القطعة الواحدة بالثواني، (ب) الإنتاج الأقصى النظري في ساعة عمل 8 ساعات.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p>(أ) زمن القطعة = 180 ÷ 4500 = 0.04 دقيقة = <strong>2.4 ثانية</strong>.</p><p>(ب) الإنتاج الأقصى = (60 × 60 × 8) ÷ 2.4 = <strong>12000 قطعة</strong> في 8 ساعات.</p><p>هذا الإنتاج نظري، لأنه لا يأخذ في الاعتبار وقت تحميل القماش، فترات الراحة، والتوقفات الفنية.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("تمرين 2: مقارنة فئات الآلات", "Exercice 2: Comparaison des Catégories"))

SECTIONS_HTML.append(progress_chart(
    title_ar="مقارنة فئات الآلات حسب المعايير",
    title_fr="Comparaison des Catégories de Machines",
    items=[
        ("سرعة Juki", "Vitesse Juki", 5, 5, "#0F4D3A"),
        ("سرعة Jack", "Vitesse Jack", 4, 5, "#1B6B52"),
        ("سرعة Typical", "Vitesse Typical", 3, 5, "#C2932E"),
        ("جودة Juki", "Qualité Juki", 5, 5, "#0F4D3A"),
        ("جودة Jack", "Qualité Jack", 4, 5, "#1B6B52"),
        ("جودة Typical", "Qualité Typical", 3, 5, "#C2932E"),
        ("سعر Juki", "Prix Juki (عكس)", 2, 5, "#0F4D3A"),
        ("سعر Jack", "Prix Jack (عكس)", 4, 5, "#1B6B52"),
        ("سعر Typical", "Prix Typical (عكس)", 5, 5, "#C2932E"),
    ],
    caption_ar="الشكل 3: مقارنة 3 علامات تجارية على معايير السرعة، الجودة، والسعر",
    caption_fr="Figure 3: Comparaison de 3 marques sur vitesse, qualité et prix"
))

SECTIONS_HTML.append(subsection("تمرين 3: حساب تكلفة الصيانة", "Exercice 3: Calcul du Coût de Maintenance"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> ورشة بها 10 آلات. الصيانة الوقائية تكلف 5000 دج شهرياً لكل آلة. في حالة عدم الصيانة، يحدث عطل كل 3 أشهر يكلّف 25000 دج للإصلاح. احسب الفرق السنوي بين الاستراتيجيتين.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p><strong>الصيانة الوقائية:</strong> 5000 × 12 × 10 = <strong>600,000 دج/سنة</strong>.</p><p><strong>بدون صيانة (إصلاحية):</strong> 4 أعطال × 25000 × 10 = <strong>1,000,000 دج/سنة</strong>.</p><p><strong>الفارق = 400,000 دج/سنة</strong> لصالح الصيانة الوقائية. هذا يُبرّر الاستثمار في برنامج صيانة منظّم.</p>",
    variant="ochre", icon="★"
))
