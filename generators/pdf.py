"""Optional HTML-to-PDF adapters with metadata stamping.

Rendering order:
1. Playwright-driven Chromium (best fidelity, supports local @font-face, CSS page size)
2. Standalone Chromium / Chrome headless
3. WeasyPrint fallback

After rendering, document-level metadata (title, author, subject, keywords)
supplied by the JSON input is stamped onto the PDF generically with pypdf.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Any


def _apply_metadata(pdf_path: Path, metadata: dict[str, Any] | None) -> None:
    if not metadata or not pdf_path.exists():
        return
    try:
        from pypdf import PdfReader, PdfWriter

        reader = PdfReader(str(pdf_path))
        writer = PdfWriter()
        writer.append(reader)
        info = {k: str(v) for k, v in metadata.items() if isinstance(v, (str, int))}
        if info:
            writer.add_metadata({f"/{k}": v for k, v in info.items()})
            with open(pdf_path, "wb") as handle:
                writer.write(handle)
    except Exception:
        pass


def _render_with_playwright(html_path: Path, pdf_path: Path) -> bool:
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            page.goto(html_path.as_uri(), wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(250)
            page.pdf(
                path=str(pdf_path),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            )
            browser.close()
            return pdf_path.exists()
    except Exception:
        return False


def _render_with_chromium(html_path: Path, pdf_path: Path) -> bool:
    browsers = ("google-chrome", "chromium", "chromium-browser", "msedge")
    browser = next((shutil.which(name) for name in browsers if shutil.which(name)), None)
    if not browser:
        return False
    command = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=2000",
        f"--print-to-pdf={pdf_path}",
        str(html_path),
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return result.returncode == 0 and pdf_path.exists()
    except OSError:
        return False


def _render_with_weasyprint(html_path: Path, pdf_path: Path) -> bool:
    try:
        from weasyprint import HTML

        HTML(filename=str(html_path)).write_pdf(str(pdf_path))
        return pdf_path.exists()
    except ImportError:
        return False
    except Exception as exc:
        print(f"WeasyPrint error: {exc}")
        return False


def render_pdf(html_path: Path, pdf_path: Path, metadata: dict[str, Any] | None = None) -> bool:
    html_path = Path(html_path).resolve()
    pdf_path = Path(pdf_path).resolve()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    for adapter in (_render_with_playwright, _render_with_chromium, _render_with_weasyprint):
        if adapter(html_path, pdf_path):
            _apply_metadata(pdf_path, metadata)
            return True

    return False
