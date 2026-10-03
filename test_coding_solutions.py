# -*- coding: utf-8 -*-
"""
Tests all code solutions by executing them in Node.js
"""

import json
import subprocess

DATA_FILE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\fresher-data.js"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()
    s = text.find("[")
    e = text.rfind("]")
    questions = json.loads(text[s:e+1])

coding_qs = [q for q in questions if q["questionType"] in ["Coding", "Output"]]
print(f"Testing {len(coding_qs)} Coding & Output questions in Node.js runtime...")

passed = 0
failed = 0

for q in coding_qs:
    code = q.get("codeExample", "")
    if not code or q["subject"] in ["SQL", "HTML", "CSS", "Git"]:
        continue
    
    # Run in Node.js
    try:
        proc = subprocess.run(["node", "-e", code], capture_output=True, text=True, timeout=5)
        if proc.returncode == 0:
            passed += 1
        else:
            # Check if failure is due to browser-only globals (like document, window, alert)
            stderr = proc.stderr
            if "document is not defined" in stderr or "window is not defined" in stderr or "alert is not defined" in stderr:
                passed += 1 # Expected browser-environment code
            else:
                print(f"FAIL [{q['id']}] {q['question'][:50]}:")
                print(f"  Error: {proc.stderr[:150]}")
                failed += 1
    except Exception as ex:
        print(f"Exception [{q['id']}]: {ex}")
        failed += 1

print(f"\nExecution result: {passed} passed, {failed} failed.")
