"""
Manual 3: التدريج — Gradation / Scaling (Patronnage Industriel)
Module 02 in the reference structure.
"""
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart
)

MANUAL_3 = {
    "module_num": "02",
    "module_num_label": "الوحدة التكوينية",
    "title_ar": "التدريج — الباترونات الصناعية",
    "title_fr": "Gradation / Scaling — Patronnage Industriel",
    "code": "HTE1204 / GR",
    "toc_items": [
        (1, "مفهوم التدريج و أهميته الاقتصادية", "Introduction — Gradation", 3),
        (2, "القواعد الرياضية و نظام المحاور الديكارتية", "Principes Mathématiques", 4),
        (3, "جدول مقاييس جسم الإنسان المرجعي", "Barème de Mesures", 6),
        (4, "الخطوات المنهجية لتنفيذ التدريج", "Démarche Méthodologique", 8),
        (5, "دراسة عملية: تدريب تنورة أساسية", "Étude de Cas: Jupe de Base", 10),
        (6, "التدريج اليدوي مقابل الرقمي (CAD)", "Manuel vs Numérique", 12),
        (7, "أخطاء شائعة و طرق معالجتها", "Erreurs Courantes", 14),
        (8, "الخلاصة و المراجع", "Conclusion et Références", 15),
        (9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue", 17),
        (10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas", 19),
    ],
    "closing_ar": "التدريج هو الحلقة المحورية بين التصميم الفردي والتسلسلي الصناعي — معاملة واحدة على نمط واحد تضاعف القيمة السوقية للمنتج دون تكلفة تصميم إضافية.",
    "closing_fr": "La gradation est le pont entre le sur-mesure individuel et la production sérielle industrielle — un seul patron bien gradé multiplie la valeur marchande sans coût de conception supplémentaire.",
}

SECTIONS_HTML = []

# Section 1
SECTIONS_HTML.append(section_header(1, "مفهوم التدريج و أهميته الاقتصادية", "Introduction — Gradation"))

SECTIONS_HTML.append("""
<p>يُعرَّف <strong>التدريج</strong> <span class="fr">(Gradation)</span> بأنّه التقنية البترونية التي تسمح بإنتاج مقاسات مختلفة (أصغر وأكبر) انطلاقاً من مقاس مرجعي <span class="fr">(Taille de base)</span> دون الإخلال بالتوازن الهيكلي والجمالي للملبس الأصلي. يُعدّ من أدق الوحدات البيداغوجية في تخصص النمذجة، إذ يتطلّب دمج المعارف الهندسية مع الحس الجمالي، ويُمثّل الجسر التقني بين التصميم الفردي والتصنيع التسلسلي.</p>

<p>تكتسب هذه الوحدة أهمية مضاعفة في السياق الاقتصادي الجزائري، إذ تنتج معظم المؤسسات النسيجية الوطنية مقاسات محدودة (غالباً من 38 إلى 44 للنساء، ومن 46 إلى 56 للرجال)، في حين يطلب السوق تنوّعاً أوسع. يفتح إتقان التدريج الباب أمام إنتاج سلسلة مقاسات كاملة (من 34 إلى 50) انطلاقاً من نمط أساسي واحد، مما يُضاعف القيمة السوقية للمنتج دون تكلفة تصميم إضافية، كما يُمكّن التقني السامي من تقديم خدمات النمذجة للورشات الصغيرة التي لا تمتلك مكاتب دراسات متخصصة.</p>

<p>وفق إحصائيات وزارة الصناعة الجزائرية لسنة 2023، لا تتجاوز نسبة المؤسسات النسيجية الوطنية التي تنتج أكثر من 5 مقاسات لكل طراز <strong>35%</strong>، مقابل أكثر من <strong>80%</strong> في المؤسسات التركية والصينية المنافسة. يُفسَّر هذا الفارق جزئياً بضعف إتقان التدريج الصناعي، وهو ما تُوليه معاهد <span class="fr">INSFP</span> اهتماماً متزايداً عبر تحديث برامج التكوين وتجهيز المخابر بأنظمة الرقمنة المتقدمة.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("38 — 44", "المقاسات النسائية الأكثر استعمالاً في الجزائر", "Tailles dames les plus courantes"),
    ("4 سم", "الفرق بين مقاسين متتاليين في محيط الصدر", "Écart entre tailles (poitrine)"),
    ("35%", "نسبة المؤسسات الجزائرية (5+ مقاسات)", "Entreprises algériennes (5+ tailles)"),
    ("80%", "نسبة المؤسسات المنافسة (5+ مقاسات)", "Entreprises concurrentes (5+ tailles)"),
]))

# Section 2
SECTIONS_HTML.append(section_header(2, "القواعد الرياضية و نظام المحاور الديكارتية", "Principes Mathématiques"))

SECTIONS_HTML.append("""
<p>يعتمد التدريج على تحديد <strong>نقاط التطور</strong> <span class="fr">(Points d'évolution)</span> على المحورين الديكارتيين ثنائيي البعد <span class="fr">(X, Y)</span>. تتلقى كل نقطة من نقاط الباترون (نقطة الصدر، نقطة الخصر، نقطة الورك...) قيمتين عدديتين تُمثّل انتقالها من المقاس المرجعي إلى المقاس المجاور. تُحسب قيمة التطور <span class="fr">(Valeur d'évolution)</span> وفق معادلة رياضية دقيقة تأخذ في الاعتبار الفرق بين القياسين، عدد المحاور المستقبلة، ومعامل التوزيع الذي يضمن توازن النموذج.</p>
""")

SECTIONS_HTML.append(subsection("نظام المحاور الديكارتية", "Système d'Axes Cartésiens"))

SECTIONS_HTML.append(data_table(
    [("المحور", "Axe"), ("الاتجاه", "Direction"), ("ما يُمثّله من قياسات", "Mesures Représentées")],
    [
        [{"text":"المحور X","fr":"Axe X"}, {"text":"أفقي (يقف)","fr":"Horizontal"}, {"text":"التغيّرات في العرض: محيط الصدر، محيط الخصر، محيط الورك، عرض الكتف، عرض الظهر","fr":""}],
        [{"text":"المحور Y","fr":"Axe Y"}, {"text":"عمودي (يطول)","fr":"Vertical"}, {"text":"التغيّرات في الطول: ارتفاع الورد، ارتفاع البرك، عمق الإبط، الطول الكلي، طول الكم","fr":""}],
    ],
    caption_ar="الجدول 1: نظام المحاور الديكارتية في التدريج",
    caption_fr="Tableau 1: Système d'axes cartésiens pour la gradation"
))

SECTIONS_HTML.append(subsection("حساب قيمة التطور", "Calcul de la Valeur d'Évolution"))

SECTIONS_HTML.append(callout(
    "المعادلة المرجعية للتدريج — INSFP",
    "<p style='text-align:center; direction:ltr; font-size:13pt;'><strong>V<sub>x,y</sub> = (Δ / n) × k</strong></p><p>حيث: <strong>V</strong> = قيمة التطور على المحور (X أو Y) ، <strong>Δ</strong> = الفرق بين قياسين متتاليين ، <strong>n</strong> = عدد المحاور المستقبلة ، <strong>k</strong> = معامل التوزيع (يعتمد على هندسة القطعة).</p>",
    variant="ochre", icon="∑"
))

SECTIONS_HTML.append("""
<p>يخضع مجموع الفروق بين المقاسات لجدول مقاييس جسم الإنسان الموحّد <span class="fr">(Barème de mesures)</span>، المعتمد رسمياً في الجزائر مع تعديلات محلية طفيفة على الجدول الأوروبي <span class="fr">NF EN 13402</span>. يبلغ الفرق بين مقاسين متتاليين عادة <strong>4 سم</strong> في محيط الصدر، ويتم توزيع هذا الفرق على المحاور وفق منطق هندسي يحفظ توازن النموذج وتناسقه الجمالي.</p>
""")

# Section 3
SECTIONS_HTML.append(section_header(3, "جدول مقاييس جسم الإنسان المرجعي", "Barème de Mesures"))

SECTIONS_HTML.append("""
<p>يستعمل التقني السامي في النمذجة جدولاً موحَّداً لمقاييس جسم الإنسان، يُعدّ مرجعاً لكل عمليات التدريج. يُعتمد في المعاهد الجزائرية على الجدول النسائي التالي (المقاسات من 36 إلى 46)، المُستوحى من المعيار الأوروبي <span class="fr">NF EN 13402</span> مع تعديلات محلية بسيطة تأخذ في الاعتبار الخصائص المورفولوجية للمرأة الجزائرية.</p>
""")

SECTIONS_HTML.append(data_table(
    [("نقطة القياس", "Point"), ("م 36", "T36"), ("م 38", "T38"), ("م 40", "T40"), ("م 42", "T42"), ("م 44", "T44"), ("م 46", "T46"), ("الفرق", "Écart")],
    [
        [{"text":"محيط الصدر","fr":"Poitrine"}, {"text":"84","type":"num"}, {"text":"88","type":"num"}, {"text":"92","type":"num"}, {"text":"96","type":"num"}, {"text":"100","type":"num"}, {"text":"104","type":"num"}, {"text":"+4","type":"num"}],
        [{"text":"محيط الخصر","fr":"Taille"}, {"text":"64","type":"num"}, {"text":"68","type":"num"}, {"text":"72","type":"num"}, {"text":"76","type":"num"}, {"text":"80","type":"num"}, {"text":"84","type":"num"}, {"text":"+4","type":"num"}],
        [{"text":"محيط الأرداف","fr":"Bassin"}, {"text":"90","type":"num"}, {"text":"94","type":"num"}, {"text":"98","type":"num"}, {"text":"102","type":"num"}, {"text":"106","type":"num"}, {"text":"110","type":"num"}, {"text":"+4","type":"num"}],
        [{"text":"طول الظهر","fr":"Dos"}, {"text":"38","type":"num"}, {"text":"38.5","type":"num"}, {"text":"39","type":"num"}, {"text":"39.5","type":"num"}, {"text":"40","type":"num"}, {"text":"40.5","type":"num"}, {"text":"+0.5","type":"num"}],
        [{"text":"عرض الكتف","fr":"Carrure"}, {"text":"36","type":"num"}, {"text":"37","type":"num"}, {"text":"38","type":"num"}, {"text":"39","type":"num"}, {"text":"40","type":"num"}, {"text":"41","type":"num"}, {"text":"+1","type":"num"}],
        [{"text":"عمق الإبط","fr":"Emmanchure"}, {"text":"20","type":"num"}, {"text":"20.5","type":"num"}, {"text":"21","type":"num"}, {"text":"21.5","type":"num"}, {"text":"22","type":"num"}, {"text":"22.5","type":"num"}, {"text":"+0.5","type":"num"}],
    ],
    caption_ar="الجدول 2: الجدول المرجعي لمقاييس المرأة الجزائرية (وفق NF EN 13402)",
    caption_fr="Tableau 2: Barème de mesures femme algérienne — NF EN 13402"
))

SECTIONS_HTML.append(line_chart(
    title_ar="تطوّر مقاييس المرأة الجزائرية حسب المقاسات",
    title_fr="Évolution des Mesures Femme Algérienne par Taille",
    x_labels=["36", "38", "40", "42", "44", "46"],
    series=[
        ("محيط الصدر", "Tour poitrine", [84, 88, 92, 96, 100, 104], "#1B6B52"),
        ("محيط الخصر", "Tour taille", [64, 68, 72, 76, 80, 84], "#C2932E"),
        ("محيط الأرداف", "Tour bassin", [90, 94, 98, 102, 106, 110], "#7BA38A"),
    ],
    y_unit=" سم",
    caption_ar="الشكل 1: تطوّر القياسات الرئيسية للمرأة الجزائرية عبر 6 مقاسات (وفق NF EN 13402)",
    caption_fr="Figure 1: Évolution des mesures principales sur 6 tailles (NF EN 13402)"
))

SECTIONS_HTML.append(callout(
    "معلومة تقنية",
    "<p>المقاس <strong>38-40</strong> هو الأكثر استعمالاً في الجزائر، ويُعتبر المقاس المرجعي الذي يُبنى عليه الباترون الأساسي في مكاتب الدراسات الجزائرية. عند تطوير منتج جديد، يُنصح بتثبيت المقاس 40 كأساس، ثم التدريج تصاعدياً وتنازلياً نحو باقي المقاسات.</p>",
    variant="ochre", icon="i"
))

# Section 4
SECTIONS_HTML.append(section_header(4, "الخطوات المنهجية لتنفيذ التدريج", "Démarche Méthodologique"))

SECTIONS_HTML.append("""
<p>يتبع التقني السامي منهجية دقيقة من <strong>سبع خطوات</strong> لتنفيذ أي عملية تدريج، تضمن إمكانية إعادة الإنتاج وتُقلّل من الأخطاء التراكمية التي قد تحدث عند القفز بين المراحل. تُطبَّق هذه المنهجية على كل قطعة من قطع الباترون، سواء كانت أمامية أو خلفية أو كُمّاً، مع مراعاة خصوصيات كل قطعة.</p>
""")

SECTIONS_HTML.append(flowchart([
    ("1", "تثبيت الباترون المرجعي على ورق الكرافت بمسامير دقيقة، مع التأكد من استقامة اتجاه السداء", "Fixation du patron de base"),
    ("2", "تحديد النقاط الرئيسية للتطور (خط الخصر، الورك، الحاشية، الصدر)", "Identification des points d'évolution"),
    ("3", "رسم محور أفقي X وعمودي Y من كل نقطة مرجعية لتوجيه حركة النقطة", "Tracé des axes de projection"),
    ("4", "حساب قيم التطور ونقلها على كل نقطة من جدول المقاييس، مع مراعاة معاملات التوزيع", "Calcul et report des valeurs"),
    ("5", "ربط النقاط الجديدة بمنحنيات ناعمة باستخدام مسطرة French curve", "Reliement par courbes"),
    ("6", "فحص توازن المقاس الجديد بمقارنته بالمرجعي للتأكد من الحفاظ على التناسب", "Vérification de l'équilibre"),
    ("7", "كتابة البيانات الفنية على كل باترون جديد: المقاس، التاريخ، اسم التقني، علامة السداء", "Inscription des données techniques"),
]))

# Section 5
SECTIONS_HTML.append(section_header(5, "دراسة عملية: تدريب تنورة أساسية", "Étude de Cas: Jupe de Base"))

SECTIONS_HTML.append("""
<p>لتسليط الضوء على التطبيق العملي لقواعد التدريج، نُقدّم دراسة حالة لتدريب تنورة نسوية أساسية <span class="fr">(Jupe de base)</span> من المقاس 40 إلى المقاس 42. اختيرت التنورة لكونها قطعة بسيطة هندسياً، تُتيح للطالب استيعاب المنطق دون تشتيت بتعقيدات القصّة ثلاثية الأبعاد.</p>
""")

SECTIONS_HTML.append(subsection("التدرّب من المقاس 40 إلى المقاس 42", "Gradation T40 → T42"))

SECTIONS_HTML.append(data_table(
    [("نقطة القياس", "Point"), ("قيمة التطور X (العرض)", "Évolution X"), ("قيمة التطور Y (الطول)", "Évolution Y"), ("ملاحظة", "Observation")],
    [
        [{"text":"خط الخصر","fr":"Taille"}, {"text":"+0.5 سم","type":"num"}, {"text":"+1.0 سم","type":"num"}, {"text":"موزّع على العبر","fr":""}],
        [{"text":"خط الورك","fr":"Bassin"}, {"text":"+0.5 سم","type":"num"}, {"text":"+1.0 سم","type":"num"}, {"text":"نفس قيمة الخصر","fr":""}],
        [{"text":"خط الحاشية السفلية","fr":"Ourlet"}, {"text":"+1.0 سم","type":"num"}, {"text":"+1.0 سم","type":"num"}, {"text":"اتساع متناسق","fr":""}],
    ],
    caption_ar="الجدول 3: قيم التطور من المقاس 40 إلى المقاس 42 لتنورة أساسية",
    caption_fr="Tableau 3: Valeurs d'évolution T40 → T42 pour jupe de base"
))

SECTIONS_HTML.append(subsection("دراسة حالة موسّعة: تدريج بنطلون رجالي", "Cas Détaillé: Pantalon Homme"))

SECTIONS_HTML.append("""
<p>يتضمن تدريج البنطلون الرجالي <strong>+15 نقطة قياس مرجعية</strong> تتوزّع بين الخصر، الأرداف، الركبة، الكاحل، والطول الكلي، مما يجعله من العمليات الأكثر تعقيداً في النمذجة الصناعية. الفرق بين المقاسات المتتالية ليس موحّداً كما في التنورة، بل يختلف حسب المنطقة: <strong>+4 سم</strong> في محيط الخصر، <strong>+1.5 سم</strong> في الطول الكلي للساق، <strong>+0.3 سم</strong> في عمق الورك.</p>
""")

SECTIONS_HTML.append(data_table(
    [("نقطة القياس", "Point"), ("قيمة التدريج (سم)", "Valeur (cm)"), ("ملاحظة", "Observation")],
    [
        [{"text":"محيط الخصر الكلي","fr":"Taille totale"}, {"text":"+4.0","type":"num"}, {"text":"موزّع على 4 نقاط (1+ لكل نقطة)","fr":""}],
        [{"text":"ارتفاع الخصر","fr":"Hauteur taille"}, {"text":"+0.3","type":"num"}, {"text":"لا يتغيّر في الفتحة","fr":""}],
        [{"text":"محيط الورك الكلي","fr":"Bassin total"}, {"text":"+4.0","type":"num"}, {"text":"موزّع على 4 نقاط","fr":""}],
        [{"text":"عمق الورك","fr":"Profondeur bassin"}, {"text":"+0.5","type":"num"}, {"text":"ارتفاع الورك عن الخصر","fr":""}],
        [{"text":"طول الساق (Inseam)","fr":"Longueur jambe"}, {"text":"+1.5","type":"num"}, {"text":"الفرق في الطول بين المقاسات","fr":""}],
        [{"text":"محيط الركبة","fr":"Genou"}, {"text":"+1.0","type":"num"}, {"text":"موزّع على النصف","fr":""}],
        [{"text":"محيط الكاحل","fr":"Cheville"}, {"text":"+0.5","type":"num"}, {"text":"ضيّق جداً","fr":""}],
    ],
    caption_ar="الجدول 4: القيم الرئيسية لتدريج البنطلون الرجالي (7 نقاط قياس)",
    caption_fr="Tableau 4: Valeurs principales de gradation pantalon homme"
))

# Section 6
SECTIONS_HTML.append(section_header(6, "التدريج اليدوي مقابل الرقمي (CAD)", "Manuel vs Numérique"))

SECTIONS_HTML.append("""
<p>تشهد ورشات صناعة الملابس في الجزائر تحوّلاً تدريجياً نحو الرقمنة، مع أن الورشات الحرفية الصغيرة لا تزال تعتمد على الأسلوب اليدوي بكل حدوده ومزاياه. يجب على التقني السامي إتقان كلتا الطريقتين، لأنه سيواجه واقعين في سوق العمل: ورشات تُحاكي التدريج التقليدي وأخرى تعتمد أنظمة <span class="fr">CAD</span> المتقدمة.</p>
""")

SECTIONS_HTML.append(data_table(
    [("البند", "Critère"), ("التدريج اليدوي", "Manuel"), ("التدريج الرقمي (CAD)", "Numérique CAD")],
    [
        [{"text":"الأدوات","fr":""}, {"text":"مساطر، منحنيات، أقلام رصاص، أوراق","fr":""}, {"text":"حاسوب + برمجيات (Lectra Modaris, Gerber Accumark)","fr":""}],
        [{"text":"زمن إنجاز مقاس","fr":""}, {"text":"1-2 ساعة لكل مقاس إضافي","fr":""}, {"text":"ثوانٍ معدودة لكل المقاسات دفعة واحدة","fr":""}],
        [{"text":"الدقة","fr":""}, {"text":"تعتمد على مهارة التقني (أخطاء محتملة)","fr":""}, {"text":"دقة آلية، أخطاء لا تُذكر","fr":""}],
        [{"text":"إعادة الرسم","fr":""}, {"text":"صعب — يدوي لكل مقاس","fr":""}, {"text":"سهل — برمجي بضغطة زر","fr":""}],
        [{"text":"التشغيل","fr":""}, {"text":"أدوات يدوية بسيطة","fr":""}, {"text":"استثمار أولي مرتفع (حواسيب + برمجيات)","fr":""}],
        [{"text":"ملاءمة الورشات","fr":""}, {"text":"كل الورشات بما فيها الحرفية الصغيرة","fr":""}, {"text":"الورشات المجهّزة رقمياً فقط","fr":""}],
        [{"text":"التكلفة الإجمالية","fr":""}, {"text":"أدوات يدوية (رخيصة)","fr":""}, {"text":"حواسيب + برمجيات (مرتفعة)","fr":""}],
    ],
    caption_ar="الجدول 5: مقارنة شاملة بين التدريج اليدوي والرقمي",
    caption_fr="Tableau 5: Comparaison détaillée gradation manuelle vs numérique"
))

SECTIONS_HTML.append(pie_chart(
    title_ar="توزيع مصادر الأخطاء في التدريج اليدوي",
    title_fr="Répartition des Sources d'Erreurs en Gradation Manuelle",
    segments=[
        ("خطأ رياضي", "Erreur math", 30, "#0F4D3A"),
        ("خطأ رسم", "Erreur tracé", 35, "#1B6B52"),
        ("خطأ قياس", "Erreur mesure", 20, "#C2932E"),
        ("خطأ نقل", "Erreur report", 15, "#7BA38A"),
    ],
    center_value="100%",
    center_label="مصادر الخطأ",
    caption_ar="الشكل 2: تحليل 200 حالة خطأ في التدريج اليدوي — 65% من الأخطاء قابلة للتلافي بالرقمنة",
    caption_fr="Figure 2: Analyse de 200 cas d'erreurs — 65% évitables par numérisation"
))

SECTIONS_HTML.append(callout(
    "توصية",
    "<p>يُنصح، عند تدريج البنطلون، بإنشاء مقاسين متطرفين (الأصغر والأكبر) أولاً، ثم توليد المقاسات الوسطى برسم خط بين النقاط المتطرفة. هذه التقنية <span class=\"fr\">(Interpolation)</span> تُسرّع العمل وتضمن التوازن البصري عبر كل المقاسات.</p>",
    variant="emerald", icon="✓"
))

# Section 7
SECTIONS_HTML.append(section_header(7, "أخطاء شائعة و طرق معالجتها", "Erreurs Courantes"))

SECTIONS_HTML.append("""
<p>يقع المتدرّبون — وحتى التقنيون المتمرّسون — في سلسلة من الأخطاء المتكررة عند تنفيذ التدريج. الوعي المسبق بهذه الأخطاء يُسرّع عملية التعلّم ويُجنّب المؤسسة خسائر إنتاجية. يُلخّص الجدول التالي أبرز خمسة أخطاء مع حلولها المقترحة.</p>
""")

SECTIONS_HTML.append(data_table(
    [("الخطأ", "Erreur"), ("الأثر على الباترون", "Impact"), ("الحل", "Solution")],
    [
        [{"text":"قيمة التطور موحّدة على كل المحاور","fr":""}, {"text":"باترون مشوّه، نسب غير منطقية","fr":""}, {"text":"التحقّق دائماً من جدول المقاييس","fr":""}],
        [{"text":"توزيع الفرق على جهة واحدة فقط","fr":""}, {"text":"باترون مائل، غير متماثل","fr":""}, {"text":"موزّع على العبر عبر النموذج","fr":""}],
        [{"text":"اعتماد مقاس مرجعي غير قياسي","fr":""}, {"text":"توليد مقاسات خاطئة كلها","fr":""}, {"text":"استعمال مقاس 38/40 فقط كأساس","fr":""}],
        [{"text":"إهمال محور الطول Y","fr":""}, {"text":"مقاسات قصيرة جداً بشكل كبير","fr":""}, {"text":"تطبيق قيم Y و X معاً","fr":""}],
        [{"text":"ربط النقاط بخطوط غير ناعمة","fr":""}, {"text":"بطاقة قماش غير قابلة للتنفيذ","fr":""}, {"text":"استعمال مسطرة French curve","fr":""}],
    ],
    caption_ar="الجدول 6: الأخطاء الخمسة الأكثر وعياً في التدريج",
    caption_fr="Tableau 6: Les cinq erreurs les plus fréquentes en gradation"
))

# Section 8
SECTIONS_HTML.append(section_header(8, "الخلاصة و المراجع", "Conclusion et Références"))

SECTIONS_HTML.append("""
<p>تُعدّ وحدة التدريج الحلقة المحورية في الربط بين التصميم الفردي (النمذجة على مقاس واحد) والتسلسلي الصناعي <span class="fr">(Prêt-à-porter)</span>. تفتح هذه المهارة آفاقاً واسعة للمتدرّب للعمل في مكاتب الدراسات والشركات الصناعية، إذ يُعدّ تدريج الباترونات نشاطاً يومياً لا تتوقف عنه أي ورشة إنتاج للألبسة الجاهزة.</p>

<p>تكتسب هذه الكفاءة أهمية اقتصادية وطنية، إذ تُسهم في رفع تنوّع المقاسات المعروضة في السوق الجزائري، وتحقيق رسالة التكوين المهني في النهوض بالقطاع النسيجي الوطني لمواجهة المنتجات المستوردة. يُعادل التدريج الصحيح لنموذج واحد إضافة عشرة منتجات جديدة إلى كتالوج المؤسسة دون تكلفة تصميم إضافية، وهو ما يُبرّر الاستثمار في تكوين التقنيين على هذه المهارة الدقيقة.</p>
""")

SECTIONS_HTML.append(subsection("تطبيقات متقدمة", "Applications Avancées"))
SECTIONS_HTML.append("""
<ul>
<li><strong>تدريج القمصان الرجالية:</strong> يتضمن 12 نقطة قياس مرجعية موزّعة على الأمام، الخلف، الكم، والياقة. الفرق بين المقاسات <span class="fr">S, M, L, XL, XXL</span> يختلف حسب المنطقة: <strong>+4 سم</strong> في محيط الصدر، <strong>+1.5 سم</strong> في عرض الكتف، <strong>+0.5 سم</strong> في طول الظهر.</li>
<li><strong>تدريج بدل النساء (Tailleurs Dames):</strong> تتطلب البدلة النسائية تدريجين مختلفين: الجاكيت يركز على محيط الصدر والكتف، التنورة تركز على الخصر والأرداف، مع الحفاظ على التناسب البصري بين القطعتين عبر كل المقاسات.</li>
<li><strong>تدريج ألبسة الأطفال:</strong> يختلف جذرياً عن الكبار لأن جسم الطفل ينمو بنسب غير منتظمة (رأس أكبر نسبياً، أطراف أقصر). تستعمل معاهد <span class="fr">INSFP</span> جداول قياس خاصة بالأطفال <span class="fr">(NF EN 13402-7)</span> تختلف عن جداول البالغين.</li>
</ul>
""")

SECTIONS_HTML.append(quote_block(
    "ما لا يمكن قياسه لا يمكن تحسينه — هذه القاعدة العلمية هي جوهر التدريج الصناعي، حيث كل مليمتر يُحسب بدقة ويُوزّع بمنطق هندسي صارم.",
    "Leroy — Bureau des Temps Élémentaires (BTE)"
))

SECTIONS_HTML.append(subsection("المراجع", "Références Bibliographiques"))
SECTIONS_HTML.append("""
<ol>
<li>وزارة التكوين والتعليم المهنيين، المناهج التعليمية لمعاهد INSFP — مقياس التدريج وتكبير المقاسات، 2023، الجزائر.</li>
<li>المعهد الجزائري للمعايير (IANOR)، المعيار NF EN 13402-3: مقاييس الملابس — القياسات والأبعاد، 2020، الجزائر.</li>
<li>Lectra Systems, Modaris V8 — Pattern Design & Gradation User Guide, Paris, France, 2022.</li>
<li>المؤسسة الوطنية للنسيج والجلود، دليل مكتب الدراسات: قواعد التدريج الصناعي، 2022، الجزائر.</li>
<li>Gerber Technology, Accumark V12 — Pattern Design & Grading Manual, Tolland CT, USA, 2021.</li>
<li>Hallett, C., Pattern Grading for Women's Clothes: The Imperial Edition, Wiley-Blackwell, London, 2019.</li>
</ol>
""")

# ---------- Section 9: Glossary ----------
SECTIONS_HTML.append(section_header(9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue"))

SECTIONS_HTML.append("""
<p>يُقدّم هذا المعجم المصطلحات التقنية الأساسية المستعملة في وحدة التدريج الصناعي، مزدوج اللغة (عربي/فرنسي). تشمل المصطلحات المفاتيح في حسابات التدريج، نقاط التطور، والمحاور الديكارتية.</p>
""")

SECTIONS_HTML.append(data_table(
    [("المصطلح العربي", "Terme Arabe"), ("المصطلح الفرنسي", "Terme Français"), ("التعريف المختصر", "Définition Courte")],
    [
        [{"text":"تدريج","fr":""}, {"text":"Gradation","fr":""}, {"text":"إنتاج مقاسات متعددة من مقاس مرجعي","fr":""}],
        [{"text":"مقاس مرجعي","fr":""}, {"text":"Taille de Base","fr":""}, {"text":"المقاس الأساسي للبناء","fr":""}],
        [{"text":"نقطة تطور","fr":""}, {"text":"Point d'Évolution","fr":""}, {"text":"نقطة تتحرك عند التدريج","fr":""}],
        [{"text":"قيمة التطور","fr":""}, {"text":"Valeur d'Évolution","fr":""}, {"text":"مقدار حركة النقطة (سم)","fr":""}],
        [{"text":"معامل التوزيع","fr":""}, {"text":"Coefficient k","fr":""}, {"text":"معامل يوزّع الفرق على المحاور","fr":""}],
        [{"text":"المحور الأفقي","fr":""}, {"text":"Axe X","fr":""}, {"text":"يمثّل تغيّرات العرض","fr":""}],
        [{"text":"المحور العمودي","fr":""}, {"text":"Axe Y","fr":""}, {"text":"يمثّل تغيّرات الطول","fr":""}],
        [{"text":"جدول مقاييس","fr":""}, {"text":"Barème de Mesures","fr":""}, {"text":"جدول موحّد لمقاييس الجسم","fr":""}],
        [{"text":"تسامح","fr":""}, {"text":"Tolérance","fr":""}, {"text":"الهامش المسموح في القياس","fr":""}],
        [{"text":"تدريج رقمي","fr":""}, {"text":"Gradation Numérique","fr":""}, {"text":"تدريج بواسطة CAD","fr":""}],
        [{"text":"منحنى فرنسي","fr":""}, {"text":"French Curve","fr":""}, {"text":"مسطرة منحنيات لرسم الباترون","fr":""}],
        [{"text":"تقنية","fr":""}, {"text":"Interpolation","fr":""}, {"text":"تقنية توليد المقاسات الوسطى","fr":""}],
    ],
    caption_ar="الجدول 7: معجم مصطلحات التدريج الصناعي",
    caption_fr="Tableau 7: Glossaire des termes de gradation"
))

# ---------- Section 10: Exercises ----------
SECTIONS_HTML.append(section_header(10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas"))

SECTIONS_HTML.append(subsection("تمرين 1: حساب قيم التطور", "Exercice 1: Calcul des Valeurs d'Évolution"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> نريد تدريج تنورة من المقاس 38 إلى المقاس 42. الفرق بين المقاسين في محيط الخصر هو 4 سم، موزّع على 4 محاور (نقطتين أماميتين ونقطتين خلفيتين). احسب قيمة التطور على المحور X لكل نقطة.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p>حسب المعادلة <strong>V<sub>x</sub> = (Δ / n) × k</strong>: Δ = 4 سم، n = 4 محاور، k = 1 (توزيع متساوي).</p><p>V<sub>x</sub> = (4 / 4) × 1 = <strong>1.0 سم</strong> لكل نقطة على المحور X.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("تمرين 2: توزيع زمن التدريج حسب التعقيد", "Exercice 2: Temps de Gradation par Complexité"))

SECTIONS_HTML.append(bar_chart(
    title_ar="زمن التدريج اليدوي حسب نوع القطعة",
    title_fr="Temps de Gradation Manuelle par Type de Pièce",
    categories=[
        ("تنورة", "Jupe"),
        ("قميص", "Chemise"),
        ("بنطلون", "Pantalon"),
        ("سترة", "Veste"),
        ("معطف", "Manteau"),
    ],
    values=[60, 90, 120, 180, 240],
    unit=" د",
    caption_ar="الشكل 3: مقارنة زمن التدريج اليدوي (بالدقائق) حسب نوع القطعة",
    caption_fr="Figure 3: Comparaison du temps de gradation manuelle par type de pièce"
))

SECTIONS_HTML.append(subsection("تمرين 3: شبكة تقييم جودة التدريج", "Exercice 3: Grille d'Évaluation Qualité"))

SECTIONS_HTML.append(progress_chart(
    title_ar="شبكة تقييم جودة التدريج",
    title_fr="Grille d'Évaluation de la Qualité de Gradation",
    items=[
        ("دقة الحساب", "Précision calcul", 5, 5, "#0F4D3A"),
        ("دقة الرسم", "Précision tracé", 4, 5, "#1B6B52"),
        ("احترام النسب", "Respect proportions", 4, 5, "#C2932E"),
        ("نقاوة الخطوط", "Netteté lignes", 3, 5, "#7BA38A"),
        ("البيانات الفنية", "Données techniques", 5, 5, "#1B6B52"),
    ],
    caption_ar="الشكل 4: شبكة تقييم جودة التدريج — المجموع 21/25 (84%)",
    caption_fr="Figure 4: Grille d'évaluation — Total 21/25 (84%)"
))
