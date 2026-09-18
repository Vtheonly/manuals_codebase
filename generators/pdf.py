from pathlib import Path

def render_pdf(html_path: Path, pdf_path: Path) -> bool:
    try:
        from weasyprint import HTML
        HTML(filename=str(html_path)).write_pdf(str(pdf_path))
        return True
    except Exception:
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import A4
            c=canvas.Canvas(str(pdf_path),pagesize=A4)
            c.setFont("Helvetica",10)
            c.drawString(40,800,"PDF renderer fallback: install weasyprint for HTML/CSS fidelity.")
            c.drawString(40,780,f"Source: {html_path.name}")
            c.save()
            return True
        except Exception:
            return False
