# -*- coding: utf-8 -*-
import json
import re

DATA_FILE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\fresher-data.js"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()
    s = text.find("[")
    e = text.rfind("]")
    questions = json.loads(text[s:e+1])

def get_tokens(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    stopwords = {"what", "is", "the", "difference", "between", "how", "do", "you", "and", "in", "a", "an", "of", "to", "for", "with", "why", "are", "can", "explain"}
    tokens = set(text.split()) - stopwords
    return tokens

# Check subject by subject
by_subject = {}
for q in questions:
    by_subject.setdefault(q["subject"], []).append(q)

for sub, qlist in sorted(by_subject.items()):
    print(f"\n=== Checking {sub} ({len(qlist)} Qs) ===")
    for i in range(len(qlist)):
        t1 = get_tokens(qlist[i]["question"])
        for j in range(i + 1, len(qlist)):
            t2 = get_tokens(qlist[j]["question"])
            inter = len(t1.intersection(t2))
            union = len(t1.union(t2))
            sim = inter / union if union > 0 else 0
            if sim >= 0.45:
                print(f"  ({sim:.2f}) [{qlist[i]['id']}] {qlist[i]['question'][:50]}... <-> [{qlist[j]['id']}] {qlist[j]['question'][:50]}...")
