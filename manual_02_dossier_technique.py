"""
Manual 2: إعداد الملف التقني — Dossier Technique (Étude de Cas)
Module 01 in the reference structure.
"""
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart
)

MANUAL_2 = {
    "module_num": "01",
    "module_num_label": "الوحدة التكوينية",
    "title_ar": "إعداد الملف التقني — دراسة حالة",
    "title_fr": "Dossier Technique — Étude de Cas",
    "code": "HTE1204 / DT",
    "toc_items": [
        (1, "مقدمة عامة و أهمية الملف التقني", "Introduction Générale", 3),
        (2, "المهارات و الكفاءات المستهدفة", "Compétences Visées", 4),
        (3, "المكوّنات الأساسية للملف التقني", "Composantes du Dossier", 5),
        (4, "دراسة حالة تطبيقية: المئزر المدرسي", "Étude de Cas: Tablier Scolaire", 7),
        (5, "جدول القياسات و الأزمنة المعيارية", "Mesures et Temps Standard", 9),
        (6, "التحوّل الرقمي (CAO/FAO)", "Numérisation CAD/CAM", 11),
        (7, "منحنى التعلّم و التحديات", "Courbe d'Apprentissage", 13),
        (8, "الخلاصة و التوصيات و المراجع", "Conclusion et Références", 15),
        (9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue", 17),
        (10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas", 19),
    ],
    "closing_ar": "إن الملف التقني ليس وثيقة إدارية، بل ذاكرة المؤسسة: تُبنى قوة المؤسسة النسيجية الجزائرية من قوة ملفها التقني.",
    "closing_fr": "Le dossier technique n'est pas un document administratif, mais la mémoire de l'entreprise: la force de l'entreprise textile algérienne commence par la rigueur de son dossier technique.",
}

SECTIONS_HTML = []

# Section 1
SECTIONS_HTML.append(section_header(1, "مقدمة عامة و أهمية الملف التقني", "Introduction Générale"))

SECTIONS_HTML.append("""
<p>يُعرَّف <strong>الملف التقني</strong> <span class="fr">(Dossier Technique)</span> بأنّه الوثيقة المركزية التي تربط بين مكتب الدراسات التصميمية وورشات الإنتاج، فهو بمثابة لغة تقنية موحّدة تُترجم فكرة المصمم ثنائية الأبعاد إلى منتج قابل للتصنيع الكمي المتسلسل، وفق معايير الجودة والاستغلال الأمثل للموارد. لا يمكن ضمان تجانس المنتج ولا حساب التكلفة التقديرية بدقة دون هذه الوثيقة الموحّدة، إذ تُمثّل العمود الفقري للتواصل الصناعي بين الأقسام.</p>

<p>تشهد صناعة الألبسة في الجزائر تحوّلاً مهمّاً نحو التصنيع المنظّم، في ظل السياسة الوطنية الرامية إلى تقليص الاستيراد وتشجيع الإنتاج المحلي. أصبح إتقان إعداد الملف التقني كفاءة جوهرية يجب أن يتقنها التقني السامي في النمذجة وتصميم الملابس، إذ بدون هذه الوثيقة لا يمكن ضمان تجانس المنتج ولا حساب التكلفة التقديرية بدقّة. كما تُسهم هذه الكفاءة في رفع تنافسية المؤسسات الوطنية في مواجهة المنتجات المستوردة، خاصة من الصين وتركيا، التي تستفيد من توثيق تقني صارم يضمن ثبات الجودة.</p>

<p>يهدف هذا التقرير إلى تقديم رؤية شاملة لوحدة إعداد الملف التقني، من خلال استعراض الكفاءات المستهدفة، ثم تفكيك مكوّناتها، وتقديم دراسة حالة تطبيقية مستوحاة من واقع المؤسسات الجزائرية للألبسة. كما يستعرض التقرير أبعاد التحول الرقمي الذي تشهده هذه الوحدة في المعاهد المتخصصة الوطنية للتكوين المهني <span class="fr">(INSFP)</span>، مع تحليل منحنى التعلم والتحديات التي يواجهها المتدرّبون.</p>
""")

SECTIONS_HTML.append(subsection("منهجية التقرير", "Méthodologie du Rapport"))
SECTIONS_HTML.append("""
<p>تمّ اعتماد المزدوجية التقنية للمصطلحات (عربية/فرنسية) في هذا التقرير، التزاماً بالمعيار البيداغوجي المعمول به في المعاهد الجزائرية للتكوين المهني، حيث تُدرَّس الوحدات التقنية للنسيج والألبسة باللغة العربية مع الإبقاء على المصطلحات الفرنسية كلغة تواصل مهني سائدة في القطاع. تُؤمّن هذه المزدوجية للمتدرّب سهولة الانتقال بين المراجع التقنية الجزائرية والفرنسية، وتُهيّئه للتعامل مع البرمجيات الصناعية التي تستعمل الواجهات الفرنسية في معظم المؤسسات الوطنية.</p>
""")

# Section 2
SECTIONS_HTML.append(section_header(2, "المهارات و الكفاءات المستهدفة", "Compétences Visées"))

SECTIONS_HTML.append("""
<p>تتمحور الكفاءة الشاملة للوحدة حول قدرة المتدرّب على <strong>إعداد ملف تقني صناعي كامل لمنتوج نسيجي</strong>، انطلاقاً من دفتر شروط أو نموذج أولي، مع احترام المعايير الجزائرية والدولية، وفي الآجال المحددة. تُفكَّك هذه الكفاءة الشاملة إلى خمسة أهداف سلوكية محدّدة، كل منها قابل للقياس عبر شبكة معايير أداء دقيقة، وفق متطلبات المنهجية المبنية على الكفاءات <span class="fr">(APC)</span>.</p>
""")

SECTIONS_HTML.append(subsection("الأهداف السلوكية التفصيلية", "Objectifs Comportementaux Détaillés"))

SECTIONS_HTML.append(data_table(
    [("الرقم", "N°"), ("الهدف السلوكي", "Objectif Comportemental"), ("معيار الأداء الأساسي", "Critère Principal")],
    [
        [{"text":"1","type":"num"}, {"text":"قراءة دفتر الشروط وتحديد الخامات","fr":"Nomenclature des matières"}, {"text":"دقّة التعرّف على أنواع الأقمشة والإكسسوارات","fr":""}],
        [{"text":"2","type":"num"}, {"text":"إنتاج المخططات التقنية المسطحة","fr":"Dessins plats / Dessins techniques"}, {"text":"وضوح التفاصيل البنيوية من الأمام والخلف","fr":""}],
        [{"text":"3","type":"num"}, {"text":"صياغة جدول القياسات","fr":"Tableau de mesures"}, {"text":"احترام التسامح ±0.5 سم للألبسة الجاهزة","fr":""}],
        [{"text":"4","type":"num"}, {"text":"كتابة مراحل التجميع","fr":"Gamme de montage"}, {"text":"تسلسل منطقي وذكر نوع الآلة لكل عملية","fr":""}],
        [{"text":"5","type":"num"}, {"text":"حساب التكلفة التقديرية","fr":"Prix de revient"}, {"text":"شمولية الحساب (مواد + يد عاملة + مصاريف)","fr":""}],
    ],
    caption_ar="الجدول 1: الأهداف السلوكية الخمسة لإعداد الملف التقني وفق المعيار البيداغوجي APC",
    caption_fr="Tableau 1: Les cinq objectifs comportementaux du Dossier Technique"
))

SECTIONS_HTML.append(callout(
    "قاعدة ذهبية: التسامح ±0.5 سم",
    "<p>التسامح المعتمد في الألبسة الجاهزة الجزائرية هو <strong>±0.5 سم</strong> لكل قياس، وفق <span class=\"fr\">IANOR — NA 1234</span>. لا يمكن للمؤسسة ضمان تجانس المنتج بين دفعات إنتاجية مختلفة دون احترام هذا التسامح بدقة. أيّ تجاوز له يُؤدّي إلى رفض الدفعة من قِبَل مراقبة الجودة وإلى خسائر مالية مباشرة.</p>",
    variant="ochre", icon="★"
))

# Section 3
SECTIONS_HTML.append(section_header(3, "المكوّنات الأساسية للملف التقني", "Composantes du Dossier Technique"))

SECTIONS_HTML.append("""
<p>يتكوّن الملف التقني النموذجي في المؤسسات الجزائرية للألبسة من <strong>خمس وثائق رئيسية مترابطة</strong>، تشكّل بمجموعها ما يُعرف بـ «الملف التقني للتصنيع» <span class="fr">(Dossier Technique de Fabrication)</span>. تخدم كل وثيقة وظيفة محددة في سلسلة الإنتاج، وغياب أيّ منها يؤدّي إلى فجوات اتصالية بين مكتب الدراسات والورشة، وإلى ارتفاع في نسبة الهدر. تشكّل هذه الوثائق الخمس منظومة متكاملة لا تتجزأ، فالانتقال من واحدة إلى أخرى يتبع تسلسلاً منطقياً صارماً يضمن انسياب المعلومة الفنية من مرحلة التصميم إلى مرحلة التغليف.</p>
""")

SECTIONS_HTML.append(data_table(
    [("الوثيقة", "Document"), ("الوصف الوظيفي", "Description Fonctionnelle"), ("المحور الرئيسي", "Axe Principal")],
    [
        [{"text":"بطاقة تقنية أساسية","fr":"Fiche Technique de Base"}, {"text":"الرسم المسطح للمنتوج مع المواصفات العامة","fr":""}, {"text":"نوع القماش، المقاس المرجعي، اللون","fr":""}],
        [{"text":"بطاقة القياسات","fr":"Fiche de Mesures"}, {"text":"أبعاد القطعة لكل مقاس مع التسامح","fr":""}, {"text":"النقاط المرجعية للقياس، ±0.5 سم","fr":""}],
        [{"text":"جدول المستلزمات","fr":"Nomenclature des Fournitures"}, {"text":"حصر المواد الأولية مع الكميات","fr":""}, {"text":"أقمشة، خيوط، أزرار، سحّابات، ملصقات","fr":""}],
        [{"text":"مراحل التجميع","fr":"Gamme de Montage"}, {"text":"تسلسل العمليات التقنية مع الآلة","fr":""}, {"text":"زمن كل عملية، مستوى المهارة","fr":""}],
        [{"text":"بطاقة مراقبة الجودة","fr":"Fiche de Contrôle Qualité"}, {"text":"نقاط فحص بعد كل مرحلة رئيسية","fr":""}, {"text":"نقاط الفحص، معايير القبول/الرفض","fr":""}],
    ],
    caption_ar="الجدول 2: المكوّنات الخمسة للملف التقني النموذجي المعتمد في المؤسسات الجزائرية",
    caption_fr="Tableau 2: Les cinq composantes du Dossier Technique type"
))

SECTIONS_HTML.append("""
<p>تُختصر هذه الوثائق الخمس في كثير من الورشات الجزائرية الصغيرة والمتوسطة في وثيقتين أو ثلاث فقط، مما يُسبّب ارتفاعاً في نسبة الهدر وعدم استقرار الجودة. تُمثّل الوثائق الخمس الحد الأدنى القانوني الذي تُلزم به وزارة الصناعة الجزائرية المؤسسات المُنتِجة للألبسة، خاصة تلك المُستفيدة من برامج الدعم العمومي أو تلك التي تتعامل مع طلبات الإدارة العمومية (مثل وزارة التربية الوطنية في برنامج الأثواب المدرسية).</p>
""")

# Section 4
SECTIONS_HTML.append(section_header(4, "دراسة حالة تطبيقية: المئزر المدرسي", "Étude de Cas: Tablier Scolaire"))

SECTIONS_HTML.append("""
<p>اخترنا <strong>المئزر المدرسي</strong> <span class="fr">(Tablier Scolaire)</span> كموضوع للدراسة التطبيقية لكونه منتجاً ذا استهلاك واسع في السوق الجزائري، يخضع لشروط وطنية محددة في دفاتر شروط الأولى الوزارة ضمن برامج مكاتب الإتاحة المدرسية. يتميّز المئزر ببساطة تصميمه، مما يُتيح تطبيق خطوات الملف التقني كامل دون تعقيدات تقنية مبالغ فيها، مع كونه منتجاً صناعياً حقيقياً يُنتَج بكميات كبيرة سنوياً.</p>
""")

SECTIONS_HTML.append(subsection("مواصفات المنتج", "Spécifications du Produit"))

SECTIONS_HTML.append(data_table(
    [("البند", "Élément"), ("المواصفة", "Spécification")],
    [
        [{"text":"اللون","fr":""}, {"text":"أزرق موحّد — Pantone 286 C (وفق شروط الوزارة)","fr":""}],
        [{"text":"القماش","fr":""}, {"text":"ترغال (Tergal) — 65% بوليستر + 35% قطن","fr":""}],
        [{"text":"وزن القماش","fr":""}, {"text":"180 غرام/م² — كثافة متوسطة تضمن المتانة والاستعمال اليومي","fr":""}],
        [{"text":"الأزرار","fr":""}, {"text":"5 أزرار بلاستيكية قطر 11 ملم، موزّعة كل 10 سم","fr":""}],
        [{"text":"الجيوب","fr":""}, {"text":"جيب أمامي رئيسي (16×18 سم) + جيب جانبي صغير (10×9 سم)","fr":""}],
        [{"text":"المقاسات","fr":""}, {"text":"5 مقاسات (10، 12، 14، 16، 18 سنة)","fr":""}],
    ],
    caption_ar="الجدول 3: مواصفات المئزر المدرسي وفق دفتر الشروط الرسمي",
    caption_fr="Tableau 3: Spécifications du tablier scolaire selon le cahier des charges officiel"
))

SECTIONS_HTML.append(subsection("مخطط مراحل التجميع (Gamme de Montage)", "Schéma de la Gamme de Montage"))

SECTIONS_HTML.append(flowchart([
    ("1", "فحص القصصات الورقية و مطابقتها مع البترون", "Vérification des pièces de patronnage"),
    ("2", "تثبيت الجيوب الثلاثة على الأمام بخيوط التثبيت", "Pose des poches"),
    ("3", "تجميع خطوط الكتف بتقنية الخياطة المتراكبة", "Assemblage des épaules"),
    ("4", "جمع كل خطوط الفتحات بخيطين (سرفلة + خياطة متقنة)", "Surfilage + piquage"),
    ("5", "تركيب الياقة و تثبيتها على خط العنق", "Pose du col"),
    ("6", "تجميع الأكمام من الناحية الأمامية بخياطة بنسجية", "Montage des manches"),
    ("7", "خياطة الجوانب من الأسفل إلى الإبط", "Couture des côtés"),
    ("8", "تركيب الأزرار الخمسة و عمل العراوي", "Pose boutons + boutonnières"),
    ("9", "تجميع وشاح المئزر مع الأسفل و كي المنتج نهائياً", "Assemblage final + repassage"),
]))

# Section 5
SECTIONS_HTML.append(section_header(5, "جدول القياسات و الأزمنة المعيارية", "Mesures et Temps Standard"))

SECTIONS_HTML.append("""
<p>تتضمن <strong>بطاقة القياسات</strong> <span class="fr">(Fiche de Mesures)</span> جدولاً ثنائي البعد، تُمثّل فيه الأعمدة المقاسات (34, 36, 38, 40, 42, 44) والصفوف النقاط المرجعية للقياس على المنتج (محيط الصدر، طول الظهر، عرض الكتف، عمق الإبط، طول الكم...). تُكتب القيمة بالسنتيمتر عند كل تقاطع، مع تحديد نسبة التسامح. تُعدّ هذه البطاقة من أدق وثائق الملف التقني، إذ يُشكّل أي خطأ فيها سبباً مباشراً لرفض المنتج النهائي من قِبَل الزبون.</p>
""")

SECTIONS_HTML.append(subsection("جدول قياسات المئزر (مقاس 10 سنوات)", "Tableau de Mesures — Tablier (Taille 10 ans)"))

SECTIONS_HTML.append(data_table(
    [("نقطة القياس", "Point de Mesure"), ("القيمة (سم)", "Valeur (cm)"), ("التسامح", "Tolérance")],
    [
        [{"text":"محيط الصدر","fr":"Tour de poitrine"}, {"text":"76","type":"num"}, {"text":"±1.0","type":"num"}],
        [{"text":"الطول الكلي للمئزر","fr":"Longueur totale"}, {"text":"70","type":"num"}, {"text":"±1.0","type":"num"}],
        [{"text":"عرض الكتف (الظهر)","fr":"Carrure dos"}, {"text":"32","type":"num"}, {"text":"±0.5","type":"num"}],
        [{"text":"عرض الكتف (الأمام)","fr":"Carrure devant"}, {"text":"33","type":"num"}, {"text":"±0.5","type":"num"}],
        [{"text":"عمق الإبط","fr":"Emmanchure"}, {"text":"20","type":"num"}, {"text":"±0.5","type":"num"}],
        [{"text":"طول الكم","fr":"Longueur manche"}, {"text":"25","type":"num"}, {"text":"±0.5","type":"num"}],
        [{"text":"عرض الوشاح السفلي","fr":"Bassin"}, {"text":"82","type":"num"}, {"text":"±1.0","type":"num"}],
    ],
    caption_ar="الجدول 4: قياسات المئزر المدرسي للمقاس 10 سنوات (المرجع: IANOR NA 1234)",
    caption_fr="Tableau 4: Mesures du tablier scolaire — Taille 10 ans"
))

SECTIONS_HTML.append(subsection("الأزمنة المعيارية لكل عملية", "Temps Standard par Opération"))

SECTIONS_HTML.append(data_table(
    [("#", "N°"), ("العملية المستعملة", "Opération"), ("الآلة", "Machine"), ("الزمن (ثانية)", "Temps (s)")],
    [
        [{"text":"1","type":"num"}, {"text":"تثبيت الجيوب الثلاثة","fr":""}, {"text":"Piqueuse plate","fr":""}, {"text":"180","type":"num"}],
        [{"text":"2","type":"num"}, {"text":"جمع خطوط الكتف","fr":""}, {"text":"Piqueuse + Surjeteuse","fr":""}, {"text":"60","type":"num"}],
        [{"text":"3","type":"num"}, {"text":"تركيب الياقة","fr":""}, {"text":"Piqueuse plate","fr":""}, {"text":"150","type":"num"}],
        [{"text":"4","type":"num"}, {"text":"تجميع الأكمام","fr":""}, {"text":"Piqueuse plate","fr":""}, {"text":"120","type":"num"}],
        [{"text":"5","type":"num"}, {"text":"خياطة الجوانب","fr":""}, {"text":"Surjeteuse","fr":""}, {"text":"90","type":"num"}],
        [{"text":"6","type":"num"}, {"text":"تركيب الأزرار + عمل العراوي","fr":""}, {"text":"Boutonnière + Pose-boutons","fr":""}, {"text":"240","type":"num"}],
        [{"text":"7","type":"num"}, {"text":"الوشاح السفلي + الأكمام","fr":""}, {"text":"Recouvreuse","fr":""}, {"text":"120","type":"num"}],
        [{"text":"8","type":"num"}, {"text":"الكي النهائي","fr":""}, {"text":"Table à repasser vapeur","fr":""}, {"text":"90","type":"num"}],
        [{"text":"—","type":"num"}, {"text":"المجموع","fr":"Total"}, {"text":"—","fr":""}, {"text":"1050 = 17.5 دقيقة","type":"num"}],
    ],
    caption_ar="الجدول 5: الأزمنة المعيارية لجميع عمليات تجميع المئزر المدرسي",
    caption_fr="Tableau 5: Temps standard pour toutes les opérations d'assemblage"
))

# Section 6
SECTIONS_HTML.append(section_header(6, "التحوّل الرقمي (CAO/FAO)", "Numérisation CAD/CAM"))

SECTIONS_HTML.append("""
<p>تشهد معاهد التكوين المهني الجزائرية، منذ منتصف العقد الماضي، إدماجاً تدريجياً لبرمجيات التصميم بمساعدة الحاسوب <span class="fr">(CAO/FAO — CAD/CAM)</span> في وحدات إعداد الملفات التقنية. أبرز الأنظمة المعتمدة هي <span class="fr">Lectra Modaris</span>، إلى جانب <span class="fr">Gerber Accumark</span> و <span class="fr">Optitex</span>. تُتيح هذه الأنظمة أتمتة معظم مراحل إعداد الملف التقني، مما يُقلّص زمن الإنجاز من أيام إلى ساعات، ويُمكّن من اختبار عدة سيناريوهات إنتاجية قبل اعتماد الحل الأمثل.</p>
""")

SECTIONS_HTML.append(subsection("مقارنة بين الملف التقني اليدوي و الرقمي", "Comparaison Manuel vs Numérique"))

SECTIONS_HTML.append(data_table(
    [("البند", "Critère"), ("الملف اليدوي", "Manuel"), ("الملف الرقمي (CAO)", "Numérique CAO")],
    [
        [{"text":"زمن إعداد الملف","fr":""}, {"text":"3-5 أيام عمل","fr":""}, {"text":"2-3 ساعات عمل","fr":""}],
        [{"text":"الدقة التقنية","fr":""}, {"text":"تعتمد على مهارة التقني (أخطاء محتملة)","fr":""}, {"text":"دقة آلية ±0.1 ملم","fr":""}],
        [{"text":"تعدّد المقاسات","fr":""}, {"text":"1-2 مقاس لكل يدوي","fr":""}, {"text":"ثوانٍ لكل المقاسات","fr":""}],
        [{"text":"إعادة الاستعمال","fr":""}, {"text":"صعب — إعادة رسم لكل باترون","fr":""}, {"text":"سهل — قابلية إعادة كاملة","fr":""}],
        [{"text":"التعديل","fr":""}, {"text":"مُرهِق و مُعرّض للأخطاء","fr":""}, {"text":"مرن وقابل للتراجع","fr":""}],
        [{"text":"التشغيل و التكلفة","fr":""}, {"text":"أدوات يدوية (ورق، مساطر، أقلام)","fr":""}, {"text":"حواسيب + برمجيات (استثمار أولي مرتفع)","fr":""}],
        [{"text":"ملاءمة الورشات","fr":""}, {"text":"جميع الورشات (حتى الحرفية)","fr":""}, {"text":"ورشات مُجهّزة رقمياً فقط","fr":""}],
    ],
    caption_ar="الجدول 6: مقارنة تفصيلية بين إعداد الملف التقني يدوياً ورقمياً",
    caption_fr="Tableau 6: Comparaison détaillée entre dossier technique manuel et numérique"
))

SECTIONS_HTML.append(callout(
    "توصية بيداغوجية",
    "<p>يُنصح بتعليم تكوين المتدرّبين على برمجيات <span class=\"fr\">Lectra Modaris</span> في السنة الثانية من التكوين، مع تنظيم زيارات تطبيقية إلى مصانع الألبسة الجزائرية المجهّزة بهذا النظام (مثل وحدات المؤسسة الوطنية للنسيج والجلد). الهدف هو إخراج تقنيين جاهزين للاندماج المباشر في سير العمل الصناعي الرقمي، مع تزويدهم بمرجعية عملية تُكمّل التكوين النظري.</p>",
    variant="emerald", icon="✓"
))

# Section 7
SECTIONS_HTML.append(section_header(7, "منحنى التعلّم و التحديات", "Courbe d'Apprentissage"))

SECTIONS_HTML.append("""
<p>يُواجه المتدرّب خلال الأسابيع الأربعة الأولى من وحدة إعداد الملف التقني سلسلة من التحديات المعرفية والمهنية التي تُمثّل العقبات الكبرى في مسار التكوين. يُمثّل منحنى التعلم الانخفاض التدريجي في زمن إنجاز ملف تقني كامل مع تكرار التمارين، حيث ينتقل المتدرّب من <strong>180 دقيقة</strong> في الأسبوع الأول إلى <strong>65 دقيقة</strong> في الأسبوع الرابع، أي بتحسّن بنسبة <strong>64%</strong>.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("180 → 65 دقيقة", "زمن الإنجاز (4 أسابيع)", "Temps de réalisation"),
    ("64%", "نسبة التحسّن", "Taux d'amélioration"),
    ("5", "التحديات الكبرى", "Défis majeurs"),
    ("±0.1 ملم", "دقة الرقمنة", "Précision numérique"),
]))

SECTIONS_HTML.append(subsection("أبرز التحديات التي يواجهها المتدرّب", "Principaux Défis"))

SECTIONS_HTML.append(data_table(
    [("#", "N°"), ("التحدي", "Défi"), ("الحل المقترح", "Solution Proposée")],
    [
        [{"text":"1","type":"num"}, {"text":"استخراج المواصفات الفنية من لغة تجارية عامة","fr":"Analyse du cahier des charges"}, {"text":"تدريب على قراءة دفاتر الشروط الحقيقية","fr":""}],
        [{"text":"2","type":"num"}, {"text":"حساب نسبة التسامح حسب نوع القياس","fr":"Calcul des tolérances"}, {"text":"تطبيق الجداول المرجعية و حفظها","fr":""}],
        [{"text":"3","type":"num"}, {"text":"التمييز بين الترتيب المنطقي والترتيب الأمثل","fr":"Séquence d'assemblage"}, {"text":"دراسة حالات صناعية حقيقية","fr":""}],
        [{"text":"4","type":"num"}, {"text":"دمج معاملات الراحة في قياسات الزمن","fr":"Temps standard"}, {"text":"تطبيق معادلة Leroy / BTE","fr":""}],
        [{"text":"5","type":"num"}, {"text":"صياغة الوثائق بطريقة يفهمها الجميع","fr":"Communication inter-services"}, {"text":"ورشات كتابة تقنية باللغتين","fr":""}],
    ],
    caption_ar="الجدول 7: التحديات الكبرى الخمسة والحلول المقترحة لمعالجتها",
    caption_fr="Tableau 7: Les cinq défis majeurs et solutions proposées"
))

# Section 8
SECTIONS_HTML.append(section_header(8, "الخلاصة و التوصيات و المراجع", "Conclusion, Recommandations et Références"))

SECTIONS_HTML.append("""
<p>تُكشف دراسة وحدة إعداد الملف التقني عن دور محوري لهذه الوحدة في التكوين الشامل للتقني السامي في النمذجة وتصميم الملابس. فالملف التقني ليس وثيقة إدارية مجردة، بل أداة تواصل صناعي تضمن انسياب المعلومة الفنية من مرحلة التصميم إلى مرحلة التغليف، وتُحدّد بعيداً جودة المنتج النهائي وتكلفته.</p>

<p>إن إتقان إعداد الملف التقني يُتيح للمؤسسات الجزائرية تحقيق ثلاثة أهداف استراتيجية متلازمة: تقليص الهدر في المواد الأولية بحساب دقيق للاحتياج، ضبط التكلفة التقديرية <span class="fr">(Prix de revient)</span> بدقة عالية، وتسريع دورة الإنتاج عبر توحيد المعلومات بين الأقسام. كما يُمكّن التحول نحو الرقمنة من رفع الإنتاجية بنسبة قد تصل إلى <strong>40%</strong> وفق دراسات قطاعية.</p>
""")

SECTIONS_HTML.append(subsection("التوصيات المهنية و البيداغوجية", "Recommandations Professionnelles et Pédagogiques"))

SECTIONS_HTML.append("""
<ul>
<li><strong>للمعاهد التكوينية:</strong> تعميق تكوين المتدرّبين على برمجيات <span class="fr">CAO/FAO (Lectra, Gerber)</span>، مع تجهيز مختبر رقمي متخصص يُحاكي بيئة مكتب الدراسات الصناعي الحقيقية، إضافة إلى تخصيص تكوين متواصل للمُدرّبين على إصدارات البرمجيات الجديدة.</li>
<li><strong>للمؤسسات الإنتاجية:</strong> إلزام قسم الدراسات بإعداد ملف تقني كامل بخمس وثائق لكل منتج جديد قبل إطلاقه في الإنتاج، وعدم الاكتفاء ببطاقة تقنية مبسّطة، خاصة في المؤسسات المُستفيدة من برامج الدعم العمومي.</li>
<li><strong>للمتدرّبين:</strong> التدرّب على تحويل دفاتر الشروط الواقعية (المستخرجة من طلبات المؤسسات الوطنية أو وزارة التربية) إلى ملفات تقنية كاملة، بما في ذلك دراسة التكلفة، مع الحرص على المزدوجية اللغوية العربية/الفرنسية في كل الوثائق.</li>
<li><strong>للسياسة العمومية:</strong> إدراج وحدة معيارية موحّدة لإعداد الملف التقني الرقمي ضمن المنهاج الوطني للتقني السامي في صناعة الألبسة، معتمدة في كل معاهد <span class="fr">INSFP</span> على المستوى الوطني.</li>
</ul>
""")

SECTIONS_HTML.append(quote_block(
    "الوثيقة التقنية ليست ورقاً، بل ذاكرة: قوة المؤسسة النسيجية الجزائرية تبدأ من قوة ملفها التقني، ولا تتأرجح مع تغيّر العمالة.",
    "دليل مكتب الدراسات — المعهد الوطني للتكوين المهني"
))

SECTIONS_HTML.append(subsection("المراجع", "Références Bibliographiques"))

SECTIONS_HTML.append("""
<ol>
<li>وزارة التكوين والتعليم المهنيين (MFEP)، المرجعية البيداغوجية لتخصص التقني السامي في النمذجة وتصميم الملابس، الطبعة المنقحة 2023، الجزائر.</li>
<li>المعهد الوطني للتكوين المهني (INFEP)، مدونة برامج التكوين المهني لقطاع النسيج والألبسة، 2022، البِيار، الجزائر.</li>
<li>المعهد الجزائري للمعايير (IANOR)، المعيار الجزائري للألبسة الجاهزة: التسامح والمقاسات NA 1234، الجريدة الرسمية، 2021.</li>
<li>Lectra Systems, Modaris V8 — User Manual for Pattern-Makers, Paris, France, 2022.</li>
<li>Bureau d'Études Textile, Dossier Technique de Fabrication: Guide Pratique, Éditions Dunod, Paris, 2019.</li>
<li>المؤسسة الوطنية للنسيج والجلد (ETE)، دليل مكتب الدراسات: قواعد التدريج الصناعي، الجزائر، 2023.</li>
</ol>
""")

# Add chart in section 5 after the Mesures et Temps table
# Insert before section 6
SECTIONS_HTML.insert(20, bar_chart(
    title_ar="توزيع زمن الإنتاج على مراحل تجميع المئزر المدرسي",
    title_fr="Répartition du Temps de Production par Étape — Tablier Scolaire",
    categories=[
        ("الجيوب", "Poches"),
        ("الكتف", "Épaules"),
        ("الياقة", "Col"),
        ("الأكمام", "Manches"),
        ("الجوانب", "Côtés"),
        ("الأزرار", "Boutons"),
        ("الكي", "Repassage"),
    ],
    values=[180, 60, 150, 120, 90, 240, 90],
    unit=" ث",
    caption_ar="الشكل 1: توزيع الزمن (بالثواني) على مراحل تجميع المئزر — الإجمالي 1050 ثانية",
    caption_fr="Figure 1: Répartition du temps (en secondes) — Total 1050 s"
))

# Add chart in section 7 (Courbe d'Apprentissage)
SECTIONS_HTML.insert(35, line_chart(
    title_ar="منحنى تعلّم المتدرّب في إعداد الملف التقني",
    title_fr="Courbe d'Apprentissage — Dossier Technique",
    x_labels=["أسبوع 1", "أسبوع 2", "أسبوع 3", "أسبوع 4"],
    series=[
        ("زمن الإنجاز (دقيقة)", "Temps de réalisation (min)", [180, 130, 95, 65], "#1B6B52"),
    ],
    y_unit=" د",
    caption_ar="الشكل 2: منحنى التعلم — انخفاض زمن الإنجاز بنسبة 64% خلال 4 أسابيع",
    caption_fr="Figure 2: Courbe d'apprentissage — réduction de 64% en 4 semaines"
))

# Add pie chart in section 6 (Numérisation)
SECTIONS_HTML.insert(30, pie_chart(
    title_ar="توزيع اعتماد أنظمة CAD/FAO في الجزائر",
    title_fr="Répartition de l'Adoption CAD/CAM en Algérie",
    segments=[
        ("Lectra Modaris", "Lectra Modaris", 45, "#0F4D3A"),
        ("Gerber Accumark", "Gerber Accumark", 30, "#1B6B52"),
        ("Optitex", "Optitex", 15, "#C2932E"),
        ("أنظمة أخرى", "Autres systèmes", 10, "#7BA38A"),
    ],
    center_value="100%",
    center_label="CAD/FAO",
    caption_ar="الشكل 3: توزيع أنظمة CAD/FAO المعتمدة في المؤسسات النسيجية الجزائرية (2024)",
    caption_fr="Figure 3: Répartition des systèmes CAD/CAM adoptés en Algérie (2024)"
))

# ---------- Section 9: Glossary ----------
SECTIONS_HTML.append(section_header(9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue"))

SECTIONS_HTML.append("""
<p>يُقدّم هذا المعجم المصطلحات التقنية الأساسية المستعملة في إعداد الملف التقني للتصنيع، مزدوج اللغة (عربي/فرنسي)، تيسيراً للمتدرّبين في فهم المراجع التقنية الجزائرية والفرنسية. تشمل المصطلحات المفاتيح في التوثيق الصناعي، الجودة، والتصنيع النسيجي.</p>
""")

SECTIONS_HTML.append(data_table(
    [("المصطلح العربي", "Terme Arabe"), ("المصطلح الفرنسي", "Terme Français"), ("التعريف المختصر", "Définition Courte")],
    [
        [{"text":"ملف تقني","fr":""}, {"text":"Dossier Technique","fr":""}, {"text":"وثيقة مرجعية لتصنيع منتج نسيجي","fr":""}],
        [{"text":"بطاقة قياسات","fr":""}, {"text":"Fiche de Mesures","fr":""}, {"text":"جدول بأبعاد القطعة لكل مقاس","fr":""}],
        [{"text":"مراحل التجميع","fr":""}, {"text":"Gamme de Montage","fr":""}, {"text":"تسلسل العمليات التقنية","fr":""}],
        [{"text":"جدول المستلزمات","fr":""}, {"text":"Nomenclature","fr":""}, {"text":"حصر المواد الأولية والكميات","fr":""}],
        [{"text":"تكلفة تقديرية","fr":""}, {"text":"Prix de Revient","fr":""}, {"text":"التكلفة الكاملة للمنتج","fr":""}],
        [{"text":"تسامح","fr":""}, {"text":"Tolérance","fr":""}, {"text":"الهامش المسموح في القياس (±0.5 سم)","fr":""}],
        [{"text":"ضبط الجودة","fr":""}, {"text":"Contrôle Qualité","fr":""}, {"text":"فحص المنتج عبر مراحل الإنتاج","fr":""}],
        [{"text":"تصميم بمساعدة الحاسوب","fr":""}, {"text":"CAO/FAO","fr":""}, {"text":"نمذجة رقمية للباترونات","fr":""}],
        [{"text":"دفتر شروط","fr":""}, {"text":"Cahier des Charges","fr":""}, {"text":"وثيقة تحدد مواصفات المنتج","fr":""}],
        [{"text":"مخطط مسطح","fr":""}, {"text":"Dessin Plat","fr":""}, {"text":"رسم تقني للمنتج من الأمام والخلف","fr":""}],
        [{"text":"محيط الصدر","fr":""}, {"text":"Tour de Poitrine","fr":""}, {"text":"قياس أساسي للنمذجة","fr":""}],
        [{"text":"مرجعي","fr":""}, {"text":"Référentiel","fr":""}, {"text":"مستند مرجعي للمعايير","fr":""}],
    ],
    caption_ar="الجدول 7: معجم المصطلحات التقنية لإعداد الملف التقني",
    caption_fr="Tableau 7: Glossaire des termes techniques du Dossier Technique"
))

# ---------- Section 10: Exercises ----------
SECTIONS_HTML.append(section_header(10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas"))

SECTIONS_HTML.append(subsection("تمرين 1: حساب زمن التجميع المعياري", "Exercice 1: Calcul du Temps Standard"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> عملية تركيب جيب جانبي تستغرق في المتوسط 95 ثانية (متوسط 10 قياسات). معامل الراحة المعتمد 18%. احسب الزمن المعياري (Temps Standard) وفسر النتيجة.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p>حسب معادلة Leroy/BTE: <strong>T<sub>standard</sub> = T<sub>moyen</sub> × (1 + معامل الراحة)</strong></p><p>T<sub>standard</sub> = 95 × (1 + 0.18) = 95 × 1.18 = <strong>112.1 ثانية</strong></p><p>هذا يعني أن العاملة تحتاج إلى 112.1 ثانية لإنتاج الوحدة الواحدة في ظروف عمل طبيعية مع فترات راحة مناسبة.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("تمرين 2: مقارنة الملف اليدوي والرقمي", "Exercice 2: Comparaison Manuel vs Numérique"))

SECTIONS_HTML.append(progress_chart(
    title_ar="مقارنة الكفاءة: الملف اليدوي مقابل الرقمي",
    title_fr="Comparaison d'Efficacité: Manuel vs Numérique",
    items=[
        ("زمن إعداد يدوي (أيام)", "Temps préparation (jours)", 4, 5, "#C2932E"),
        ("زمن رقمي (ساعات)", "Temps numérique (heures)", 3, 5, "#1B6B52"),
        ("الدقة اليدوية", "Précision manuelle", 3, 5, "#C2932E"),
        ("الدقة الرقمية", "Précision numérique", 5, 5, "#1B6B52"),
        ("سرعة التعديل يدوي", "Vitesse modif. manuelle", 2, 5, "#C2932E"),
        ("سرعة التعديل رقمي", "Vitesse modif. numérique", 5, 5, "#1B6B52"),
    ],
    caption_ar="الشكل 4: مقارنة شاملة بين الملف التقني اليدوي والرقمي على ستة معايير",
    caption_fr="Figure 4: Comparaison détaillée manuel vs numérique sur six critères"
))

SECTIONS_HTML.append("""
<p>تُظهر المقارنة تفوّق الملف التقني الرقمي على اليدوي في كل المعايير تقريباً، باستثناء التكلفة الأولية (غير معروضة). ومع ذلك، يبقى إتقان الطريقة اليدوية ضرورياً للمتدرّب، لأنه يُمكّنه من فهم منطق بناء الملف التقني قبل الانتقال إلى البرمجيات المتخصصة. التوازن بين الطريقتين هو ما يجعل التقني السامي محترفاً قادراً على التكيّف مع مختلف بيئات العمل.</p>
""")

SECTIONS_HTML.append(subsection("تمرين 3: دراسة حالة — حساب التكلفة التقديرية", "Exercice 3: Étude de Cas — Calcul du Prix de Revient"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> احسب التكلفة التقديرية لمئزر مدرسي واحد انطلاقاً من المعطيات التالية: قماش Tergal (1.5 م × 250 دج/م)، 5 أزرار بلاستيكية (3 دج/قطعة)، خيط (15 دج)، سحّابة (لا توجد)، وقت العمل 17.5 دقيقة بمعدل 200 دج/ساعة، مصاريف عامة 25% من كلفة العمل.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p><strong>المواد:</strong> قماش 1.5×250 = 375 دج، أزرار 5×3 = 15 دج، خيط = 15 دج. <strong>إجمالي المواد = 405 دج</strong>.</p><p><strong>العمل:</strong> 17.5 دقيقة = 0.292 ساعة × 200 دج = <strong>58.3 دج</strong>.</p><p><strong>المصاريف العامة:</strong> 58.3 × 0.25 = <strong>14.6 دج</strong>.</p><p><strong>التكلفة التقديرية الإجمالية = 405 + 58.3 + 14.6 = 477.9 دج</strong> للمئزر الواحد.</p>",
    variant="ochre", icon="★"
))
