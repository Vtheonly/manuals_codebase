from core.design import DESIGN
from core.components import section

def stylesheet() -> str:
    d=DESIGN; p=d.palette; ty=d.typography; s=d.spacing; b=d.borders
    return f"""*{{box-sizing:border-box}}@page{{size:A4;margin:0}}body{{margin:0;background:#e2e8f0;color:{p.text};font-family:{ty.arabic};direction:rtl}}.page{{width:{d.page.width};min-height:{d.page.height};margin:0 auto 18px;background:{p.surface};padding:{s.page_y} {s.page_x};page-break-after:always}}h1{{font-size:{ty.sizes["3xl"]};color:{p.primary_deep};margin:0 0 {s.lg}}}h2{{font-size:{ty.sizes["xl"]};color:{p.primary_deep};border-bottom:2px solid {p.primary};padding-bottom:6px;margin:0 0 {s.md}}}h3{{font-size:{ty.sizes["md"]};color:{p.primary_deep}}}.text{{line-height:{ty.line_height["normal"]};margin:0 0 {s.md}}}.text-quote{{border-right:4px solid {p.accent};background:{p.accent_light};padding:{s.md};font-style:italic}}.artifact{{margin:{s.md} 0}}.table{{overflow:hidden;border:1px solid {p.border_light};border-radius:{b.md}}}table{{width:100%;border-collapse:collapse}}th{{background:{p.primary};color:white;padding:{s.cell};text-align:right}}td{{padding:{s.cell};border:1px solid {p.border_light}}}tbody tr:nth-child(even){{background:{p.surface_alt}}}.callout{{padding:{s.card};border-right:4px solid {p.primary};background:{p.primary_light};border-radius:{b.md}}}.callout-warning{{border-color:{p.accent};background:{p.accent_light}}}.artifact svg{{width:100%;height:auto}}.cover{{display:flex;flex-direction:column;justify-content:center;text-align:center;border:2px solid {p.primary};padding:30mm}}.meta{{color:{p.muted};font-size:{ty.sizes["sm"]}}}@media print{{body{{background:white}}.page{{margin:0;box-shadow:none}}}}"""

def render(report: dict, artifact_html: dict) -> str:
    pages=[f'<main class="page cover"><h1>{report["title"]}</h1><p class="meta">{report["metadata"].get("subtitle","")}</p></main>']
    for s in report["sections"]:
        pages.append(f'<main class="page">{section(s,artifact_html)}</main>')
    return "<!doctype html><html lang=""+report.get("language","ar")+"" dir="rtl"><head><meta charset="utf-8"><title>"+report["title"]+"</title><style>"+stylesheet()+"</style></head><body>"+"".join(pages)+"</body></html>"
