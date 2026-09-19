"""HTML-to-PDF adapters with layout measurement and metadata stamping.

Rendering order:
1. Playwright-driven Chromium (best fidelity, supports local @font-face, CSS
   page size, and — uniquely — JavaScript layout measurement)
2. Standalone Chromium / Chrome headless (PDF only)
3. WeasyPrint fallback (PDF only)

The Playwright backend doubles as the **layout measurement engine**: it loads
the document, waits for fonts, and reports per-sheet content geometry (content
box height, per-block heights, flex gap) so the compiler can paginate with
real rendered numbers instead of trusting hand-authored page budgets. This is
what guarantees the PDF is produced by the exact same Blink layout that was
measured — HTML and PDF cannot diverge.

After rendering, document-level metadata (title, author, subject, keywords)
supplied by the JSON input is stamped onto the PDF generically with pypdf.
"""
from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class RenderResult:
    generated: bool = False
    backend: str = ""
    measurements: list[dict[str, Any]] = field(default_factory=list)


_MEASURE_JS = """
() => Array.from(document.querySelectorAll('.page-sheet')).map(sheet => {
  const token = sheet.getAttribute('data-page-token');
  const content = sheet.querySelector('.page-content');
  if (!content) return {token: token, measured: false};
  const blocks = Array.from(content.children);
  const style = getComputedStyle(content);
  const blockData = blocks.map(b => {
    const r = b.getBoundingClientRect();
    const cs = getComputedStyle(b);
    const outer = r.height + (parseFloat(cs.marginTop) || 0) + (parseFloat(cs.marginBottom) || 0);
    // Table detail: needed for row-boundary splitting of long tables.
    let tableDetail = null;
    if (b.classList && b.classList.contains('table-wrapper')) {
      const table = b.querySelector('table.standard-table');
      if (table) {
        const thead = table.querySelector('thead');
        const rows = Array.from(table.querySelectorAll('tbody tr'));
        const titleEl = b.querySelector('.table-header');
        const capEl = b.querySelector('.caption');
        const rr = table.getBoundingClientRect();
        tableDetail = {
          marginTop: parseFloat(cs.marginTop) || 0,
          marginBottom: parseFloat(cs.marginBottom) || 0,
          titleHeight: titleEl ? titleEl.getBoundingClientRect().height : 0,
          headerHeight: thead ? thead.getBoundingClientRect().height : 0,
          captionHeight: capEl ? capEl.getBoundingClientRect().height : 0,
          rowHeights: rows.map(row => row.getBoundingClientRect().height),
        };
      }
    }
    return {outer: outer, tableDetail: tableDetail};
  });
  return {
    token: token,
    measured: true,
    contentClient: content.clientHeight,
    contentScroll: content.scrollHeight,
    blockHeights: blockData.map(d => d.outer),
    tableDetails: blockData.map(d => d.tableDetail),
    gap: parseFloat(style.rowGap || '0') || 0,
  };
})
"""


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


def _render_with_playwright(
    html_path: Path, pdf_path: Path | None
) -> RenderResult:
    result = RenderResult()
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            page.goto(html_path.as_uri(), wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(250)
            # Measure real rendered geometry with the same engine that prints.
            result.measurements = page.evaluate(_MEASURE_JS)
            if pdf_path is not None:
                page.pdf(
                    path=str(pdf_path),
                    format="A4",
                    print_background=True,
                    prefer_css_page_size=True,
                    margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
                )
            browser.close()
        result.backend = "playwright-chromium"
        result.generated = pdf_path is None or pdf_path.exists()
        return result
    except Exception:
        return result


def _render_with_chromium(html_path: Path, pdf_path: Path) -> RenderResult:
    result = RenderResult(backend="chromium-headless")
    browsers = ("google-chrome", "chromium", "chromium-browser", "msedge")
    browser = next((shutil.which(name) for name in browsers if shutil.which(name)), None)
    if not browser:
        return result
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
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
        result.generated = completed.returncode == 0 and pdf_path.exists()
    except OSError:
        pass
    return result


def _render_with_weasyprint(html_path: Path, pdf_path: Path) -> RenderResult:
    result = RenderResult(backend="weasyprint")
    try:
        from weasyprint import HTML

        HTML(filename=str(html_path)).write_pdf(str(pdf_path))
        result.generated = pdf_path.exists()
    except ImportError:
        pass
    except Exception as exc:
        print(f"WeasyPrint error: {exc}")
    return result


def render_document(
    html_path: Path | str,
    pdf_path: Path | str | None = None,
    metadata: dict[str, Any] | None = None,
) -> RenderResult:
    """Render (and optionally export) a document with the best backend.

    Always prefers Playwright because it is the only backend that can also
    measure the laid-out geometry, which the compiler needs for overflow-safe
    pagination. Returns a ``RenderResult`` with measurements included.
    """
    html_path = Path(html_path).resolve()
    pdf_path = Path(pdf_path).resolve() if pdf_path is not None else None

    if pdf_path is not None:
        pdf_path.parent.mkdir(parents=True, exist_ok=True)

    result = _render_with_playwright(html_path, pdf_path)
    if result.backend:
        if result.generated:
            _apply_metadata(pdf_path, metadata)
        return result

    if pdf_path is None:
        return RenderResult(backend="unavailable")

    for adapter in (_render_with_chromium, _render_with_weasyprint):
        attempt = adapter(html_path, pdf_path)
        if attempt.generated:
            _apply_metadata(pdf_path, metadata)
            return attempt

    return RenderResult(backend="unavailable")


def render_pdf(html_path: Path | str, pdf_path: Path | str, metadata: dict[str, Any] | None = None) -> bool:
    """Backward-compatible boolean wrapper around :func:`render_document`."""
    outcome = render_document(html_path, pdf_path, metadata)
    return outcome.generated
