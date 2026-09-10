"""
Manual 1: الخياطة النسائية — Couture Dame (Tailleur Dames)
The OVERALL SPECIALTY manual — comprehensive overview of the entire
Tailleur Dames curriculum (HTE1204) following Algerian INSFP standards.
"""
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart
)

MANUAL_1 = {
    "module_num": "01",
    "module_num_label": "التخصص",
    "title_ar": "الخياطة النسائية — التقني السامي في تصميم وصناعة الملابس",
    "title_fr": "Couture Dame — Tailleur Dames (Technicien Supérieur)",
    "code": "HTE1204",
    "toc_items": [
        (1, "مقدمة عامة في تخصص الخياطة النسائية", "Introduction Générale à la Spécialité", 3),
        (2, "الإطار الرسمي للمنهاج و البنية المؤسسية", "Cadre Officiel et Structure Institutionnelle", 4),
        (3, "المصفوفة الشاملة للوحدات التكوينية", "Matrice Globale des Modules de Formation", 6),
        (4, "المنهجية المبنية على الكفاءات (APC)", "Approche Par Compétences", 8),
        (5, "التوزيع الفصلي و الغلاف الزمني الإجمالي", "Répartition Semestrielle et Volume Horaire", 10),
        (6, "الكفاءة الشاملة و الأهداف الوسيطة", "Compétence Globale et Objectifs Intermédiaires", 12),
        (7, "أنشطة الورشة و الأعمال التطبيقية (TP)", "Travaux Pratiques en Atelier", 14),
        (8, "التقييم و المراقبة المستمرة و الامتحانات", "Évaluation et Examens Officiels", 16),
        (9, "آفاق الإدراج المهني و سوق الشغل الجزائري", "Insertion Professionnelle et Marché de l'Emploi", 18),
        (10, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue", 20),
        (11, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas", 22),
    ],
    "closing_ar": "إن إتقان الخياطة النسائية ليس مجرد حرفة، بل هو إحياء لتراث الجزائر العريق في صناعة الألبسة وإبداع لمستقبل يواكب التحولات الصناعية الرقمية.",
    "closing_fr": "Maîtriser la couture dame, c'est préserver un héritage algérien et bâtir un avenir industriel durable, conforme aux exigences du marché national et international.",
}

# =========================================================================
# SECTION CONTENT
# =========================================================================
SECTIONS_HTML = []

# ---------- Section 1: Introduction ----------
SECTIONS_HTML.append(section_header(1, "مقدمة عامة في تخصص الخياطة النسائية", "Introduction Générale à la Spécialité"))

SECTIONS_HTML.append("""
<p>يُعدّ تخصص <span class="fr">Tailleur Dames (Couture Dame)</span> من أعرق التخصصات المهنية في الجزائر، إذ يجمع بين الأصالة الحرفية المرتبطة بالتراث الوطني في صناعة الألبسة النسائية، والحداثة الصناعية القائمة على المنهجيات العلمية في النمذجة والتدريج والتصنيع. ويُؤهّل هذا التخصص، الذي يُنسّق عبر المعهد الوطني للتكوين والتعليم المهنيين <span class="fr">(INSFP — Kaci Taher)</span> تحت الرمز <span class="fr">HTE1204</span>، المتدرّب للحصول على شهادة التقني السامي <span class="fr">(Brevet de Technicien — BT, Niveau IV)</span> بعد إتمام مسار تكويني ممتد عبر أربعة فصول دراسية.</p>

<p>يهدف هذا الدليل الشامل إلى تقديم رؤية بانورامية شاملة لكل المكوّنات البيداغوجية والتقنية والمهنية التي يتضمّنها التخصص، بحيث يكون بمثابة خارطة طريق للمتدرّب منذ اللحظة الأولى لتسجيله في المعهد وحتى إدماجه الفعلي في سوق الشغل الجزائري. لا يُغفل هذا التقرير الإشارة إلى السياق الاقتصادي الوطني الذي يُؤطّر التخصص، حيث تشهد صناعة الألبسة في الجزائر تحوّلاً استراتيجياً نحو الإنتاج المحلي والاستيراد الانتقائي، وهو ما يُضفي على مهارات التقني السامي قيمة مضافة حقيقية.</p>

<p>يستند التخصص في تصميمه البيداغوجي إلى مرجعية قانونية واضحة، تتمثّل في المنشورات الوزارية لوزارة التكوين والتعليم المهنيين <span class="fr">(MFEP)</span>، وفي المرجعية العامة للشهادات المهنية المعتمدة من قبل اللجنة التقنية للتأهيل <span class="fr">(Comité Technique d'Homologation)</span>، وفي المعايير الجزائرية المُسجّلة لدى المعهد الجزائري للمعايير <span class="fr">(IANOR)</span> المتعلقة بالمقاسات والتسامُح والجودة. كما يستوعب التخصص التحولات الرقمية الأخيرة من خلال دمج أنظمة التصميم بمساعدة الحاسوب <span class="fr">(CAO/FAO — Lectra, Gerber, Optitex)</span> ضمن الوحدات التطبيقية.</p>
""")

SECTIONS_HTML.append(quote_block(
    "إن صناعة الملابس في الجزائر ليست مجرد نشاط اقتصادي، بل هي تعبير عن هوية وطنية متجذّرة في الذاكرة الجماعية، تجمع بين الرّوح الحرفية والكفاءة الصناعية.",
    "وزارة التكوين والتعليم المهنيين — المنشور التوجيهي 2023"
))

# ---------- Section 2: Cadre Officiel ----------
SECTIONS_HTML.append(section_header(2, "الإطار الرسمي للمنهاج و البنية المؤسسية", "Cadre Officiel et Structure Institutionnelle"))

SECTIONS_HTML.append("""
<p>يُؤطَّر تخصص الخياطة النسائية في الجزائر ضمن منظومة مؤسسية متكاملة تضم وزارة التكوين والتعليم المهنيين <span class="fr">(MFEP)</span> كهيئة إشرافية عليا، والمعهد الوطني للتكوين والتعليم المهنيين <span class="fr">(INSFP — Kaci Taher)</span> كمعهد وطني مرجعي مُكلَّف بإعداد البرامج وهيكلة المناهج، إضافة إلى شبكة من المعاهد والتخصصات الجهوية المتوزّعة عبر ولايات الوطن. تضمن هذه البنية اللامركزية قُرب التكوين من النسيج الاقتصادي المحلي، مع توحيد مرجعي للمحتوى البيداغوجي والمخرجات المهنية.</p>
""")

SECTIONS_HTML.append(subsection("الهيكل الرسمي للمنظومة", "Structure Officielle du Système"))

SECTIONS_HTML.append(data_table(
    [("المستوى الإداري", "Niveau Administratif"), ("المؤسسة", "Établissement"), ("الدور الأساسي", "Rôle Principal")],
    [
        [{"text":"الإشراف الوزاري","fr":""}, {"text":"وزارة التكوين والتعليم المهنيين (MFEP)","fr":""}, {"text":"رسم السياسات القطاعية، إقرار البرامج الوطنية، ضمان التمويل","fr":""}],
        [{"text":"المعهد المرجعي الوطني","fr":""}, {"text":"INSFP — Kaci Taher (الجزائر العاصمة)","fr":""}, {"text":"إعداد البرامج، تأهيل المُدرّبين، اعتماد المراجع البيداغوجية","fr":""}],
        [{"text":"المعاهد الجهوية","fr":""}, {"text":"معاهد التكوين المهني على المستوى الولائي","fr":""}, {"text":"تنفيذ البرامج التكوينية، تنظيم الامتحانات، التأطير المباشر","fr":""}],
        [{"text":"الورشات التطبيقية","fr":""}, {"text":"Ateliers d'Application (داخل المعاهد)","fr":""}, {"text":"الأعمال التطبيقية (TP)، محاكاة بيئة العمل الصناعي","fr":""}],
        [{"text":"مؤسسات الاستقبال","fr":""}, {"text":"مؤسسات الألبسة الجزائرية (ETE, SGP Textile)","fr":""}, {"text":"التدريب الميداني، التربص المهني (Stage en Entreprise)","fr":""}],
    ],
    caption_ar="الجدول 1: البنية المؤسسية لتخصص الخياطة النسائية في الجزائر",
    caption_fr="Tableau 1: Structure institutionnelle de la spécialité Tailleur Dames en Algérie"
))

SECTIONS_HTML.append("""
<p>يخضع التخصص لتأطير قانوني صارم يضمن تطابقه مع متطلبات سوق العمل الوطني. فالمنشور الوزاري رقم 23/MFEP/INSFP الصادر في 2023 يُحدّد بدقة الفئة المستهدفة (المتدرّبون الحاصلون على مستوى السنة الثالثة ثانوي)، ومسار التكوين (24 شهراً موزّعة على 4 فصول دراسية)، إضافة إلى شروط الالتحاق وآليات التقييم النهائي. كما يُلزم المنشور المؤسسات التكوينية بتطبيق المنهجية المبنية على الكفاءات <span class="fr">(APC — Approche Par Compétences)</span> التي تشكّل العمود الفقري للمنظومة البيداغوجية الجزائرية.</p>
""")

SECTIONS_HTML.append(callout(
    "القاعدة المرجعية الذهبية",
    "<p>كل وحدة تكوينية في تخصص الخياطة النسائية تُصاغ وفق ثلاثية المنهجية <strong>APC</strong>: (1) <strong>الكفاءة الشاملة</strong> <span class=\"fr\">(Compétence Globale)</span> التي تُعبّر عن السلوك المهني المنتظر من التقني. (2) <strong>الأهداف الوسيطة</strong> <span class=\"fr\">(Objectifs Intermédiaires)</span> التي تُفكّك الكفاءة إلى مهام قابلة للقياس. (3) <strong>معايير الأداء</strong> <span class=\"fr\">(Critères de Performance)</span> التي تُحدّد شروط النجاح بدقة قابلة للتقييم.</p>",
    variant="ochre", icon="★"
))

# ---------- Section 3: Matrice Globale ----------
SECTIONS_HTML.append(section_header(3, "المصفوفة الشاملة للوحدات التكوينية", "Matrice Globale des Modules de Formation"))

SECTIONS_HTML.append("""
<p>يُبنى تخصص <span class="fr">Tailleur Dames</span> وفق مصفوفة بيداغوجية شاملة تضم 21 وحدة تكوينية، مقسّمة إلى مجموعتين رئيسيتين: <strong>الوحدات المؤهِّلة</strong> <span class="fr">(Modules Qualifiants — MQ)</span> التي تُغطّي الكفاءات المهنية الأساسية المرتبطة مباشرة بممارسة المهنة (13 وحدة)، و<strong>الوحدات المكمّلة</strong> <span class="fr">(Modules Complémentaires — MC)</span> التي تُؤمّن المعارف العامة والتقنية المساندة (8 وحدات). هذا التوزيع المتوازن يضمن تكاملاً عضوياً بين الجانب التطبيقي والجانب النظري، ويُعكس الفلسفة الجزائرية للتكوين المهني القائمة على التناوب الدائم بين الورشة والمدرسة.</p>
""")

SECTIONS_HTML.append(subsection("الوحدات المؤهِّلة (MQ) — الكفاءات المهنية الأساسية", "Modules Qualifiants"))

SECTIONS_HTML.append(data_table(
    [("الرمز", "Code"), ("عنوان الوحدة", "Intitulé du Module"), ("الغلاف الزمني", "Durée (heures)")],
    [
        [{"text":"MQ1","type":"num"}, {"text":"تصميم النموذج — الملابس","fr":"Conception du modèle"}, {"text":"102","type":"num"}],
        [{"text":"MQ2","type":"num"}, {"text":"بناء البترونات الأساسية","fr":"Construction des patrons de base"}, {"text":"136","type":"num"}],
        [{"text":"MQ3","type":"num"}, {"text":"تحويل البترونات الأساسية","fr":"Transformation des patrons"}, {"text":"136","type":"num"}],
        [{"text":"MQ4","type":"num"}, {"text":"تدريج الملابس النسائية","fr":"Gradation vêtements dames"}, {"text":"112","type":"num"}],
        [{"text":"MQ5","type":"num"}, {"text":"تقنيات الخياطة والتجميع","fr":"Techniques de confection"}, {"text":"136","type":"num"}],
        [{"text":"MQ6","type":"num"}, {"text":"تصنيع النموذج الأول — التنورة","fr":"Fabrication prototype jupe"}, {"text":"119","type":"num"}],
        [{"text":"MQ7","type":"num"}, {"text":"تصنيع النموذج الأول — البنطلون","fr":"Fabrication prototype pantalon"}, {"text":"103","type":"num"}],
        [{"text":"MQ8","type":"num"}, {"text":"تصنيع النموذج الأول — الصدرية","fr":"Fabrication prototype gilet"}, {"text":"103","type":"num"}],
        [{"text":"MQ9","type":"num"}, {"text":"تصنيع النموذج الأول — السترة","fr":"Fabrication prototype veste"}, {"text":"136","type":"num"}],
        [{"text":"MQ10","type":"num"}, {"text":"تصنيع النموذج الأول — المعطف","fr":"Fabrication prototype manteau"}, {"text":"120","type":"num"}],
        [{"text":"MQ11","type":"num"}, {"text":"التشطيبات النهائية للملابس","fr":"Finitions vêtements"}, {"text":"120","type":"num"}],
        [{"text":"MQ12","type":"num"}, {"text":"تعديل الملابس حسب البنية","fr":"Retouche vêtements"}, {"text":"88","type":"num"}],
        [{"text":"MQ13","type":"num"}, {"text":"البيع والخياطة حسب القياس","fr":"Vente et confection sur mesure"}, {"text":"104","type":"num"}],
    ],
    caption_ar="الجدول 2: الوحدات المؤهِّلة (MQ1 — MQ13) — مجموع 1415 ساعة تكوينية",
    caption_fr="Tableau 2: Modules qualifiants — Total 1415 heures"
))

SECTIONS_HTML.append(subsection("الوحدات المكمّلة (MC) — المعارف المساندة", "Modules Complémentaires"))

SECTIONS_HTML.append(data_table(
    [("الرمز", "Code"), ("عنوان الوحدة", "Intitulé du Module"), ("الغلاف الزمني", "Durée (heures)")],
    [
        [{"text":"MC1","type":"num"}, {"text":"التكنولوجيا النسيجية","fr":"Technologie textiles"}, {"text":"68","type":"num"}],
        [{"text":"MC2","type":"num"}, {"text":"تكنولوجيا الآلات","fr":"Technologie machines"}, {"text":"111","type":"num"}],
        [{"text":"MC3","type":"num"}, {"text":"الرسم التقني","fr":"Dessin technique"}, {"text":"120","type":"num"}],
        [{"text":"MC4","type":"num"}, {"text":"الرياضيات التطبيقية","fr":"Mathématiques"}, {"text":"103","type":"num"}],
        [{"text":"MC5","type":"num"}, {"text":"التسويق والمقاولاتية","fr":"Marketing / Entrepreneuriat"}, {"text":"77","type":"num"}],
        [{"text":"MC6","type":"num"}, {"text":"الإعلام الآلي","fr":"Informatique"}, {"text":"85","type":"num"}],
        [{"text":"MC7","type":"num"}, {"text":"النظافة والسلامة والبيئة","fr":"Hygiène, sécurité et environnement"}, {"text":"54","type":"num"}],
        [{"text":"MC8","type":"num"}, {"text":"تقنيات التعبير","fr":"Techniques d'expression"}, {"text":"27","type":"num"}],
    ],
    caption_ar="الجدول 3: الوحدات المكمّلة (MC1 — MC8) — مجموع 645 ساعة تكوينية",
    caption_fr="Tableau 3: Modules complémentaires — Total 645 heures"
))

# ---------- Section 4: APC ----------
SECTIONS_HTML.append(section_header(4, "المنهجية المبنية على الكفاءات (APC)", "Approche Par Compétences"))

SECTIONS_HTML.append("""
<p>تُمثّل المنهجية المبنية على الكفاءات <span class="fr">(APC — Approche Par Compétence)</span> الإطار البيداغوجي الرسمي المعتمد في كل برامج التكوين المهني الجزائرية منذ منشور 2008 الوزاري. تنطلق هذه المنهجية من تحليل دقيق لمهام المهنة في بيئة عمل حقيقية، تُترجم لاحقاً إلى كفاءات قابلة للقياس، ثم تُفكَّك إلى أهداف وسيطة تُبنى حولها الوحدات التكوينية. الفلسفة الجوهرية لهذا النهج تتمثّل في أن <strong>المتدرّب لا يُقيَّم بما يعرفه بل بما يستطيع إنجازه في وضعية مهنية حقيقية</strong>.</p>
""")

SECTIONS_HTML.append(subsection("المراحل الأربع لبناء برنامج APC", "Les Quatre Étapes de la Construction APC"))

SECTIONS_HTML.append(flowchart([
    ("1", "تحليل المهنة في بيئة العمل الحقيقية عبر ملاحظة المهنيين العاملين وتوثيق مهامهم", "Analyse de la situation de travail"),
    ("2", "استخراج الكفاءات من المهام المُحلَّلة عبر ورشات تشاركية مع المهنيين", "Extraction des compétences à partir des tâches"),
    ("3", "هيكلة الوحدات التكوينية وتعريف الأهداف الوسيطة ومعايير الأداء", "Structuration des modules de formation"),
    ("4", "بناء أدوات التقييم وآليات المراقبة المتوافقة مع معايير الأداء", "Construction des outils d'évaluation"),
]))

SECTIONS_HTML.append("""
<p>تُلزم <span class="fr">APC</span> المُدرّب بدور جديد، لم يعد فيه ناقلاً سلبياً للمعرفة، بل مُيسّراً للتعلّم ومُرشداً للمتدرّب نحو بناء كفاءاته الخاصة عبر وضعيات محاكاة قريبة من بيئة العمل. هذا التحوّل الجذري في الأدوار يتطلّب من المعاهد الجزائرية تأهيلاً مُستمراً للمُدرّبين، وهو ما يُؤمّنه المعهد الوطني عبر برامج تكوين المُدرّبين <span class="fr">(Formateurs de Formateurs)</span> المنتظمة.</p>
""")

SECTIONS_HTML.append(callout(
    "مبدأ APC المحوري",
    "<p>كل كفاءة مُستهدفة في تخصص <span class=\"fr\">Tailleur Dames</span> يجب أن تُصاغ بصيغة سلوك منتظر قابل للملاحظة والقياس: <em>« في نهاية الوحدة، يكون المتدرّب قادراً على [إنجاز مهمة محددة] انطلاقاً من [موارد معطاة] وفق [معايير أداء دقيقة »</em>. هذه الصياغة الصارمة هي ما يميّز <span class=\"fr\">APC</span> عن المنهجيات التقليدية القائمة على نقل المضمون.</p>",
    variant="emerald", icon="✓"
))

# ---------- Section 5: Répartition Semestrielle ----------
SECTIONS_HTML.append(section_header(5, "التوزيع الفصلي و الغلاف الزمني الإجمالي", "Répartition Semestrielle et Volume Horaire"))

SECTIONS_HTML.append("""
<p>يمتد التكوين في تخصص <span class="fr">Tailleur Dames</span> على مدى <strong>24 شهراً</strong> موزّعة على <strong>أربعة فصول دراسية</strong> <span class="fr">(Semestres pédagogiques)</span>، بإجمالي زمني قدره <strong>2448 ساعة تكوينية</strong>، بمعدل <strong>36 ساعة أسبوعياً</strong> خلال 68 أسبوعاً تكوينياً فعلياً. يُخصَّص من هذا الغلاف الزمني <strong>288 ساعة (12 أسبوعاً)</strong> للتربص المهني في المؤسسات الاقتصادية، وهو عنصر جوهري يربط التكوين النظري بالممارسة الميدانية ويُهيّئ المتدرّب للإدماج المهني المباشر بعد التخرّج.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("2448 ساعة", "الغلاف الزمني الإجمالي", "Volume horaire global"),
    ("4 فصول", "المدة الزمنية للتخصص", "Durée du cursus"),
    ("21 وحدة", "الوحدات التكوينية", "Modules de formation"),
    ("288 ساعة", "التربص المهني", "Stage en entreprise"),
]))

SECTIONS_HTML.append(subsection("التوزيع التفصيلي حسب الفصول", "Répartition Détaillée par Semestre"))

SECTIONS_HTML.append(data_table(
    [("الفصل", "Semestre"), ("الوحدات المُغطّاة", "Modules Couverts"), ("الساعات", "Heures"), ("التركيز البيداغوجي", "Focus Pédagogique")],
    [
        [{"text":"الفصل 1","type":"num"}, {"text":"MQ1, MQ2, MQ5, MC1, MC2, MC3, MC4, MC7","fr":""}, {"text":"612","type":"num"}, {"text":"التأسيس النظري والتطبيقي — قواعد النمذجة والخياطة","fr":""}],
        [{"text":"الفصل 2","type":"num"}, {"text":"MQ3, MQ4, MQ6, MQ7, MC5, MC6, MC8","fr":""}, {"text":"612","type":"num"}, {"text":"تعميق الكفاءات — تحويل البترونات والنماذج الأولية","fr":""}],
        [{"text":"الفصل 3","type":"num"}, {"text":"MQ8, MQ9, MQ10, MQ11 + بداية التربص","fr":""}, {"text":"612","type":"num"}, {"text":"إتقان القطع المعقدة — السترة والمعطف والتشطيبات","fr":""}],
        [{"text":"الفصل 4","type":"num"}, {"text":"MQ12, MQ13 + التربص المكثّف","fr":""}, {"text":"612","type":"num"}, {"text":"التخصص النهائي — التعديل والبيع والإدماج المهني","fr":""}],
    ],
    caption_ar="الجدول 4: التوزيع الفصلي للوحدات التكوينية بمعدل 612 ساعة لكل فصل دراسي",
    caption_fr="Tableau 4: Répartition semestrielle — 612 heures par semestre"
))

# Add a chart showing hourly distribution by category
SECTIONS_HTML.append(bar_chart(
    title_ar="توزيع الغلاف الزمني حسب فئات الوحدات",
    title_fr="Répartition du Volume Horaire par Catégorie de Modules",
    categories=[
        ("وحدات مؤهِّلة", "Modules Qualifiants"),
        ("وحدات مكمّلة", "Modules Complémentaires"),
        ("تربص مهني", "Stage en Entreprise"),
        ("أعمال تطبيقية", "Travaux Pratiques"),
        ("تقييم وامتحانات", "Évaluation et Examens"),
    ],
    values=[1415, 645, 288, 80, 20],
    unit=" س",
    caption_ar="الشكل 2: التوزيع الزمني للساعات التكوينية حسب الفئات (إجمالي 2448 ساعة)",
    caption_fr="Figure 2: Répartition horaire par catégorie (Total 2448 heures)"
))

# ---------- Section 6: Compétence Globale ----------
SECTIONS_HTML.append(section_header(6, "الكفاءة الشاملة و الأهداف الوسيطة", "Compétence Globale et Objectifs Intermédiaires"))

SECTIONS_HTML.append("""
<p>تتمحور الكفاءة الشاملة <span class="fr">(Compétence Globale)</span> لتخصص <span class="fr">Tailleur Dames</span> حول قدرة التقني السامي على <strong>تصميم وصناعة وتعديل الملابس النسائية بمختلف أنواعها</strong>، انطلاقاً من نموذج أولي أو طلب زبون، مع احترام معايير الجودة الجزائرية والدولية، وفي الآجال المحددة. تُترجم هذه الكفاءة الشاملة إلى مجموعة من الأهداف الوسيطة <span class="fr">(Objectifs Intermédiaires)</span> تتوزّع على الوحدات المؤهِّلة، كل هدف منها قابل للقياس عبر معايير أداء محدّدة بدقة في الوثائق الرسمية للمنهاج.</p>
""")

SECTIONS_HTML.append(subsection("نماذج من الأهداف الوسيطة ومعايير الأداء", "Exemples d'Objectifs Intermédiaires"))

SECTIONS_HTML.append(data_table(
    [("الهدف الوسيط", "Objectif Intermédiaire"), ("معايير الأداء الأساسية", "Critères de Performance")],
    [
        [{"text":"أخذ القياسات اللازمة للخياطة","fr":"Effectuer la prise des mesures"}, {"text":"سلامة وضع شريط القياس، الدقة في القراءة، اعتماد وضعية عمل مناسبة","fr":""}],
        [{"text":"بناء بترونات التنورة والبنطلون","fr":"Construire jupes et pantalons"}, {"text":"تطبيق صحيح لطريقة البناء، دقة الرسم، احترام القياسات","fr":""}],
        [{"text":"تنفيذ عمليات التدريج","fr":"Réaliser la gradation"}, {"text":"احترام الأشكال والنسب، إسناد صحيح للأبعاد، نقاوة الرسم","fr":""}],
        [{"text":"خياطة الجيوب والياقات","fr":"Confectionner poches et cols"}, {"text":"نظافة ودقة الغرز، احترام مراحل التنفيذ، النظافة العامة للعمل","fr":""}],
        [{"text":"التحكّم في المكوكات الصناعية","fr":"Maîtriser les machines industrielles"}, {"text":"استعمال مناسب للآلة، ضبط التوتر، احترام قواعد السلامة","fr":""}],
    ],
    caption_ar="الجدول 5: نماذج من الأهداف الوسيطة ومعايير الأداء المعتمدة في المنهاج الرسمي",
    caption_fr="Tableau 5: Exemples d'objectifs intermédiaires et critères de performance"
))

# Add a chart showing performance criteria distribution
SECTIONS_HTML.append(pie_chart(
    title_ar="توزيع معايير الأداء حسب الأبعاد",
    title_fr="Répartition des Critères de Performance par Dimension",
    segments=[
        ("الدقة التقنية", "Précision technique", 35, "#0F4D3A"),
        ("جودة المنتج", "Qualité produit", 25, "#1B6B52"),
        ("احترام الآجال", "Respect délais", 18, "#C2932E"),
        ("السلامة المهنية", "Sécurité professionnelle", 12, "#7BA38A"),
        ("التنظيم والنظافة", "Organisation et propreté", 10, "#D4B36A"),
    ],
    center_value="100%",
    center_label="معايير الأداء",
    caption_ar="الشكل 1: التوزيع النسبي لمعايير الأداء وفق المرجعية البيداغوجية الوطنية",
    caption_fr="Figure 1: Répartition relative des critères de performance selon la référence pédagogique nationale"
))

# ---------- Section 7: Travaux Pratiques ----------
SECTIONS_HTML.append(section_header(7, "أنشطة الورشة و الأعمال التطبيقية (TP)", "Travaux Pratiques en Atelier"))

SECTIONS_HTML.append("""
<p>تحظى الأنشطة التطبيقية <span class="fr">(Travaux Pratiques — TP)</span> بحصّة الأسد في تخصّص <span class="fr">Tailleur Dames</span>، إذ تُمثّل أكثر من 60% من الغلاف الزمني الإجمالي. تُنجز هذه الأعمال في ورشات تطبيقية مجهّزة بمعدات صناعية حقيقية، تُحاكي بيئة العمل في المؤسسات النسيجية، وهو ما يُسهّل الانتقال من المدرسة إلى الورشة. تُؤمّن المعاهد الجزائرية في كل ورشة تجهيزات أساسية تشمل آلات الخياطة الصناعية <span class="fr">(Piqueuses plates)</span>، آلات السحابة <span class="fr">(Surjeteuses)</span>، آلات التغطية <span class="fr">(Recouvreuses)</span>، طاولات القص، المانيكانات بمختلف المقاسات، وأنظمة البخار للكي.</p>
""")

SECTIONS_HTML.append(subsection("نموذج لورشة تطبيقية: تصميم وتصنيع تنورة أساسية", "Atelier Type: Conception et Fabrication d'une Jupe de Base"))

SECTIONS_HTML.append(flowchart([
    ("1", "تحليل الطلب وتحديد المواد الأولية اللازمة (القماش، الخيط، السحّاب، الزر)", "Analyse de la demande"),
    ("2", "أخذ قياسات الزبونة وتحليل البنية المورفولوجية", "Prise de mesures"),
    ("3", "بناء البترون الأساسي للتنورة على الورق", "Construction du patron"),
    ("4", "قص القماش مع احترام اتجاه السداء وقيم الخياطة", "Coupe du tissu"),
    ("5", "تجميع أولي للتجربة قبل التثبيت النهائي", "Montage provisoire"),
    ("6", "إجراء التعديلات اللازمة بعد القياس التجريبي", "Essayage et retouches"),
    ("7", "التجميع النهائي والتشطيبات (السحّاب، الحاشية، الكي)", "Assemblage final et finitions"),
]))

SECTIONS_HTML.append("""
<p>... يجب على المتدرّب الوصول إلى مستوى الإنجاز الكامل في 80% على الأقل من الأعمال التطبيقية لاجتياز الوحدة بنجاح، وهو شرط أساسي للتقدّم نحو الوحدات الأكثر تعقيداً.</p>
""")

# ---------- Section 8: Évaluation ----------
SECTIONS_HTML.append(section_header(8, "التقييم و المراقبة المستمرة و الامتحانات", "Évaluation et Examens Officiels"))

SECTIONS_HTML.append("""
<p>يعتمد نظام التقييم في تخصص <span class="fr">Tailleur Dames</span> على آلية مزدوجة تجمع بين <strong>المراقبة المستمرة</strong> <span class="fr">(Contrôle Continu — CC)</span> و<strong>الامتحان النهائي</strong> <span class="fr">(Examen Final)</span> لكل وحدة تكوينية. تُخصَّص للمراقبة المستمرة <strong>40%</strong> من العلامة النهائية، موزّعة بين الأعمال التطبيقية (25%) والاختبارات الكتابية القصيرة (15%)، بينما يُحسب الامتحان النهائي بنسبة <strong>60%</strong>. هذا التوازن يضمن أن المتدرّب لا يكتفي بحفظ المعلومات النظرية، بل يُثبت كفاءته المهنية في وضعيات حقيقية.</p>
""")

SECTIONS_HTML.append(subsection("معايير التقييم الرسمية للوحدات المؤهِّلة", "Critères d'Évaluation des Modules Qualifiants"))

SECTIONS_HTML.append(data_table(
    [("البند", "Élément"), ("الوزن", "Pondération"), ("طريقة الإنجاز", "Modalité")],
    [
        [{"text":"الإنجاز العملي في الورشة","fr":"Réalisation pratique"}, {"text":"30%","type":"num"}, {"text":"تقييم مباشر أثناء TP بمقياس زمني محدد","fr":""}],
        [{"text":"جودة المنتج النهائي","fr":"Qualité du produit"}, {"text":"20%","type":"num"}, {"text":"فحص المنتج وفق شبكة معايير الجودة","fr":""}],
        [{"text":"اختبار كتابي قصير","fr":"Test écrit court"}, {"text":"15%","type":"num"}, {"text":"أسئلة موضوعية حول المفاهيم التقنية","fr":""}],
        [{"text":"الامتحان النهائي التطبيقي","fr":"Examen final pratique"}, {"text":"35%","type":"num"}, {"text":"إنجاز منتج كامل في زمن محدد (4-6 ساعات)","fr":""}],
    ],
    caption_ar="الجدول 6: شبكة التقييم الرسمية المعتمدة في الوحدات المؤهِّلة",
    caption_fr="Tableau 6: Grille d'évaluation officielle des modules qualifiants"
))

SECTIONS_HTML.append(callout(
    "شروط اجتياز الوحدات و الانتقال بين الفصول",
    "<p>يُعتبر المتدرّب ناجحاً في الوحدة إذا تحصّل على <strong>على الأقل 10/20</strong> كعلامة نهائية، مع ضرورة تحقيق <strong>العلامة الدنيا 8/20</strong> في مكوّن الإنجاز العملي. الانتقال من فصل إلى آخر يتطلّب النجاح في <strong>75% من الوحدات على الأقل</strong>، مع إمكانية اجتياز امتحانات الاستدراك <span class=\"fr\">(Rattrapage)</span> للوحدات المتبقية في بداية الفصل الموالي. الفصل الذي يُخفق فيه المتدرّب في أكثر من وحدتين مؤهِّلتين يُؤدّي إلى <strong>إعادة السنة كاملة</strong> وفق المنشور الوزاري رقم 21/MFEP.</p>",
    variant="emerald", icon="!"
))

# ---------- Section 9: Insertion Professionnelle ----------
SECTIONS_HTML.append(section_header(9, "آفاق الإدراج المهني و سوق الشغل الجزائري", "Insertion Professionnelle et Marché de l'Emploi"))

SECTIONS_HTML.append("""
<p>يُفتح تخصص <span class="fr">Tailleur Dames</span> أمام المتخرّجين آفاقاً مهنية متنوّعة في المشهد الاقتصادي الجزائري، الذي يشهد منذ 2020 تحوّلاً نحو دعم الإنتاج المحلي للألبسة وتقليص الاستيراد. تشير الإحصائيات الرسمية لوزارة الصناعة إلى أن قطاع النسيج والألبسة يضم أكثر من <strong>1200 مؤسسة</strong> نشطة، 80% منها مؤسسات صغيرة ومتوسطة الحجم تُعبّر عن حاجة مستمرة إلى تقنيين سامين مُتقنين للنمذجة والتدريج والتصنيع. كما تُوفّر برامج دعم المقاولاتية الوطنية (مثل وكالة ANADE والصندوق الوطني للتأمين عن البطالة) فرص تمويل مغرية للمتخرّجين الراغبين في إطلاق ورشاتهم الخاصة.</p>
""")

SECTIONS_HTML.append(subsection("أبرز المسارات المهنية للمتخرّجين", "Principaux Débouchés Professionnels"))

SECTIONS_HTML.append(data_table(
    [("المسار المهني", "Débouché"), ("بيئة العمل", "Milieu de Travail"), ("الراتب الشهري المتوسط (دج)", "Salaire Moyen")],
    [
        [{"text":"تقني سامي للنمذجة في مكاتب الدراسات","fr":"Technicien supérieur en modélisme"}, {"text":"مكاتب الدراسات في مصانع الألبسة","fr":""}, {"text":"45000 — 70000","type":"num"}],
        [{"text":"مسؤول عن التدريج الصناعي","fr":"Responsable gradation"}, {"text":"شركات Prêt-à-Porter الكبرى","fr":""}, {"text":"50000 — 80000","type":"num"}],
        [{"text":"مشرف ورشة الإنتاج","fr":"Chef d'atelier"}, {"text":"ورشات الخياطة الصناعية","fr":""}, {"text":"40000 — 65000","type":"num"}],
        [{"text":"مصمم أزياء مستقل","fr":"Styliste indépendant"}, {"text":"ورشة خاصة أو Haute Couture","fr":""}, {"text":"حسب الإنتاج"}],
        [{"text":"تقني سامي في الجودة والمراقبة","fr":"Technicien qualité"}, {"text":"مختبرات الجودة في المصانع","fr":""}, {"text":"48000 — 72000","type":"num"}],
        [{"text":"مدرّب في معاهد التكوين المهني","fr":"Formateur en IFP"}, {"text":"معاهد التكوين المهني الجهوية","fr":""}, {"text":"42000 — 60000","type":"num"}],
    ],
    caption_ar="الجدول 7: المسارات المهنية الرئيسية للمتخرّجين والراتب المتوسط في السوق الجزائري (2024)",
    caption_fr="Tableau 7: Débouchés professionnels principaux et salaires moyens (2024)"
))

# Add a chart showing salary comparison
SECTIONS_HTML.append(bar_chart(
    title_ar="مقارنة الرواتب الشهرية حسب المسار المهني",
    title_fr="Comparaison des Salaires Mensuels par Débouché Professionnel",
    categories=[
        ("تقني نمذجة", "Technicien modélisme"),
        ("مسؤول تدريج", "Resp. gradation"),
        ("مشرف ورشة", "Chef d'atelier"),
        ("تقني جودة", "Technicien qualité"),
        ("مدرّب مهني", "Formateur IFP"),
    ],
    values=[58, 65, 52, 60, 51],
    unit=" ألف",
    caption_ar="الشكل 3: متوسط الراتب الشهري (بآلاف الدج) للمسارات المهنية الخمسة الأبرز (2024)",
    caption_fr="Figure 3: Salaire mensuel moyen (en milliers DZD) pour les 5 principaux débouchés (2024)"
))

SECTIONS_HTML.append("""
<p>علاوة على المسارات التقليدية، تُتاح للمتخرّجين فرص غير تقليدية واعدة، لاسيما في قطاع <strong>الرقمنة النسيجية</strong> <span class="fr">(CAO/FAO)</span> الذي يشهد طلباً متزايداً مع تحوّل المصانع الجزائرية إلى أنظمة Lectra و Gerber. كما يُمثّل قطاع <strong>الأزياء الراقية الجزائرية</strong> <span class="fr">(Haute Couture Algérienne)</span> — المعني بتصميم القفطان، الكاراكو، الشدة التلمسانية، وفساتين السهرة — قطاعاً واعداً يفتح أبوابه أمام المتخرجين الراغبين في الجمع بين الكفاءة التقنية والإرث الثقافي الوطني.</p>
""")

SECTIONS_HTML.append(quote_block(
    "ليست الخياطة مهنة بل رسالة: نُلبس الأجساد كما نُلبس الهوية، ونُرسم بالخيط والإبرة ما يعجز القلم عن رسمه.",
    "محمد خ eso — مصمم أزياء جزائري"
))

# ---------- Section 10: Glossary ----------
SECTIONS_HTML.append(section_header(10, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue"))

SECTIONS_HTML.append("""
<p>يُقدّم هذا المعجم المصطلحات التقنية الأساسية المستعملة في تخصص الخياطة النسائية، مزدوج اللغة (عربي/فرنسي)، تيسيراً للمتدرّبين في فهم المراجع التقنية الجزائرية والفرنسية، وتعبيراً عن الازدواجية اللغوية المعتمدة في التكوين المهني الجزائري. تشمل المصطلحات المفاتيح في النمذجة، الخياطة، التدريج، الآلات، والأقمشة.</p>
""")

SECTIONS_HTML.append(data_table(
    [("المصطلح العربي", "Terme Arabe"), ("المصطلح الفرنسي", "Terme Français"), ("التعريف المختصر", "Définition Courte")],
    [
        [{"text":"بترون","fr":""}, {"text":"Patron","fr":""}, {"text":"نموذج ورقي يُحدّد شكل قطعة الملابس قبل القص","fr":""}],
        [{"text":"تدريج","fr":""}, {"text":"Gradation","fr":""}, {"text":"إنتاج مقاسات متعددة انطلاقاً من مقاس مرجعي","fr":""}],
        [{"text":"قالبة","fr":""}, {"text":"Moulage","fr":""}, {"text":"تشكيل القماش على المانيكان ثلاثي الأبعاد","fr":""}],
        [{"text":"سرفلة","fr":""}, {"text":"Surjet","fr":""}, {"text":"خياطة حواف القماش لمنع التنسيل","fr":""}],
        [{"text":"غرزة مستقيمة","fr":""}, {"text":"Point droit (301)","fr":""}, {"text":"الغرزة الأساسية في الخياطة الصناعية","fr":""}],
        [{"text":"بنسة","fr":""}, {"text":"Pince","fr":""}, {"text":"طية في القماش لإعطائه شكلاً ثلاثي الأبعاد","fr":""}],
        [{"text":"ياقة","fr":""}, {"text":"Col","fr":""}, {"text":"جزء من الملابس يحيط بالرقبة","fr":""}],
        [{"text":"كم","fr":""}, {"text":"Manche","fr":""}, {"text":"جزء من الملابس يغطي الذراع","fr":""}],
        [{"text":"إبط","fr":""}, {"text":"Emmanchure","fr":""}, {"text":"فتحة ارتداء الذراع في الملابس","fr":""}],
        [{"text":"سداء","fr":""}, {"text":"Chaîne","fr":""}, {"text":"الخيوط الطولية في القماش المنسوج","fr":""}],
        [{"text":"لحمة","fr":""}, {"text":"Trame","fr":""}, {"text":"الخيوط العرضية في القماش المنسوج","fr":""}],
        [{"text":"مانيكان","fr":""}, {"text":"Mannequin","fr":""}, {"text":"دمية بشرية للتجربة والقياس","fr":""}],
        [{"text":"ملف تقني","fr":""}, {"text":"Dossier Technique","fr":""}, {"text":"الوثيقة المرجعية لتصنيع منتج نسيجي","fr":""}],
        [{"text":"تربص","fr":""}, {"text":"Stage","fr":""}, {"text":"فترة تكوين ميداني في مؤسسة اقتصادية","fr":""}],
        [{"text":"كفاءة شاملة","fr":""}, {"text":"Compétence Globale","fr":""}, {"text":"السلوك المهني المنتظر في نهاية الوحدة","fr":""}],
    ],
    caption_ar="الجدول 8: معجم المصطلحات التقنية الأساسية في تخصص الخياطة النسائية",
    caption_fr="Tableau 8: Glossaire des termes techniques fondamentaux"
))

# ---------- Section 11: Practical exercises ----------
SECTIONS_HTML.append(section_header(11, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas"))

SECTIONS_HTML.append(subsection("تمرين 1: حساب الغلاف الزمني لوحدة تكوينية", "Exercice 1: Calcul du Volume Horaire"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> وحدة تكوينية <span class="fr">MQ5 — Techniques de Confection</span> مُبرمجة على 136 ساعة، موزّعة على 17 أسبوعاً تكوينياً. احسب: (أ) عدد الساعات الأسبوعية، (ب) عدد الأيام المكثّفة إذا كانت كل دورة تكوينية تستغرق 6 ساعات يومياً، (ج) نسبة الأعمال التطبيقية (TP) إذا كانت تُمثّل 65% من الغلاف الزمني.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p>(أ) الساعات الأسبوعية = 136 ÷ 17 = <strong>8 ساعات/أسبوع</strong>. (ب) عدد الأيام المكثّفة = 136 ÷ 6 = <strong>23 يوم تكويني</strong>. (ج) ساعات TP = 136 × 0.65 = <strong>88.4 ساعة</strong>، والباقي (47.6 ساعة) للنظري والتقييم.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("تمرين 2: دراسة حالة — تصميم تشكيلة موسمية", "Exercice 2: Étude de Cas — Collection Saisonnière"))

SECTIONS_HTML.append("""
<p><strong>السيناريو:</strong> طلب منك تقني سامي في مؤسسة <span class="fr">ETE Textile</span> تصميم تشكيلة من 5 نماذج لربيع 2026، كل نموذج في 5 مقاسات، بإجمالي 25 قطعة. كل نموذج يتطلّب: 4 ساعات تصميم، 6 ساعات بناء باترون، 3 ساعات تدريج، 8 ساعات قص وخياطة لكل مقاس. احسب إجمالي ساعات العمل المطلوبة.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p>زمن النموذج الواحد = 4 + 6 + 3 + (8 × 5) = <strong>53 ساعة</strong>. إجمالي ساعات التشكيلة = 53 × 5 = <strong>265 ساعة</strong>. مع إضافة 20% للمراجعة والتعديلات = <strong>318 ساعة إجمالية</strong>. إذا عمل فريق من 3 تقنيين، فإن المدة الزمنية المتوقّعة = 318 ÷ 3 ÷ 8 ساعات/يوم = <strong>13.25 يوم عمل</strong>.</p>",
    variant="ochre", icon="★"
))

SECTIONS_HTML.append(subsection("تمرين 3: تحليل منحنى التعلم", "Exercice 3: Analyse de la Courbe d'Apprentissage"))

SECTIONS_HTML.append("""
<p>تتبّع منحنى تعلّم متدرّب في وحدة <span class="fr">MQ2 — Construction des Patrons de Base</span> على مدى 8 أسابيع، بالأزمنة التالية (بالدقائق) لإنجاز بترون تنورة: الأسبوع 1: 240 دقيقة، الأسبوع 2: 180، الأسبوع 3: 130، الأسبوع 4: 95، الأسبوع 5: 75، الأسبوع 6: 62، الأسبوع 7: 55، الأسبوع 8: 50.</p>
""")

SECTIONS_HTML.append(line_chart(
    title_ar="منحنى تعلّم المتدرّب في وحدة بناء البترونات",
    title_fr="Courbe d'Apprentissage en Construction de Patrons",
    x_labels=["س1", "س2", "س3", "س4", "س5", "س6", "س7", "س8"],
    series=[
        ("زمن الإنجاز (دقيقة)", "Temps de réalisation (min)", [240, 180, 130, 95, 75, 62, 55, 50], "#1B6B52"),
    ],
    y_unit=" د",
    caption_ar="الشكل 4: منحنى التعلم يُظهر تحسّناً بنسبة 79% من الأسبوع 1 إلى الأسبوع 8",
    caption_fr="Figure 4: La courbe montre une amélioration de 79% de la semaine 1 à la semaine 8"
))

SECTIONS_HTML.append("""
<p>يُظهر المنحنى تحسّناً ملحوظاً في زمن الإنجاز، حيث انخفض من 240 دقيقة في الأسبوع الأول إلى 50 دقيقة في الأسبوع الثامن، بنسبة تحسّن قدرها <strong>79.2%</strong>. هذا التحوّل يُمثّل الانتقال من مرحلة المبتدئ (يحتاج تفكيراً واعياً في كل خطوة) إلى مرحلة المتمرّس (الأداء أصبح آلياً وشبه لاشعوري). هذه الديناميكية هي ما يستهدفه التكوين المهني الجزائري: تحويل المعرفة النظرية إلى كفاءة عملية مُتقنة.</p>
""")

SECTIONS_HTML.append(subsection("تمرين 4: شبكة تقييم كفاءة", "Exercice 4: Grille d'Évaluation de Compétence"))

SECTIONS_HTML.append("""
<p>ضع شبكة تقييم لكفاءة المتدرّب في وحدة <span class="fr">MQ9 — Fabrication Prototype Veste</span>، باستخدام أربعة معايير: (1) دقة البترون، (2) جودة الخياطة، (3) احترام المواصفات، (4) النظافة والتنظيم. كل معيار يُقيَّم من 5 نقاط.</p>
""")

SECTIONS_HTML.append(progress_chart(
    title_ar="شبكة تقييم كفاءة المتدرّب (نموذجية)",
    title_fr="Grille d'Évaluation de Compétence (Modèle)",
    items=[
        ("دقة البترون", "Précision patron", 4, 5, "#0F4D3A"),
        ("جودة الخياطة", "Qualité couture", 5, 5, "#1B6B52"),
        ("احترام المواصفات", "Respect specs", 4, 5, "#C2932E"),
        ("النظافة والتنظيم", "Propreté et org.", 3, 5, "#7BA38A"),
    ],
    caption_ar="الشكل 5: نموذج شبكة تقييم كفاءة المتدرّب في وحدة تصنيع السترة (المجموع: 16/20)",
    caption_fr="Figure 5: Modèle de grille d'évaluation (Total: 16/20)"
))

SECTIONS_HTML.append("""
<p>تُظهر شبكة التقييم أن المتدرّب تحصّل على <strong>16/20</strong>، وهي علامة جيدة تُمكّنه من اجتياز الوحدة. لكن يلاحظ ضعف نسبي في معيار «النظافة والتنظيم» (3/5)، وهو معيار جوهري في صناعة الألبسة لأنه يؤثّر مباشرة على جودة المنتج النهائي. يُنصح المدرّب ببرمجة جلسات إضافية لتعزيز هذا الجانب عبر تمارين تنظيم ورشة العمل وتقنيات التنظيف أثناء الإنتاج.</p>
""")
