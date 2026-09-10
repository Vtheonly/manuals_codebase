"""
Manual 5: التنظيم العلمي للعمل — OST (Organisation Scientifique du Travail)
Module 04 in the reference structure.
"""
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart
)

MANUAL_5 = {
    "module_num": "04",
    "module_num_label": "الوحدة التكوينية",
    "title_ar": "التنظيم العلمي للعمل — OST",
    "title_fr": "Organisation Scientifique du Travail (OST)",
    "code": "HTE1204 / OST",
    "toc_items": [
        (1, "مقدمة في التنظيم العلمي للعمل", "Introduction à l'OST", 3),
        (2, "الإطار النظري: من تايلور إلى لوريت", "Cadre Théorique", 4),
        (3, "دراسة الحركات و الأزمنة (Chronométrage)", "Étude des Mouvements", 6),
        (4, "موازنة خطوط الإنتاج (Équilibrage)", "Équilibrage des Lignes", 8),
        (5, "دراسة حالة: ورشة الرويبة", "Étude de Cas: Rouiba", 10),
        (6, "النتائج و مؤشرات الأداء (KPIs)", "Résultats et KPIs", 12),
        (7, "الإرغونوميا و ظروف العمل", "Ergonomie", 13),
        (8, "الخلاصة و المراجع", "Conclusion et Références", 15),
        (9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue", 17),
        (10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas", 19),
    ],
    "closing_ar": "لا يمكن للورشات الجزائرية المنافسة عالمياً ومحلياً دون الاعتماد على دراسات دقيقة للتنظيم العلمي للعمل — فما لا يمكن قياسه لا يمكن تحسينه.",
    "closing_fr": "Les ateliers algériens ne peuvent rivaliser sans s'appuyer sur l'OST — ce qui ne se mesure pas ne peut s'améliorer.",
}

SECTIONS_HTML = []

# Section 1
SECTIONS_HTML.append(section_header(1, "مقدمة في التنظيم العلمي للعمل", "Introduction à l'OST"))

SECTIONS_HTML.append("""
<p>يُعرَّف <strong>التنظيم العلمي للعمل</strong> <span class="fr">(Organisation Scientifique du Travail — OST)</span> بأنّه علم الإدارة والترشيد الصناعي، الذي يهدف إلى تعظيم الإنتاجية وتقليل التكاليف وزيادة كفاءة العمّال والآلات، من خلال دراسة الحركات وتقدير الأوقات القياسية لكل عملية إنتاجية في صناعة الملابس.</p>

<p>نشأ هذا العلم في مطلع القرن العشرين على يد المهندس الأمريكي <strong>فريدريك تايلور</strong> <span class="fr">(Frederick W. Taylor, 1856-1915)</span> الذي طوّر مبادئه في كتابه الشهير «مبادئ الإدارة العلمية» <span class="fr">(Principles of Scientific Management, 1911)</span>، ثم طوّرها لاحقاً <strong>فرانك وليليان جيلبريث</strong> <span class="fr">(Frank & Lillian Gilbreth)</span> عبر دراسة الحركات الدقيقة، و<strong>هنري جانت</strong> <span class="fr">(Henry Gantt)</span> عبر المخططات الزمنية للإنتاج.</p>

<p>تكتسب هذه الوحدة أهمية قصوى في صناعة الألبسة الجزائرية، لأن المؤسسات الوطنية تعاني من ضعف الإنتاجية مقارنة بالمنافسين الأجانب (تركيا، الصين، بنغلاديش). تشير دراسات قطاعية إلى أن إنتاجية العامل الجزائري في قطاع النسيج لا تتجاوز <strong>60%</strong> من نظيره التركي، وهو فارق يُفسَّر أساساً بضعف تطبيق مبادئ الـ <span class="fr">OST</span>. هذا الفارق يُكلّف الاقتصاد الوطني مئات الملايين من الدولارات سنوياً، ويُهدّد قدرة المؤسسات المحلية على المنافسة في ظل انفتاح السوق الجزائرية على المنتجات المستوردة.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("5-4", "قطعة/عامل/ساعة في المؤسسات العمومية", "Pièces/ouvrier/heure — EPE"),
    ("8-12", "قطعة/عامل/ساعة في المؤسسات التركية", "Pièces/ouvrier/heure — Turquie"),
    ("60%", "نسبة إنتاجية العامل الجزائري", "Productivité relative"),
    ("百万$", "خسائر سنوية للقطاع النسيجي", "Pertes annuelles du secteur"),
]))

# Section 2
SECTIONS_HTML.append(section_header(2, "الإطار النظري: من تايلور إلى لوريت", "Cadre Théorique"))

SECTIONS_HTML.append("""
<p>تطوّرت مبادئ التنظيم العلمي للعمل منذ نشأتها على يد تايلور حتى وصلت إلى صيغتها المعاصرة على يد المهندس الفرنسي لوريت <span class="fr">(Leroy)</span> الذي طوّر نظام مكتب الأزمنة الأولية <span class="fr">(Bureau des Temps Élémentaires — BTE)</span>. تتمحور المبادئ الأربعة الكبرى للـ <span class="fr">OST</span> حول استبداد الطرق التجريبية بطرق علمية مدروسة، وتقسيم العمل وتدريب العمّال، وتوحيد أدوات العمل، والفصل بين التخطيط والتنفيذ.</p>
""")

SECTIONS_HTML.append(subsection("المبادئ الأربعة لتايلور المُحدّثة", "Les Quatre Principes de Taylor"))

SECTIONS_HTML.append(data_table(
    [("#", "N°"), ("المبدأ", "Principe"), ("التطبيق في صناعة الألبسة", "Application dans l'Habillement")],
    [
        [{"text":"1","type":"num"}, {"text":"استبدال الطرق التجريبية بطرق علمية مدروسة","fr":""}, {"text":"تحليل كل عملية خياطة وتحديد الحركات الأكثر كفاءة","fr":""}],
        [{"text":"2","type":"num"}, {"text":"اختيار العامل المناسب لكل عملية وتدريبه علمياً","fr":""}, {"text":"إسناد عمليات الياقات للعمال الأكثر مهارة","fr":""}],
        [{"text":"3","type":"num"}, {"text":"تقسيم العمل والمسؤوليات بوضوح","fr":""}, {"text":"فصل مهام القص عن الخياطة عن التشطيبات","fr":""}],
        [{"text":"4","type":"num"}, {"text":"التعاون الودي بين الإدارة والعمّال","fr":""}, {"text":"إشراك العمّال في تحسين العمليات وتقديم اقتراحات","fr":""}],
    ],
    caption_ar="الجدول 1: المبادئ الأربعة للتنظيم العلمي للعمل المُحدّثة وفق Leroy/BTE",
    caption_fr="Tableau 1: Les quatre principes de l'OST selon Leroy/BTE"
))

SECTIONS_HTML.append(callout(
    "مكتب الأزمنة الأولية (BTE)",
    "<p>طوّر <strong>لوريت</strong> نظام <span class=\"fr\">Bureau des Temps Élémentaires (BTE)</span> المعتمد على التقييم الحركي ومعاملات الراحة. يُقدّم هذا النظام جداول مرجعية لزمن كل حركة أساسية في صناعة الألبسة، تُمكّن من حساب الزمن القياسي لأي عملية دون الحاجة لقياسها مباشرة، عبر تجميع الأزمنة الأولية للحركات المكوّنة لها.</p>",
    variant="emerald", icon="✓"
))

# Section 3
SECTIONS_HTML.append(section_header(3, "دراسة الحركات و الأزمنة (Chronométrage)", "Étude des Mouvements"))

SECTIONS_HTML.append("""
<p>تتألف دراسة الحركات والأزمنة من شقّين متلازمين: <strong>تحليل الحركة</strong> (ما يفعله العامل؟) و<strong>قياس الزمن</strong> (كم يستغرق ذلك؟). يُمثّل الشقان معاً القاعدة العلمية لأي تحسين في الإنتاجية، إذ لا يمكن تحسين ما لا يُقاس. تنتهج دراسة الحركات إلى تحليل الحركات الفيزيائية التي يقوم بها عامل الخياطة، بهدف القضاء على الحركات المجدية غير الضرورية مثل البحث عن المقص، التالية القطعة، أو الالتفات غير الضروري.</p>
""")

SECTIONS_HTML.append(subsection("تصنيف الحركات الثلاث وفق جيلبريث", "Classification des Trois Mouvements"))

SECTIONS_HTML.append(data_table(
    [("النوع", "Type"), ("الوصف", "Description"), ("الزمن (ثانية)", "Temps (s)"), ("التوصية", "Recommandation")],
    [
        [{"text":"حركة فعّالة","fr":"Mouvement efficace"}, {"text":"تُسهم في إنجاز العمل (مثل: قص القماش)","fr":""}, {"text":"1-3","type":"num"}, {"text":"يجب تطويرها وتحسينها","fr":""}],
        [{"text":"حركة مساعدة","fr":"Mouvement auxiliaire"}, {"text":"تُكمّل الحركة الفعّالة (مثل: إمساك القطعة)","fr":""}, {"text":"0.5-1","type":"num"}, {"text":"يجب تقليلها قدر الإمكان","fr":""}],
        [{"text":"حركة ضائعة","fr":"Mouvement perdu"}, {"text":"لا تُسهم في الإنجاز (مثل: البحث عن أداة)","fr":""}, {"text":"+0","type":"num"}, {"text":"يجب القضاء عليها كلياً","fr":""}],
    ],
    caption_ar="الجدول 2: تصنيف الحركات الثلاث وفق جيلبريث مع الأزمنة المرجعية",
    caption_fr="Tableau 2: Classification des trois mouvements selon Gilbreth"
))

SECTIONS_HTML.append(subsection("معادلة الزمن القياسي (Temps Standard)", "Formule du Temps Standard"))

SECTIONS_HTML.append(callout(
    "معادلة الزمن القياسي — Leroy / BTE",
    "<p style='text-align:center; direction:ltr; font-size:13pt;'><strong>T<sub>standard</sub> = T<sub>moyen</sub> × (1 + معامل الراحة)</strong></p><p>حيث: <strong>T<sub>standard</sub></strong> = الزمن القياسي المعتمد للعملية، <strong>T<sub>moyen</sub></strong> = الزمن المُسجّل (متوسط القياسات)، <strong>معامل الراحة</strong> = 15-25% حسب طبيعة العمل وظروفه.</p>",
    variant="ochre", icon="∑"
))

# Section 4
SECTIONS_HTML.append(section_header(4, "موازنة خطوط الإنتاج (Équilibrage)", "Équilibrage des Lignes"))

SECTIONS_HTML.append("""
<p>تُعدّ موازنة الخط الإنتاجي <span class="fr">(Équilibrage de chaîne)</span> من أدق مهام المهندس أو التقني في صناعة الملابس. تتمثّل المهمة في توزيع العمليات الإنتاجية على ماكينات الخياطة بطريقة تمنع حدوث <strong>عنق الزجاجة</strong> <span class="fr">(Goulot d'étranglement)</span>، وتضمن تدفّقاً سلساً للمنتج من البداية إلى التغليف.</p>
""")

SECTIONS_HTML.append(subsection("مفهوم عنق الزجاجة", "Concept du Goulot d'étranglement"))

SECTIONS_HTML.append("""
<p>عنق الزجاجة هو العملية التي يكون زمنها أطول بكثير من العمليات السابقة واللاحقة، مما يؤدّي إلى تكدّس القطع قبلها وانتظار العمّال بعدها. في صناعة الملابس، يحدث ذلك غالباً عند العمليات المعقّدة مثل تركيب الجيوب، الياقات، أو السحّابات، حيث يكون الزمن أعلى من المتوسط. تحديد عنق الزجاجة هو الخطوة الأولى في أي مشروع تحسين إنتاجي.</p>
""")

SECTIONS_HTML.append(subsection("مؤشرات موازنة خط الإنتاج", "Indicateurs d'Équilibrage"))

SECTIONS_HTML.append(data_table(
    [("المؤشّر", "Indicateur"), ("المعادلة", "Formule"), ("الحدّ الأدنى المقبول", "Seuil Minimal")],
    [
        [{"text":"معدل التوازن","fr":"Taux d'équilibre"}, {"text":"(الزمن الأقصى / متوسط الزمن) × 100","fr":""}, {"text":"≥ 85%","type":"num"}],
        [{"text":"كفاءة الخط","fr":"Efficacité"}, {"text":"(مجموع الأزمنة / (الزمن الأقصى × عدد العمّال)) × 100","fr":""}, {"text":"≥ 80%","type":"num"}],
    ],
    caption_ar="الجدول 3: مؤشّرات جودة موازنة خطوط الإنتاج",
    caption_fr="Tableau 3: Indicateurs de qualité d'équilibrage des lignes"
))

# Section 5
SECTIONS_HTML.append(section_header(5, "دراسة حالة: ورشة الرويبة", "Étude de Cas: Atelier Rouiba"))

SECTIONS_HTML.append("""
<p>طلب مدير إحدى الورشات بالمنطقة الصناعية بالرويبة (الجزائر العاصمة) رفع الإنتاجية لخط تجميع السراويل الكلاسيكية الرجالية. كانت الورشة تُنتج <strong>280 وحدة/يوم</strong> من 8 ساعات عمل يومياً، أي ما يعادل <strong>35 وحدة/ساعة</strong>. الهدف كان رفع الإنتاج إلى <strong>400 وحدة/يوم</strong> (<strong>50 وحدة/ساعة</strong>).</p>
""")

SECTIONS_HTML.append(subsection("الوضع الأول: تحديد عنق الزجاجة", "Situation Initiale"))

SECTIONS_HTML.append(data_table(
    [("#", "N°"), ("العملية المستعملة", "Opération"), ("الآلة", "Machine"), ("الزمن (ثانية)", "Temps (s)"), ("ملاحظة", "Obs.")],
    [
        [{"text":"1","type":"num"}, {"text":"تركيب الجيب الجانبي","fr":""}, {"text":"Piqueuse","fr":""}, {"text":"120","type":"num"}, {"text":"عنق الزجاجة","fr":""}],
        [{"text":"2","type":"num"}, {"text":"جمع الجوانب","fr":""}, {"text":"Surjeteuse","fr":""}, {"text":"45","type":"num"}, {"text":"يعادل ⅓ الزمن","fr":""}],
        [{"text":"3","type":"num"}, {"text":"تركيب السحّابة","fr":""}, {"text":"Piqueuse","fr":""}, {"text":"55","type":"num"}, {"text":"يعادل النصف","fr":""}],
        [{"text":"4","type":"num"}, {"text":"عمل الوشاح السفلي","fr":""}, {"text":"Recouvreuse","fr":""}, {"text":"50","type":"num"}, {"text":"يعادل النصف","fr":""}],
        [{"text":"5","type":"num"}, {"text":"المراقبة النهائية و الكي","fr":""}, {"text":"—","fr":""}, {"text":"40","type":"num"}, {"text":"ضمن المتوسط","fr":""}],
    ],
    caption_ar="الجدول 4: تحليل زمن العمليات قبل التحسين — ظهور عنق الزجاجة في تركيب الجيب",
    caption_fr="Tableau 4: Analyse des temps avant amélioration — goulot d'étranglement: pose poche"
))

SECTIONS_HTML.append(bar_chart(
    title_ar="مقارنة زمن العمليات قبل و بعد تطبيق OST",
    title_fr="Comparaison des Temps d'Opération Avant/Après OST",
    categories=[
        ("تركيب الجيب", "Pose poche"),
        ("جمع الجوانب", "Côtés"),
        ("تركيب السحّابة", "Fermeture"),
        ("الوشاح السفلي", "Ourlet"),
        ("المراقبة النهائية", "Contrôle final"),
    ],
    values=[120, 45, 55, 50, 40],
    unit=" ث",
    caption_ar="الشكل 1: زمن العمليات (بالثواني) قبل التحسين — تركيب الجيب هو عنق الزجاجة",
    caption_fr="Figure 1: Temps d'opérations avant amélioration — goulot d'étranglement: pose poche"
))

SECTIONS_HTML.append("""
<p>يُظهر التحليل أن عملية تركيب الجيب الجانبي تستغرق <strong>120 ثانية</strong>، أي ما يقارب ثلاثة أضعاف متوسط العمليات الأخرى. هذا الفارق يُسبّب تكدّس القطع عند الماكينة الثانية وانتظار العمّال في العمليات اللاحقة، وهو ما يُفسّر عدم قدرة الورشة على تجاوز 280 وحدة يومياً رغم توافر ساعات عمل إضافية.</p>
""")

SECTIONS_HTML.append(subsection("الحلول المقترحة وفق مبادئ OST", "Solutions Proposées"))

SECTIONS_HTML.append(flowchart([
    ("1", "تقسيم عملية تركيب الجيب إلى عمليتين فرعيتين: التحضير (50 ثا) و التثبيت (55 ثا)", "Division de l'opération poche"),
    ("2", "إضافة ماكينة خياطة مساعدة Overlock متخصصة في قص حواف الجيب أثناء تركيبه", "Ajout machine Overlock"),
    ("3", "تنظيم بيئة العمل: وضع حاويات القطع بالقرب من اليد اليسرى لتفادي الالتفات غير الضروري", "Réaménagement poste"),
    ("4", "تدريب العامل على الإيقاع الصحيح عبر SOP (Standard Operating Procedure) لمدة 3 أيام", "Formation SOP"),
]))

# Section 6
SECTIONS_HTML.append(section_header(6, "النتائج و مؤشرات الأداء (KPIs)", "Résultats et KPIs"))

SECTIONS_HTML.append("""
<p>بعد تطبيق مبادئ الـ <span class="fr">OST</span> في ورشة الرويبة، ارتفعت كفاءة خط الإنتاج بنسبة <strong>28%</strong>، مع انخفاض ملحوظ في زمن تعطّل العمالة. كما تحسّنت معنويات العمّال بفضل انخفاض الضغط الناتج عن تكدّس القطع. يُبرز هذا المثال كيف يمكن لتطبيق مبادئ علمية بسيطة أن يُحدث فارقاً اقتصادياً ضخماً دون استثمار في تجهيزات جديدة.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("55 ثا", "زمن عملية الجيب بعد التحسين (كان 120 ثا)", "Temps poche après amélioration"),
    ("28%", "نسبة التحسين في كفاءة الخط", "Taux d'amélioration efficacité"),
    ("420", "إنتاج يومي بعد التحسين (كان 280)", "Production journalière"),
    ("+50%", "زيادة الإنتاجية الكلية", "Hausse productivité globale"),
]))

# Section 7
SECTIONS_HTML.append(section_header(7, "الإرغونوميا و ظروف العمل", "Ergonomie et Conditions de Travail"))

SECTIONS_HTML.append("""
<p>تُعرَّف <strong>الإرغونوميا</strong> <span class="fr">(Ergonomie)</span> بأنها العلم الذي يدرس علاقة الإنسان ببيئة عمله، بهدف تصميم بيئة عمل تُلائم قدراته الفيزيولوجية والذهنية وتُجنّبه الإصابات المهنية. في صناعة الملابس، تُعدّ الإرغونوميا ضرورة قانونية (وفق القانون الجزائري 13-03)، قبل أن تكون تحسيناً إنتاجياً.</p>
""")

SECTIONS_HTML.append(data_table(
    [("العامل", "Facteur"), ("القيمة المعيارية", "Valeur Normale"), ("المخاطر عند التجاوز", "Risques")],
    [
        [{"text":"ارتفاع طاولة الخياطة","fr":""}, {"text":"75-80 سم","type":"num"}, {"text":"آلام أسفل الظهر، إرهاق الكتف","fr":""}],
        [{"text":"الإضاءة على طاولة العمل","fr":""}, {"text":"500-750 لوكس","type":"num"}, {"text":"صداع، إرهاق العين، أخطاء بصرية","fr":""}],
        [{"text":"مستوى الضوضاء","fr":""}, {"text":"أقل من 80 ديسيبل","type":"num"}, {"text":"إرهاق ذهني، فقدان السمع التدريجي","fr":""}],
        [{"text":"حرارة الورشة","fr":""}, {"text":"20-24°C شتاء / 22-26°C صيف","type":"num"}, {"text":"إرهاق حراري، انخفاض التركيز","fr":""}],
        [{"text":"وضع الجلوس على الماكينة","fr":""}, {"text":"100-110° للورك / 90-100° للركبة","type":"num"}, {"text":"آلام الظهر والدورة الدموية","fr":""}],
    ],
    caption_ar="الجدول 5: المعايير الإرغونومية المعتمدة في معاهد INSFP",
    caption_fr="Tableau 5: Normes ergonomiques adoptées dans les INSFP"
))

SECTIONS_HTML.append(pie_chart(
    title_ar="مصادر الإصابات المهنية في صناعة الألبسة",
    title_fr="Sources des Accidents du Travail dans l'Habillement",
    segments=[
        ("إرهاق الظهر", "Mal de dos", 35, "#0F4D3A"),
        ("إجهاد العين", "Fatigue visuelle", 25, "#1B6B52"),
        ("إصابات اليد", "Blessures main", 20, "#C2932E"),
        ("فقدان السمع", "Perte auditive", 12, "#7BA38A"),
        ("أخرى", "Autres", 8, "#D4B36A"),
    ],
    center_value="100%",
    center_label="مصادر الإصابات",
    caption_ar="الشكل 2: توزيع مصادر الإصابات المهنية في صناعة الألبسة الجزائرية (2023)",
    caption_fr="Figure 2: Répartition des accidents du travail (2023)"
))

# Section 8
SECTIONS_HTML.append(section_header(8, "الخلاصة و المراجع", "Conclusion et Références"))

SECTIONS_HTML.append("""
<p>جوهر التنظيم العلمي للعمل هو تحويل الإنتاج من فن ذاتي إلى علم قابل للتكرار والتطوير المستمر. لا يمكن لورشات الملابس الجزائرية المنافسة عالمياً ومحلياً دون اعتماد دراسات دقيقة للـ <span class="fr">OST</span> لتثمين الوقت وتقليص نسبة الهدر في الموارد. ينبغي لكل تقني سامي يطمح لمنصب مسؤول في ورشة إنتاج أو مكتب دراسات أن يتقن مبادئ هذه الوحدة ويُطبّقها في الواقع المهني.</p>

<p>كما تُكمِّل وحدة الـ <span class="fr">OST</span> الوحدات السابقة (النمذجة، التدريج، الملف التقني)، إذ تُتيح للمصمم حساب الأزمنة المطلوبة لكل عملية منذ مرحلة التصميم، وبالتالي تقدير التكلفة التقديرية بدقة، وتحديد ما إذا كان المنتج قابلاً للتصنيع الاقتصادي. هذا التكامل هو ما يصنع الفرق بين تقني قادر على الإدارة الإنتاجية الكاملة وتقني يقتصر على التنفيذ التقني.</p>
""")

SECTIONS_HTML.append(subsection("نماذج إضافية لتطبيق OST", "Cas Pratiques Supplémentaires"))
SECTIONS_HTML.append("""
<ul>
<li><strong>ورشة نقاش بوهار:</strong> المشكلة: نسبة أخطاء قص عالية (12%)، الحل: رقمنة الباترونات واعتماد قص آلي <span class="fr">(Cutting machine)</span>. النتيجة: انخفاض الهدر إلى 4%، توفير 18 مليون دج سنوياً.</li>
<li><strong>ورشة نسوية في تلمسان:</strong> المشكلة: إرهاق العاملات (10 ساعات/يوم) وارتفاع نسبة الأخطاء. الحل: تطبيق مبادئ الإرغونوميا: تعديل ارتفاع طاولات الخياطة (من 70 إلى 78 سم)، تحسين الإضاءة (إلى 650 لوكس)، تقليل ساعات العمل إلى 8 ساعات مع فترات راحة. النتيجة: انخفاض الأخطاء بـ 40%، تحسّن الإنتاجية بـ 22%.</li>
</ul>
""")

SECTIONS_HTML.append(callout(
    "العامل الحاسم في نجاح OST",
    "<p>لا يعتمد نجاح تطبيق <span class=\"fr\">OST</span> على الجانب التقني فقط، بل بشكل أساسي على إشراك العمّال في عملية التحسين. العمّال الذين يرون فائدتهم ويُقدّمون اقتراحات قيّمة من تجربتهم اليومية يُبدون تعاوناً أعلى، ويُحقّقون نتائج أفضل من تلك المحسوبة نظرياً من قِبَل المهندسين.</p>",
    variant="emerald", icon="!"
))

SECTIONS_HTML.append(quote_block(
    "الإدارة العلمية ليست مجرد مجموعة من القواعد، بل هي ثورة عقلية كاملة في طريقة تفكير الإدارة والعمّال معاً حول العمل المشترك.",
    "Henri Fayol — Principles of Management"
))

SECTIONS_HTML.append(subsection("المراجع", "Références Bibliographiques"))
SECTIONS_HTML.append("""
<ol>
<li>Taylor, F.W., The Principles of Scientific Management, Harper & Brothers, New York, 1911.</li>
<li>Leroy, H., Bureau des Temps Élémentaires (BTE) — Manuel Pratique, Éditions de l'Organisation, Paris, 2018.</li>
<li>وزارة الصناعة الجزائرية، تقرير قطاع النسيج والألبسة 2023، المديرية العامة للصناعة، الجزائر، 2024.</li>
<li>المعهد الوطني للسلامة والصحة المهنية (INRS)، دليل الإرغونوميا في صناعة الألبسة، الجزائر، 2022.</li>
<li>Buzacott, J.A., Production Planning and Control in the Apparel Industry, Wiley, London, 2019.</li>
<li>وزارة العمل الجزائرية، القانون التوجيهي للسلامة والصحة المهنية (القانون 13-03)، الجريدة الرسمية، الجزائر، 2013.</li>
</ol>
""")

# ---------- Section 9: Glossary ----------
SECTIONS_HTML.append(section_header(9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue"))

SECTIONS_HTML.append("""
<p>يُقدّم هذا المعجم المصطلحات التقنية الأساسية المستعملة في وحدة التنظيم العلمي للعمل، مزدوج اللغة (عربي/فرنسي). تشمل المصطلحات المفاتيح في دراسة الحركات والأزمنة، موازنة خطوط الإنتاج، والإرغونوميا.</p>
""")

SECTIONS_HTML.append(data_table(
    [("المصطلح العربي", "Terme Arabe"), ("المصطلح الفرنسي", "Terme Français"), ("التعريف المختصر", "Définition Courte")],
    [
        [{"text":"التنظيم العلمي للعمل","fr":""}, {"text":"OST","fr":""}, {"text":"علم الإدارة والترشيد الصناعي","fr":""}],
        [{"text":"دراسة الحركات","fr":""}, {"text":"Étude des Mouvements","fr":""}, {"text":"تحليل الحركات الفيزيائية للعامل","fr":""}],
        [{"text":"دراسة الأزمنة","fr":""}, {"text":"Chronométrage","fr":""}, {"text":"قياس زمن كل عملية","fr":""}],
        [{"text":"الزمن المعياري","fr":""}, {"text":"Temps Standard","fr":""}, {"text":"الزمن المرجعي للعملية","fr":""}],
        [{"text":"معامل الراحة","fr":""}, {"text":"Coefficient de Repos","fr":""}, {"text":"نسبة مضافة للراحة (15-25%)","fr":""}],
        [{"text":"عنق الزجاجة","fr":""}, {"text":"Goulot d'Étranglement","fr":""}, {"text":"العملية الأبطأ في الإنتاج","fr":""}],
        [{"text":"موازنة الخط","fr":""}, {"text":"Équilibrage","fr":""}, {"text":"توزيع العمليات لتجنّب التكدّس","fr":""}],
        [{"text":"الإرغونوميا","fr":""}, {"text":"Ergonomie","fr":""}, {"text":"علم تصميم بيئة العمل","fr":""}],
        [{"text":"مكتب الأزمنة الأولية","fr":""}, {"text":"BTE","fr":""}, {"text":"Bureau des Temps Élémentaires","fr":""}],
        [{"text":"حركة ضائعة","fr":""}, {"text":"Mouvement Perdu","fr":""}, {"text":"حركة لا تُسهم في الإنجاز","fr":""}],
        [{"text":"حركة فعّالة","fr":""}, {"text":"Mouvement Efficace","fr":""}, {"text":"حركة تُسهم في الإنجاز","fr":""}],
        [{"text":"كفاءة الخط","fr":""}, {"text":"Efficacité de Ligne","fr":""}, {"text":"نسبة كفاءة خط الإنتاج","fr":""}],
    ],
    caption_ar="الجدول 7: معجم مصطلحات التنظيم العلمي للعمل",
    caption_fr="Tableau 7: Glossaire des termes de l'OST"
))

# ---------- Section 10: Exercises ----------
SECTIONS_HTML.append(section_header(10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas"))

SECTIONS_HTML.append(subsection("تمرين 1: حساب الزمن المعياري", "Exercice 1: Calcul du Temps Standard"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> عملية تركيب ياقة تستغرق في المتوسط 145 ثانية (متوسط 12 قياسة). معامل الراحة المعتمد 20%. احسب الزمن المعياري.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p><strong>T<sub>standard</sub> = T<sub>moyen</sub> × (1 + معامل الراحة)</strong></p><p>T<sub>standard</sub> = 145 × (1 + 0.20) = 145 × 1.20 = <strong>174 ثانية</strong> (أي 2.9 دقيقة).</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("تمرين 2: حساب كفاءة خط الإنتاج", "Exercice 2: Calcul d'Efficacité de Ligne"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> خط إنتاج يتضمّن 6 عمليات بأزمنة: 60، 75، 120 (عنق الزجاجة)، 90، 80، 70 ثانية. احسب كفاءة الخط.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p><strong>كفاءة الخط = (مجموع الأزمنة / (الزمن الأقصى × عدد العمّال)) × 100</strong></p><p>مجموع الأزمنة = 60+75+120+90+80+70 = 495 ثانية.</p><p>الزمن الأقصى × عدد العمّال = 120 × 6 = 720 ثانية.</p><p>كفاءة الخط = (495 / 720) × 100 = <strong>68.75%</strong></p><p>هذه الكفاءة دون الحد الأدنى المقبول (80%)، مما يستدعي إعادة موازنة الخط.</p>",
    variant="ochre", icon="★"
))

SECTIONS_HTML.append(subsection("تمرين 3: منحنى التحسين بعد تطبيق OST", "Exercice 3: Courbe d'Amélioration après OST"))

SECTIONS_HTML.append(line_chart(
    title_ar="منحنى تحسّن الإنتاجية بعد تطبيق OST",
    title_fr="Courbe d'Amélioration de la Productivité après OST",
    x_labels=["قبل", "أسبوع 1", "أسبوع 2", "أسبوع 3", "أسبوع 4"],
    series=[
        ("إنتاج يومي (وحدة)", "Production journalière", [280, 310, 350, 390, 420], "#1B6B52"),
    ],
    y_unit=" وحدة",
    caption_ar="الشكل 3: تطوّر الإنتاج اليومي بعد تطبيق مبادئ OST — تحسّن بنسبة 50% في 4 أسابيع",
    caption_fr="Figure 3: Évolution de la production après OST — amélioration de 50% en 4 semaines"
))
