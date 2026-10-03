"""
scripts/expand_backend.py
Extracts items from scripts/build_backend.py, fixes tuples, adds new items to reach 215+ for:
- Node.js (215)
- Express.js (215)
- REST API / HTTP (215)
And writes bank_builders/pack_backend.py cleanly.
"""

import ast
import re

with open('scripts/build_backend.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's fix the two known merged tuples in text
# Fix 1: nodemon in prod_items
text = text.replace(
    '("Why should nodemon NEVER be used in production?", "nodemon is designed for development file watching. In production, use an enterprise process manager like PM2, Docker, or Kubernetes.", "Easy", "Best Practice", "", "Express Architecture MCQ: What is the recommended way to separate app configuration from port binding for testability?", "Option B is correct. Export app in app.js and call listen in server.js.", "Easy", "MCQ", "", {"A": "Call listen in every route", "B": "Export app from app.js, listen in server.js", "C": "Use two package.json files", "D": "Run nodemon in tests"}, "B", "Why does this help Supertest?"),',
    '("Why should nodemon NEVER be used in production?", "nodemon is designed for development file watching. In production, use an enterprise process manager like PM2, Docker, or Kubernetes.", "Easy", "Best Practice", "", "What is process management?"),\n        ("Express Architecture MCQ: What is the recommended way to separate app configuration from port binding for testability?", "Option B is correct. Export app in app.js and call listen in server.js.", "Easy", "MCQ", "", {"A": "Call listen in every route", "B": "Export app from app.js, listen in server.js", "C": "Use two package.json files", "D": "Run nodemon in tests"}, "B", "Why does this help Supertest?"),'
)

# Fix 2: SSO in rest_items
text = text.replace(
    '("What is Single Sign-On (SSO)?", "An authentication scheme that allows a user to log in with a single ID and password to access multiple independent software systems.", "Easy", "Concept", "", "REST MCQ: Which HTTP method should be used to create a new resource in a REST API?", "Option B is correct. POST creates new resources.", "Easy", "MCQ", "", {"A": "GET", "B": "POST", "C": "PUT", "D": "PATCH"}, "B", "What should be used for full replacement?"),',
    '("What is Single Sign-On (SSO)?", "An authentication scheme that allows a user to log in with a single ID and password to access multiple independent software systems.", "Easy", "Concept", "", "What is IAM?"),\n        ("REST MCQ: Which HTTP method should be used to create a new resource in a REST API?", "Option B is correct. POST creates new resources.", "Easy", "MCQ", "", {"A": "GET", "B": "POST", "C": "PUT", "D": "PATCH"}, "B", "What should be used for full replacement?"),'
)

# Fix 3: GET mutations in rest_items
text = text.replace(
    '("Why is performing mutations (delete or purchase) via HTTP GET catastrophically dangerous?", "Search engine crawlers, prefetchers, and browser accelerators follow all GET links automatically, accidentally deleting user accounts or purchasing items.", "Intermediate", "Scenario", "", "REST Coding: Design full CRUD endpoints for a ' + "'products'" + ' resource with paths and HTTP methods.", "GET /products (list), POST /products (create), GET /products/:id (read), PUT /products/:id (replace), PATCH /products/:id (partial update), DELETE /products/:id (delete).", "Easy", "Coding", "// List all: GET /api/v1/products\\n// Create: POST /api/v1/products\\n// Read one: GET /api/v1/products/:id\\n// Full update: PUT /api/v1/products/:id\\n// Partial update: PATCH /api/v1/products/:id\\n// Delete: DELETE /api/v1/products/:id", "What status code should each return?"),',
    '("Why is performing mutations (delete or purchase) via HTTP GET catastrophically dangerous?", "Search engine crawlers, prefetchers, and browser accelerators follow all GET links automatically, accidentally deleting user accounts or purchasing items.", "Intermediate", "Scenario", "", "Why should GET be safe?"),\n        ("REST Coding: Design full CRUD endpoints for a products resource with paths and HTTP methods.", "GET /products (list), POST /products (create), GET /products/:id (read), PUT /products/:id (replace), PATCH /products/:id (partial update), DELETE /products/:id (delete).", "Easy", "Coding", "// List all: GET /api/v1/products\\n// Create: POST /api/v1/products\\n// Read one: GET /api/v1/products/:id\\n// Full update: PUT /api/v1/products/:id\\n// Partial update: PATCH /api/v1/products/:id\\n// Delete: DELETE /api/v1/products/:id", "What status code should each return?"),'
)

print("Text replaced and cleaned")
