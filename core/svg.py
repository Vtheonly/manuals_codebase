import html
import math
from core.design import DESIGN

def esc(value: object) -> str:
    return html.escape(str(value), quote=True)

def shell(title: str, body: str, width: int, height: int) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">{body}</svg>'

def bar_chart(a: dict) -> str:
    p=DESIGN.palette; w,h=760,360; ml,mr,mt,mb=65,25,35,70
    vals=[float(x) for x in a["values"]]; mx=max(vals,default=1) or 1
    pw,ph=w-ml-mr,h-mt-mb; n=max(1,len(vals)); gap=pw/n*.2; bw=max(10,pw/n-gap)
    parts=[f'<text x="{w/2}" y="22" text-anchor="middle" font-family="Arial" font-weight="700" font-size="18" fill="{p.text_dark}">{esc(a["title"])}</text>']
    for i in range(5):
        y=mt+ph*i/4; val=mx*(1-i/4)
        parts += [f'<line x1="{ml}" y1="{y:.1f}" x2="{w-mr}" y2="{y:.1f}" stroke="{p.border_light}" stroke-dasharray="3 3"/>',
                  f'<text x="{ml-8}" y="{y+4:.1f}" text-anchor="end" font-size="10" fill="{p.muted}">{val:g}</text>']
    for i,(label,val) in enumerate(zip(a["labels"],vals)):
        x=ml+i*pw/n+(gap/2); bh=ph*val/mx; y=mt+ph-bh; color=p.series[i%len(p.series)]
        parts += [f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4" fill="{color}"/>',
                  f'<text x="{x+bw/2:.1f}" y="{y-6:.1f}" text-anchor="middle" font-size="10" font-weight="700" fill="{p.text_dark}">{val:g}</text>',
                  f'<text x="{x+bw/2:.1f}" y="{h-38}" text-anchor="middle" font-size="10" fill="{p.text}">{esc(label)}</text>']
    return shell(a["title"],"".join(parts),w,h)

def donut_chart(a: dict) -> str:
    p=DESIGN.palette; w,h=760,340; cx,cy,r=190,170,105
    vals=[float(x) for x in a["values"]]; total=sum(vals) or 1
    parts=[f'<text x="{w/2}" y="24" text-anchor="middle" font-family="Arial" font-weight="700" font-size="18" fill="{p.text_dark}">{esc(a["title"])}</text>']
    start=-math.pi/2
    for i,(label,val) in enumerate(zip(a["labels"],vals)):
        sweep=2*math.pi*val/total; end=start+sweep; large=int(sweep>math.pi)
        x1,y1=cx+r*math.cos(start),cy+r*math.sin(start); x2,y2=cx+r*math.cos(end),cy+r*math.sin(end)
        ri=62; x3,y3=cx+ri*math.cos(end),cy+ri*math.sin(end); x4,y4=cx+ri*math.cos(start),cy+ri*math.sin(start)
        color=p.series[i%len(p.series)]
        d=f"M{x1:.2f},{y1:.2f} A{r},{r} 0 {large} 1 {x2:.2f},{y2:.2f} L{x3:.2f},{y3:.2f} A{ri},{ri} 0 {large} 0 {x4:.2f},{y4:.2f} Z"
        parts.append(f'<path d="{d}" fill="{color}" stroke="{p.surface}" stroke-width="2"/>')
        ly=70+i*42; parts += [f'<rect x="390" y="{ly}" width="14" height="14" rx="3" fill="{color}"/>',
            f'<text x="414" y="{ly+12}" font-size="11" fill="{p.text}">{esc(label)} — {val/total*100:.1f}%</text>']
        start=end
    parts += [f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="24" font-weight="800" fill="{p.primary_deep}">{sum(vals):g}</text>']
    return shell(a["title"],"".join(parts),w,h)

def line_chart(a: dict) -> str:
    p=DESIGN.palette; w,h=760,360; ml,mr,mt,mb=65,25,35,65
    vals=[float(x) for x in a["values"]]; mx=max(vals,default=1) or 1; pw,ph=w-ml-mr,h-mt-mb
    pts=[]
    for i,v in enumerate(vals):
        x=ml+(pw*i/max(1,len(vals)-1)); y=mt+ph-(v/mx)*ph; pts.append((x,y))
    poly=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    parts=[f'<text x="{w/2}" y="22" text-anchor="middle" font-size="18" font-weight="700" fill="{p.text_dark}">{esc(a["title"])}</text>',
           f'<polyline points="{poly}" fill="none" stroke="{p.primary}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>']
    for x,y in pts: parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{p.accent}"/>')
    for i,label in enumerate(a["labels"]):
        x=ml+(pw*i/max(1,len(vals)-1)); parts.append(f'<text x="{x:.1f}" y="{h-30}" text-anchor="middle" font-size="10" fill="{p.text}">{esc(label)}</text>')
    return shell(a["title"],"".join(parts),w,h)

def diagram(a: dict) -> str:
    p=DESIGN.palette; w,h=760,220; n=len(a["nodes"]); gap=w/max(1,n)
    parts=[f'<text x="{w/2}" y="22" text-anchor="middle" font-size="18" font-weight="700" fill="{p.text_dark}">{esc(a["title"])}</text>']
    for u,v in a.get("edges",[]):
        x1=gap*(u+.5); x2=gap*(v+.5); y=125
        parts.append(f'<line x1="{x1+80}" y1="{y}" x2="{x2-80}" y2="{y}" stroke="{p.primary}" stroke-width="3" marker-end="url(#arrow)"/>')
    for i,node in enumerate(a["nodes"]):
        x=gap*(i+.5)-70
        parts.append(f'<rect x="{x:.1f}" y="90" width="140" height="70" rx="12" fill="{p.primary_light}" stroke="{p.primary}" stroke-width="2"/>')
        parts.append(f'<text x="{x+70:.1f}" y="132" text-anchor="middle" font-size="11" font-weight="700" fill="{p.text_dark}">{esc(node)}</text>')
    defs=f'<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{p.primary}"/></marker></defs>'
    return shell(a["title"],defs+"".join(parts),w,h)
