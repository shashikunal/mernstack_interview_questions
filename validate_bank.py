# -*- coding: utf-8 -*-
"""
Validation and Quality Audit Script for Fresher Interview Question Bank
"""

import json
import re
from collections import Counter, defaultdict

DATA_FILE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\fresher-data.js"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()
    s = text.find("[")
    e = text.rfind("]")
    questions = json.loads(text[s:e+1])

print(f"Total questions loaded: {len(questions)}")

# Check 1: Allowed Question Types
ALLOWED_TYPES = {
    "Concept",
    "MCQ",
    "Output",
    "Coding",
    "Debugging",
    "Scenario",
    "SQL Query",
    "Aptitude",
    "Logical Reasoning",
    "Project",
    "HR"
}

# Check 2: Allowed Difficulties
ALLOWED_DIFFS = {
    "Easy",
    "Medium",
    "Fresher Coding"
}

# Check 3: Check for exact or near duplicates
def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return set(text.split())

duplicates = []
for i in range(len(questions)):
    w1 = normalize_text(questions[i]["question"])
    for j in range(i + 1, len(questions)):
        w2 = normalize_text(questions[j]["question"])
        intersection = len(w1.intersection(w2))
        union = len(w1.union(w2))
        sim = intersection / union if union > 0 else 0
        if sim > 0.80:
            duplicates.append((questions[i], questions[j], sim))

print(f"\n--- DUPLICATE CHECK ---")
print(f"Potential duplicates (similarity > 0.80): {len(duplicates)}")
for q1, q2, sim in duplicates:
    print(f"  [{q1['id']}] {q1['question']} <-> [{q2['id']}] {q2['question']} (sim: {sim:.2f})")

# Check 4: Metadata and type validation
type_mismatches = []
diff_mismatches = []
missing_fields = []

for q in questions:
    if q["questionType"] not in ALLOWED_TYPES:
        type_mismatches.append((q["id"], q["questionType"], q["question"][:40]))
    if q["difficulty"] not in ALLOWED_DIFFS:
        diff_mismatches.append((q["id"], q["difficulty"]))
    for field in ["id", "num", "subject", "topic", "subTopic", "question", "answer", 
                  "shortExplanation", "difficulty", "questionType", "interviewRound", 
                  "frequency", "references", "followUpQuestions"]:
        if not q.get(field):
            missing_fields.append((q["id"], field))

print(f"\n--- METADATA ENUM VALIDATION ---")
print(f"QuestionType not in allowed list: {len(type_mismatches)}")
for tm in type_mismatches:
    print(f"  {tm}")

print(f"Difficulty not in allowed list: {len(diff_mismatches)}")
print(f"Missing required fields: {len(missing_fields)}")

# Check 5: Aptitude question verification
aptitude_qs = [q for q in questions if q["subject"] == "Aptitude"]
print(f"\n--- APTITUDE QUESTIONS AUDIT ({len(aptitude_qs)} Qs) ---")
for q in aptitude_qs:
    print(f"  [{q['id']}] ({q['topic']}) {q['question'][:60]}... -> Answer: {q['answer'][:40]}")

# Check 6: SQL questions verification
sql_qs = [q for q in questions if q["subject"] == "SQL"]
print(f"\n--- SQL QUESTIONS AUDIT ({len(sql_qs)} Qs) ---")
for q in sql_qs:
    print(f"  [{q['id']}] ({q['topic']}) {q['question'][:60]}... Type: {q['questionType']}")

# Check 7: Output questions verification
output_qs = [q for q in questions if q["questionType"] == "Output"]
print(f"\n--- OUTPUT QUESTIONS AUDIT ({len(output_qs)} Qs) ---")
for q in output_qs:
    print(f"  [{q['id']}] ({q['subject']} > {q['topic']}) {q['question'][:60]}...")
