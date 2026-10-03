import os, re, json, html

BASE_DIR = r"C:\Users\Qsp\Documents\mernstack_interview_questions"
MERN_DIR = os.path.join(BASE_DIR, "mern-200")

CATEGORIES = [
    {
        "id": "crash",
        "slug": "crash-plan",
        "name": "1-Day Crash Plan",
        "icon": "🚀",
        "badgeColor": "from-rose-500 to-pink-600",
        "color": "#f43f5e"
    },
    {
        "id": "js-frontend",
        "slug": "js-frontend",
        "name": "JS / TS / HTML / CSS",
        "icon": "⚡",
        "badgeColor": "from-amber-500 to-yellow-500",
        "color": "#f59e0b"
    },
    {
        "id": "react-redux",
        "slug": "react-redux",
        "name": "React & Redux",
        "icon": "⚛️",
        "badgeColor": "from-cyan-500 to-blue-500",
        "color": "#06b6d4"
    },
    {
        "id": "express-node",
        "slug": "express-node",
        "name": "Express & Node.js",
        "icon": "🟢",
        "badgeColor": "from-emerald-500 to-teal-500",
        "color": "#10b981"
    },
    {
        "id": "mongodb",
        "slug": "mongodb",
        "name": "MongoDB & DB",
        "icon": "🍃",
        "badgeColor": "from-green-500 to-emerald-600",
        "color": "#22c55e"
    },
    {
        "id": "dsa-git",
        "slug": "dsa-git",
        "name": "DSA, Git & HR",
        "icon": "🧩",
        "badgeColor": "from-purple-500 to-indigo-600",
        "color": "#8b5cf6"
    }
]

def extract_tags(text, title, category):
    combined = (title + " " + text).lower()
    tags = set()
    
    tag_keywords = {
        "Closure": ["closure", "lexical scope"],
        "Event Loop": ["event loop", "microtask", "macrotask", "call stack", "libuv"],
        "Promise / Async": ["promise", "async/await", "then", "catch", "allsettled"],
        "Debounce / Throttle": ["debounce", "throttle"],
        "Prototypes": ["prototype", "prototypal", "__proto__"],
        "TypeScript": ["typescript", "interface", "generics", "type alias", "ts"],
        "HTML5 / CSS": ["flex", "grid", "box-sizing", "reflow", "repaint", "semantic", "a11y", "css", "html"],
        "Hooks": ["useeffect", "usememo", "usecallback", "usestate", "useref", "usereducer", "custom hook"],
        "Redux Toolkit": ["redux", "rtk", "createslice", "createasyncthunk", "store", "dispatch", "actions"],
        "Context API": ["context", "usecontext", "provider"],
        "Virtual DOM": ["virtual dom", "reconciliation", "diffing", "fiber", "render cycle"],
        "JWT / Auth": ["jwt", "token", "auth", "httponly", "samesite", "cookie", "bearer", "bcrypt", "rbac"],
        "Middleware": ["middleware", "req, res, next", "cors", "body-parser", "helmet"],
        "REST API": ["rest", "http", "status code", "endpoint", "get", "post", "put", "delete"],
        "Streams / Buffers": ["stream", "buffer", "pipe", "chunk"],
        "Redis / Caching": ["redis", "cache", "caching", "ttl", "in-memory"],
        "Indexes": ["index", "compound index", "b-tree", "single field index", "multikey"],
        "Aggregation": ["aggregation", "pipeline", "$match", "$group", "$lookup", "$project", "$unwind"],
        "Mongoose": ["mongoose", "schema", "model", "populate", "pre/post", "virtuals"],
        "Embedding vs Ref": ["embed", "reference", "normalization", "denormalization", "16mb"],
        "Big-O": ["big-o", "o(1)", "o(n)", "o(log n)", "time complexity", "space complexity"],
        "Two Pointers": ["two pointer", "sliding window", "two sum"],
        "Stack & Queue": ["stack", "queue", "parentheses", "lru"],
        "Tree & Graph": ["tree", "graph", "bfs", "dfs", "binary tree"],
        "Git Flow": ["git", "merge", "rebase", "cherry-pick", "conflict", "stash", "commit"],
        "STAR Stories": ["star", "project story", "challenge", "result", "metric", "situation"],
        "System Design": ["system design", "rate limit", "scale", "load balancer", "microservice", "architecture"]
    }
    
    for tag, kws in tag_keywords.items():
        if any(kw in combined for kw in kws):
            tags.add(tag)
            
    # Category fallback tag if empty
    if not tags:
        if category == "js-frontend": tags.add("JavaScript")
        elif category == "react-redux": tags.add("React")
        elif category == "express-node": tags.add("Node.js")
        elif category == "mongodb": tags.add("MongoDB")
        elif category == "dsa-git": tags.add("DSA")
        elif category == "crash": tags.add("Crash Plan")
        
    return sorted(list(tags))

