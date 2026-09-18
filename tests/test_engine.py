import json
from pathlib import Path

from compiler import build, load_source


def document(title: str, language: str, direction: str) -> dict:
    return {
        "id": f"test-{language}",
        "title": title,
        "language": language,
        "direction": direction,
        "theme": {"palette": {"primary": "#22577a", "accent": "#e09f3e"}},
        "pages": [
            {
                "id": "page-1",
                "layout": "framed",
                "footer": {"left": "External", "center": "{page}/{pages}", "right": "JSON"},
                "blocks": [
                    {"type": "heading", "level": 1, "badge": "1", "title": title, "subtitle": "External content"},
                    {"type": "text", "content": "This value came from the JSON input."},
                    {
                        "type": "group",
                        "layout": "row",
                        "children": [
                            {"type": "stats", "columns": 2, "items": [{"value": "42", "label": "Count"}, {"value": "91%", "label": "Rate"}]},
                            {"type": "table", "columns": ["Key", "Value"], "rows": [["A", "B"], ["C", "D"]]},
                            {"type": "artifact_ref", "artifact_id": "trend"},
                        ],
                    },
                ],
            }
        ],
        "artifacts": [
            {"id": "trend", "type": "chart", "kind": "line", "title": "Trend", "labels": ["One", "Two", "Three"], "values": [2, 4, 3]},
            {"id": "process", "type": "diagram", "kind": "flow", "title": "Process", "steps": [{"label": "Input"}, {"label": "Transform"}, {"label": "Output"}]},
        ],
    }


def test_source_is_validated(tmp_path):
    source = tmp_path / "input.json"
    source.write_text(json.dumps(document("Document A", "en", "ltr")), encoding="utf-8")
    assert load_source(source)["id"] == "test-en"


def test_same_engine_compiles_different_inputs(tmp_path):
    for language, direction, title in [("en", "ltr", "Financial Summary"), ("ar", "rtl", "دليل تشغيلي")]:
        source = tmp_path / f"{language}.json"
        output = tmp_path / f"out-{language}"
        source.write_text(json.dumps(document(title, language, direction)), encoding="utf-8")
        manifest = build(source, output)
        html = (output / f"{source.stem}.html").read_text(encoding="utf-8")

        assert (output / "manifest.json").exists()
        assert title in html
        assert len(manifest["artifacts"]) == 5
        assert not (output / "report_data.py").exists()


def test_high_fidelity_components_and_multi_series_chart(tmp_path):
    source_document = document("Styled", "ar", "rtl")
    source_document["pages"][0]["blocks"].extend([
        {"type": "subsection", "title": "Secondary Section", "subtitle": "Sous-section"},
        {
            "type": "formula",
            "title": "Reference Formula",
            "html_expression": "V<sub>x</sub> = (Δ / n) × k",
            "description": "Uses <strong>inline emphasis</strong> without escaping the markup.",
        },
        {"type": "text", "content": "A <strong>formatted</strong> sentence and <small>small text</small>."},
    ])
    source_document["artifacts"].append({
        "id": "multi",
        "type": "chart",
        "kind": "line",
        "title": "Multi-Series",
        "labels": ["A", "B", "C"],
        "series": [
            {"label": "First", "values": [1, 2, 3]},
            {"label": "Second", "values": [3, 2, 1]},
            {"label": "Third", "values": [2, 3, 2]},
        ],
    })
    source_document["pages"][0]["blocks"].append(
        {"type": "artifact_ref", "artifact_id": "multi"}
    )

    source = tmp_path / "styled.json"
    output = tmp_path / "styled-output"
    source.write_text(json.dumps(source_document, ensure_ascii=False), encoding="utf-8")
    manifest = build(source, output)

    rendered = (output / "styled.html").read_text(encoding="utf-8")
    assert "<strong>formatted</strong>" in rendered
    assert "<small>small text</small>" in rendered
    assert 'class="formula-math"' in rendered
    assert 'class="subsection-header sub-accent-bar"' in rendered

    svg = (output / "artifacts" / "multi.svg").read_text(encoding="utf-8")
    assert svg.count("<polyline") == 3
    assert svg.count('class="svg-viewport"') == 1
    assert 'direction:ltr !important' in svg

    assert manifest["outputs"]["html"]["path"] == "styled.html"


def test_divider_component_and_heading_rule(tmp_path):
    source_document = document("Rules", "ar", "rtl")
    source_document["pages"][0]["blocks"].extend([
        {"type": "divider", "variant": "section"},
        {"type": "divider", "variant": "dotted", "color": "accent", "margin": "lg"},
        {"type": "divider", "variant": "gradient", "start": "primary", "end": "accent"},
        {"type": "heading", "level": 2, "title": "No rule", "rule": False},
    ])
    source = tmp_path / "rules.json"
    output = tmp_path / "rules-out"
    source.write_text(json.dumps(source_document, ensure_ascii=False), encoding="utf-8")
    build(source, output)
    rendered = (output / "rules.html").read_text(encoding="utf-8")

    assert 'class="divider divider-section' in rendered
    assert 'class="divider divider-dotted' in rendered
    assert 'class="divider divider-gradient' in rendered
    # heading with rule disabled must not emit a divider
    no_rule_heading = rendered.split("No rule")[1][:400]
    assert "divider-section" not in no_rule_heading


