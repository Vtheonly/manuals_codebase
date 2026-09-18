import html
from core.design import DESIGN

def text_block(block: dict) -> str:
    p=DESIGN.palette; t=block.get("text",""); role=block.get("role","body")
    tag={"title":"h1","heading":"h2","subheading":"h3","body":"p","quote":"blockquote"}.get(role,"p")
    cls=f"text text-{role}"
    return f'<{tag} class="{cls}">{html.escape(t)}</{tag}>'

def table(block: dict) -> str:
    p=DESIGN.palette
    head="".join(f"<th>{html.escape(str(x))}</th>" for x in block["columns"])
    rows="".join("<tr>"+"".join(f"<td>{html.escape(str(x))}</td>" for x in row)+"</tr>" for row in block["rows"])
    return f'<section class="artifact table"><h3>{html.escape(block["title"])}</h3><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></section>'

def callout(block: dict) -> str:
    return f'<aside class="artifact callout callout-{html.escape(block.get("variant","info"))}"><strong>{html.escape(block["title"])}</strong><div>{html.escape(block["content"])}</div></aside>'

def section(section: dict, artifact_html: dict) -> str:
    body=[]
    for block in section.get("blocks",[]):
        kind=block.get("type")
        if kind=="text": body.append(text_block(block))
        elif kind=="table": body.append(table(block))
        elif kind=="callout": body.append(callout(block))
        elif kind=="artifact_ref": body.append(artifact_html.get(block["artifact_id"],""))
    return f'<section class="report-section" id="{html.escape(section["id"])}"><h2>{html.escape(section["title"])}</h2>{"".join(body)}</section>'
