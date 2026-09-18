"""Generic JSON -> artifact compilation pipeline."""
from __future__ import annotations

import hashlib
import json
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from core import svg
from core.components import render_block
from core.design import DesignSystem
from core.validate import validate
from generators.html import render as render_html
from generators.pdf import render_pdf


ENGINE_VERSION = "2.0.0"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_source(path: str | Path) -> dict[str, Any]:
    source_path = Path(path)
    data = json.loads(source_path.read_text(encoding="utf-8"))
    validate(data)
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


def build(source_path: str | Path, output_dir: str | Path) -> dict[str, Any]:
    source_path = Path(source_path).resolve()
    output_dir = Path(output_dir).resolve()
    document = load_source(source_path)
    design = DesignSystem.from_mapping(document.get("theme"))

    if output_dir.exists():
        shutil.rmtree(output_dir)
    artifact_dir = output_dir / "artifacts"
    artifact_dir.mkdir(parents=True)

    artifact_html: dict[str, str] = {}
    block_html: dict[str, str] = {}
    manifest: dict[str, Any] = {
        "engine_version": ENGINE_VERSION,
        "document_id": document["id"],
        "source": source_path.name,
        "source_sha256": sha256_bytes(source_path.read_bytes()),
        "artifacts": [],
        "outputs": {},
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

    for page_index, page in enumerate(document["pages"], start=1):
        page_token = str(page.get("id", page_index))
        for block_index, block in enumerate(page.get("blocks", []), start=1):
            if block.get("type") == "artifact_ref":
                continue
            block_id = f"page-{page_token}-block-{block_index}"
            rendered = render_content_block(block, design, artifact_html)
            block_path = artifact_dir / f"{block_id}.html"
            block_path.write_text(rendered, encoding="utf-8")
            block_html[block_id] = rendered
            manifest["artifacts"].append(
                {
                    "id": block_id,
                    "type": block["type"],
                    "path": str(block_path.relative_to(output_dir)),
                    "sha256": sha256_bytes(block_path.read_bytes()),
                }
            )

    html_output = render_html(document, artifact_html, block_html, design)
    html_path = output_dir / f"{source_path.stem}.html"
    html_path.write_text(html_output, encoding="utf-8")
    manifest["outputs"]["html"] = {
        "path": str(html_path.relative_to(output_dir)),
        "sha256": sha256_bytes(html_path.read_bytes()),
    }

    pdf_path = output_dir / f"{source_path.stem}.pdf"
    generated = render_pdf(html_path, pdf_path)
    manifest["outputs"]["pdf"] = {
        "path": str(pdf_path.relative_to(output_dir)),
        "generated": generated,
    }
    if pdf_path.exists():
        manifest["outputs"]["pdf"]["sha256"] = sha256_bytes(pdf_path.read_bytes())

    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return manifest
