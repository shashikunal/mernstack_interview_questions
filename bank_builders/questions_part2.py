"""
Question Bank Part 2 (Expanded):
- 4. Prompt Engineering (40 questions)
- 5. AI + JavaScript (15 questions)
- 6. AI + React (15 questions)
- 7. AI APIs (20 questions)
Total: 90 Questions
"""

from pe_data import pe_40_items

# 5. AI + JAVASCRIPT (15 Questions)
ai_js_15_items = [
    ("How do you call an AI API using vanilla `fetch` and async/await in JavaScript?",
     "Use `fetch` with POST method, include `Authorization: Bearer ${API_KEY}` and `Content-Type: application/json` headers, pass the model and messages in the JSON body, and await `response.json()`.",
     "Standard `fetch` call with headers and JSON body.",
     "const res = await fetch('https://api.openai.com/v1/chat/completions', {\n  method: 'POST',\n  headers: { 'Authorization': `Bearer ${process.env.AI_KEY}`, 'Content-Type': 'application/json' },\n  body: JSON.stringify({ model: 'gpt-4o-mini', messages: [{ role: 'user', content: 'Hello' }] })\n});\nconst data = await res.json();",
     "Basic", "Code", "High", "Why should you use an official SDK instead of raw `fetch` when available?"),

    ("How do you handle errors and HTTP status codes when calling AI APIs in Node.js?",
     "Check `if (!response.ok)` after fetch. Handle specific status codes: 401 (Invalid API Key), 429 (Rate limit exceeded), 503 (Model overloaded). Throw descriptive errors to prevent unhandled promise rejections.",
     "Always verify `response.ok` and handle 429/503 gracefully.",
     "if (!res.ok) {\n  const errData = await res.json();\n  throw new Error(`AI API Error ${res.status}: ${errData.error?.message}`);\n}",
     "Basic", "Code", "High", "What does a 429 status code signify in AI APIs?"),

    ("How do you securely manage AI API keys in a Node.js project using `dotenv`?",
     "Install `dotenv`, store the key in a `.env` file (`AI_API_KEY=sk-...`), add `.env` to `.gitignore`, and load it at server startup using `require('dotenv').config()`. Access it exclusively via `process.env.AI_API_KEY` on the server.",
     "Never hardcode keys or commit `.env` files to Git.",
     "require('dotenv').config();\nconst apiKey = process.env.AI_API_KEY;\nif (!apiKey) throw new Error('AI_API_KEY missing in environment variables');",
     "Basic", "Security", "High", "What happens if an API key is accidentally committed to GitHub?"),

    ("How do you consume a streaming AI response in Node.js using an async iterator?",
     "Initialize the OpenAI SDK with `stream: true`, and loop through chunks using `for await (const chunk of stream)`. Extract token deltas using `chunk.choices[0]?.delta?.content || ''`.",
     "Async iterators enable clean sequential processing of streaming tokens.",
     "const stream = await openai.chat.completions.create({ model: 'gpt-4o-mini', messages, stream: true });\nfor await (const chunk of stream) {\n  process.stdout.write(chunk.choices[0]?.delta?.content || '');\n}",
     "Intermediate", "Code", "High", "How do you forward this stream to an Express HTTP response?"),

    ("How do you measure token count in JavaScript before calling the API?",
     "Use tokenizer libraries like `tiktoken` or `gpt-tokenizer`. Encode the string into token integers and check the array length (`tokenizer.encode(text).length`). This allows pre-call token estimation and budget enforcement.",
     "Pre-flight token counting prevents unexpected context overflows.",
     "import { encode } from 'gpt-tokenizer';\nconst tokenCount = encode(promptText).length;\nconsole.log(`Estimated tokens: ${tokenCount}`);",
     "Intermediate", "Code", "High", "Why is character count divided by 4 only an approximation?"),

    ("How do you implement a request timeout for AI API calls in JavaScript using `AbortController`?",
     "Create an `AbortController`, pass `controller.signal` to `fetch` or the OpenAI SDK options, and set a `setTimeout` to call `controller.abort()` after e.g. 25,000ms. Clear timeout on success.",
     "Prevents hung requests from blocking backend server worker threads.",
     "const controller = new AbortController();\nconst timeout = setTimeout(() => controller.abort(), 25000);\ntry {\n  const res = await fetch(url, { signal: controller.signal, ... });\n} finally { clearTimeout(timeout); }",
     "Intermediate", "Code", "High", "What error is thrown when `abort()` is triggered? (`AbortError`)"),

    ("How do you implement Exponential Backoff with Jitter in JavaScript for retry handling?",
     "When an API call returns 429 or 503, retry up to N times. Calculate delay using `delay = Math.pow(2, attempt) * 1000 + Math.random() * 500`. Await a sleep promise for that duration before retrying.",
     "Exponential backoff with jitter prevents thundering herd problems on overloaded APIs.",
     "async function fetchWithRetry(fn, retries = 3) {\n  for (let i = 0; i < retries; i++) {\n    try { return await fn(); }\n    catch (err) {\n      if (i === retries - 1) throw err;\n      const delay = Math.pow(2, i) * 1000 + Math.random() * 500;\n      await new Promise(r => setTimeout(r, delay));\n    }\n  }\n}",
     "Intermediate", "Code", "High", "Why is random jitter added to exponential backoff delays?"),

    ("How do you implement an in-memory LRU cache in JavaScript for AI responses?",
     "Use a JavaScript `Map` or `lru-cache` package. Hash the input prompt as the key. Before calling the API, check `cache.get(key)`. If present, return cached text immediately with 0 tokens and sub-10ms latency.",
     "Caching repeated queries eliminates redundant token expenditures.",
     "const cache = new Map();\nfunction getAiResponse(prompt) {\n  if (cache.has(prompt)) return cache.get(prompt);\n  const res = await callLLM(prompt);\n  cache.set(prompt, res);\n  return res;\n}",
     "Intermediate", "Architecture", "High", "Why should an in-memory cache have a maximum size or TTL?"),

    ("How do you safely parse and validate an AI-generated JSON string in JavaScript?",
     "Never use `eval()`. Wrap `JSON.parse()` in a try/catch block. If it fails, use regex to strip accidental markdown backticks (`replace(/```json|```/g, '')`). Then validate the parsed object with a Zod schema.",
     "Combine safe parsing with markdown sanitization and Zod validation.",
     "function parseAiJson(rawText, schema) {\n  const cleaned = rawText.replace(/```(?:json)?|```/g, '').trim();\n  return schema.parse(JSON.parse(cleaned));\n}",
     "Intermediate", "Code", "High", "Why is `JSON.parse()` prone to failing on raw LLM outputs?"),

    ("How do you process an array of prompts concurrently in JavaScript without hitting rate limits?",
     "Use a concurrency-limiting helper (like `p-limit` or batch chunks) instead of `Promise.all()` over 1,000 items. Limit concurrent executions to e.g. 5 requests at a time to stay under TPM/RPM limits.",
     "Controlled concurrency prevents triggering HTTP 429 rate limit errors.",
     "import pLimit from 'p-limit';\nconst limit = pLimit(5); // 5 concurrent requests max\nconst results = await Promise.all(prompts.map(p => limit(() => callLLM(p))));",
     "Intermediate", "Code", "High", "What is the difference between RPM (Requests Per Minute) and TPM (Tokens Per Minute)?"),

    ("How do you sanitize user inputs in JavaScript before interpolating them into prompts?",
     "Escape XML special characters (`<`, `>`, `&`) to prevent users from breaking out of delimiter tags like `<user_query>`. Strip null bytes and normalize whitespace to prevent injection attacks.",
     "Sanitizing prevents delimiter breakout and prompt injection.",
     "function escapeXml(str) {\n  return str.replace(/[<>&]/g, c => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;' }[c]));\n}",
     "Intermediate", "Security", "High", "How does XML escaping prevent delimiter spoofing?"),

    ("How do you build a command-line AI assistant tool in Node.js?",
     "Use `readline` or `inquirer` to accept user input in terminal, format messages array, call OpenAI SDK, stream chunks directly to `process.stdout.write()`, and loop for multi-turn chat.",
     "Node.js CLI tools provide interactive terminal-based AI assistants.",
     "const rl = readline.createInterface({ input: process.stdin, output: process.stdout });\nrl.on('line', async (line) => { /* stream to process.stdout */ });",
     "Practical", "Code", "Medium", "How do you handle terminal colors with `chalk` for AI outputs?"),

    ("Practical: How do you read local project files and send them as context in a Node.js script?",
     "Use `fs.promises.readFile(filePath, 'utf8')`. Wrap the content in delimited tags (`<file name=\"app.js\">...content...</file>`). Check file size to ensure it does not exceed the model context window.",
     "File reading + XML encapsulation + Context size validation.",
     "const code = await fs.readFile('./src/App.tsx', 'utf8');\nconst prompt = `Review this component:\\n<file name=\"App.tsx\">\\n${code}\\n</file>`;",
     "Practical", "Code", "High", "What happens if you try to read a binary file (like a PNG) with 'utf8' encoding?"),

    ("Scenario: An AI API call fails intermittently with network socket hang-ups. How do you troubleshoot?",
     "1) Check TCP keep-alive settings in your Node.js HTTP agent. 2) Increase agent timeout settings (`keepAliveTimeout`). 3) Inspect if your cloud provider (AWS/Vercel) has a 10-second serverless function timeout killing long generations. 4) Switch to streaming.",
     "Network socket hang-ups are usually caused by serverless function timeouts during long text generation.",
     "// In Vercel / AWS Lambda: Increase maxDuration to 60s for AI routes",
     "Scenario", "Debugging", "High", "What is the maximum execution duration for serverless functions on free tiers?"),

    ("Scenario: How do you build a local fallback mechanism if the primary cloud AI API fails?",
     "In your Node.js service, catch cloud API failures (500/503/timeout) and automatically fallback to a secondary provider (e.g. Anthropic Claude or a local Ollama instance running on port 11434).",
     "Multi-provider failover guarantees high availability for mission-critical web apps.",
     "try {\n  return await callOpenAI(prompt);\n} catch (err) {\n  console.warn('OpenAI failed, falling back to Anthropic');\n  return await callAnthropic(prompt);\n}",
     "Scenario", "Architecture", "High", "How do you normalize response schemas across different AI providers?")
]

