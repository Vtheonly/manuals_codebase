"""
Manual 8: حماية المستهلك — Protection du Consommateur
Module 07 in the reference structure.
"""
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart
)

MANUAL_8 = {
    "module_num": "07",
    "module_num_label": "الوحدة التكوينية",
    "title_ar": "حماية المستهلك في قطاع النسيج",
    "title_fr": "Protection du Consommateur dans le Secteur Textile",
    "code": "HTE1204 / PC",
    "toc_items": [
        (1, "مقدمة: حماية المستهلك في قطاع النسيج", "Introduction", 3),
        (2, "الإطار القانوني الجزائري (قانون 09-03)", "Cadre Juridique", 4),
        (3, "وسم المنتجات النسيجية و الإلصاق", "Étiquetage", 6),
        (4, "المخاطر الكيميائية و الفيزيائية", "Risques Chimiques", 8),
        (5, "نسبة المطابقة في الجزائر", "Taux de Conformité", 10),
        (6, "حماية المستهلك كألبسة أطفال", "Sécurité Enfants", 12),
        (7, "دور المصمم الجزائري", "Rôle du Concepteur", 14),
        (8, "الخلاصة و المراجع", "Conclusion et Références", 15),
        (9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue", 17),
        (10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas", 19),
    ],
    "closing_ar": "حماية المستهلك في قطاع النسيج ليست قيداً قانونياً، بل التزام أخلاقي يقع على عاتق كل عامل في سلسلة الإنتاج من المصمم إلى البائع.",
    "closing_fr": "La protection du consommateur dans le secteur textile n'est pas une contrainte légale, mais un engagement éthique reposant sur chaque acteur de la chaîne de production, du concepteur au vendeur.",
}

SECTIONS_HTML = []

# Section 1
SECTIONS_HTML.append(section_header(1, "مقدمة: حماية المستهلك في قطاع النسيج", "Introduction"))

SECTIONS_HTML.append("""
<p>تُعرَّف <strong>حماية المستهلك</strong> <span class="fr">(Protection du Consommateur)</span> في التشريعات التجارية الجزائرية بأنها صيانة سلامة المستهلك وحقوقه الاقتصادية والصحية. تهدف هذه الوحدة البيداغوجية إلى إكساب متربص النمذجة وتصميم الملابس وعياً قانونياً وتقنياً حول المعايير والقيود المفروضة على جودة المنتجات النسيجية المعروضة للاستهلاك المحلي.</p>

<p>حماية المستهلك في قطاع النسيج ليست قيداً قانونياً مجرداً، بل هي التزام مهني وأخلاقي يقع على عاتق كل عامل في سلسلة الإنتاج، من المصمم إلى البائع. على عكس الأطعمة والأدوية التي لا تحمل تاريخ انتهاء الصلاحية، فإن الملابس قد تحمل مخاطر فيزيائية (اختناق، حساسية) تهدد صحة المستهلك، خاصة الأطفال. لذلك تفرض التشريعات الجزائرية معايير صارمة على المنتجات النسيجية قبل طرحها في السوق.</p>

<p>في السياق الجزائري، تتزايد أهمية حماية المستهلك مع فتح السوق أمام المنتجات المستوردة بأثمان منخفضة، بعضها لا يخضع لأي مراقبة جودة. هذا الوضع يفرض على التقني السامي الجزائري معرفة دقيقة بالمعايير القانونية والفنية، ليس فقط لتجنب المخاطر القانونية، بل أيضاً لإنتاج منتجات وطنية قادرة على المنافسة بالجودة لا بالسعر فقط.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("09-03", "القانون الجزائري لحماية المستهلك", "Loi algérienne de protection"),
    ("80%+", "نسبة المطابقة المستهدفة في 2025", "Taux de conformité visé 2025"),
    ("7", "مخاطر رئيسية في الألبسة", "Risques principaux"),
    ("IANOR", "الجهة المعيارية الجزائرية", "Organisme normatif algérien"),
]))

# Section 2
SECTIONS_HTML.append(section_header(2, "الإطار القانوني الجزائري (قانون 09-03)", "Cadre Juridique"))

SECTIONS_HTML.append("""
<p>يستند الإطار القانوني لحماية المستهلك في الجزائر إلى <strong>القانون رقم 09-03</strong> المؤرّخ في 25 فبراير 2009، المتعلق بحماية المستهلك وقمع الغش. يُحدّد هذا القانون حقوق وواجبات كل من المستهلك والمُنتِج والمُوزّع، ويفرض عقوبات صارمة على المخالفات. كما يستكمل هذا القانون بمراسيم تطبيقية ومناشير وزارية تُحدّد التفاصيل التقنية لكل قطاع.</p>
""")

SECTIONS_HTML.append(subsection("أبرز بنود القانون 09-03", "Principaux Articles de la Loi 09-03"))

SECTIONS_HTML.append(data_table(
    [("البند", "Article"), ("المضمون", "Contenu"), ("التطبيق على قطاع النسيج", "Application au Textile")],
    [
        [{"text":"المادة 3","fr":""}, {"text":"حق المستهلك في المعلومات الصحيحة","fr":""}, {"text":"إلصاق بيانات صحيحة على المنتج","fr":""}],
        [{"text":"المادة 7","fr":""}, {"text":"منع الغش في طبيعة المنتج","fr":""}, {"text":"عدم الإدعاء بأن قماشاً صناعياً قطني","fr":""}],
        [{"text":"المادة 12","fr":""}, {"text":"ضمان السلامة الصحية","fr":""}, {"text":"منع استخدام أصباغ مسرطنة","fr":""}],
        [{"text":"المادة 18","fr":""}, {"text":"إلزامية ذكر البلد الأصلي","fr":""}, {"text":"وسم «صنع في الجزائر» أو بلد المنشأ","fr":""}],
        [{"text":"المادة 25","fr":""}, {"text":"عقوبات جزائية ومالية","fr":""}, {"text":"غرامات من 50,000 إلى 500,000 دج","fr":""}],
        [{"text":"المادة 30","fr":""}, {"text":"سحب المنتجات المعيبة","fr":""}, {"text":"استدعاء الألبسة المعيبة من السوق","fr":""}],
    ],
    caption_ar="الجدول 1: أبرز بنود القانون 09-03 وتطبيقها على قطاع النسيج",
    caption_fr="Tableau 1: Principaux articles de la Loi 09-03 et application au textile"
))

SECTIONS_HTML.append(callout(
    "الجهات الرقابية الجزائرية",
    "<p>تشرف على تطبيق القانون 09-03 ثلاث جهات رئيسية: (1) <strong>المديرية العامة لحماية المستهلك وقمع الغش</strong> التابعة لوزارة التجارة، (2) <strong>الجمارك الجزائرية</strong> لمراقبة المنتجات المستوردة، (3) <strong>المعهد الجزائري للمعايير (IANOR)</strong> لإصدار المعايير الفنية. تقوم هذه الجهات بزيارات تفتيشية مفاجئة للمؤسسات النسيجية، ولها صلاحية مصادرة المنتجات المخالفة وفرض غرامات.</p>",
    variant="emerald", icon="!"
))

# Section 3
SECTIONS_HTML.append(section_header(3, "وسم المنتجات النسيجية و الإلصاق", "Étiquetage"))

SECTIONS_HTML.append("""
<p>يُعدّ <strong>الإلصاق</strong> <span class="fr">(Étiquetage)</span> الوسيلة الرئيسية لنقل المعلومات من المنتج إلى المستهلك. يفرض القانون الجزائري مجموعة من البيانات الإلزامية التي يجب أن تظهر على كل قطعة ملابس معروضة للبيع، إما على بطاقة ملصقة أو مطبوعة مباشرة على القماش. هذه البيانات تُمكّن المستهلك من اتخاذ قرار شراء مدروس، وتُسهّل تتبّع المنتج في حالة ظهور عيوب.</p>
""")

SECTIONS_HTML.append(data_table(
    [("البيان", "Information"), ("الإلزامية", "Obligatoire"), ("التفاصيل", "Détails")],
    [
        [{"text":"تركيب القماش","fr":"Composition"}, {"text":"إلزامي","fr":""}, {"text":"نسبة كل ليف (مثال: 65% بوليستر، 35% قطن)","fr":""}],
        [{"text":"تعليمات العناية","fr":"Entretien"}, {"text":"إلزامي","fr":""}, {"text":"رموز الغسل، الكي، التنظيف الجاف","fr":""}],
        [{"text":"المقاس","fr":"Taille"}, {"text":"إلزامي","fr":""}, {"text":"وفق الجدول الجزائري (36-46 نساء، 46-56 رجال)","fr":""}],
        [{"text":"البلد الأصلي","fr":"Origine"}, {"text":"إلزامي","fr":""}, {"text":"«صنع في الجزائر» أو بلد المنشأ","fr":""}],
        [{"text":"اسم المنتج","fr":"Désignation"}, {"text":"إلزامي","fr":""}, {"text":"«قميص رجالي»، «تنورة نسوية»","fr":""}],
        [{"text":"الرمز التجاري","fr":"Réf. Article"}, {"text":"اختياري","fr":""}, {"text":"للتتبع الداخلي","fr":""}],
        [{"text":"شهادات المطابقة","fr":"Certificats"}, {"text":"اختياري","fr":""}, {"text":"IANOR، Oeko-Tex، ISO","fr":""}],
    ],
    caption_ar="الجدول 2: البيانات الإلزامية والاختيارية على ملصقات الألبسة",
    caption_fr="Tableau 2: Informations obligatoires et facultatives sur les étiquettes"
))

# Section 4
SECTIONS_HTML.append(section_header(4, "المخاطر الكيميائية و الفيزيائية", "Risques Chimiques et Physiques"))

SECTIONS_HTML.append("""
<p>تتعلق المخاطر الكيميائية بالمواد الكيميائية المستعملة في صناعة النسيج، من أصباغ إلى مثبتات ومواد تشطيب. بعض هذه المواد قد يبقى في القماش النهائي ويتسبب في حساسية جلدية أو أمراض أطول أمداً. المخاطر الفيزيائية تشمل الأزرار الصغيرة التي قد تبتلع، الخيوط الطويلة التي قد تسبب اختناق، والسحّابات المعيبة.</p>
""")

SECTIONS_HTML.append(subsection("أبرز المخاطر الكيميائية في صناعة النسيج", "Principaux Risques Chimiques"))

SECTIONS_HTML.append(data_table(
    [("المادة", "Substance"), ("المخاطر", "Risque"), ("الحد المسموح", "Limite Autorisée")],
    [
        [{"text":"الفورمالدهيد","fr":"Formaldéhyde"}, {"text":"حساسية، مسرطن محتمل","fr":""}, {"text":"75 mg/kg (جلد الأطفال)","type":"num"}],
        [{"text":"الأمينات العطرية","fr":"Amines aromatiques"}, {"text":"مسرطنة (من أصباغ azo)","fr":""}, {"text":"30 mg/kg","type":"num"}],
        [{"text":"الرصاص","fr":"Plomb"}, {"text":"تسمم عصبي، خاص للأطفال","fr":""}, {"text":"90 mg/kg","type":"num"}],
        [{"text":"الكادميوم","fr":"Cadmium"}, {"text":"تسمم كبدي","fr":""}, {"text":"50 mg/kg","type":"num"}],
        [{"text":"المبيدات","fr":"Pesticides"}, {"text":"تبقّى من زراعة القطن","fr":""}, {"text":"0.05 mg/kg","type":"num"}],
        [{"text":"كلوريدات","fr":"Chlorures"}, {"text":"تهيج الجلد","fr":""}, {"text":"حسب نوع المادة","fr":""}],
    ],
    caption_ar="الجدول 3: المواد الكيميائية الخطيرة في صناعة النسيج وحدودها المسموحة",
    caption_fr="Tableau 3: Substances chimiques dangereuses et limites autorisées"
))

SECTIONS_HTML.append(bar_chart(
    title_ar="توزيع المخالفات في الألبسة المستوردة",
    title_fr="Répartition des Infractions dans les Vêtements Importés",
    categories=[
        ("وسم خاطئ", "Étiquetage faux"),
        ("مواد كيميائية", "Chimique"),
        ("أمان الأطفال", "Sécurité enfant"),
        ("جودة القماش", "Qualité tissu"),
        ("أخرى", "Autres"),
    ],
    values=[42, 28, 15, 10, 5],
    unit="%",
    caption_ar="الشكل 2: توزيع أنواع المخالفات في الألبسة المستوردة المعيبة (2024)",
    caption_fr="Figure 2: Répartition des infractions (2024)"
))

SECTIONS_HTML.append(callout(
    "قاعدة ذهبية: شهادة Oeko-Tex",
    "<p>شهادة <strong>Oeko-Tex Standard 100</strong> هي المعيار الدولي الأكثر اعتماداً لسلامة الأقمشة من المواد الكيميائية الخطيرة. الأقمشة الحاصلة على هذه الشهادة مضمونة خالية من الفورمالدهيد والأمينات العطرية والمواد المسرطنة. يُوصى للمؤسسات الجزائرية التي تُصدّر إلى أوروبا الحصول على هذه الشهادة، حيث تُعدّ شرطاً أساسياً للدخول إلى السوق الأوروبية.</p>",
    variant="ochre", icon="★"
))

# Section 5
SECTIONS_HTML.append(section_header(5, "نسبة المطابقة في الجزائر", "Taux de Conformité"))

SECTIONS_HTML.append("""
<p>تُجرى فحوص دورية على المنتجات النسيجية المعروضة في السوق الجزائري من قبل المديرية العامة لحماية المستهلك. تشير الإحصائيات الأخيرة إلى تحسّن نسبي في نسبة المطابقة، لكنها لا تزال دون المستهدفات الوطنية. تُعزى النسبة المنخفضة إلى استمرار استيراد منتجات بدون مراقبة، وإلى ضعف الوعي لدى بعض المنتجين المحليين بالمعايير المطلوبة.</p>
""")

SECTIONS_HTML.append(data_table(
    [("السنة", "Année"), ("نسبة المطابقة (%)", "Conformité (%)"), ("المنتجات المخالفة", "Produits Non Conformes")],
    [
        [{"text":"2020","type":"num"}, {"text":"58%","type":"num"}, {"text":"42% (أغلبها مستوردة)","fr":""}],
        [{"text":"2021","type":"num"}, {"text":"62%","type":"num"}, {"text":"38%","fr":""}],
        [{"text":"2022","type":"num"}, {"text":"67%","type":"num"}, {"text":"33%","fr":""}],
        [{"text":"2023","type":"num"}, {"text":"72%","type":"num"}, {"text":"28%","fr":""}],
        [{"text":"2024 (تقديري)","type":"num"}, {"text":"78%","type":"num"}, {"text":"22%","fr":""}],
        [{"text":"المستهدف 2025","type":"num"}, {"text":"85%+","type":"num"}, {"text":"15%-","fr":""}],
    ],
    caption_ar="الجدول 4: تطوّر نسبة المطابقة في السوق الجزائري 2020-2025",
    caption_fr="Tableau 4: Évolution du taux de conformité sur le marché algérien 2020-2025"
))

SECTIONS_HTML.append(line_chart(
    title_ar="تطوّر نسبة المطابقة في السوق الجزائري",
    title_fr="Évolution du Taux de Conformité en Algérie",
    x_labels=["2020", "2021", "2022", "2023", "2024", "2025 (هدف)"],
    series=[
        ("نسبة المطابقة (%)", "Taux conformité (%)", [58, 62, 67, 72, 78, 85], "#1B6B52"),
    ],
    y_unit="%",
    caption_ar="الشكل 1: تطوّر نسبة المطابقة للمنتجات النسيجية في السوق الجزائري (2020-2025)",
    caption_fr="Figure 1: Évolution du taux de conformité (2020-2025)"
))

# Section 6
SECTIONS_HTML.append(section_header(6, "حماية المستهلك كألبسة أطفال", "Sécurité Enfants"))

SECTIONS_HTML.append("""
<p>تُعدّ ألبسة الأطفال الفئة الأكثر حساسية في حماية المستهلك، إذ تفرض التشريعات الجزائرية والدولية معايير صارمة جداً عليها. الطفل أكثر عرضة للمخاطر الكيميائية (جلد رقيق، جهاز مناعي غير مكتمل) والفيزيائية (قد يبتلع أزراراً، يختنق بخيوط). لذلك، تُطبّق على ألبسة الأطفال معايير خاصة تتجاوز تلك المفروضة على ألبسة الكبار.</p>
""")

SECTIONS_HTML.append(subsection("المعايير الخاصة بألبسة الأطفال", "Normes Spécifiques aux Vêtements Enfants"))

SECTIONS_HTML.append(data_table(
    [("البند", "Élément"), ("المعيار للأطفال", "Norme Enfants"), ("المعيار للكبار", "Norme Adultes")],
    [
        [{"text":"الفورمالدهيد","fr":""}, {"text":"≤ 20 mg/kg","type":"num"}, {"text":"≤ 75 mg/kg","type":"num"}],
        [{"text":"الأزرار و الإكسسوارات","fr":""}, {"text":"قوة شد ≥ 90 نيوتن","type":"num"}, {"text":"قوة شد ≥ 50 نيوتن","type":"num"}],
        [{"text":"الخيوط الطويلة","fr":""}, {"text":"ممنوعة في ألبسة < 7 سنوات","fr":""}, {"text":"مسموحة","fr":""}],
        [{"text":"السحّابات","fr":""}, {"text":"ممنوعة في رقبة الأطفال","fr":""}, {"text":"مسموحة","fr":""}],
        [{"text":"الأصباغ","fr":""}, {"text":"خالية من azo المسرطنة","fr":""}, {"text":"خالية من azo المسرطنة","fr":""}],
        [{"text":"الوظيفة المضادة للحريق","fr":""}, {"text":"إلزامية للنوم < 7 سنوات","fr":""}, {"text":"غير إلزامية","fr":""}],
    ],
    caption_ar="الجدول 5: مقارنة المعايير بين ألبسة الأطفال وألبسة الكبار",
    caption_fr="Tableau 5: Comparaison des normes entre vêtements enfants et adultes"
))

# Section 7
SECTIONS_HTML.append(section_header(7, "دور المصمم الجزائري", "Rôle du Concepteur"))

SECTIONS_HTML.append("""
<p>يقع على عاتق <strong>المصمم الجزائري</strong> دور محوري في حماية المستهلك، إذ يبدأ الالتزام بمعايير السلامة من مرحلة التصميم. المصمم الذي يختار أقمشة عالية الجودة، يحدد إكسسوارات آمنة، يراعى متطلبات الفئة المستهدفة، يُنتج منتجاً آمناً منذ البداية. على عكس المصمم الذي يركّز فقط على الجانب الجمالي دون اعتبار لمعايير السلامة، ويترك المشاكل لتُكتشف لاحقاً في مرحلة الإنتاج أو ما هو أسوأ، في يد المستهلك.</p>
""")

SECTIONS_HTML.append(subsection("قائمة تحقّق المصمم المسؤول", "Checklist du Concepteur Responsable"))

SECTIONS_HTML.append(flowchart([
    ("1", "اختيار أقمشة من موردين معتمدين، مع طلب شهادات الجودة (Oeko-Tex، ISO)", "Sélection des tissus"),
    ("2", "اختيار إكسسوارات آمنة: أزرار مقاومة للشد، خيوط مختبرة، سحّابات معتمدة", "Choix des accessoires"),
    ("3", "تصميم يراعى الفئة المستهدفة: لا خيوط طويلة للأطفال، لا سحّابات على رقبة الأطفال", "Design adapté"),
    ("4", "إعداد ملف تقني كامل يحدد تركيب القماش، تعليمات العناية، تحذيرات السلامة", "Dossier technique"),
    ("5", "إجراء فحوص أولية على عيّنات من المنتج النهائي قبل الإنتاج الكمي", "Tests préalables"),
    ("6", "وضع ملصق واضح وشامل بكل البيانات الإلزامية على المنتج", "Étiquetage complet"),
    ("7", "تتبّع المنتج بعد البيع، وجمع ملاحظات المستهلكين للتحسين المستمر", "Suivi post-vente"),
]))

SECTIONS_HTML.append(callout(
    "المسؤولية القانونية للمصمم",
    "<p>وفق القانون 09-03، يتحمّل المصمم مسؤولية قانونية كاملة عن أي عيب في المنتج يُسبب ضرراً للمستهلك. هذا يعني أن المصمم الذي يختار قماشاً يحتوي على فورمالدهيد فوق الحد المسموح يمكن ملاحقته قضائياً ومالياً، حتى لو لم يكن على علم بالخطر. لذلك، يجب على المصمم طلب شهادات الجودة من الموردين قبل اعتماد أي قماش في الإنتاج.</p>",
    variant="emerald", icon="!"
))

# Section 8
SECTIONS_HTML.append(section_header(8, "الخلاصة و المراجع", "Conclusion et Références"))

SECTIONS_HTML.append("""
<p>حماية المستهلك في قطاع النسيج ليست قيداً قانونياً يُثقل كاهل المنتج، بل هي التزام أخلاقي ومهني يحمي المؤسسة من المخاطر القانونية ويُعزّز سمعتها في السوق. التقني السامي الذي يتقن معايير حماية المستهلك يصبح عنصراً لا غنى عنه في المؤسسات النسيجية الجادة، ويفتح أمامه آفاقاً مهنية في مختبرات الجودة وإدارات المراقبة.</p>

<p>تشهد السوق الجزائرية تحسّناً مطّرداً في نسبة المطابقة، لكنها لا تزال دون المستويات الدولية. المستقبل ينتمي للمؤسسات الجزائرية التي تتبنى معايير الجودة وقواعد حماية المستهلك طوعاً، قبل أن تُفرض عليها. هذه المؤسسات ستنافس بثقة في الأسواق المحلية والإقليمية، وستفتح أبواب التصدير إلى الأسواق الأوروبية والافريقية.</p>
""")

SECTIONS_HTML.append(subsection("آفاق التطوير المستقبلي", "Perspectives d'Évolution Future"))
SECTIONS_HTML.append("""
<ul>
<li><strong>الرقمنة في مراقبة الجودة:</strong> استخدام الحاسوب لربط كل منتج بشهادة جودة رقمية قابلة للتتبع عبر QR Code، يُمكّن المستهلك من التحقق من أصالة وجودة المنتج بهاتفه.</li>
<li><strong>التوعية الاستهلاكية:</strong> إطلاق حملات وطنية لتوعية المستهلك الجزائري بحقوقه وكيفية التعرّف على المنتجات المطابقة، عبر الإعلام والمدارس والجمعيات.</li>
<li><strong>الاعتماد المتبادل:</strong> عقد اتفاقيات مع المنظمات الدولية (ISO، Oeko-Tex، CE) للاعتراف المتبادل بالشهادات، مما يُسهّل تصدير المنتجات الجزائرية.</li>
<li><strong>مختبرات الجودة الجهوية:</strong> توسيع شبكة المختبرات المعتمدة في ولايات الجزائر، لتقريب الفحوص من المنتجين وتقليل زمن الانتظار.</li>
</ul>
""")

SECTIONS_HTML.append(quote_block(
    "المستهلك الواعي هو الحارس الأول للجودة. كلما ارتفع وعي المستهلك، ارتفعت جودة المنتجات، لأن المؤسسات تجد نفسها مضطرة للاستجابة لطلبات السوق.",
    "IANOR — المعهد الجزائري للمعايير"
))

SECTIONS_HTML.append(subsection("المراجع", "Références Bibliographiques"))
SECTIONS_HTML.append("""
<ol>
<li>الجمهورية الجزائرية الديمقراطية الشعبية، القانون رقم 09-03 المؤرّخ في 25 فبراير 2009 المتعلق بحماية المستهلك وقمع الغش، الجريدة الرسمية رقم 15، 2009.</li>
<li>المعهد الجزائري للمعايير (IANOR)، المعايير الجزائرية للألبسة: السلامة والوسم NA 2345، الجزائر، 2022.</li>
<li>Oeko-Tex Association, Standard 100 — Testing for Harmful Substances, Zurich, Switzerland, 2023.</li>
<li>ISO 3071: Textiles — Determination of pH of aqueous extract, International Organization for Standardization, Geneva, 2020.</li>
<li>وزارة التجارة الجزائرية، تقرير حماية المستهلك 2023، المديرية العامة لحماية المستهلك وقمع الغش، الجزائر، 2024.</li>
<li>European Commission, Regulation (EU) 1007/2011 on Textile Labelling, Brussels, Belgium, 2011.</li>
</ol>
""")

# ---------- Section 9: Glossary ----------
SECTIONS_HTML.append(section_header(9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue"))

SECTIONS_HTML.append("""
<p>يُقدّم هذا المعجم المصطلحات التقنية والقانونية الأساسية المستعملة في وحدة حماية المستهلك، مزدوج اللغة (عربي/فرنسي). تشمل المصطلحات المفاتيح في التشريع، الوسم، والمخاطر الكيميائية.</p>
""")

SECTIONS_HTML.append(data_table(
    [("المصطلح العربي", "Terme Arabe"), ("المصطلح الفرنسي", "Terme Français"), ("التعريف المختصر", "Définition Courte")],
    [
        [{"text":"حماية المستهلك","fr":""}, {"text":"Protection du Consommateur","fr":""}, {"text":"صيانة حقوق المستهلك","fr":""}],
        [{"text":"وسم","fr":""}, {"text":"Étiquetage","fr":""}, {"text":"بطاقة بيانات المنتج","fr":""}],
        [{"text":"مطابقة","fr":""}, {"text":"Conformité","fr":""}, {"text":"احترام المعايير المطلوبة","fr":""}],
        [{"text":"معيار","fr":""}, {"text":"Norme","fr":""}, {"text":"مواصفة فنية مرجعية","fr":""}],
        [{"text":"IANOR","fr":""}, {"text":"IANOR","fr":""}, {"text":"المعهد الجزائري للمعايير","fr":""}],
        [{"text":"ISO","fr":""}, {"text":"ISO","fr":""}, {"text":"المنظمة الدولية للمعايير","fr":""}],
        [{"text":"Oeko-Tex","fr":""}, {"text":"Oeko-Tex","fr":""}, {"text":"شهادة سلامة الأقمشة","fr":""}],
        [{"text":"فورمالدهيد","fr":""}, {"text":"Formaldéhyde","fr":""}, {"text":"مادة كيميائية خطيرة","fr":""}],
        [{"text":"تسامح","fr":""}, {"text":"Tolérance","fr":""}, {"text":"الهامش المسموح في القياس","fr":""}],
        [{"text":"سحب المنتج","fr":""}, {"text":"Rappel de Produit","fr":""}, {"text":"استدعاء منتج معيب","fr":""}],
        [{"text":"غرامة","fr":""}, {"text":"Amende","fr":""}, {"text":"عقوبة مالية على المخالفة","fr":""}],
        [{"text":"دفتر شروط","fr":""}, {"text":"Cahier des Charges","fr":""}, {"text":"وثيقة مواصفات المنتج","fr":""}],
    ],
    caption_ar="الجدول 7: معجم مصطلحات حماية المستهلك",
    caption_fr="Tableau 7: Glossaire des termes de protection du consommateur"
))

# ---------- Section 10: Exercises ----------
SECTIONS_HTML.append(section_header(10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas"))

SECTIONS_HTML.append(subsection("تمرين 1: تحليل ملصق منتج", "Exercice 1: Analyse d'Étiquette"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> قم بتحليل الملصق التالي لقميص رجالي: «صنع في الصين، 65% بوليستر، 35% قطن، المقاس L، الغسل at 30°C». اذكر البيانات الإلزامية الموجودة والبيانات الناقصة وفق القانون الجزائري.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p><strong>البيانات الموجودة:</strong> البلد الأصلي ✓، تركيب القماش ✓، المقاس ✓، تعليمات العناية ✓.</p><p><strong>البيانات الناقصة:</strong> اسم المنتج (قميص رجالي)، الرمز التجاري، شهادات المطابقة (إن وجدت).</p><p>المنتج <strong>مطابق تقريباً</strong> ولكن ينقصه بيان اسم المنتج بوضوح.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("تمرين 2: حساب غرامة مخالفة", "Exercice 2: Calcul d'Amende"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> مؤسسة نسيجية جزائرية تبيع قمصان بوسم «100% قطن» بينما التركيب الحقيقي 65% بوليستر + 35% قطن. باعوا 500 قطعة. احسب الغرامة المحتملة وفق القانون 09-03.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p>هذه مخالفة للمادة 7 (منع الغش في طبيعة المنتج).</p><p><strong>الغرامة القانونية:</strong> 50,000 — 500,000 دج حسب المادة 25.</p><p>بالإضافة إلى <strong>سحب المنتجات</strong> من السوق (المادة 30) و<strong>تعويض المستهلكين</strong>.</p><p>تقدّر الغرامة المتوسطة لهذه المخالفة بـ <strong>200,000 دج</strong> + تكاليف السحب (500 قطعة × سعر البيع).</p>",
    variant="ochre", icon="★"
))

SECTIONS_HTML.append(subsection("تمرين 3: شبكة تقييم مطابقة المنتج", "Exercice 3: Grille d'Évaluation de Conformité"))

SECTIONS_HTML.append(progress_chart(
    title_ar="شبكة تقييم مطابقة منتج نسيجي",
    title_fr="Grille d'Évaluation de Conformité",
    items=[
        ("وسم صحيح", "Étiquetage correct", 5, 5, "#0F4D3A"),
        ("تركيب صحيح", "Composition correcte", 5, 5, "#1B6B52"),
        ("خلو من الكيماويات", "Sans chimique", 4, 5, "#C2932E"),
        ("سلامة الأطفال", "Sécurité enfant", 5, 5, "#1B6B52"),
        ("شهادات الجودة", "Certificats qualité", 3, 5, "#7BA38A"),
    ],
    caption_ar="الشكل 3: شبكة تقييم مطابقة منتج — المجموع 22/25 (88%) — منتج مطابق",
    caption_fr="Figure 3: Grille d'évaluation — Total 22/25 (88%) — produit conforme"
))
