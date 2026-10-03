"""
generate_all_subjects.py
Master orchestrator to build genuine, complete, interview-focused fresher questions:
- >=200 questions for each subject (>=300 for JavaScript, React, SQL, Aptitude, DSA)
- Easy -> Intermediate -> Advanced progression
- Types: Concept, MCQ, Output, Coding, Debugging, Scenario, Practical, Comparison, SQL Query
- Simple English, short sentences, direct answers, real references, zero fake data
"""

import os
import json
import re

print("Starting generation of comprehensive fresher interview question bank...")