# 6. AI + REACT (15 Questions)
ai_react_15_items = [
    ("How do you architect a real-time AI Chat interface in React?",
     "State: `messages` array of `{ id, role: 'user'|'assistant', text, isStreaming }`, `input` string, `isLoading` boolean. Components: MessageList, MessageItem (with Markdown support), ChatInput, and AutoScroll anchor ref.",
     "Standard state-driven chat architecture in React.",
     "const [messages, setMessages] = useState<Message[]>([]);\nconst [input, setInput] = useState('');\nconst [isLoading, setIsLoading] = useState(false);",
     "Basic", "Architecture", "High", "Why should each message have a unique ID instead of relying on array index?"),

    ("How do you implement typewriter streaming in React using `ReadableStream` and `TextDecoder`?",
     "Call `const reader = response.body.getReader()`. In an async `while (true)` loop, read chunks, decode with `TextDecoder`, and update state incrementally: `setMessages(prev => [...prev.slice(0, -1), { role: 'assistant', text: accumulatedText }])`.",
     "Streams tokens directly into component state for real-time rendering.",
     "while (true) {\n  const { done, value } = await reader.read();\n  if (done) break;\n  accumulated += decoder.decode(value);\n  updateAssistantMessage(accumulated);\n}",
     "Basic", "Code", "High", "How do you avoid unnecessary React re-renders during high-frequency token streams?"),

    ("How do you automatically scroll a chat container to the bottom as new tokens stream in?",
     "Create an empty `div` at the bottom of the message list with a React `useRef`. In a `useEffect` triggered whenever the active streaming message updates, call `bottomRef.current?.scrollIntoView({ behavior: 'smooth' })`.",
     "Automatic scroll anchored to bottom ref on message state updates.",
     "const bottomRef = useRef<HTMLDivElement>(null);\nuseEffect(() => {\n  bottomRef.current?.scrollIntoView({ behavior: 'smooth' });\n}, [messages]);",
     "Basic", "Code", "High", "How do you prevent auto-scrolling if the user has manually scrolled up to read earlier messages?"),

    ("How do you render Markdown and syntax-highlighted code blocks in a React AI chat?",
     "Use `react-markdown` with `remark-gfm` and a syntax highlighter component (like `prismjs` or `@tailwindcss/typography`). Custom code renderers add a copy-to-clipboard button and language badge to codeblocks.",
     "Renders AI markdown into clean HTML with syntax-highlighted code blocks.",
     "<ReactMarkdown components={{\n  code({ node, inline, className, children, ...props }) {\n    return <CodeBlock language={match[1]}>{String(children)}</CodeBlock>;\n  }\n}}>{message.text}</ReactMarkdown>",
     "Intermediate", "Code", "High", "Why is it important to sanitize HTML when rendering markdown from an LLM?"),

    ("How do you implement a Stop Generation button in React using `AbortController`?",
     "Store an `AbortController` instance in a React `useRef`. Pass `controller.signal` to the `fetch` call. When user clicks 'Stop', call `abortControllerRef.current?.abort()`. Reset loading state and keep whatever text was generated so far.",
     "Allows users to immediately halt unwanted long generations.",
     "const abortRef = useRef<AbortController | null>(null);\nconst handleStop = () => abortRef.current?.abort();",
     "Intermediate", "Code", "High", "What HTTP signal is sent across the wire when an AbortController aborts?"),

    ("How do you handle loading states, skeletons, and disabled buttons in React AI apps?",
     "When `isLoading` is true: Disable submit button and input box. Render a pulsing skeleton or typing indicator (3 bouncing dots) at the bottom of the chat list. Change submit button to a 'Stop' button.",
     "Clear visual feedback reassures users during model latency.",
     "{isLoading && <div class='typing-indicator'><span></span><span></span><span></span></div>}",
     "Basic", "UI/UX", "High", "What is the UX benefit of an immediate optimistic update before the API responds?"),

    ("What is an Optimistic UI Update in chat applications?",
     "Immediately appending the user's message to the `messages` array and clearing the text input before the backend API call resolves. This makes the interface feel instantaneous and responsive.",
     "Optimistic updates eliminate UI lag when users press Enter.",
     "setMessages(prev => [...prev, { role: 'user', text: input }]);\nsetInput('');\nawait callChatApi(input);",
     "Intermediate", "UI/UX", "High", "What must you do if the API call subsequently fails? (Rollback or show error banner)"),

    ("How do you implement a Copy-to-Clipboard button on AI-generated code blocks?",
     "Use the browser `navigator.clipboard.writeText(codeText)` API. Maintain a transient `isCopied` state that displays 'Copied!' for 2 seconds before reverting to 'Copy'.",
     "Essential developer UX for AI coding assistants.",
     "const handleCopy = async () => {\n  await navigator.clipboard.writeText(code);\n  setCopied(true);\n  setTimeout(() => setCopied(false), 2000);\n};",
     "Basic", "Code", "High", "How do you handle clipboard copy in insecure HTTP environments? (Fallback to execCommand)"),

    ("How do you persist chat history across page refreshes in React?",
     "Store the `messages` array in `localStorage` or `sessionStorage` inside a `useEffect` on change: `localStorage.setItem('chat_history', JSON.stringify(messages))`. On component mount, initialize state from storage.",
     "Saves user conversational state across browser reloads.",
     "const [messages, setMessages] = useState(() => {\n  return JSON.parse(localStorage.getItem('chat_history') || '[]');\n});",
     "Basic", "Code", "High", "What is the storage limit of browser `localStorage`? (~5MB)"),

    ("How do you implement quick-start Prompt Suggestion Chips in a React AI interface?",
     "Render an array of sample prompt strings as clickable badges when the conversation is empty. When clicked, set the input state and automatically trigger submission.",
     "Onboarding chips guide users on what capabilities the assistant possesses.",
     "const SUGGESTIONS = ['Explain React useEffect', 'Debug this async error', 'Write a Jest test'];\n// Clicking chip calls handleSend(promptText)",
     "Basic", "UI/UX", "Medium", "Why do suggestion chips improve user conversion rates in AI apps?"),

    ("How do you integrate Voice Input using the Web Speech API in React?",
     "Use `window.SpeechRecognition || window.webkitSpeechRecognition`. Initialize recognition, listen for `onresult` events, concatenate speech transcript to your text input state, and display a pulsing microphone icon while listening.",
     "Enables hands-free voice prompting directly in the browser without third-party libraries.",
     "const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();\nrecognition.onresult = (e) => setInput(e.results[0][0].transcript);",
     "Intermediate", "Code", "Medium", "What browser compatibility issues exist with the Web Speech API?"),

    ("How do you optimize React rendering performance during high-frequency token streaming?",
     "Avoid updating large component trees on every token chunk. Use a dedicated `StreamingMessage` component, throttle UI updates using `requestAnimationFrame`, or store streaming text in a ref and update DOM text directly to avoid full React re-renders.",
     "Throttling state updates prevents UI frame drops during fast token generation.",
     "// Throttling stream updates to 60fps via requestAnimationFrame",
     "Practical", "Performance", "High", "Why does updating React state 80 times per second cause mobile device stutter?"),

    ("Practical: Build a reusable `useAiChat` custom hook in React.",
     "Encapsulate messages array, input state, loading/error states, `sendMessage`, `stopGeneration`, and `clearChat` into a clean custom hook that components can consume with one line.",
     "Custom hook separates AI networking logic from presentational UI.",
     "export function useAiChat(endpoint = '/api/chat') {\n  const [messages, setMessages] = useState([]);\n  // handles streaming, abort, and error logic\n  return { messages, sendMessage, stop, isLoading };\n}",
     "Practical", "Architecture", "High", "How does this hook compare to Vercel AI SDK's `useChat`?"),

    ("Scenario: A user rapidly clicks 'Send' multiple times before the first request finishes. How do you prevent duplicate calls?",
     "Disable the submit button when `isLoading` is true. Guard the submission handler: `if (isLoading || !input.trim()) return;`. Set `isLoading = true` synchronously at the start of the function.",
     "Button disabling and guard clauses prevent concurrent duplicate submissions.",
     "const handleSend = async () => {\n  if (isLoading || !input.trim()) return;\n  setIsLoading(true);\n  // ...\n};",
     "Scenario", "UI/UX", "High", "How do you handle keyboard Enter press while streaming?"),

    ("Scenario: Markdown codeblocks stream in as unclosed triple-backticks (```). How does your UI prevent broken rendering?",
     "During streaming, check if the string contains an unclosed ```` `. If yes, append a temporary closing ```` ` to the string passed to the markdown renderer so that code syntax highlighting does not break or leak into following text.",
     "Synthesizing closing backticks during streaming ensures clean code block rendering.",
     "const renderableText = hasUnclosedCodeBlock(text) ? text + '\\n```' : text;",
     "Scenario", "UI/UX", "High", "Why do markdown parsers flicker if codeblocks are unclosed?")
]

