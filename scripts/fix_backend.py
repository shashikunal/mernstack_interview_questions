import re

with open('scripts/build_backend.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix the merged tuple first
fixed_code = code.replace(
    '("Why should nodemon NEVER be used in production?", "nodemon is designed for development file watching. In production, use an enterprise process manager like PM2, Docker, or Kubernetes.", "Easy", "Best Practice", "", "Express Architecture MCQ: What is the recommended way to separate app configuration from port binding for testability?", "Option B is correct. Export app in app.js and call listen in server.js.", "Easy", "MCQ", "", {"A": "Call listen in every route", "B": "Export app from app.js, listen in server.js", "C": "Use two package.json files", "D": "Run nodemon in tests"}, "B", "Why does this help Supertest?"),',
    '("Why should nodemon NEVER be used in production?", "nodemon is designed for development file watching. In production, use an enterprise process manager like PM2, Docker, or Kubernetes.", "Easy", "Best Practice", "", "What is process management?"),\n        ("Express Architecture MCQ: What is the recommended way to separate app configuration from port binding for testability?", "Option B is correct. Export app in app.js and call listen in server.js.", "Easy", "MCQ", "", {"A": "Call listen in every route", "B": "Export app from app.js, listen in server.js", "C": "Use two package.json files", "D": "Run nodemon in tests"}, "B", "Why does this help Supertest?"),'
)

with open('scripts/build_backend.py', 'w', encoding='utf-8') as f:
    f.write(fixed_code)

print("Fixed line 426 in scripts/build_backend.py")
