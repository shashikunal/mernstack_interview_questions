"""
Course Curriculum Data for 28 Step-by-Step Vibe Coding Lessons,
14 Video Guides, 6 Project Blueprints, and Bad vs Improved Prompt Exercises.
"""

# =============================================================================
# 28 STEP-BY-STEP VIBE CODING & PROJECT LESSONS (Steps 1 to 28)
# =============================================================================
COURSE_STEPS = [
    {
        "step": 1,
        "title": "Understand AI-Assisted Development",
        "category": "Foundations",
        "description": "Learn the modern paradigm of human-in-the-loop AI software engineering.",
        "workflow": "Requirement → Developer → AI Tool → Code → Developer Review → Testing → Fix → Git",
        "concepts": [
            "What is AI-assisted development?",
            "What is Generative AI & how code models work",
            "AI coding assistants (Copilot, Cursor) vs AI coding agents (Antigravity, Claude Code)",
            "What AI coding tools can do: boilerplate, refactoring, regex, test cases, explanations",
            "What AI tools cannot do: system architecture, domain knowledge, security validation, production debugging",
            "Developer responsibility: Never blindly commit unreviewed code"
        ],
        "activity": {
            "title": "Interactive Requirement Breakdown",
            "prompt": "Requirement: 'Create a React login form with email, password, remember me, validation, and loading state.'",
            "exercise": "Before asking AI for code, draft the 4 key architectural constraints and requirements you must provide to the AI tool."
        }
    },
    {
        "step": 2,
        "title": "Learn Vibe Coding",
        "category": "Foundations",
        "description": "Understand what Vibe Coding means, why it is transformative, and how to stay in control.",
        "workflow": "Idea → Requirement → AI Prompt → Plan → Implementation → Run → Test → Debug → Review → Improve → Commit",
        "concepts": [
            "What Vibe Coding means: High-level intent-driven development where you direct the AI with natural language",
            "Why it is useful: 10x faster prototyping, rapid feedback loops, reduced cognitive friction",
            "Common mistakes: Accepting code without reading, generating entire applications at once, ignoring types and tests",
            "How to stay in control: Small incremental steps, strict project rules, Git checkpointing after every feature"
        ],
        "activity": {
            "title": "Vibe Coding Mindset Exercise",
            "prompt": "You want to build a Markdown Previewer in React.",
            "exercise": "Write down the step-by-step feature sequence you will prompt the AI to build one by one, rather than asking for the full app at once."
        }
    },
    {
        "step": 3,
        "title": "Learn AI Coding Tools",
        "category": "Tooling",
        "description": "Master the primary AI coding assistants and agentic tools without vendor lock-in.",
        "workflow": "Understand project → Give context → Plan → Implement → Review → Test → Debug → Commit",
        "tools": [
            {"name": "Cursor", "type": "AI-First IDE", "strength": "Multi-file codebase indexing (@Codebase, @Docs), inline editing (Ctrl+K), Composer (Ctrl+I)"},
            {"name": "Claude Code", "type": "CLI Agent", "strength": "Terminal-based autonomous agent, edits files, runs terminal commands, executes tests"},
            {"name": "Google Antigravity", "type": "Advanced Agentic IDE", "strength": "Multi-agent workflows, browser subagent testing, artifact verification, rules engine"},
            {"name": "GitHub Copilot", "type": "IDE Extension", "strength": "Real-time ghost-text autocomplete, Copilot Chat, workspace context"},
            {"name": "Windsurf", "type": "AI-First IDE", "strength": "Cascade flow, deep predictive code changes across multiple files"},
            {"name": "ChatGPT / Gemini", "type": "Web Chat", "strength": "Architecture brainstorming, algorithm explanation, code snippet refactoring"}
        ],
        "activity": {
            "title": "Tool Selection Decision",
            "exercise": "Which tool would you pick for: 1) Fixing a typo in 1 line? 2) Refactoring a 5-file module? 3) Debugging a production CLI build?"
        }
    },
    {
        "step": 4,
        "title": "First Vibe Coding Project: React Task Manager",
        "category": "Project",
        "description": "Build a responsive React + TypeScript + Tailwind CSS Task Manager using the structured Vibe Coding loop.",
        "techStack": "React 18, TypeScript, Tailwind CSS, Lucide React, localStorage",
        "process": [
            "4.1 Requirement: Tasks with title, priority (Low/Med/High), category, status (Todo/In Progress/Done), search & filter",
            "4.2 Ask AI for Plan: Request architecture and types only (do not generate JSX yet)",
            "4.3 Review Plan: Verify `Task` interface and state management strategy",
            "4.4 Implement Feature 1: Task list view & TaskCard component",
            "4.5 Implement Feature 2: Add task modal with validation",
            "4.6 Run Application: Test live in browser",
            "4.7 Fix Errors with AI: Provide exact console/compiler errors with file context",
            "4.8 Review Code: Verify no hardcoded mock data, check accessibility",
            "4.9 Git Commit: Commit clean feature branch with descriptive message"
        ]
    },
    {
        "step": 5,
        "title": "Learn How to Write Good Prompts (Enterprise Template)",
        "category": "Prompt Engineering",
        "description": "Master the 8-part Enterprise Prompt Template for predictable, high-quality code generation.",
        "template": """Role: You are a Senior React & TypeScript Engineer.
Objective: Create a reusable, accessible TaskCard component.
Context: Existing task management app using React 18, Tailwind CSS, and Lucide icons.
Instructions:
  1. Render task title, priority badge, and status dropdown.
  2. Call onStatusChange(id, newStatus) when user selects status.
  3. Include delete button with confirmation tooltip.
Constraints:
  - Do not create fake/sample data.
  - Do not modify unrelated components.
  - Adhere strictly to WCAG 2.1 AA keyboard accessibility.
Input: Task interface { id: string, title: string, priority: 'low'|'med'|'high', status: 'todo'|'done' }
Expected Output: Single TypeScript file with exported TaskCard component and props interface.
Output Format: Executable TypeScript code block without chat commentary.""",
        "activity": {
            "title": "Prompt Template Practice",
            "exercise": "Convert a vague prompt ('Make a navbar') into the 8-part Enterprise Prompt Template."
        }
    },
    {
        "step": 6,
        "title": "Practice Prompt Engineering: 12 Core Exercises",
        "category": "Prompt Engineering",
        "description": "Examine 12 real-world exercises comparing Bad Prompts vs Improved Prompts with token comparisons.",
        "exercisesCount": 12
    },
    {
        "step": 7,
        "title": "Learn Token Fundamentals",
        "category": "Economics & Latency",
        "description": "Understand what tokens are, how they are metered, and why token efficiency dictates cost and speed.",
        "concepts": [
            "What is a token? (~4 characters or 0.75 words in English)",
            "Input Tokens vs Output Tokens (Output tokens cost 3x-4x more and generate sequentially)",
            "Total Tokens and Context Window limits",
            "Token Latency (Time-To-First-Token vs Generation speed)",
            "What consumes tokens: Prompts, conversation history, attached files, terminal logs, tool schemas"
        ]
    },
    {
        "step": 8,
        "title": "Learn Token Optimization: 12 Production Techniques",
        "category": "Economics & Latency",
        "description": "Master the 12 non-negotiable rules of token reduction in web applications.",
        "corePrinciple": "Relevant context > maximum context.",
        "techniques": [
            "1. Keep prompts concise: Strip polite conversational filler.",
            "2. Remove repeated instructions across chat turns.",
            "3. Send only relevant files (use @file or @symbol rather than full codebase).",
            "4. Don't send entire repository unnecessarily.",
            "5. Summarize long conversations (sliding window of last 6 messages).",
            "6. Limit unnecessary output: Instruct model 'No commentary, code only'.",
            "7. Use structured output: Direct JSON instead of prose explanations.",
            "8. Use RAG for large documents instead of raw document stuffing.",
            "9. Cache repeated requests in Redis.",
            "10. Use smaller models (GPT-4o-mini / Haiku) for 90% of routine tasks.",
            "11. Use project instruction files (PROJECT_RULES.md) to define conventions once.",
            "12. Avoid repeatedly sending the same context across API calls."
        ]
    },
    {
        "step": 9,
        "title": "Create Project AI Rules (PROJECT_RULES.md)",
        "category": "Tooling",
        "description": "Establish a project instruction file to keep AI coding tools consistent, clean, and context-aware.",
        "templateFile": "PROJECT_RULES.md",
        "rulesContent": """# PROJECT CODING & ARCHITECTURE RULES

## Technology Stack
- Frontend: React 18, TypeScript, Tailwind CSS, Vite
- Backend: Node.js, Express, PostgreSQL / Supabase, Zod
- AI Integration: OpenAI Node SDK, Server-Sent Events (SSE)

## Architectural Guidelines
- All AI calls must be proxied through the Express backend.
- Never expose API keys in client-side React code.
- Validate all incoming API request bodies using Zod schemas.
- Use Server-Sent Events (SSE) for streaming text responses.

## Development Standards
- Strictly NO mock/fake data in production routes.
- Always check and preserve existing functionality before modifying files.
- Do not add new external libraries without explicit instruction.
- Follow TypeScript strict mode; avoid `any`.
- Keep components small and modular (<200 lines)."""
    },
    {
        "step": 10,
        "title": "Learn AI + JavaScript",
        "category": "Full Stack AI",
        "description": "Learn to call AI APIs from vanilla JavaScript and Node.js using async/await, fetch, and error handling.",
        "project": "Simple AI Chat Application (Console & Express API)"
    },
    {
        "step": 11,
        "title": "Learn AI + React",
        "category": "Full Stack AI",
        "description": "Build an AI Chat Assistant UI in React with typewriter streaming, auto-scroll, loading states, and Markdown.",
        "project": "Streaming AI Chat Assistant Component"
    },
    {
        "step": 12,
        "title": "Learn AI + Node.js / Express",
        "category": "Full Stack AI",
        "description": "Build a secure backend AI proxy with rate limiting, timeouts, exponential backoff, and token logging.",
        "project": "Production AI Proxy Microservice"
    },
    {
        "step": 13,
        "title": "Learn Database + AI",
        "category": "Full Stack AI",
        "description": "Store users, conversations, messages, prompt templates, and token audit logs in PostgreSQL or MongoDB.",
        "project": "Multi-Tenant Chat Database Schema"
    },
    {
        "step": 14,
        "title": "Learn AI Fundamentals Theory",
        "category": "Theory",
        "description": "Deep dive into the theoretical concepts: ML, DL, Foundation Models, Inference, Parameters, Temperature, Context."
    },
    {
        "step": 15,
        "title": "Learn LLM Fundamentals & Mechanics",
        "category": "Theory",
        "description": "Understand tokenization, self-attention, autoregressive loops, roles, structured outputs, and tool calling."
    },
    {
        "step": 16,
        "title": "Learn RAG (Retrieval-Augmented Generation)",
        "category": "RAG",
        "description": "Learn the complete RAG pipeline: Parsing → Chunking → Embeddings → Vector DB → Top-K Retrieval → LLM.",
        "workflow": "Document → Parser → Chunking → Embeddings → Vector Database → User Question → Relevant Chunks → LLM → Answer + Sources"
    },
    {
        "step": 17,
        "title": "Build RAG Project: AI Documentation Assistant",
        "category": "RAG Project",
        "description": "Build an interactive documentation search and Q&A bot in React & Express with PDF/Markdown upload and citation links.",
        "features": ["Document upload", "Chunking with overlap", "Vector search via pgvector", "Source attribution links"]
    },
    {
        "step": 18,
        "title": "Learn AI Agents",
        "category": "AI Agents",
        "description": "Understand AI agents: Agent loops, tool selection, memory, planning, and human-in-the-loop approval.",
        "workflow": "User Request → Agent (Search, DB, Calculator, GitHub, API) → Action Loop → Response"
    },
    {
        "step": 19,
        "title": "Build AI Agent Project: AI Developer Assistant",
        "category": "Agent Project",
        "description": "Build an autonomous developer assistant agent with tools to analyze code, search files, run tests, and create PR reviews."
    },
    {
        "step": 20,
        "title": "Learn AI Security",
        "category": "Security",
        "description": "Protect applications against Prompt Injection, PII leakage, unauthenticated tool execution, and quota exhaustion.",
        "rules": ["Delimiters for untrusted input", "Backend proxy for API keys", "Output validation with Zod", "User rate limiting with Redis"]
    },
    {
        "step": 21,
        "title": "Learn AI Evaluation (Evals)",
        "category": "Testing",
        "description": "Implement automated evaluation test suites using programmatic assertions, golden test datasets, and LLM-as-a-judge."
    },
    {
        "step": 22,
        "title": "Build Project: AI Technical Interview Assistant",
        "category": "Portfolio Project",
        "description": "Build an interview preparation application that asks questions, evaluates user answers with rubrics, and tracks scores.",
        "subjects": ["HTML", "CSS", "JavaScript", "React", "TypeScript", "Node.js", "SQL", "MongoDB", "Git"]
    },
    {
        "step": 23,
        "title": "Build Project: AI Resume Reviewer",
        "category": "Portfolio Project",
        "description": "Build a resume scoring portal that parses PDF resumes, matches skills against job descriptions, and gives actionable fixes."
    },
    {
        "step": 24,
        "title": "Build Project: AI Coding Assistant & Sandbox",
        "category": "Portfolio Project",
        "description": "Build a web-based coding assistant that generates, explains, debugs, refactors, and tests code snippets in real-time."
    },
    {
        "step": 25,
        "title": "Build Project: AI MCQ Assessment Generator",
        "category": "Portfolio Project",
        "description": "Build a quiz generator that synthesizes non-duplicate multiple choice questions with verified explanations and stores them."
    },
    {
        "step": 26,
        "title": "Complete AI Vibe-Coding Project: End-to-End SaaS",
        "category": "Capstone Project",
        "description": "Take a project from Idea → Architecture → Database → API → Frontend → AI Integration → Git → Netlify Deployment.",
        "checklist": ["Prompt logs recorded", "Zero fake data", "Token optimization applied", "Architecture diagram documented"]
    },
    {
        "step": 27,
        "title": "AI Coding Tool Practical Videos",
        "category": "Video Curriculum",
        "description": "14 practical, structured demonstration video guides covering workflows, prompts, and exercises.",
        "videosCount": 14
    },
    {
        "step": 28,
        "title": "Interactive Practice Flow",
        "category": "Mastery",
        "description": "The complete 7-step learning mastery loop applied to every topic.",
        "loop": "Learn → Watch → Practice → Build → Test → Quiz → Interview Question"
    }
]

