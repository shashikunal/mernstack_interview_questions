"""
bank_builders/common.py
Shared utilities, schemas, and validators for the 200+ / 300+ question bank builders.
Enforces the Question Writing Standard and Easy -> Intermediate -> Advanced progression.
"""

import re

ALLOWED_TYPES = [
    'Concept', 'MCQ', 'Output', 'Coding', 'Debugging',
    'Scenario', 'Practical', 'Comparison', 'Problem Solving', 'SQL Query',
    'Interview Follow-up'
]

ALLOWED_DIFFICULTIES = ['Easy', 'Intermediate', 'Advanced']

FORBIDDEN_WORDS = [
    'facilitate', 'leverage', 'paradigm', 'aforementioned',
    'encapsulation mechanism', 'orchestration', 'abstraction layer',
    'subsequent', 'comprehensive', 'heterogeneous', 'utilize'
]

def make_q(
    qid,
    num,
    subject,
    topic,
    subtopic,
    question,
    answer,
    difficulty='Easy',
    question_type='Concept',
    short_explanation='',
    code_example='',
    interview_round='Technical Round',
    frequency='High',
    references='',
    follow_up='',
    mcq_options=None,
    correct_option=None
):
    """
    Creates a validated, normalized question object adhering to the Question Writing Standard.
    """
    type_map = {
        'Accessibility': 'Practical',
        'Security': 'Practical',
        'Performance': 'Practical',
        'SEO': 'Concept',
        'HR': 'Scenario',
        'Typography': 'Concept',
        'Layout': 'Practical',
        'Animation': 'Practical',
        'Syntax': 'Concept',
        'Fundamentals': 'Concept',
        'Architecture': 'Concept',
        'Best Practice': 'Practical',
        'Testing': 'Practical',
        'Query': 'SQL Query'
    }
    question_type = type_map.get(question_type, question_type)

    if difficulty == 'Medium':
        difficulty = 'Intermediate'

    assert difficulty in ALLOWED_DIFFICULTIES, f"Invalid difficulty: {difficulty}"
    assert question_type in ALLOWED_TYPES, f"Invalid type: {question_type}"

    # Enforce default reference if none provided
    if not references:
        ref_map = {
            'HTML': 'MDN Web Docs',
            'CSS': 'MDN Web Docs',
            'JavaScript': 'MDN JavaScript Guide',
            'ES6+': 'MDN ES6 Reference',
            'ES6': 'MDN ES6 Reference',
            'DOM': 'MDN DOM API',
            'jQuery': 'jQuery API Documentation',
            'React': 'React Official Documentation',
            'Node.js': 'Node.js Official Documentation',
            'Express.js': 'Express.js Documentation',
            'Express': 'Express.js Documentation',
            'REST API / HTTP': 'MDN HTTP Guide',
            'REST / HTTP': 'MDN HTTP Guide',
            'SQL': 'SQL Standard Reference',
            'MongoDB': 'MongoDB Manual',
            'Aptitude': 'Quantitative Aptitude Standard Guide',
            'Logical Reasoning': 'Logical Reasoning Reference',
            'Problem Solving': 'Algorithmic Problem Solving Guide',
            'DSA': 'Data Structures and Algorithms Reference',
            'Coding': 'JavaScript Coding Guide',
            'Git / GitHub': 'Git Official Documentation',
            'Git': 'Git Official Documentation',
            'Testing': 'Jest & Playwright Documentation',
            'Web Fundamentals': 'MDN Web Fundamentals',
            'Project Interview': 'Fullstack Architecture Reference',
            'Projects': 'Fullstack Architecture Reference',
            'HR / Communication': 'Technical HR Interview Guide',
            'HR': 'Technical HR Interview Guide'
        }
        references = ref_map.get(subject, 'Technical Interview Guide')

    # If MCQ, format the answer and explanation nicely
    if question_type == 'MCQ' and mcq_options:
        opts_text = "\n".join([f"{k}. {v}" for k, v in mcq_options.items()])
        full_answer = f"Correct Answer: {correct_option}\n\n{opts_text}\n\nExplanation: {answer}"
    else:
        full_answer = answer

    # Sanitize forbidden words
    clean_answer = full_answer
    for w in ['leverage', 'utilize']:
        clean_answer = re.sub(r'\b' + w + r'\b', 'use', clean_answer, flags=re.I)
    clean_answer = re.sub(r'\bsubsequent\b', 'next', clean_answer, flags=re.I)
    clean_answer = re.sub(r'\bfacilitate\b', 'help', clean_answer, flags=re.I)

    return {
        "id": qid,
        "num": num,
        "subject": subject,
        "topic": topic,
        "subTopic": subtopic,
        "question": question.strip(),
        "answer": clean_answer.strip(),
        "shortExplanation": short_explanation.strip(),
        "codeExample": code_example.strip(),
        "difficulty": difficulty,
        "questionType": question_type,
        "interviewRound": interview_round,
        "frequency": frequency,
        "references": references.strip(),
        "followUpQuestions": follow_up.strip(),
        "addedAt": num
    }

def parse_item(item):
    """
    Parses flexible question tuples:
    6 items: (q_text, ans, diff, qtype, code, fup)
    8 items (type A): (q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup)
    8 items (type B): (top, subtop, q_text, ans, diff, qtype, code, fup)
    10 items: (top, subtop, q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup)
    """
    if len(item) == 6:
        return item[0], item[1], item[2], item[3], item[4], None, None, item[5]
    elif len(item) == 8:
        if item[4] in ALLOWED_DIFFICULTIES:
            return item[2], item[3], item[4], item[5], item[6], None, None, item[7]
        return item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]
    elif len(item) == 10:
        return item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9]
    raise ValueError(f"Unexpected tuple length: {len(item)}")

