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
    assert 'class="subsection-header"' in rendered

    svg = (output / "artifacts" / "multi.svg").read_text(encoding="utf-8")
    assert svg.count("<polyline") == 3
    assert svg.count('class="svg-viewport"') == 1
    assert 'direction:ltr !important' in svg

    assert manifest["outputs"]["html"]["path"] == "styled.html"

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