# =============================================================================
# 14 VIDEO DEMONSTRATIONS CURRICULUM (Step 27)
# =============================================================================
VIDEO_LESSONS = [
    {
        "id": "vid-1",
        "title": "1. Modern AI-Assisted Web Development",
        "objective": "Understand how senior engineers use AI coding tools to accelerate development without losing control.",
        "demonstration": "Walkthrough of human-in-the-loop workflow: Requirement → Prompt → Review → Test → Git Commit.",
        "promptUsed": "Role: Senior Web Developer. Help me plan a React counter component with reset and step size. Outline props and state first.",
        "exercise": "Formulate a prompt to plan a shopping cart component without generating JSX code.",
        "interviewQuestions": ["What is developer responsibility in AI-assisted coding?", "Why shouldn't you accept AI code without reading it?"]
    },
    {
        "id": "vid-2",
        "title": "2. The Art of Vibe Coding: Concept to Code",
        "objective": "Master high-speed iterative Vibe Coding while maintaining strict code quality standards.",
        "demonstration": "Building an animated toggle button from a simple natural language idea in 3 iterative turns.",
        "promptUsed": "Create a smooth animated dark/light mode toggle button in React using Tailwind CSS. Use clean micro-interactions.",
        "exercise": "Vibe code an interactive star rating component in 2 prompt iterations.",
        "interviewQuestions": ["What is Vibe Coding and when is it most useful?", "What are the common pitfalls of Vibe Coding?"]
    },
    {
        "id": "vid-3",
        "title": "3. Building Your First AI-Built React Project",
        "objective": "Build a React Task Manager step by step using an AI coding assistant.",
        "demonstration": "Step-by-step feature implementation: types first, then UI, then localStorage persistence.",
        "promptUsed": "Based on our Task interface, create the TaskCard component with priority badges and delete button.",
        "exercise": "Add a category filter dropdown to the task manager using AI.",
        "interviewQuestions": ["Why shouldn't you ask an AI tool to generate an entire project at once?", "How do you test AI-generated React components?"]
    },
    {
        "id": "vid-4",
        "title": "4. Mastering Cursor: Codebase Indexing & Composer",
        "objective": "Learn Cursor's @Codebase, @Docs, Ctrl+K inline edits, and multi-file Composer features.",
        "demonstration": "Using `@Codebase` to find all API routes and refactoring authentication middleware in seconds.",
        "promptUsed": "@Codebase Find all components using legacy React context and refactor to use Zustand store.",
        "exercise": "Use Cursor's inline edit (Ctrl+K) to add TypeScript types to a legacy JS function.",
        "interviewQuestions": ["How does Cursor index a codebase?", "What is the difference between inline editing and Composer?"]
    },
    {
        "id": "vid-5",
        "title": "5. Claude Code CLI: Autonomous Terminal Agent",
        "objective": "Use Claude Code in your terminal to inspect errors, run tests, and commit fixes autonomously.",
        "demonstration": "Running `claude` in terminal, asking it to fix failing Jest tests, reviewing diffs, and committing.",
        "promptUsed": "claude 'Run vitest, identify failing auth tests, and fix the expired token validation logic'",
        "exercise": "Use Claude Code to generate JSDoc comments for all exported functions in a file.",
        "interviewQuestions": ["What is an AI coding agent?", "How do you review changes made by a terminal AI agent before pushing?"]
    },
    {
        "id": "vid-6",
        "title": "6. Google Antigravity & Agentic IDE Workflows",
        "objective": "Learn Antigravity IDE agent workflows, browser subagent testing, and artifact verification.",
        "demonstration": "Deploying a full-stack feature with automated browser validation and artifact inspection.",
        "promptUsed": "Verify the checkout flow in the browser subagent, take screenshots of success state, and report any UI errors.",
        "exercise": "Create a customization rule in AGY to enforce clean Git commit messages.",
        "interviewQuestions": ["What is an Antigravity browser subagent?", "How do project rules improve agent consistency?"]
    },
    {
        "id": "vid-7",
        "title": "7. GitHub Copilot: Ghost Text & Workspace Context",
        "objective": "Maximize autocomplete efficiency, Copilot Chat, and `/explain` commands in VS Code.",
        "demonstration": "Using inline ghost text to auto-complete boilerplate API handlers and typing `/tests` in Copilot Chat.",
        "promptUsed": "/tests Generate comprehensive Vitest unit tests covering null inputs and network errors for this hook.",
        "exercise": "Use Copilot Chat to explain a complex regex pattern in plain English.",
        "interviewQuestions": ["How does GitHub Copilot select context from open editor tabs?", "What are the limitations of inline ghost text?"]
    },
    {
        "id": "vid-8",
        "title": "8. ChatGPT & Gemini for Architecture & Planning",
        "objective": "Use web AI chats for high-level system design, schema planning, and API contract design.",
        "demonstration": "Brainstorming a scalable database schema for an AI interview platform and designing API routes.",
        "promptUsed": "Act as a Database Architect. Design a normalized PostgreSQL schema for a multi-tenant AI chat app. Include token audit logs.",
        "exercise": "Plan the REST API endpoints and payload schemas for an AI resume review platform.",
        "interviewQuestions": ["When should you use ChatGPT/Gemini web chat vs an in-editor AI tool?", "How do you transfer architecture plans into your IDE?"]
    },
    {
        "id": "vid-9",
        "title": "9. AI-Powered Debugging & Root Cause Analysis",
        "objective": "Diagnose tricky React re-render loops, async race conditions, and memory leaks with AI.",
        "demonstration": "Pasting console error traces and component code into AI to find root cause and clean fix.",
        "promptUsed": "Here is the React console warning 'Maximum update depth exceeded' and the component code. Identify which useEffect is triggering the loop.",
        "exercise": "Debug an unhandled promise rejection in an Express async route handler using AI.",
        "interviewQuestions": ["How do you formulate an effective debugging prompt?", "Why must you provide both the error trace and relevant code?"]
    },
    {
        "id": "vid-10",
        "title": "10. Automated Code Review with AI Tools",
        "objective": "Build automated PR review workflows checking SOLID principles, security, and performance.",
        "demonstration": "Running an automated prompt against a Git diff to catch missing indexes, XSS flaws, and dead code.",
        "promptUsed": "Review this Git diff for security flaws, missing error handling, and performance bottlenecks. Output as a Markdown checklist.",
        "exercise": "Create a code review prompt that specifically enforces your team's TypeScript conventions.",
        "interviewQuestions": ["Can AI replace human code reviews?", "What security vulnerabilities does AI code review excel at catching?"]
    },
    {
        "id": "vid-11",
        "title": "11. Unit & Integration Test Generation",
        "objective": "Generate high-coverage unit tests with mocks, edge cases, and boundary value tests using AI.",
        "demonstration": "Prompting AI to generate a complete Vitest test suite for an async custom hook, including network failure mocks.",
        "promptUsed": "Write Vitest unit tests for this useFetch hook. Mock global fetch. Cover: 200 OK, 404 Not Found, 500 Server Error, and timeout.",
        "exercise": "Generate unit tests for a currency formatting utility covering zero, negative numbers, and non-numeric inputs.",
        "interviewQuestions": ["Why is AI particularly effective at generating unit test cases?", "What is the danger of AI-generated tests passing trivially?"]
    },
    {
        "id": "vid-12",
        "title": "12. Token & Latency Optimization in Practice",
        "objective": "Cut API costs by 80% and drop response latency using streaming, chunking, and concise prompts.",
        "demonstration": "Live comparison: Naive 100-page document prompt vs 500-token RAG chunk prompt showing token count and latency metrics.",
        "promptUsed": "Rewrite this 300-word prompt into a 30-word prompt that produces identical output without conversational filler.",
        "exercise": "Calculate monthly cost savings for an app processing 20,000 requests/day after reducing prompt tokens from 2,000 to 400.",
        "interviewQuestions": ["Why do output tokens cost more than input tokens?", "How does response caching in Redis eliminate token costs for frequent queries?"]
    },
    {
        "id": "vid-13",
        "title": "13. Project Planning with AI Project Rules",
        "objective": "Set up a clean `PROJECT_RULES.md` and instruct AI tools to adhere to architecture standards.",
        "demonstration": "Creating a `PROJECT_RULES.md` in a fresh repository and observing how Cursor / Copilot respects coding standards.",
        "promptUsed": "Read our PROJECT_RULES.md. Create the user authentication service adhering strictly to our JWT and Zod conventions.",
        "exercise": "Write a `PROJECT_RULES.md` for a Next.js 14 project enforcing Server Components and Tailwind CSS.",
        "interviewQuestions": ["Why do project instruction files reduce token consumption across chat sessions?", "What rules should every production project file include?"]
    },
    {
        "id": "vid-14",
        "title": "14. Complete Full-Stack Project: Idea to Deployment",
        "objective": "Watch an entire full-stack application built, tested, and deployed live using AI tools.",
        "demonstration": "From initial blank folder → schema → Express API → React UI → AI streaming → Netlify deploy in 40 minutes.",
        "promptUsed": "Let's build the AI Interview Assistant. Phase 1: Initialize Express server with Zod validation and OpenAI streaming route.",
        "exercise": "Deploy your own AI Task Manager or Documentation Assistant project to Netlify or Vercel.",
        "interviewQuestions": ["How would you explain your AI project architecture in a job interview?", "What challenges did you face and how did you resolve them?"]
    }
]

