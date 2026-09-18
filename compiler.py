import hashlib, json, shutil
from pathlib import Path
from core.validate import validate
from core import svg
from generators.html import render as render_html
from generators.pdf import render_pdf

ROOT=Path(__file__).parent
SOURCE=ROOT/"source"/"report.json"
OUTPUT=ROOT/"output"

def sha256_bytes(data: bytes)->str:
    return hashlib.sha256(data).hexdigest()

def load_source(path=SOURCE):
    data=json.loads(path.read_text(encoding="utf-8")); validate(data); return data

def generate_artifact(a):
    typ=a["type"]
    if typ=="chart":
        return {"bar":svg.bar_chart,"line":svg.line_chart,"donut":svg.donut_chart}[a["kind"]](a)
    if typ=="diagram": return svg.diagram(a)
    raise ValueError(f"Unsupported visual artifact: {typ}")

def build(source_path=SOURCE, output=OUTPUT):
    report=load_source(source_path)
    if output.exists(): shutil.rmtree(output)
    visuals=output/"artifacts"; visuals.mkdir(parents=True)
    artifact_html={}
    manifest={"report_id":report["id"],"source_sha256":sha256_bytes(Path(source_path).read_bytes()),"artifacts":[]}
    for a in report["artifacts"]:
        content=generate_artifact(a)
        path=visuals/f'{a["id"]}.svg'; path.write_text(content,encoding="utf-8")
        artifact_html[a["id"]]=f'<div class="artifact visual">{content}</div>'
        manifest["artifacts"].append({"id":a["id"],"type":a["type"],"path":str(path.relative_to(output)),"sha256":sha256_bytes(path.read_bytes())})
    html=render_html(report,artifact_html)
    html_path=output/"report.html"; html_path.write_text(html,encoding="utf-8")
    manifest["html"]={"path":"report.html","sha256":sha256_bytes(html_path.read_bytes())}
    pdf_path=output/"report.pdf"
    manifest["pdf"]={"path":"report.pdf","generated":render_pdf(html_path,pdf_path)}
    if pdf_path.exists(): manifest["pdf"]["sha256"]=sha256_bytes(pdf_path.read_bytes())
    py_path=output/"report_data.py"
    py_path.write_text("# Generated from source/report.json\nREPORT_DATA = "+repr(report)+"\n",encoding="utf-8")
    manifest["python"]={"path":"report_data.py","sha256":sha256_bytes(py_path.read_bytes())}
    manifest_path=output/"manifest.json"; manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    return manifest

if __name__=="__main__":
    print(json.dumps(build(),indent=2,ensure_ascii=False))
