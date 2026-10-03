# -*- coding: utf-8 -*-
import json

DATA_FILE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\fresher-data.js"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()
    s = text.find("[")
    e = text.rfind("]")
    questions = json.loads(text[s:e+1])

print("=== CSS Questions ===")
for q in questions:
    if q["subject"] == "CSS":
        print(f"[{q['id']}] {q['topic']} | {q['subTopic']}: {q['question']}")
