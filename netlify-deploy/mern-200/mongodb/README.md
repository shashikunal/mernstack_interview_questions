# MongoDB - 200 Q&A

1. **What is MongoDB?**
What: MongoDB is a document-oriented NoSQL database that stores data as flexible BSON documents in collections, not fixed rows/tables.
Why: It fits MERN apps because JSON-like documents map directly to JS objects and allow fast iteration without migrations.
How: You create collections implicitly on insert, store nested objects/arrays, and query with `find()` or aggregation pipelines.
Example: `db.users.insertOne({name:"Asha", age:24, tags:["mern"]})`
Use-case (1 YOE): I stored user profiles with varying social links without ALTER TABLE pain in my auth project.
Mistake/Tip: Don't call it schemaless — say schema-flexible and mention validation; interviewers love that nuance.
2. **What is BSON?**
What: BSON is Binary JSON — MongoDB's storage format that extends JSON with types like ObjectId, Date, Decimal128, and Binary.
Why: It enables fast scanning, typed sorting, and compact storage while staying convertible to JS objects in Node.
How: Driver serializes JS objects to BSON on write and deserializes back on read; shell shows ISODate/ObjectId helpers.
Example: `ObjectId("65a1b2c3d4e5f0011223344") // 12-byte BSON type`
Use-case (1 YOE): I used BSON Date for `createdAt` and Decimal128 for prices to avoid float rounding in e-commerce.
Mistake/Tip: Don't say BSON is just JSON; name 2 extra types and the 16MB document limit.
3. **What is a collection in MongoDB?**
What: A collection is a group of documents, roughly like a SQL table but schema-flexible by default with dynamic fields.
Why: It lets different documents in `users` have different fields while still indexing/querying them together.
How: Created implicitly on first insert or explicitly via `db.createCollection("users")` with validation rules.
Example: `db.createCollection("users", {validator:{$jsonSchema:{required:["email"]}}})`
Use-case (1 YOE): I kept `users`, `posts`, `orders` as separate collections with indexes per query pattern in my blog.
Mistake/Tip: Don't create a collection per user; interview tip — mention capped vs regular collections.
4. **What is a document in MongoDB?**
What: A document is a JSON-like BSON record of key-value pairs, max 16MB, uniquely identified by `_id`.
Why: It allows embedding related data together for single-fetch reads, ideal for MERN object mapping.
How: Fields can nest objects/arrays; you insert via driver/Mongoose and query with dot notation.
Example: `db.users.insertOne({_id:ObjectId(), name:"Asha", address:{city:"Pune"}})`
Use-case (1 YOE): I embedded `address` in user docs so profile fetch needed no join.
Mistake/Tip: Mistake is unbounded embedding; tip — mention 16MB limit proactively.
5. **How do you insert one document?**
What: Single-doc insert adds one BSON doc to a collection atomically and generates `_id` if omitted.
Why: Used for signup, create-post, or add-product flows where one entity is created per request.
How: It validates against schema, writes to oplog, and returns `acknowledged` + `insertedId`.
Example: `db.users.insertOne({name:"Asha", age:24})`
Use-case (1 YOE): I used `User.create(req.body)` in Express signup controller to insert one user.
Mistake/Tip: Mistake is ignoring duplicate-key errors; always catch E11000 for email conflicts.
6. **How do you insert multiple documents?**
What: Bulk insert adds many docs in one round-trip and returns `insertedIds`, supporting ordered/unordered modes.
Why: Essential for seeding, CSV imports, and sync jobs where per-doc inserts would be too slow.
How: With `ordered:false` it continues past failures; with `ordered:true` it stops on first error.
Example: `db.users.insertMany([{name:"A"},{name:"B"}], {ordered:false})`
Use-case (1 YOE): I seeded 500 products with `insertMany` in a seed script for dev testing.
Mistake/Tip: Don't insert 100k docs at once — batch in 1k-5k; mention `bulkWrite` for mixed ops.
7. **How do you read all documents?**
What: `find()` returns a cursor to matching docs; `findOne()` returns a single doc or null.
Why: Cursors stream results to avoid loading entire collections into Node memory.
How: Chain `.sort().skip().limit()` and iterate with `toArray()` or `for await` in Node driver.
Example: `db.users.find({}).toArray() // findOne({email:"a@test.com"}) for single`
Use-case (1 YOE): I listed all products for admin panel with `find().lean().limit(50)`.
Mistake/Tip: Mistake is `find()` without limit on large collections; always paginate.
8. **How do you update one document?**
What: `updateOne(filter, update)` modifies the first match atomically using operators like `$set`.
Why: Used for profile edits or status changes where only one entity should change.
How: Filter selects doc, update doc applies operators; check `matchedCount` vs `modifiedCount`.
Example: `db.users.updateOne({name:"Asha"}, {$set:{age:25}})`
Use-case (1 YOE): I updated user city in profile PUT API with `updateOne({_id}, {$set:req.body})`.
Mistake/Tip: Forgetting `$set` overwrites; tip — mention `upsert:false` default.
9. **How do you update many documents?**
What: `updateMany` applies the same mutation to all docs matching the filter.
Why: Needed for bulk status changes like activating pending users or discounting a category.
How: Scans via index on filter, applies operators per doc, returns `modifiedCount`.
Example: `db.users.updateMany({status:"pending"}, {$set:{status:"active"}})`
Use-case (1 YOE): I bulk-activated sellers after KYC approval in admin API.
Mistake/Tip: Always test filter with `find()` first; a broad filter can corrupt data.
10. **How do you delete one document?**
What: `deleteOne(filter)` removes the first doc matching the filter.
Why: Used for removing a session, revoking a token, or deleting a specific cart item doc.
How: Finds via index, deletes, returns `deletedCount:0/1`; consider soft-delete instead.
Example: `db.users.deleteOne({email:"a@test.com"})`
Use-case (1 YOE): I deleted refresh tokens on logout with `deleteOne({token})`.
Mistake/Tip: Prefer soft-delete with `isDeleted`; hard delete loses audit trail.
11. **How do you delete many documents?**
What: `deleteMany(filter)` removes all docs matching the filter in one operation.
Why: Used for cleanup jobs like purging inactive users or expired OTPs.
How: Uses filter index if present; for full purge use `{}` but prefer `drop()` for whole collection.
Example: `db.users.deleteMany({status:"inactive"})`
Use-case (1 YOE): I cleaned expired sessions nightly with `deleteMany({expiresAt:{$lt:new Date()}})`.
Mistake/Tip: Mistake is empty filter accidents; always guard and require confirmation in admin APIs.
12. **What does `replaceOne()` do?**
What: `replaceOne` replaces an entire document (except immutable `_id`) with a new doc.
Why: Useful when you have a full new representation, e.g. sync from external source.
How: Unlike `$set` partial update, omitted fields are removed; set `upsert:true` to insert if missing.
Example: `db.users.replaceOne({email:"a@test.com"}, {name:"Asha", age:26, city:"Pune"})`
Use-case (1 YOE): I synced Shopify product snapshots by replacing full product docs.
Mistake/Tip: Mistake is losing fields by forgetting them; prefer `updateOne`+`$set` for partial edits.
13. **What is `upsert` in MongoDB?**
What: With `{upsert:true}`, an update creates the doc if no match is found, merging filter + update.
Why: Perfect for counters, settings, and sync jobs where insert-or-update logic is needed atomically.
How: MongoDB applies `$set`/`$setOnInsert` and inserts filter equality fields as new doc.
Example: `db.counters.updateOne({key:"visits"}, {$inc:{n:1}}, {upsert:true})`
Use-case (1 YOE): I upserted user preferences on first login without separate exists-check.
Mistake/Tip: Beware race-created duplicates without unique index; mention `$setOnInsert`.
14. **What is `findOneAndUpdate()`?**
What: Atomically finds, updates, and returns a doc — either before or after the change.
Why: Avoids read-then-write races for queues, seat booking, and stock decrement.
How: Pass `returnDocument:"after"` (or `new:true` in Mongoose) and `sort` to pick which match.
Example: `db.tasks.findOneAndUpdate({status:"pending"}, {$set:{status:"doing"}}, {returnDocument:"after", sort:{createdAt:1}})`
Use-case (1 YOE): I popped next email job from queue safely with this in a worker.
Mistake/Tip: Default returns old doc — explicitly ask for `after`; interviewers test this.
15. **What is `findOneAndDelete()`?**
What: Atomically finds and deletes one matching doc and returns it.
Why: Ideal for job queues where you must pop a task exactly once under concurrency.
How: Uses filter + sort to pick doc, deletes, returns deleted doc or null.
Example: `db.jobs.findOneAndDelete({status:"queued"}, {sort:{priority:-1}})`
Use-case (1 YOE): I implemented OTP consume-once by find-and-delete.
Mistake/Tip: Don't do find+delete separately — race causes double processing.
16. **How do you count documents?**
What: `countDocuments(filter)` gives accurate filtered counts; `estimatedDocumentCount()` uses metadata for fast totals.
Why: Needed for pagination totals, dashboard stats, and badge counts.
How: `countDocuments` scans/index-counts; estimated just reads collection size.
Example: `db.users.countDocuments({age:{$gt:20}}) // estimatedDocumentCount() for total`
Use-case (1 YOE): I showed total orders + filtered counts in admin dashboard with both.
Mistake/Tip: Don't use deprecated `count()`; use `countDocuments` with index on filter.
17. **What is ObjectId?**
What: 12-byte unique ID default for `_id` — 4B timestamp + 5B machine/process + 3B counter.
Why: Globally unique, sortable by creation time, and generatable without central coordination.
How: Auto-created on insert; you can extract timestamp via `ObjectId().getTimestamp()`.
Example: `new ObjectId() // e.g. ObjectId("65a1b2c3d4e5f0011223344")`
Use-case (1 YOE): I sorted feeds by `_id` desc as proxy for creation order.
Mistake/Tip: Don't store ObjectId as string for refs; keep type consistent or populate fails.
18. **Can you use custom _id?**
What: Yes, `_id` can be string, UUID, number, or ObjectId as long as it's unique and immutable.
Why: Useful for slugs, tenant keys, or syncing with external IDs like Firebase UID.
How: Provide `_id` on insert; MongoDB enforces unique index automatically.
Example: `db.users.insertOne({_id:"user_asha_01", name:"Asha"})`
Use-case (1 YOE): I used Firebase UID as `_id` to join auth and profile without mapping table.
Mistake/Tip: Custom monotonic IDs hotspot sharding; prefer ObjectId/hashed for scale.
19. **What happens if you omit _id on insert?**
What: MongoDB auto-generates an ObjectId for `_id` to guarantee uniqueness.
Why: Ensures every doc is addressable for updates, refs, and replication without app logic.
How: Driver generates ObjectId client-side before sending, so `insertedId` is known immediately.
Example: `db.users.insertOne({name:"Asha"}) // _id:ObjectId() auto-added`
Use-case (1 YOE): I relied on auto `_id` for posts and referenced it from comments.
Mistake/Tip: Don't manually generate weak IDs like timestamps; collisions break replication.
20. **How do you check if a document exists?**
What: Existence check via `findOne` or `countDocuments(filter,{limit:1})` without fetching full data.
Why: Critical for signup duplicate checks and idempotent webhook handling.
How: Project `_id:1` and limit 1 for minimal cost; index the checked field.
Example: `db.users.findOne({email:"a@test.com"}, {projection:{_id:1}})`
Use-case (1 YOE): I checked email exists before signup to return 409 early.
Mistake/Tip: Don't `find().toArray().length`; use limit-1 count for speed.
21. **How do you limit fields in results?**
What: Projection returns only needed fields, reducing network and memory.
Why: Hides secrets like password and speeds MERN lists on slow networks.
How: Pass `{name:1,email:1,_id:0}` inclusion or `{password:0}` exclusion (can't mix except `_id`).
Example: `db.users.find({}, {name:1, email:1, _id:0})`
Use-case (1 YOE): I projected `name,email,avatar` for user list, excluding `passwordHash`.
Mistake/Tip: Forgetting `_id:0` leaks ids; in Mongoose use `.select("-password")`.
22. **How do you sort results?**
What: `sort({field:1/-1})` orders by ascending/descending, supporting multi-key sorts.
Why: Needed for latest-first feeds, price low-high, and alphabetical lists.
How: Sort uses index if prefix matches; else in-memory sort limited to 32MB.
Example: `db.users.find().sort({age:-1, name:1})`
Use-case (1 YOE): I sorted products by `price:1` then `rating:-1` in listing API.
Mistake/Tip: Sorting without index on large data fails/slow; create index matching sort.
23. **How do you paginate results?**
What: Offset pagination via `.skip(n).limit(m)`; cursor pagination via range on indexed field.
Why: Prevents loading 100k docs at once and enables infinite scroll.
How: `skip((page-1)*limit)` is simple but scans; cursor `({_id:{$gt:lastId}}).limit(10)` is constant-time.
Example: `db.users.find().sort({_id:1}).skip(20).limit(10)`
Use-case (1 YOE): I built `/users?page=3&limit=10` with skip/limit for admin table.
Mistake/Tip: Deep skip is slow; interview tip — propose cursor pagination for scale.
24. **What is `$set` operator?**
What: `$set` sets/creates specific fields without replacing the whole document.
Why: Enables safe partial updates for profile edits and patch APIs.
How: Merges given paths, creating nested fields if needed; combine with `$unset` for removals.
Example: `db.users.updateOne({_id:id}, {$set:{city:"Pune", "address.pin":411001}})`
Use-case (1 YOE): I patched user settings with `$set` from `req.body` allowlist.
Mistake/Tip: Mistake is plain object update wiping doc; always wrap in `$set`.
25. **What is `$unset` operator?**
What: `$unset` removes fields from a document.
Why: Cleans deprecated fields or user-removed data like middleName or avatar.
How: Pass `{$unset:{field:""}}` — value ignored; works with dot notation for nested.
Example: `db.users.updateOne({_id:id}, {$unset:{middleName:""}})`
Use-case (1 YOE): I removed `legacyPhone` after migration to `phones[]`.
Mistake/Tip: `$unset` vs `null` differ — null keeps field; mention for interview depth.
26. **What is `$inc` operator?**
What: `$inc` atomically increments/decrements a numeric field by given amount.
Why: Safe counters for views/likes/stock under concurrency without read-modify-write races.
How: Creates field as 0+inc if missing; use negative to decrement.
Example: `db.posts.updateOne({_id:id}, {$inc:{views:1}})`
Use-case (1 YOE): I counted post views and decremented stock with `$inc:{stock:-qty}`.
Mistake/Tip: Don't read-then-write counters; `$inc` is atomic — stress this.
27. **What is `$push` operator?**
What: `$push` appends value(s) to an array, creating array if missing.
Why: Adds tags, comments, or cart items without fetching whole array.
How: Use `$each` for multiples, `$position` for insert index, `$slice` to cap length.
Example: `db.posts.updateOne({_id:id}, {$push:{tags:{$each:["mern","mongo"]}}})`
Use-case (1 YOE): I pushed new comment IDs to post's `comments` in blog.
Mistake/Tip: Unbounded `$push` hits 16MB; cap with `$slice` or separate collection.
28. **What is `$pull` operator?**
What: `$pull` removes all array elements matching a value/condition.
Why: Removes a tag, unfollows, or deletes cart item atomically.
How: Pass value or query `{scores:{$lt:50}}`; `$pullAll` for multiple exact values.
Example: `db.posts.updateOne({_id:id}, {$pull:{tags:"old"}})`
Use-case (1 YOE): I removed product from wishlist with `$pull:{wishlist:productId}`.
Mistake/Tip: `$pull` scans array; for huge arrays prefer separate collection.
29. **What is `$addToSet` operator?**
What: `$addToSet` adds to array only if not already present, ensuring uniqueness.
Why: Implements likes/follows/tags without app-level duplicate checks or races.
How: Uses `$each` for multiples; creates unique set semantics at DB level.
Example: `db.posts.updateOne({_id:id}, {$addToSet:{likes:userId}})`
Use-case (1 YOE): I prevented double-likes with `$addToSet` + `likesCount` via `$inc` guard.
Mistake/Tip: Slightly slower than `$push`; need unique index alternative for large sets.
30. **What is `bulkWrite()`?**
What: `bulkWrite` batches mixed inserts/updates/deletes in one request with ordered/unordered control.
Why: 10x faster imports/syncs by cutting round-trips for ETL and migration scripts.
How: Pass array of `{insertOne:{document}}`, `{updateOne:{filter,update}}`, `{deleteOne:{filter}}`.
Example: `db.users.bulkWrite([{insertOne:{document:{name:"A"}}}, {updateOne:{filter:{email:"a@test.com"}, update:{$set:{age:25}}}}])`
Use-case (1 YOE): I synced 10k Shopify products nightly with unordered `bulkWrite`.
Mistake/Tip: Default ordered stops on error; use `ordered:false` for best-effort syncs.
31. **How do you query with equality?**
What: Equality filter `{field:value}` matches docs where field equals value (using index if present).
Why: Most common MERN filter — login by email, products by category.
How: BSON type matters; `"24"` != `24`; ObjectId must be typed correctly.
Example: `db.users.find({city:"Mumbai"})`
Use-case (1 YOE): I fetched users by `city` for location filter dropdown.
Mistake/Tip: Type mismatch silently returns empty; validate/cast in Mongoose.
32. **How do you query with `$gt`, `$lt`, `$gte`, `$lte`?**
What: Comparison operators filter ranges on numbers/dates/strings.
Why: Price ranges, age filters, and date windows in listings and reports.
How: Combine in one field `{price:{$gte:100,$lte:500}}`; index supports range scan.
Example: `db.products.find({price:{$gte:100, $lte:500}})`
Use-case (1 YOE): I built price slider filter with `$gte/$lte` in products API.
Mistake/Tip: Range on low-selectivity field still scans many; order ESR index correctly.
33. **How do you query with `$in`?**
What: `$in` matches if field equals any value in given list.
Why: Multi-select filters like cities, tags, or statuses in one query.
How: Uses index; keep list small (<100s) else consider `$lookup` or separate query.
Example: `db.users.find({city:{$in:["Pune","Delhi"]}})`
Use-case (1 YOE): I filtered orders by `status:{$in:["shipped","delivered"]}`.
Mistake/Tip: Huge `$in` lists blow up planning; paginate or normalize.
34. **How do you query with `$nin`?**
What: `$nin` excludes docs matching any listed value (NOT IN).
Why: Blacklists like banned/deleted statuses or muted users.
How: Often non-selective and can't use index efficiently; combine with other filters.
Example: `db.users.find({status:{$nin:["banned","deleted"]}})`
Use-case (1 YOE): I hid blocked posts with `authorId:{$nin:blockedIds}`.
Mistake/Tip: `$nin` with null/missing semantics surprises; test with `$exists`.
35. **How do you query with `$ne`?**
What: `$ne` matches docs where field != value, including missing field docs.
Why: Show all non-admins or non-archived items quickly.
How: `db.users.find({role:{$ne:"admin"}})`; add `$exists:true` if you want field present.
Example: `db.users.find({role:{$ne:"admin"}})`
Use-case (1 YOE): I listed non-admin users for role-assignment UI.
Mistake/Tip: `$ne` is poorly indexed; prefer `$in` allowlist for performance.
36. **How do you combine with `$and`?**
What: `$and` requires all conditions; comma-separated fields already imply AND.
Why: Explicit `$and` needed for multiple conditions on same field or complex nesting.
How: `{ $and:[{age:{$gt:20}},{city:"Pune"}] }` or simply `{age:{$gt:20}, city:"Pune"}`.
Example: `db.users.find({$and:[{age:{$gt:20}}, {city:"Pune"}]})`
Use-case (1 YOE): I filtered candidates by age+city+skills for search.
Mistake/Tip: Redundant `$and` clutters; use implicit AND unless same-field twice.
37. **How do you combine with `$or`?**
What: `$or` matches docs satisfying at least one clause, each clause can use indexes.
Why: Roles, multi-field search (name OR email), or status alternatives.
How: `{$or:[{role:"admin"},{role:"seller"}]}`; each branch planned separately.
Example: `db.users.find({$or:[{role:"admin"}, {role:"seller"}]})`
Use-case (1 YOE): I allowed login by email OR username with `$or`.
Mistake/Tip: Unindexed `$or` branch causes COLLSCAN; index every branch.
38. **How do you negate with `$nor`?**
What: `$nor` matches docs failing all given conditions (NOR logic).
Why: Exclusion filters like neither banned nor underage.
How: `{$nor:[{banned:true},{age:{$lt:18}}]}` returns docs matching none.
Example: `db.users.find({$nor:[{banned:true}, {age:{$lt:18}}]})`
Use-case (1 YOE): I filtered eligible voters as neither banned nor minor.
Mistake/Tip: `$nor` rarely uses indexes; prefer `$nin`/`$ne` combos where possible.
39. **How do you query nested fields?**
What: Dot notation `"address.city"` reaches into embedded objects.
Why: Query address, specs, or meta without unwinding.
How: Index nested path for speed; quote dotted key in shell/JS.
Example: `db.users.find({"address.city":"Pune"})`
Use-case (1 YOE): I searched users by city inside embedded address.
Mistake/Tip: Deep nesting complicates indexes; keep nesting ≤2 levels.
40. **How do you query array contains value?**
What: Simple equality on array field matches if array contains that value.
Why: Tags, roles, or categories stored as arrays for quick filtering.
How: `db.posts.find({tags:"mongodb"})` uses multikey index automatically.
Example: `db.posts.find({tags:"mongodb"})`
Use-case (1 YOE): I filtered blogs by tag without `$elemMatch` for single value.
Mistake/Tip: Case sensitivity bites; normalize tags to lowercase on write.
41. **How do you query array with `$all`?**
What: `$all` requires array to contain all listed values (order irrelevant).
Why: AND for tags — posts with both node AND mongo.
How: `db.posts.find({tags:{$all:["node","mongo"]}})`; index helps but order not guaranteed.
Example: `db.posts.find({tags:{$all:["node","mongo"]}})`
Use-case (1 YOE): I filtered products having all selected features.
Mistake/Tip: `$all` ≠ `$and` on array of objects; use `$elemMatch` for objects.
42. **How do you query array size?**
What: `$size` matches arrays of exact length.
Why: Find posts with 3 tags or users with empty carts.
How: `db.posts.find({tags:{$size:3}})`; can't use index or range — store `tagsCount` for frequent queries.
Example: `db.posts.find({tags:{$size:3}})`
Use-case (1 YOE): I found carts with 0 items via `items:{$size:0}` for abandonment email.
Mistake/Tip: Can't combine `$size` with `$gt`; maintain counter field instead.
43. **What is `$elemMatch`?**
What: Matches array elements satisfying multiple criteria on the same element.
Why: Scores where same entry has subject math AND marks >90 — plain AND would match across elements.
How: `{scores:{$elemMatch:{subject:"math", marks:{$gt:90}}}}` ensures single-element match.
Example: `db.students.find({scores:{$elemMatch:{subject:"math", marks:{$gt:90}}}})`
Use-case (1 YOE): I found variants with size M AND stock >0 in same variant object.
Mistake/Tip: Forgetting `$elemMatch` causes false positives; classic interview trap.
44. **How do you query for field existence?**
What: `$exists:true/false` filters by presence of field.
Why: Find incomplete profiles missing phone or legacy docs without new field.
How: `db.users.find({phone:{$exists:false}})`; index sparse/partial helps.
Example: `db.users.find({phone:{$exists:false}})`
Use-case (1 YOE): I backfilled users missing `avatar` after adding feature.
Mistake/Tip: `null` vs missing differ; combine with `$type`/`$eq:null` as needed.
45. **How do you query for null?**
What: `{field:null}` matches explicit null OR missing field — a common gotcha.
Why: Distinguish unset vs intentionally nulled phone numbers.
How: Add `$exists:true` to match only explicit null: `{phone:{$in:[null], $exists:true}}` pattern.
Example: `db.users.find({phone:null}) // add {phone:{$type:"null"}} for strict`
Use-case (1 YOE): I audited users with null phone vs missing phone separately.
Mistake/Tip: Interview favorite — always mention null matches missing too.
46. **How do you do text search?**
What: Text index + `$text` enables stemmed full-text relevance search with scores.
Why: Blog/product search by keywords without external Elastic for MVP.
How: Create `createIndex({title:"text",body:"text"})` then `find({$text:{$search:"mern interview"}})`.
Example: `db.posts.find({$text:{$search:"mern interview"}}, {score:{$meta:"textScore"}}).sort({score:{$meta:"textScore"}})`
Use-case (1 YOE): I added blog search with text score sorting in 1 hour.
Mistake/Tip: Only one text index per collection; for advanced need Atlas Search.
47. **How do you do regex search?**
What: `$regex` pattern-matches strings with options like `i` for case-insensitive.
Why: Autocomplete, prefix search, email domain filter.
How: `db.users.find({name:{$regex:"^ash", $options:"i"}})`; anchored prefix can use index, leading wildcard cannot.
Example: `db.users.find({name:{$regex:"^ash", $options:"i"}})`
Use-case (1 YOE): I built user autocomplete with prefix regex + limit 10.
Mistake/Tip: `/.*ash.*/` full scans; prefer text index or Atlas Search for contains.
48. **How do you query dates?**
What: Store dates as BSON Date (ISODate) and query with comparison operators.
Why: Ranges for orders, logs, and analytics by day/month.
How: `db.orders.find({createdAt:{$gte:ISODate("2025-01-01")}})`; index date field.
Example: `db.orders.find({createdAt:{$gte:ISODate("2025-01-01"), $lt:ISODate("2025-02-01")}})`
Use-case (1 YOE): I fetched this month's orders for revenue report.
Mistake/Tip: Storing dates as strings breaks sorting; always use Date type.
49. **What is `$expr`?**
What: `$expr` allows aggregation expressions inside `find`, comparing fields within same doc.
Why: Find where `price > cost` or `qty*price > 1000` without aggregation.
How: `{$expr:{$gt:["$price","$cost"]}}` references fields with `$`.
Example: `db.products.find({$expr:{$gt:["$price","$cost"]}})`
Use-case (1 YOE): I flagged loss-making products where discount pushed price below cost.
Mistake/Tip: `$expr` may not use indexes efficiently; prefer normal query when possible.
50. **How do you handle case-insensitive queries?**
What: Collation `{locale:"en", strength:2}` or regex `i` enables case-insensitive matching.
Why: Login by email or search by name should ignore case.
How: `find({email}).collation({locale:"en",strength:2})` with case-insensitive index is fastest.
Example: `db.users.find({email:"ASHA@test.com"}).collation({locale:"en", strength:2})`
Use-case (1 YOE): I made email login case-insensitive with collation index.
Mistake/Tip: Regex `i` is slow at scale; create collation index — strong interview point.
51. **What is projection with `$slice`?**
What: `$slice` in projection returns a subset of an array without fetching the whole array.
Why: Preview last 5 comments or first image to save bandwidth on feeds.
How: `{comments:{$slice:-5}}` for last 5, `{comments:{$slice:[0,10]}}` for first 10.
Example: `db.posts.find({_id:id}, {comments:{$slice:-5}})`
Use-case (1 YOE): I showed post preview with last 5 comments on homepage.
Mistake/Tip: `$slice` is projection-only; for aggregation use `$slice` expression differently.
52. **What is `$where` and why avoid it?**
What: `$where` runs JS per document for complex logic that query operators can't express.
Why: Avoid it — it can't use indexes, is slow, and risks injection if built from user input.
How: Prefer `$expr` or aggregation; if must, use function with indexed pre-filter.
Example: `db.users.find({$where:"this.age > this.limit"}) // prefer {$expr:{$gt:["$age","$limit"]}}`
Use-case (1 YOE): I replaced legacy `$where` age check with `$expr` and cut latency 10x.
Mistake/Tip: Never concat user input into `$where`; interview red flag if you suggest it first.
53. **How do you find distinct values?**
What: `distinct(field)` returns unique values for a field across matches.
Why: Populate filter dropdowns like unique cities or categories.
How: `db.users.distinct("city", {status:"active"})` with optional filter; uses index if available.
Example: `db.users.distinct("city")`
Use-case (1 YOE): I built category dropdown from `products.distinct("category")`.
Mistake/Tip: Large-cardinality distinct scans many; cache results in Redis.
54. **How do you query geospatial nearby?**
What: `2dsphere` index + `$near` finds GeoJSON points near a location within distance.
Why: Nearby shops, drivers, or delivery partners sorted by distance.
How: Store `{loc:{type:"Point",coordinates:[lng,lat]}}`, index `2dsphere`, query with `$geometry`.
Example: `db.shops.find({loc:{$near:{$geometry:{type:"Point",coordinates:[73.85,18.52]}, $maxDistance:5000}}})`
Use-case (1 YOE): I showed restaurants within 5km in food-delivery clone.
Mistake/Tip: Coordinates are [lng,lat] not lat,lng — classic bug.
55. **What is `$type` operator?**
What: `$type` filters by BSON type to find dirty data like numbers stored as strings.
Why: Audit schema drift after loose validation or CSV imports.
How: `{age:{$type:"string"}}` or `{$type:["string","null"]}` for multiples.
Example: `db.users.find({age:{$type:"string"}})`
Use-case (1 YOE): I found prices imported as strings and migrated them to Decimal128.
Mistake/Tip: Numeric type codes are confusing; use string aliases like "string".
56. **How do you paginate with cursor?**
What: Cursor pagination uses range on indexed `_id`/`createdAt` instead of `skip`.
Why: Constant-time pages and stable infinite scroll even with concurrent inserts.
How: `find({_id:{$gt:lastId}}).sort({_id:1}).limit(10)`; client sends `lastId`.
Example: `db.users.find({_id:{$gt:ObjectId("65a...")}}).sort({_id:1}).limit(10)`
Use-case (1 YOE): I built Instagram-like feed with `lastId` cursor for smooth scroll.
Mistake/Tip: Don't mix skip+cursor; handle sort direction for prev/next correctly.
57. **How do you filter subdocuments in array?**
What: `$elemMatch` in find matches docs; `$filter` in aggregation returns only matching elements.
Why: Show only in-stock variants or passing scores without returning whole array.
How: Find: `{items:{$elemMatch:{stock:{$gt:0}}}}`; Agg: `{$project:{items:{$filter:{input:"$items", cond:{$gt:["$$this.stock",0]}}}}}`
Example: `db.orders.find({items:{$elemMatch:{productId:id, qty:{$gte:2}}}})`
Use-case (1 YOE): I returned only available sizes for product detail page.
Mistake/Tip: `$elemMatch` filters docs not array contents — need `$filter` to trim array.
58. **What is covered query?**
What: Covered query is answered from index alone without fetching documents.
Why: Fastest reads — minimal IO for counts and id lookups.
How: All query + projection + sort fields must be in index and projection must exclude `_id` unless indexed.
Example: `db.users.find({email:"a@test.com"}, {_id:0, email:1}).hint("email_1") // IXSCAN, no FETCH`
Use-case (1 YOE): I covered email-exists check with `{email:1}` index for signup speed.
Mistake/Tip: Including `_id` without index breaks coverage; verify with `explain()`.
59. **How do you search MERN products by name and category?**
What: Combined regex on name + equality on category with compound index.
Why: Typical e-commerce search bar + category dropdown.
How: `{category, name:{$regex:q,$options:"i"}}` with index `{category:1, name:1}`.
Example: `db.products.find({category:"mobiles", name:{$regex:"realme", $options:"i"}})`
Use-case (1 YOE): I built product search with category filter and debounced regex.
Mistake/Tip: Leading-wildcard regex ignores index; consider text index for contains.
60. **How do you implement search + filter + sort API?**
What: Express controller builds dynamic Mongo filter/sort/skip/limit from whitelisted query params.
Why: One `/products?q=&category=&sort=&page=` endpoint powers listing pages.
How: Parse `req.query`, build `{filter}`, call `.sort().skip().limit()` plus `countDocuments` for total.
Example: `Product.find(filter).sort({[sort]:order}).skip((page-1)*limit).limit(limit).lean()`
Use-case (1 YOE): I shipped product listing API with search/filter/sort in MERN shop.
Mistake/Tip: Never pass `req.query` directly — NoSQL injection; whitelist and cast.
61. **What is an index in MongoDB?**
What: B-tree structure that avoids full collection scans; `_id` index exists by default.
Why: Turns O(n) COLLSCAN into O(log n) IXSCAN for filters/sorts.
How: Created on fields, used automatically by planner; verify with `explain()`.
Example: `db.users.createIndex({email:1}) // then find({email}) uses IXSCAN`
Use-case (1 YOE): I cut login query from 800ms to 5ms by indexing email.
Mistake/Tip: Over-indexing slows writes; index only queried/sorted fields.
62. **How do you create an index?**
What: `createIndex(keys, options)` builds ascending/descending index on field(s).
Why: Speed filters, sorts, and enforce uniqueness.
How: `{email:1}` ascending, `{age:-1}` descending; background build on live systems.
Example: `db.users.createIndex({email:1}, {unique:true})`
Use-case (1 YOE): I added `{createdAt:-1}` for latest-first feed.
Mistake/Tip: Building index on huge collection blocks; use rolling build/Atlas.
63. **What is a unique index?**
What: Enforces uniqueness — duplicate insert fails with E11000.
Why: Deduplicate emails/usernames at DB level, race-safe unlike app checks.
How: `createIndex({email:1},{unique:true})`; handle error in API with 409.
Example: `db.users.createIndex({email:1}, {unique:true})`
Use-case (1 YOE): I prevented duplicate signups even under double-click race.
Mistake/Tip: `unique:true` in Mongoose is index not validator — must catch E11000.
64. **What is a compound index?**
What: Index on multiple fields supporting filtered sorts in one scan.
Why: E-commerce `{category:1, price:-1}` for category filter + price sort.
How: Order matters — follows ESR (Equality, Sort, Range); prefix queries use it.
Example: `db.products.createIndex({category:1, price:-1})`
Use-case (1 YOE): I sped category+price listing with compound index.
Mistake/Tip: Wrong field order wastes index; test with `explain()`.
65. **What is index order ESR rule?**
What: ESR = Equality first, Sort second, Range last for optimal compound index design.
Why: Maximizes index efficiency by narrowing, ordering, then scanning ranges.
How: Query `{status:"active", sort:{age:1}, price:{$gt:100}}` → index `{status:1, age:1, price:1}`.
Example: `db.users.createIndex({status:1, age:1, price:1}) // E,S,R`
Use-case (1 YOE): I reordered index to ESR and fixed slow admin filter.
Mistake/Tip: Putting range before sort forces in-memory sort — common failure.
66. **What is a text index?**
What: Special index enabling `$text` stemmed search across string fields; one per collection.
Why: Quick MVP search on title+body without external engine.
How: `createIndex({title:"text",body:"text"})` with weights; query with `$meta` score.
Example: `db.posts.createIndex({title:"text", body:"text"})`
Use-case (1 YOE): I added blog search ranking title higher via weights.
Mistake/Tip: Only one text index — combine fields; for fuzzy need Atlas Search.
67. **What is a 2dsphere index?**
What: Geospatial index for GeoJSON points/polygons supporting `$near`/`$geoWithin`.
Why: Location apps — nearby drivers, stores, delivery zones.
How: `createIndex({loc:"2dsphere"})` on `{type:"Point",coordinates:[lng,lat]}`.
Example: `db.places.createIndex({loc:"2dsphere"})`
Use-case (1 YOE): I enabled 5km restaurant search in delivery app.
Mistake/Tip: Forgetting GeoJSON format breaks queries; validate lng/lat ranges.
68. **What is a TTL index?**
What: Auto-deletes docs after seconds via background thread (60s granularity).
Why: OTPs, sessions, temp tokens without cron jobs.
How: `createIndex({createdAt:1},{expireAfterSeconds:3600})`; field must be Date.
Example: `db.otps.createIndex({createdAt:1}, {expireAfterSeconds:300})`
Use-case (1 YOE): I auto-expired OTPs after 5 mins and sessions after 1h.
Mistake/Tip: Not exact-time — up to 60s delay; don't use for precise expiry logic.
69. **What is a partial index?**
What: Indexes only docs matching filter expression — smaller, faster, cheaper.
Why: Index active users only when 90% queries filter `status:"active"`.
How: `{partialFilterExpression:{status:"active"}}` on `{email:1}`.
Example: `db.users.createIndex({email:1}, {partialFilterExpression:{status:"active"}})`
Use-case (1 YOE): I indexed active sellers only, halving index size.
Mistake/Tip: Query must include same filter to use partial index.
70. **What is a sparse index?**
What: Only indexes docs containing the field; skips missing-field docs.
Why: Optional fields like `phone` without indexing nulls.
How: `{sparse:true}`; largely superseded by partial indexes which are more explicit.
Example: `db.users.createIndex({phone:1}, {sparse:true})`
Use-case (1 YOE): I sparsely indexed optional referral codes.
Mistake/Tip: Deprecated pattern — prefer partial; sparse unique behaves oddly with nulls.
71. **How do you list indexes?**
What: `getIndexes()` shows all indexes with keys, options, and sizes.
Why: Audit duplicates/missing before perf tuning or deploys.
How: `db.users.getIndexes()` in shell; `User.listIndexes()` in Mongoose.
Example: `db.users.getIndexes()`
Use-case (1 YOE): I found duplicate `email_1` + `email_unique` wasting writes.
Mistake/Tip: Don't guess — always list and `explain()` before adding new index.
72. **How do you drop an index?**
What: `dropIndex(name)` removes one; `dropIndexes()` removes all except `_id`.
Why: Remove unused/slow-write indexes after query pattern changes.
How: `db.users.dropIndex("email_1")`; get name from `getIndexes()`.
Example: `db.users.dropIndex("email_1")`
Use-case (1 YOE): I dropped low-use `age_1` index that slowed bulk import.
Mistake/Tip: Dropping in prod spikes queries; recreate during off-peak.
73. **What is `explain()`?**
What: Shows query plan — stages, index use, docs examined vs returned.
Why: Prove IXSCAN vs COLLSCAN and justify index additions.
How: `find({email}).explain("executionStats")`; check `totalDocsExamined` ≈ `nReturned`.
Example: `db.users.find({email:"a@test.com"}).explain("executionStats")`
Use-case (1 YOE): I proved missing index caused 100k scans for login.
Mistake/Tip: `queryPlanner` alone insufficient; use `executionStats` for real numbers.
74. **What is COLLSCAN vs IXSCAN?**
What: COLLSCAN scans all docs (slow); IXSCAN traverses index (fast).
Why: Production queries must be IXSCAN to scale beyond thousands of docs.
How: Check `explain()` winningPlan; add index to convert COLLSCAN → IXSCAN.
Example: `db.users.find({email:"x"}).explain() // want IXSCAN on email_1`
Use-case (1 YOE): I fixed feed COLLSCAN by adding `{createdAt:-1}` index.
Mistake/Tip: Small dev collections hide COLLSCAN; test with realistic data size.
75. **How do indexes affect writes?**
What: Each index adds write overhead + storage — every insert/update/delete updates all indexes.
Why: Tradeoff: faster reads vs slower writes and RAM pressure.
How: Keep 5-10 useful indexes; monitor `db.users.stats()` for index sizes.
Example: `db.users.stats() // check indexSizes`
Use-case (1 YOE): I removed 4 unused indexes and bulk import went 2x faster.
Mistake/Tip: Indexing every field is anti-pattern; measure with profiler.
76. **What is index selectivity?**
What: High-cardinality fields (email) benefit more than low-cardinality (gender).
Why: Selective indexes narrow to few docs; non-selective still scans many.
How: Prefer `{email:1}` over `{gender:1}` alone; combine low-cardinality into compound.
Example: `db.users.createIndex({email:1}) // high selectivity`
Use-case (1 YOE): I replaced `status` single index with `{status:1, createdAt:-1}` compound.
Mistake/Tip: Don't single-index booleans; compound them.
77. **What is a covered query with index?**
What: Query + projection + sort all served from index without FETCH stage.
Why: Minimal IO — ideal for existence checks and dropdowns.
How: Ensure fields in index, project only indexed fields with `_id:0`.
Example: `db.users.find({email:"a@test.com"}, {_id:0, email:1}) // covered by email_1`
Use-case (1 YOE): I covered username autocomplete for sub-10ms latency.
Mistake/Tip: Verify `totalDocsExamined:0` in explain; else not covered.
78. **How do you index for sort?**
What: Create index matching sort order to avoid in-memory 32MB sort limit.
Why: Latest-first feeds and price sorts need indexed order.
How: `createIndex({createdAt:-1})` for `sort({createdAt:-1})`; compound order must match.
Example: `db.posts.createIndex({createdAt:-1})`
Use-case (1 YOE): I fixed feed sort overflow by adding desc index.
Mistake/Tip: Asc vs desc matters in compound sorts; mismatch causes in-memory sort.
79. **How do you enforce unique username in MERN?**
What: DB unique index + Mongoose `unique:true` + E11000 handling for race safety.
Why: App-level `findOne` check alone races under double submit.
How: `schema.index({username:1},{unique:true})`, catch `err.code===11000` → 409.
Example: `User.create({username, email}) // catch E11000 → "Username taken"`
Use-case (1 YOE): I enforced unique handle in Twitter clone with collation strength 2.
Mistake/Tip: Forgetting to handle E11000 crashes signup; always map to 409.
80. **How many indexes per collection?**
What: Max 64 per collection, but 5-10 in practice to balance reads vs writes.
Why: Too many inflate RAM, slow writes, and confuse planner.
How: Audit with `getIndexes()` + profiler; drop unused, merge into compounds.
Example: `db.users.aggregate([{$indexStats:{}}]) // check usage`
Use-case (1 YOE): I trimmed 15 to 7 indexes after `$indexStats` review.
Mistake/Tip: Creating index per query without merging — prefer ESR compounds.
81. **What is aggregation pipeline?**
What: Multi-stage framework (`$match`→`$group`→`$sort`) for analytics/joins/reports.
Why: Does in-DB what would need multiple finds + JS loops in Node.
How: `db.orders.aggregate([{$match:{status:"paid"}}, {$group:{_id:"$city", total:{$sum:"$amount"}}}])`.
Example: `db.orders.aggregate([{$match:{status:"paid"}}, {$group:{_id:"$city", total:{$sum:1}}}])`
Use-case (1 YOE): I built revenue-by-city dashboard with one pipeline.
Mistake/Tip: Putting `$group` before `$match` scans everything; filter early.
82. **What does `$match` do?**
What: Filters docs like `find`; should be first to reduce data and use indexes.
Why: Early filtering cuts memory and lets optimizer use indexes.
How: `{$match:{status:"paid", createdAt:{$gte:start}}}` with indexed fields.
Example: `{$match:{status:"paid"}} // first stage`
Use-case (1 YOE): I pre-filtered paid orders before grouping for monthly revenue.
Mistake/Tip: Late `$match` after `$group` wastes work; move selective filters first.
83. **What does `$group` do?**
What: Groups by `_id` key and accumulates with `$sum`/`$avg`/`$push`.
Why: Counts per category, revenue per month, ratings per product.
How: `{$group:{_id:"$category", total:{$sum:1}, avgPrice:{$avg:"$price"}}}`
Example: `{$group:{_id:"$category", total:{$sum:1}}}`
Use-case (1 YOE): I counted users per city for admin chart.
Mistake/Tip: Grouping without index + huge cardinality spills to disk; add `$match` first.
84. **What does `$project` do?**
What: Reshapes docs — include/rename/compute fields, exclude `_id` if needed.
Why: Return only UI-needed fields and derive year/month/fullName.
How: `{$project:{name:1, year:{$year:"$createdAt"}, _id:0}}`
Example: `{$project:{name:1, year:{$year:"$createdAt"}}}`
Use-case (1 YOE): I projected order `year,month,total` for chart API.
Mistake/Tip: Late `$project` wastes memory; project early to trim fields.
85. **What does `$sort` do?**
What: Orders pipeline docs by fields `1/-1`, typically after `$group` for Top-N.
Why: Leaderboards, top products, latest orders.
How: `{$sort:{total:-1}}` + `{$limit:5}`; uses index if early `$sort` on indexed field.
Example: `{$sort:{total:-1}}`
Use-case (1 YOE): I sorted categories by sales desc for homepage.
Mistake/Tip: Sorting huge unindexed data hits 100MB limit; add `allowDiskUse:true` or index.
86. **What does `$limit` and `$skip` do?**
What: `$limit:N` takes top N; `$skip:N` discards first N for pages.
Why: Paginate aggregation results without returning all groups.
How: Place after `$sort`: `{$sort:{total:-1}}, {$skip:20}, {$limit:10}`.
Example: `{$sort:{total:-1}}, {$limit:5}`
Use-case (1 YOE): I paginated top-seller report page-by-page.
Mistake/Tip: Deep `$skip` still scans; prefer `$facet` + cursor for large reports.
87. **What does `$lookup` do?**
What: Left-joins another collection (like populate but in-DB).
Why: Orders with user details in one query instead of N+1 finds.
How: `{$lookup:{from:"users", localField:"userId", foreignField:"_id", as:"user"}}` + `$unwind`.
Example: `{$lookup:{from:"users", localField:"userId", foreignField:"_id", as:"user"}}`
Use-case (1 YOE): I joined orders→users for admin order table.
Mistake/Tip: Forgetting `$unwind` leaves array; also ensure indexed foreignField.
88. **What does `$unwind` do?**
What: Flattens array into one doc per element for per-element grouping.
Why: Group by tag or sum per cart item.
How: `{$unwind:"$tags"}`; use `preserveNullAndEmptyArrays:true` to keep empties.
Example: `{$unwind:"$tags"}`
Use-case (1 YOE): I unwound `items` to sum revenue per product.
Mistake/Tip: Unwinding huge arrays explodes docs; `$match` first.
89. **What does `$count` do?**
What: Counts pipeline docs and outputs `{fieldName: N}`.
Why: Totals after filters for dashboard badges.
How: `{$count:"totalUsers"}` as final stage.
Example: `db.users.aggregate([{$match:{active:true}}, {$count:"total"}])`
Use-case (1 YOE): I counted premium users after match for pricing page stats.
Mistake/Tip: `$count` ends pipeline — can't add stages after except `$addFields`.
90. **What does `$facet` do?**
What: Runs multiple sub-pipelines in parallel on same input — data + total in one trip.
Why: Paginated list + count without two queries.
How: `{$facet:{data:[{$skip},{$limit}], total:[{$count:"n"}]}}`
Example: `{$facet:{data:[{$skip:20},{$limit:10}], total:[{$count:"n"}]}}`
Use-case (1 YOE): I returned products page + totalPages in one aggregation.
Mistake/Tip: `$facet` can't use indexes after split; keep pre-facet `$match` indexed.
91. **How do you sum revenue per month?**
What: Group by month extracted from date and sum amount, then sort.
Why: Monthly P&L chart in admin dashboard.
How: `{$group:{_id:{$month:"$createdAt"}, revenue:{$sum:"$amount"}}}, {$sort:{_id:1}}`
Example: `{$group:{_id:{$month:"$createdAt"}, revenue:{$sum:"$amount"}}}`
Use-case (1 YOE): I built SaaS MRR chart grouping subscriptions by month.
Mistake/Tip: `$month` loses year; group by `{y:{$year}, m:{$month}}` for multi-year.
92. **How do you get top 5 products?**
What: Group sales by product, sort desc, limit 5.
Why: Bestsellers carousel and inventory priority.
How: `{$group:{_id:"$productId", qty:{$sum:"$qty"}}}, {$sort:{qty:-1}}, {$limit:5}`
Example: `{$group:{_id:"$productId", qty:{$sum:"$qty"}}}, {$sort:{qty:-1}}, {$limit:5}`
Use-case (1 YOE): I showed top 5 selling phones on homepage.
Mistake/Tip: Grouping all history is heavy; `$match` recent window first.
93. **What is `$addFields`?**
What: Adds/computes new fields without listing all existing ones (vs `$project`).
Why: Derive `fullName` or `total = qty*price` while keeping all fields.
How: `{$addFields:{fullName:{$concat:["$first"," ","$last"]}}}`
Example: `{$addFields:{total:{$multiply:["$qty","$price"]}}}`
Use-case (1 YOE): I computed cart line totals in pipeline for checkout.
Mistake/Tip: Overwriting existing field silently; check names.
94. **What is `$replaceRoot`?**
What: Promotes subdocument to top-level for clean output after `$lookup`.
Why: Flatten joined user object so API returns `{orderId, name}` not nested array.
How: After `$unwind:"$user"`, do `{$replaceRoot:{newRoot:"$user"}}` or merge.
Example: `{$replaceRoot:{newRoot:{$mergeObjects:["$$ROOT","$user"]}}}`
Use-case (1 YOE): I flattened order+user join for CSV export.
Mistake/Tip: Loses original fields if not merged; use `$mergeObjects` to keep both.
95. **How do you paginate with aggregation?**
What: `$facet` with `data:[$skip,$limit]` + `total:[$count]` returns page + total together.
Why: Avoids two round-trips for table pagination.
How: Precede with `$match`+`$sort`, then single `$facet`.
Example: `{$facet:{data:[{$skip:20},{$limit:10}], total:[{$count:"n"}]}}`
Use-case (1 YOE): I paginated filtered orders with totalPages in one call.
Mistake/Tip: `$facet` loads all in memory; keep pre-facet result small.
96. **What is `$bucket`?**
What: Groups numbers/dates into ranges (buckets) for histograms.
Why: Price filters 0-100, 100-500 counts for faceted search.
How: `{$bucket:{groupBy:"$price", boundaries:[0,100,500,1000]}}`
Example: `{$bucket:{groupBy:"$price", boundaries:[0,100,500,1000], default:"Other"}}`
Use-case (1 YOE): I built price-range facet counts for filters UI.
Mistake/Tip: Boundaries must be sorted; use `$bucketAuto` for auto ranges.
97. **How to optimize aggregation?**
What: `$match`+`$project` early, use indexes, limit fields, avoid `$group` on huge sets.
Why: Pipelines easily OOM or COLLSCAN without discipline.
How: Filter first, project needed fields, ensure `$match`/`$sort` hit indexes.
Example: `// good: [$match, $project, $group, $sort, $limit]`
Use-case (1 YOE): I cut report from 12s to 900ms by moving `$match` first.
Mistake/Tip: `$lookup` without index on foreignField is killer; always index join keys.
98. **Can aggregation use indexes?**
What: Yes, early `$match`/`$sort` can use indexes if they match prefix and precede transforms.
Why: Indexed pre-filter makes pipelines scale to millions.
How: Place `$match` on indexed field first; check `explain:true`.
Example: `db.orders.aggregate([{$match:{status:"paid"}}, {$sort:{createdAt:-1}}], {explain:true})`
Use-case (1 YOE): I indexed `status+createdAt` to speed monthly sales pipeline.
Mistake/Tip: `$group`/`$unwind` before `$match` blocks index use.
99. **How to join in MERN orders API?**
What: `$lookup` orders→users then `$unwind`+`$project` for order with customer name/email.
Why: Admin table needs order + customer in one fetch.
How: Lookup, unwind, project `{orderId, amount, "user.name":1}`.
Example: `Order.aggregate([{$lookup:{from:"users", localField:"userId", foreignField:"_id", as:"u"}}, {$unwind:"$u"}, {$project:{amount:1, "u.name":1}}])`
Use-case (1 YOE): I built orders admin API with customer details joined.
Mistake/Tip: N+1 `findById` loop is slower; prefer single pipeline.
100. **How to compute average rating?**
What: `$group` by product with `$avg` stars and `$sum` count.
Why: Product cards show 4.3★ (120 reviews).
How: `{$group:{_id:"$productId", avg:{$avg:"$stars"}, count:{$sum:1}}}`
Example: `{$group:{_id:"$productId", avg:{$avg:"$stars"}, count:{$sum:1}}}`
Use-case (1 YOE): I computed ratings for 10k reviews nightly via pipeline.
Mistake/Tip: `$avg` ignores non-numerics silently; validate stars 1-5.
101. **How to filter after grouping?**
What: `$match` after `$group` acts like SQL HAVING to keep groups meeting condition.
Why: Show categories with total >100 or customers with >5 orders.
How: `{$group:{_id:"$city", total:{$sum:1}}}, {$match:{total:{$gt:100}}}`
Example: `{$group:{_id:"$city", total:{$sum:1}}}, {$match:{total:{$gt:100}}}`
Use-case (1 YOE): I filtered power buyers with >10 orders for loyalty email.
Mistake/Tip: Don't confuse pre-group `$match` (WHERE) vs post-group `$match` (HAVING).
102. **What is `$out` vs `$merge`?**
What: Both write pipeline results to collection; `$out` overwrites, `$merge` upserts/merges.
Why: Materialize nightly reports without app loops.
How: End pipeline with `{$merge:{into:"monthly_sales", on:"_id", whenMatched:"replace"}}`.
Example: `{$merge:{into:"reports", on:"_id", whenMatched:"merge"}} // $out:{db:"x", coll:"y"} overwrites`
Use-case (1 YOE): I materialized daily sales into `reports` for fast dashboard reads.
Mistake/Tip: `$out` drops existing data — dangerous; prefer `$merge`.
103. **How to unwind with empty arrays?**
What: Default `$unwind` drops docs with missing/empty arrays; preserve flag keeps them.
Why: Keep posts with zero tags or orders with no items in reports.
How: `{$unwind:{path:"$tags", preserveNullAndEmptyArrays:true}}`
Example: `{$unwind:{path:"$tags", preserveNullAndEmptyArrays:true}}`
Use-case (1 YOE): I kept users with no orders in left-join-like report.
Mistake/Tip: Forgetting flag silently drops docs — counts mismatch mystery.
104. **What is `$arrayElemAt`?**
What: Returns nth array element for thumbnails or first/last values.
Why: Show first image as cover without fetching all images.
How: `{$project:{thumb:{$arrayElemAt:["$images",0]}}}`
Example: `{$project:{thumb:{$arrayElemAt:["$images",0]}}}`
Use-case (1 YOE): I returned product thumbnail from `images[0]` in listing.
Mistake/Tip: Out-of-bounds returns null — handle fallback image in UI.
105. **How to debug slow aggregation?**
What: `explain:true` on aggregate shows per-stage plans and index use.
Why: Pinpoint COLLSCAN stage or memory spill.
How: `db.coll.aggregate(pipeline,{explain:true})` or Atlas Profiler.
Example: `db.orders.aggregate([{$match:{status:"paid"}}], {explain:true})`
Use-case (1 YOE): I found `$lookup` without index caused 9s pipeline.
Mistake/Tip: Don't guess — always explain; check `docsExamined` per stage.
106. **Embed vs reference in schema design?**
What: Embed when data accessed together (one-to-few); reference when large/many/shared.
Why: Embedding gives single-fetch reads; referencing avoids duplication and 16MB limit.
How: Embed address in user; reference orders→users via `userId`.
Example: `{name:"Asha", address:{city:"Pune"}} // vs {authorId:ObjectId("...")}`
Use-case (1 YOE): I embedded address but referenced orders for my shop.
Mistake/Tip: Say it depends on read/write ratio — interviewers want tradeoffs.
107. **When to embed comments?**
What: Embed if few, small, always shown with post; separate collection if huge/paginated/queried alone.
Why: Embedding avoids join for small threads but blows 16MB for viral posts.
How: Embed `comments:[{user,text,at}]` capped via `$slice`; else `comments` collection with `postId` index.
Example: `db.posts.updateOne({_id:id}, {$push:{comments:{user:"A", text:"nice"}}})`
Use-case (1 YOE): I embedded ≤50 comments for MVP, moved to collection after growth.
Mistake/Tip: Unbounded embed is classic fail; mention cap + migration plan.
108. **When to reference products in orders?**
What: Reference by `productId` because products shared, updated independently, reused across orders.
Why: Embedding full product duplicates price/specs and goes stale on price change.
How: Store `{productId, qty, priceAtPurchase}` snapshot + ref for current details.
Example: `{items:[{productId:ObjectId("..."), qty:2, price:499}]}`
Use-case (1 YOE): I snapshotted price at order time but linked ID for catalog.
Mistake/Tip: Storing only live price breaks history; snapshot price.
109. **What is one-to-many pattern?**
What: One parent links many children via parent ref in child or array of ids in parent.
Why: User→posts or post→comments relationships.
How: Child holds `authorId` with index, or parent holds `postIds[]` if few.
Example: `db.posts.insertOne({title:"Hi", authorId:ObjectId("...")})`
Use-case (1 YOE): I stored `authorId` in posts for fast author filter.
Mistake/Tip: Giant `ids[]` arrays hit 16MB; prefer child-side ref for many.
110. **What is many-to-many pattern?**
What: Both sides link many — use junction collection or arrays both sides.
Why: Students↔courses enrollments with extra fields like grade/date.
How: `enrollments:{studentId, courseId, grade}` with compound indexes.
Example: `db.enrollments.insertOne({studentId:ObjectId("..."), courseId:ObjectId("...")})`
Use-case (1 YOE): I modeled users↔groups via memberships with role field.
Mistake/Tip: Dual arrays desync; single junction collection is source of truth.
111. **What is denormalization?**
What: Duplicate small stable fields like `authorName` in post to avoid `$lookup`.
Why: Feed reads 10x faster by skipping joins at cost of update fan-out.
How: Store `author:{id,name,avatar}` snapshot; update on profile change via async job.
Example: `db.posts.insertOne({title:"Hi", authorId:id, authorName:"Asha"})`
Use-case (1 YOE): I denormalized seller name in products for fast cards.
Mistake/Tip: Forgetting sync causes stale names; mention eventual-consistency job.
112. **What is bucket pattern?**
What: Group time-series into hourly/daily bucket docs to avoid huge arrays and 16MB limit.
Why: IoT/sensor logs or views per hour would explode single doc.
How: `{day:"2025-01-01", measurements:[...]}` with 24*60 capped entries per bucket.
Example: `{sensorId:id, hour:ISODate("2025-01-01T10:00:00Z"), readings:[12,15,14]}`
Use-case (1 YOE): I bucketed page-views hourly for analytics dashboard.
Mistake/Tip: Don't bucket too coarse (hot doc) or too fine (too many docs).
113. **How to model MERN blog?**
What: `users`, `posts{authorId}`, `comments{postId}` with indexes for paginated fetch.
Why: Separates growing comments from posts for scale and independent queries.
How: Index `posts.authorId`, `comments.postId+createdAt`; populate via `$lookup`.
Example: `db.comments.createIndex({postId:1, createdAt:-1})`
Use-case (1 YOE): I built blog with cursor-paginated comments per post.
Mistake/Tip: Embedding all comments fails at viral scale; reference + paginate.
114. **How to model e-commerce cart?**
What: Embed `items[{productId,qty,price}]` in user for fast reads; reference products for details.
Why: Cart is small, per-user, always fetched with user — single read.
How: Cap items, `$inc` qty or `$push` new, snapshot price.
Example: `db.users.updateOne({_id:u}, {$push:{cart:{productId:p, qty:1, price:499}}})`
Use-case (1 YOE): I stored cart embedded for sub-50ms checkout fetch.
Mistake/Tip: Don't embed full product docs; store id+qty+price snapshot.
115. **How to model likes?**
What: `likesCount` + separate `likes{userId,postId}` with compound unique index.
Why: Prevents duplicates race-safe and avoids 16MB likes array on viral posts.
How: `createIndex({userId:1,postId:1},{unique:true})`, `$inc` count on insert.
Example: `db.likes.createIndex({userId:1, postId:1}, {unique:true})`
Use-case (1 YOE): I scaled likes to 100k/post with this pattern.
Mistake/Tip: `$addToSet` array fails at scale; separate collection wins.
116. **How to handle 16MB limit?**
What: Avoid unbounded arrays; split into separate collection with parent ref + paginate.
Why: Viral comments/l Logs exceed single-doc cap and break writes.
How: Move to child collection `{parentId}` indexed, or bucket pattern.
Example: `db.comments.find({postId:id}).sort({createdAt:-1}).limit(20)`
Use-case (1 YOE): I migrated embedded chat history to messages collection.
Mistake/Tip: Interview must-mention: 16MB + strategy (ref/bucket/GridFS).
117. **Should you store images in MongoDB?**
What: No — store S3/Cloudinary URLs; GridFS only if you must store >16MB files in DB.
Why: DB bloat slows replication/backups; CDN serves images faster/cheaper.
How: Upload to S3, save `{images:["https://cdn/...jpg"]}`.
Example: `{title:"Shoe", images:["https://cdn/shop/shoe1.jpg"]}`
Use-case (1 YOE): I stored Cloudinary URLs for product images in MERN shop.
Mistake/Tip: Base64 in docs explodes size; always use object storage.
118. **How to model hierarchical categories?**
What: Materialized path `path:",electronics,mobiles,"` or parent ref for subtree queries.
Why: Fetch all descendants with prefix regex in one query.
How: `find({path:{$regex:"^,electronics,"}})` with index on path.
Example: `{name:"Mobiles", path:",electronics,mobiles,"}`
Use-case (1 YOE): I built nested shop categories with path for breadcrumb + subtree.
Mistake/Tip: Deep recursive refs need multiple queries; path is one query.
119. **What is polymorphism in schemas?**
What: One collection holds different shapes with `type` discriminator.
Why: Notifications for order/message/promo share base but differ in payload.
How: `{type:"order", orderId}` vs `{type:"promo", code}` with validation per type.
Example: `db.notifs.insertOne({userId:id, type:"order", orderId:oid})`
Use-case (1 YOE): I unified notifications in one collection with type index.
Mistake/Tip: Over-generic docs complicate validation; use `discriminator` in Mongoose.
120. **How to version schemas?**
What: Add `schemaVersion` field and migrate lazily on read for zero-downtime evolution.
Why: Rolling deploys can't stop-the-world rewrite of millions of docs.
How: On read, if `v:1` transform to `v:2` and save back async.
Example: `{name:"Asha", schemaVersion:2}`
Use-case (1 YOE): I migrated `phone:string` → `phones[]` lazily in my app.
Mistake/Tip: Big-bang migration locks DB; lazy + background job is safer.
121. **What is Mongoose?**
What: Node ODM providing schemas, validation, middleware, and populate over native driver.
Why: Adds structure + DX to flexible Mongo for MERN teams.
How: Define schema → model → `create/find/populate`; handles casting and validation.
Example: `const User = mongoose.model("User", new mongoose.Schema({email:String}))`
Use-case (1 YOE): I used Mongoose for all CRUD + validation in Express APIs.
Mistake/Tip: ODM overhead vs driver speed; use `.lean()` when you don't need docs.
122. **How to define a Mongoose schema?**
What: `new mongoose.Schema(fields, {timestamps:true})` declares types/validators/indexes.
Why: Enforces shape at app layer while Mongo stays flexible.
How: `{name:{type:String,required:true,trim:true}, age:{type:Number,min:0}}`.
Example: `new mongoose.Schema({name:{type:String, required:true}, age:Number}, {timestamps:true})`
Use-case (1 YOE): I defined User schema with required email + timestamps.
Mistake/Tip: Forgetting `timestamps:true` loses audit fields; add by default.
123. **How to create a Mongoose model?**
What: `mongoose.model("User", schema)` maps to `users` collection for CRUD.
Why: Single entry point for queries, hooks, statics, and validation.
How: Export model and use `User.create()`, `User.find()`.
Example: `const User = mongoose.model("User", userSchema)`
Use-case (1 YOE): I created Product/Order/User models per collection.
Mistake/Tip: Overwriting model in hot-reload throws OverwriteModelError; guard it.
124. **How to connect Mongoose to MongoDB?**
What: Single `mongoose.connect(MONGO_URI)` at startup with pooling and error handling.
Why: Reuses connection pool; per-request connects exhaust sockets.
How: `await mongoose.connect(process.env.MONGO_URI, {maxPoolSize:10})` then start server.
Example: `await mongoose.connect(process.env.MONGO_URI)`
Use-case (1 YOE): I connected once in `server.js` before `app.listen`.
Mistake/Tip: Starting server before DB ready hides errors; await connect first.
125. **What is validation in Mongoose?**
What: Declarative rules (`required`, `minlength`, `enum`, `match`) enforced before save.
Why: Rejects bad data early with friendly 400s instead of dirty DB.
How: Schema options + custom `validate`; runs on `save/create` (need `runValidators` on update).
Example: `{email:{type:String, required:true, match:/.+@.+/}, role:{enum:["user","admin"]}}`
Use-case (1 YOE): I validated signup email/role enum before insert.
Mistake/Tip: Validators don't run on `updateOne` by default — pass `runValidators:true`.
126. **How to add custom validator?**
What: `validate:{validator:fn, message}` for business rules like positive price.
Why: Beyond built-ins — stock>0, strong password, future date.
How: Sync or async function returning boolean; attach to field.
Example: `{price:{type:Number, validate:{validator:v=>v>0, message:"Price must be positive"}}}`
Use-case (1 YOE): I rejected past-date bookings with custom validator.
Mistake/Tip: Async validators need promises; keep them fast or writes slow.
127. **What is `required:true`?**
What: Ensures field present (non-null) on save; combine with `trim:true` for strings.
Why: Guarantees core fields like email/name exist.
How: `{name:{type:String, required:[true,"Name required"]}}`.
Example: `{email:{type:String, required:true, trim:true}}`
Use-case (1 YOE): I required email+password on signup schema.
Mistake/Tip: `required` doesn't trim whitespace — `" "` passes without `trim:true`.
128. **What is `unique:true` in Mongoose?**
What: Creates DB unique index (not validator) — duplicates fail with E11000.
Why: Race-safe dedup for email/username.
How: Add `unique:true` then catch `err.code===11000` → 409.
Example: `{email:{type:String, unique:true}} // handle E11000`
Use-case (1 YOE): I set unique email and mapped E11000 to friendly message.
Mistake/Tip: Thinking it's validator — it isn't; needs index build + error handling.
129. **What are timestamps in Mongoose?**
What: `{timestamps:true}` auto-adds `createdAt`/`updatedAt` managed on save/update.
Why: Sorting, auditing, TTL expiry without manual dates.
How: Enabled in schema options; customize names if needed.
Example: `new Schema({name:String}, {timestamps:true})`
Use-case (1 YOE): I sorted feeds by `createdAt:-1` using auto timestamps.
Mistake/Tip: `updateOne` without timestamps config may not touch `updatedAt`; verify.
130. **What is middleware/pre-save hook?**
What: `schema.pre("save")` runs logic before save — hashing, slugs, defaults.
Why: Centralize cross-cutting logic vs repeating in controllers.
How: `schema.pre("save", async function(){ if(this.isModified("password")) this.password=await hash(...) })`.
Example: `schema.pre("save", async function(){ this.slug = slugify(this.title) })`
Use-case (1 YOE): I hashed passwords pre-save in auth service.
Mistake/Tip: Arrow function breaks `this`; use `function()` — classic bug.
131. **How to hash password with Mongoose?**
What: Hash in `pre("save")` only if `isModified("password")` with bcrypt.
Why: Avoids rehashing already-hashed password on profile edits.
How: `if(!this.isModified("password")) return next(); this.password=await bcrypt.hash(this.password,10)`.
Example: `if(this.isModified("password")) this.password = await bcrypt.hash(this.password, 10)`
Use-case (1 YOE): I secured signup with bcrypt 10 rounds pre-save.
Mistake/Tip: Rehashing on every save locks users out; guard with `isModified`.
132. **What is population?**
What: Auto-joins refs — replaces ObjectId with doc from another collection.
Why: `Post.find().populate("author","name email")` avoids manual second query.
How: Needs `ref` in schema; uses extra query under hood (not join).
Example: `Post.find().populate("author", "name email")`
Use-case (1 YOE): I populated order customer details for admin list.
Mistake/Tip: Over-populating large lists is N+1-ish; prefer `$lookup` for bulk.
133. **How to define ref in schema?**
What: `author:{type:Schema.Types.ObjectId, ref:"User"}` links collections for populate.
Why: Typed join key enabling populate + casting.
How: Store ObjectId, set `ref` to model name.
Example: `author:{type:Schema.Types.ObjectId, ref:"User", required:true}`
Use-case (1 YOE): I linked posts→users and comments→posts with refs.
Mistake/Tip: String vs ObjectId mismatch breaks populate silently.
134. **What is lean() in Mongoose?**
What: Returns plain JS objects not Mongoose docs — faster, less memory.
Why: Read-only lists don't need save/validate/hooks overhead (2-5x faster).
How: `User.find().lean()`; add `lean({virtuals:true})` if you need virtuals.
Example: `User.find().lean() // plain objects`
Use-case (1 YOE): I sped product listing 3x with `.lean()` in high-traffic API.
Mistake/Tip: Lean docs lack `.save()`/virtuals by default — don't call save on them.
135. **How to paginate with Mongoose?**
What: `find(filter).sort().skip().limit()` + `countDocuments(filter)` for page+total.
Why: Standard admin tables and infinite scroll backends.
How: `skip((page-1)*limit).limit(limit).lean()`; validate page/limit numbers.
Example: `Model.find(f).sort({createdAt:-1}).skip((page-1)*limit).limit(limit).lean()`
Use-case (1 YOE): I built `/products?page=&limit=` with this pattern.
Mistake/Tip: No cap on limit allows DoS (`limit=100000`); clamp to 100.
136. **What is `select()` in Mongoose?**
What: Limits fields — `select("name email")` include, `select("-password")` exclude.
Why: Hide secrets and trim payloads.
How: Chain after find; schema can also set `select:false` for password.
Example: `User.find().select("name email -_id") // or .select("-password")`
Use-case (1 YOE): I excluded `passwordHash` from all user responses.
Mistake/Tip: Forgetting to exclude password leaks hashes — set `select:false` in schema.
137. **How to handle E11000 duplicate error?**
What: Catch `err.code===11000` (duplicate key) and return 409 with friendly message.
Why: Unique email/username races surface as DB error, not validator error.
How: In catch, check code, read `keyValue` to name field.
Example: `if(err.code===11000) return res.status(409).json({msg:"Email already registered"})`
Use-case (1 YOE): I mapped signup duplicates to 409 in auth controller.
Mistake/Tip: Returning 500 for duplicates confuses UX; always map to 409.
138. **What are virtuals?**
What: Computed props not stored — `fullName` from first+last.
Why: Derive without storage/duplication.
How: `schema.virtual("fullName").get(function(){return this.first+" "+this.last})`, enable in JSON.
Example: `schema.virtual("fullName").get(function(){return this.first+" "+this.last})`
Use-case (1 YOE): I exposed `fullName` in profile API without storing it.
Mistake/Tip: Virtuals missing in JSON unless `toJSON:{virtuals:true}` + `lean({virtuals:true})`.
139. **What are instance methods?**
What: Doc-level helpers like `user.comparePassword(pw)` for login check.
Why: Encapsulate domain logic with document context.
How: `schema.methods.comparePassword = async function(pw){return bcrypt.compare(pw,this.password)}`.
Example: `userSchema.methods.comparePassword = function(pw){return bcrypt.compare(pw, this.password)}`
Use-case (1 YOE): I added `user.comparePassword` for login controller.
Mistake/Tip: Arrow functions lose `this`; use `function`.
140. **What are statics?**
What: Model-level helpers like `User.findByEmail(email)` reusable across controllers.
Why: DRY queries with consistent filters (e.g. exclude deleted).
How: `schema.statics.findByEmail = function(email){return this.findOne({email})}`.
Example: `User.findByEmail("a@test.com")`
Use-case (1 YOE): I centralized `Product.search(q)` static for listing.
Mistake/Tip: Confusing statics vs methods — statics on Model, methods on doc.
141. **How to add index in Mongoose?**
What: `schema.index({email:1},{unique:true})` or field `index:true`; auto-created on startup.
Why: Ensure query/sort fields indexed via code not manual shell.
How: Define indexes, check `autoIndex` (disable in prod + use migrations).
Example: `schema.index({email:1}, {unique:true})`
Use-case (1 YOE): I added compound `{category:1,price:1}` via schema for shop.
Mistake/Tip: `autoIndex:true` in prod slows boot; manage via Atlas/migration.
142. **What is `findByIdAndUpdate` gotcha?**
What: Skips validation by default and returns old doc unless `{new:true, runValidators:true}`.
Why: Causes invalid data + confusing API responses.
How: Always pass `{new:true, runValidators:true}`.
Example: `User.findByIdAndUpdate(id, {$set:req.body}, {new:true, runValidators:true})`
Use-case (1 YOE): I fixed profile update returning stale data with `new:true`.
Mistake/Tip: Forgetting `runValidators` lets bad email through — interview staple.
143. **How to do transactions with Mongoose?**
What: `startSession()` + `withTransaction()` passing `session` to every op for atomic multi-doc writes.
Why: Order + stock + payment must all succeed or all rollback.
How: `await session.withTransaction(async()=>{ await Order.create([o],{session}); await Stock.updateOne(...,{session}) })`.
Example: `await session.withTransaction(async()=>{ await Order.create([order], {session}) })`
Use-case (1 YOE): I wrapped order-create + stock-decrement in transaction.
Mistake/Tip: Omitting `session` on one op excludes it from txn — silent inconsistency.
144. **How to soft-delete with Mongoose?**
What: Add `isDeleted`+`deletedAt` and global `pre(/^find/)` filter instead of hard delete.
Why: Recoverable deletes + audit trail for admin.
How: `schema.pre(/^find/, function(){this.where({isDeleted:false})})`; delete = `$set:{isDeleted:true}`.
Example: `schema.pre(/^find/, function(){ this.where({isDeleted:false}) })`
Use-case (1 YOE): I soft-deleted posts with restore option in CMS.
Mistake/Tip: Forgetting to filter deleted in aggregations; add `$match` there too.
145. **What is discriminator in Mongoose?**
What: Schema inheritance in one collection sharing base fields with `type` key.
Why: Admin/Seller share User base but add specific fields.
How: `const Seller = User.discriminator("Seller", new Schema({shop:String}))`.
Example: `User.discriminator("Seller", sellerSchema)`
Use-case (1 YOE): I modeled Vehicle→Car/Bike with shared + specific fields.
Mistake/Tip: Overuse complicates validation; prefer separate collection if shapes diverge a lot.
146. **How to validate ObjectId param?**
What: `mongoose.isValidObjectId(id)` before `findById` to return 400 for malformed ids.
Why: Prevents CastError 500s on `/users/abc`.
How: `if(!mongoose.isValidObjectId(id)) return res.status(400).json({msg:"Invalid id"})`.
Example: `if(!mongoose.isValidObjectId(id)) return res.status(400).send("Bad id")`
Use-case (1 YOE): I validated `:id` params in all detail APIs.
Mistake/Tip: Letting CastError bubble as 500 — map to 400.
147. **How to sanitize MERN query params?**
What: Whitelist `sort/page/limit`, allowlist `select` fields to block injection/leaks.
Why: Raw `req.query` enables NoSQL injection and password exfiltration.
How: Pick known keys, cast numbers, validate sort enum.
Example: `const sort = ["createdAt","price"].includes(q.sort)? q.sort : "createdAt"`
Use-case (1 YOE): I sanitized listing params to prevent `?select=password`.
Mistake/Tip: Passing `req.query` straight to `find()` is critical vulnerability.
148. **How to prevent NoSQL injection?**
What: Never pass raw input to query; validate types and use `$eq` to block `{"$gt":""}` payloads.
Why: `?email[$gt]=` can bypass login if naively passed.
How: Cast to string, use `{email:{$eq:req.body.email}}`, use express-mongo-sanitize.
Example: `User.findOne({email:{$eq:String(req.body.email)}})`
Use-case (1 YOE): I hardened login with `$eq` + sanitize middleware.
Mistake/Tip: `express.json` alone doesn't block `$gt` injection — need explicit guard.
149. **How to seed data with Mongoose?**
What: `insertMany` script with `deleteMany`/`drop` for reproducible dev/test datasets.
Why: Consistent demos and integration tests.
How: `await User.deleteMany(); await User.insertMany(seedUsers)` in `seed.js`.
Example: `await Product.insertMany([{name:"Phone", price:999}])`
Use-case (1 YOE): I seeded 200 products + users for local dev.
Mistake/Tip: Seeding prod without guard wipes data; gate by `NODE_ENV`.
150. **How to disconnect Mongoose in tests?**
What: `await mongoose.disconnect()` (and stop memory server) in `afterAll`.
Why: Prevents Jest open-handle hangs and port leaks.
How: In teardown: `await mongoose.connection.dropDatabase(); await mongoose.disconnect()`.
Example: `afterAll(async()=>{ await mongoose.disconnect() })`
Use-case (1 YOE): I fixed CI timeout by disconnecting after suites.
Mistake/Tip: Forgetting disconnect makes Jest hang — classic 1 YOE pain.
151. **What is a transaction in MongoDB?**
What: Multi-document ACID operation that commits all writes or none.
Why: Keeps order+stock+payment consistent under failures/concurrency.
How: Requires replica set; use session + `withTransaction`, pass session to all ops.
Example: `session.withTransaction(async()=>{ await db.orders.insertOne(o,{session}) })`
Use-case (1 YOE): I used txn for wallet transfer debit+credit.
Mistake/Tip: Single-doc writes already atomic — don't add txn overhead there.
152. **When to use transactions?**
What: For money transfer, order+inventory, booking where partial writes corrupt data.
Why: Two-phase writes without txn leave orphan orders or negative stock.
How: Wrap related writes in `withTransaction` with retry on transient errors.
Example: `// order + {$inc:{stock:-qty}} in one txn`
Use-case (1 YOE): I applied txn to COD order + stock decrement.
Mistake/Tip: Using txn for every write kills throughput; scope narrowly.
153. **How to start transaction in shell?**
What: `startSession()`, `startTransaction()`, then commit/abort explicitly.
Why: Manual testing of txn logic before coding in Node.
How: `s=db.getMongo().startSession(); s.startTransaction(); s.getDatabase("shop").orders.insertOne(...); s.commitTransaction()`.
Example: `s=db.getMongo().startSession(); s.startTransaction()`
Use-case (1 YOE): I rehearsed stock txn in shell before Express implementation.
Mistake/Tip: Forgetting commit leaves txn open until timeout; always abort on error.
154. **How to use transaction in Node?**
What: `withTransaction` with session passed to every `save/update/create`.
Why: Ensures driver retries and correct commit/abort handling.
How: `const s=await mongoose.startSession(); await s.withTransaction(async()=>{...})`.
Example: `await session.withTransaction(async()=>{ await User.updateOne(f,u,{session}) })`
Use-case (1 YOE): I built checkout txn in Node with session threading.
Mistake/Tip: Missing `{session}` on one call silently excludes it — verify each op.
155. **What is ACID?**
What: Atomicity, Consistency, Isolation, Durability — reliable multi-step write guarantees.
Why: Prevents half-written orders visible to other readers after crash.
How: Mongo txns provide snapshot isolation + majority durability.
Example: `// Atomic: debit+credit both commit or both rollback`
Use-case (1 YOE): I cited ACID to justify txn for payments in design review.
Mistake/Tip: Saying Mongo lacks ACID is outdated — multi-doc ACID since 4.0.
156. **Do single-document writes need transactions?**
What: No — single-doc writes are atomic by default, including embedded updates.
Why: Adding txn adds latency/locks with zero benefit for one doc.
How: Use `$set`/`$inc` on one doc directly.
Example: `db.users.updateOne({_id:id}, {$set:{city:"Pune"}, $inc:{v:1}})`
Use-case (1 YOE): I kept view-counter `$inc` txn-free for speed.
Mistake/Tip: Wrapping every write in txn is junior mistake; mention atomic single-doc.
157. **What is writeConcern?**
What: Ack level like `w:1` vs `w:"majority"` controlling durability before success.
Why: Majority prevents rollback on failover for critical payments.
How: `insertOne(doc,{writeConcern:{w:"majority", j:true}})`.
Example: `db.orders.insertOne(o, {writeConcern:{w:"majority"}})`
Use-case (1 YOE): I set majority for orders, `w:1` for analytics logs.
Mistake/Tip: Majority adds latency; choose per-collection criticality.
158. **What is readConcern?**
What: Isolation level like `local/majority/snapshot` controlling what txn sees.
Why: Snapshot gives consistent view across shards/collections during txn.
How: `session.startTransaction({readConcern:{level:"snapshot"}})`.
Example: `startTransaction({readConcern:{level:"snapshot"}, writeConcern:{w:"majority"}})`
Use-case (1 YOE): I used snapshot for inventory report during concurrent sales.
Mistake/Tip: `local` may read uncommitted/rollback data; use majority/snapshot for correctness.
159. **What happens on transaction abort?**
What: All changes roll back, none visible; app should retry or return error.
Why: Guarantees no partial state after payment failure.
How: Catch, `abortTransaction()`, handle idempotency key to avoid double charge.
Example: `try{...await s.commitTransaction()}catch{await s.abortTransaction()}`
Use-case (1 YOE): I aborted order txn on payment gateway failure.
Mistake/Tip: Not making txn idempotent causes double orders on retry.
160. **How to handle transient transaction errors?**
What: Retry on `TransientTransactionError` and `UnknownTransactionCommitResult` with backoff.
Why: Write conflicts/elections temporarily fail but succeed on retry.
How: Loop with exponential backoff, max 3-5 retries.
Example: `if(err.hasErrorLabel("TransientTransactionError")) retry()`
Use-case (1 YOE): I added retry wrapper for checkout txn during failover tests.
Mistake/Tip: Retrying non-transient errors loops forever; check labels.
161. **Can you use transactions on standalone?**
What: No — must run as replica set (even single-node) to enable oplog/txns.
Why: Txns rely on replication machinery for atomic commit.
How: Convert standalone to single-node replica set for dev.
Example: `mongod --replSet rs0 // then rs.initiate()`
Use-case (1 YOE): I hit this error locally and converted to rs0.
Mistake/Tip: Saying txns don't work locally — fix is single-node replica set.
162. **How to enable transactions locally?**
What: Run `mongod --replSet rs0`, `rs.initiate()`, connect with `?replicaSet=rs0`.
Why: Unlocks txn testing in MERN dev without Atlas.
How: Update `MONGO_URI` to include replicaSet param.
Example: `mongodb://localhost:27017/shop?replicaSet=rs0`
Use-case (1 YOE): I enabled local txns for checkout dev in 5 mins.
Mistake/Tip: Forgetting URI param still errors; include `replicaSet=rs0`.
163. **What is max transaction time?**
What: Default 60s `transactionLifetimeLimitSeconds`; keep txns short to avoid conflicts.
Why: Long txns hold snapshots/locks and abort under contention.
How: Do validation outside txn; only DB writes inside.
Example: `// keep txn <5s: validate, then withTransaction(write-only)`
Use-case (1 YOE): I moved image upload out of txn to stay under limit.
Mistake/Tip: Putting API calls inside txn times out; txn should be DB-only.
164. **Are cross-shard transactions supported?**
What: Yes, since 4.2 sharded clusters support multi-doc ACID across shards.
Why: Global orders touching multiple shards stay consistent.
How: Same `withTransaction` via `mongos`; keep shard-key aware.
Example: `// same API via mongos router`
Use-case (1 YOE): I relied on this for multi-tenant SaaS across shards.
Mistake/Tip: Cross-shard txns cost more latency; design shard key to localize.
165. **Example MERN transaction use case?**
What: Create order + decrement stock + charge wallet in one `withTransaction`.
Why: Prevents oversell and money loss on partial failure.
How: All three ops share session; abort on payment error.
Example: `s.withTransaction(async()=>{ await Order.create([o],{session:s}); await Product.updateOne({_id:p},{$inc:{stock:-1}},{session:s}) })`
Use-case (1 YOE): I shipped e-commerce checkout exactly this way.
Mistake/Tip: Forgetting stock check inside txn allows negative stock; check + decrement atomically.
166. **What is a replica set?**
What: Group of mongods with same data: one primary, secondaries + optional arbiter for HA.
Why: Auto-failover and data redundancy without manual restore.
How: Deploy 3 nodes, driver connects with `replicaSet` name.
Example: `rs.status() // PRIMARY, SECONDARY states`
Use-case (1 YOE): I deployed Atlas M10 3-node set for prod HA.
Mistake/Tip: Even number without arbiter ties elections; use odd voters.
167. **What is primary vs secondary?**
What: Primary handles writes; secondaries replicate oplog and can serve reads if allowed.
Why: Scales reads and survives node loss.
How: Writes go primary; reads default primary, `secondaryPreferred` for analytics.
Example: `db.runCommand({hello:1}) // isWritablePrimary:true means primary`
Use-case (1 YOE): I offloaded reports to secondary to protect checkout latency.
Mistake/Tip: Reading stale secondary for checkout shows old stock; use primary there.
168. **What is oplog?**
What: Capped log of writes on primary that secondaries replay to stay in sync.
Why: Foundation of replication + change streams.
How: Size it for 24h window; monitor lag via `rs.printSecondaryReplicationInfo()`.
Example: `db.oplog.rs.find().sort({$natural:-1}).limit(1) // latest op`
Use-case (1 YOE): I sized oplog to survive 12h secondary downtime.
Mistake/Tip: Tiny oplog forces full resync after brief outage.
169. **What is election?**
What: Automatic vote for new primary when old fails, typically 5-10s.
Why: Zero-manual failover for HA.
How: Majority of voters must agree; priority/votes configurable.
Example: `rs.stepDown() // triggers election`
Use-case (1 YOE): I tested failover by stepping down primary in staging.
Mistake/Tip: App must retry once on failover; driver auto-discovers new primary.
170. **What is arbiter?**
What: Vote-only member with no data, breaks ties cost-effectively in even sets.
Why: Cheap majority without extra data copy.
How: Add to 2-data-node set to make 3 voters.
Example: `rs.addArb("arb:27017")`
Use-case (1 YOE): I used arbiter for 2-region cost-saving setup.
Mistake/Tip: Arbiter can't become primary; don't count it for reads/backups.
171. **How many voting members?**
What: Max 7 voting; use odd number (3 or 5) to avoid ties.
Why: Majority consensus needs odd to elect quickly.
How: 3 for most apps, 5 for multi-region.
Example: `rs.conf().members.filter(m=>m.votes>0).length // keep 3`
Use-case (1 YOE): I kept 3 voters across 2 AZs + arbiter.
Mistake/Tip: 4 voters ties easily; add arbiter or go to 5.
172. **How to read from secondary?**
What: `readPreference:"secondaryPreferred"` offloads analytics from primary.
Why: Protects write latency during heavy reports.
How: Set per-query or URI; accept eventual consistency.
Example: `Product.find().read("secondaryPreferred")`
Use-case (1 YOE): I ran nightly reports on secondary.
Mistake/Tip: Stale reads confuse users; never use for cart/stock.
173. **What is replication lag?**
What: Delay between primary write and secondary apply; monitor to avoid stale reads.
Why: High lag serves minutes-old data and risks data loss on failover.
How: Watch `rs.printSecondaryReplicationInfo()`, Atlas metrics.
Example: `rs.printSecondaryReplicationInfo()`
Use-case (1 YOE): I alerted on >10s lag during bulk import.
Mistake/Tip: Ignoring lag + reading secondary causes phantom missing orders.
174. **How to check replica status?**
What: `rs.status()` for health/state/lag; `rs.conf()` for config.
Why: First step when app can't write or lags.
How: Check `health:1`, `stateStr:"PRIMARY/SECONDARY"`, `optimeDate` diff.
Example: `rs.status()`
Use-case (1 YOE): I diagnosed down secondary via `rs.status()` in incident.
Mistake/Tip: Confusing `rs.conf` (desired) vs `rs.status` (actual).
175. **What is failover in MERN?**
What: Driver auto-discovers new primary after election; app retries once on errors.
Why: Brief write errors during election shouldn't crash checkout.
How: Enable `retryWrites=true`, add one retry with backoff.
Example: `mongodb://h1,h2,h3/db?replicaSet=rs0&retryWrites=true`
Use-case (1 YOE): I survived Atlas maintenance with retry-once logic.
Mistake/Tip: No retry = 500s during 10s election; always handle.
176. **What is writeConcern majority?**
What: Waits until majority of voters ack write, preventing rollback on failover.
Why: Critical orders/payments must survive primary loss.
How: `{w:"majority", j:true}` per op or as default.
Example: `db.orders.insertOne(o, {writeConcern:{w:"majority"}})`
Use-case (1 YOE): I set majority for payments, `w:1` for views.
Mistake/Tip: Majority on every log slows app; tier by criticality.
177. **What is Atlas M0/M2/M5?**
What: Free/shared Atlas tiers always on 3-node replica sets with auto-failover.
Why: Free HA for learning/MVP without ops.
How: Create cluster, whitelist IP, connect via SRV URI.
Example: `mongodb+srv://user:pass@cluster0.xxx.mongodb.net/shop`
Use-case (1 YOE): I hosted portfolio MERN on M0 free tier.
Mistake/Tip: Shared tiers throttle + no profiler full; upgrade for prod perf tests.
178. **How to connect to replica set?**
What: URI with all hosts + `replicaSet` + `retryWrites=true`.
Why: Driver discovers primary/failover automatically.
How: `mongodb://host1,host2,host3/mydb?replicaSet=rs0&retryWrites=true`.
Example: `mongoose.connect("mongodb://h1,h2,h3/shop?replicaSet=rs0&retryWrites=true")`
Use-case (1 YOE): I connected Express to Atlas replica set via SRV string.
Mistake/Tip: Single-host URI defeats failover; list all hosts/SRV.
179. **What is sharding?**
What: Horizontal scaling by splitting data across shards via shard key.
Why: Beyond 500GB or single-primary write limits — scale writes + storage.
How: `mongos` router + config servers + shards; choose shard key wisely.
Example: `sh.shardCollection("shop.orders", {userId:1})`
Use-case (1 YOE): I sharded logs by `day` when single node filled.
Mistake/Tip: Sharding too early adds ops pain; replicate first, shard when needed.
180. **What is shard key?**
What: Field(s) determining distribution; choose high-cardinality, even-write key.
Why: Bad key (timestamp) hotspots one shard; good key spreads load.
How: `{userId:1}` or hashed `_id`; include tenant for SaaS.
Example: `sh.shardCollection("shop.orders", {userId:"hashed"})`
Use-case (1 YOE): I sharded events by hashed `deviceId` for even writes.
Mistake/Tip: Monotonic key = hotspot; prefer hashed/high-cardinality.
181. **What is mongos?**
What: Router process directing app queries to correct shard(s), hiding topology.
Why: App connects to one endpoint like single DB.
How: Point Mongoose to `mongos` URI; it scatters/gathers.
Example: `mongoose.connect("mongodb://mongos1:27017,mongos2:27017/shop")`
Use-case (1 YOE): I scaled reads by adding mongos routers behind LB.
Mistake/Tip: Connecting directly to shard bypasses routing — always via mongos.
182. **What is config server?**
What: 3-node replica set storing cluster metadata and chunk ranges.
Why: Tells mongos where each key range lives.
How: Managed by Atlas; on-prem deploy dedicated CSRS.
Example: `// mongos --configdb csrs/host1,host2,host3`
Use-case (1 YOE): I never touched it on Atlas — but knew to keep it healthy.
Mistake/Tip: Losing config servers kills cluster; back them up.
183. **What is chunk?**
What: Logical range of shard-key values balancer migrates to even data.
Why: Unit of movement for balancing — split when large.
How: Auto-split + balancer migrates hot/large chunks.
Example: `sh.status() // shows chunks per shard`
Use-case (1 YOE): I watched `sh.status()` during import to verify spread.
Mistake/Tip: Jumbo chunks (huge docs unsplittable) stall balancer; fix key.
184. **What is balancer?**
What: Background process moving chunks to keep data balanced across shards.
Why: Prevents one shard filling while others idle.
How: Runs in window; disable during peak, enable off-peak.
Example: `sh.getBalancerState() // true/false`
Use-case (1 YOE): I scheduled balancer nights-only during sale.
Mistake/Tip: Disabling forever skews data; re-enable after peak.
185. **What is hashed sharding?**
What: Hashes shard key for uniform distribution; great for writes, poor for ranges.
Why: Randomizes monotonic IDs across shards.
How: `shardCollection(coll, { _id:"hashed" })`.
Example: `sh.shardCollection("shop.events", {_id:"hashed"})`
Use-case (1 YOE): I hashed session IDs for even write spread.
Mistake/Tip: Range queries scatter to all shards; use ranged if ranges common.
186. **What is ranged sharding?**
What: Keeps adjacent key ranges together; good for ranges, risks hotspot on monotonic keys.
Why: `createdAt` range reports hit few shards efficiently.
How: `shardCollection(coll, {createdAt:1})` with zones.
Example: `sh.shardCollection("shop.orders", {createdAt:1})`
Use-case (1 YOE): I ranged-sharded orders by month for fast monthly reports.
Mistake/Tip: Timestamp key hotspots latest shard; combine with hashed prefix.
187. **When to shard vs replicate?**
What: Replicate for availability; shard when >500GB or writes exceed single primary.
Why: Sharding adds complexity — only pay when scale demands.
How: Monitor disk/IOPS; shard after vertical + indexing exhausted.
Example: `// replica: 3 nodes same data; sharded: N shards different data`
Use-case (1 YOE): I stayed on replica set for 50GB shop; planned shard at 400GB.
Mistake/Tip: Premature sharding is senior-level anti-pattern; justify with metrics.
188. **How to choose shard key for MERN SaaS?**
What: `tenantId` or `tenantId+createdAt` compound to isolate tenants and spread writes.
Why: Localizes tenant queries to few shards + avoids noisy-neighbor hotspot.
How: `{tenantId:1, _id:1}` or hashed tenant.
Example: `sh.shardCollection("saas.orders", {tenantId:1, createdAt:1})`
Use-case (1 YOE): I keyed multi-tenant invoices by `orgId`.
Mistake/Tip: Single global auto-inc key hotspots; always include tenant.
189. **Can you change shard key?**
What: Yes, since 4.4 you can refine by adding suffix field to improve distribution.
Why: Fix hotspot without full reshard.
How: `refineCollectionShardKey(db.coll, {oldKey:1, newField:1})`.
Example: `db.adminCommand({refineCollectionShardKey:"shop.orders", key:{userId:1, createdAt:1}})`
Use-case (1 YOE): I refined `tenantId` → `tenantId+orderId` to split jumbo chunks.
Mistake/Tip: Can't fully replace key pre-5.0 easily; choose carefully upfront.
190. **How to fix slow MERN API?**
What: `explain()`, add missing index, `.lean()`, limit fields, cache in Redis.
Why: Covers 90% of slow-list causes in one checklist.
How: Profile → index → project → lean → cache hot reads.
Example: `Product.find(f).select("name price").lean().limit(20)`
Use-case (1 YOE): I cut listing 2s→120ms with index+lean+Redis.
Mistake/Tip: Adding cache before index hides root cause; index first.
191. **How to avoid N+1 in MongoDB?**
What: Single `$lookup`/populate instead of looping `findById` per doc.
Why: 100 orders → 1 query not 101 round-trips.
How: `Order.aggregate([$lookup...])` or `Order.find().populate("userId")`.
Example: `Orders.find().populate("userId", "name") // 2 queries not N+1`
Use-case (1 YOE): I fixed 5s order list by replacing loop with populate.
Mistake/Tip: Populate in loop is red flag; batch it.
192. **Why is `skip` slow on large pages?**
What: Skip scans+discards docs; deep pages read thousands to return 10.
Why: `skip(100000)` still walks 100k index entries.
How: Use cursor `({_id:{$gt:lastId}}).limit(10)` for constant time.
Example: `db.posts.find({_id:{$gt:lastId}}).sort({_id:1}).limit(10)`
Use-case (1 YOE): I switched feed to cursor and page 1000 stayed fast.
Mistake/Tip: Offset UI page numbers tempt skip; offer load-more cursor instead.
193. **How to cache MongoDB results?**
What: Cache hot lists/profiles in Redis with short TTL, invalidate on write.
Why: Drops DB QPS 10x for homepage/top products.
How: `GET cache || DB → SETEX 60s`; del on update.
Example: `` `GET products:page:1` || `Product.find().lean()` → `SETEX 60` ``
Use-case (1 YOE): I cached top products 60s in shop, invalidated on price change.
Mistake/Tip: No invalidation serves stale prices; version keys or pub/sub clear.
194. **How to monitor slow queries?**
What: Profiler `setProfilingLevel(1,{slowms:100})` + Atlas Performance Advisor.
Why: Finds missing indexes with real stats.
How: Check `system.profile`, add suggested indexes.
Example: `db.setProfilingLevel(1, {slowms:100})`
Use-case (1 YOE): I found 2s login via profiler and added email index.
Mistake/Tip: Leaving profiler level 2 logs everything and slows prod; use level 1.
195. **How to handle connection pool exhaustion?**
What: Reuse single Mongoose connection, `maxPoolSize:10-20`, no per-request connects.
Why: Exhaustion queues requests and times out under load.
How: Connect once, monitor `db.serverStatus().connections`, close idle.
Example: `mongoose.connect(uri, {maxPoolSize:15, minPoolSize:2})`
Use-case (1 YOE): I fixed ETIMEDOUT by removing per-request connect in Lambda.
Mistake/Tip: Creating client per API call is top 1 YOE bug; singleton it.
196. **How did you design MERN auth project?**
What: Users with unique email index, bcrypt pre-save, JWT access + TTL refresh collection.
Why: Secure, scalable login with revokable sessions.
How: `unique:true` email, `pre("save")` hash, `otps` TTL, `select("-password")`.
Example: `UserSchema.pre("save", async function(){ if(this.isModified("password")) this.password=await bcrypt.hash(this.password,10) })`
Use-case (1 YOE): I shipped auth with 409 on duplicate + 15m JWT in internship project.
Mistake/Tip: Storing JWT in localStorage vs httpOnly cookie — know XSS/CSRF tradeoff.
197. **How did you build product listing?**
What: Compound `{category:1,price:1}` index, regex search, pagination, Redis cache top pages.
Why: Fast filtered/sorted browsing under load.
How: `find({category, name:{$regex}}).sort().skip().limit().lean()` + `SETEX`.
Example: `Product.find({category:"mobiles"}).sort({price:1}).skip(0).limit(20).lean()`
Use-case (1 YOE): I built Flipkart-like listing with filters in capstone.
Mistake/Tip: Uncapped `limit` DoS; clamp + validate sort keys.
198. **How did you handle order placement?**
What: Mongoose txn: create order, `$inc` stock, rollback on payment failure.
Why: Prevents oversell/orphan orders.
How: `withTransaction` with session on all ops + idempotency key.
Example: `await s.withTransaction(async()=>{ await Order.create([o],{session:s}); await Product.updateOne({_id:p},{$inc:{stock:-qty}},{session:s}) })`
Use-case (1 YOE): I implemented checkout txn for college e-commerce project.
Mistake/Tip: Stock check outside txn races; check and decrement inside txn.
199. **How did you debug duplicate signup bug?**
What: Missing unique index caused race duplicates; added `unique:true`, handled E11000 409 + retry.
Why: App `findOne` check alone fails under double-click.
How: `createIndex({email:1},{unique:true})`, catch 11000, dedupe script for legacy.
Example: `if(err.code===11000) return res.status(409).json({msg:"Email taken"})`
Use-case (1 YOE): I fixed prod double-signup during load test this way.
Mistake/Tip: Just adding `unique` without handling E11000 still 500s; do both.
200. **How did you scale MERN feed?**
What: `{createdAt:-1}` index, cursor pagination, `lean()`, denormalized authorName, secondary reads.
Why: Feed is hottest read — every ms counts.
How: `find({_id:{$lt:lastId}}).sort({createdAt:-1}).limit(20).lean()` + cache.
Example: `Post.find({_id:{$lt:lastId}}).sort({createdAt:-1}).limit(20).lean()`
Use-case (1 YOE): I scaled Instagram-clone feed to 100k posts with this stack.
Mistake/Tip: `skip` + full populate kills feed; cursor + denormalize wins.



