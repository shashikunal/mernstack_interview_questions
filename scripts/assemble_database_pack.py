"""
scripts/assemble_database_pack.py
Compiles bank_builders/pack_database.py containing:
- SQL (320 Qs)
- MongoDB (220 Qs)
Total: 540 questions.
"""

from database_sql import sql_basics
from database_sql_part2 import sql_crud_ddl, sql_aggregates_grouping
from database_sql_part3 import sql_joins, sql_subqueries_adv, sql_design_perf
from database_mongo import (
    mongo_basics,
    mongo_crud,
    mongo_query_adv,
    mongo_aggregation,
    mongo_perf_arch
)
from mongo_additions import mongo_extra_items

sql_all = (
    sql_basics +
    sql_crud_ddl +
    sql_aggregates_grouping +
    sql_joins +
    sql_subqueries_adv +
    sql_design_perf
)

mongo_all = (
    mongo_basics +
    mongo_crud +
    mongo_query_adv +
    mongo_aggregation +
    mongo_perf_arch +
    mongo_extra_items
)

print(f"Total SQL items: {len(sql_all)}")
print(f"Total MongoDB items: {len(mongo_all)}")

output = '''"""
bank_builders/pack_database.py
Generates 320+ questions for SQL and 220+ questions for MongoDB.
"""

from .common import make_q, parse_item

SQL_ITEMS = ''' + repr(sql_all) + '''

MONGO_ITEMS = ''' + repr(mongo_all) + '''

def build_sql_pack(start_num=1):
    qs = []
    num = start_num
    for item in SQL_ITEMS:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-sql-{num}", num, "SQL", "SQL & Relational Databases", "Queries, Joins, Aggregation & Design",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs

def build_mongodb_pack(start_num=1):
    qs = []
    num = start_num
    for item in MONGO_ITEMS:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-mongo-{num}", num, "MongoDB", "NoSQL & MongoDB", "CRUD, Aggregation, Indexing & Modeling",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs
'''

with open('bank_builders/pack_database.py', 'w', encoding='utf-8') as f:
    f.write(output)

print("Successfully wrote bank_builders/pack_database.py")
