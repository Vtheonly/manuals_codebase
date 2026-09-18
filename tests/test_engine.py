import json
from pathlib import Path
from compiler import load_source, build

def test_source_validates():
    report=load_source()
    assert report["id"]

def test_build_creates_individual_artifacts(tmp_path):
    manifest=build(output=tmp_path)
    assert (tmp_path/"report.html").exists()
    assert (tmp_path/"report_data.py").exists()
    assert (tmp_path/"manifest.json").exists()
    assert len(manifest["artifacts"]) == 4
    for a in manifest["artifacts"]:
        assert (tmp_path/a["path"]).exists()
