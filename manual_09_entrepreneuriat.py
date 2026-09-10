"""
Manual 9: المقاولاتية — Entrepreneuriat
Module 08 in the reference structure.
"""
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart
)

MANUAL_9 = {
    "module_num": "08",
    "module_num_label": "الوحدة التكوينية",
    "title_ar": "المقاولاتية — إنشاء مؤسسة نسيجية",
    "title_fr": "Entrepreneuriat — Création d'Entreprise Textile",
    "code": "HTE1204 / ENT",
    "toc_items": [
        (1, "مقدمة في المقاولاتية", "Introduction", 3),
        (2, "أجهزة الدعم الحكومي", "Dispositifs d'Accompagnement", 4),
        (3, "مراحل إنشاء مؤسسة مصغّرة", "Étapes de Création", 6),
        (4, "دراسة مشروع: ورشة تصميم أزياء", "Étude de Projet", 8),
        (5, "تحليل SWOT للمشروع", "Analyse SWOT", 10),
        (6, "الخطة الشاملة للأعمال (Business Plan)", "Business Plan", 11),
        (7, "التوقعات المالية و الموارد", "Projections Financières", 13),
        (8, "التسويق الرقمي للمصمم الجزائري", "Marketing Digital", 14),
        (9, "الخلاصة و المراجع", "Conclusion et Références", 15),
        (10, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue", 17),
        (11, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas", 19),
    ],
    "closing_ar": "المقاولاتية في قطاع النسيج الجزائري ليست مجرد خيار مهني، بل رسالة وطنية لإحياء الصناعة وتوفير فرص الشغل للشباب.",
    "closing_fr": "L'entrepreneuriat dans le secteur textile algérien n'est pas seulement un choix professionnel, mais une mission nationale pour relancer l'industrie et créer des emplois pour la jeunesse.",
}

SECTIONS_HTML = []

# Section 1
SECTIONS_HTML.append(section_header(1, "مقدمة في المقاولاتية", "Introduction"))

SECTIONS_HTML.append("""
<p>تُعرَّف <strong>المقاولاتية</strong> <span class="fr">(Entrepreneuriat)</span> بأنها القدرة على تحويل فكرة مشروع إلى مؤسسة اقتصادية قابلة للحياة، عبر تجميع الموارد البشرية والمادية والمالية اللازمة، وتحمل المخاطر المرتبطة بذلك. في السياق الجزائري المعاصر، تُمثّل المقاولاتية قطاعاً استراتيجياً وطنياً، حيث تُولي الدولة أهمية متزايدة لدعم الشباب الراغب في إنشاء مشاريعهم الخاصة، خاصة في القطاعات الإنتاجية كالنسيج والألبسة.</p>

<p>تُمثّل المقاولاتية في قطاع النسيج الجزائري فرصة استثنائية للمتخرّجين في تخصص التقني السامي في تصميم الملابس. فمن جهة، يشهد القطاع إحياءً ملحوظاً بدعم من السياسة الوطنية لتقليل الاستيراد. ومن جهة أخرى، يتمتع المتخرّجون بكفاءات تقنية عالية تُمكّنهم من إنتاج منتجات وطنية جاذبة. كما تُتيح المقاولاتية للمصمم الشاب التحكم في مشروعه، وتحقيق دخل يفوق ما يتقاضاه في الوظيفة العمومية، مع المساهمة في تطوير الاقتصاد الوطني.</p>

<p>تشير الإحصائيات الرسمية إلى أن القطاع النسيجي الجزائري يضم حالياً حوالي <strong>1200 مؤسسة</strong>، 90% منها مؤسسات صغيرة ومتوسطة. الهدف الاستراتيجي للوزارة هو رفع هذا العدد إلى <strong>2500 مؤسسة بحلول 2027</strong>، عبر تشجيع الشباب على إنشاء ورشات خاصة. هذا الهدف يخلق بيئة محفّزة للمتخرّجين، مع توفر برامج دعم مالي وتكويني وتوجيهي.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("1200+", "مؤسسة نسيجية حالية في الجزائر", "Entreprises textiles actuelles"),
    ("90%", "مؤسسات صغيرة ومتوسطة", "PME dans le secteur"),
    ("2500", "هدف 2027 للمؤسسات النسيجية", "Objectif 2027"),
    ("ANADE", "الوكالة الوطنية لدعم المقاولاتية", "Agence Nationale d'Appui"),
]))

# Section 2
SECTIONS_HTML.append(section_header(2, "أجهزة الدعم الحكومي", "Dispositifs d'Accompagnement"))

SECTIONS_HTML.append("""
<p>تُوفّر الدولة الجزائرية منظومة دعم متكاملة للمقاولين الشباب، تتمحور حول ثلاث جهات رئيسية: <strong>الوكالة الوطنية لدعم وتطوير المقاولاتية (ANADE)</strong>، <strong>الصندوق الوطني للتأمين عن البطالة (CNAC)</strong>، و<strong>بنك المؤسسات المصغّرة والحرفية (BEMC)</strong>. تُكمّل هذه الجهات عمل بعضها البعض: ANADE توفّر التكوين والتوجيه، CNAC توفّر التمويل عبر منحة، BEMC يوفّر القروض المصرفية بأسعار مدعّمة.</p>
""")

SECTIONS_HTML.append(data_table(
    [("الجهاز", "Organisme"), ("نوع الدعم", "Type de Soutien"), ("الحد الأقصى", "Plafond")],
    [
        [{"text":"ANADE","fr":""}, {"text":"تكوين، توجيه، مرافقة تقنية","fr":""}, {"text":"مجاني","fr":""}],
        [{"text":"CNAC","fr":""}, {"text":"تمويل عبر منحة (لا تُسترجع)","fr":""}, {"text":"1,000,000 دج","type":"num"}],
        [{"text":"BEMC","fr":""}, {"text":"قرض مصغّر بفائدة مدعّمة","fr":""}, {"text":"10,000,000 دج","type":"num"}],
        [{"text":"FGAR","fr":""}, {"text":"صندوق ضمان القروض","fr":""}, {"text":"85% من القرض","type":"num"}],
        [{"text":"ALGEX","fr":""}, {"text":"دعم التصدير للأسواق الخارجية","fr":""}, {"text":"حسب المشروع","fr":""}],
        [{"text":"CNPTC","fr":""}, {"text":"تكوين مهني مستمر","fr":""}, {"text":"مجاني","fr":""}],
    ],
    caption_ar="الجدول 1: أجهزة الدعم الحكومي للمقاولاتية في الجزائر",
    caption_fr="Tableau 1: Dispositifs gouvernementaux d'appui à l'entrepreneuriat en Algérie"
))

SECTIONS_HTML.append(callout(
    "قاعدة ذهبية: شروط الاستفادة من دعم CNAC",
    "<p>للاستفادة من منحة <strong>CNAC</strong> (1,000,000 دج)، يجب: (1) أن يكون المترشح عمره بين 19 و 35 سنة، (2) حاصل على شهادة مهنية على الأقل، (3) دون نشاط مهني سابق، (4) يلتزم بإنشاء مشروع يخلق فرص شغل. يُضاف إلى المنحة قرض بفائدة مدعّمة من BEMC بحد أقصى 10,000,000 دج. المشروع يجب أن يكون في قطاع مُحفّز (النسيج من بينها).</p>",
    variant="ochre", icon="★"
))

# Section 3
SECTIONS_HTML.append(section_header(3, "مراحل إنشاء مؤسسة مصغّرة", "Étapes de Création"))

SECTIONS_HTML.append("""
<p>إنشاء مؤسسة مصغّرة في الجزائر يمرّ بمراحل إدارية وفنية محددة، تتطلب صبراً وتنظيماً. تختلف المراحل قليلاً بحسب نوع المؤسسة (مؤسسة فردية، شركة ذات مسؤولية محدودة SARL، إلخ)، لكن المراحل الأساسية تظل موحّدة. تُقدّم ANADE مرافقة مجانية عبر كل المراحل لضمان نجاح المشروع.</p>
""")

SECTIONS_HTML.append(flowchart([
    ("1", "تقديم فكرة المشروع وتسجيلها لدى ANADE عبر منصة الإيداع الإلكتروني", "Dépôt de l'idée"),
    ("2", "حضور التكوين الإجباري لمدة 5 أيام في مقر ANADE الجهوي", "Formation obligatoire"),
    ("3", "إعداد دراسة الجدوى والمخطط المالي بالتعاون مع مستشار ANADE", "Étude de faisabilité"),
    ("4", "إيداع ملف طلب التمويل لدى CNAC أو BEMC مع كل الوثائق المطلوبة", "Dépôt du dossier de financement"),
    ("5", "انتظار دراسة الملف من اللجنة الفنية (60 يوم عمل عادة)", "Étude du dossier"),
    ("6", "الحصول على الموافقة وتوقيع عقد التمويل", "Approbation et signature"),
    ("7", "التسجيل في السجل التجاري (CNRC) والحصول على الرقم الجبائي", "Inscription au RC"),
    ("8", "فتح حساب بنكي باسم المؤسسة وإيداع رأس المال", "Ouverture de compte"),
    ("9", "البدء في النشاط الفعلي وتقديم التقارير الدورية للجهات الممولة", "Démarrage de l'activité"),
]))

# Section 4
SECTIONS_HTML.append(section_header(4, "دراسة مشروع: ورشة تصميم أزياء", "Étude de Projet"))

SECTIONS_HTML.append("""
<p>نقدم في هذا القسم دراسة حالة لمشروع مقترح: <strong>إنشاء ورشة تصميم و تصنيع أزياء نسائية راقية</strong>، يستهدف السوق الجزائري للقفطان العصري وأزياء السهرة. اختير هذا المشروع لأنه يستفيد من الكفاءات التقنية للمتخرّج، ويستجيب لطلب وطني متزايد، ويُمثّل قيمة مضافة ثقافية واقتصادية.</p>
""")

SECTIONS_HTML.append(subsection("بطاقة تعريف المشروع", "Fiche d'Identité du Projet"))

SECTIONS_HTML.append(data_table(
    [("البند", "Élément"), ("المواصفة", "Spécification")],
    [
        [{"text":"اسم المشروع","fr":""}, {"text":"ورشة «وائل كوتور» للقفطان العصري","fr":""}],
        [{"text":"الموقع","fr":""}, {"text":"الجزائر العاصمة — حي الأبيار","fr":""}],
        [{"text":"المساحة المطلوبة","fr":""}, {"text":"80 م² (ورشة + صالة عرض)","type":"num"}],
        [{"text":"عدد العمال","fr":""}, {"text":"3 (المصمم + خياطتان + مساعد)","type":"num"}],
        [{"text":"المنتج الرئيسي","fr":""}, {"text":"قفطان عصري، فستان سهرة، كاراكو","fr":""}],
        [{"text":"السوق المستهدف","fr":""}, {"text":"نساء الجزائر العاصمة، الطبقة المتوسطة والعليا","fr":""}],
        [{"text":"السعر المتوقع للقطعة","fr":""}, {"text":"25,000 — 80,000 دج","type":"num"}],
        [{"text":"الإنتاج الشهري المستهدف","fr":""}, {"text":"20 قطعة في السنة الأولى","type":"num"}],
    ],
    caption_ar="الجدول 2: بطاقة تعريف مشروع ورشة تصميم أزياء نسائية",
    caption_fr="Tableau 2: Fiche d'identité du projet d'atelier de couture"
))

# Section 5
SECTIONS_HTML.append(section_header(5, "تحليل SWOT للمشروع", "Analyse SWOT"))

SECTIONS_HTML.append("""
<p>تحليل <strong>SWOT</strong> أداة استراتيجية تُمكّن المقاول من تقييم مشروعه من أربعة جوانب: <strong>النقاط القوة</strong> <span class="fr">(Strengths)</span>، <strong>النقاط الضعف</strong> <span class="fr">(Weaknesses)</span>، <strong>الفرص</strong> <span class="fr">(Opportunities)</span>، و<strong>التهديدات</strong> <span class="fr">(Threats)</span>. هذا التحليل يُساعد على بناء استراتيجية واقعية تستثمر النقاط القوة، تعالج النقاط الضعف، تستغل الفرص، وتتحسّب للتهديدات.</p>
""")

SECTIONS_HTML.append(data_table(
    [("العنصر", "Élément"), ("المحتوى", "Contenu")],
    [
        [{"text":"النقاط القوة (S)","fr":"Forces"}, {"text":"كفاءة تقنية عالية للمصمم، معرفة بالتراث الجزائري، تكلفة إنتاج منخفضة، مرونة في الإنتاج","fr":""}],
        [{"text":"النقاط الضعف (W)","fr":"Faiblesses"}, {"text":"عدم وجود قاعدة زبائن في البداية، رأس مال محدود، عدم وجود علامة تجارية معروفة","fr":""}],
        [{"text":"الفرص (O)","fr":"Opportunités"}, {"text":"نمو سوق الأزياء الراقية الجزائرية، إقبال متزايد على القفطان العصري، دعم حكومي للمقاولاتية، إمكانية التصدير","fr":""}],
        [{"text":"التهديدات (T)","fr":"Menaces"}, {"text":"منافسة مصممين معروفين، استيراد أزياء مغربية، تقلبات الأسعار، صعوبة الحصول على خامات نوعية","fr":""}],
    ],
    caption_ar="الجدول 3: تحليل SWOT لمشروع ورشة تصميم أزياء نسائية",
    caption_fr="Tableau 3: Analyse SWOT du projet d'atelier de couture"
))

# Section 6
SECTIONS_HTML.append(section_header(6, "الخطة الشاملة للأعمال (Business Plan)", "Business Plan"))

SECTIONS_HTML.append("""
<p>تُعدّ <strong>الخطة الشاملة للأعمال</strong> <span class="fr">(Business Plan)</span> الوثيقة المرجعية للمشروع، تُلخّص كل جوانبه: الفكرة، السوق، المنتج، التمويل، التوقعات، الفريق. تُستعمل الخطة لإقناع الممولين (بنوك، صندوق ضمان) بجدوى المشروع، وللأخذ منها مرجعاً للتسيير اليومي. كلما كانت الخطة دقيقة وشاملة، كلما زادت فرص الحصول على التمويل ونجاح المشروع.</p>
""")

SECTIONS_HTML.append(subsection("هيكل الخطة الشاملة", "Structure du Business Plan"))

SECTIONS_HTML.append(data_table(
    [("القسم", "Section"), ("المحتوى", "Contenu")],
    [
        [{"text":"1. الملخّص التنفيذي","fr":"Résumé exécutif"}, {"text":"نظرة شاملة في صفحة واحدة: الفكرة، السوق، التمويل المطلوب، العائد المتوقع","fr":""}],
        [{"text":"2. تقديم المشروع","fr":"Présentation du projet"}, {"text":"وصف المنتج/الخدمة، الرؤية، الرسالة، الأهداف","fr":""}],
        [{"text":"3. تحليل السوق","fr":"Analyse du marché"}, {"text":"حجم السوق، الزبائن المستهدفون، المنافسون، الاتجاهات","fr":""}],
        [{"text":"4. الاستراتيجية التجارية","fr":"Stratégie commerciale"}, {"text":"المنتج، السعر، التوزيع، الترويج (4Ps)","fr":""}],
        [{"text":"5. الفريق","fr":"Équipe"}, {"text":"المؤسسون، الكفاءات، المهام، نقاط القوة","fr":""}],
        [{"text":"6. التمويل","fr":"Financement"}, {"text":"الاحتياجات، مصادر التمويل، شروط الاسترجاع","fr":""}],
        [{"text":"7. التوقعات المالية","fr":"Projections financières"}, {"text":"ميزانية 3 سنوات، حساب النتائج، التدفقات النقدية","fr":""}],
        [{"text":"8. تحليل المخاطر","fr":"Analyse des risques"}, {"text":"المخاطر المحتملة، طرق معالجتها، خطة بديلة","fr":""}],
    ],
    caption_ar="الجدول 4: الهيكل المعياري للخطة الشاملة للأعمال (8 أقسام)",
    caption_fr="Tableau 4: Structure standard du Business Plan (8 sections)"
))

# Section 7
SECTIONS_HTML.append(section_header(7, "التوقعات المالية و الموارد", "Projections Financières"))

SECTIONS_HTML.append("""
<p>تُعدّ <strong>التوقعات المالية</strong> الجانب الأكثر حساسية في الخطة، إذ تُترجم كل الافتراضات إلى أرقام. يجب أن تكون التوقعات واقعية، مبنية على معطيات فعلية لا على أمنيات. تُعدّ لمدة 3 سنوات على الأقل، مع تحديد نقطة التعادل <span class="fr">(Seuil de rentabilité)</span> أي اللحظة التي يبدأ المشروع فيها تحقيق أرباح.</p>
""")

SECTIONS_HTML.append(subsection("التوقعات المالية لورشة تصميم أزياء (السنة الأولى)", "Projections Financières — Atelier Couture"))

SECTIONS_HTML.append(data_table(
    [("البند", "Poste"), ("المبلغ (دج)", "Montant (DZD)"), ("ملاحظة", "Note")],
    [
        [{"text":"الاستثمار الأولي","fr":"Investissement initial"}, {"text":"3,500,000","type":"num"}, {"text":"تجهيزات + تجهيزات الورشة","fr":""}],
        [{"text":"رأس المال العامل","fr":"Fonds de roulement"}, {"text":"1,500,000","type":"num"}, {"text":"3 أشهر من المصاريف","fr":""}],
        [{"text":"إجمالي الاستثمار","fr":"Total investissement"}, {"text":"5,000,000","type":"num"}, {"text":"—","fr":""}],
        [{"text":"التمويل المطلوب","fr":"Financement requis"}, {"text":"5,000,000","type":"num"}, {"text":"1M CNAC + 4M BEMC","fr":""}],
        [{"text":"الإيرادات السنة 1","fr":"Chiffre d'affaires Y1"}, {"text":"8,000,000","type":"num"}, {"text":"20 قطعة × 40,000 دج","fr":""}],
        [{"text":"المصاريف السنة 1","fr":"Charges Y1"}, {"text":"6,500,000","type":"num"}, {"text":"خامات + رواتب + مصاريف","fr":""}],
        [{"text":"الربح الصافي السنة 1","fr":"Bénéfice net Y1"}, {"text":"1,500,000","type":"num"}, {"text":"19% من الإيرادات","fr":""}],
        [{"text":"نقطة التعادل","fr":"Seuil de rentabilité"}, {"text":"الشهر 14","type":"num"}, {"text":"بعد سنة و شهرين","fr":""}],
    ],
    caption_ar="الجدول 5: التوقعات المالية لورشة تصميم أزياء — السنة الأولى",
    caption_fr="Tableau 5: Projections financières de l'atelier de couture — Année 1"
))

SECTIONS_HTML.append(bar_chart(
    title_ar="التوقعات المالية لورشة تصميم الأزياء (3 سنوات)",
    title_fr="Projections Financières Atelier Couture (3 ans)",
    categories=[
        ("الإيرادات", "Chiffre affaires"),
        ("المصاريف", "Charges"),
        ("الربح الصافي", "Bénéfice net"),
    ],
    values=[8000, 6500, 1500],
    unit=" كدج",
    caption_ar="الشكل 1: التوقعات المالية للسنة الأولى (بآلاف الدج) — ربح 19% من الإيرادات",
    caption_fr="Figure 1: Projections financières année 1 (en milliers DZD) — bénéfice 19%"
))

# Section 8
SECTIONS_HTML.append(section_header(8, "التسويق الرقمي للمصمم الجزائري", "Marketing Digital"))

SECTIONS_HTML.append("""
<p>يُعدّ <strong>التسويق الرقمي</strong> <span class="fr">(Marketing Digital)</span> أداة لا غنى عنها للمصمم الجزائري المعاصر. مع انتشار الإنترنت في الجزائر (أكثر من 27 مليون مستخدم)، أصبح التواجد الرقمي ضرورة لكل مقاولة، خاصة في قطاع الأزياء الذي يعتمد على الصورة البصرية. تُتيح منصات التواصل الاجتماعي لل مصمم الجزائري الوصول إلى زبائن محليين ودوليين بتكلفة منخفضة جداً مقارنة بالإعلان التقليدي.</p>
""")

SECTIONS_HTML.append(subsection("قنوات التسويق الرقمي الأساسية", "Canaux de Marketing Digital"))

SECTIONS_HTML.append(data_table(
    [("القناة", "Canal"), ("الجمهور المستهدف", "Public Cible"), ("التكلفة الشهرية", "Coût Mensuel")],
    [
        [{"text":"Instagram","fr":""}, {"text":"نساء 25-45 سنة","fr":""}, {"text":"5,000 — 20,000 دج","type":"num"}],
        [{"text":"Facebook","fr":""}, {"text":"مختلط، 30+ سنة","fr":""}, {"text":"3,000 — 15,000 دج","type":"num"}],
        [{"text":"TikTok","fr":""}, {"text":"شباب 18-30 سنة","fr":""}, {"text":"2,000 — 10,000 دج","type":"num"}],
        [{"text":"Pinterest","fr":""}, {"text":"مهتمون بالموضة","fr":""}, {"text":"1,000 — 5,000 دج","type":"num"}],
        [{"text":"موقع إلكتروني","fr":""}, {"text":"زبائن جدّيون","fr":""}, {"text":"15,000 — 50,000 دج","type":"num"}],
        [{"text":"YouTube","fr":""}, {"text":"جمهور واسع","fr":""}, {"text":"10,000 — 30,000 دج","type":"num"}],
    ],
    caption_ar="الجدول 6: قنوات التسويق الرقمي الأساسية وتكاليفها التقديرية",
    caption_fr="Tableau 6: Canaux de marketing digital et coûts estimatifs"
))

SECTIONS_HTML.append(pie_chart(
    title_ar="توزيع الميزانية التسويقية الرقمية",
    title_fr="Répartition du Budget Marketing Digital",
    segments=[
        ("Instagram", "Instagram", 35, "#0F4D3A"),
        ("Facebook", "Facebook", 25, "#1B6B52"),
        ("TikTok", "TikTok", 15, "#C2932E"),
        ("موقع إلكتروني", "Site web", 15, "#7BA38A"),
        ("Pinterest", "Pinterest", 5, "#D4B36A"),
        ("YouTube", "YouTube", 5, "#9CA3AF"),
    ],
    center_value="100%",
    center_label="الميزانية",
    caption_ar="الشكل 2: التوزيع المثالي لميزانية التسويق الرقمي لمصمم أزياء جزائري",
    caption_fr="Figure 2: Répartition idéale du budget marketing digital"
))

SECTIONS_HTML.append(callout(
    "استراتيجية المحتوى البصري",
    "<p>في قطاع الأزياء، <strong>المحتوى البصري هو الملك</strong>. يجب على المصمم الجزائري الاستثمار في تصوير احترافي لمنتجاته، نشر صور يومية على Instagram، إنتاج فيديوهات قصيرة على TikTok تُظهر مراحل التصميم. الهدف بناء علامة تجارية بصريّة مميّزة، تكسب ثقة الزبون قبل أن يطلب الشراء. الزبون الذي يرى المنتج بشكل احترافي أكثر استعداداً للدفع بسعر أعلى.</p>",
    variant="ochre", icon="★"
))

# Section 9
SECTIONS_HTML.append(section_header(9, "الخلاصة و المراجع", "Conclusion et Références"))

SECTIONS_HTML.append("""
<p>تُمثّل المقاولاتية في قطاع النسيج الجزائري فرصة استثنائية للمتخرّجين في تخصص التقني السامي في تصميم الملابس. تجمع هذه الفرصة بين تحقيق الذات المهنية، والمساهمة في إحياء الصناعة الوطنية، وخلق فرص شغل للآخرين. مع الدعم الحكومي المتوفّر (ANADE، CNAC، BEMC) والكفاءات التقنية المكتسبة في المعهد، يصبح إنشاء مشروع خاص في المتناول أكثر من أي وقت مضى.</p>

<p>النجاح في المقاولاتية لا يأتي من الفكرة وحدها، بل من التخطيط الدقيق، التنفيذ المنضبط، والقدرة على التكيّف مع متغيرات السوق. المتخرّج الذي يتقن إعداد خطة أعمال واقعية، يفهم سوقه المستهدف، يستعمل أدوات التسويق الرقمي بذكاء، ويتعلّم من تجاربه، لديه فرص حقيقية لبناء مؤسسة ناجحة ومستدامة. المستقبل ينتمي للمقادين الذين لا يخافون من المخاطر، بل يتحلّمونها بذكاء.</p>
""")

SECTIONS_HTML.append(subsection("نصائح للمقاول الشاب", "Conseils au Jeune Entrepreneur"))
SECTIONS_HTML.append("""
<ul>
<li><strong>ابدأ صغيراً ثم توسّع:</strong> لا تبدأ بمشروع ضخم يفوق طاقتك. ابدأ بورشة صغيرة، أتقن عملك، ابحث عن زبائنك الأوائل، ثم وسّع تدريجياً.</li>
<li><strong>الجودة قبل الكمية:</strong> إنتاج قطعة عالية الجودة أفضل من إنتاج 10 قطع متوسطة. السمعة الجيدة تبنى ببطء لكنها تدوم، بينما السمعة السيئة تنتشر بسرعة وتدمر المشروع.</li>
<li><strong>استثمر في التسويق:</strong> لا يعني إنتاج منتج جيد أن الزبائن سيأتون تلقائياً. خصّص 10-15% من ميزانيتك للتسويق، خاصة الرقمي.</li>
<li><strong>تعاون مع مقاولين آخرين:</strong> لا تعمل بمعزل. تعاون مع مصممين آخرين، مع موردين موثوقين، مع مقاولين في قطاعات مكمّلة (تصوير، تسويق).</li>
<li><strong>تعلّم باستمرار:</strong> سوق الأزياء يتغير بسرعة. اتبع دورات تكوينية مستمرة، احضر المعارض، اقرأ المجلات المتخصصة.</li>
<li><strong>حافظ على التوازن:</strong> المقاولاتية تتطلب جهداً كبيراً، لكن لا تهمل صحتك وعائلتك. المشروع الناجح هو الذي يخدم حياتك لا الذي يدمّرها.</li>
</ul>
""")

SECTIONS_HTML.append(quote_block(
    "المقاول الناجح ليس من لديه فكرة عظيمة، بل من ينفّذ فكرة صغيرة بكفاءة عالية. الفرق بين الحلم والإنجاز هو العمل المنظّم.",
    "ANADE — Manuel du Jeune Entrepreneur"
))

SECTIONS_HTML.append(subsection("المراجع", "Références Bibliographiques"))
SECTIONS_HTML.append("""
<ol>
<li>الوكالة الوطنية لدعم وتطوير المقاولاتية (ANADE)، دليل المقاول الشاب، الطبعة 2024، الجزائر.</li>
<li>الصندوق الوطني للتأمين عن البطالة (CNAC)، دليل الاستفادة من جهاة المساعدة على الإدماج المهني، الجزائر، 2023.</li>
<li>وزارة الصناعة الجزائرية، تقرير قطاع النسيج والألبسة 2023، الجزائر، 2024.</li>
<li>Pinson, C., Business Plans for Dummies, 4th Edition, Wiley, New York, 2021.</li>
<li>Osterwalder, A., Business Model Generation, Wiley, London, 2020.</li>
<li>Kotler, P., Marketing 4.0: Moving from Traditional to Digital, Wiley, New Jersey, 2021.</li>
<li>الجمهورية الجزائرية، القانون رقم 18-15 المتعلق بالمؤسسات المصغّرة، الجريدة الرسمية، الجزائر، 2018.</li>
</ol>
""")

# ---------- Section 10: Glossary ----------
SECTIONS_HTML.append(section_header(10, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue"))

SECTIONS_HTML.append("""
<p>يُقدّم هذا المعجم المصطلحات التقنية والاقتصادية الأساسية المستعملة في وحدة المقاولاتية، مزدوج اللغة (عربي/فرنسي). تشمل المصطلحات المفاتيح في إنشاء المؤسسات، التمويل، والتسويق الرقمي.</p>
""")

SECTIONS_HTML.append(data_table(
    [("المصطلح العربي", "Terme Arabe"), ("المصطلح الفرنسي", "Terme Français"), ("التعريف المختصر", "Définition Courte")],
    [
        [{"text":"مقاولاتية","fr":""}, {"text":"Entrepreneuriat","fr":""}, {"text":"إنشاء مؤسسة اقتصادية","fr":""}],
        [{"text":"مقاول","fr":""}, {"text":"Entrepreneur","fr":""}, {"text":"صاحب المشروع","fr":""}],
        [{"text":"خطة أعمال","fr":""}, {"text":"Business Plan","fr":""}, {"text":"وثيقة شاملة للمشروع","fr":""}],
        [{"text":"دراسة جدوى","fr":""}, {"text":"Étude de Faisabilité","fr":""}, {"text":"تحليل قابلية المشروع","fr":""}],
        [{"text":"تحليل SWOT","fr":""}, {"text":"Analyse SWOT","fr":""}, {"text":"تحليل النقاط القوة والضعف","fr":""}],
        [{"text":"تكلفة تقديرية","fr":""}, {"text":"Prix de Revient","fr":""}, {"text":"التكلفة الكاملة للمنتج","fr":""}],
        [{"text":"نقطة التعادل","fr":""}, {"text":"Seuil de Rentabilité","fr":""}, {"text":"لحظة تحقيق الأرباح","fr":""}],
        [{"text":"ANADE","fr":""}, {"text":"ANADE","fr":""}, {"text":"الوكالة الوطنية لدعم المقاولاتية","fr":""}],
        [{"text":"CNAC","fr":""}, {"text":"CNAC","fr":""}, {"text":"الصندوق الوطني للتأمين عن البطالة","fr":""}],
        [{"text":"BEMC","fr":""}, {"text":"BEMC","fr":""}, {"text":"بنك المؤسسات المصغّرة","fr":""}],
        [{"text":"تسويق رقمي","fr":""}, {"text":"Marketing Digital","fr":""}, {"text":"تسويق عبر الإنترنت","fr":""}],
        [{"text":"سوق مستهدف","fr":""}, {"text":"Marché Cible","fr":""}, {"text":"الجمهور المستهدف للمنتج","fr":""}],
    ],
    caption_ar="الجدول 7: معجم مصطلحات المقاولاتية",
    caption_fr="Tableau 7: Glossaire des termes d'entrepreneuriat"
))

# ---------- Section 11: Exercises ----------
SECTIONS_HTML.append(section_header(11, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas"))

SECTIONS_HTML.append(subsection("تمرين 1: حساب نقطة التعادل", "Exercice 1: Calcul du Seuil de Rentabilité"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> ورشة خياطة تبيع القطعة بـ 5000 دج. التكلفة المتغيرة للقطعة 3000 دج. التكاليف الثابتة الشهرية 200,000 دج. احسب نقطة التعادل (عدد القطعات الشهرية).</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p><strong>هامش المساهمة للقطعة = سعر البيع - التكلفة المتغيرة = 5000 - 3000 = 2000 دج</strong>.</p><p><strong>نقطة التعادل = التكاليف الثابتة ÷ هامش المساهمة = 200,000 ÷ 2000 = 100 قطعة شهرياً</strong>.</p><p>هذا يعني أن الورشة تبدأ في تحقيق ربح بعد بيع القطعة 101 شهرياً.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("تمرين 2: توقعات الإيرادات لـ 3 سنوات", "Exercice 2: Projections sur 3 ans"))

SECTIONS_HTML.append(line_chart(
    title_ar="توقعات الإيرادات والأرباح (3 سنوات)",
    title_fr="Projections de Revenus et Bénéfices (3 ans)",
    x_labels=["سنة 1", "سنة 2", "سنة 3"],
    series=[
        ("الإيرادات", "Chiffre d'affaires", [8000, 12000, 18000], "#1B6B52"),
        ("المصاريف", "Charges", [6500, 9000, 13000], "#C2932E"),
        ("الربح الصافي", "Bénéfice net", [1500, 3000, 5000], "#0F4D3A"),
    ],
    y_unit=" كدج",
    caption_ar="الشكل 3: توقعات الإيرادات والأرباح لورشة تصميم أزياء (بآلاف الدج)",
    caption_fr="Figure 3: Projections de revenus et bénéfices (en milliers DZD)"
))

SECTIONS_HTML.append(subsection("تمرين 3: تحليل SWOT لمشروع ورشة", "Exercice 3: Analyse SWOT"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> أجرِ تحليل SWOT لمشروع ورشة خياطة نسائية في مدينة وهران، مع ذكر عنصرين على الأقل لكل بند.</p>
""")

SECTIONS_HTML.append(data_table(
    [("البند", "Élément"), ("المحتوى", "Contenu")],
    [
        [{"text":"نقاط القوة (S)","fr":"Forces"}, {"text":"كفاءة تقنية عالية، معرفة بالتراث الجزائري","fr":""}],
        [{"text":"نقاط الضعف (W)","fr":"Faiblesses"}, {"text":"رأس مال محدود، عدم وجود قاعدة زبائن في البداية","fr":""}],
        [{"text":"الفرص (O)","fr":"Opportunités"}, {"text":"سوق وهران الواسع، إقبال على القفطان العصري، دعم ANADE","fr":""}],
        [{"text":"التهديدات (T)","fr":"Menaces"}, {"text":"منافسة مصممين معروفين، استيراد أزياء مغربية","fr":""}],
    ],
    caption_ar="الجدول 8: تحليل SWOT لمشروع ورشة خياطة في وهران",
    caption_fr="Tableau 8: Analyse SWOT d'un projet d'atelier à Oran"
))