def parse_markdown_category(cat_id, filepath):
    with open(filepath, encoding='utf-8') as f:
        lines = f.read().splitlines()
        
    questions = []
    current = None
    q_pattern = re.compile(r'^\s*(\d+)\.\s+\*\*(.+?)\*\*\s*(.*)$')
    
    for line in lines:
        m = q_pattern.match(line)
        if m:
            if current:
                questions.append(process_question(current, cat_id))
            q_num = int(m.group(1))
            q_title = m.group(2).strip()
            rest = m.group(3).strip()
            current = {
                'id': f"{cat_id}-{q_num}",
                'category': cat_id,
                'num': q_num,
                'title': q_title,
                'raw_lines': [rest] if rest else []
            }
        elif current is not None:
            if line.strip().startswith('##') or line.strip().startswith('#'):
                continue
            current['raw_lines'].append(line)
            
    if current:
        questions.append(process_question(current, cat_id))
        
    return questions

def process_question(q, cat_id):
    explanation_parts = []
    code_parts = []
    use_parts = []
    tip_parts = []
    
    for line in q['raw_lines']:
        line_clean = re.sub(r'^\s*[-*•]\s*', '', line).strip()
        if not line_clean:
            continue
            
        lower = line_clean.lower()
        if lower.startswith(('code example:', 'code:', 'example:')):
            idx = line_clean.find(':')
            val = line_clean[idx+1:].strip()
            if val: code_parts.append(val)
        elif lower.startswith(('project use:', 'project example:', 'use:', 'use-case (1 yoe):', 'use-case:')):
            idx = line_clean.find(':')
            val = line_clean[idx+1:].strip()
            if val: use_parts.append(val)
        elif lower.startswith(('tip/mistake:', 'mistake/tip:', 'mistake:', 'tip:')):
            idx = line_clean.find(':')
            val = line_clean[idx+1:].strip()
            if val: tip_parts.append(val)
        elif lower.startswith(('say:', 'edge cases:')):
            idx = line_clean.find(':')
            label = line_clean[:idx].strip()
            val = line_clean[idx+1:].strip()
            tip_parts.append(f"{label}: {val}")
        elif lower.startswith(('concept:', 'explanation:', 'what:', 'why:', 'how:', 'why it matters:', 'how it works:', 'approach:', 'complexity:')):
            idx = line_clean.find(':')
            label = line_clean[:idx].strip()
            val = line_clean[idx+1:].strip()
            explanation_parts.append((label, val))
        else:
            explanation_parts.append(("", line_clean))
            
    # Clean code snippets (strip backticks if wrapping full line)
    clean_code = []
    for c in code_parts:
        c_strip = c.strip()
        if c_strip.startswith('`') and c_strip.endswith('`') and len(c_strip) > 2:
            clean_code.append(c_strip[1:-1])
        else:
            clean_code.append(c_strip)
            
    full_explanation = ""
    for label, text in explanation_parts:
        if label:
            full_explanation += f"<p><strong>{html.escape(label)}:</strong> {html.escape(text)}</p>"
        else:
            full_explanation += f"<p>{html.escape(text)}</p>"
            
    use_case = " ".join(use_parts)
    tip = " ".join(tip_parts)
    code_text = "\n".join(clean_code)
    
    all_text = f"{q['title']} {use_case} {tip} {code_text} " + " ".join([t[1] for t in explanation_parts])
    tags = extract_tags(all_text, q['title'], cat_id)
    
    return {
        "id": q["id"],
        "category": cat_id,
        "num": q["num"],
        "title": q["title"],
        "explanation": full_explanation,
        "code": code_text,
        "useCase": use_case,
        "tip": tip,
        "tags": tags,
        "searchIndex": f"{q['num']} {q['title']} {use_case} {tip} {code_text} {' '.join(tags)}".lower()
    }