# 7. AI APIS & INTEGRATION (20 Questions)
ai_api_20_items = [
    ("REST API vs WebSockets vs Server-Sent Events (SSE): Which is best for AI applications?",
     "Server-Sent Events (SSE) is the industry standard for AI text generation: it provides simple, lightweight unidirectional streaming over standard HTTP, automatic reconnects, and works with standard proxies. WebSockets is bidirectional (better for real-time voice). REST without streaming has high perceived latency.",
     "SSE is optimal for LLM text generation; WebSockets for voice; REST for batch jobs.",
     "// SSE: Lightweight, standard HTTP, perfect for LLM token streaming.",
     "Basic", "Architecture", "High", "Why is SSE simpler to deploy than WebSockets behind NGINX?"),

    ("What are the core parameters in an AI Chat Completion request payload?",
     "1) `model` (e.g. 'gpt-4o-mini'), 2) `messages` (array of { role, content }), 3) `temperature` (0.0-2.0), 4) `top_p` (0.0-1.0), 5) `max_tokens` (output limit), 6) `stream` (boolean), 7) `response_format` (JSON mode/schema), 8) `tools` (tool definitions).",
     "Standard API request anatomy across OpenAI, Anthropic, and Gemini.",
     "const payload = { model: 'gpt-4o', messages, temperature: 0.2, max_tokens: 500 };",
     "Basic", "Concept", "High", "What happens if `max_tokens` is omitted?"),

    ("What is the anatomy of an AI Chat Completion response payload?",
     "Returns `{ id, object: 'chat.completion', created, model, choices: [{ index, message: { role, content }, finish_reason }], usage: { prompt_tokens, completion_tokens, total_tokens } }`.",
     "Contains generated message, why it stopped (`finish_reason`), and exact token usage.",
     "// choices[0].message.content has the answer; usage has the billing metrics.",
     "Basic", "Concept", "High", "What are the common values for `finish_reason`? ('stop', 'length', 'tool_calls')"),

    ("What HTTP Status Codes are common when interacting with AI APIs?",
     "200 OK (Success), 400 Bad Request (Invalid parameters/schema), 401 Unauthorized (Invalid API key), 404 Not Found (Invalid model ID), 429 Too Many Requests (Rate limit or quota exceeded), 500 Internal Server Error, 503 Service Unavailable (Model overloaded).",
     "HTTP status codes indicate client mistakes vs vendor capacity issues.",
     "// 401 = Bad key; 429 = Slow down / out of credits; 503 = Vendor capacity issue.",
     "Basic", "Concept", "High", "How should your application react to a 503 Service Unavailable error?"),

    ("What is the difference between RPM (Requests Per Minute) and TPM (Tokens Per Minute) limits?",
     "RPM limits the absolute number of HTTP calls allowed per minute. TPM limits the cumulative volume of tokens (prompt + output tokens) processed per minute. You can hit a TPM limit on a single request if you send a massive 100,000-token prompt!",
     "RPM limits call frequency; TPM limits token volume throughput.",
     "// Tier 1: 500 RPM, 30,000 TPM. A 25,000-token prompt consumes 83% of your TPM quota for that minute!",
     "Intermediate", "Economics", "High", "How do chunked requests prevent TPM limit spikes?"),

    ("What causes HTTP 429 (Rate Limit Exceeded) and what are the two main types?",
     "1) Concurrency / Frequency Limit: Sending requests too fast within a 60-second window (transient; retry with backoff). 2) Account Quota Limit: Running out of prepaid credits or monthly spending limit (permanent until credits are added).",
     "Check error message: 'Rate limit reached' (wait 1s) vs 'You exceeded your current quota' (add credits).",
     "// Inspect error.type: 'insufficient_quota' means billing account is empty.",
     "Intermediate", "Debugging", "High", "How do you distinguish transient 429 from empty account balance?"),

    ("How do AI provider tier levels work (e.g. OpenAI Usage Tiers)?",
     "Providers unlock higher RPM and TPM limits as your account spends and pays for usage. Tier 1 ($5 paid) has low limits; Tier 4 ($250 paid) has high limits (10,000 RPM, 2M TPM). Upgrading tiers requires prepaying credits.",
     "Spending history automatically increases your rate limit ceilings.",
     "// Free Tier -> Tier 1 ($5) -> Tier 2 ($50) -> Tier 3 ($100) -> Tier 4 ($250+)",
     "Intermediate", "Economics", "Medium", "Why do new production apps crash when deployed on Free Tier accounts?"),

    ("What is the OpenAI Batch API and how does it offer a 50% discount?",
     "The Batch API allows submitting asynchronous non-urgent requests in bulk (via JSONL file). The provider executes the jobs during idle GPU capacity and returns results within 24 hours at a 50% discount with separate, higher rate limits.",
     "Batch API cuts costs by 50% for non-realtime jobs like nightly document indexing.",
     "// Ideal for: Nightly embeddings, bulk translations, test dataset evaluation.",
     "Intermediate", "Economics", "High", "Why can't the Batch API be used for interactive user chat?"),

    ("What is the OpenAI Moderation API and why is it free?",
     "The Moderation API (`/v1/moderations`) analyzes text for hate speech, harassment, self-harm, sexual content, and violence. It is 100% free to use to encourage developers to build safe AI applications.",
     "Free safety check to filter abusive inputs before calling expensive generative models.",
     "const mod = await openai.moderations.create({ input: userText });\nif (mod.results[0].flagged) throw new Error('Content policy violation');",
     "Intermediate", "Security", "High", "Why should moderation be run before calling generative LLMs?"),

    ("How do you call local models running on Ollama via its REST API?",
     "Ollama runs a local HTTP server on `http://localhost:11434`. Make a standard POST request to `/api/generate` or `/api/chat` with `{ model: 'llama3:8b', messages: [...] }`. It returns streaming JSON responses locally with zero internet access.",
     "Standard REST interface for running private models on local machines or VPCs.",
     "const res = await fetch('http://localhost:11434/api/chat', {\n  method: 'POST',\n  body: JSON.stringify({ model: 'llama3', messages: [{ role: 'user', content: 'Hi' }] })\n});",
     "Intermediate", "Tooling", "High", "What hardware is required to run LLaMA 3 8B locally at acceptable speeds?"),

    ("What are OpenAI-Compatible API endpoints (e.g. Groq, Together AI, vLLM)?",
     "Many AI infrastructure providers adopt the exact OpenAI REST format (`/v1/chat/completions`) and SDK interfaces. By simply changing `baseURL` and `apiKey`, you can switch your entire web app from OpenAI to Groq, Together AI, or a self-hosted vLLM instance with zero code changes.",
     "Enables switching model providers by changing two environment variables.",
     "const client = new OpenAI({\n  apiKey: process.env.GROQ_API_KEY,\n  baseURL: 'https://api.groq.com/openai/v1'\n});",
     "Intermediate", "Architecture", "High", "Why is OpenAI API compatibility an industry standard?"),

    ("How do you track latency metrics across AI API calls?",
     "Record timestamps: `start = performance.now()` before the call, record `firstToken = performance.now()` when the first SSE chunk arrives (TTFT), and `end = performance.now()` on completion. Log these metrics to your telemetry dashboard (Datadog, Langfuse).",
     "Tracking TTFT and total duration identifies slow prompts and model bottlenecks.",
     "const ttft = firstTokenTime - startTime;\nconst totalLatency = endTime - startTime;",
     "Intermediate", "Performance", "High", "What is an acceptable TTFT for web chat? (<800ms)"),

    ("How do you inspect and audit exact token usage from API responses?",
     "Read `response.usage` object: `prompt_tokens` (input), `completion_tokens` (output), and `total_tokens`. Store these integers in your database alongside the message record to generate user usage reports and monitor billing.",
     "Every non-streaming response returns exact token counts in the `usage` block.",
     "const { prompt_tokens, completion_tokens } = response.usage;\nawait db.usageLog.create({ data: { userId, prompt_tokens, completion_tokens } });",
     "Basic", "Economics", "High", "How do you obtain token usage metrics when streaming responses?"),

    ("How do you stream token usage in OpenAI streaming completions?",
     "By setting `stream_options: { include_usage: true }`, the API sends a final SSE chunk before closing that includes the full `usage` object with exact prompt and completion token counts.",
     "`include_usage: true` enables precise token metering even during real-time streaming.",
     "const stream = await openai.chat.completions.create({\n  model: 'gpt-4o-mini',\n  messages,\n  stream: true,\n  stream_options: { include_usage: true }\n});",
     "Intermediate", "Code", "High", "Why did early streaming implementations require custom tokenizer counting?"),

    ("What is Prompt Caching in AI provider APIs and how does it save 50-80% on costs?",
     "When an API receives a prompt with a long, static prefix (e.g. system instructions, documentation, few-shot examples > 1024 tokens) that matches recent requests, the provider reuses cached neural activations from memory, billing cached input tokens at a 50% to 80% discount with lower latency.",
     "Put static instructions and documentation at the top of prompts to trigger automatic prompt caching discounts.",
     "// OpenAI & Anthropic automatically cache prompt prefixes >= 1,024 tokens.",
     "Intermediate", "Economics", "High", "Why must the dynamic user input be placed at the END of the prompt to leverage caching?"),

    ("Practical: How do you build a multi-provider fallback client (OpenAI -> Anthropic)?",
     "Wrap primary API call in a try/catch. If primary fails with 500, 503, or timeout, catch the error and dispatch the request to the secondary provider using an adapter that normalizes the messages payload and output format.",
     "Multi-provider failover protects critical production services against vendor outages.",
     "async function chatWithFallback(messages) {\n  try { return await callOpenAI(messages); }\n  catch (e) { return await callAnthropic(messages); }\n}",
     "Practical", "Architecture", "High", "How do you handle feature parity differences between providers (e.g. tool calling schemas)?"),

    ("Practical: How do you implement server-side rate limiting per user in Express?",
     "Use `express-rate-limit` with a Redis store. Key by authenticated user ID (`req.user.id`). Set a window (e.g. 1 minute) and max requests (e.g. 10). Return 429 if the user exceeds their tier limit.",
     "Protects your backend from malicious or accidental user query spamming.",
     "const limiter = rateLimit({\n  windowMs: 60 * 1000,\n  max: (req) => req.user.tier === 'pro' ? 50 : 10,\n  keyGenerator: (req) => req.user.id\n});",
     "Practical", "Security", "High", "Why is rate limiting by IP address insufficient for authenticated SaaS apps?"),

    ("Scenario: Your API key was leaked on GitHub and disabled. How do you recover quickly?",
     "1) Immediately revoke the leaked key in the provider console. 2) Generate a new key and update environment variables in your hosting provider (Vercel/AWS). 3) Inspect audit logs for unauthorized billing spikes. 4) Set up GitHub Secret Scanning and pre-commit hooks (`gitleaks`) to prevent recurrence.",
     "Immediate revocation -> New key deployment -> Audit log review -> Secret scanning enforcement.",
     "// Never push .env files. Use secret managers in production.",
     "Scenario", "Security", "Critical", "What tool automatically blocks git commits containing secret keys? (`gitleaks` / `husky`)"),

    ("Scenario: An enterprise customer requires all AI traffic to stay within Europe. How do you configure the API?",
     "Use data residency controls provided by enterprise vendors (e.g. Azure OpenAI European endpoints, or AWS Bedrock in `eu-central-1`). These guarantee data processing and storage remain strictly within EU boundaries for GDPR compliance.",
     "Select regional API endpoints to comply with data residency and GDPR regulations.",
     "// Using Azure OpenAI with endpoint deployed in Frankfurt (westeurope).",
     "Scenario", "Security", "High", "What is the GDPR risk of sending EU citizen data to US-hosted AI APIs?"),

    ("Scenario: Your application needs to call AI for 100,000 users once a day to generate morning summaries. How do you architect this cost-effectively?",
     "Do not make 100,000 real-time API calls at 8 AM (you will hit TPM limits and pay full price). Instead: 1) Build a cron worker at midnight that compiles prompt requests into a JSONL file. 2) Submit via the OpenAI Batch API for a 50% discount. 3) Download completed summaries at 6 AM and cache in database for user display.",
     "Batch API cuts costs in half and avoids peak-hour rate limits for offline jobs.",
     "// 100,000 requests via Batch API = 50% discount + zero rate limit bottlenecks.",
     "Scenario", "Architecture", "High", "How much money does the Batch API save on a $1,000 generation job? ($500)")
]

