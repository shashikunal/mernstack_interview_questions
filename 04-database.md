# 04 - Databases: MongoDB vs Postgres

## Must Say in 30 sec
- Mongo: document/BSON, flexible schema, BASE, horizontal scale, embed for read-heavy 1-few.
- Postgres: relational, strict schema, ACID, joins, vertical+read replicas, best for relations/money.

## MongoDB - Top 12
1. **Embed vs reference?** Embed (user+addresses) for together-read, <100 items, no dup. Reference (posts/userId) for many/shared/enormous.
2. **Index?** `db.users.createIndex({email:1},{unique:true})`. Compound order matters (ESR: equality, sort, range). Too many slows writes.
3. **Aggregation?** `db.orders.aggregate([{$match:{status:'paid'}},{$group:{_id:'$userId',total:{$sum:'$amt'}}},{$sort:{total:-1}}])`.
4. **Find in array?** `db.p.find({tags:{$in:['js']}})` + multikey index auto.
5. **Transactions?** Replica-set sessions `startSession()->withTransaction()` for multi-doc. Single doc atomic by default.
6. **ObjectId?** 12-byte time+rand, sortable, use as `_id`. Store refs as ObjectId not string.
7. **Schema design e-comm?** users, products(index sku), orders {userId, items[{productId,qty,price}], status} - embed items snapshot price.
8. **N+1 fix?** `$lookup` or batch fetch + in-memory join, or denormalize.
9. **TTL/Capped?** `expireAfterSeconds` for OTP/sessions.
10. **Backup/scale?** Replica set (failover) + sharding by shard key (userId). Choose high-cardinality key.
11. **Mongoose validation?** Schema `required, unique, enum`, pre-save hash pw, never store plain.
12. **Slow query?** `explain('executionStats')`, check COLLSCAN -> add index.

## Postgres - Top 12
1. **Normalization vs denorm?** 3NF to avoid dup, denorm counts for read speed. Say tradeoff.
2. **Joins?** INNER only match, LEFT all left+null, RIGHT, FULL. `SELECT u.name,o.id FROM users u LEFT JOIN orders o ON o.user_id=u.id`.
3. **Indexes?** B-tree default, `CREATE INDEX idx_orders_user ON orders(user_id)`; `UNIQUE(email)`. Partial `WHERE status='active'`. Over-index hurts writes.
4. **ACID?** Atomic/Consistent/Isolated/Durable. Use transaction for transfer: `BEGIN; UPDATE...; COMMIT;` + `ROLLBACK` on err.
5. **Isolation?** Read Committed default, Serializable strictest. Race: `SELECT ... FOR UPDATE`.
6. **N+1 fix?** JOIN + `select_related` / DataLoader batch, add FK index.
7. **Pagination?** Keyset `WHERE id > $1 ORDER BY id LIMIT 20` (fast) vs `OFFSET` (slow large).
8. **Constraints?** PK/FK `REFERENCES users(id) ON DELETE CASCADE`, CHECK, NOT NULL, DEFAULT `now()`.
9. **1-N / N-M?** 1-N via FK, N-M via junction `post_tags(post_id,tag_id)`.
10. **JSONB?** `SELECT * FROM p WHERE meta @> '{"color":"red"}'` + GIN index. Hybrid relational+doc.
11. **Migrations?** Prisma/TypeORM/Alembic versioned, reversible, never manual prod edits.
12. **Connection pooling?** PgBouncer / RDS proxy, limit pool (e.g. 20), close idle.

## Prisma Quick (if asked)
```prisma
model User { id Int @id @default(autoincrement()) email String @unique orders Order[] }
model Order { id Int @id @default(autoincrement()) userId Int user User @relation(fields:[userId],references:[id]) total Decimal }
```

## 5 Likely Questions
1. SQL find 2nd highest salary? `SELECT MAX(salary) FROM emp WHERE salary < (SELECT MAX(salary) FROM emp)`
2. Users with order count? `SELECT u.id,COUNT(o.id) FROM users u LEFT JOIN orders o ON o.user_id=u.id GROUP BY u.id`
3. Mongo top products? aggregate group+sort+limit
4. How prevent duplicate email? unique index + handle 11000 / 23505
5. When Mongo vs Postgres? flexible catalog vs payments/inventory -> Postgres.
