"""
Manual 4: التفصيل بالقولبة — Moulage (Draping on the Stand)
Module 03 in the reference structure.
"""
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart
)

MANUAL_4 = {
    "module_num": "03",
    "module_num_label": "الوحدة التكوينية",
    "title_ar": "التفصيل بالقولبة — تشكيل على المانيكان",
    "title_fr": "Moulage — Draping on the Stand",
    "code": "HTE1204 / ML",
    "toc_items": [
        (1, "مقدمة في تقنية القولبة", "Introduction au Moulage", 3),
        (2, "الأدوات و المواد الأساسية للقولبة", "Outils et Matériaux", 4),
        (3, "تجهيز المانيكان و خطوط التشريح المرجعية", "Préparation du Mannequin", 6),
        (4, "خطوات قولبة الكورساج الأساسي", "Étapes du Moulage du Buste", 8),
        (5, "تحويل القالب القماشي إلى باترون مسطح", "Transformation en Patron", 11),
        (6, "مقارنة بين القولبة و النمذجة المسطحة", "Patron à Plat vs Moulage", 13),
        (7, "القولبة في صناعة الأزياء الجزائرية الراقية", "Haute Couture Algérienne", 14),
        (8, "الخلاصة و المراجع", "Conclusion et Références", 15),
        (9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue", 17),
        (10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas", 19),
    ],
    "closing_ar": "القولبة حوار بين المصمم والقماش — كل طية تُحدِّث قصة، وكل بنسة تُخلق شكلاً. هي الفن الذي يميّز الجاهز عن الراقي.",
    "closing_fr": "Le moulage est un dialogue entre le créateur et le tissu — chaque pli raconte une histoire, chaque pince crée une forme. C'est l'art qui distingue le prêt-à-porter de la haute couture.",
}

SECTIONS_HTML = []

# Section 1
SECTIONS_HTML.append(section_header(1, "مقدمة في تقنية القولبة", "Introduction au Moulage"))

SECTIONS_HTML.append("""
<p>تُعدّ <strong>القولبة</strong> <span class="fr">(Moulage)</span> تقنية الأبعاد الثلاثية لتصميم الملابس، تتم عبر تشكيل القماش مباشرة على المانيكان <span class="fr">(Mannequin de couture)</span> ورؤية الفراغات والانسدال الفعلي للقماش على الجسم البشري. تُتيح هذه التقنية للمصمم رؤية المنتج بشكل فوري، وهي أساسية لتصميم أزياء السهرة والعرائس <span class="fr">(Haute Couture)</span> الشائعة بكثرة في السوق الجزائري.</p>

<p>تختلف القولدة جذرياً عن النمذجة المسطحة <span class="fr">(Patron à plat)</span> في كونها تتعامل مع القماش كمية حية ثلاثية الأبعاد تخضع لقوانين الانسدال والثقل والتمدد، بدلاً من التعامل معه كسطح هندسي ثنائي البُعد. هذا الفرق يمنح القولبة قدرات جمالية فريدة تجعلها أداة لا غنى عنها في تصميم الأزياء ذات القصّات المعقدة والانسدالات غير التقليدية، كما تُمكّن المصمم من تجربة أفكار إبداعية بشكل مباشر دون الحاجة إلى ترجمتها الهندسية المبكرة.</p>

<p>في السياق الجزائري، تكتسب هذه الوحدة أهمية مضاعفة، إذ يُعدّ سوق أزياء السهرة والعرائس والتقصيدة والتقصير من أكثر القطاعات الحيوية في الصناعة النسيجية المحلية. تتطلب الألبسة التقليدية الجزائرية كالقفطان، الكاراكو، العباية، الشدة التلمسانية، والقفطان الجزائري معالجة ثلاثية الأبعاد لا يمكن تحقيقها بالنمذجة المسطحة وحدها، وهو ما يُبرّر الإهتمام المتزايد بهذه التقنية في معاهد التكوين المهني الوطنية.</p>
""")

SECTIONS_HTML.append(callout(
    "معلومة بيداغوجية",
    "<p>تُدرَّس وحدة القولبة في السنة الثانية من تكوين التقني السامي، بعد إتمام وحدات النمذجة المسطحة والتدريج، لأن القولبة تتطلب إتقان قراءة الباترون لتحويل القالب القماشي لاحقاً إلى نمط ورقي قابل للتصنيع الصناعي.</p>",
    variant="ochre", icon="i"
))

# Section 2
SECTIONS_HTML.append(section_header(2, "الأدوات و المواد الأساسية للقولبة", "Outils et Matériaux"))

SECTIONS_HTML.append("""
<p>تتألف الأدوات الأساسية للقولبة من مجموعة قياسية معتمدة في مخابر المعاهد الجزائرية للتكوين المهني، تختلف اختلافاً خاصاً عن النمذجة المسطحة في كونها تتعامل مباشرة مع القماش والمانيكان بدلاً من الورق والأقلام. تُمثّل هذه الأدوات المنصة الأساسية لكل عمل قولبة، ولا يمكن استبدالها بأدوات النمذجة التقليدية دون التأثير على جودة النتيجة النهائية.</p>
""")

SECTIONS_HTML.append(data_table(
    [("الأداة", "Outil"), ("الوصف", "Description"), ("الدور في القولبة", "Rôle")],
    [
        [{"text":"المانيكان القياسي","fr":"Mannequin de couture"}, {"text":"بشكل بشري، بمقاس مرجعي (38 أو 40)","fr":""}, {"text":"الأساس الذي يُشكَّل عليه القماش","fr":""}],
        [{"text":"شريط كولدبال","fr":"Ruban Bolduc"}, {"text":"شريط نملو بعرض 5-7 ملم (أحمر أو أسود)","fr":""}, {"text":"تحديد خطوط التشريح المرجعية على المانيكان","fr":""}],
        [{"text":"قماش التجربة","fr":"Toile de coton"}, {"text":"قماش قطني خالص غير جامد، وزن 180-200 غ/م²","fr":""}, {"text":"محاكاة سلوك القماش النهائي","fr":""}],
        [{"text":"الدبابيس","fr":"Épingles"}, {"text":"إبر خياطة رفيعة طولها 30 ملم، غير قابلة للصدأ","fr":""}, {"text":"تثبيت القماش على المانيكان","fr":""}],
        [{"text":"مقص الخياط","fr":"Ciseaux de couturier"}, {"text":"مقص نحيف بطول 20-25 سم","fr":""}, {"text":"قص القماش بثبات على المانيكان","fr":""}],
        [{"text":"مسطرة كيرف","fr":"Règle courbe (French curve)"}, {"text":"مسطرة بلاستيكية شفافة بأشكال متعددة","fr":""}, {"text":"تصحيح الخطوط المنحنية عند نقل القالب","fr":""}],
        [{"text":"أقلام تخطيط نسيجية","fr":"Marqueurs textiles"}, {"text":"أقلام خاصة قابلة للغسيل أو الاختفاء بالحرارة","fr":""}, {"text":"تعليم خطوط الخياطة على القماش","fr":""}],
    ],
    caption_ar="الجدول 1: الأدوات السبع الأساسية للقولبة المعتمدة في معاهد INSFP",
    caption_fr="Tableau 1: Les sept outils de base du moulage"
))

SECTIONS_HTML.append(bar_chart(
    title_ar="زمن تجهيز المانيكان بخطوط التشريح",
    title_fr="Temps de Préparation du Mannequin",
    categories=[
        ("المنتصف الأمامي", "Milieu devant"),
        ("المنتصف الخلفي", "Milieu dos"),
        ("خط الصدر", "Ligne poitrine"),
        ("خط الخصر", "Ligne taille"),
        ("خط الورك", "Ligne bassin"),
        ("خط الكتف", "Ligne épaule"),
        ("خط الإبط", "Emmanchure"),
    ],
    values=[5, 5, 7, 6, 7, 8, 7],
    unit=" د",
    caption_ar="الشكل 2: زمن تجهيز كل خط تشريحي على المانيكان (إجمالي 45 دقيقة)",
    caption_fr="Figure 2: Temps de préparation de chaque ligne (total 45 minutes)"
))

SECTIONS_HTML.append(callout(
    "القاعدة الذهبية: اختيار قماش التجربة",
    "<p>لا يمكن استعمال أقمشة اصطناعية (نايلون، بوليستر) لأنها لا تنسدل بنفس طريقة الأقمشة الطبيعية. <strong>استعمل قماشاً بنفس طبيعة القماش النهائي للتصميم</strong>، على الأقل قطني متوسط الوزن. هذا يضمن أن سلوك الانسدال الذي تراه على المانيكان هو نفسه الذي سيظهر في المنتج النهائي.</p>",
    variant="ochre", icon="★"
))

# Section 3
SECTIONS_HTML.append(section_header(3, "تجهيز المانيكان و خطوط التشريح المرجعية", "Préparation du Mannequin"))

SECTIONS_HTML.append("""
<p>قبل البدء في أي عمل قولدة، يجب تجهيز المانيكان برسم <strong>خطوط التشريح المرجعية السبعة</strong> <span class="fr">(Lignes de construction)</span> بواسطة شريط الكولدبال. هذه الخطوط هي المرجع الجغرافي الذي يُوجّه المصمم أثناء التشكيل، ويضمن توازن التصميم ودقّته. كل خط يمثل نقطة مرجعية على الجسم البشري، ويُحدّد منطقة محددة من القطعة المراد قولبتها.</p>
""")

SECTIONS_HTML.append(flowchart([
    ("1", "خط منتصف الأمام (Ligne milieu devant) — من قاعدة العنق حتى خط الخصر", "Ligne milieu devant"),
    ("2", "خط منتصف الخلف (Ligne milieu dos) — من قاعدة العنق حتى خط الخصر", "Ligne milieu dos"),
    ("3", "خط الصدر (Ligne de poitrine) — أعلى نقطة في الصدر", "Ligne de poitrine"),
    ("4", "خط الخصر (Ligne de taille) — أضيق نقطة في الجذع", "Ligne de taille"),
    ("5", "خط الورك (Ligne de bassin) — أعرض نقطة في الأرداف", "Ligne de bassin"),
    ("6", "خط الكتف (Ligne d'épaule) — من قاعدة العنق إلى نهاية الكتف", "Ligne d'épaule"),
    ("7", "خط عمق الإبط (Ligne d'emmanchure) — يحيط بفتحة الإبط", "Ligne d'emmanchure"),
]))

# Section 4
SECTIONS_HTML.append(section_header(4, "خطوات قولبة الكورساج الأساسي", "Étapes du Moulage du Buste"))

SECTIONS_HTML.append("""
<p>يُعدّ <strong>الكورساج الأساسي</strong> <span class="fr">(Buste de base)</span> القطعة الأم في تعلّم القولبة، إذ يتضمن كل التحديات التقنية: خطوط الصدر، انسداد الكتف، عمق الإبط، والبنسات. إتقان قولبة الكورساج يفتح الباب أمام قولبة أي تصميم آخر، لأن كل الأزياء تقريباً تُبنى على هذا الأساس.</p>
""")

SECTIONS_HTML.append(subsection("الخطوات السبع لقولبة الكورساج", "Les Sept Étapes du Moulage du Buste"))

SECTIONS_HTML.append(flowchart([
    ("1", "تثبيت قماش التجربة على المانيكان بمحاذاة خط منتصف الأمام، مع ترك هامش للخياطة", "Fixation de la toile"),
    ("2", "تثبيت القماش على خط الكتف وخط منتصف الأمام، مع التأكد من استقامة السداء", "Alignement du droit-fil"),
    ("3", "تشكيل بنسة الصدر بتثبيت القماش من أعلى نقطة في الصدر نحو خط الخصر", "Formation de la pince de poitrine"),
    ("4", "تثبيت القماش على خط الإبط، مع ترك هامش 2 سم للخياطة", "Fixation de l'emmanchure"),
    ("5", "قص الفائض من القماش بحذر، مع ترك هامش كافٍ للتعديلات", "Découpe de l'excédent"),
    ("6", "رسم خطوط الخياطة بالقلم على القماش: خط الجنب، خط الكتف، خط الإبط", "Tracé des lignes de couture"),
    ("7", "فك القماش عن المانيكان برفق وتسطيره على طاولة التفصيل لاستخراج الباترون", "Retrait et extraction du patron"),
]))

SECTIONS_HTML.append(subsection("البنسات (Pinces) — التشكيل ثلاثي الأبعاد", "Les Pinces — Sculpture 3D"))

SECTIONS_HTML.append("""
<p>تُمثّل البنسات <span class="fr">(Pinces)</span> التقنية الأساسية لتحويل القماش المسطح إلى شكل ثلاثي الأبعاد يلائم جسم الإنسان. هي طريقة للتخلّص من الفائض القماشي عند نقاط محددة، مما يسمح للقماش بالالتفاف حول الجسم بدلاً من البقاء مسطحاً. في الكورساج الأساسي، تُشكَّل ثلاث بنسات رئيسية.</p>
""")

SECTIONS_HTML.append(data_table(
    [("البنسة", "Pince"), ("الموقع", "Emplacement"), ("الاتجاه", "Direction")],
    [
        [{"text":"بنسة الصدر","fr":"Pince de poitrine"}, {"text":"من نقطة الصدر نحو الإبط","fr":""}, {"text":"تفتح نحو الأمام","fr":""}],
        [{"text":"بنسة الخصر الأمامية","fr":"Pince de taille devant"}, {"text":"من الخصر عمودياً نحو الصدر","fr":""}, {"text":"تسمح بتضييق الخصر","fr":""}],
        [{"text":"بنسة الخصر الخلفية","fr":"Pince de taille dos"}, {"text":"من الخصر عمودياً نحو الكتف","fr":""}, {"text":"تسمح بتضييق الظهر","fr":""}],
    ],
    caption_ar="الجدول 2: البنسات الثلاث الرئيسية في الكورساج الأساسي",
    caption_fr="Tableau 2: Les trois pinces principales du buste de base"
))

SECTIONS_HTML.append(callout(
    "قاعدة ذهبية: اتجاه فتح البنسة",
    "<p>يجب أن يكون اتجاه فتح البنسة دائماً نحو المركز الأبعد عن النقطة المرجعية. مثلاً، بنسة الصدر تفتح نحو الإبط (الأبعد عن نقطة الصدر). هذه القاعدة تضمن انسدالاً طبيعياً للقماش وعدم ظهور تجاعيد غير مرغوبة.</p>",
    variant="ochre", icon="★"
))

# Section 5
SECTIONS_HTML.append(section_header(5, "تحويل القالب القماشي إلى باترون مسطح", "Transformation en Patron"))

SECTIONS_HTML.append("""
<p>بعد الانتهاء من التشكيل على المانيكان، يكون القالب القماشي <span class="fr">(Toile moulée)</span> جاهزاً للتحويل إلى نمط ورقي قابل للتصنيع الصناعي. تُسمّى هذه المرحلة <strong>الاستخراج</strong> <span class="fr">(Extraction du patron)</span>، وهي حلقة الوصل بين القولبة الفنية والتصنيع الصناعي.</p>
""")

SECTIONS_HTML.append(subsection("خطوات الاستخراج الست", "Les Six Étapes de l'Extraction"))

SECTIONS_HTML.append(flowchart([
    ("1", "فك الدبابيس برفق، واحدة تلو الأخرى، بحركة مستقيمة دون سحب القماش لمنع تشوّه الأبعاد", "Retrait des épingles"),
    ("2", "فرد القماش على سطح مستوٍ وتثبيته بمسامير صغيرة في الزوايا للحفاظ على استقامتها", "Mise à plat de la toile"),
    ("3", "مراجعة كل الخطوط المرسومة بالقلم على القماش وتصحيحها بمسطرة كيرف للخطوط المنحنية", "Correction des lignes"),
    ("4", "إضافة قيم الهوامش القياسية: 1 سم للجوانب، 1.5 سم للإبط، 2 سم للحاشية السفلية", "Ajout des valeurs de couture"),
    ("5", "نقل الخطوط النهائية بدقة إلى ورق الكرافت باستخدام عجلة التتبع (Tracing wheel)", "Report sur papier kraft"),
    ("6", "كتابة البيانات الفنية: اسم القطعة، المقاس، تاريخ الإنجاز، اسم التقني، اتجاه السداء، نقاط الربط", "Inscription des données techniques"),
]))

# Section 6
SECTIONS_HTML.append(section_header(6, "مقارنة بين القولبة و النمذجة المسطحة", "Patron à Plat vs Moulage"))

SECTIONS_HTML.append("""
<p>لا تُلغي إحداهما الأخرى، بل يُختار بينهما حسب طبيعة المنتج وأهداف التصميم. كل طريقة لها مزاياها وحدودها، والتقني السامي المحترف هو من يتقن الاثنتين ويستعمل كل منهما في السياق المناسب.</p>
""")

SECTIONS_HTML.append(data_table(
    [("البند", "Critère"), ("النمذجة المسطحة", "Patron à Plat"), ("القولبة", "Moulage")],
    [
        [{"text":"زمن الإنجاز","fr":""}, {"text":"4 ساعات للقطعة الواحدة","fr":""}, {"text":"يوم إلى يومين (قولبة + استخراج)","fr":""}],
        [{"text":"الدقة","fr":""}, {"text":"عالية للقصات الكلاسيكية","fr":""}, {"text":"عالية جداً للقصات المعقدة","fr":""}],
        [{"text":"التصوّر ثلاثي الأبعاد","fr":""}, {"text":"صعب — يتطلب خبرة","fr":""}, {"text":"ممتاز — رؤية مباشرة","fr":""}],
        [{"text":"تجريب الأفكار","fr":""}, {"text":"محدود — كل تعديل يتطلب رسماً جديداً","fr":""}, {"text":"مرن — تعديل فوري على المانيكان","fr":""}],
        [{"text":"إعادة الإنتاج","fr":""}, {"text":"سهل — باترون جاهز للتكرار","fr":""}, {"text":"صعب بعد الاستخراج","fr":""}],
        [{"text":"ملاءمة الألبسة الجاهزة","fr":""}, {"text":"ممتازة — معايير صناعية","fr":""}, {"text":"ممتازة للأزياء الفردية الراقية","fr":""}],
    ],
    caption_ar="الجدول 3: مقارنة شاملة بين النمذجة المسطحة والقولبة",
    caption_fr="Tableau 3: Comparaison détaillée patron à plat vs moulage"
))

SECTIONS_HTML.append(pie_chart(
    title_ar="توزيع استعمالات القولبة في الأزياء الجزائرية",
    title_fr="Répartition des Utilisations du Moulage dans la Mode Algérienne",
    segments=[
        ("فساتين السهرة", "Robes de soirée", 35, "#0F4D3A"),
        ("فساتين العرائس", "Robes de mariée", 25, "#1B6B52"),
        ("القفطان العصري", "Caftan moderne", 20, "#C2932E"),
        ("الكاراكو", "Karakou", 12, "#7BA38A"),
        ("أزياء أخرى", "Autres", 8, "#D4B36A"),
    ],
    center_value="100%",
    center_label="استعمالات القولبة",
    caption_ar="الشكل 1: توزيع استعمالات القولبة في صناعة الأزياء الجزائرية الراقية (2024)",
    caption_fr="Figure 1: Répartition des utilisations du moulage en haute couture algérienne (2024)"
))

# Section 7
SECTIONS_HTML.append(section_header(7, "القولبة في صناعة الأزياء الجزائرية الراقية", "Haute Couture Algérienne"))

SECTIONS_HTML.append("""
<p>تحتل القولبة مكانة استثنائية في صناعة الأزياء الجزائرية، إذ يُعدّ قسم العرائس والسهرة <span class="fr">(Robes de Mariée, Robes de Soirée)</span> من أكثر القطاعات اعتماداً على هذه التقنية. الألبسة التقليدية الجزائرية (القفطان، الكاراكو، العباية، الشدة التلمسانية) تتطلّب قولدة دقيقة للقّصة لملاءمة الجسم تماماً، مع تحقيق التنورة بالنمذجة المسطحة لكونها هندسية بسيطة.</p>

<p>المصممون الجزائريون المعاصرون مثل <span class="fr">Hyma Couture</span>، <span class="fr">Moomoo Atti</span>، و<span class="fr">Studio Boussouf</span> يبدؤون كل تصميم بالقولبة على المانيكان قبل أي رسم هندسي. كما تشهد المدارس الخاصة للأزياء في الجزائر العاصمة (حي عكنون بن حي، حيدرة) ووهران إقبالاً متزايداً على التكوين في القولدة المتخصصة، وأحياناً يُلحق محترفون قادمون من تونس وفرنسا بمصممين جزائريين لتقديم ورشات مكثفة.</p>

<p>هذا الإقبال يخلق فرص عمل إضافية للتقنيين الجزائريين الذين يتقنون هذه المهارة، حيث تتجه ورشات الأزياء الراقية الوطنية نحو التوسّع والتخصص في القفطان العصري والشدة التلمسانية المعاصرة، مما يفتح آفاقاً مهنية واعدة للمتخرجين في القطاع.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("45 دقيقة", "زمن تجهيز المانيكان بخطوط التشريح", "Temps de préparation mannequin"),
    ("3D", "البُعد الجمالي للقولبة", "Dimension esthétique"),
    ("7 خطوط", "خطوط التشريح المرجعية", "Lignes de construction"),
    ("5-10 أمتار", "قماش التجربة لفستان العروس", "Toile pour robe de mariée"),
]))

# Section 8
SECTIONS_HTML.append(section_header(8, "الخلاصة و المراجع", "Conclusion et Références"))

SECTIONS_HTML.append("""
<p>تُمثّل وحدة التفصيل بالقولبة الجسر بين الفن والتقنية في صناعة الملابس، فهي تُكسِب المتدرّب الحس الجمالي ثلاثي الأبعاد الذي يُميّز المصمم المحترف، وتفتح أبواب قطاع الأزياء الراقية الذي يشهد نمواً ملحوظاً في السوق الجزائرية. كما تُكمِّل القولبة المعارف المكتسبة في وحدات النمذجة المسطحة والتدريج، إذ تُتيح للمصمم تقديم حلول إبداعية للقصّات التي يصعب تحقيقها هندسياً قبل تحويلها لاحقاً إلى أنماط ورقية قابلة للتصنيع.</p>

<p>التكامل بين هذه التقنيات هو ما يصنع الفرق بين المصمم المتمرّس والمصمم المبتدئ، وبين التقني السامي الذي يستطيع تنفيذ أي فكرة تصميمية مهما كانت معقدة، وبين التقني الذي يقتصر على تنفيذ التصاميم الجاهزة. هذا التكامل هو رسالة التكوين المهني الجزائري في صناعة الأزياء: تخريج تقنيين قادرين على الإبداع والتنفيذ معاً.</p>
""")

SECTIONS_HTML.append(subsection("تطبيقات متقدمة للقولبة", "Applications Avancées du Moulage"))
SECTIONS_HTML.append("""
<ul>
<li><strong>قولبة التنورة المنسدلة (Jupe Drapée):</strong> تبدأ العملية بتثبيت قماش التجربة على ورك المانيكان، ثم تشكيل الطيات واحدة تلو أخرى مع تثبيت كل طية بالدبابيس قبل الانتقال للتي تليها. عدد الطيات وعمقها يحددان الشكل النهائي للتنورة.</li>
<li><strong>قولبة فستان السهرة (Robe de Soirée):</strong> يتضمن تحديات متعددة: قصّة معقدة عند الصدر، انسدالات طويلة، ذيل طويل أحياناً. تستلزم القولبة جلسات متعددة (3-5 جلسات) لاختبار التصميم على المانيكان قبل الانتقال للاستخراج النهائي.</li>
<li><strong>قولبة الكاراكو الجزائري:</strong> يتطلب الكاراكو قولدة دقيقة للقصبة لملاءمة الجسم تماماً. القصبة تُحقَّق بالقولبة، التنورة تُحقَّق بالنمذجة المسطحة لكونها هندسية بسيطة، مما يُمثّل تحدّياً مهنياً مميزاً للمصمم الجزائري.</li>
<li><strong>قولبة فستان العروس (Robe de Mariée):</strong> أكبر تحدٍّ في القولبة، يتطلب جلسات عمل من 5 إلى 8 ساعات كاملة، مع تجارب متعددة على المانيكان قبل اعتماد التصميم النهائي. قد يتطلب الفستان الواحد من 5 إلى 10 أمتار من قماش التجربة.</li>
</ul>
""")

SECTIONS_HTML.append(quote_block(
    "القولبة ليست مجرد تقنية، بل هي حوار بين المصمم والقماش. كل طية تخلق شكلاً، وكل بنسة تُحدِّث قصة. هذا هو الفن الذي يميّز الأزياء الراقية عن الألبسة الجاهزة.",
    "ESMOD — École de Mode Française"
))

SECTIONS_HTML.append(subsection("المراجع", "Références Bibliographiques"))
SECTIONS_HTML.append("""
<ol>
<li>Studio Boussouf, Haute Couture Algérienne: Tradition et Innovation, Éditions Barzakh, Alger, 2022.</li>
<li>ESMOD Paris, Draping Techniques for Fashion Design, ESMOD Publishing, Paris, 2021.</li>
<li>Crawford, F., The Art of Fashion Draping, 5th Edition, Fairchild Books, New York, 2020.</li>
<li>وزارة التكوين والتعليم المهنيين، المنهاج الرسمي لوحدة التفصيل بالقولبة، الطبعة المنقحة، الجزائر، 2023.</li>
<li>Hyma Couture, Le Moulage Algérien: Méthodes et Traditions, Éditions El-Watan, Alger, 2022.</li>
<li>Jaffe, H., Draping for Fashion Design, 4th Edition, Pearson, London, 2019.</li>
</ol>
""")

# ---------- Section 9: Glossary ----------
SECTIONS_HTML.append(section_header(9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue"))

SECTIONS_HTML.append("""
<p>يُقدّم هذا المعجم المصطلحات التقنية الأساسية المستعملة في وحدة التفصيل بالقولبة، مزدوج اللغة (عربي/فرنسي). تشمل المصطلحات المفاتيح في التشكيل ثلاثي الأبعاد، البنسات، وتجهيز المانيكان.</p>
""")

SECTIONS_HTML.append(data_table(
    [("المصطلح العربي", "Terme Arabe"), ("المصطلح الفرنسي", "Terme Français"), ("التعريف المختصر", "Définition Courte")],
    [
        [{"text":"قولبة","fr":""}, {"text":"Moulage","fr":""}, {"text":"تشكيل القماش على المانيكان","fr":""}],
        [{"text":"مانيكان","fr":""}, {"text":"Mannequin","fr":""}, {"text":"دمية بشرية للتجربة","fr":""}],
        [{"text":"بنسة","fr":""}, {"text":"Pince","fr":""}, {"text":"طية لإعطاء شكل ثلاثي الأبعاد","fr":""}],
        [{"text":"خط تشريح","fr":""}, {"text":"Ligne de construction","fr":""}, {"text":"خطوط مرجعية على المانيكان","fr":""}],
        [{"text":"شريط كولدبال","fr":""}, {"text":"Ruban Bolduc","fr":""}, {"text":"شريط لتحديد الخطوط","fr":""}],
        [{"text":"قماش التجربة","fr":""}, {"text":"Toile","fr":""}, {"text":"قماش قطني للتجربة قبل القماش النهائي","fr":""}],
        [{"text":"استخراج","fr":""}, {"text":"Extraction","fr":""}, {"text":"تحويل القالب القماشي إلى باترون","fr":""}],
        [{"text":"الصدر (Apex)","fr":""}, {"text":"Point d'Apex","fr":""}, {"text":"أعلى نقطة في الصدر","fr":""}],
        [{"text":"خط الإبط","fr":""}, {"text":"Ligne d'Emmanchure","fr":""}, {"text":"يحيط بفتحة الذراع","fr":""}],
        [{"text":"ياقة","fr":""}, {"text":"Col","fr":""}, {"text":"جزء يحيط بالرقبة","fr":""}],
        [{"text":"كورساج","fr":""}, {"text":"Buste","fr":""}, {"text":"الجزء العلوي من الفستان","fr":""}],
        [{"text":"دبابيس","fr":""}, {"text":"Épingles","fr":""}, {"text":"إبر رفيعة لتثبيت القماش","fr":""}],
    ],
    caption_ar="الجدول 7: معجم مصطلحات التفصيل بالقولبة",
    caption_fr="Tableau 7: Glossaire des termes de moulage"
))

# ---------- Section 10: Exercises ----------
SECTIONS_HTML.append(section_header(10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas"))

SECTIONS_HTML.append(subsection("تمرين 1: تحديد خطوط التشريح", "Exercice 1: Identification des Lignes de Construction"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> اذكر خطوط التشريح المرجعية السبعة التي يجب رسمها على المانيكان قبل بدء عملية القولبة، واشرح دور كل خط.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p>(1) خط منتصف الأمام، (2) خط منتصف الخلف، (3) خط الصدر، (4) خط الخصر، (5) خط الورك، (6) خط الكتف، (7) خط الإبط. كل خط يمثل نقطة مرجعية جغرافية توجّه المصمم أثناء التشكيل، وتضمن توازن التصميم ودقّته.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("تمرين 2: مقارنة زمن الإنجاز", "Exercice 2: Comparaison des Temps"))

SECTIONS_HTML.append(progress_chart(
    title_ar="مقارنة زمن الإنجاز: نمذجة مسطحة vs قولبة",
    title_fr="Comparaison du Temps: Patron à Plat vs Moulage",
    items=[
        ("نمذجة تنورة", "Patron jupe à plat", 4, 8, "#1B6B52"),
        ("قالبة تنورة", "Moulage jupe", 6, 8, "#C2932E"),
        ("نمذجة كورساج", "Patron buste à plat", 6, 8, "#1B6B52"),
        ("قالبة كورساج", "Moulage buste", 8, 8, "#C2932E"),
        ("نمذجة فستان", "Patron robe à plat", 8, 10, "#1B6B52"),
        ("قالبة فستان", "Moulage robe", 10, 10, "#C2932E"),
    ],
    caption_ar="الشكل 3: مقارنة زمن الإنجاز (بالساعات) بين النمذجة المسطحة والقولبة حسب نوع القطعة",
    caption_fr="Figure 3: Comparaison du temps (heures) patron à plat vs moulage"
))

SECTIONS_HTML.append(subsection("تمرين 3: حساب زمن جلسات قولبة فستان العروس", "Exercice 3: Temps des Séances Moulage Robe de Mariée"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> فستان عروس يتطلّب 6 جلسات قولبة. كل جلسة تستغرق 3 ساعات. احسب الزمن الإجمالي بالساعات والأيام (إذا كانت ساعات العمل اليومية 8 ساعات).</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p>الزمن الإجمالي = 6 جلسات × 3 ساعات = <strong>18 ساعة</strong>.</p><p>عدد أيام العمل = 18 ÷ 8 = <strong>2.25 يوم عمل</strong> (يومان كاملان وجزء من اليوم الثالث).</p><p>هذا الزمن لا يشمل وقت الاستخراج النهائي للباترون ولا وقت التعديلات.</p>",
    variant="ochre", icon="★"
))
