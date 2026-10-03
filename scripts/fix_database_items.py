with open('scripts/database_sql_part2.py', 'r', encoding='utf-8') as f:
    t2 = f.read()

t2 = t2.replace(
    '("Why is conditional aggregation (SUM(CASE WHEN ...)) powerful?", "It allows pivoting row data into columnar summary statistics in a single table scan without needing multiple queries or joins.", "Intermediate", "Best Practice", "", "Aggregate Coding: Count active vs inactive users in a single query using conditional aggregation.", "SELECT SUM(CASE WHEN is_active THEN 1 ELSE 0 END) AS active, SUM(CASE WHEN NOT is_active THEN 1 ELSE 0 END) AS inactive FROM users;", "Easy", "Coding", "SELECT\\n  COUNT(CASE WHEN status = \'active\' THEN 1 END) AS active_users,\\n  COUNT(CASE WHEN status = \'inactive\' THEN 1 END) AS inactive_users\\nFROM users;", "How does COUNT(CASE WHEN...) work?"),',
    '("Why is conditional aggregation (SUM(CASE WHEN ...)) powerful?", "It allows pivoting row data into columnar summary statistics in a single table scan without needing multiple queries or joins.", "Intermediate", "Best Practice", "", "What is query pivoting?"),\n    ("Aggregate Coding: Count active vs inactive users in a single query using conditional aggregation.", "SELECT SUM(CASE WHEN is_active THEN 1 ELSE 0 END) AS active, SUM(CASE WHEN NOT is_active THEN 1 ELSE 0 END) AS inactive FROM users;", "Easy", "Coding", "SELECT\\n  COUNT(CASE WHEN status = \'active\' THEN 1 END) AS active_users,\\n  COUNT(CASE WHEN status = \'inactive\' THEN 1 END) AS inactive_users\\nFROM users;", "How does COUNT(CASE WHEN...) work?"),'
)

with open('scripts/database_sql_part2.py', 'w', encoding='utf-8') as f:
    f.write(t2)

with open('scripts/database_sql_part3.py', 'r', encoding='utf-8') as f:
    t3 = f.read()

t3 = t3.replace(
    '("What is the difference between IN and EXISTS?", "IN evaluates all values returned by the subquery into a set and checks membership. EXISTS evaluates conditionally row-by-row and short-circuits. EXISTS handles NULLs safely, whereas NOT IN fails if NULLs exist.", "Intermediate", "Comparison", "", "What is a Common Table Expression (CTE) and what keyword defines it?", "A CTE is a temporary named result set defined within a single SQL statement using the WITH keyword: WITH cte_name AS (SELECT ...).", "Easy", "Concept", "WITH HighEarners AS (\\n  SELECT * FROM employees WHERE salary > 100000\\n)\\nSELECT department_id, COUNT(*) FROM HighEarners GROUP BY department_id;", "What are the benefits of CTEs over subqueries?"),',
    '("What is the difference between IN and EXISTS?", "IN evaluates all values returned by the subquery into a set and checks membership. EXISTS evaluates conditionally row-by-row and short-circuits. EXISTS handles NULLs safely, whereas NOT IN fails if NULLs exist.", "Intermediate", "Comparison", "", "When is EXISTS faster?"),\n    ("What is a Common Table Expression (CTE) and what keyword defines it?", "A CTE is a temporary named result set defined within a single SQL statement using the WITH keyword: WITH cte_name AS (SELECT ...).", "Easy", "Concept", "WITH HighEarners AS (\\n  SELECT * FROM employees WHERE salary > 100000\\n)\\nSELECT department_id, COUNT(*) FROM HighEarners GROUP BY department_id;", "What are the benefits of CTEs over subqueries?"),'
)

t3 = t3.replace(
    '("Which window function should you use to find the top 3 highest unique salaries?", "DENSE_RANK(), because it does not skip ranks when duplicate salaries tie.", "Intermediate", "Best Practice", "", "Window Functions Coding: Find the top 2 highest paid employees in every department.", "WITH ranked AS (SELECT *, DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) as r FROM employees) SELECT * FROM ranked WHERE r <= 2;", "Intermediate", "Coding", "WITH RankedEmployees AS (\\n  SELECT id, name, department_id, salary,\\n    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS sal_rank\\n  FROM employees\\n)\\nSELECT * FROM RankedEmployees\\nWHERE sal_rank <= 2;", "Why must window function filtering be wrapped in a CTE or subquery?"),',
    '("Which window function should you use to find the top 3 highest unique salaries?", "DENSE_RANK(), because it does not skip ranks when duplicate salaries tie.", "Intermediate", "Best Practice", "", "Why does DENSE_RANK not skip?"),\n    ("Window Functions Coding: Find the top 2 highest paid employees in every department.", "WITH ranked AS (SELECT *, DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) as r FROM employees) SELECT * FROM ranked WHERE r <= 2;", "Intermediate", "Coding", "WITH RankedEmployees AS (\\n  SELECT id, name, department_id, salary,\\n    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS sal_rank\\n  FROM employees\\n)\\nSELECT * FROM RankedEmployees\\nWHERE sal_rank <= 2;", "Why must window function filtering be wrapped in a CTE or subquery?"),'
)

with open('scripts/database_sql_part3.py', 'w', encoding='utf-8') as f:
    f.write(t3)

with open('scripts/database_mongo.py', 'r', encoding='utf-8') as f:
    tm = f.read()

tm = tm.replace(
    '("Does findOneAndUpdate trigger Mongoose pre(\'save\') hooks?", "No! findOneAndUpdate() bypasses document middleware and executes directly on the database. It triggers pre(\'findOneAndUpdate\') query middleware instead.", "Intermediate", "Concept", "", "Performance Debugging: A TTL index was created with expireAfterSeconds: 60, but documents are not deleted immediately after 60 seconds. Why?", "The background TTL cleanup thread runs once every 60 seconds. Documents expire and are deleted during the next scheduled run (may take up to 60-120 seconds).", "Intermediate", "Debugging", "-- This is normal: background thread runs periodically", "How do you force immediate expiration in tests?")',
    '("Does findOneAndUpdate trigger Mongoose pre(\'save\') hooks?", "No! findOneAndUpdate() bypasses document middleware and executes directly on the database. It triggers pre(\'findOneAndUpdate\') query middleware instead.", "Intermediate", "Concept", "", "What hook fires on updateOne?"),\n    ("Performance Debugging: A TTL index was created with expireAfterSeconds: 60, but documents are not deleted immediately after 60 seconds. Why?", "The background TTL cleanup thread runs once every 60 seconds. Documents expire and are deleted during the next scheduled run (may take up to 60-120 seconds).", "Intermediate", "Debugging", "-- This is normal: background thread runs periodically", "How do you force immediate expiration in tests?")'
)

with open('scripts/database_mongo.py', 'w', encoding='utf-8') as f:
    f.write(tm)

print("Fixed split tuples in database sql and mongo files")
