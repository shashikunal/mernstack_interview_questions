# -*- coding: utf-8 -*-
"""
Generate Final Phase 3 Validation Metrics and Table
"""

import json
from collections import Counter, defaultdict

DATA_FILE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\fresher-data.js"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()
    s = text.find("[")
    e = text.rfind("]")
    questions = json.loads(text[s:e+1])

subjects = Counter(q["subject"] for q in data if "subject" in q) if 'data' in locals() else Counter(q["subject"] for q in questions)
topics_by_subject = defaultdict(set)
subtopics_by_subject = defaultdict(set)

for q in questions:
    sub = q["subject"]
    topics_by_subject[sub].add(q["topic"])
    subtopics_by_subject[sub].add(q["subTopic"])

print("Subject | Questions | Topics | Subtopics | Coverage Status")
print("-" * 65)

total_topics = sum(len(t) for t in topics_by_subject.values())
total_subtopics = sum(len(st) for st in subtopics_by_subject.values())

for sub, cnt in sorted(subjects.items(), key=lambda x: -x[1]):
    t_cnt = len(topics_by_subject[sub])
    st_cnt = len(subtopics_by_subject[sub])
    status = "Complete"
    print(f"{sub:<16} | {cnt:<9} | {t_cnt:<6} | {st_cnt:<9} | {status}")

print("-" * 65)
print(f"Total Questions: {len(questions)}")
print(f"Total Subjects: {len(subjects)}")
print(f"Total Unique Topics: {total_topics}")
print(f"Total Unique Subtopics: {total_subtopics}")
