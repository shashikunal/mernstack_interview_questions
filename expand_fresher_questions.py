# -*- coding: utf-8 -*-
import json, os

DATA_FILE = r"C:\Users\Qsp\Documents\mernstack_interview_questions\mern-200\fresher-data.js"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()
    # strip prefix
    idx = text.find("[")
    end_idx = text.rfind("]") + 1
    questions = json.loads(text[idx:end_idx])

qid = len(questions) + 1

def add_q(subject, topic, subtopic, question, answer, explanation="", code="", difficulty="Easy", q_type="Concept", round_type="Technical Round", freq="High", ref="", followup=""):
    global qid
    questions.append({
        "id": f"q-{qid}",
        "num": qid,
        "subject": subject,
        "topic": topic,
        "subTopic": subtopic,
        "question": question,
        "answer": answer,
        "shortExplanation": explanation,
        "codeExample": code,
        "difficulty": difficulty,
        "questionType": q_type,
        "interviewRound": round_type,
        "frequency": freq,
        "references": ref,
        "followUpQuestions": followup,
        "addedAt": qid
    })
    qid += 1

# Additional jQuery questions
add_q("jQuery", "AJAX", "$.ajax and $.get",
      "How do you perform an asynchronous HTTP GET request using jQuery?",
      "Use $.ajax({ url, method: 'GET', success, error }) or the shorthand $.get(url, callback). jQuery automatically parses JSON responses.",
      "In modern projects, native fetch() or axios is preferred over jQuery AJAX.",
      "$.get('https://api.example.com/items', function(data) {\n  console.log('Received:', data);\n}).fail(function(err) {\n  console.error('Error:', err);\n});",
      "Easy", "Concept", "Technical Round", "Medium", "jQuery Docs", "What is the difference between $.get and $.post?")

add_q("jQuery", "Traversal", "Finding Elements",
      "How do you traverse elements in jQuery using parent(), children(), find(), and siblings()?",
      "parent() gets the immediate parent. children() gets immediate children. find(selector) searches all descendants. siblings() gets all adjacent sibling elements.",
      "Useful for navigating DOM hierarchies in component widgets.",
      "$('#my-item').parent().find('.badge').addClass('active');",
      "Easy", "Concept", "Technical Round", "Medium", "jQuery Docs", "What does .closest() do in jQuery?")

# Additional React questions
add_q("React", "State Management", "Lifting State Up",
      "What does 'Lifting State Up' mean in React and when is it required?",
      "Lifting state up means moving shared state to the closest common parent component when multiple sibling components need to reflect or modify the same data.",
      "The parent manages state and passes the value down via props and updater callbacks.",
      "function Parent() {\n  const [val, setVal] = useState('');\n  return (\n    <>\n      <InputComponent value={val} onChange={setVal} />\n      <DisplayComponent text={val} />\n    </>\n  );\n}",
      "Easy", "Concept", "Technical Round", "High", "React Docs", "How does lifting state up compare to using Context API?")

add_q("React", "Context API", "createContext & useContext",
      "What is the React Context API and what problem does it solve?",
      "Context API allows sharing global data (like current user, theme, or language) across the component tree without manually passing props down through intermediate levels (avoiding 'prop drilling').",
      "It consists of createContext(), a <Context.Provider value={val}>, and the useContext(Context) hook.",
      "const ThemeContext = React.createContext('dark');\n\nfunction Button() {\n  const theme = React.useContext(ThemeContext);\n  return <button className={theme}>Click Me</button>;\n}",
      "Medium", "Concept", "Technical Round", "High", "React Docs", "Does updating a Context value cause all consumer components to re-render?")

add_q("React", "Routing", "React Router Basics",
      "How do you implement client-side routing in a React app using React Router v6?",
      "Wrap the app in <BrowserRouter>, define routes inside <Routes>, and map paths to components using <Route path=\"/about\" element={<About />} />. Use <Link to=\"/about\"> for navigation without page reload.",
      "useNavigate() programmatically navigates, and useParams() reads URL parameters.",
      "import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';\n\nfunction App() {\n  return (\n    <BrowserRouter>\n      <nav><Link to=\"/\">Home</Link> | <Link to=\"/about\">About</Link></nav>\n      <Routes>\n        <Route path=\"/\" element={<Home />} />\n        <Route path=\"/about\" element={<About />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}",
      "Easy", "Concept", "Technical Round", "High", "React Router Docs", "What is the difference between Link and a regular <a> tag in React Router?")

