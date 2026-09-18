import html
from core.design import DESIGN

def text_block(block: dict) -> str:
    role=block.get("role","body")
    tag={"title":"h1","heading":"h2","subheading":"h3","body":"p","quote":"blockquote"}.get(role,"p")
    return f'<{tag} class="text text-{html.escape(role)}">{html.escape(block.get("text",""))}</{tag}>'

def table(block: dict) -> str:
    head="".join(f"<th>{html.escape(str(x))}</th>" for x in block["columns"])
    rows="".join("<tr>"+"".join(f"<td>{html.escape(str(x))}</td>" for x in row)+"</tr>" for row in block["rows"])
    return f'<section class="artifact table"><h3>{html.escape(block["title"])}</h3><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></section>'

def callout(block: dict) -> str:
    variant=html.escape(block.get("variant","info"))
    return f'<aside class="artifact callout callout-{variant}"><strong>{html.escape(block["title"])}</strong><div>{html.escape(block["content"])}</div></aside>'

def render_block(block: dict) -> str:
    kind=block.get("type")
    if kind=="text": return text_block(block)
    if kind=="table": return table(block)
    if kind=="callout": return callout(block)
    raise ValueError(f"Unsupported block type: {kind}")

def section(section: dict, artifact_html: dict) -> str:
    body=[]
    for index, block in enumerate(section.get("blocks", []), 1):
        if block.get("type")=="artifact_ref":
            body.append(artifact_html[block["artifact_id"]])
        else:
            body.append(artifact_html[f'{section["id"]}-block-{index}'])
    return f'<section class="report-section" id="{html.escape(section["id"])}"><h2>{html.escape(section["title"])}</h2>{"".join(body)}</section>'
