import os, re, html
BASE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\mern-200"
SUBJECTS = {
 "js-frontend": ("JS / TS / HTML / CSS — 200 Q&A", "100 JS + 40 TS + 30 HTML + 30 CSS"),
 "react-redux": ("React + Redux — 200 Q&A", "Hooks, Redux Toolkit, RTK Query, performance"),
 "express-node": ("Express + Node — 200 Q&A", "Middleware, JWT, REST, Redis, testing"),
 "mongodb": ("MongoDB — 200 Q&A", "CRUD, indexes, aggregation, Mongoose"),
 "dsa-git": ("DSA + Git/HR — 200 Q&A", "100 DSA + 50 design + 50 Git/HR"),
}
CSS = """*{box-sizing:border-box}body{margin:0;font-family:system-ui,Segoe UI,Roboto,Arial;background:#0f172a;color:#e2e8f0}header{position:sticky;top:0;background:#020617;padding:14px 18px;border-bottom:1px solid #1e293b;z-index:10}header h1{margin:0;font-size:18px;color:#38bdf8}header p{margin:4px 0 0;color:#94a3b8;font-size:13px}.search{margin-top:10px;display:flex;gap:8px}input{flex:1;padding:10px;border-radius:8px;border:1px solid #334155;background:#0f172a;color:#fff}main{padding:18px;max-width:900px;margin:auto}.back{color:#7dd3fc;text-decoration:none;font-size:14px}.card{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:14px 16px;margin:10px 0}.card h3{margin:0 0 6px;font-size:15px;color:#facc15}.card h3 .n{color:#38bdf8;margin-right:8px}.card p{margin:0;font-size:14px;line-height:1.6;color:#e2e8f0}.card code{background:#020617;padding:2px 6px;border-radius:6px;color:#7dd3fc;font-size:13px}.hub-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}.hub-card{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:18px;text-decoration:none;color:#e2e8f0}.hub-card:hover{border-color:#38bdf8}.hub-card h2{margin:0 0 6px;font-size:17px;color:#38bdf8}footer{padding:20px;text-align:center;color:#64748b;font-size:12px}a{color:#7dd3fc}
"""
with open(os.path.join(BASE,"style.css"),"w",encoding="utf-8") as f: f.write(CSS)

def md_to_cards(md_path):
    txt=open(md_path,encoding="utf-8").read().splitlines()
    title=txt[0].lstrip("# ").strip() if txt else "Q&A"
    items=[]; q=None; buf=[]
    pat=re.compile(r"^\s*(\d+)\.\s+\*\*(.+?)\*\*\s*(.*)$")
    for line in txt[1:]:
        s=line.strip()
        if s.startswith("##") or s.startswith("> "): continue
        m=pat.match(line)
        if m:
            if q: items.append((q," ".join(buf).strip()))
            q=m.group(2).strip(); rest=m.group(3).strip(); buf=[rest] if rest else []
        else:
            if q and s: buf.append(s)
    if q: items.append((q," ".join(buf).strip()))
    return title, items

def esc_inline(s):
    s=html.escape(s)
    s=re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s

for slug,(subtitle,desc) in SUBJECTS.items():
    md=os.path.join(BASE,slug,"README.md")
    title,cards=md_to_cards(md)
    html_cards="\n".join(f'<div class="card"><h3><span class="n">{i}.</span>{esc_inline(q)}</h3><p>{esc_inline(a)}</p></div>' for i,(q,a) in enumerate(cards,1))
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><link rel="stylesheet" href="../style.css"></head><body><header><a class="back" href="../index.html">← All subjects</a><h1>{html.escape(title)}</h1><p>{html.escape(desc)} • {len(cards)} questions</p><div class="search"><input id="q" placeholder="Search... e.g. closure, JWT, index" oninput="filter()"></div></header><main id="list">{html_cards}</main><footer>MERN 1 YOE • localhost:8000</footer><script>function filter(){{const v=document.getElementById('q').value.toLowerCase();document.querySelectorAll('.card').forEach(c=>c.style.display=c.textContent.toLowerCase().includes(v)?'':'none')}}</script></body></html>"""
    open(os.path.join(BASE,slug,"index.html"),"w",encoding="utf-8").write(page)
    print(f"{slug}: {len(cards)}")

hub_cards="\n".join(f'<a class="hub-card" href="./{s}/"><h2>{t}</h2><p>{d}</p></a>' for s,(t,d) in SUBJECTS.items())
hub=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MERN 1000 Q&A</title><link rel="stylesheet" href="./style.css"></head><body><header><h1>MERN Fullstack — 1000 Q&A</h1><p>200 per subject • styled with CSS • search included</p><div class="search"><input id="q" placeholder="Filter subjects..." oninput="document.querySelectorAll('.hub-card').forEach(c=>c.style.display=c.textContent.toLowerCase().includes(this.value.toLowerCase())?'':'none')"></div></header><main><div class="hub-grid">{hub_cards}<a class="hub-card" href="/interview-prep.html"><h2>Original Crash Site</h2><p>Tabs + search • interview-prep.html</p></a></div></main><footer>python -m http.server 8000 • /mern-200/</footer></body></html>"""
open(os.path.join(BASE,"index.html"),"w",encoding="utf-8").write(hub)
print("hub done")