def test_list_rows_variant_and_custom_spacer(tmp_path):
    source_document = document("Rows", "ar", "rtl")
    source_document["pages"][0]["blocks"].extend([
        {"type": "spacer", "height": "18pt"},
        {
            "type": "list",
            "variant": "rows",
            "items": [
                {"title": "One", "subtitle": "First item", "tag": "REF-1"},
                {"title": "Two", "subtitle": "Second item"},
            ],
        },
    ])
    source = tmp_path / "rows.json"
    output = tmp_path / "rows-out"
    source.write_text(json.dumps(source_document, ensure_ascii=False), encoding="utf-8")
    build(source, output)
    rendered = (output / "rows.html").read_text(encoding="utf-8")

    assert 'class="content-list list-rows"' in rendered
    assert 'class="list-row"' in rendered
    assert 'style="height:18pt"' in rendered


def test_color_scale_and_series_override(tmp_path):
    source_document = document("Scaled", "en", "ltr")
    source_document["artifacts"].extend([
        {
            "id": "scaled",
            "type": "chart",
            "kind": "progress",
            "title": "Ramp",
            "color_scale": ["#111111", "#eeeeee"],
            "items": [
                {"label": "A", "value": 1, "max": 4},
                {"label": "B", "value": 2, "max": 4},
                {"label": "C", "value": 3, "max": 4},
                {"label": "D", "value": 4, "max": 4},
            ],
        },
        {
            "id": "custom_colors",
            "type": "chart",
            "kind": "bar",
            "title": "Custom",
            "labels": ["X", "Y", "Z"],
            "values": [1, 2, 3],
            "colors": ["#123456", "#654321"],
        },
    ])
    source_document["pages"][0]["blocks"].extend([
        {"type": "artifact_ref", "artifact_id": "scaled"},
        {"type": "artifact_ref", "artifact_id": "custom_colors"},
    ])
    source = tmp_path / "scaled.json"
    output = tmp_path / "scaled-out"
    source.write_text(json.dumps(source_document, ensure_ascii=False), encoding="utf-8")
    build(source, output)

    scaled = (output / "artifacts" / "scaled.svg").read_text(encoding="utf-8")
    assert "#111111" in scaled and "#eeeeee" in scaled
    assert "#5b5b5b" in scaled  # interpolated middle color

    bars = (output / "artifacts" / "custom_colors.svg").read_text(encoding="utf-8")
    assert bars.count("#123456") >= 2  # cycles through the override list
    assert "#654321" in bars


def test_bundled_fonts_are_copied_and_referenced(tmp_path):
    source = tmp_path / "fonts.json"
    output = tmp_path / "fonts-out"
    source.write_text(json.dumps(document("Fonts", "ar", "rtl")), encoding="utf-8")
    build(source, output)
    html = (output / "fonts.html").read_text(encoding="utf-8")

    assert (output / "fonts" / "NotoKufiArabic-700.ttf").exists()
    assert "@font-face" in html
    assert "url('fonts/NotoKufiArabic-700.ttf')" in html
    assert "fonts.googleapis.com" not in html


def test_pdf_metadata_from_document(tmp_path):
    source_document = document("Meta", "ar", "rtl")
    source_document["metadata"] = {
        "Title": "Meta Report",
        "Author": "Engine Test",
        "Subject": "Metadata stamping",
    }
    source = tmp_path / "meta.json"
    output = tmp_path / "meta-out"
    source.write_text(json.dumps(source_document, ensure_ascii=False), encoding="utf-8")
    build(source, output)

    import fitz

    pdf_path = output / "meta.pdf"
    if pdf_path.exists():
        doc = fitz.open(pdf_path)
        assert doc.metadata.get("title") == "Meta Report"
        assert doc.metadata.get("author") == "Engine Test"


def test_batch_build(tmp_path, monkeypatch):
    from build import main
    input_dir = tmp_path / "inputs"
    output_dir = tmp_path / "outputs"
    input_dir.mkdir()

    for name in ("one", "two"):
        (input_dir / f"{name}.json").write_text(json.dumps(document(name, "en", "ltr")), encoding="utf-8")

    monkeypatch.setattr(
        "sys.argv",
        ["build.py", "--batch", str(input_dir), "--output", str(output_dir)],
    )
    assert main() == 0
    assert (output_dir / "one" / "one.html").exists()
    assert (output_dir / "two" / "two.html").exists()


def test_batch_json_file(tmp_path, monkeypatch):
    from build import main

    batch_source = tmp_path / "batch.json"
    output_dir = tmp_path / "batch-output"
    batch_source.write_text(
        json.dumps(
            {
                "documents": [
                    document("First", "en", "ltr"),
                    document("Second", "ar", "rtl"),
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        ["build.py", "--batch", str(batch_source), "--output", str(output_dir)],
    )
    assert main() == 0
    assert (output_dir / "001-test-en" / "batch-001-test-en.html").exists()
    assert (output_dir / "002-test-ar" / "batch-002-test-ar.html").exists()


def test_engine_contains_no_sample_domain_strings():
    root = Path(__file__).resolve().parents[1]
    targets = [root / "compiler.py", root / "build.py", root / "core", root / "generators"]
    forbidden = ("وزارة التكوين", "trainee_name", "training_season", "HTE1204", "Lectra Modaris")

    for target in targets:
        files = [target] if target.is_file() else list(target.rglob("*.py"))
        for file in files:
            content = file.read_text(encoding="utf-8")
            for token in forbidden:
                assert token not in content