# Additional Backend & Security
add_q("Express", "Security", "Authentication & JWT Basics",
      "What is a JSON Web Token (JWT) and how is it structured?",
      "A JWT is a compact, URL-safe standard (RFC 7519) for transmitting claims securely between parties. It consists of three parts separated by dots (.): Header (algorithm & type), Payload (user claims), and Signature (secret verification).",
      "The client sends the JWT in the HTTP Authorization header as: Bearer <token>.",
      "// Format: header.payload.signature\n// Verification middleware:\nfunction auth(req, res, next) {\n  const token = req.headers['authorization']?.split(' ')[1];\n  if (!token) return res.status(401).json({ error: 'Unauthorized' });\n  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {\n    if (err) return res.status(403).json({ error: 'Invalid token' });\n    req.user = user;\n    next();\n  });\n}",
      "Medium", "Concept", "Technical Round", "High", "JWT.io", "Why should sensitive information like passwords never be stored inside a JWT payload?")

add_q("Express", "Security", "CORS & Security Basics",
      "What is CORS and how do you configure it in an Express backend?",
      "CORS (Cross-Origin Resource Sharing) is a browser security mechanism that blocks web pages from making AJAX requests to a different domain/port than the one that served the page.",
      "Configure it in Express using the 'cors' middleware package by specifying an allowed origin whitelist.",
      "const cors = require('cors');\napp.use(cors({\n  origin: 'http://localhost:3000',\n  credentials: true\n}));",
      "Easy", "Concept", "Technical Round", "High", "MDN", "What is a CORS preflight OPTIONS request?")

# Additional SQL questions
add_q("SQL", "Database Design", "Normalization (1NF, 2NF, 3NF)",
      "What is Database Normalization and what are 1NF, 2NF, and 3NF?",
      "Normalization is organizing database tables to reduce data redundancy and improve data integrity. 1NF: Atomic values (no repeating groups/arrays in cells). 2NF: In 1NF and no partial dependencies (all non-key columns depend on entire primary key). 3NF: In 2NF and no transitive dependencies (non-key columns depend only on primary key).",
      "Normalized databases prevent insertion, update, and deletion anomalies.",
      "-- 1NF: Each column holds single atomic value\n-- 2NF: No partial key dependencies\n-- 3NF: No non-key column determines another non-key column",
      "Medium", "Concept", "Technical Round", "High", "SQL Standard", "What is Denormalization and why is it used in read-heavy reporting?")

add_q("SQL", "Performance", "Indexes in SQL",
      "What is a database Index in SQL, how does it speed up queries, and what is its drawback?",
      "An index is a B-tree data structure that allows the database engine to find rows quickly without scanning the entire table (avoiding full table scans).",
      "Drawback: Indexes consume disk space and slow down INSERT, UPDATE, and DELETE operations because the index must be updated on every write.",
      "CREATE INDEX idx_user_email ON users(email);\n-- Queries filtering by email now run in O(log n) instead of O(n)!\nSELECT * FROM users WHERE email = 'asha@example.com';",
      "Medium", "Concept", "Technical Round", "High", "SQL Standard", "When should you NOT add an index to a column?")

add_q("SQL", "Queries", "Find Duplicate Records",
      "Write a SQL query to find all duplicate emails in a Users table.",
      "SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;.",
      "GROUP BY groups identical emails together, and HAVING filters only groups where the occurrence count exceeds 1.",
      "SELECT email, COUNT(*) AS count \nFROM users \nGROUP BY email \nHAVING COUNT(*) > 1;",
      "Easy", "SQL Query", "Coding Round", "High", "LeetCode #182", "How would you delete the duplicate rows while keeping one original?")

# Additional MongoDB questions
add_q("MongoDB", "Aggregation", "Basic Aggregation Pipeline",
      "How does the MongoDB Aggregation Pipeline work and what do $match and $group do?",
      "The aggregation pipeline processes documents through stages: documents enter, each stage transforms them, and outputs results. $match filters documents (like WHERE), and $group aggregates documents by an _id key (like GROUP BY).",
      "Common pipeline stages include $match, $group, $sort, $project, and $limit.",
      "db.orders.aggregate([\n  { $match: { status: 'completed' } },\n  { $group: { _id: '$customerId', totalSpent: { $sum: '$amount' } } },\n  { $sort: { totalSpent: -1 } }\n]);",
      "Medium", "Concept", "Technical Round", "High", "MongoDB Docs", "What is the difference between find() and aggregate() in MongoDB?")

