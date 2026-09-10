"""
Manual 7: التكنولوجيا النسيجية — Technologie Textile
Module 06 in the reference structure.
"""
from manuals_template import (
    section_header, subsection, data_table, callout, flowchart,
    stat_row, quote_block, bar_chart, pie_chart, line_chart, progress_chart
)

MANUAL_7 = {
    "module_num": "06",
    "module_num_label": "الوحدة التكوينية",
    "title_ar": "التكنولوجيا النسيجية — الألياف و الأقمشة",
    "title_fr": "Technologie Textile — Fibres et Tissus",
    "code": "HTE1204 / TT",
    "toc_items": [
        (1, "مقدمة في علم النسيج", "Introduction", 3),
        (2, "تصنيف الألياف النسيجية", "Classification des Fibres", 4),
        (3, "الخصائص الفيزيائية للألياف", "Propriétés Physiques", 6),
        (4, "تراكيب النسيج الأساسية (Armures)", "Armures de Tissage", 8),
        (5, "فحوص المختبر على الأقمشة", "Tests Laboratoires", 10),
        (6, "النسيج في الصناعة الجزائرية", "Textile Algérien", 12),
        (7, "التشطيبات و الإنهاء (Finishing)", "Finitions", 13),
        (8, "الخلاصة و المراجع", "Conclusion et Références", 15),
        (9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue", 17),
        (10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas", 19),
    ],
    "closing_ar": "إتقان التكنولوجيا النسيجية هو إتقان للّغة القماش: كل خيط يحكي قصة، وكل نسيج يُحدّد مصير المنتج النهائي.",
    "closing_fr": "Maîtriser la technologie textile, c'est maîtriser le langage du tissu: chaque fil raconte une histoire, chaque armure détermine le destin du produit final.",
}

SECTIONS_HTML = []

# Section 1
SECTIONS_HTML.append(section_header(1, "مقدمة في علم النسيج", "Introduction"))

SECTIONS_HTML.append("""
<p>تُعرَّف <strong>التكنولوجيا النسيجية</strong> <span class="fr">(Technologie Textile)</span> بأنها العلم الذي يدرس الألياف والخيوط والأقمشة من حيث المنشأ، الخصائص الفيزيائية والكيميائية، طرق الإنتاج، ومعايير الجودة. تُمثّل هذه الوحدة الأساس المعرفي الذي يبني عليه التقني السامي قراراته في اختيار الأقمشة المناسبة لكل منتج، وتحديد طرق التعامل معها في مختلف مراحل التصنيع.</p>

<p>لا يمكن للمصمم أو التقني إنتاج ملابس عالية الجودة دون فهم عميق لطبيعة القماش الذي يعمل به. كل قماش له سلوكه الخاص: بعضها ينكمش بعد الغسل، بعضها يتعرض للحرارة، بعضها يتمدّد مع الاستعمال، بعضها يتأثر بالمواد الكيميائية. هذه المعرفة ليست ترفاً أكاديمياً، بل ضرورة عملية تُحدّد نجاح أو فشل المنتج النهائي.</p>

<p>في السياق الجزائري، تكتسب التكنولوجيا النسيجية أهمية مضاعفة لسببين: أولاً، تنوّع التراث النسيجي الوطني (الصوف في الأطلس، الحرير في الشاوية، الكتان في الشمال) يفرض على التقني معرفة واسعة بمختلف أنواع الألياف. ثانياً، سياسة الاستيراد الانتقائي والحثّ على الإنتاج المحلي تُلزم المؤسسات الجزائرية بإنتاج أقمشة وطنية تنافس المستوردة، وهو ما يتطلب كفاءات نسيجية متقدمة. تشير إحصائيات وزارة الصناعة لسنة 2023 إلى أن القطاع النسيجي الجزائري يضم 1200 مؤسسة، تستوعب 70,000 عامل، وتُساهم بنسبة 2.3% من الناتج الصناعي الوطني.</p>
""")

SECTIONS_HTML.append(stat_row([
    ("1200+", "مؤسسة نسيجية في الجزائر", "Entreprises textiles en Algérie"),
    ("70,000", "عامل في القطاع النسيجي", "Employés dans le secteur textile"),
    ("2.3%", "مساهمة القطاع في الناتج الصناعي", "Contribution au PIB industriel"),
    ("6", "فئات رئيسية للألياف النسيجية", "Catégories principales de fibres"),
]))

# Section 2
SECTIONS_HTML.append(section_header(2, "تصنيف الألياف النسيجية", "Classification des Fibres"))

SECTIONS_HTML.append("""
<p>تُصنّف الألياف النسيجية وفق منشئها إلى ثلاث فئات رئيسية: <strong>ألياف طبيعية</strong> (نباتية وحيوانية)، <strong>ألياف كيميائية صناعية</strong> (مُجدَّدة وصناعية بحتة)، و<strong>ألياف مخلوطة</strong> (مزيج بين النوعين). كل فئة لها خصائصها وتطبيقاتها، واختيار النوع المناسب يُحدّد جودة المنتج النهائي وسعره. تُعدّ معرفة مصدر الألياف وخصائصها الخطوة الأولى في اختيار القماش المناسب لكل تصميم.</p>
""")

SECTIONS_HTML.append(data_table(
    [("الفئة", "Catégorie"), ("الألياف", "Fibres"), ("الاستخدام الرئيسي", "Usage Principal")],
    [
        [{"text":"طبيعية نباتية","fr":"Naturelles végétales"}, {"text":"قطن، كتان، جوت، أنواعا","fr":""}, {"text":"الألبسة اليومية، الأثاث","fr":""}],
        [{"text":"طبيعية حيوانية","fr":"Naturelles animales"}, {"text":"صوف، حرير، أنغورا، كشمير","fr":""}, {"text":"الألبسة الشتوية، الفساتين الراقية","fr":""}],
        [{"text":"كيميائية مُجدَّدة","fr":"Artificielles régénérées"}, {"text":"viscose, lyocell, rayonne, modal","fr":""}, {"text":"بديل اقتصادي للحرير الطبيعي","fr":""}],
        [{"text":"كيميائية صناعية","fr":"Synthétiques"}, {"text":"بوليستر، نايلون، أكريليك، إيلاستان","fr":""}, {"text":"الألبسة الرياضية، الجينز، التريكو","fr":""}],
        [{"text":"مخلوطة","fr":"Mixtes"}, {"text":"قطن/بوليستر، صوف/أكريليك","fr":""}, {"text":"معظم الألبسة الجاهزة المعاصرة","fr":""}],
        [{"text":"تقنية خاصة","fr":"Techniques"}, {"text":"Kevlar, Nomex, ألياف معدنية","fr":""}, {"text":"الألبسة الواقية، التطبيقات الصناعية","fr":""}],
    ],
    caption_ar="الجدول 1: تصنيف الألياف النسيجية الست الفئات الرئيسية",
    caption_fr="Tableau 1: Classification des six catégories de fibres textiles"
))

SECTIONS_HTML.append(pie_chart(
    title_ar="توزيع استعمال الألياف في صناعة الألبسة الجزائرية",
    title_fr="Répartition de l'Utilisation des Fibres en Algérie",
    segments=[
        ("قطن", "Coton", 40, "#0F4D3A"),
        ("بوليستر", "Polyester", 35, "#1B6B52"),
        ("خلط قطن/بولي", "Mixte C/P", 15, "#C2932E"),
        ("صوف", "Laine", 5, "#7BA38A"),
        ("فيزكوز", "Viscose", 3, "#D4B36A"),
        ("أخرى", "Autres", 2, "#9CA3AF"),
    ],
    center_value="100%",
    center_label="استعمال الألياف",
    caption_ar="الشكل 1: توزيع استعمال الألياف في صناعة الألبسة الجزائرية (2024)",
    caption_fr="Figure 1: Répartition de l'utilisation des fibres en Algérie (2024)"
))

SECTIONS_HTML.append(callout(
    "قاعدة ذهبية: الخلط القطن/بوليستر",
    "<p>الخلط الأكثر استعمالاً في صناعة الألبسة الجزائرية هو <strong>65% بوليستر + 35% قطن</strong> (يُسمّى Tergal في الجزائر). يجمع هذا الخلط بين متانة البوليستر وراحة القطن، ويُستعمل في الأثواب المدرسية، أزياء العمل، والألبسة اليومية. لكن يجب الانتباه: نسبة البوليستر العالية تُقلّل من قابلية امتصاص العرق وتُسبب إزعاجاً في المناخ الحار.</p>",
    variant="ochre", icon="★"
))

# Section 3
SECTIONS_HTML.append(section_header(3, "الخصائص الفيزيائية للألياف", "Propriétés Physiques"))

SECTIONS_HTML.append("""
<p>لكل نوع من الألياف خصائص فيزيائية وكيميائية تُحدّد سلوكه في التصنيع والاستعمال. يجب على التقني السامي معرفة هذه الخصائص بالتفصيل لاختيار القماش المناسب لكل تطبيق. تتضمن الخصائص الرئيسية: المتانة، المرونة، الامتصاصية، المقاومة الحرارية، والمقاومة الكيميائية.</p>
""")

SECTIONS_HTML.append(data_table(
    [("الليف", "Fibre"), ("المتانة (g/denier)", "Ténacité"), ("الاستطالة (%)", "Allongement"), ("امتصاص الماء (%)", "Absorption")],
    [
        [{"text":"قطن","fr":"Coton"}, {"text":"3.0-5.0","type":"num"}, {"text":"3-10","type":"num"}, {"text":"7-8","type":"num"}],
        [{"text":"صوف","fr":"Laine"}, {"text":"1.0-1.7","type":"num"}, {"text":"25-40","type":"num"}, {"text":"13-18","type":"num"}],
        [{"text":"حرير","fr":"Soie"}, {"text":"2.5-5.0","type":"num"}, {"text":"10-25","type":"num"}, {"text":"9-11","type":"num"}],
        [{"text":"كتان","fr":"Lin"}, {"text":"5.0-6.5","type":"num"}, {"text":"2-3","type":"num"}, {"text":"7-9","type":"num"}],
        [{"text":"بوليستر","fr":"Polyester"}, {"text":"4.0-8.0","type":"num"}, {"text":"15-45","type":"num"}, {"text":"0.4-0.8","type":"num"}],
        [{"text":"نايلون","fr":"Nylon"}, {"text":"4.5-9.0","type":"num"}, {"text":"15-40","type":"num"}, {"text":"3.5-5.0","type":"num"}],
        [{"text":"أكريليك","fr":"Acrylique"}, {"text":"2.0-3.5","type":"num"}, {"text":"25-45","type":"num"}, {"text":"1.5-2.5","type":"num"}],
    ],
    caption_ar="الجدول 2: الخصائص الفيزيائية الرئيسية للألياف النسيجية",
    caption_fr="Tableau 2: Propriétés physiques principales des fibres textiles"
))

# Section 4
SECTIONS_HTML.append(section_header(4, "تراكيب النسيج الأساسية (Armures)", "Armures de Tissage"))

SECTIONS_HTML.append("""
<p>تُحدّد <strong>تراكيب النسيج</strong> <span class="fr">(Armures de Tissage)</span> الطريقة التي تتشابك بها خيوط السداء <span class="fr">(Chaîne)</span> مع خيوط اللحمة <span class="fr">(Trame)</span> لإنتاج القماش. كل تركيب يُنتج قماشاً له خصائص بصرية وملمسية وميكانيكية مختلفة. هناك ثلاثة تراكيب أساسية تُعتبر الأمهات لكل التراكيب النسيجية الأخرى.</p>
""")

SECTIONS_HTML.append(data_table(
    [("التركيب", "Armure"), ("الوصف", "Description"), ("الخصائص", "Caractéristiques"), ("الأمثلة", "Exemples")],
    [
        [{"text":"النسيج البسيط","fr":"Toile"}, {"text":"خيط فوق و خيط تحت","fr":""}, {"text":"متناسق، متين، أقل مرونة","fr":""}, {"text":"قطن خام، كتان، موسلين","fr":""}],
        [{"text":"النسيج المائل","fr":"Serge"}, {"text":"إزاحة في كل خيط","fr":""}, {"text":"مائل العروض، مرونة عالية","fr":""}, {"text":"جينز، تيد، gabardine","fr":""}],
        [{"text":"النسيج الساتان","fr":"Satin"}, {"text":"خيوط تطفو على سطح","fr":""}, {"text":"لمعان، نعومة، أقل متانة","fr":""}, {"text":"ساتان، دوقس، شarmeuse","fr":""}],
        [{"text":"النسيج الجاكار","fr":"Jacquard"}, {"text":"تركيب مركّب بصور","fr":""}, {"text":"زخارف منسوجة، فاخر","fr":""}, {"text":"قفطان، داماس، بروكار","fr":""}],
        [{"text":"التجعيد","fr":"Crêpe"}, {"text":"خيوط مفتولة بإحكام","fr":""}, {"text":"سطح مجعّد، مرونة عالية","fr":""}, {"text":"كريب جورجيت، كريب دي شين","fr":""}],
        [{"text":"المخمل","fr":"Velours"}, {"text":"خيوط قصية على السطح","fr":""}, {"text":"ملمس ناعم، فاخر","fr":""}, {"text":"مخمل قطني، مخمل حريري","fr":""}],
    ],
    caption_ar="الجدول 3: التراكيب النسيجية الأساسية وخصائصها",
    caption_fr="Tableau 3: Armures de tissage fondamentales et caractéristiques"
))

# Section 5
SECTIONS_HTML.append(section_header(5, "فحوص المختبر على الأقمشة", "Tests Laboratoires"))

SECTIONS_HTML.append("""
<p>تُجرى فحوص المختبر على الأقمشة للتأكد من مطابقتها للمعايير المطلوبة قبل اعتمادها في الإنتاج. تُمثّل هذه الفحوص ضمانة الجودة الأساسية، وتمنع المؤسسة من إنتاج كميات كبيرة من منتجات معيبة. تُجرى الفحوص في مختبرات الجودة التابعة للمؤسسات أو في مختبرات معتمدة مستقلة مثل مختبر المعهد الجزائري للمعايير <span class="fr">(IANOR)</span>.</p>
""")

SECTIONS_HTML.append(data_table(
    [("الفحص", "Test"), ("المعيار المرجعي", "Norme"), ("الهدف", "Objectif")],
    [
        [{"text":"فحص المتانة","fr":"Résistance"}, {"text":"ISO 13934-1","fr":""}, {"text":"قياس قوة الشد للقماش","fr":""}],
        [{"text":"فحص الانكماش","fr":"Rétrécissement"}, {"text":"ISO 6330","fr":""}, {"text":"قياس الانكماش بعد الغسل","fr":""}],
        [{"text":"فحص ثبات اللون","fr":"Solidité couleur"}, {"text":"ISO 105-C06","fr":""}, {"text":"تقيّيم ثبات اللون بعد الغسل","fr":""}],
        [{"text":"فحص التنسيل","fr":"Peluchage"}, {"text":"ISO 12945-2","fr":""}, {"text":"قياس ميل القماش للتنسيل","fr":""}],
        [{"text":"فحص التنفّس","fr":"Respirabilité"}, {"text":"ISO 9237","fr":""}, {"text":"قياس نفاذية الهواء","fr":""}],
        [{"text":"فحص الاحتراق","fr":"Inflammabilité"}, {"text":"ISO 6941","fr":""}, {"text":"تقييم سلوك القماش مع النار","fr":""}],
        [{"text":"فحص الرقم الهيدروجيني","fr":"pH"}, {"text":"ISO 3071","fr":""}, {"text":"تأكيد خلوّ القماش من الأحماض","fr":""}],
    ],
    caption_ar="الجدول 4: الفحوص المخبرية الأساسية على الأقمشة وفق معايير ISO",
    caption_fr="Tableau 4: Tests laboratoires fondamentaux sur tissus selon ISO"
))

SECTIONS_HTML.append(bar_chart(
    title_ar="تطوّر نسبة تغطية السوق الوطني",
    title_fr="Évolution du Taux de Couverture du Marché National",
    categories=[("2018", "2018"), ("2020", "2020"), ("2022", "2022"), ("2024", "2024"), ("2027 (هدف)", "2027")],
    values=[15, 22, 30, 40, 70],
    unit="%",
    caption_ar="الشكل 2: تطوّر نسبة تغطية السوق الجزائري بالأقمشة الوطنية (2018-2027)",
    caption_fr="Figure 2: Évolution du taux de couverture du marché (2018-2027)"
))

# Section 6
SECTIONS_HTML.append(section_header(6, "النسيج في الصناعة الجزائرية", "Textile Algérien"))

SECTIONS_HTML.append("""
<p>يشهد القطاع النسيجي الجزائري منذ 2020 إحياءً ملحوظاً بعد عقود من التراجع، في إطار سياسة وطنية ترمي إلى تقليل الاستيراد وتعزيز الإنتاج المحلي. تتوزّع المؤسسات النسيجية الوطنية بين مؤسسات عمومية تاريخية مثل المؤسسة الوطنية للنسيج والجلد <span class="fr">(ETE)</span>، ومؤسسات خاصة صغيرة ومتوسطة تنمو بسرعة في ولايات الجزائر، وهران، قسنطينة، وتلمسان.</p>

<p>تُنتج المؤسسات الجزائرية حالياً تشكيلة متنوعة من الأقمشة، تشمل: الأقمشة القطنية الأساسية للألبسة اليومية، أقمشة Tergal المُستعملة في الأثواب المدرسية وأزياء العمل، الأقمشة الصوفية المنتجة في تعاونيات الأطلس، والأقمشة التقليدية الفاخرة كالمخمل والجاكار للقفطان والكاراكو. كما تشهد الصناعة الجزائرية تطوّراً في إنتاج الأقمشة التقنية (للاستعمال الطبي والصناعي) عبر شراكات مع مؤسسات دولية.</p>

<p>تشير الإحصائيات الرسمية لوزارة الصناعة إلى أن المؤسسات النسيجية الجزائرية تُغطّي حالياً حوالي <strong>40% من الطلب الوطني</strong> على الأقمشة الأساسية، مقابل <strong>15% فقط</strong> في 2018. الهدف الاستراتيجي للوزارة هو الوصول إلى <strong>70% بحلول 2027</strong>، عبر برامج دعم الاستثمار في القطاع وتأهيل اليد العاملة المتخصصة.</p>
""")

# Section 7
SECTIONS_HTML.append(section_header(7, "التشطيبات و الإنهاء (Finishing)", "Finitions"))

SECTIONS_HTML.append("""
<p>تُعدّ <strong>عمليات التشطيب</strong> <span class="fr">(Finishing)</span> المرحلة الأخيرة في إنتاج القماش، حيث تُجرى عليها معالجات كيميائية وميكانيكية لتحسين خصائصه ومظهره. تُحدّد هذه العمليات الجودة النهائية للقماش وقيمته السوقية، وهي ما يميّز القماش الفاخر عن القماش الاقتصادي.</p>
""")

SECTIONS_HTML.append(data_table(
    [("نوع التشطيب", "Type de Finition"), ("الهدف", "Objectif"), ("التقنية", "Technique")],
    [
        [{"text":"الكوي و التنعيم","fr":"Calandrage"}, {"text":"تنعيم السطح و إعطاء لمعان","fr":""}, {"text":"مرور القماش بين أسطوانتين ساخنتين","fr":""}],
        [{"text":"السَنْجَرَة","fr":"Sanforisation"}, {"text":"منع الانكماش بعد الغسل","fr":""}, {"text":"ضغط ميكانيكي مع بخار","fr":""}],
        [{"text":"العلاج المضاد للماء","fr":"Hydrofuge"}, {"text":"جعل القماش يصدّ الماء","fr":""}, {"text":"طلاء كيميائي بفلور","fr":""}],
        [{"text":"العلاج المضاد للتجعد","fr":"Anti-repass"}, {"text":"تقليل ميل القماش للتجعد","fr":""}, {"text":"راتنجات صناعية حرارية","fr":""}],
        [{"text":"العلاج المضاد للبكتيريا","fr":"Antibactérien"}, {"text":"منع نمو البكتيريا المسببة للروائح","fr":""}, {"text":"جزيئات فضية نانوية","fr":""}],
        [{"text":"صباغة الطرف","fr":"Teinture pièce"}, {"text":"صباغة القماش بعد النسيج","fr":""}, {"text":"غمر في حوض صبغة","fr":""}],
        [{"text":"الطباعة","fr":"Impression"}, {"text":"إضافة زخارف أو نقوشات","fr":""}, {"text":"طباعة رقمية أو بكسلوار","fr":""}],
    ],
    caption_ar="الجدول 5: أنواع عمليات التشطيب النسيجي وأهدافها",
    caption_fr="Tableau 5: Types de finitions textiles et leurs objectifs"
))

# Section 8
SECTIONS_HTML.append(section_header(8, "الخلاصة و المراجع", "Conclusion et Références"))

SECTIONS_HTML.append("""
<p>تُمثّل التكنولوجيا النسيجية الأساس المعرفي الذي يبني عليه التقني السامي كل قراراته في اختيار الأقمشة وتقييم جودتها. لا يمكن إنتاج ملابس عالية الجودة دون فهم عميق لطبيعة القماش وسلوكه في مختلف الظروف. هذه المعرفة هي ما يميّز التقني المحترف عن العامل البسيط، وهي ما يفتح أمامه آفاق الترقي المهني في مختبرات الجودة ومكاتب الدراسات.</p>

<p>يشهد القطاع النسيجي الجزائري إحياءً واعداً، مع توجّه وطني واضح نحو تعزيز الإنتاج المحلي وتقليل الاستيراد. هذا التوجّه يخلق فرصاً مهنية واسعة للتقنيين الذين يتقنون التكنولوجيا النسيجية، سواء في المؤسسات الإنتاجية أو في مختبرات الجودة أو في مكاتب الدراسات. المستقبل ينتمي للتقنيين القادرين على الجمع بين المعرفة النظرية والكفاءة العملية في التعامل مع الأقمشة الحديثة.</p>
""")

SECTIONS_HTML.append(callout(
    "توصية بيداغوجية",
    "<p>يُنصح بتخصيص مخابر مجهّزة بمجاهر ومعدات فحص للأقمشة في معاهد <span class=\"fr\">INSFP</span>، مع تزويد المتدرّبين بعينات من مختلف الألياف والأقمشة للتجربة المباشرة. كما يُوصى بتنظيم زيارات منتظمة إلى مصانع النسيج الجزائرية للاطلاع على مراحل الإنتاج من الألياف إلى القماش النهائي.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("التطبيقات المتقدمة", "Applications Avancées"))
SECTIONS_HTML.append("""
<ul>
<li><strong>الأقمشة التقنية:</strong> أقمشة مصممة لاستعمالات خاصة (طبية، عسكرية، صناعية) مثل أقمشة مقاومة للحريق للرجال الإطفاء، أقمشة طبية معقمة، أقمشة فلترة للصناعة.</li>
<li><strong>الأقمشة الذكية:</strong> أقمشة مدمجة بألياف موصلة أو حساسات إلكترونية، تُستعمل في الألبسة الرياضية لمراقبة النبض والحرارة، أو في الألبسة الطبية لمتابعة حالة المريض.</li>
<li><strong>الأقمشة المُستدامة:</strong> اتجاه عالمي نحو إنتاج أقمشة صديقة للبيئة من ألياف معاد تدويرها أو ألياف طبيعية عضوية، مع تقليل استهلاك المياه والطاقة في الإنتاج.</li>
<li><strong>النانو تكنولوجيا:</strong> استخدام جزيئات نانوية لتحسين خصائص القماش (مقاومة البقع، الحماية من الأشعة فوق البنفسجية، مضاد للروائح).</li>
</ul>
""")

SECTIONS_HTML.append(quote_block(
    "القماش ليس مجرد مادة خام، بل هو لغة. من يتقن لغتها يستطيع تصميم منتجات تتحدث بفصاحة عن الجودة والذوق والكفاءة.",
    "Bureau d'Études Textile — Guide Pratique"
))

SECTIONS_HTML.append(subsection("المراجع", "Références Bibliographiques"))
SECTIONS_HTML.append("""
<ol>
<li>Hatch, K.L., Textile Science, West Publishing, Minneapolis, 2019.</li>
<li>وزارة الصناعة الجزائرية، تقرير قطاع النسيج والألبسة 2023، المديرية العامة للصناعة، الجزائر، 2024.</li>
<li>ISO 4915: Textiles — Stitch types: Classification and terminology, International Organization for Standardization, Geneva, 2019.</li>
<li>المعهد الجزائري للمعايير (IANOR)، المعايير الجزائرية للأقمشة النسيجية، المجموعة الكاملة، الجزائر، 2022.</li>
<li>ETE — Entreprise Nationale du Textile et du Cuir, Catalogue de Production 2023, Alger, 2023.</li>
<li>Kadolph, S.J., Textiles, 12th Edition, Pearson, London, 2020.</li>
</ol>
""")

# ---------- Section 9: Glossary ----------
SECTIONS_HTML.append(section_header(9, "معجم المصطلحات التقنية", "Glossaire Technique Bilingue"))

SECTIONS_HTML.append("""
<p>يُقدّم هذا المعجم المصطلحات التقنية الأساسية المستعملة في وحدة التكنولوجيا النسيجية، مزدوج اللغة (عربي/فرنسي). تشمل المصطلحات المفاتيح في الألياف، التراكيب النسيجية، والفحوص المخبرية.</p>
""")

SECTIONS_HTML.append(data_table(
    [("المصطلح العربي", "Terme Arabe"), ("المصطلح الفرنسي", "Terme Français"), ("التعريف المختصر", "Définition Courte")],
    [
        [{"text":"ليف","fr":""}, {"text":"Fibre","fr":""}, {"text":"الوحدة الأساسية للخيط","fr":""}],
        [{"text":"خيط","fr":""}, {"text":"Fil","fr":""}, {"text":"تجمع من الألياف ملفوف","fr":""}],
        [{"text":"قماش","fr":""}, {"text":"Tissu","fr":""}, {"text":"نسيج من خيوط متشابكة","fr":""}],
        [{"text":"سداء","fr":""}, {"text":"Chaîne","fr":""}, {"text":"الخيوط الطولية في القماش","fr":""}],
        [{"text":"لحمة","fr":""}, {"text":"Trame","fr":""}, {"text":"الخيوط العرضية في القماش","fr":""}],
        [{"text":"تركيب نسيجي","fr":""}, {"text":"Armure","fr":""}, {"text":"طريقة تشابك الخيوط","fr":""}],
        [{"text":"تركيب بسيط","fr":""}, {"text":"Toile","fr":""}, {"text":"خيط فوق وخيط تحت","fr":""}],
        [{"text":"تركيب مائل","fr":""}, {"text":"Serge","fr":""}, {"text":"إزاحة في كل خيط","fr":""}],
        [{"text":"ساتان","fr":""}, {"text":"Satin","fr":""}, {"text":"خيوط تطفو على السطح","fr":""}],
        [{"text":"جاكار","fr":""}, {"text":"Jacquard","fr":""}, {"text":"تركيب مركّب بصور","fr":""}],
        [{"text":"تشطيب","fr":""}, {"text":"Finition","fr":""}, {"text":"معالجة نهائية للقماش","fr":""}],
        [{"text":"صباغة","fr":""}, {"text":"Teinture","fr":""}, {"text":"إعطاء اللون للقماش","fr":""}],
    ],
    caption_ar="الجدول 7: معجم مصطلحات التكنولوجيا النسيجية",
    caption_fr="Tableau 7: Glossaire des termes de technologie textile"
))

# ---------- Section 10: Exercises ----------
SECTIONS_HTML.append(section_header(10, "تمارين تطبيقية و دراسات حالة", "Exercices Pratiques et Études de Cas"))

SECTIONS_HTML.append(subsection("تمرين 1: حساب وزن القماش", "Exercice 1: Calcul du Poids du Tissu"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> قماش مساحته 2 م² ووزنه 360 غرام. احسب وزن القماش بـ غ/م²، وصنّفه (خفيف/متوسط/ثقيل) حسب التصنيف النسيجي.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p>الوزن لكل م² = 360 ÷ 2 = <strong>180 غ/م²</strong>.</p><p>التصنيف: <strong>قماش متوسط الوزن</strong> (150-250 غ/م²).</p><p>هذا الوزن مناسب للأثواب المدرسية وأزياء العمل، لأنه يجمع بين المتانة والراحة.</p>",
    variant="emerald", icon="✓"
))

SECTIONS_HTML.append(subsection("تمرين 2: مقارنة خصائص الألياف", "Exercice 2: Comparaison des Propriétés"))

SECTIONS_HTML.append(progress_chart(
    title_ar="مقارنة خصائص الألياف الرئيسية",
    title_fr="Comparaison des Propriétés des Fibres Principales",
    items=[
        ("متانة قطن", "Ténacité coton", 4, 5, "#0F4D3A"),
        ("متانة بوليستر", "Ténacité polyester", 5, 5, "#1B6B52"),
        ("متانة صوف", "Ténacité laine", 2, 5, "#C2932E"),
        ("امتصاص قطن", "Absorption coton", 5, 5, "#0F4D3A"),
        ("امتصاص بوليستر", "Absorption polyester", 1, 5, "#1B6B52"),
        ("امتصاص صوف", "Absorption laine", 5, 5, "#C2932E"),
        ("مرونة قطن", "Élasticité coton", 2, 5, "#0F4D3A"),
        ("مرونة بوليستر", "Élasticité polyester", 5, 5, "#1B6B52"),
        ("مرونة صوف", "Élasticité laine", 4, 5, "#C2932E"),
    ],
    caption_ar="الشكل 3: مقارنة 3 ألياف على معايير المتانة، الامتصاص، والمرونة",
    caption_fr="Figure 3: Comparaison de 3 fibres sur ténacité, absorption et élasticité"
))

SECTIONS_HTML.append(subsection("تمرين 3: حساب تكلفة الخلط", "Exercice 3: Calcul du Coût de Mélange"))

SECTIONS_HTML.append("""
<p><strong>السؤال:</strong> خليط نسيجي يتكوّن من 65% بوليستر (سعر 350 دج/م) و 35% قطن (سعر 500 دج/م). احسب سعر المتوسط المرجّح للمتر الواحد.</p>
""")

SECTIONS_HTML.append(callout(
    "الحل النموذجي",
    "<p><strong>السعر المرجّح = (0.65 × 350) + (0.35 × 500) = 227.5 + 175 = 402.5 دج/م</strong>.</p><p>هذا السعر يُمثّل التكلفة الحقيقية للقماش المختلط، ويُستعمل في حساب التكلفة التقديرية للمنتج النهائي.</p>",
    variant="ochre", icon="★"
))
