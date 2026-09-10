# Algerian Vocational Education Manuals — Codebase

This codebase generates **9 pedagogical manuals (PDFs)** for the Algerian Vocational Education and Training System (التكوين المهني), covering the **Tailleur Dames (Couture Dame)** specialty under the **INSFP (Institut National de la Formation et de l'Enseignement Professionnels)** curriculum.

**Author:** Ouail Fatiha / وعيل فتيحة

---

## 📁 Project Structure

```
scripts/
├── manuals_template.py              # Shared HTML template with charts (bar, pie, line, progress)
├── manual_01_couture_dame.py        # Manual 1: الخياطة النسائية (overall specialty)
├── manual_02_dossier_technique.py   # Manual 2: إعداد الملف التقني
├── manual_03_gradation.py           # Manual 3: التدريج
├── manual_04_moulage.py             # Manual 4: التفصيل بالقولبة
├── manual_05_ost.py                 # Manual 5: التنظيم العلمي للعمل
├── manual_06_technologie_machines.py # Manual 6: تكنولوجيا الآلة
├── manual_07_technologie_textile.py # Manual 7: التكنولوجيا النسيجية
├── manual_08_protection_consommateur.py # Manual 8: حماية المستهلك
├── manual_09_entrepreneuriat.py     # Manual 9: المقاولاتية
├── generate_all_manuals.py          # Main script: builds all 9 HTML files
├── convert_all_to_pdf.sh            # Converts HTML → PDF via html2pdf-next.js
├── apply_extensions_3_4.py          # Helper: adds charts/glossary/exercises to manuals 3-4
├── apply_extensions_5_9.py          # Helper: adds charts/glossary/exercises to manuals 5-9
├── manual_extensions.py             # Extension definitions (helper module)
├── html_out/                        # Generated HTML output (intermediate)
└── package.json                     # Node.js deps (pagedjs, playwright)
```

---

## 🚀 How to Use

### Prerequisites
- Python 3.10+
- Node.js 18+
- The PDF skill from `/home/z/my-project/skills/pdf/`

### Install Node dependencies
```bash
cd scripts/
npm install pagedjs playwright
npx playwright install chromium
```

### Step 1 — Generate HTML files
```bash
cd scripts/
python3 generate_all_manuals.py
```
This creates 9 HTML files in `html_out/`.

### Step 2 — Convert HTML to PDF
```bash
bash convert_all_to_pdf.sh
```
This converts each HTML to PDF using `html2pdf-next.js` with Chromium native pagination (`--nopaged` flag).

PDFs are saved to: `/home/z/my-project/download/manuals/`

---

## 🎨 Template Features

The `manuals_template.py` file provides:

### Layout Components
- **Cover page** — 3-section design (emerald top bar, white center with title, emerald bottom with author)
- **Table of Contents** — bilingual (Arabic + French) with page numbers
- **Section headers** — numbered circles + bilingual titles + emerald divider
- **Subsection headers** — ochre right-border accent
- **Back cover** — INSFP mark + closing message + metadata

### Content Components
- `data_table()` — bordered tables with header row, alternate row shading, bilingual captions
- `callout()` — colored alert boxes (ochre or emerald variants) for "Golden Rules"
- `flowchart()` — step-by-step process diagrams with numbered circles + arrows
- `stat_row()` — KPI stat cards with large numbers
- `quote_block()` — epigraph blocks with author attribution

### Chart Components (SVG-based)
- `bar_chart()` — vertical bar chart with gridlines, value labels, bilingual category labels
- `pie_chart()` — pie/donut chart with legend, optional center label
- `line_chart()` — multi-series line chart with gridlines, legend
- `progress_chart()` — horizontal progress bars for comparisons

### Color Palette (per spec)
- **Emerald/Pine Green** — `#0F4D3A` (primary), `#1B6B52` (secondary)
- **Ochre/Gold** — `#C2932E` (accent), `#FBF3DC` (light tint)
- **Neutral** — `#FFFFFF` (bg), `#F5F3EA` (cards), `#1F2937` (text)

### Fonts
- **Arabic:** Cairo (headings), Tajawal (body), Amiri (quotes)
- **Latin:** Inter (body), Playfair Display (numbers/serif accents)

---

## 📚 Manual Content

Each manual follows the **INSFP pedagogical standard** (Approche Par Compétences — APC) with:

1. **Introduction** — context, importance, methodology
2. **Skills & Competencies** — Compétence Globale, Objectifs Intermédiaires
3. **Technical Content** — tables, diagrams, case studies
4. **Practical Applications** — TP exercises, real-world scenarios
5. **Assessment** — evaluation grids, performance criteria
6. **Conclusion** — summary + recommendations + references
7. **Glossary** — bilingual (Arabic/French) technical terms
8. **Exercises** — practical problems with model solutions + charts

All content is **bilingual (Arabic + French)** with RTL layout for Arabic and LTR for French technical terms.

---

## 🔧 Customization

To customize for a different student name, edit the `render_cover()` function in `manuals_template.py`:
```python
<div class="author-name-ar">وعيل فتيحة</div>
<div class="author-name-fr">Ouail Fatiha</div>
```

To add a new manual, create `manual_10_xxx.py` following the same structure as the existing ones, then add it to the `MANUALS` list in `generate_all_manuals.py`.

---

## 📄 Output

Each PDF is **15-21 pages** with:
- Cover page
- Table of contents
- 8-11 content sections
- Back cover
- Embedded SVG charts (bar, pie, line, progress)
- Bilingual tables with proper RTL/LTR rendering
- Proper page margins (22mm top, 24mm bottom, 20mm sides)

---

Generated: 2025/2026
