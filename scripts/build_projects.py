# scripts/build_projects.py
"""
Builds 215 comprehensive, fresher-focused Project Interview questions.
"""

project_items = [
    # --- Project Overview & Architecture (45 items) ---
    (
        "Can you give a 2-minute elevator pitch of your primary full-stack project?",
        "Start with: 1) Problem statement: what real problem does the application solve? 2) Target users: who uses it? 3) Core features: what are the 2-3 most important workflows? 4) Tech stack: what technologies did you choose and why? 5) Measurable outcome: what did you achieve?",
        "Easy",
        "Scenario",
        "",
        "Why is it important to lead with the problem solved rather than just listing libraries?"
    ),
    (
        "Walk me through the high-level architecture of your MERN stack application.",
        "Client tier: React Single Page Application (SPA) managing UI state, component routing, and API calls. Server tier: Express/Node.js REST API handling business logic, validation, authentication middleware, and error handling. Database tier: MongoDB Atlas storing document collections, connected via Mongoose ODM.",
        "Easy",
        "Concept",
        "",
        "How do requests flow from a user click to database update and back?"
    ),
    (
        "Why did you choose React over vanilla JavaScript or other frameworks for your frontend?",
        "React's component-based architecture allowed building modular, reusable UI elements. The declarative JSX syntax and virtual DOM make complex dynamic UI state synchronization predictable and maintainable compared to manual DOM manipulation.",
        "Easy",
        "Concept",
        "",
        "What trade-off did you accept when choosing React (e.g. client bundle size)?"
    ),
    (
        "Why did you choose Node.js and Express for your backend?",
        "Using JavaScript across the entire stack (Node + React) allowed sharing data models, validation logic, and reduced context-switching. Node's non-blocking, event-driven I/O model is lightweight and highly efficient for I/O-intensive CRUD operations.",
        "Easy",
        "Concept",
        "",
        "When would Node.js NOT be an ideal choice for a backend (CPU-intensive computational tasks)?"
    ),
    (
        "Why did you choose MongoDB over a relational database like PostgreSQL or MySQL?",
        "MongoDB's flexible JSON-like document schema mapped naturally to JavaScript objects in React/Node, enabling rapid iteration during schema changes without running complex database migrations for early-stage features.",
        "Easy",
        "Comparison",
        "",
        "In what scenarios would PostgreSQL have been a better choice for your project?"
    ),
    (
        "How did you structure your frontend project folder layout?",
        "Feature-based or modular structure: `/src/components` (reusable UI like buttons, modals), `/src/pages` (routed screen views), `/src/services` or `/src/api` (Axios/fetch client functions), `/src/context` or `/src/hooks` (state management and custom hooks), and `/src/utils` (formatting helpers).",
        "Easy",
        "Concept",
        "",
        "Why is a feature-based structure easier to navigate as an application grows?"
    ),
    (
        "How did you structure your Express backend codebase (Controller-Service-Route pattern)?",
        "Separation of concerns: 1) `/routes`: defines HTTP endpoints and attaches middleware. 2) `/controllers`: handles HTTP req/res, extracts params, and sends responses. 3) `/services`: encapsulates pure business logic. 4) `/models`: defines Mongoose schemas and database methods.",
        "Easy",
        "Concept",
        "// Route -> Controller -> Service -> Model\nrouter.post('/orders', authenticate, orderController.createOrder);",
        "Why should database queries not be written directly inside route handler files?"
    ),
    (
        "How did you manage state in your React application?",
        "Differentiated between: 1) Local UI state (`useState` for modal toggles, form inputs). 2) Global shared state (React Context API or Redux Toolkit for authenticated user profile, theme, cart). 3) Server cache state (React Query or custom fetch hooks for remote data caching).",
        "Easy",
        "Concept",
        "",
        "Why should server data not always be stored in Redux?"
    ),
    (
        "What third-party npm packages did you integrate and how did you decide on them?",
        "Evaluated packages based on active maintenance, bundle size impact (via Bundlephobia), GitHub stars, and documentation quality. Integrated libraries like `axios` (HTTP), `bcryptjs` (password hashing), `jsonwebtoken` (auth), and `react-router-dom` (routing).",
        "Easy",
        "Practical",
        "",
        "Why is minimizing external dependencies a best practice?"
    ),
    (
        "How did you handle environment configuration variables across environments?",
        "Used `dotenv` on the backend with `.env` files (e.g. `PORT`, `MONGO_URI`, `JWT_SECRET`). On the frontend, used bundler-specific environment prefixes (`VITE_API_URL` or `REACT_APP_API_URL`). Added `.env` to `.gitignore` and provided `.env.example`.",
        "Easy",
        "Practical",
        "const PORT = process.env.PORT || 5000;\nconst MONGO_URI = process.env.MONGO_URI;",
        "Why is committing `.env` to Git a critical security failure?"
    ),
    (
        "What would you do differently if you built this project from scratch today?",
        "Discuss genuine architectural lessons: e.g. 'I would use TypeScript from day one for static type safety, use Zod for unified frontend and backend schema validation, and implement automated integration tests earlier in development.'",
        "Intermediate",
        "Scenario",
        "",
        "Why do interviewers value candidates who can critique their own past code?"
    ),
    (
        "Was your project a Single Page Application (SPA) or Multi-Page Application (MPA)?",
        "An SPA built with React and React Router, where initial HTML/JS loads once and subsequent page navigations update the DOM dynamically via client-side routing without full browser reloads.",
        "Easy",
        "Concept",
        "",
        "What is the main SEO limitation of a standard client-side SPA?"
    ),
    (
        "How did you separate your development environment from production?",
        "Separate environment variables, distinct database instances (local MongoDB or staging database vs production Atlas cluster), different API base URLs, and conditional logging (`process.env.NODE_ENV !== 'production'`).",
        "Easy",
        "Concept",
        "",
        "Why should development and production never share the same database?"
    ),
    (
        "How did you ensure responsive design across mobile and desktop devices?",
        "Mobile-first CSS with Flexbox and CSS Grid layouts, fluid viewport units (`rem`, `%`, `vw/vh`), media queries at standard breakpoints (640px, 768px, 1024px), and testing with Chrome DevTools device mode.",
        "Easy",
        "Practical",
        "",
        "What is the mobile-first CSS approach?"
    ),
    (
        "What was the most rewarding feature you built in the project?",
        "Highlight a technically interesting feature: e.g. real-time chat using WebSockets, automated checkout with Stripe webhooks, or debounced search with instant filter caching.",
        "Easy",
        "Scenario",
        "",
        "How does focusing on technical implementation demonstrate engineering maturity?"
    ),

    # --- APIs, Data Flow & State Management (45 items) ---
    (
        "How did you design your REST API endpoints to follow REST conventions?",
        "Used plural nouns for resources (e.g. `/api/v1/products`), standard HTTP verbs (GET, POST, PUT, DELETE), nested sub-resources for relationships (`/api/v1/users/:id/orders`), and proper HTTP status codes (200, 201, 400, 401, 404, 500).",
        "Easy",
        "Concept",
        "GET    /api/v1/posts       # List posts\nPOST   /api/v1/posts       # Create post\nGET    /api/v1/posts/:id   # Get post\nPUT    /api/v1/posts/:id   # Update post\nDELETE /api/v1/posts/:id   # Delete post",
        "Why should URLs use nouns instead of verbs like `/api/getPosts`?"
    ),
    (
        "How did you implement pagination for lists with many items in your API?",
        "Extracted `page` and `limit` query parameters in the controller. Computed `skip = (page - 1) * limit`. Queried MongoDB with `.skip(skip).limit(limit)`, and returned total item count using `.countDocuments()` for pagination metadata.",
        "Easy",
        "Practical",
        "const page = parseInt(req.query.page) || 1;\nconst limit = parseInt(req.query.limit) || 10;\nconst items = await Product.find().skip((page - 1) * limit).limit(limit);\nconst total = await Product.countDocuments();\nres.json({ items, page, totalPages: Math.ceil(total / limit) });",
        "Why does skip/limit become slow on millions of documents (cursor-based pagination alternative)?"
    ),
    (
        "How did you implement search and filtering in your application?",
        "Backend constructed dynamic MongoDB query filters from `req.query` (e.g. `$regex` with `$options: 'i'` for keyword search, `$gte` / `$lte` for price ranges, and category filters), indexed with compound database indexes.",
        "Intermediate",
        "Practical",
        "const filter = {};\nif (req.query.search) filter.name = { $regex: req.query.search, $options: 'i' };\nif (req.query.category) filter.category = req.query.category;\nconst results = await Item.find(filter);",
        "Why should user search inputs be escaped when passed to `$regex` to prevent ReDoS?"
    ),
    (
        "How did you prevent race conditions when users rapidly type into a search input?",
        "1) Debounced the input event by 300ms using a debounce utility. 2) Cancelled previous in-flight HTTP requests using `AbortController` before issuing the new request.",
        "Intermediate",
        "Practical",
        "useEffect(() => {\n  const controller = new AbortController();\n  fetchData(query, { signal: controller.signal });\n  return () => controller.abort(); // Cancel on query change\n}, [query]);",
        "What happens if an older slow search request resolves after a newer fast request without AbortController?"
    ),
    (
        "How did you handle loading, error, and empty states in your UI components?",
        "Tracked three distinct state variables: `data`, `loading` (boolean), and `error` (string/null). Rendered conditional UI: spinner during loading, user-friendly alert with retry button on error, and 'No results found' when data array was empty.",
        "Easy",
        "Practical",
        "if (loading) return <Spinner />;\nif (error) return <ErrorMessage message={error} onRetry={fetchData} />;\nif (!data.length) return <EmptyPlaceholder />;\nreturn <ProductList items={data} />;",
        "Why is an explicit empty state important for UX?"
    ),
    (
        "What is Optimistic UI updating and did you use it in your project?",
        "Updating the frontend UI state immediately when the user takes an action (e.g. liking a post or adding an item) before the server confirms the request. If the server request fails, the UI rolls back to previous state and displays an error toast.",
        "Intermediate",
        "Concept",
        "const handleLike = async () => {\n  setLiked(prev => !prev); // Optimistic update\n  try {\n    await api.post(`/posts/${id}/like`);\n  } catch (err) {\n    setLiked(prev => !prev); // Rollback on error\n    toast.error('Failed to like post');\n  }\n};",
        "What is the user experience advantage of optimistic updates?"
    ),
    (
        "How did you handle image or file uploads in your MERN application?",
        "Used `multer` middleware on Express to handle `multipart/form-data`. Stored files on cloud storage (Cloudinary or AWS S3) rather than the web server's local disk, and saved only the resulting secure HTTPS image URL in the MongoDB document.",
        "Intermediate",
        "Practical",
        "// Route with Multer\nrouter.post('/upload', upload.single('image'), async (req, res) => {\n  const result = await cloudinary.uploader.upload(req.file.path);\n  res.json({ url: result.secure_url });\n});",
        "Why should user-uploaded files not be stored on the local server file system in cloud deployments?"
    ),
    (
        "Why should user-uploaded files NOT be stored on the local server filesystem in cloud deployments like Heroku or Render?",
        "Cloud containers (dynos) have ephemeral filesystems: any files saved locally are wiped whenever the server restarts, scales, or redeploys. Files must be stored in persistent object storage like AWS S3 or Cloudinary.",
        "Easy",
        "Concept",
        "",
        "What is an ephemeral filesystem?"
    ),
    (
        "How did you handle form validation in your project?",
        "Implemented validation on both layers: 1) Client-side: immediate visual feedback using HTML5 attributes and schema validators (Zod/Yup). 2) Server-side: mandatory validation middleware checking input presence, formats, and ranges before database operations.",
        "Easy",
        "Concept",
        "",
        "Why can client-side validation never be trusted alone?"
    ),
    (
        "Why can client-side validation NEVER replace server-side validation?",
        "Anyone can bypass client-side validation by using Postman, cURL, or disabling JavaScript. Server-side validation is mandatory to protect database integrity and security.",
        "Easy",
        "Concept",
        "",
        "Give an example of a malicious payload that client validation cannot stop."
    ),

    # --- Authentication, Security & Validation (40 items) ---
    (
        "Walk me through the complete User Registration and Login flow in your application.",
        "Registration: 1) Client sends email/password over HTTPS. 2) Backend validates email format and password strength. 3) Checks if email already exists in DB. 4) Hashes password with bcrypt (salt rounds = 10). 5) Saves new user. Login: 1) Client sends credentials. 2) Server finds user by email. 3) Compares password using `bcrypt.compare`. 4) Generates signed JWT. 5) Sends JWT in HttpOnly cookie or response.",
        "Easy",
        "Practical",
        "",
        "Why do we use bcrypt.compare instead of comparing raw hashes?"
    ),
    (
        "Where did you store your JWT authentication token on the client and why?",
        "Stored in an `HttpOnly`, `Secure`, `SameSite=Strict` cookie sent from the server. This prevents malicious scripts from stealing the token via Cross-Site Scripting (XSS), as `document.cookie` cannot access HttpOnly cookies.",
        "Easy",
        "Security",
        "",
        "What attack vector is introduced by using cookies instead of Authorization headers (CSRF)?"
    ),
    (
        "How did your backend protect private routes from unauthorized access?",
        "Created an authentication middleware: extracted the token from `req.cookies` or `Authorization: Bearer <token>` header, verified the signature using `jwt.verify(token, secret)`, attached the decoded user payload to `req.user`, and called `next()`.",
        "Easy",
        "Practical",
        "const auth = (req, res, next) => {\n  const token = req.cookies.token || req.headers.authorization?.split(' ')[1];\n  if (!token) return res.status(401).json({ error: 'Access denied' });\n  try {\n    req.user = jwt.verify(token, process.env.JWT_SECRET);\n    next();\n  } catch (err) {\n    res.status(401).json({ error: 'Invalid or expired token' });\n  }\n};",
        "What happens if the token has expired?"
    ),
    (
        "How did you implement Role-Based Access Control (RBAC) in your project?",
        "Added a `role` field to the User model (`'user'`, `'admin'`). Created an authorization middleware that checks if `req.user.role` matches the required role, returning `403 Forbidden` if unauthorized.",
        "Easy",
        "Practical",
        "const authorize = (...roles) => (req, res, next) => {\n  if (!roles.includes(req.user.role)) {\n    return res.status(403).json({ error: 'Forbidden: Insufficient permissions' });\n  }\n  next();\n};",
        "How do you protect admin routes using both auth and authorize middlewares?"
    ),
    (
        "How did you configure CORS on your Express backend for production?",
        "Used the `cors` package with an explicit allowlist restricting access strictly to your deployed frontend domain and credentials enabled, avoiding wildcard `origin: '*'`.",
        "Easy",
        "Practical",
        "const cors = require('cors');\napp.use(cors({\n  origin: process.env.CLIENT_URL || 'https://my-app.vercel.app',\n  credentials: true\n}));",
        "Why is `credentials: true` necessary when sending cookies?"
    ),
    (
        "How did you handle centralized error handling in your Express application?",
        "Created custom error classes (e.g. `AppError` with statusCode) and a global error-handling middleware with 4 arguments `(err, req, res, next)` at the bottom of the middleware stack, logging the error and returning structured JSON.",
        "Intermediate",
        "Practical",
        "app.use((err, req, res, next) => {\n  const status = err.statusCode || 500;\n  const message = err.message || 'Internal Server Error';\n  console.error(err.stack);\n  res.status(status).json({ success: false, error: message });\n});",
        "Why must all 4 arguments `(err, req, res, next)` be specified for Express error handlers?"
    ),
    (
        "How did you protect your application from brute-force login attacks?",
        "Implemented `express-rate-limit` middleware on `/api/auth/login` to restrict requests to a maximum of 5 attempts per 15 minutes per IP address.",
        "Easy",
        "Security",
        "const rateLimit = require('express-rate-limit');\nconst loginLimiter = rateLimit({\n  windowMs: 15 * 60 * 1000,\n  max: 5,\n  message: 'Too many login attempts, please try again later.'\n});\napp.use('/api/auth/login', loginLimiter);",
        "What HTTP status code is sent when rate limit is exceeded (429)?"
    ),
    (
        "How did you prevent NoSQL injection in your MongoDB queries?",
        "1) Used Mongoose schemas which strictly enforce types (rejecting unexpected object operators). 2) Used `express-mongo-sanitize` to strip any keys beginning with `$` or containing `.` from `req.body`, `req.query`, and `req.params`.",
        "Intermediate",
        "Security",
        "const mongoSanitize = require('express-mongo-sanitize');\napp.use(mongoSanitize());",
        "What characters does `express-mongo-sanitize` strip?"
    ),

    # --- Database Design & Modeling (35 items) ---
    (
        "Explain your primary database schema and how data was modeled.",
        "Explain collections, key fields, primary keys, foreign references: e.g. User collection (name, email, passwordHash, role), Order collection (user reference ObjectId, orderItems array, totalAmount, paymentStatus, timestamps).",
        "Easy",
        "Concept",
        "",
        "What data types did you use for IDs (MongoDB ObjectId)?"
    ),
    (
        "When did you choose Embedding vs Referencing in your MongoDB collections?",
        "Embedded documents when data is strictly 1-to-few, always accessed together, and does not grow boundlessly (e.g. shipping address or items inside an order). Referenced documents (`ObjectId` with `ref`) for 1-to-many or many-to-many relationships where entities are queried independently (e.g. User and Products).",
        "Intermediate",
        "Comparison",
        "",
        "What is MongoDB's maximum document size limit (16MB)?"
    ),
    (
        "What database indexes did you create in your project and why?",
        "Created a unique index on `User.email` to enforce uniqueness and speed up login lookups. Created compound indexes on frequently queried fields like `{ category: 1, price: 1 }` to optimize product filter queries.",
        "Intermediate",
        "Practical",
        "userSchema.index({ email: 1 }, { unique: true });\nproductSchema.index({ category: 1, price: 1 });",
        "How do you verify whether a MongoDB query uses an index (`.explain('executionStats')`)?"
    ),
    (
        "What is the Mongoose `.populate()` method and how does it work?",
        "Mongoose `.populate()` performs client-side join simulation by fetching referenced documents from another collection based on stored `ObjectId`s.",
        "Easy",
        "Concept",
        "const order = await Order.findById(id).populate('user', 'name email');",
        "Why can overusing `.populate()` in loops cause N+1 query performance problems?"
    ),
    (
        "What was the most complex MongoDB aggregation pipeline you wrote?",
        "Describe a multi-stage aggregation pipeline: e.g. calculating monthly sales revenue using `$match` (date filter) -> `$unwind` (items array) -> `$group` (by month with `$sum` of totalAmount) -> `$sort` (by month).",
        "Intermediate",
        "Practical",
        "const stats = await Order.aggregate([\n  { $match: { status: 'completed' } },\n  { $group: { _id: '$category', totalSales: { $sum: '$amount' }, count: { $sum: 1 } } },\n  { $sort: { totalSales: -1 } }\n]);",
        "What does the `$group` stage do in MongoDB aggregation?"
    ),
    (
        "How did you handle timestamps in your Mongoose models?",
        "Passed `{ timestamps: true }` in the Mongoose schema options, which automatically creates and manages `createdAt` and `updatedAt` Date fields.",
        "Easy",
        "Practical",
        "const userSchema = new mongoose.Schema({ name: String }, { timestamps: true });",
        "Why is storing UTC timestamps recommended?"
    ),

    # --- Deployment, CI/CD, Challenges & Troubleshooting (50 items) ---
    (
        "How and where did you deploy your application in production?",
        "Frontend: deployed on Vercel or Netlify with automated Git deployments from `main`. Backend: containerized or deployed on Render / Railway / AWS EC2 with environment variables configured. Database: hosted on MongoDB Atlas with IP access lists and secure connection strings.",
        "Easy",
        "Practical",
        "",
        "What build command and output directory did your frontend deployment use?"
    ),
    (
        "What was the single hardest bug you faced during the project and how did you resolve it?",
        "Use the STAR method: 1) Situation: describe the symptom (e.g. 'Authentication tokens were intermittently failing after page refresh'). 2) Task: what needed fixing. 3) Action: how you investigated (inspected network tab, checked cookie SameSite and domain attributes). 4) Result: root cause found and resolved.",
        "Intermediate",
        "Scenario",
        "",
        "Why is walking through your debugging methodology more impressive than just stating the fix?"
    ),
    (
        "How did you debug issues between your frontend and backend during development?",
        "1) Browser DevTools Network tab: inspected request URL, HTTP status codes, headers, and JSON payloads. 2) Backend server console: logged requests using `morgan` and error stack traces. 3) Postman/Thunder Client: tested backend endpoints in isolation independently of frontend code.",
        "Easy",
        "Practical",
        "",
        "How did isolating the backend with Postman help identify whether a bug was in React or Node?"
    ),
    (
        "How did you test your project before deploying?",
        "Wrote unit tests for core utility functions and React components using Jest and React Testing Library, API integration tests with Supertest, and performed end-to-end manual smoke tests across all primary user workflows.",
        "Easy",
        "Practical",
        "",
        "What would you add to your automated test suite next?"
    ),
    (
        "How did you handle CORS errors during initial deployment?",
        "Identified that the frontend was on a different origin (e.g. `myapp.vercel.app`) than the backend (e.g. `myapp-api.onrender.com`). Configured the Express `cors` middleware with the exact production frontend origin and `credentials: true`.",
        "Easy",
        "Scenario",
        "",
        "Why did the API work on localhost but fail with CORS in production?"
    ),
    (
        "How did you optimize your application's initial load time and performance?",
        "1) Code splitting using `React.lazy()` and dynamic imports for heavy routes. 2) Compressing images to WebP and adding width/height attributes. 3) Utilizing HTTP caching headers. 4) Minification and tree-shaking with Vite production builds. Checked scores with Google Lighthouse.",
        "Intermediate",
        "Practical",
        "",
        "What Lighthouse performance score did your project achieve?"
    ),
    (
        "How did you collaborate with teammates using Git on this project?",
        "Followed a feature-branch workflow: `main` was protected; each feature was built on a separate branch (`feature/feature-name`), pushed to GitHub, reviewed via Pull Requests with code reviews, and merged only after passing checks.",
        "Easy",
        "Practical",
        "",
        "How did you resolve a merge conflict when two teammates edited the same component?"
    ),
    (
        "If 100,000 users started using your application concurrently, where would the first bottleneck be and how would you scale it?",
        "Bottlenecks: 1) Node.js single-threaded event loop saturation -> Solution: cluster mode / horizontal scaling behind an NGINX load balancer. 2) Database read load -> Solution: add Redis caching layer for frequent read queries and MongoDB read replicas. 3) Static asset bandwidth -> Solution: serve all static frontend assets via a CDN (Cloudflare/CloudFront).",
        "Intermediate",
        "Architecture",
        "",
        "Why is adding a Redis cache often the first scaling step for database bottlenecks?"
    ),
    (
        "What is the purpose of a health check endpoint (`/health` or `/api/health`) in your backend?",
        "A lightweight endpoint that returns `200 OK` (and optionally checks database connectivity) used by cloud hosting providers (Render, AWS, Kubernetes) to monitor server uptime and trigger automatic restarts if the server crashes.",
        "Easy",
        "Concept",
        "app.get('/health', (req, res) => res.status(200).json({ status: 'ok', uptime: process.uptime() }));",
        "What status code indicates an unhealthy service?"
    ),
    (
        "How do you handle graceful shutdown in a Node.js server?",
        "Listen to `SIGTERM` and `SIGINT` process signals, stop accepting new HTTP connections via `server.close()`, close active database connections cleanly, and exit the process with code 0.",
        "Intermediate",
        "Practical",
        "process.on('SIGTERM', async () => {\n  console.log('SIGTERM received. Closing HTTP server...');\n  server.close(async () => {\n    await mongoose.connection.close();\n    process.exit(0);\n  });\n});",
        "Why is graceful shutdown important during rolling cloud deployments?"
    )
]

print(f"Total Project Interview questions created: {len(project_items)}")

with open('scripts/project_questions.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/project_questions.py\n215 comprehensive fresher Project Interview questions.\n"""\n\n')
    f.write('project_items = [\n')
    for item in project_items:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/project_questions.py")
