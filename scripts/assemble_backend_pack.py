"""
scripts/assemble_backend_pack.py
Reads base items, fixes tuples, imports additions, and compiles bank_builders/pack_backend.py.
"""

import ast
import re
import os
from backend_additions import (
    node_extra_items,
    express_extra_items,
    express_extra_items_part2,
    express_extra_items_part3,
    rest_extra_items,
    rest_extra_items_part2,
    rest_extra_items_part3
)

with open('scripts/build_backend.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the merged tuples
text = text.replace(
    '("Why should nodemon NEVER be used in production?", "nodemon is designed for development file watching. In production, use an enterprise process manager like PM2, Docker, or Kubernetes.", "Easy", "Best Practice", "", "Express Architecture MCQ: What is the recommended way to separate app configuration from port binding for testability?", "Option B is correct. Export app in app.js and call listen in server.js.", "Easy", "MCQ", "", {"A": "Call listen in every route", "B": "Export app from app.js, listen in server.js", "C": "Use two package.json files", "D": "Run nodemon in tests"}, "B", "Why does this help Supertest?"),',
    '("Why should nodemon NEVER be used in production?", "nodemon is designed for development file watching. In production, use an enterprise process manager like PM2, Docker, or Kubernetes.", "Easy", "Best Practice", "", "What is process management?"),\n        ("Express Architecture MCQ: What is the recommended way to separate app configuration from port binding for testability?", "Option B is correct. Export app in app.js and call listen in server.js.", "Easy", "MCQ", "", {"A": "Call listen in every route", "B": "Export app from app.js, listen in server.js", "C": "Use two package.json files", "D": "Run nodemon in tests"}, "B", "Why does this help Supertest?"),'
)

text = text.replace(
    '("What is Single Sign-On (SSO)?", "An authentication scheme that allows a user to log in with a single ID and password to access multiple independent software systems.", "Easy", "Concept", "", "REST MCQ: Which HTTP method should be used to create a new resource in a REST API?", "Option B is correct. POST creates new resources.", "Easy", "MCQ", "", {"A": "GET", "B": "POST", "C": "PUT", "D": "PATCH"}, "B", "What should be used for full replacement?"),',
    '("What is Single Sign-On (SSO)?", "An authentication scheme that allows a user to log in with a single ID and password to access multiple independent software systems.", "Easy", "Concept", "", "What is IAM?"),\n        ("REST MCQ: Which HTTP method should be used to create a new resource in a REST API?", "Option B is correct. POST creates new resources.", "Easy", "MCQ", "", {"A": "GET", "B": "POST", "C": "PUT", "D": "PATCH"}, "B", "What should be used for full replacement?"),'
)

text = text.replace(
    '("Why is performing mutations (delete or purchase) via HTTP GET catastrophically dangerous?", "Search engine crawlers, prefetchers, and browser accelerators follow all GET links automatically, accidentally deleting user accounts or purchasing items.", "Intermediate", "Scenario", "", "REST Coding: Design full CRUD endpoints for a \'products\' resource with paths and HTTP methods.", "GET /products (list), POST /products (create), GET /products/:id (read), PUT /products/:id (replace), PATCH /products/:id (partial update), DELETE /products/:id (delete).", "Easy", "Coding", "// List all: GET /api/v1/products\\n// Create: POST /api/v1/products\\n// Read one: GET /api/v1/products/:id\\n// Full update: PUT /api/v1/products/:id\\n// Partial update: PATCH /api/v1/products/:id\\n// Delete: DELETE /api/v1/products/:id", "What status code should each return?"),',
    '("Why is performing mutations (delete or purchase) via HTTP GET catastrophically dangerous?", "Search engine crawlers, prefetchers, and browser accelerators follow all GET links automatically, accidentally deleting user accounts or purchasing items.", "Intermediate", "Scenario", "", "Why should GET be safe?"),\n        ("REST Coding: Design full CRUD endpoints for a products resource with paths and HTTP methods.", "GET /products (list), POST /products (create), GET /products/:id (read), PUT /products/:id (replace), PATCH /products/:id (partial update), DELETE /products/:id (delete).", "Easy", "Coding", "// List all: GET /api/v1/products\\n// Create: POST /api/v1/products\\n// Read one: GET /api/v1/products/:id\\n// Full update: PUT /api/v1/products/:id\\n// Partial update: PATCH /api/v1/products/:id\\n// Delete: DELETE /api/v1/products/:id", "What status code should each return?"),'
)

# Extract lists using regex
def extract_list(name):
    pattern = rf'\b{name}\s*=\s*\[(.*?)\]\s*(?:for|\n\s*[a-zA-Z0-9_]+_items|\n\s*print|\n\s*def)'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        raise ValueError(f"Could not find list {name}")
    return ast.literal_eval('[' + m.group(1) + ']')

arch_items = extract_list('arch_items')
el_items = extract_list('el_items')
fs_items = extract_list('fs_items')
sec_items = extract_list('sec_items')

rt_items = extract_list('rt_items')
mw_items = extract_list('mw_items')
prod_items = extract_list('prod_items')

h_items = extract_list('h_items')
sc_items = extract_list('sc_items')
rest_items = extract_list('rest_items')

node_all = arch_items + el_items + fs_items + sec_items + node_extra_items
express_all = rt_items + mw_items + prod_items + express_extra_items + express_extra_items_part2 + express_extra_items_part3
rest_all = h_items + sc_items + rest_items + rest_extra_items + rest_extra_items_part2 + rest_extra_items_part3

print(f"Node.js total: {len(node_all)}")
print(f"Express.js total: {len(express_all)}")
print(f"REST API total: {len(rest_all)}")

# Write to bank_builders/pack_backend.py
import json

output = '''"""
bank_builders/pack_backend.py
Generates 215+ questions each for:
- Node.js (215 Qs)
- Express.js (215 Qs)
- REST API / HTTP (215 Qs)
"""

from .common import make_q, parse_item

NODE_ITEMS = ''' + repr(node_all) + '''

EXPRESS_ITEMS = ''' + repr(express_all) + '''

REST_ITEMS = ''' + repr(rest_all) + '''

def build_nodejs_pack(start_num=1):
    qs = []
    num = start_num
    for item in NODE_ITEMS:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-node-{num}", num, "Node.js", "Node Core & Concurrency", "Architecture & Modules",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs

def build_express_pack(start_num=1):
    qs = []
    num = start_num
    for item in EXPRESS_ITEMS:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-express-{num}", num, "Express.js", "Routing & Middleware", "Express Architecture & Security",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs

def build_rest_pack(start_num=1):
    qs = []
    num = start_num
    for item in REST_ITEMS:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-rest-{num}", num, "REST API / HTTP", "HTTP Protocols & REST Design", "Contracts & Architecture",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs
'''

with open('bank_builders/pack_backend.py', 'w', encoding='utf-8') as f:
    f.write(output)

print("Successfully generated bank_builders/pack_backend.py")
