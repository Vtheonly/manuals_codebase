"""Generic JSON -> artifact compilation pipeline."""
from __future__ import annotations

import hashlib
import json
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from core import paginate, svg
from core.components import render_block
from core.design import DesignSystem
from core.normalize import normalize_document_spec
from core.text import document_integrity_report
from core.validate import validate
from generators.html import FONT_FACES, render as render_html
from generators.pdf import render_document


ENGINE_VERSION = "4.0.0"
ASSETS_DIR = Path(__file__).resolve().parent / "assets"

# Measured-layout passes: 1 fit check + spill correction rounds (content
# chains can cascade forward through several pages before converging).
MAX_LAYOUT_PASSES = 20


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def copy_font_assets(output_dir: Path) -> bool:
    """Copy the bundled font library next to the generated HTML so that
    @font-face relative URLs resolve identically for every PDF backend."""
    source = ASSETS_DIR / "fonts"
    if not source.is_dir():
        return False
    target = output_dir / "fonts"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)
    return True


def copy_image_assets(source_path: Path, output_dir: Path) -> bool:
    """Copy image assets from source/images and assets/images into the output build folder."""
    copied = False

    src_images = source_path.parent / "images"
    if src_images.is_dir():
        target = output_dir / "images"
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(src_images, target)
        copied = True

    assets_images = ASSETS_DIR / "images"
    if assets_images.is_dir():
        target = output_dir / "images"
        target.mkdir(parents=True, exist_ok=True)
        for item in assets_images.glob("*"):
            dest = target / item.name
            if item.is_file():
                shutil.copy2(item, dest)
            elif item.is_dir():
                shutil.copytree(item, dest, dirs_exist_ok=True)
        copied = True
    return copied

def load_source(path: str | Path) -> dict[str, Any]:
    source_path = Path(path)
    data = json.loads(source_path.read_text(encoding="utf-8"))
    # 1) Canonicalize the data contract (NFC + chart aliases + numerics).
    data = normalize_document_spec(data)
    # 2) Strict schema contract — fails fast on ghost charts, TOC starvation,
    #    unknown references, malformed blocks.
    validate(data)
    # 3) Arabic joining-integrity lint — fails fast on unambiguous corruption
    #    so broken text is repaired in the source data, never guessed at
    #    render time.
    integrity = document_integrity_report(data)
    if integrity:
        details = "; ".join(
            f"{entry['path']}: {'; '.join(entry['problems'])}" for entry in integrity[:5]
        )
        more = "" if len(integrity) <= 5 else f" (+{len(integrity) - 5} more)"
        raise ValueError(
            "Arabic text integrity problems detected (fix the source JSON):\n"
            f"{details}{more}"
        )
    return data


def generate_visual(spec: dict[str, Any], design: DesignSystem) -> str:
    if spec["type"] == "chart":
        renderer = {
            "bar": svg.bar_chart,
            "line": svg.line_chart,
            "donut": svg.donut_chart,
            "progress": svg.progress_chart,
        }.get(spec["kind"])
        if renderer is None:
            raise ValueError(f"Unsupported chart kind: {spec['kind']}")
        return renderer(spec, design)
    if spec["type"] == "diagram":
        return svg.diagram(spec, design)
    raise ValueError(f"Unsupported visual artifact type: {spec['type']}")


def render_content_block(
    block: dict[str, Any],
    design: DesignSystem,
    artifact_html: dict[str, str],
) -> str:
    kind = block.get("type")
    if kind == "artifact_ref":
        return artifact_html[block["artifact_id"]]

    if kind == "group":
        resolved = deepcopy(block)
        resolved["_rendered_children"] = [
            render_content_block(child, design, artifact_html)
            for child in block.get("children", [])
        ]
        return render_block(resolved, design)

    return render_block(block, design)


def render_block_map(
    document: dict[str, Any],
    design: DesignSystem,
    artifact_html: dict[str, str],
    output_dir: Path | None = None,
) -> dict[str, str]:
    """Render every block of every page; optionally persist block artifacts."""
    block_html: dict[str, str] = {}
    for page_index, page in enumerate(document["pages"], start=1):
        page_token = str(page.get("id", page_index))
        for block_index, block in enumerate(page.get("blocks", []), start=1):
            if block.get("type") == "artifact_ref":
                continue
            block_id = f"page-{page_token}-block-{block_index}"
            rendered = render_content_block(block, design, artifact_html)
            if output_dir is not None:
                block_path = output_dir / "artifacts" / f"{block_id}.html"
                block_path.write_text(rendered, encoding="utf-8")
            block_html[block_id] = rendered
    return block_html


def build(source_path: str | Path, output_dir: str | Path) -> dict[str, Any]:
    source_path = Path(source_path).resolve()
    output_dir = Path(output_dir).resolve()
    document = load_source(source_path)
    design = DesignSystem.from_mapping(document.get("theme"))

    if output_dir.exists():
        shutil.rmtree(output_dir)
    artifact_dir = output_dir / "artifacts"
    artifact_dir.mkdir(parents=True)
    copy_font_assets(output_dir)
    copy_image_assets(source_path, output_dir)

    # Every page gets a stable token so measurements survive reflow passes.
    for ordinal, page in enumerate(document["pages"], start=1):
        if "id" not in page:
            page["id"] = f"page-{ordinal}"

    artifact_html: dict[str, str] = {}
    manifest: dict[str, Any] = {
        "engine_version": ENGINE_VERSION,
        "document_id": document["id"],
        "source": source_path.name,
        "source_sha256": sha256_bytes(source_path.read_bytes()),
        "artifacts": [],
        "outputs": {},
        "pagination": {
            "mode": "measured",
            "passes": 0,
            "spills": [],
            "warnings": [],
        },
    }

    for spec in document["artifacts"]:
        rendered = generate_visual(spec, design)
        artifact_path = artifact_dir / f'{spec["id"]}.svg'
        artifact_path.write_text(rendered, encoding="utf-8")
        artifact_html[spec["id"]] = rendered
        manifest["artifacts"].append(
            {
                "id": spec["id"],
                "type": spec["type"],
                "kind": spec.get("kind"),
                "path": str(artifact_path.relative_to(output_dir)),
                "sha256": sha256_bytes(artifact_path.read_bytes()),
            }
        )

    # ---- Measured pagination loop -------------------------------------
    work = deepcopy(document)
    probe_path = output_dir / "_layout_probe.html"
    pagination = manifest["pagination"]

    for _ in range(MAX_LAYOUT_PASSES):
        block_html = render_block_map(work, design, artifact_html)
        probe_path.write_text(
            render_html(work, artifact_html, block_html, design), encoding="utf-8"
        )
        probe = render_document(probe_path)
        if not probe.backend or probe.backend == "unavailable":
            pagination["mode"] = "trust"
            pagination["warnings"].append(
                "No JavaScript-capable backend available: measured overflow "
                "protection disabled (install Playwright)."
            )
            break
        outcome = paginate.reflow(work, probe.measurements)
        pagination["passes"] += 1
        pagination["spills"].extend(outcome["spills"])
        pagination["warnings"].extend(outcome["warnings"])
        if not outcome["changed"]:
            break
    probe_path.unlink(missing_ok=True)

    # Resolve TOC page references against the final page ordinals.
    if paginate.resolve_toc_page_refs(work):
        pagination["warnings"].append("TOC page references resolved after reflow")

    # ---- Final render ---------------------------------------------------
    block_html = render_block_map(work, design, artifact_html, output_dir)
    for page_index, page in enumerate(work["pages"], start=1):
        page_token = str(page.get("id", page_index))
        for block_index, block in enumerate(page.get("blocks", []), start=1):
            if block.get("type") == "artifact_ref":
                continue
            block_id = f"page-{page_token}-block-{block_index}"
            manifest["artifacts"].append(
                {
                    "id": block_id,
                    "type": block["type"],
                    "path": str((artifact_dir / f"{block_id}.html").relative_to(output_dir)),
                    "sha256": sha256_bytes((artifact_dir / f"{block_id}.html").read_bytes()),
                }
            )

    html_output = render_html(work, artifact_html, block_html, design)
    html_path = output_dir / f"{source_path.stem}.html"
    html_path.write_text(html_output, encoding="utf-8")
    manifest["outputs"]["html"] = {
        "path": str(html_path.relative_to(output_dir)),
        "sha256": sha256_bytes(html_path.read_bytes()),
    }

    pdf_path = output_dir / f"{source_path.stem}.pdf"
    metadata = document.get("metadata") if isinstance(document.get("metadata"), dict) else {}
    result = render_document(html_path, pdf_path, metadata)
    manifest["outputs"]["pdf"] = {
        "path": str(pdf_path.relative_to(output_dir)),
        "generated": result.generated,
        "backend": result.backend,
    }
    if pdf_path.exists():
        manifest["outputs"]["pdf"]["sha256"] = sha256_bytes(pdf_path.read_bytes())

    # Final safety audit: report (never silently ignore) residual overflow.
    for issue in paginate.remaining_overflow(result.measurements):
        pagination["warnings"].append(f"residual overflow on page {issue['page']}")
    if pagination["warnings"]:
        print(f"[pagination] {source_path.stem}: " + " | ".join(pagination["warnings"]))

    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return manifest
