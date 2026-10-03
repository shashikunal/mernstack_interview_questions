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
    # remove common stop words
    stopwords = {"what", "is", "the", "difference", "between", "how", "do", "you", "and", "in", "a", "an", "of", "to", "for", "with", "why", "are", "can", "explain"}
    tokens = set(text.split()) - stopwords
    return tokens

print(f"Total questions: {len(questions)}")
similar_pairs = []

for i in range(len(questions)):
    t1 = get_tokens(questions[i]["question"])
    for j in range(i + 1, len(questions)):
        t2 = get_tokens(questions[j]["question"])
        inter = len(t1.intersection(t2))
        union = len(t1.union(t2))
        sim = inter / union if union > 0 else 0
        if sim >= 0.60:
            similar_pairs.append((questions[i], questions[j], sim))

print(f"Pairs with >= 60% content word similarity: {len(similar_pairs)}")
for q1, q2, sim in similar_pairs:
    print(f"\n({sim:.2f}) [{q1['id']}] ({q1['subject']}) {q1['question']}\n      [{q2['id']}] ({q2['subject']}) {q2['question']}")
