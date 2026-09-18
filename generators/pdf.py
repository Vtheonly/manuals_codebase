"""Optional HTML-to-PDF adapters."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def render_pdf(html_path: Path, pdf_path: Path) -> bool:
    html_path = Path(html_path).resolve()
    pdf_path = Path(pdf_path).resolve()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        from weasyprint import HTML
        HTML(filename=str(html_path)).write_pdf(str(pdf_path))
        return pdf_path.exists()
    except ImportError:
        pass
    except Exception as exc:
        print(f"WeasyPrint error: {exc}")

    browsers = ("google-chrome", "chromium", "chromium-browser", "msedge")
    browser = next((shutil.which(name) for name in browsers if shutil.which(name)), None)
    if browser:
        command = [
            browser,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            str(html_path),
        ]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=False)
            if result.returncode == 0 and pdf_path.exists():
                return True
        except OSError:
            pass

    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as playwright:
            browser_instance = playwright.chromium.launch()
            page = browser_instance.new_page()
            page.goto(html_path.as_uri(), wait_until="networkidle")
            page.pdf(
                path=str(pdf_path),
                format="A4",
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            )
            browser_instance.close()
            return pdf_path.exists()
    except Exception:
        return False
