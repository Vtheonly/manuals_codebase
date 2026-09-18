"""
generators/pdf.py — High-Fidelity PDF Exporter
Uses Headless Chromium / Playwright or WeasyPrint to guarantee exact A4 CSS rendering.
"""
import subprocess
import shutil
from pathlib import Path

def render_pdf(html_path: Path, pdf_path: Path) -> bool:
    html_path = Path(html_path).resolve()
    pdf_path = Path(pdf_path).resolve()

    # الخيار 1: استخدام WeasyPrint إذا كان مثبتاً
    try:
        from weasyprint import HTML
        HTML(filename=str(html_path)).write_pdf(str(pdf_path))
        return True
    except ImportError:
        pass
    except Exception as e:
        print(f"WeasyPrint error: {e}")

    # الخيار 2: استخدام متصفح Chrome / Chromium المدمج (طباعة مطبعية نقية بدون هوامش متصفح)
    browsers = ["google-chrome", "chromium", "chromium-browser", "msedge"]
    chrome_bin = next((shutil.which(b) for b in browsers if shutil.which(b)), None)
    
    if chrome_bin:
        cmd = [
            chrome_bin,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            str(html_path)
        ]
        res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if res.returncode == 0 and pdf_path.exists():
            return True

    # الخيار 3: استخدام Playwright عبر Node.js
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(html_path.as_uri(), wait_until="networkidle")
            page.pdf(
                path=str(pdf_path),
                format="A4",
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
            )
            browser.close()
            return True
    except Exception:
        pass

    return False