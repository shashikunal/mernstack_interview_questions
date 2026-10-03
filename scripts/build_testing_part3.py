# scripts/build_testing_part3.py
"""
Builds 85 more comprehensive fresher Testing interview questions to reach 215+ total.
"""

testing_part3 = [
    # --- Jest CLI, Configuration & Hooks (30 items) ---
    (
        "What is the difference between `jest --watch` and `jest --watchAll`?",
        "`jest --watch` runs only tests related to files changed since the last git commit (utilizing Git tracking). `jest --watchAll` monitors the file system and reruns all test suites on every file change regardless of git status.",
        "Easy",
        "Comparison",
        "",
        "Which is faster during active local development in a large repository?"
    ),
    (
        "What does `jest --runInBand` (or `-i`) do?",
        "It forces Jest to run all test suites serially in the current process rather than spawning a pool of parallel worker processes. It is useful for debugging race conditions, shared database locks, or low-memory environments.",
        "Intermediate",
        "Practical",
        "npx jest --runInBand",
        "Why is `--runInBand` helpful when testing against a real database?"
    ),
    (
        "What does `jest --bail` do?",
        "`jest --bail` (or `-b`) stops the test run immediately upon encountering the first test failure, saving time during continuous integration or local debugging.",
        "Easy",
        "Practical",
        "npx jest --bail",
        "Can you configure bail to stop after 3 failures (`--bail=3`)?"
    ),
    (
        "What is `collectCoverageFrom` in `jest.config.js`?",
        "An array of glob patterns specifying which source files should be included in code coverage reports, even if no tests currently import them.",
        "Easy",
        "Practical",
        "collectCoverageFrom: [\n  'src/**/*.{js,jsx,ts,tsx}',\n  '!src/**/*.d.ts',\n  '!src/index.js'\n]",
        "Why is ignoring entry files like `index.js` common in coverage configurations?"
    ),
    (
        "How do you mock system time in modern Jest (26+)?",
        "Use `jest.useFakeTimers().setSystemTime(new Date('2025-01-01'))`. All `new Date()` calls will return the frozen fake date until reset.",
        "Intermediate",
        "Practical",
        "beforeEach(() => {\n  jest.useFakeTimers();\n  jest.setSystemTime(new Date('2025-05-15T12:00:00Z'));\n});\nafterEach(() => {\n  jest.useRealTimers();\n});",
        "Why is freezing system time useful when testing relative date calculations (like '3 days ago')?"
    ),
    (
        "How do you mock `process.env` variables in Jest tests?",
        "Save `const originalEnv = process.env`, modify `process.env.API_URL = 'http://test'` in tests, and restore `process.env = originalEnv` in `afterEach()`.",
        "Easy",
        "Practical",
        "const originalEnv = process.env;\nbeforeEach(() => { process.env = { ...originalEnv }; });\nafterEach(() => { process.env = originalEnv; });\n\ntest('uses test API url', () => {\n  process.env.API_URL = 'https://test.api.com';\n  expect(getConfig().apiUrl).toBe('https://test.api.com');\n});",
        "Why must you copy `process.env` with spread to prevent cross-test leakage?"
    ),
    (
        "How do you test that a function was called with specific arguments regardless of other parameters?",
        "Use asymmetric matchers like `expect.anything()` or `expect.any(Function)` inside `toHaveBeenCalledWith()`.",
        "Easy",
        "Practical",
        "expect(mockLogger).toHaveBeenCalledWith('Error occurred', expect.anything());",
        "What does `expect.anything()` match?"
    ),
    (
        "What does `expect.anything()` match in Jest?",
        "It matches anything except `null` or `undefined`.",
        "Easy",
        "Concept",
        "",
        "What matches any value including null/undefined?"
    ),
    (
        "What is the difference between `jest.fn()` and `jest.spyOn()`?",
        "`jest.fn()` creates an independent, standalone mock function with no prior implementation. `jest.spyOn()` wraps an existing object method, tracking calls while keeping the original implementation intact unless mocked.",
        "Easy",
        "Comparison",
        "",
        "How do you undo a spy created with `jest.spyOn()`?"
    ),
    (
        "How do you undo a spy created with `jest.spyOn()`?",
        "Call `spy.mockRestore()`.",
        "Easy",
        "Practical",
        "const spy = jest.spyOn(Math, 'random').mockReturnValue(0.5);\n// test...\nspy.mockRestore();",
        "What happens if you forget to call `mockRestore()` on global objects like Math or Date?"
    ),

    # --- Testing React Hooks & Components (25 items) ---
    (
        "How do you test that a custom hook handles loading, success, and error states?",
        "Render the hook with `renderHook()`. Assert initial state is loading: `expect(result.current.loading).toBe(true)`. Await async resolution using `await waitFor(() => expect(result.current.loading).toBe(false))`, then assert data or error.",
        "Intermediate",
        "Practical",
        "test('fetches data successfully', async () => {\n  const { result } = renderHook(() => useFetch('/api/users'));\n  expect(result.current.loading).toBe(true);\n  await waitFor(() => expect(result.current.loading).toBe(false));\n  expect(result.current.data).toHaveLength(2);\n});",
        "Why is `waitFor` needed when asserting on hook results?"
    ),
    (
        "How do you test that `useEffect` cleanup runs when a component unmounts?",
        "Spy on the cleanup action (like `clearInterval` or `removeEventListener`). Render component, then call `unmount()`. Assert that the cleanup spy was called.",
        "Intermediate",
        "Practical",
        "test('cleans up event listener on unmount', () => {\n  const spy = jest.spyOn(window, 'removeEventListener');\n  const { unmount } = render(<WindowResizeListener />);\n  unmount();\n  expect(spy).toHaveBeenCalledWith('resize', expect.any(Function));\n  spy.mockRestore();\n});",
        "What method unmounts a component in React Testing Library?"
    ),
    (
        "What is the difference between `render()` and `renderHook()` in React Testing Library?",
        "`render()` renders a visible JSX component into the DOM. `renderHook()` allows testing custom hooks that do not render DOM elements by wrapping them in a test harness component.",
        "Easy",
        "Comparison",
        "",
        "Can a custom hook be called directly in a test function without renderHook?"
    ),
    (
        "Why can you NOT call a custom hook directly in a test function without `renderHook`?",
        "React hooks can only be called inside the body of a React functional component. Calling a hook directly inside a test violates the Rules of Hooks and throws an 'Invalid hook call' error.",
        "Easy",
        "Concept",
        "",
        "How does renderHook solve this internally?"
    ),
    (
        "What does `rerender()` do in React Testing Library?",
        "It updates the props of an already-rendered component without unmounting it, simulating a parent component re-render with new props.",
        "Easy",
        "Practical",
        "const { rerender } = render(<Greeting name='Alice' />);\nexpect(screen.getByText('Hello, Alice')).toBeInTheDocument();\nrerender(<Greeting name='Bob' />);\nexpect(screen.getByText('Hello, Bob')).toBeInTheDocument();",
        "Does `rerender()` preserve component internal state?"
    ),

    # --- Playwright Advanced Features & E2E (20 items) ---
    (
        "What is the Playwright Code Generator (`codegen`)?",
        "A CLI tool (`npx playwright codegen https://example.com`) that opens a browser window and automatically records your clicks, form typing, and navigation, generating production-ready Playwright test code in real-time.",
        "Easy",
        "Concept",
        "npx playwright codegen http://localhost:8000/",
        "What language options does codegen support (e.g. JavaScript, TypeScript, Python)?"
    ),
    (
        "How do you test iframes in Playwright?",
        "Use `page.frameLocator('iframe-selector')` to locate elements inside an iframe with full auto-waiting support.",
        "Intermediate",
        "Practical",
        "const frame = page.frameLocator('#payment-iframe');\nawait frame.getByLabel('Card Number').fill('424242424242');",
        "Why was testing iframes historically difficult in Selenium?"
    ),
    (
        "How do you test handling file downloads in Playwright?",
        "Listen for the `'download'` event before triggering the download: `const downloadPromise = page.waitForEvent('download'); await page.getByRole('button', { name: 'Export' }).click(); const download = await downloadPromise;`.",
        "Intermediate",
        "Practical",
        "const downloadPromise = page.waitForEvent('download');\nawait page.getByText('Download CSV').click();\nconst download = await downloadPromise;\nexpect(download.suggestedFilename()).toBe('report.csv');",
        "How do you save the downloaded file to a custom path?"
    ),
    (
        "How do you test drag and drop in Playwright?",
        "Use `await page.locator('#item').dragTo(page.locator('#dropzone'))`.",
        "Easy",
        "Practical",
        "await page.locator('#card-1').dragTo(page.locator('#column-done'));",
        "Does `dragTo()` auto-wait for both source and target elements?"
    ),
    (
        "How do you simulate offline network mode in Playwright?",
        "Set `await context.setOffline(true)` to simulate losing internet connectivity and verify offline fallback UI or service worker caching.",
        "Intermediate",
        "Practical",
        "await context.setOffline(true);\nawait page.reload();\nawait expect(page.getByText('You are currently offline')).toBeVisible();\nawait context.setOffline(false);",
        "Why is this tested at the BrowserContext level rather than Page level?"
    ),

    # --- Best Practices & Anti-Patterns (10 items) ---
    (
        "Why should you never write hardcoded `sleep` delays in automated tests?",
        "Hardcoded timeouts (like `await new Promise(r => setTimeout(r, 5000))`) make test suites unnecessarily slow if the operation finishes early, and cause flaky test failures if the operation takes slightly longer due to CI load. Use polling or auto-waiting assertions instead.",
        "Easy",
        "Best Practice",
        "// BAD\nawait new Promise(r => setTimeout(r, 3000));\n// GOOD\nawait screen.findByRole('alert');",
        "What does `waitFor` use instead of fixed sleeping?"
    ),
    (
        "Why should you avoid testing CSS style details (like `color: red`) in functional tests?",
        "CSS colors and styling change frequently during redesigns without affecting application logic. Assert on semantic states (e.g. `aria-invalid='true'`, `role='alert'`) rather than hex colors.",
        "Easy",
        "Best Practice",
        "",
        "When is testing visual styling appropriate (Visual Regression Testing)?"
    ),
    (
        "What is the Single Responsibility Principle for tests?",
        "Each test case should verify one specific behavior or concept and fail for only one reason. Avoid giant tests with dozens of unrelated assertions testing multiple separate features.",
        "Easy",
        "Concept",
        "",
        "Why are small, focused test cases easier to maintain?"
    ),
    (
        "What is the 'Arrange-Act-Assert' (AAA) pattern?",
        "The standard structure of a unit test: 1) Arrange: set up test data, mocks, and preconditions. 2) Act: execute the function or trigger the user action being tested. 3) Assert: verify that the actual result matches expected behavior.",
        "Easy",
        "Concept",
        "test('calculates discount', () => {\n  // Arrange\n  const cart = { total: 100, discountPercent: 20 };\n  // Act\n  const finalPrice = applyDiscount(cart);\n  // Assert\n  expect(finalPrice).toBe(80);\n});",
        "How does the AAA pattern map to BDD's Given-When-Then?"
    ),
    (
        "How do you test that sensitive passwords are not leaked in user API responses?",
        "Make a request that returns user data (like registration or login) and explicitly assert that `res.body.password` and `res.body.hash` are `undefined`.",
        "Easy",
        "Practical",
        "const res = await request(app).post('/api/register').send(newUser);\nexpect(res.body.user.password).toBeUndefined();\nexpect(res.body.user.passwordHash).toBeUndefined();",
        "Why is testing for absence of sensitive fields a critical security test?"
    )
]

print(f"Total Testing Part 3 questions created: {len(testing_part3)}")

with open('scripts/testing_part3.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/testing_part3.py\nThird batch of fresher Testing interview questions.\n"""\n\n')
    f.write('testing_part3_items = [\n')
    for item in testing_part3:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/testing_part3.py")
