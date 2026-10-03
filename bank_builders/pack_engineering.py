# bank_builders/pack_engineering.py
"""
Packs for:
- Git / GitHub (215 items)
- Testing (215 items)
- Web Fundamentals (216 items)
- Project Interview (232 items)
- HR / Communication (220 items)
"""

from .common import make_q, parse_item

import scripts.git_questions as g1
import scripts.git_part2 as g2

import scripts.testing_questions as t1
import scripts.testing_part2 as t2
import scripts.testing_part3 as t3
import scripts.testing_part4 as t4

import scripts.webfundamentals_questions as w1
import scripts.webfundamentals_part2 as w2
import scripts.webfundamentals_part3 as w3
import scripts.webfundamentals_part4 as w4

import scripts.project_questions as p1
import scripts.project_part2 as p2
import scripts.project_part3 as p3
import scripts.project_part4 as p4
import scripts.project_part5 as p5

import scripts.hr_questions as h1
import scripts.hr_part2 as h2
import scripts.hr_part3 as h3
import scripts.hr_part4 as h4
import scripts.hr_part5 as h5


def build_git_pack(start_num=1):
    items = g1.git_items + g2.git_part2_items
    qs = []
    num = start_num
    for item in items:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-git-{num}", num, "Git / GitHub", "Version Control", "Branching & Collaboration",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs


def build_testing_pack(start_num=1):
    items = (
        t1.testing_items
        + t2.testing_part2_items
        + t3.testing_part3_items
        + t4.testing_part4_items
    )
    qs = []
    num = start_num
    for item in items:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-test-{num}", num, "Testing", "Unit & Integration Testing", "Test Automation & Assertions",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs


def build_webfundamentals_pack(start_num=1):
    items = (
        w1.web_items
        + w2.web_part2_items
        + w3.web_part3_items
        + w4.web_part4_items
    )
    qs = []
    num = start_num
    for item in items:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-web-{num}", num, "Web Fundamentals", "HTTP & Browsers", "Web Architecture & Security",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs


def build_project_pack(start_num=1):
    items = (
        p1.project_items
        + p2.project_part2_items
        + p3.project_part3_items
        + p4.project_part4_items
        + p5.project_part5_items
    )
    qs = []
    num = start_num
    for item in items:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-proj-{num}", num, "Project Interview", "Full-Stack Architecture", "Project Workflows & Lifecycle",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs


def build_hr_pack(start_num=1):
    items = (
        h1.hr_questions_part1
        + h2.hr_questions_part2
        + h3.hr_questions_part3
        + h4.hr_questions_part4
        + h5.hr_questions_part5
    )
    qs = []
    num = start_num
    for item in items:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-hr-{num}", num, "HR / Communication", "Behavioral & Communication", "Workplace Scenarios",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs
