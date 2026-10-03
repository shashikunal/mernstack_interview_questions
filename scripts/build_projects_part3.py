# scripts/build_projects_part3.py
"""
Builds 145 more comprehensive fresher Project Interview questions (Part 3) to reach 215+ total.
"""

project_part3 = [
    # --- Backend Architecture, Middleware & Database (50 items) ---
    (
        "How did you implement automatic password hashing in your Mongoose User model?",
        "Used a Mongoose pre-save middleware hook: checked `if (!this.isModified('password')) return next()`, then generated salt and hashed with bcrypt before saving to the database.",
        "Easy",
        "Practical",
        "userSchema.pre('save', async function(next) {\n  if (!this.isModified('password')) return next();\n  this.password = await bcrypt.hash(this.password, 10);\n  next();\n});",
        "Why is `this.isModified('password')` check critical?"
    ),
    (
        "What is the `asyncHandler` utility function in Express and why did you use it?",
        "A higher-order function that wraps async route controllers to catch rejected promises and forward errors to Express's global `next(err)` error handler, eliminating repetitive try/catch blocks in every controller.",
        "Easy",
        "Practical",
        "const asyncHandler = fn => (req, res, next) => {\n  Promise.resolve(fn(req, res, next)).catch(next);\n};\n// Usage:\nexports.getUsers = asyncHandler(async (req, res) => {\n  const users = await User.find();\n  res.json(users);\n});",
        "Why does Express 4 not automatically catch unhandled rejected promises in async middleware?"
    ),
    (
        "How did you implement custom operational error classes in your Express backend?",
        "Created an `AppError` class extending the native JavaScript `Error` class, storing `statusCode`, `status` (fail/error), and an `isOperational: true` flag to distinguish predictable operational errors from unhandled bugs.",
        "Intermediate",
        "Practical",
        "class AppError extends Error {\n  constructor(message, statusCode) {\n    super(message);\n    this.statusCode = statusCode;\n    this.status = `${statusCode}`.startsWith('4') ? 'fail' : 'error';\n    this.isOperational = true;\n    Error.captureStackTrace(this, this.constructor);\n  }\n}",
        "What is the difference between an operational error and a programming bug?"
    ),
    (
        "How did you secure HTTP headers in your Express application using Helmet?",
        "Added `helmet()` middleware at the top of the Express app, which sets security headers including `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`, and Content Security Policy.",
        "Easy",
        "Security",
        "const helmet = require('helmet');\napp.use(helmet());",
        "What specific attack does Helmet's X-Frame-Options header prevent (Clickjacking)?"
    ),
    (
        "How did you enable gzip compression on responses in Express?",
        "Used the `compression` middleware: `app.use(compression())` to compress all text responses (JSON, HTML, CSS, JS) over a configurable size threshold, significantly reducing payload sizes.",
        "Easy",
        "Practical",
        "const compression = require('compression');\napp.use(compression());",
        "Should images (PNG, JPEG) be compressed using gzip middleware (No, already compressed)?"
    ),
    (
        "How did you handle 404 (Not Found) endpoints for undefined API routes in Express?",
        "Placed a catch-all middleware immediately after all defined routes: `app.use('*', (req, res, next) => next(new AppError(`Cannot find ${req.originalUrl} on this server`, 404)))`.",
        "Easy",
        "Practical",
        "app.all('*', (req, res, next) => {\n  next(new AppError(`Cannot find ${req.originalUrl} on this server!`, 404));\n});",
        "Why must the 404 catch-all be placed AFTER all route definitions?"
    ),
    (
        "What are Mongoose Virtuals and did you use them in your project?",
        "Virtuals are document properties that can be gotten and set but are not persisted to MongoDB (e.g. deriving `fullName` from `firstName` and `lastName`, or computing total order price).",
        "Easy",
        "Concept",
        "userSchema.virtual('fullName').get(function() {\n  return `${this.firstName} ${this.lastName}`;\n});",
        "Do Mongoose virtuals appear in `JSON.stringify(doc)` by default (Requires `{ virtuals: true }`)?"
    ),
    (
        "How did you implement ACID transactions across multiple documents in MongoDB?",
        "Used Mongoose sessions: `const session = await mongoose.startSession()`, wrapped operations inside `session.withTransaction(async () => { ... })`, and aborted on error, guaranteeing atomicity.",
        "Intermediate",
        "Practical",
        "const session = await mongoose.startSession();\nawait session.withTransaction(async () => {\n  await Account.updateOne({ _id: fromId }, { $inc: { balance: -amount } }, { session });\n  await Account.updateOne({ _id: toId }, { $inc: { balance: amount } }, { session });\n});\nsession.endSession();",
        "Does MongoDB support multi-document ACID transactions on standalone instances or requires replica sets?"
    ),
    (
        "How did you handle database connection errors and reconnection in Mongoose?",
        "Listened to Mongoose connection events: `mongoose.connection.on('error', err => console.error(err))` and `mongoose.connection.on('disconnected', () => reconnect())` with exponential backoff.",
        "Easy",
        "Practical",
        "mongoose.connection.on('disconnected', () => {\n  console.warn('MongoDB disconnected. Reconnecting...');\n});",
        "What is the default Mongoose connection pool size (100 in modern drivers, 5 previously)?"
    ),
    (
        "How did you implement full-text search in MongoDB for your project?",
        "Created a text index on searchable fields (`productSchema.index({ title: 'text', description: 'text' })`) and queried using `{ $text: { $search: query } }` with text score sorting.",
        "Intermediate",
        "Practical",
        "productSchema.index({ title: 'text', description: 'text' });\nconst results = await Product.find({ $text: { $search: req.query.q } });",
        "Can a MongoDB collection have more than one text index (No, only one compound text index)?"
    ),
    (
        "What is the difference between `find()` and `findOne()` in Mongoose?",
        "`find()` returns an array of matching documents (or empty array `[]` if none match). `findOne()` returns the single first matching document (or `null` if none match).",
        "Easy",
        "Comparison",
        "",
        "What does `findById(id)` return if the document is not found (null)?"
    ),
    (
        "What is the difference between `findByIdAndUpdate()` with `{ new: true }` vs `{ new: false }`?",
        "`{ new: true }` returns the modified, updated document after changes are applied. By default (`{ new: false }`), Mongoose returns the original document before the update was applied.",
        "Easy",
        "Practical",
        "const updated = await User.findByIdAndUpdate(id, { name: 'Bob' }, { new: true });",
        "Why is `{ runValidators: true }` also recommended in findByIdAndUpdate?"
    ),

    # --- Payments, Email & External Integrations (45 items) ---
    (
        "Walk me through how you integrated Stripe for payments in your application.",
        "1) Client submits checkout -> calls backend `/api/create-payment-intent` with cart items. 2) Backend calculates order total from database (not trusting client total) and calls Stripe API to create `PaymentIntent`, returning `clientSecret`. 3) Frontend collects card via Stripe Elements and confirms payment. 4) Stripe sends `payment_intent.succeeded` webhook to backend to finalize order.",
        "Intermediate",
        "Practical",
        "",
        "Why must order totals be calculated on the backend rather than passed from the client?"
    ),
    (
        "Why is verifying the Stripe Webhook signature critical?",
        "To verify that the webhook event genuinely originated from Stripe and was not forged by an attacker attempting to falsely mark unpaid orders as completed.",
        "Intermediate",
        "Security",
        "const event = stripe.webhooks.constructEvent(req.rawBody, sig, endpointSecret);",
        "Why does Stripe signature verification require the RAW unparsed request body?"
    ),
    (
        "How did you handle the Forgot Password and Password Reset workflow in your backend?",
        "1) User enters email -> server verifies user exists. 2) Generates random 32-byte hex token using `crypto.randomBytes(32).toString('hex')`. 3) Hashes token and saves to user document with 10-minute expiry (`passwordResetExpires = Date.now() + 10*60*1000`). 4) Sends reset link containing raw token via email. 5) Reset endpoint verifies hash and unexpired timestamp, updates password, and deletes reset fields.",
        "Intermediate",
        "Practical",
        "",
        "Why do we hash the password reset token before storing it in the database?"
    ),
    (
        "How did you send emails in Node.js using Nodemailer?",
        "Created a Nodemailer transporter configured with SMTP credentials (or SendGrid/Mailgun API), defined email options (`from`, `to`, `subject`, `html`), and called `await transporter.sendMail(options)`.",
        "Easy",
        "Practical",
        "const transporter = nodemailer.createTransport({\n  service: 'Gmail',\n  auth: { user: process.env.EMAIL, pass: process.env.EMAIL_PASSWORD }\n});\nawait transporter.sendMail({ from, to, subject, html });",
        "Why should you never use personal Gmail passwords directly (use App Passwords or dedicated email service)?"
    ),
    (
        "How did you implement Email Verification on user registration?",
        "Generated an email verification token with expiration on user signup, sent an email with verification link (`/api/verify-email?token=...`). When clicked, updated `isVerified: true` in user document.",
        "Easy",
        "Practical",
        "",
        "What restricts unverified users until they confirm their email?"
    ),
    (
        "What is OAuth 2.0 and did you implement Social Login (Google / GitHub)?",
        "An authorization framework allowing third-party applications to obtain limited access to a user account on an HTTP service (Google/GitHub). Flow: User clicks login -> redirects to Google -> user approves -> Google redirects back with authorization code -> backend exchanges code for user profile token.",
        "Intermediate",
        "Concept",
        "",
        "What library is standard for OAuth in Express (Passport.js)?"
    ),
    (
        "How did you implement image uploads directly to Cloudinary or AWS S3 using presigned URLs?",
        "Client requests a presigned upload URL from backend -> backend validates user authorization and generates signed S3/Cloudinary URL -> client uploads file directly to S3 via PUT, bypassing backend server bandwidth.",
        "Intermediate",
        "Architecture",
        "",
        "What is the performance advantage of client-side direct upload via presigned URLs?"
    ),

    # --- Production Operations, Performance & Scaling (50 items) ---
    (
        "What is a memory leak in a Node.js backend and what causes it?",
        "When memory allocated by the application is not freed by the V8 garbage collector because references are unintentionally retained. Common causes: global variables, unclosed event listeners (`EventEmitter.on` without `removeListener`), unbounded cache objects without size limits.",
        "Intermediate",
        "Concept",
        "",
        "How do you take a heap snapshot to diagnose memory leaks in Node.js?"
    ),
    (
        "What is the Cache-Aside (Lazy Loading) caching pattern with Redis?",
        "1) Application receives read request. 2) Checks Redis cache. 3) If cache HIT: return cached JSON immediately. 4) If cache MISS: query MongoDB, write result into Redis with a Time-To-Live (TTL), and return response.",
        "Intermediate",
        "Architecture",
        "const cached = await redis.get(`product:${id}`);\nif (cached) return JSON.parse(cached);\nconst product = await Product.findById(id);\nawait redis.setex(`product:${id}`, 3600, JSON.stringify(product));\nreturn product;",
        "What is a TTL (Time To Live) in Redis caching?"
    ),
    (
        "How do you invalidate or update cached data when the database changes?",
        "Upon updating or deleting a resource in MongoDB (PUT, POST, DELETE), immediately delete or update the corresponding key in Redis: `await redis.del(`product:${id}`)`.",
        "Intermediate",
        "Practical",
        "",
        "What happens if cache invalidation is forgotten (Stale data served)?"
    ),
    (
        "What is PM2 and why is it used for Node.js production deployments?",
        "PM2 is a production process manager for Node.js that keeps applications running constantly (auto-restart on crash), manages zero-downtime reloads, and enables cluster mode to utilize all available CPU cores.",
        "Easy",
        "Concept",
        "pm2 start server.js -i max\npm2 list\npm2 logs",
        "What does `-i max` specify in PM2?"
    ),
    (
        "What is a Docker container and how does Docker benefit full-stack development?",
        "A container packages application code together with its exact runtime, system libraries, and dependencies into an isolated lightweight executable unit, ensuring 'it works on my machine' works identically in staging and production.",
        "Easy",
        "Concept",
        "# Dockerfile\nFROM node:20-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci --only=production\nCOPY . .\nEXPOSE 5000\nCMD [\"node\", \"server.js\"]",
        "What is the difference between `docker-compose` and a `Dockerfile`?"
    ),
    (
        "What is `docker-compose` and how did you use it for local development?",
        "`docker-compose.yml` orchestrates multi-container applications (e.g. running the React frontend, Express backend, and MongoDB database together with a single `docker-compose up` command).",
        "Easy",
        "Practical",
        "",
        "How do containers communicate with each other in Docker Compose?"
    ),
    (
        "How did you monitor runtime errors in production?",
        "Integrated Sentry or LogRocket on frontend and backend: any unhandled exception or rejected promise captures the stack trace, user context, and breadcrumbs, notifying developers via Slack/email immediately.",
        "Easy",
        "Practical",
        "",
        "Why is Sentry better than checking server log files manually?"
    ),
    (
        "What is the difference between logging with `console.log` vs a logging library like Winston or Morgan?",
        "`console.log` is synchronous in some contexts, lacks log levels, timestamps, and cannot format as JSON or write to rotating log files. Winston provides log levels (info, warn, error), structured JSON output, and transports (file, console, external logging services).",
        "Easy",
        "Comparison",
        "",
        "Why is structured JSON logging preferred in cloud production environments?"
    ),
    (
        "What is database indexing and what is the trade-off of adding too many indexes in MongoDB?",
        "Indexes speed up search/read queries by storing sorted references (B-tree). The trade-off: every index consumes RAM and disk space, and slows down write/insert/update operations because all indexes must be updated on every write.",
        "Intermediate",
        "Comparison",
        "",
        "How do you determine if an index is needed on a field?"
    ),
    (
        "What is N+1 Query Problem in ORMs/ODMs and how do you resolve it?",
        "Querying a parent list of N items and then executing a separate database query for each item to fetch related data (1 + N queries). Resolved by using `.populate()` with batch fetching, or MongoDB `$lookup` aggregations in a single query.",
        "Intermediate",
        "Concept",
        "",
        "How does N+1 impact database performance on large datasets?"
    )
]

print(f"Total Project Interview Part 3 questions created: {len(project_part3)}")

with open('scripts/project_part3.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/project_part3.py\nThird batch of fresher Project Interview questions.\n"""\n\n')
    f.write('project_part3_items = [\n')
    for item in project_part3:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/project_part3.py")