# =============================================================================
# 12 BAD VS IMPROVED PROMPT EXERCISES (Step 6)
# =============================================================================
PROMPT_EXERCISES = [
    {
        "id": "pe-1",
        "task": "Generate React Component",
        "badPrompt": "Make a React button component.",
        "whyBad": "Lacks framework version, styling rules, props interface, accessibility requirements, and error boundaries. Produces generic, un-typed code.",
        "improvedPrompt": "Role: Senior React Engineer. Create a reusable PrimaryButton component using React 18, TypeScript, and Tailwind CSS. Props: label (string), onClick, disabled (boolean), loading (boolean). Requirements: WCAG 2.1 AA accessible, spinner when loading, disabled styles. Output: TypeScript code only.",
        "expectedOutput": "Fully typed Button component with LoadingSpinner and accessible ARIA attributes.",
        "tokenComparison": "Bad Prompt: 7 tokens -> Output: ~180 tokens (Generic/Useless). Improved Prompt: 62 tokens -> Output: ~140 tokens (100% Production-Ready). Net engineering time saved: 20 minutes."
    },
    {
        "id": "pe-2",
        "task": "Debug JavaScript Bug",
        "badPrompt": "Fix this code it is not working.",
        "whyBad": "Provides no error trace, no context on what 'not working' means, no input examples, and no expected behavior.",
        "improvedPrompt": "Debug this Express async route. Issue: When db.query throws an error, the request hangs forever instead of returning 500. Identify root cause and provide fixed code with try/catch and next(err). Code: ```app.get('/users', async (req, res) => { const users = await db.get(); res.json(users); });```",
        "expectedOutput": "Explanation of unhandled promise rejection in Express 4 + fixed route with error middleware.",
        "tokenComparison": "Bad Prompt: 8 tokens -> 3 follow-up turns required (Total ~900 tokens). Improved Prompt: 68 tokens -> 1 turn fix (~150 tokens). 75% token reduction."
    },
    {
        "id": "pe-3",
        "task": "Explain TypeScript Code",
        "badPrompt": "What does this code do?",
        "whyBad": "Produces overly academic, verbose explanations without context on how a junior developer should apply it.",
        "improvedPrompt": "Explain this TypeScript generic utility `type DeepPartial<T> = { [P in keyof T]?: DeepPartial<T[P]> };` to a junior web developer. Use a realistic UserProfile state analogy and show a before/after example.",
        "expectedOutput": "Concise analogy comparing shallow partial vs recursive deep partial with clean code snippet.",
        "tokenComparison": "Bad: Vague 500-word essay. Improved: Structured 120-word explanation with actionable example."
    },
    {
        "id": "pe-4",
        "task": "Review Code for Security",
        "badPrompt": "Is this code good?",
        "whyBad": "'Good' is subjective. The model will give generic compliments rather than auditing security vulnerabilities.",
        "improvedPrompt": "Role: Web Security Auditor. Audit this Node.js endpoint for OWASP Top 10 vulnerabilities (specifically SQL injection, missing rate limiting, and unvalidated user input). Output a markdown checklist of findings with line numbers and remediation code.",
        "expectedOutput": "Targeted vulnerability report highlighting parameterized query fixes and rate limiting middleware.",
        "tokenComparison": "Focused security audit saves hours of potential security review revisions."
    },
    {
        "id": "pe-5",
        "task": "Refactor Code",
        "badPrompt": "Make this code cleaner.",
        "whyBad": "Subjective. Might rewrite working logic or introduce unnecessary dependencies.",
        "improvedPrompt": "Refactor this legacy React class component to a functional component using React Hooks (useState, useEffect). Constraints: Preserve exact prop names, do not introduce external state libraries, ensure cleanup function handles event listeners.",
        "expectedOutput": "Clean, drop-in replacement functional component with identical behavior.",
        "tokenComparison": "Explicit constraints prevent hallucinated dependencies and unwanted architectural rewrites."
    },
    {
        "id": "pe-6",
        "task": "Generate Unit Tests",
        "badPrompt": "Write tests for this function.",
        "whyBad": "Will generate 1 trivial test case and omit edge cases, mock dependencies, and error branches.",
        "improvedPrompt": "Write unit tests for this calculateCartTotal function using Vitest. Requirements: Cover happy path, empty cart, negative quantities, floating-point rounding errors (0.1 + 0.2), and invalid item prices. Provide 100% executable code without placeholder comments.",
        "expectedOutput": "Complete Vitest test suite with describe/it blocks covering all boundary conditions.",
        "tokenComparison": "Saves developer from manually writing 5 edge-case test definitions."
    },
    {
        "id": "pe-7",
        "task": "Generate REST API Route",
        "badPrompt": "Create an API for products.",
        "whyBad": "Omits HTTP method, path, validation rules, authentication requirements, and database schema.",
        "improvedPrompt": "Create an Express router handler for POST /api/v1/products. Requirements: 1) Validate request body using Zod (name: string, price: number > 0, category: enum). 2) Return 201 Created on success with JSON envelope { success: true, data }. 3) Return 400 Bad Request on validation failure. TypeScript code only.",
        "expectedOutput": "Production-grade Express router with Zod validation middleware.",
        "tokenComparison": "Clean, error-handled route in 1 turn without back-and-forth debugging."
    },
    {
        "id": "pe-8",
        "task": "Generate API Documentation",
        "badPrompt": "Document this API.",
        "whyBad": "Generates informal text paragraphs that cannot be rendered in Swagger or developer portals.",
        "improvedPrompt": "Generate OpenAPI 3.0 YAML documentation for this Express checkout endpoint. Include path parameters, requestBody schema with required fields, 200 response with orderId, and 402 Payment Required response.",
        "expectedOutput": "Valid, copy-pasteable OpenAPI 3.0 YAML specification.",
        "tokenComparison": "Standardized YAML specification ready for Swagger UI rendering."
    },
    {
        "id": "pe-9",
        "task": "Generate SQL Query",
        "badPrompt": "Write SQL to find top users.",
        "whyBad": "Has no database schema, no definition of 'top users', and risks SQL injection.",
        "improvedPrompt": "Write a PostgreSQL query to find the top 10 users by total spend in 2024. Schema: users (id, name, created_at), orders (id, user_id, amount_cents, status, created_at). Constraints: Consider only status = 'completed', use parameterized year placeholder $1, output total in dollars (amount_cents / 100).",
        "expectedOutput": "Safe, parameterized SQL query with JOIN, GROUP BY, and LIMIT.",
        "tokenComparison": "Parameterized query prevents SQL injection vulnerabilities."
    },
    {
        "id": "pe-10",
        "task": "Analyze Resume for Web Dev Role",
        "badPrompt": "Check this resume.",
        "whyBad": "Lacks job criteria, scoring rubric, and output structure. Generates vague praise.",
        "improvedPrompt": "Analyze this candidate resume for a Junior React & Node.js Developer position. Evaluate against criteria: 1) Core JavaScript/TypeScript depth, 2) React ecosystem (Hooks, state management), 3) Node.js/Express APIs, 4) Real project complexity. Output a JSON object with: matchScore (1-100), keyStrengths, missingKeywords, and 3 technical interview questions.",
        "expectedOutput": "Structured evaluation JSON with objective score and tailored interview questions.",
        "tokenComparison": "JSON format enables direct database insertion and candidate scorecard rendering."
    },
    {
        "id": "pe-11",
        "task": "Generate Technical Interview Questions",
        "badPrompt": "Give me React interview questions.",
        "whyBad": "Produces generic questions like 'What is React?' found on every basic blog.",
        "improvedPrompt": "Generate 5 scenario-based technical interview questions for a Mid-Level React Developer. Focus areas: 1) Performance optimization with useMemo/useCallback, 2) Race conditions in useEffect data fetching, 3) Custom hook state isolation. For each question, provide the evaluation rubric and expected candidate answer.",
        "expectedOutput": "5 deep, scenario-driven interview questions with scoring criteria.",
        "tokenComparison": "Scenario questions evaluate real problem-solving over rote memorization."
    },
    {
        "id": "pe-12",
        "task": "Evaluate Interview Answer",
        "badPrompt": "Is this answer right?",
        "whyBad": "Binary 'yes/no' without constructive feedback, depth analysis, or missed nuances.",
        "improvedPrompt": "Evaluate this candidate's answer to 'Explain Event Loop in JavaScript'. Rubric: Call stack, Web APIs, Macrotask queue (setTimeout), Microtask queue (Promises). Score accuracy (1-5) and identify any technical misconceptions. Output constructive feedback in markdown.",
        "expectedOutput": "Objective score with breakdown of microtask vs macrotask execution order.",
        "tokenComparison": "Calibrated scoring prevents subjective or biased interview assessments."
    }
]