def get_part2_questions(start_idx=75):
    all_q = []
    
    # 4. Prompt Engineering (40 questions)
    for idx, item in enumerate(pe_40_items):
        q_num = start_idx + len(all_q) + 1
        all_q.append({
            "id": f"q-aivibe-{q_num}",
            "num": q_num,
            "subject": "AI & Generative AI",
            "topic": "4. Prompt Engineering",
            "subTopic": "Techniques & Evaluation",
            "question": item[0],
            "answer": item[1],
            "shortExplanation": item[2],
            "codeExample": item[3],
            "difficulty": item[4],
            "questionType": item[5],
            "interviewImportance": item[6],
            "interviewRound": "Technical Round" if item[4] != "Scenario" else "System Design",
            "frequency": "High",
            "references": "Enterprise Prompt Engineering Standards",
            "followUpQuestions": item[7],
            "addedAt": q_num,
            "globalId": 5478 + q_num
        })

    # 5. AI + JavaScript (15 questions)
    for idx, item in enumerate(ai_js_15_items):
        q_num = start_idx + len(all_q) + 1
        all_q.append({
            "id": f"q-aivibe-{q_num}",
            "num": q_num,
            "subject": "AI & Generative AI",
            "topic": "5. AI + JavaScript",
            "subTopic": "Node.js & Client Integration",
            "question": item[0],
            "answer": item[1],
            "shortExplanation": item[2],
            "codeExample": item[3],
            "difficulty": item[4],
            "questionType": item[5],
            "interviewImportance": item[6],
            "interviewRound": "Technical Round" if item[4] != "Scenario" else "System Design",
            "frequency": "High",
            "references": "MDN / Node.js AI Best Practices",
            "followUpQuestions": item[7],
            "addedAt": q_num,
            "globalId": 5478 + q_num
        })

    # 6. AI + React (15 questions)
    for idx, item in enumerate(ai_react_15_items):
        q_num = start_idx + len(all_q) + 1
        all_q.append({
            "id": f"q-aivibe-{q_num}",
            "num": q_num,
            "subject": "AI & Generative AI",
            "topic": "6. AI + React",
            "subTopic": "UI/UX & Streaming Hooks",
            "question": item[0],
            "answer": item[1],
            "shortExplanation": item[2],
            "codeExample": item[3],
            "difficulty": item[4],
            "questionType": item[5],
            "interviewImportance": item[6],
            "interviewRound": "Technical Round" if item[4] != "Scenario" else "System Design",
            "frequency": "High",
            "references": "React 18 & Streaming Architecture",
            "followUpQuestions": item[7],
            "addedAt": q_num,
            "globalId": 5478 + q_num
        })

    # 7. AI APIs & Integration (20 questions)
    for idx, item in enumerate(ai_api_20_items):
        q_num = start_idx + len(all_q) + 1
        all_q.append({
            "id": f"q-aivibe-{q_num}",
            "num": q_num,
            "subject": "AI & Generative AI",
            "topic": "7. AI APIs & Integration",
            "subTopic": "API Architecture & Resilience",
            "question": item[0],
            "answer": item[1],
            "shortExplanation": item[2],
            "codeExample": item[3],
            "difficulty": item[4],
            "questionType": item[5],
            "interviewImportance": item[6],
            "interviewRound": "Technical Round" if item[4] != "Scenario" else "System Design",
            "frequency": "High",
            "references": "OpenAI / Anthropic API Reference",
            "followUpQuestions": item[7],
            "addedAt": q_num,
            "globalId": 5478 + q_num
        })

    return all_q

if __name__ == "__main__":
    qs = get_part2_questions(75)
    print(f"Part 2 questions total: {len(qs)}")
