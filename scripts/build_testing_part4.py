# scripts/build_testing_part4.py
"""
Builds 57 more Testing interview questions to reach 215 total.
"""

testing_part4 = [
    (
        "What does `toHaveReturned()` assert in Jest?",
        "It asserts that a mock function successfully returned at least once without throwing an error.",
        "Easy",
        "Practical",
        "const mockFn = jest.fn(() => 42);\nmockFn();\nexpect(mockFn).toHaveReturned();",
        "What matcher verifies the exact returned value?"
    ),
    (
        "What does `toHaveReturnedWith(value)` assert in Jest?",
        "It verifies that a mock function returned a specific value on at least one invocation.",
        "Easy",
        "Practical",
        "expect(mockCalculator).toHaveReturnedWith(100);",
        "What is `toHaveLastReturnedWith`?"
    ),
    (
        "What does `toBeGreaterThan()` and `toBeLessThan()` test in Jest?",
        "They assert numerical comparisons: `expect(age).toBeGreaterThan(18)` and `expect(price).toBeLessThan(100)`.",
        "Easy",
        "Practical",
        "expect(user.age).toBeGreaterThanOrEqual(21);",
        "Can these matchers be used on floats?"
    ),
    (
        "Which HTTP status code should be asserted when testing API rate limiting?",
        "429 Too Many Requests.",
        "Easy",
        "MCQ",
        "",
        {"A": "403 Forbidden", "B": "429 Too Many Requests", "C": "503 Service Unavailable", "D": "500 Internal Error"},
        "B",
        "What header typically accompanies a 429 response?"
    ),
    (
        "What header is commonly returned with a 429 Too Many Requests status to indicate when the client can retry?",
        "`Retry-After` (specifying wait duration in seconds or an HTTP-date timestamp).",
        "Easy",
        "Concept",
        "",
        "How do you test rate limiting using Supertest in a loop?"
    ),
    (
        "How do you test API rate limiting using Supertest in a loop?",
        "Send requests in a loop up to the rate limit threshold, assert they return 200/201, then send one additional request and assert that it returns 429.",
        "Intermediate",
        "Practical",
        "test('enforces rate limit of 5 requests', async () => {\n  for (let i = 0; i < 5; i++) {\n    await request(app).get('/api/limited').expect(200);\n  }\n  await request(app).get('/api/limited').expect(429);\n});",
        "Why is resetting the rate limiter between tests necessary?"
    ),
    (
        "How do you test CORS preflight requests using Supertest?",
        "Send an `OPTIONS` HTTP request with `Origin` and `Access-Control-Request-Method` headers and assert that `Access-Control-Allow-Origin` and `Access-Control-Allow-Methods` are returned in response headers.",
        "Intermediate",
        "Practical",
        "const res = await request(app)\n  .options('/api/data')\n  .set('Origin', 'https://trusted-site.com')\n  .set('Access-Control-Request-Method', 'POST')\n  .expect(204);\nexpect(res.headers['access-control-allow-origin']).toBe('https://trusted-site.com');",
        "What status code is standard for preflight OPTIONS responses (204 No Content or 200 OK)?"
    ),
    (
        "How do you test pagination headers (like `X-Total-Count`) with Supertest?",
        "Send a GET request with query params `?page=1&limit=10` and inspect `res.headers['x-total-count']`.",
        "Easy",
        "Practical",
        "const res = await request(app).get('/api/items?page=1&limit=5').expect(200);\nexpect(res.headers['x-total-count']).toBe('25');\nexpect(res.body).toHaveLength(5);",
        "Why do APIs use headers for metadata like total count rather than polluting the data array?"
    ),
    (
        "How do you test that an expired JWT token returns 401 with an appropriate message?",
        "Sign a test token with an expired timestamp (e.g. `expiresIn: '0s'`), send request with that token, and assert `res.status === 401` and `res.body.message === 'Token expired'`.",
        "Intermediate",
        "Practical",
        "const expiredToken = jwt.sign({ id: 1 }, 'secret', { expiresIn: '-10s' });\nconst res = await request(app)\n  .get('/api/dashboard')\n  .set('Authorization', `Bearer ${expiredToken}`)\n  .expect(401);\nexpect(res.body.error).toMatch(/expired/i);",
        "What library is standard for signing JWTs in tests?"
    ),
    (
        "What is the difference between `page.waitForResponse()` and `page.waitForRequest()` in Playwright?",
        "`page.waitForRequest()` waits until a specific outgoing HTTP request is dispatched by the browser. `page.waitForResponse()` waits until the server response for that request is received.",
        "Intermediate",
        "Comparison",
        "const [response] = await Promise.all([\n  page.waitForResponse(res => res.url().includes('/api/login') && res.status() === 200),\n  page.getByRole('button', { name: 'Login' }).click()\n]);",
        "Why is `Promise.all` used to pair action and response waiting?"
    ),
    (
        "How do you filter locators in Playwright using `.filter({ hasText })`?",
        "Narrow down a list of elements to those containing specific text: `page.getByRole('listitem').filter({ hasText: 'Product A' })`.",
        "Easy",
        "Practical",
        "const row = page.getByRole('row').filter({ hasText: 'Alice' });\nawait row.getByRole('button', { name: 'Delete' }).click();",
        "What other option does `.filter` accept (`has: locator`)?"
    ),
    (
        "What does `locator.or()` do in Playwright?",
        "It creates a locator that matches either of two candidate locators, useful for handling varying UI states (like 'Save' vs 'Submit' button).",
        "Intermediate",
        "Practical",
        "const submitBtn = page.getByRole('button', { name: 'Submit' }).or(page.getByRole('button', { name: 'Save' }));\nawait submitBtn.click();",
        "What does `locator.and()` do?"
    ),
    (
        "What does `page.waitForTimeout()` do in Playwright and why is it discouraged in production tests?",
        "It forces the test to pause for a fixed millisecond duration (`await page.waitForTimeout(3000)`). It is discouraged because it causes flaky tests and wastes execution time; web-first auto-waiting assertions should be used instead.",
        "Easy",
        "Best Practice",
        "",
        "When is waitForTimeout acceptable (quick local debugging only)?"
    ),
    (
        "What is the Playwright UI Mode (`npx playwright test --ui`)?",
        "An interactive graphical interface that lets you browse, filter, run, watch, and step through tests with time-travel DOM inspection, console logs, and network monitoring.",
        "Easy",
        "Concept",
        "npx playwright test --ui",
        "How does UI mode accelerate test authoring?"
    ),
    (
        "What is the difference between shallow rendering and full DOM rendering in component testing?",
        "Shallow rendering renders only the parent component and mocks all child components as empty tags. Full DOM rendering renders the complete component subtree including children, providing much greater confidence in user interactions.",
        "Easy",
        "Comparison",
        "",
        "Why did Enzyme's shallow rendering fall out of favor compared to React Testing Library?"
    ),
    (
        "What is `test.concurrent` in Jest?",
        "It instructs Jest to execute asynchronous tests inside a test file concurrently (in parallel) rather than sequentially, speeding up independent tests.",
        "Intermediate",
        "Practical",
        "test.concurrent('calculates tax async', async () => {\n  expect(await calcTax(100)).toBe(10);\n});",
        "Why can concurrent tests NOT share mutable global variables?"
    ),
    (
        "What is a Fixture in testing?",
        "A fixture is a consistent, predetermined set of test data or objects (e.g. sample mock users, fake JSON responses, database seeds) used repeatedly across test suites.",
        "Easy",
        "Concept",
        "",
        "Where are test fixtures usually stored in a project repository?"
    ),
    (
        "What is Contract Testing and what problem does it solve in microservices?",
        "Contract testing verifies that services adhere to a shared contract or API schema without requiring full end-to-end integration environments, enabling independent deployments.",
        "Advanced",
        "Concept",
        "",
        "Name a popular contract testing tool."
    ),
    (
        "What is Chaos Engineering in testing?",
        "The discipline of experimenting on a software system by intentionally injecting failures (like killing server nodes, introducing network latency) to build confidence in the system's capability to withstand turbulent conditions.",
        "Advanced",
        "Concept",
        "",
        "What famous Netflix tool pioneered chaos engineering (Chaos Monkey)?"
    ),
    (
        "Which matcher verifies that a string matches a regular expression in Jest?",
        "`expect(string).toMatch(/regex/)`.",
        "Easy",
        "MCQ",
        "",
        {"A": "expect(str).matches(regex)", "B": "expect(str).toMatch(regex)", "C": "expect(str).hasPattern(regex)", "D": "expect(str).toContain(regex)"},
        "B",
        "What does toMatch do if passed a string instead of regex?"
    ),
    (
        "What is the difference between `toBeDefined()` and `not.toBeUndefined()`?",
        "They are functionally equivalent: both assert that a variable is not equal to `undefined`.",
        "Easy",
        "Comparison",
        "",
        "Can a defined variable still have the value null?"
    ),
    (
        "What does `expect.hasAssertions()` ensure in a test?",
        "It verifies that at least one assertion was called during the test, preventing asynchronous tests from passing silently if promises or callbacks never execute.",
        "Easy",
        "Concept",
        "test('async work', () => {\n  expect.hasAssertions();\n  return doWork().then(data => expect(data).toBe('ok'));\n});",
        "How is it different from `expect.assertions(number)`?"
    ),
    (
        "What is the purpose of `faker.js` (@faker-js/faker) in automated testing?",
        "A library that generates realistic mock test data on-demand (e.g. fake user names, realistic emails, street addresses, phone numbers, avatars, UUIDs).",
        "Easy",
        "Concept",
        "const randomEmail = faker.internet.email();",
        "Why is realistic mock data better than hardcoded 'test1', 'test2'?"
    ),
    (
        "What does `npm test` do by default in a standard Create React App or modern Vite project?",
        "It triggers the configured test runner (Jest or Vitest) in interactive watch mode.",
        "Easy",
        "Practical",
        "npm test",
        "What environment variable sets CI mode in Jest (`CI=true`)?"
    ),
    (
        "What does setting `CI=true` do when running Jest in terminal or CI pipelines?",
        "It runs all tests once without interactive prompts or watch mode, generates coverage reports if configured, and exits with a non-zero code upon any failure.",
        "Easy",
        "Practical",
        "CI=true npm test",
        "Why would interactive watch mode hang in a GitHub Actions runner without CI=true?"
    ),
    (
        "What is Vitest and how does it compare to Jest?",
        "Vitest is a blazing-fast next-generation test runner built natively on Vite that shares Vite's transform pipeline and configuration, offering near-instantaneous HMR and complete Jest-compatible API.",
        "Intermediate",
        "Comparison",
        "",
        "Can Vitest run tests written with Jest syntax (`describe`, `it`, `expect`)?"
    ),
    (
        "What is Storybook interaction testing?",
        "Testing component interactions inside Storybook using Playwright/Testing Library primitives in a `play()` function, validating UI components visually and behaviorally in isolation.",
        "Intermediate",
        "Concept",
        "",
        "How does Storybook testing compare to RTL?"
    ),
    (
        "What is an Assert in software testing?",
        "An assert is a boolean expression that states an expected condition must hold true at a given point in execution; if false, test execution halts with a descriptive failure.",
        "Easy",
        "Concept",
        "",
        "What happens to subsequent assertions in a test case if the first assertion fails?"
    ),
    (
        "What is Property-Based Testing (e.g. fast-check)?",
        "A testing methodology where you define universal properties that must hold true for all valid inputs, and the framework automatically generates hundreds of randomized edge-case inputs to try and disprove the property.",
        "Advanced",
        "Concept",
        "",
        "Give an example of an invariant property for an array sorting function (e.g. result has same length and is non-decreasing)."
    ),
    (
        "How do you test that an API returns correct CORS headers for unauthorized origins?",
        "Send an OPTIONS/GET request with an untrusted origin and assert that `Access-Control-Allow-Origin` is either omitted or does not match the untrusted origin.",
        "Intermediate",
        "Practical",
        "const res = await request(app)\n  .get('/api/data')\n  .set('Origin', 'https://malicious-site.com');\nexpect(res.headers['access-control-allow-origin']).toBeUndefined();",
        "What is the security risk of setting `Access-Control-Allow-Origin: *` with credentials enabled?"
    ),
    (
        "What is the difference between integration testing and system testing?",
        "Integration testing verifies interactions between pairs or groups of interconnected modules. System testing evaluates the complete, integrated system as a whole to ensure compliance with end-to-end specifications.",
        "Easy",
        "Comparison",
        "",
        "Is system testing usually black-box?"
    ),
    (
        "What is the role of `supertest.agent()`?",
        "`request.agent(app)` persists cookies and session state across multiple consecutive requests, allowing testing multi-step flows like logging in followed by accessing protected routes.",
        "Intermediate",
        "Practical",
        "const agent = request.agent(app);\nawait agent.post('/api/login').send(creds);\nconst res = await agent.get('/api/dashboard');\nexpect(res.status).toBe(200);",
        "Why is `agent()` cleaner than manually extracting and passing Set-Cookie headers?"
    ),
    (
        "What is Test Smells?",
        "Sub-optimal patterns or anti-patterns in test code (like assertion roulette, duplicate test code, mystery guest, fragile tests) that indicate poor maintainability or design flaws.",
        "Intermediate",
        "Concept",
        "",
        "What is 'Assertion Roulette' (multiple assertions without messages in a single test)?"
    ),
    (
        "What is 'Assertion Roulette' in test code?",
        "A test smell where multiple assertions exist in one test case without explanation, making it difficult to understand which assertion failed from error reports alone.",
        "Easy",
        "Concept",
        "",
        "How do you fix Assertion Roulette?"
    ),
    (
        "How do you test a component with react-router-dom in RTL?",
        "Wrap the component in `<MemoryRouter initialEntries={['/users/42']}>` to simulate being at a specific URL route and test route parameter extraction.",
        "Intermediate",
        "Practical",
        "import { MemoryRouter, Route, Routes } from 'react-router-dom';\nrender(\n  <MemoryRouter initialEntries={['/users/42']}>\n    <Routes>\n      <Route path='/users/:id' element={<UserProfile />} />\n    </Routes>\n  </MemoryRouter>\n);\nexpect(screen.getByText('User #42')).toBeInTheDocument();",
        "Why is `MemoryRouter` preferred over `BrowserRouter` in tests?"
    ),
    (
        "Why is `MemoryRouter` preferred over `BrowserRouter` in automated tests?",
        "`BrowserRouter` depends on browser history API and window URL, which can leak state across test runs. `MemoryRouter` stores history entirely in an internal array in memory, ensuring complete test isolation.",
        "Easy",
        "Concept",
        "",
        "What prop sets the initial active URL in MemoryRouter?"
    ),
    (
        "What does `jest.mocked()` utility do in TypeScript?",
        "It casts a mocked function or module to its Jest mocked type, providing full TypeScript intellisense and type-safety for mock methods (like `.mockResolvedValue`).",
        "Intermediate",
        "Practical",
        "import axios from 'axios';\njest.mock('axios');\nconst mockedAxios = jest.mocked(axios);\nmockedAxios.get.mockResolvedValue({ data: {} });",
        "What was previously required before `jest.mocked()` was added?"
    ),
    (
        "What is a SpyOn method leak in tests?",
        "When `jest.spyOn()` modifies an object method and the test finishes without calling `spy.mockRestore()`, the mock remains active in subsequent tests, causing unexpected behavior.",
        "Intermediate",
        "Debugging",
        "",
        "What configuration setting in Jest automatically restores mocks between tests (`restoreMocks: true`)?"
    ),
    (
        "How do you automatically restore all mocked spies between tests in `jest.config.js`?",
        "Set `restoreMocks: true` in your `jest.config.js` file.",
        "Easy",
        "Practical",
        "// jest.config.js\nmodule.exports = {\n  restoreMocks: true\n};",
        "How does `restoreMocks` differ from `clearMocks`?"
    ),
    (
        "What does `clearMocks: true` do in `jest.config.js`?",
        "It automatically clears mock call history (`mock.calls`, `mock.instances`) before every test, equivalent to calling `jest.clearAllMocks()` in `beforeEach()`.",
        "Easy",
        "Practical",
        "module.exports = {\n  clearMocks: true\n};",
        "Does `clearMocks` reset mock implementations?"
    ),
    (
        "What does `resetMocks: true` do in `jest.config.js`?",
        "It resets all mock state and resets mock implementations to return `undefined` before each test, equivalent to calling `jest.resetAllMocks()`.",
        "Easy",
        "Practical",
        "module.exports = {\n  resetMocks: true\n};",
        "Why is `clearMocks` more commonly used than `resetMocks`?"
    ),
    (
        "What does `test.failing()` do in Jest?",
        "It marks a test that is currently expected to fail (e.g. tracking a known unaddressed bug). If the test fails, Jest passes; if the test unexpectedly passes, Jest fails.",
        "Intermediate",
        "Practical",
        "test.failing('known bug #104 in tax calculation', () => {\n  expect(calcTax(0)).toBe(0);\n});",
        "When should `test.failing()` be removed?"
    ),
    (
        "What is Cross-Browser Testing and why is it important?",
        "Testing that a web application functions and displays consistently across different browser rendering engines (Chromium, Gecko/Firefox, WebKit/Safari) and operating systems.",
        "Easy",
        "Concept",
        "",
        "How does Playwright make cross-browser testing easy?"
    ),
    (
        "What is the difference between WebKit and Chromium?",
        "Chromium is the open-source engine powering Chrome, Edge, and Brave. WebKit is the rendering engine powering Apple Safari. Different engines may have slight variations in CSS support and JavaScript engine behaviors.",
        "Easy",
        "Comparison",
        "",
        "Can Playwright run WebKit on Linux and Windows?"
    ),
    (
        "Can Playwright run tests against Safari's WebKit engine on Windows or Linux?",
        "Yes! Playwright bundles builds of WebKit for Linux and Windows, allowing developers to test Safari rendering behaviors without owning a Mac.",
        "Easy",
        "Concept",
        "",
        "Why is testing on WebKit critical for mobile web compatibility?"
    ),
    (
        "What is Continuous Integration (CI) and how do automated tests fit in?",
        "CI is the software engineering practice where developers regularly merge code changes into a central repository, after which automated builds and test suites run automatically to detect integration errors immediately.",
        "Easy",
        "Concept",
        "",
        "What happens to a Pull Request if CI tests fail?"
    ),
    (
        "What is a Test Harness?",
        "A collection of software, test data, and configuration designed to run a program unit under controlled test conditions and capture its behavior and outputs.",
        "Easy",
        "Concept",
        "",
        "How does `renderHook()` act as a test harness for React hooks?"
    ),
    (
        "What is the difference between Verification and Validation in software engineering?",
        "Verification: 'Are we building the product right?' (ensuring software conforms to technical specifications and design). Validation: 'Are we building the right product?' (ensuring software meets real user needs and expectations).",
        "Intermediate",
        "Comparison",
        "",
        "Do automated unit tests perform verification or validation?"
    ),
    (
        "What is Exploratory Testing?",
        "A simultaneous process of test design, test execution, and learning where a human tester dynamically explores the application using intuition and domain knowledge without scripted test cases.",
        "Easy",
        "Concept",
        "",
        "Why is automated testing complementary to exploratory testing?"
    ),
    (
        "What is Boundary Value Analysis (BVA)?",
        "A black-box test design technique based on testing boundaries between input partitions (e.g. testing minimum, minimum - 1, minimum + 1, maximum, maximum - 1, maximum + 1), where software bugs occur most frequently.",
        "Easy",
        "Concept",
        "",
        "For an input field accepting ages 18 to 65, what boundary values should be tested?"
    ),
    (
        "For an input field accepting integers from 18 to 65, what boundary values should you test?",
        "17 (just below min), 18 (min), 19 (just above min), 64 (just below max), 65 (max), and 66 (just above max).",
        "Easy",
        "Practical",
        "",
        "What is Equivalence Partitioning?"
    ),
    (
        "What is Equivalence Partitioning (Equivalence Class Partitioning)?",
        "A test technique that divides input data into valid and invalid partitions where all members of a partition are expected to be processed similarly. Testing one value from each partition is assumed to represent the whole class.",
        "Easy",
        "Concept",
        "",
        "How does equivalence partitioning reduce total number of tests required?"
    ),
    (
        "What is the output of `expect([1, 2]).toBe([1, 2])` in Jest and why?",
        "It FAILS because `toBe()` tests reference identity (`Object.is`), and the two arrays are distinct objects in memory. You must use `toEqual()`.",
        "Easy",
        "Output",
        "expect([1, 2]).toBe([1, 2]); // Fails with error: deep equality mismatch",
        "What matcher makes this test pass?"
    ),
    (
        "What is the output of `expect(NaN).toBe(NaN)` in Jest?",
        "It PASSES because Jest's `toBe` uses `Object.is(NaN, NaN)`, which evaluates to `true` in JavaScript.",
        "Easy",
        "Output",
        "expect(NaN).toBe(NaN); // Passes!",
        "How does `Object.is(NaN, NaN)` differ from `NaN === NaN`?"
    ),
    (
        "What is the output of `expect(+0).toBe(-0)` in Jest?",
        "It FAILS because `Object.is(+0, -0)` evaluates to `false` in JavaScript.",
        "Easy",
        "Output",
        "expect(+0).toBe(-0); // Fails!",
        "Why does JavaScript differentiate between +0 and -0 in Object.is?"
    ),
    (
        "What is the output of `expect({ a: undefined }).toEqual({})` in Jest?",
        "It PASSES in `toEqual()`, but FAILS in `toStrictEqual()`.",
        "Intermediate",
        "Output",
        "expect({ a: undefined }).toEqual({}); // Passes!\nexpect({ a: undefined }).toStrictEqual({}); // Fails!",
        "Why does `toStrictEqual` fail on undefined keys?"
    ),
    (
        "What does `expect.not.stringContaining('admin')` do?",
        "It asserts that the target string does not contain the substring 'admin'.",
        "Easy",
        "Practical",
        "expect(userRole).toEqual(expect.not.stringContaining('admin'));",
        "When is negative asymmetric matching useful?"
    )
]

print(f"Total Testing Part 4 questions created: {len(testing_part4)}")

with open('scripts/testing_part4.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/testing_part4.py\nFourth batch of fresher Testing interview questions.\n"""\n\n')
    f.write('testing_part4_items = [\n')
    for item in testing_part4:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/testing_part4.py")
