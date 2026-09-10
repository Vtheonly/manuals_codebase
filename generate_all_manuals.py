"""
==================================================================================
ALGERIAN VOCATIONAL TRAINING SYSTEM — MAIN GENERATION SCRIPT
Unified compiler: builds 9 HTML manuals from content modules + registry.
Eliminates need for fragile patch scripts (apply_extensions_3_4.py, etc.).
==================================================================================
Author: Ouail Fati7a wa3il fati7a / وائل فتيحة
Version: 2.0 — Unified Core Architecture
==================================================================================
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from manuals_template import build_manual_html

# Import all 9 manuals
from manual_01_couture_dame          import MANUAL_1, SECTIONS_HTML as S1
from manual_02_dossier_technique     import MANUAL_2, SECTIONS_HTML as S2
from manual_03_gradation             import MANUAL_3, SECTIONS_HTML as S3
from manual_04_moulage               import MANUAL_4, SECTIONS_HTML as S4
from manual_05_ost                   import MANUAL_5, SECTIONS_HTML as S5
from manual_06_technologie_machines  import MANUAL_6, SECTIONS_HTML as S6
from manual_07_technologie_textile   import MANUAL_7, SECTIONS_HTML as S7
from manual_08_protection_consommateur import MANUAL_8, SECTIONS_HTML as S8
from manual_09_entrepreneuriat       import MANUAL_9, SECTIONS_HTML as S9

MANUALS = [
    (MANUAL_1, S1, "01_couture_dame_tailleur_dames"),
    (MANUAL_2, S2, "02_dossier_technique"),
    (MANUAL_3, S3, "03_gradation"),
    (MANUAL_4, S4, "04_moulage"),
    (MANUAL_5, S5, "05_ost"),
    (MANUAL_6, S6, "06_technologie_machines"),
    (MANUAL_7, S7, "07_technologie_textile"),
    (MANUAL_8, S8, "08_protection_consommateur"),
    (MANUAL_9, S9, "09_entrepreneuriat"),
]

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output_builds")


def build_one(manual_meta, sections_html, filename):
    """Assemble one manual's HTML file."""
    body = "\n".join(sections_html)
    html = build_manual_html(
        module_num       = manual_meta["module_num"],
        module_num_label = manual_meta["module_num_label"],
        title_ar         = manual_meta["title_ar"],
        title_fr         = manual_meta["title_fr"],
        toc_items        = manual_meta["toc_items"],
        body_sections_html = body,
        closing_ar       = manual_meta["closing_ar"],
        closing_fr       = manual_meta["closing_fr"],
        year             = "2025 / 2026",
    )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, filename + ".html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ Generated: {out_path}  ({len(html)//1024} KB)")
    return out_path


def main():
    print("=" * 70)
    print("  GENERATING 9 ALGERIAN VOCATIONAL EDUCATION MANUALS")
    print("  Author: Wa3il Fatiha / وائل فتيحة")
    print("  Output: " + OUTPUT_DIR)
    print("=" * 70)

    paths = []
    for meta, secs, fname in MANUALS:
        p = build_one(meta, secs, fname)
        paths.append(p)

    print()
    print("=" * 70)
    print(f"  ✓ ALL {len(paths)} HTML FILES GENERATED SUCCESSFULLY")
    print(f"  → Output directory: {OUTPUT_DIR}")
    print("=" * 70)

    # Summary table
    print()
    print(f"  {'File':<40} {'Size':<10}")
    print(f"  {'-'*40:<40} {'-'*10:<10}")
    total_kb = 0
    for p in paths:
        size_kb = os.path.getsize(p) // 1024
        total_kb += size_kb
        print(f"  {os.path.basename(p):<40} {size_kb:<10} KB")
    print(f"  {'-'*40:<40} {'-'*10:<10}")
    print(f"  {'TOTAL':<40} {total_kb:<10} KB")

    return paths


if __name__ == "__main__":
    main()