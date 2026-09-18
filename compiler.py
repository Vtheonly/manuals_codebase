import hashlib, json, shutil
from pathlib import Path
from core.validate import validate
from core import svg
from core.components import render_block
from generators.html import render as render_html
from generators.pdf import render_pdf

ROOT=Path(__file__).parent
SOURCE=ROOT/"source"/"report.json"
OUTPUT=ROOT/"output"
GENERATOR_VERSION="1.0.0"

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load_source(path=SOURCE):
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    validate(data)
    return data


# عدل دالة generate_visual في compiler.py:
def generate_visual(a: dict) -> str:
    if a["type"] == "chart":
        renderer = {
            "bar": svg.bar_chart,
            "line": svg.line_chart,
            "donut": svg.donut_chart,
            "progress": svg.progress_chart
        }.get(a["kind"])
        if renderer is None: raise ValueError(f"Unsupported chart kind: {a['kind']}")
        return renderer(a)
    if a["type"] == "diagram": return svg.diagram(a)
    raise ValueError(f"Unsupported visual artifact: {a['type']}")

def build(source_path=SOURCE, output=OUTPUT):
    source_path=Path(source_path); output=Path(output)
    report=load_source(source_path)
    if output.exists(): shutil.rmtree(output)
    artifact_dir=output/"artifacts"; artifact_dir.mkdir(parents=True)
    artifact_html={}
    manifest={"generator_version":GENERATOR_VERSION,"report_id":report["id"],
              "source_sha256":sha256_bytes(source_path.read_bytes()),"artifacts":[]}

    # Every source-defined visual artifact is rendered independently.
    for spec in report["artifacts"]:
        content=generate_visual(spec)
        path=artifact_dir/f'{spec["id"]}.svg'
        path.write_text(content,encoding="utf-8")
        artifact_html[spec["id"]]=f'<div class="artifact visual">{content}</div>'
        manifest["artifacts"].append({"id":spec["id"],"type":spec["type"],
            "path":str(path.relative_to(output)),"sha256":sha256_bytes(path.read_bytes())})

    # Every content block is also materialized independently.
    for section in report["sections"]:
        for index, block in enumerate(section.get("blocks",[]),1):
            if block.get("type")=="artifact_ref": continue
            artifact_id=f'{section["id"]}-block-{index}'
            content=render_block(block)
            path=artifact_dir/f"{artifact_id}.html"
            path.write_text(content,encoding="utf-8")
            artifact_html[artifact_id]=content
            manifest["artifacts"].append({"id":artifact_id,"type":block["type"],
                "path":str(path.relative_to(output)),"sha256":sha256_bytes(path.read_bytes())})

    html=render_html(report,artifact_html)
    html_path=output/"report.html"; html_path.write_text(html,encoding="utf-8")
    manifest["html"]={"path":"report.html","sha256":sha256_bytes(html_path.read_bytes())}

    pdf_path=output/"report.pdf"
    generated=render_pdf(html_path,pdf_path)
    manifest["pdf"]={"path":"report.pdf","generated":generated}
    if pdf_path.exists(): manifest["pdf"]["sha256"]=sha256_bytes(pdf_path.read_bytes())

    py_path=output/"report_data.py"
    py_path.write_text("# Generated from source/report.json\nREPORT_DATA = "+repr(report)+"\n",encoding="utf-8")
    manifest["python"]={"path":"report_data.py","sha256":sha256_bytes(py_path.read_bytes())}

    manifest_path=output/"manifest.json"
    manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    return manifest

if __name__=="__main__":
    print(json.dumps(build(),indent=2,ensure_ascii=False))
