# -*- coding: utf-8 -*-
import json

with open("fresher-data.js", "r", encoding="utf-8") as f:
    text = f.read()
    s = text.find("[")
    e = text.rfind("]")
    questions = json.loads(text[s:e+1])

for q in questions:
    if q["id"] in ["q-58", "q-89"]:
        print(f"[{q['id']}] {q['subject']} > {q['topic']} > {q['subTopic']}:")
        print(f"  Q: {q['question']}")
        print(f"  Ans: {q['answer'][:100]}...\n")