# Additional Aptitude questions
add_q("Aptitude", "Quantitative", "Simple vs Compound Interest",
      "What are the formulas for Simple Interest and Compound Interest, and calculate SI on $5000 at 8% per annum for 3 years.",
      "Simple Interest formula: SI = (P * R * T) / 100. Calculation: (5000 * 8 * 3) / 100 = 1200. Total amount = $6200. Compound Interest formula: A = P * (1 + R/100)^T, CI = A - P.",
      "Simple interest is calculated only on the principal amount, while compound interest is calculated on principal plus accumulated interest.",
      "// SI = (5000 * 8 * 3) / 100 = 1200\n// CI accumulates interest every year",
      "Easy", "Aptitude", "Aptitude Round", "High", "RS Aggarwal", "Why is CI always greater than or equal to SI for the same rate and principal?")

add_q("Aptitude", "Quantitative", "Ages Problem",
      "The ratio of the ages of father and son is 5:2. If the sum of their ages is 49 years, what is the father's age?",
      "The father's age is 35 years. Calculation: Let common ratio be x. Father's age = 5x, Son's age = 2x. 5x + 2x = 49 => 7x = 49 => x = 7. Father's age = 5 * 7 = 35 years. Son's age = 2 * 7 = 14 years.",
      "Verify: 35 + 14 = 49. Ratio = 35:14 = 5:2.",
      "// 5x + 2x = 49 => 7x = 49 => x = 7\n// Father = 5 * 7 = 35 years",
      "Easy", "Aptitude", "Aptitude Round", "High", "RS Aggarwal", "What will be their age ratio after 7 years?")

add_q("Aptitude", "Quantitative", "Probability Basics",
      "What is the probability of rolling a sum of 7 when two standard 6-sided dice are thrown?",
      "The probability is 1/6 (or ~16.67%). Total outcomes = 6 * 6 = 36. Favorable outcomes for sum 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes. Probability = 6 / 36 = 1/6.",
      "Probability formula: P(Event) = (Number of favorable outcomes) / (Total possible outcomes).",
      "// Favorable: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6\n// Total: 36\n// P = 6 / 36 = 1/6",
      "Easy", "Aptitude", "Aptitude Round", "High", "RS Aggarwal", "What is the probability of rolling a sum greater than 10?")

# Additional Problem Solving & DSA
add_q("DSA", "Searching", "Linear vs Binary Search",
      "What is the difference between Linear Search and Binary Search, and what is the prerequisite for Binary Search?",
      "Linear Search checks each element sequentially; works on unsorted arrays with O(n) time. Binary Search repeatedly divides a sorted search interval in half; requires a SORTED array and runs in O(log n) time.",
      "Binary Search checks the middle element: if target is smaller, search left; if greater, search right.",
      "function binarySearch(arr, target) {\n  let left = 0, right = arr.length - 1;\n  while (left <= right) {\n    let mid = Math.floor((left + right) / 2);\n    if (arr[mid] === target) return mid;\n    if (arr[mid] < target) left = mid + 1;\n    else right = mid - 1;\n  }\n  return -1; // Not found\n}",
      "Easy", "Coding", "Coding Round", "High", "DSA Guide", "What is the worst-case number of comparisons for binary search on 1024 elements?")

add_q("DSA", "Sorting", "Bubble Sort vs Merge Sort",
      "Compare Bubble Sort and Merge Sort in terms of mechanism and time complexity.",
      "Bubble Sort repeatedly steps through the list, swaps adjacent elements if in wrong order; average & worst case O(n^2), O(1) space. Merge Sort uses divide-and-conquer to split array into halves, recursively sorts them, and merges them back; guaranteed O(n log n) time in all cases, O(n) space.",
      "Merge Sort is stable and preferred for large datasets.",
      "// Bubble sort: O(n^2) - nested loops\n// Merge sort: O(n log n) - divide and conquer",
      "Easy", "Concept", "Technical Round", "High", "DSA Guide", "Why is QuickSort often faster in practice than MergeSort despite O(n^2) worst case?")