def parse_crash_plan():
    crash_path = os.path.join(BASE_DIR, "00-crash-plan.md")
    questions = []
    if not os.path.isfile(crash_path):
        return questions
        
    with open(crash_path, encoding='utf-8') as f:
        content = f.read()
        
    # Extract "10 Must-Know for Tomorrow"
    m = re.search(r'## 10 Must-Know for Tomorrow.*?\n(1\..*?)(?=\n##|\Z)', content, re.DOTALL)
    if m:
        items = re.findall(r'(\d+)\.\s+(.+?)(?=\n\d+\.|\Z)', m.group(1), re.DOTALL)
        for num, text in items:
            text = text.strip().replace('\n', ' ')
            title = text.split(' - ')[0].split(' OR ')[0].split(' + ')[0]
            if len(title) > 65:
                title = title[:65] + "..."
            questions.append({
                "id": f"crash-{num}",
                "category": "crash",
                "num": int(num),
                "title": f"Must-Know #{num}: {title}",
                "explanation": f"<p><strong>Core Concept & Requirements:</strong> {html.escape(text)}</p><p><em>1-Day High Yield Strategy:</em> Memorize this with 1 project example and metric ready.</p>",
                "code": "",
                "useCase": "1 YOE Interview focus: Say 'I built/fixed' with 1 concrete metric from your project (load time, bug count, API call reduction).",
                "tip": "Explain aloud in 30 seconds: Concept -> Why -> Code/Architecture -> 1 Project Metric. Never stay silent.",
                "tags": extract_tags(text, title, "crash"),
                "searchIndex": f"{num} {title} {text} crash must-know".lower()
            })
    return questions

def main():
    all_questions = []
    
    # 1. Crash plan
    crash_qs = parse_crash_plan()
    all_questions.extend(crash_qs)
    print(f"Parsed {len(crash_qs)} crash plan questions")
    
    # 2. MERN categories
    for cat_slug in ["js-frontend", "react-redux", "express-node", "mongodb", "dsa-git"]:
        fp = os.path.join(MERN_DIR, cat_slug, "README.md")
        cat_qs = parse_markdown_category(cat_slug, fp)
        all_questions.extend(cat_qs)
        print(f"Parsed {len(cat_qs)} questions from {cat_slug}")
        
    print(f"Total Questions: {len(all_questions)}")
    
    # Collect all unique tags
    all_tags = sorted(list(set(tag for q in all_questions for tag in q["tags"])))
    
    data_payload = {
        "categories": CATEGORIES,
        "tags": all_tags,
        "questions": all_questions
    }
    
    js_content = "window.INTERVIEW_DATA = " + json.dumps(data_payload, indent=None) + ";"
    
    out_js = os.path.join(BASE_DIR, "questions-data.js")
    with open(out_js, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Wrote questions-data.js ({os.path.getsize(out_js) // 1024} KB)")
    
    # Also save to mern-200/questions-data.js for easy access from subfolder
    sub_js = os.path.join(MERN_DIR, "questions-data.js")
    with open(sub_js, "w", encoding="utf-8") as f:
        f.write(js_content)

if __name__ == "__main__":
    main()