add_q("DSA", "Recursion", "Factorial & Base Case",
      "What is recursion and write a function to calculate factorial of n?",
      "Recursion is a technique where a function calls itself to solve a smaller instance of the same problem. Every recursive function must have a Base Case to terminate recursion and prevent stack overflow.",
      "Base case for factorial is n <= 1 return 1.",
      "function factorial(n) {\n  if (n <= 1) return 1; // Base case\n  return n * factorial(n - 1); // Recursive call\n}\nconsole.log(factorial(5)); // 120",
      "Easy", "Coding", "Coding Round", "High", "DSA Guide", "What happens if a recursive function has no base case?")

add_q("DSA", "Data Structures", "Linked List Basics",
      "What is a Singly Linked List and how does it differ from an Array?",
      "A Linked List is a linear collection of data elements called Nodes, where each node points to the next node via a pointer/reference. Unlike arrays, linked list elements are not stored in contiguous memory locations.",
      "Array: O(1) random index access, O(n) insertion/deletion at beginning. Linked List: O(n) traversal access, O(1) insertion/deletion at beginning once pointer is known.",
      "class Node {\n  constructor(val) {\n    this.value = val;\n    this.next = null;\n  }\n}",
      "Easy", "Concept", "Technical Round", "High", "DSA Guide", "What is a Doubly Linked List?")

# Additional Coding Questions
add_q("Coding", "Strings", "First Non-Repeating Character",
      "Write a function to find the first non-repeating character in a string.",
      "Build a character frequency map in the first pass. In the second pass, return the first character with frequency === 1. Return null if none exists. Runs in O(n) time.",
      "Using an object or Map keeps lookup constant O(1).",
      "function firstNonRepeating(str) {\n  const freq = {};\n  for (let char of str) {\n    freq[char] = (freq[char] || 0) + 1;\n  }\n  for (let char of str) {\n    if (freq[char] === 1) return char;\n  }\n  return null;\n}\nconsole.log(firstNonRepeating('swiss')); // 'w'",
      "Easy", "Coding", "Coding Round", "High", "JS Interview", "What is the space complexity of this approach?")

add_q("Coding", "Arrays", "Find Missing Number",
      "Find the missing number in an array containing numbers 1 to n with one missing number.",
      "Calculate expected sum of numbers 1 to n using formula: total = (n * (n + 1)) / 2. Subtract actual sum of array elements. The difference is the missing number. Runs in O(n) time and O(1) space.",
      "Avoids sorting (which would be O(n log n)).",
      "function findMissing(arr, n) {\n  const expectedSum = (n * (n + 1)) / 2;\n  const actualSum = arr.reduce((acc, curr) => acc + curr, 0);\n  return expectedSum - actualSum;\n}\nconsole.log(findMissing([1, 2, 4, 5, 6], 6)); // 3",
      "Easy", "Coding", "Coding Round", "High", "LeetCode #268", "Can you solve this using the XOR bitwise operator?")

add_q("Coding", "Arrays", "Flatten Nested Array",
      "Write a function to flatten a deeply nested array without using Array.prototype.flat().",
      "Use recursion with reduce or a loop: for each item, if it is an array, recursively flatten it; else push to result.",
      "Array.isArray(item) checks if an element is an array.",
      "function flatten(arr) {\n  return arr.reduce((acc, item) => {\n    return acc.concat(Array.isArray(item) ? flatten(item) : item);\n  }, []);\n}\nconsole.log(flatten([1, [2, [3, [4]], 5]])); // [1, 2, 3, 4, 5]",
      "Medium", "Fresher Coding", "Coding Round", "High", "JS Interview", "How does arr.flat(Infinity) work in modern ES2019?")

# Additional Engineering Basics
add_q("Engineering", "Performance", "Web Performance Basics",
      "What are three effective ways to optimize web page loading speed for freshers?",
      "1) Compress and optimize images (use modern formats like WebP). 2) Minify CSS and JavaScript bundles to reduce payload size. 3) Use script 'defer' or 'async' so JavaScript downloads don't block DOM parsing. 4) Leverage browser caching with HTTP Cache-Control headers.",
      "Measuring with Google Lighthouse helps identify slow bottlenecks.",
      "<!-- Defer non-critical scripts -->\n<script src=\"bundle.js\" defer></script>\n<!-- Use responsive picture element -->\n<img src=\"hero.webp\" loading=\"lazy\" alt=\"Hero\">",
      "Easy", "Concept", "Technical Round", "Medium", "Web.dev", "What does the loading=\"lazy\" attribute on <img> tags do?")

add_q("Engineering", "Testing", "Unit vs Integration vs E2E",
      "Explain the testing pyramid: Unit Tests, Integration Tests, and End-to-End (E2E) Tests.",
      "Unit Tests: Test individual functions or components in isolation (fast, numerous, cheap). Integration Tests: Test how multiple units/modules work together (e.g. API endpoint + database). E2E Tests: Test complete user journeys through real browser automation like Playwright (slow, fewer, realistic).",
      "A healthy codebase has many unit tests, fewer integration tests, and key smoke E2E tests.",
      "// Unit test (Jest): test('sum adds numbers', () => expect(sum(1,2)).toBe(3));\n// E2E test (Playwright): await page.click('#submit-btn');",
      "Easy", "Concept", "Technical Round", "Medium", "Testing Guide", "Why shouldn't you only write E2E tests?")

# Additional Project Questions
add_q("Projects", "Architecture", "Project Flow Explanation",
      "Explain how a user request flows through your full-stack project from browser to database and back.",
      "1) User enters data in React form and clicks Submit. 2) React triggers an asynchronous fetch/axios request to Express backend with Bearer JWT header. 3) Express routes request through auth middleware. 4) Controller validates req.body. 5) Mongoose model queries/inserts into MongoDB. 6) MongoDB returns result; controller sends JSON with appropriate HTTP status code (200/201). 7) React updates state and re-renders UI.",
      "Clearly articulating the end-to-end request lifecycle demonstrates strong fullstack comprehension to the interviewer.",
      "// Browser (React) -> HTTP Request (JSON/JWT) -> Express Server -> Middleware -> Controller -> Database (MongoDB/SQL) -> Response (JSON) -> Browser State Update",
      "Easy", "Project", "Project Discussion", "High", "System Flow", "Where should input validation occur: frontend or backend?")

add_q("Projects", "Refactoring", "What Would You Improve",
      "If you had two more weeks to work on your college project, what would you improve or add?",
      "State realistic, practical improvements: 1) Add automated end-to-end tests using Playwright or Jest. 2) Implement Redis caching for frequently viewed product catalogs to reduce database load. 3) Improve accessibility (keyboard navigation and ARIA attributes). 4) Add dark mode and mobile responsiveness optimizations.",
      "Shows proactive engineering mindset and self-awareness of technical debt.",
      "// Good suggestions:\n// 1. Unit & Integration test coverage\n// 2. Redis caching layer\n// 3. Accessibility & Lighthouse audit",
      "Easy", "Project", "Project Discussion", "High", "Project Review", "Did you write any automated tests for your project?")

# Additional HR Questions
add_q("HR", "Career", "Where Do You See Yourself in 3 Years",
      "Where do you see yourself in 2 to 3 years as a software developer?",
      "State a growth-oriented, realistic goal: 'In 2 to 3 years, I see myself as a dependable core software engineer who has mastered full-stack development best practices, writes clean maintainable code, contributes significantly to production features, and assists onboarding new junior developers.'",
      "Shows commitment to software engineering craft and steady team contribution without unrealistic titles.",
      "\"In 2-3 years, I aim to be a skilled and reliable full-stack developer in this company, taking ownership of critical features, writing clean tested code, and continuously learning new technologies.\"",
      "Easy", "HR", "HR Round", "High", "HR Guide", "Are you interested in frontend, backend, or fullstack?")

add_q("HR", "Adaptability", "Learning New Technologies",
      "Are you comfortable working with technologies not on your resume (e.g. Angular, Java, or C#)?",
      "Answer positively: 'Yes, absolutely. As a fresher, I believe core computer science fundamentals—data structures, problem solving, clean code principles, and web protocols—are transferable across languages and frameworks. I learned React and Node.js quickly through hands-on projects, and I am excited to learn whatever tech stack the company needs.'",
      "Employers look for adaptability and eagerness to learn over rigid preferences in freshers.",
      "// Key talking points:\n// 1. Strong fundamentals are language-agnostic\n// 2. Proven ability to learn quickly via projects\n// 3. Enthusiastic about company's tech stack",
      "Easy", "HR", "HR Round", "High", "HR Guide", "Can you share an example of a technology you learned quickly on your own?")

# Save updated dataset
js_content = "window.FRESHER_QUESTIONS_DATA = " + json.dumps(questions, indent=2) + ";"
with open(DATA_FILE, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Updated fresher-data.js to {len(questions)} comprehensive questions!")
