# scripts/build_hr_part3.py

hr_part3 = [
    # Workplace Ethics, Integrity & Professional Conduct
    (
        "What would you do if you were asked to cut corners and skip testing to meet an urgent deadline?",
        "1) Acknowledge the business urgency. 2) Explain the risks of deploying untested code: regressions, outages, and poor user trust. 3) Propose a pragmatic compromise: write automated tests for critical happy paths and payment/auth flows now, and schedule secondary edge case tests for the next sprint.",
        "Intermediate",
        "Scenario",
        "Risk mitigation:\nHighlight production outage risk -> Prioritize critical path testing -> Schedule fast-follow tech debt ticket.",
        "Why does deploying untested code almost always result in higher total development time?"
    ),
    (
        "How do you handle confidential company information or user data?",
        "1) Never share internal documentation, credentials, or proprietary source code on personal accounts, forums, or external AI tools. 2) Adhere strictly to company Non-Disclosure Agreements (NDAs). 3) Follow least-privilege principles when accessing production user databases.",
        "Easy",
        "Concept",
        "Principles:\n- Zero sharing of proprietary IP on public forums\n- Adherence to NDAs\n- Protecting PII (Personally Identifiable Information)",
        "What is GDPR and what happens to a company that leaks customer data?"
    ),
    (
        "What would you do if you accidentally deleted or corrupted data in a test database?",
        "1) Don't panic or attempt to hide it. 2) Immediately inform the team lead or database administrator. 3) Assist in restoring data from snapshots or running seed scripts. 4) Help document permissions or safeguards to prevent accidental drops in the future.",
        "Easy",
        "Scenario",
        "Honesty and prompt notification allow swift recovery before others waste hours troubleshooting mysterious missing test data.",
        "Why should non-production environments have clear automated reset/seed scripts?"
    ),
    (
        "How do you handle working on a task where you feel the specifications are flawed?",
        "1) Avoid criticizing the author. 2) Formulate a polite, well-reasoned explanation of potential pitfalls with concrete user examples. 3) Schedule a 10-minute sync with the product manager or designer: 'I was thinking about edge case X where a user has no orders; how should the layout behave here?'",
        "Intermediate",
        "Scenario",
        "Constructive inquiry through edge cases helps designers and PMs refine requirements without feeling attacked.",
        "Why is early feedback during the design phase 10x cheaper than changing code after launch?"
    ),
    (
        "What is your approach to handling constructive criticism from someone younger or with less tenure than you?",
        "Good ideas and valid criticism have no age or tenure boundaries. Focus purely on the substance of the feedback. If the suggestion improves code readability, performance, or system stability, thank them and implement it with humility.",
        "Easy",
        "Concept",
        "Meritocracy in engineering:\nCode quality, logic, and facts matter, not seniority hierarchy.",
        "How does a culture of open peer feedback help junior engineers grow faster?"
    ),
    (
        "How do you maintain a positive attitude during a high-stress production outage?",
        "1) Stay calm and focus on stabilization rather than blame. 2) Follow the incident response protocol: communicate status clearly, rollback to the last known stable release if possible, and gather logs. 3) Keep emotional panic out of incident chat channels.",
        "Intermediate",
        "Scenario",
        "Protocol:\nStay composed -> Follow incident playbooks -> Rollback first, diagnose second.",
        "Why is 'rollback first, debug later' the standard operational procedure during production outages?"
    ),
    (
        "What would you do if you see a colleague being bullied or excluded by others in the team?",
        "1) Do not be a passive bystander. 2) Include them actively in conversations, lunch catch-ups, and discussions. 3) Privately ask them how they are doing and offer support. 4) If the behavior violates workplace harassment policies, report it confidentially to HR or team management.",
        "Easy",
        "Scenario",
        "Active inclusion and psychological safety are the collective responsibility of all team members.",
        "Why is workplace harassment or exclusion detrimental to team productivity and retention?"
    ),
    (
        "How do you handle disagreement with a peer over code formatting or style preferences?",
        "Eliminate personal preferences by relying on automated tooling: Adopt standard community style guides (like Airbnb or Google JavaScript Style Guide) enforced automatically by Prettier and ESLint. If the linter accepts it, accept it without bike-shedding.",
        "Easy",
        "Concept",
        "Automated formatting stops wasted debate over tabs vs spaces and semicolon placement.",
        "What does the term 'bike-shedding' mean in engineering discussions?"
    ),
    (
        "How do you approach learning a large, unfamiliar enterprise codebase?",
        "1) Run the app locally and step through a primary user workflow in the UI. 2) Trace the entry points: server.js/index.js for backend, App.jsx/router for frontend. 3) Read unit and integration test files to see how functions are called. 4) Sketch an architectural diagram of component interactions.",
        "Intermediate",
        "Practical",
        "Exploration strategy:\nRun locally -> Follow user request path -> Read tests -> Sketch module architecture.",
        "Why is reading test suites often the quickest way to understand what a function is supposed to do?"
    ),
    (
        "How do you handle working remotely vs working in an office? Which do you prefer?",
        "State adaptability: In an office, appreciate spontaneous collaboration, face-to-face mentorship, and building team bonds. In remote work, appreciate deep focus blocks and asynchronous documentation culture. Comfortable and productive in hybrid or either model.",
        "Easy",
        "Concept",
        "Highlight adaptability, disciplined time management, and proactive communication in remote settings.",
        "What are the key habits that make a remote software engineer effective?"
    ),
    (
        "What do you do if you are blocked by a third-party API that is down or has rate limits during development?",
        "1) Create a mock data service or stub endpoint that returns realistic dummy JSON. 2) Continue developing frontend or downstream logic against the mock interface. 3) Swap the mock service with the real API once connectivity is restored.",
        "Easy",
        "Practical",
        "Mocking external dependencies ensures your personal velocity is never blocked by external downtime.",
        "What is the role of tools like MSW (Mock Service Worker) in frontend development?"
    ),
    (
        "How do you handle sudden changes in team leadership or management?",
        "1) Maintain professionalism and keep focus on sprint deliverables. 2) Welcome the new leader and share a concise overview of your current projects and strengths. 3) Be open to new processes, metrics, or team rituals they might introduce.",
        "Easy",
        "Scenario",
        "Adaptability and positive collaboration during management transitions demonstrate professional maturity.",
        "How do 1-on-1 meetings help align expectations with a new manager?"
    ),
    (
        "What is your approach to asking for help without appearing incompetent?",
        "Structure the ask with three parts: 1) What you are trying to accomplish. 2) What you have already tried (including error logs and documentation links). 3) Where you are currently stuck. This shows initiative, saves the senior's time, and earns respect.",
        "Easy",
        "Practical",
        "The 3-part ask:\n'Goal: Setting up Redis session store. Tried: Followed docs and verified port 6379 is open. Stuck: Getting ECONNREFUSED on localhost. Could you spot what I missed?'",
        "Why do seniors appreciate structured questions over 'It is not working'?"
    ),
    (
        "How do you handle receiving conflicting feedback from two different code reviewers?",
        "1) Do not make angry back-and-forth edits on the PR. 2) Tag both reviewers on the specific PR comment thread: 'Reviewer A suggested approach X for caching, while Reviewer B suggested approach Y. Could we align on which direction best serves this module?' 3) Let them agree or follow the lead's decision.",
        "Intermediate",
        "Scenario",
        "Transparent alignment on the PR thread resolves conflicting feedback cleanly without duplicate work.",
        "Why should technical debates be resolved on the PR thread rather than private DMs?"
    ),
    (
        "What would you do if you notice a teammate taking credit for your contribution in a meeting?",
        "1) Do not cause a public confrontation in front of stakeholders. 2) In the meeting, smoothly add context: 'Yes, as Sarah mentioned, when I built the auth middleware, we ensured token expiry was 15 minutes.' 3) Later, speak to them privately to establish clear mutual attribution for future demos.",
        "Intermediate",
        "Scenario",
        "Graceful public addition of context + Private conversation to maintain positive professional boundaries.",
        "Why is staying calm and adding technical specifics the best way to claim ownership gracefully?"
    ),
    (
        "How do you handle repetitive questions from end-users or internal testers?",
        "1) Answer politely with empathy. 2) Recognize that repeated questions indicate a gap in product UX or documentation. 3) Create an FAQ guide, update tooltips in the UI, or write an internal wiki so future users can self-serve answers easily.",
        "Easy",
        "Concept",
        "Turn repetitive support questions into permanent documentation and UX improvements.",
        "How does updating self-serve documentation scale support bandwidth?"
    ),
    (
        "What does 'code readability' mean to you and why is it important?",
        "Code is read 10 times more often than it is written. Readable code has descriptive naming, small focused functions, predictable data flow, and minimal clever tricks. Readable code reduces cognitive load during reviews and dramatically decreases bug rates during maintenance.",
        "Easy",
        "Concept",
        "Quote: 'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.' — Martin Fowler.",
        "Why is overly clever one-line code often a liability in team codebases?"
    ),
    (
        "How do you approach mentoring or helping a junior peer who is struggling?",
        "1) Practice patience and create a supportive space where they feel comfortable asking questions. 2) Avoid grabbing their keyboard; guide them verbally so they build muscle memory. 3) Explain the mental model behind concepts rather than just dictating syntax.",
        "Easy",
        "Scenario",
        "Guiding principles:\n- Hands off the keyboard\n- Teach problem-solving process\n- Reinforce small wins",
        "Why does teaching someone else deepen your own technical understanding?"
    ),
    (
        "How do you ensure your code handles unexpected errors gracefully in production?",
        "1) Never leave empty catch blocks. 2) Validate all external inputs at application boundaries. 3) Implement fallback states and informative, friendly error messages for users. 4) Log full error traces with contextual metadata to logging monitoring tools.",
        "Intermediate",
        "Practical",
        "Defensive programming checklist:\nBoundary validation + Centralized error middleware + User fallback UI + Detailed structured logs.",
        "Why is swallowing errors with 'catch (e) {}' dangerous in production software?"
    ),
    (
        "What would you do if a feature you developed is rejected by the QA testing team?",
        "1) Don't get defensive; QA is your safety net before real customers see bugs. 2) Review the reproduction steps and logs provided in the bug ticket. 3) Reproduce locally in the same environment. 4) Fix the root cause, write a regression test to prevent recurrence, and communicate the fix back to QA.",
        "Easy",
        "Scenario",
        "QA collaboration:\nRespect QA as quality partners -> Reproduce -> Add regression test -> Re-test together.",
        "Why is a collaborative relationship between Developers and QA vital for product quality?"
    ),
    (
        "How do you handle working on a task where the requirements keep shifting every day ('Scope Creep')?",
        "1) Document each new request as a delta against the original scope. 2) Communicate the cumulative impact on the release timeline to the project manager. 3) Recommend freezing the current scope for v1 release and logging new requests as backlog items for v1.1.",
        "Intermediate",
        "Scenario",
        "Mitigation:\nDocument scope delta -> Quantify schedule impact -> Propose phased release freeze.",
        "What is the danger of letting scope creep unchecked without adjusting deadlines?"
    ),
    (
        "What do you do if you notice a security risk in a third-party npm package used in your project?",
        "1) Run 'npm audit' to inspect the severity level and CVE advisory. 2) Check if an updated patch version exists that resolves the vulnerability without breaking API changes. 3) If no official patch exists, evaluate alternative packages or apply an isolated patch. 4) Open a PR with audit logs.",
        "Intermediate",
        "Practical",
        "Security triage:\nAudit advisory -> Version bump test -> Safe replacement -> PR review.",
        "What is a zero-day vulnerability in the open-source supply chain?"
    ),
    (
        "How do you handle personal burnout or mental fatigue during extended coding sessions?",
        "1) Follow the 50/10 rule: 50 minutes of focused coding followed by a 10-minute break away from screens. 2) Stay hydrated and stretch to avoid physical strain. 3) If deeply fatigued, get a good night's sleep; complex bugs that take 3 hours when exhausted often take 5 minutes with a refreshed mind.",
        "Easy",
        "Practical",
        "Mental recovery:\nScheduled breaks + Physical movement + Sleep over late-night debugging.",
        "Why does sleep deprivation significantly impair short-term working memory required for coding?"
    ),
    (
        "How do you approach estimating how long a technical task will take?",
        "1) Break the task down into sub-components: database schema, API route, frontend UI, testing, and edge cases. 2) Estimate each sub-task in hours. 3) Add a 20-30% buffer for unexpected bugs, code review iterations, and integration friction. 4) Communicate assumptions clearly.",
        "Intermediate",
        "Concept",
        "Estimation formula:\nTask breakdown + Sub-task hours + 25% integration buffer = Realistic estimate.",
        "Why do developers consistently underestimate tasks when they forget to budget for testing and reviews?"
    ),
    (
        "What would you do if you make a mistake that brings down a testing or staging environment?",
        "1) Announce it immediately in the team dev channel: 'Hey team, staging is temporarily down due to an issue in PR #42; I am reverting now.' 2) Revert the commit to restore staging availability for teammates. 3) Debug locally and only re-deploy once verified.",
        "Easy",
        "Scenario",
        "Transparent announcement saves everyone on the team from wasting time debugging broken staging environments.",
        "Why is fast communication more important than feeling embarrassed about breaking staging?"
    ),
    (
        "How do you decide between building a custom utility function versus importing an npm library?",
        "Evaluate trade-offs: For simple tasks (e.g. capitalize string, debounce, simple date formatting), write a clean 5-line native utility to avoid supply-chain bloat. For complex, security-sensitive, or standards-heavy tasks (e.g. bcrypt, JWT, complex timezone math), use well-maintained, battle-tested libraries.",
        "Intermediate",
        "Comparison",
        "Trade-off criteria:\n- Maintenance burden\n- Bundle size impact\n- Security & edge-case robustness",
        "What was the infamous 'left-pad' incident in npm history and what did it teach developers?"
    ),
    (
        "What is your approach to handling negative feedback from a user during a product beta test?",
        "1) Listen without defensiveness; candid user feedback is gold for product improvement. 2) Separate emotion from user pain: identify what they were trying to achieve and where the UI caused friction. 3) Log the UX issue and brainstorm simplified workflows with the team.",
        "Easy",
        "Concept",
        "User complaints often reveal genuine usability friction points that developers overlooked due to familiarity with the system.",
        "Why are early beta test complaints valuable for long-term product success?"
    ),
    (
        "How do you communicate complex technical trade-offs to product managers?",
        "Translate technical choices into business outcomes: cost, speed, reliability, and future flexibility. For example: 'Option A is faster to build (2 days) but will require downtime to upgrade later; Option B takes 4 days but scales seamlessly to 100k users.' Let them choose based on business goals.",
        "Intermediate",
        "Scenario",
        "Frame engineering trade-offs in terms of business impact: time-to-market vs long-term maintenance cost.",
        "Why do product managers prefer choices framed as trade-offs rather than pure technical jargon?"
    ),
    (
        "What do you do if you disagree with a company policy or internal engineering standard?",
        "1) Follow the current standard diligently to maintain team consistency. 2) Seek to understand the historical context behind the policy. 3) If valid data demonstrates that an alternative is better, propose a documented RFC (Request For Comments) with benchmarks for team evaluation.",
        "Intermediate",
        "Scenario",
        "Professional evolution of policies:\nComply -> Understand context -> Propose RFC with data -> Respect outcome.",
        "What is an RFC (Request For Comments) in software engineering organizations?"
    ),
    (
        "How do you balance writing fast code with writing clean, maintainable code?",
        "Donald Knuth: 'Premature optimization is the root of all evil.' First make it work correctly with clean, readable code. Second, measure and profile real bottlenecks with performance tools. Only optimize the specific hot paths that cause measurable latency.",
        "Intermediate",
        "Concept",
        "Order of priorities:\n1. Correctness\n2. Readability & Maintainability\n3. Measured Performance Optimization",
        "Why does writing overly optimized, unreadable code make maintenance expensive?"
    ),
    (
        "What would you do if your project manager asks you for a daily progress report that feels micromanaging?",
        "1) Recognize that micromanagement usually stems from anxiety or lack of visibility into progress. 2) Over-communicate proactively: provide a concise bullet-point summary at the end of each day before they ask. 3) Once trust and predictability are established, the need for oversight naturally fades.",
        "Intermediate",
        "Scenario",
        "Proactive over-communication builds trust and eliminates the anxiety that fuels micromanagement.",
        "Why does establishing predictable delivery rhythms ease managerial micromanagement?"
    ),
    (
        "How do you ensure you are continually improving your problem-solving speed?",
        "1) Consistently practice algorithmic challenges (LeetCode, HackerRank) focusing on patterns (sliding window, two pointers, BFS/DFS). 2) Time yourself during practice. 3) Analyze optimal solutions written by top programmers to learn concise idioms and elegant data structure choices.",
        "Easy",
        "Practical",
        "Improvement cycle:\nSolve problem -> Check time/space complexity -> Study top solution -> Re-implement optimally.",
        "Why is pattern recognition more effective than memorizing hundreds of individual solutions?"
    ),
    (
        "How do you handle working on an on-call rotation or handling server alerts?",
        "1) Familiarize yourself with the system runbooks and alert dashboards before your shift begins. 2) Keep the on-call phone or Slack channel notifications audible. 3) Follow runbook triage steps systematically. 4) Escalate to secondary leads if an incident exceeds escalation time thresholds.",
        "Intermediate",
        "Practical",
        "On-call discipline:\nRead runbooks -> Monitor alerts -> Follow triage protocols -> Document incident notes.",
        "What is an 'On-Call Runbook' and why is it essential for incident responders?"
    ),
    (
        "What does 'egoless programming' mean to you?",
        "It means you are not your code. When your code has bugs, it doesn't make you a bad person; when someone finds an improvement, it's not an attack. You treat code as an asset of the collective team, welcoming peer review, constructive scrutiny, and continuous refactoring.",
        "Easy",
        "Concept",
        "Tenets of egoless programming:\n- You are not your code\n- Welcome reviews and critiques\n- Share knowledge freely",
        "How does egoless programming lead to higher team psychological safety?"
    ),
    (
        "How do you handle being assigned a mundane bug while peers are building exciting new features?",
        "1) Approach every bug with dedication: bug fixes directly improve user satisfaction and prevent customer churn. 2) Use the opportunity to trace deep system internals and understand edge cases. 3) Delivering high quality on maintenance builds trust for future feature ownership.",
        "Easy",
        "Scenario",
        "Reliability on bug fixes is often how leadership identifies engineers ready for critical feature ownership.",
        "Why does deep debugging often teach more about system architecture than writing new greenfield code?"
    ),
    (
        "How do you handle a team member who interrupts others during meetings?",
        "1) Intervene politely on behalf of the interrupted speaker: 'Hang on, let's let John finish his point on database sharding first, then we can hear your thoughts.' 2) This protects psychological safety in meetings without causing aggressive conflict.",
        "Intermediate",
        "Scenario",
        "Gentle facilitation preserves meeting etiquette and ensures everyone's voice is heard.",
        "Why is meeting facilitation an important leadership trait for software engineers?"
    ),
    (
        "What is your strategy for writing effective pull request descriptions?",
        "Include: 1) What does this PR do? (Brief summary). 2) Why is it needed? (Link to Jira issue or bug ticket). 3) How to test? (Step-by-step instructions for the reviewer). 4) Screenshots or screen recordings showing UI changes. 5) Mention any breaking changes or required environment variables.",
        "Easy",
        "Practical",
        "PR Template:\n- Summary\n- Ticket link\n- How to test / Verification steps\n- Screenshots / GIF\n- Checklist (tests added, linter passed)",
        "Why does a thorough PR description speed up code review approval times?"
    ),
    (
        "How do you handle receiving a vague feature request from a stakeholder?",
        "Schedule a short discovery chat to define the user journey: 'Who is using this? What is their current pain point? What does success look like?' Sketch mock wireframes on a whiteboard or Figma to align visually before writing a single line of backend or frontend code.",
        "Intermediate",
        "Scenario",
        "Visual discovery and wireframing bring clarity to vague requests before code development begins.",
        "Why is wireframing faster than code for resolving design ambiguities with stakeholders?"
    ),
    (
        "What do you do when you feel overwhelmed by the sheer volume of technologies to learn in modern web development?",
        "Focus on fundamentals over hype: Master JavaScript closures, event loop, HTTP protocols, DOM, SQL queries, and async patterns. Frameworks come and go, but strong core fundamentals allow you to pick up any new library or tool in days rather than months.",
        "Easy",
        "Concept",
        "Foundational mastery creates immunity to tech stack churn.",
        "Why does a strong grasp of vanilla JavaScript make learning any new UI framework easy?"
    ),
    (
        "How do you handle a situation where a teammate asks you to review an enormous pull request (+2000 lines)?",
        "1) Politely ask if it can be broken down into smaller, logical pull requests (e.g. backend schema first, API routes second, UI components third). 2) Explain that small PRs (<300 lines) receive much more thorough reviews, find more bugs, and merge faster.",
        "Intermediate",
        "Practical",
        "Small PRs (<300 lines) find 80% more bugs per line of code than massive 2000-line changes.",
        "Why is reviewing a 2000-line PR usually reduced to a superficial 'LGTM' (Looks Good To Me)?"
    ),
    (
        "What is your approach to handling technical debt in a codebase?",
        "Follow the Boy Scout Rule: 'Always leave the campground cleaner than you found it.' When touching a file for a feature, clean up a small piece of technical debt (rename a vague variable, extract a messy helper, add a missing test). Over time, the codebase improves continuously without dedicated rewrite sprints.",
        "Easy",
        "Concept",
        "The Boy Scout Rule:\nContinuous micro-refactoring prevents technical debt bankruptcy.",
        "What is the danger of letting technical debt accumulate without regular repayments?"
    ),
    (
        "How do you handle personal accountability when you cause an inadvertent database lock or slow query?",
        "1) Acknowledge the issue immediately to team leads. 2) Kill the offending query to restore database responsiveness. 3) Analyze the query execution plan with EXPLAIN. 4) Add missing indexes or rewrite the query, and verify on staging before re-running.",
        "Intermediate",
        "Practical",
        "Steps: Immediate ownership -> Kill blocking process -> EXPLAIN plan analysis -> Index addition -> Safe verification.",
        "What is a database deadlock and how can transaction ordering cause it?"
    ),
    (
        "What would you do if you notice a teammate constantly working late nights and weekends?",
        "Check in with genuine empathy: 'Hey, I noticed your commits coming in at 2 AM. Are you feeling overloaded with sprint tickets? Let's see if we can re-balance the sprint backlog.' If it stems from unrealistic management pressure, encourage them to speak with the manager during 1-on-1s.",
        "Easy",
        "Scenario",
        "Peer solidarity helps prevent burnout in teammates who may feel pressured to prove themselves.",
        "Why is working 70-hour weeks counter-productive for software quality over a full quarter?"
    ),
    (
        "How do you handle communication when working across different global time zones?",
        "Practice asynchronous communication excellence: Write detailed, self-contained messages that don't require back-and-forth ping-pong. Include links, screenshots, reproduction steps, and clear decision alternatives so colleagues in other time zones can make progress while you sleep.",
        "Intermediate",
        "Concept",
        "Asynchronous rules:\n- Self-contained context\n- Explicit questions and deadlines\n- Detailed documentation over impromptu meetings",
        "What is the difference between synchronous and asynchronous communication in engineering?"
    ),
    (
        "What do you do if you are asked to implement a feature that you believe harms user privacy?",
        "1) Raise concerns professionally by pointing to privacy standards and company reputation. 2) Ask clarifying questions: 'Have we reviewed how this complies with GDPR and privacy expectations?' 3) Propose privacy-preserving alternatives (e.g. data anonymization or opt-in consent).",
        "Intermediate",
        "Scenario",
        "Advocate for ethical user privacy while providing compliant technical alternatives.",
        "Why does preserving customer trust matter more to a business than short-term tracking gains?"
    ),
    (
        "How do you handle receiving a vague 'it does not work' bug report from an internal user?",
        "1) Respond with kindness and patience. 2) Ask specific clarifying questions: 'Could you tell me what page you were on? What button did you click? Did you see any red error text? What browser were you using?' 3) Offer to do a 3-minute screen share to observe the bug directly.",
        "Easy",
        "Practical",
        "Patient clarification transforms vague frustration into reproducible technical steps.",
        "Why is screen sharing often the fastest way to understand a non-technical user's problem?"
    ),
    (
        "How do you stay calm when defending your design choices during an architecture review?",
        "1) Remember that questions are not personal attacks; reviewers are stress-testing the architecture against failure modes. 2) Ground your defense in objective metrics: latency, throughput, simplicity, and ease of testing. 3) Acknowledge trade-offs openly: 'That is a valid drawback; here is why we chose it over the alternative.'",
        "Intermediate",
        "Concept",
        "Architecture reviews evaluate trade-offs, not personal intellect.",
        "Why does an architect who admits trade-offs gain more trust than one who claims their design is perfect?"
    ),
    (
        "What is your approach to handling customer support tickets during an engineering rotation?",
        "1) Read the customer's issue with genuine empathy. 2) Verify and reproduce the bug in staging. 3) Write a clean patch with test cases. 4) Communicate back to the customer support team in clear, non-jargon language so they can update the customer.",
        "Easy",
        "Practical",
        "Support rotations give engineers firsthand empathy for real user frustrations and edge cases.",
        "Why should every software engineer spend time directly interacting with customer tickets?"
    ),
    (
        "What do you do if you suspect you made an incorrect technical choice early in a project?",
        "1) Avoid digging the hole deeper (Sunk Cost Fallacy). 2) Quantify the cost of pivoting now versus the cumulative pain of maintaining the flawed choice for the next two years. 3) Discuss openly with the lead, present a migration plan, and execute the pivot cleanly.",
        "Intermediate",
        "Scenario",
        "Pivoting early saves exponentially more time than defending a flawed architectural choice.",
        "How do you present a technical pivot to management without sounding reckless?"
    ),
    (
        "How do you celebrate other people's successes in your engineering team?",
        "Give credit publicly and specifically in team channels or retrospectives. Acknowledge the hard work and clever problem-solving of peers. A team that celebrates each other creates high trust, eliminates toxic competition, and achieves exceptional delivery.",
        "Easy",
        "Concept",
        "Public appreciation builds a culture of mutual support and psychological safety.",
        "Why is authentic peer recognition critical for remote team morale?"
    ),
    (
        "How do you handle a code review comment that says 'Refactor this entire function' without further explanation?",
        "1) Avoid feeling defensive. 2) Reply politely asking for specific guidance: 'Could you share what aspects of the function we can improve? Are you concerned about readability, performance, or edge case handling? Happy to adapt it.'",
        "Easy",
        "Practical",
        "Politely request specific rationale to turn vague feedback into actionable code improvements.",
        "Why should reviewers always explain the 'Why' behind refactoring requests?"
    ),
    (
        "What is your approach to maintaining personal physical health during intensive computer work?",
        "1) Maintain proper posture with an ergonomic chair and monitor at eye level. 2) Practice the 20-20-20 rule for eye strain: every 20 minutes, look at an object 20 feet away for 20 seconds. 3) Use keyboard wrist rests to prevent repetitive strain injury (RSI).",
        "Easy",
        "Concept",
        "Ergonomic health safeguards your career longevity as a software engineer.",
        "What is Repetitive Strain Injury (RSI) and how can developers prevent it?"
    ),
    (
        "How do you handle working with legacy technologies that are considered outdated in the industry?",
        "1) Maintain a professional mindset: legacy systems run multi-billion dollar businesses and solve real customer problems. 2) Learn how the legacy system functions thoroughly. 3) Seek opportunities to gradually modernize components using modern wrapper interfaces or microservices.",
        "Easy",
        "Concept",
        "Every legacy system was once cutting-edge; respecting past engineering decisions is a sign of engineering maturity.",
        "What is the 'Strangler Fig Pattern' for gradually migrating legacy software?"
    ),
    (
        "What do you do if you notice a teammate struggling with basic Git merge conflicts?",
        "1) Reach out with kindness: 'Git conflicts can be tricky when multiple branches touch the same file; let's jump on a 5-minute call and resolve it together.' 2) Walk them through using VS Code's three-way merge editor. 3) Empower them so they can do it independently next time.",
        "Easy",
        "Practical",
        "Empathetic pairing turns a stressful moment into a permanent learning milestone for a peer.",
        "Why is visual three-way merge tooling helpful for resolving complex conflicts?"
    ),
    (
        "How do you handle being placed on a project that you did not initially want to work on?",
        "1) Embrace it as an opportunity to broaden your skill set and domain knowledge. 2) Every project has interesting engineering challenges if you look deeply (data scale, performance, user experience). 3) Delivering outstanding results on tough assignments earns trust for future project choices.",
        "Easy",
        "Scenario",
        "Growth mindset: There are no boring projects, only uninterested engineers.",
        "How does diverse domain knowledge make you a more versatile full-stack engineer?"
    ),
    (
        "What is your approach to writing clean, helpful Git commit messages?",
        "Follow the Conventional Commits specification: Start with a clear verb prefix (feat:, fix:, docs:, refactor:, test:). Keep the summary line under 50 characters in the imperative mood ('add user auth middleware', not 'added' or 'adds'). Explain the 'Why' in the commit body if the change is subtle.",
        "Easy",
        "Practical",
        "Conventional commit format:\nfeat: add JWT authentication middleware\nfix: resolve race condition in cart total calculation\ntest: add integration test for password reset flow",
        "Why do clear commit messages save hours during git bisect and bug investigations?"
    ),
    (
        "How do you handle being the sole developer responsible for an entire module?",
        "1) Break the module into modular sub-components with clear interfaces. 2) Write comprehensive unit and integration tests so you can refactor with confidence. 3) Document architecture and API endpoints thoroughly in the README so teammates can understand and support it.",
        "Intermediate",
        "Practical",
        "Sole ownership requires disciplined automated testing and documentation to avoid single-point-of-failure risks.",
        "What is the 'Bus Factor' in software projects and how does documentation mitigate it?"
    ),
    (
        "How do you communicate with a senior engineer who seems too busy to answer your questions?",
        "1) Respect their time by doing your homework first. 2) Batch your questions into a single structured message rather than pinging every 10 minutes. 3) Provide clear options: 'I have 2 quick questions on the billing schema; would 10 minutes before lunch or after 4 PM work better for you?'",
        "Easy",
        "Scenario",
        "Batched, structured questions respect senior engineers' focus while getting you unblocked.",
        "Why is batching questions more respectful than sending 5 separate interruptions?"
    ),
    (
        "What does 'professionalism' mean to you in day-to-day software engineering?",
        "Professionalism means being dependable: showing up on time, meeting commitments or communicating delays early, writing tested clean code, treating all colleagues with dignity, and taking pride in building robust, trustworthy systems for users.",
        "Easy",
        "Concept",
        "Hallmarks of professionalism:\n- Dependability\n- Clear communication\n- High craft standards\n- Respectful collaboration",
        "How does personal dependability build a software engineer's reputation?"
    ),
    (
        "How do you handle learning from a senior who has a blunt or curt communication style?",
        "Separate the tone from the technical truth: Focus on the technical insight in their feedback, ignoring the brevity or bluntness. Often, experienced engineers are direct because they value efficiency, not because of malice. Respond with professionalism and gratitude for the technical insight.",
        "Intermediate",
        "Scenario",
        "Filter communication for technical signal, disregarding emotional noise.",
        "Why does focusing on technical substance help maintain productive working relationships?"
    ),
    (
        "How do you stay organized when juggling multiple open bug tickets in Jira?",
        "1) Keep ticket statuses updated in real-time (In Progress, In Review, QA). 2) Add clear internal comments on tickets detailing findings and reproduction steps. 3) Prioritize by severity (P0 blockers before P2 minor glitches).",
        "Easy",
        "Practical",
        "Disciplined ticket hygiene gives managers and team members immediate clarity on progress.",
        "Why is updating ticket status important for sprint metrics and burndown charts?"
    ),
    (
        "What do you do if you realize you made a false statement during an interview or technical discussion?",
        "Correct it immediately and gracefully: 'Actually, let me correct what I said earlier about MongoDB transactions; multi-document transactions were introduced in MongoDB 4.0, not 3.6. I wanted to ensure I gave the accurate technical fact.' Interviewers deeply respect intellectual honesty.",
        "Easy",
        "Scenario",
        "Graceful self-correction demonstrates confidence, integrity, and dedication to technical truth.",
        "Why is self-correction viewed positively rather than as a failure in interviews?"
    ),
    (
        "How do you handle a disagreement between two other teammates during a technical discussion?",
        "Help ground the debate in objective criteria: 'Both ideas have merit. Team member A's approach gives us faster delivery, while Team member B's approach provides better caching. Can we measure the latency difference or test a quick benchmark to make a data-driven choice?'",
        "Intermediate",
        "Scenario",
        "Neutral mediation transforms emotional disagreement into objective, data-driven technical evaluation.",
        "Why are benchmark measurements more effective at resolving debates than philosophical arguments?"
    ),
    (
        "What is your approach to handling continuous integration (CI) build failures?",
        "Treat a broken main branch build as a top priority: 1) Stop pushing new features until main is green. 2) Inspect the CI logs to identify which test or linter rule failed. 3) Either push an immediate fix or revert the breaking commit to unblock the entire team.",
        "Easy",
        "Practical",
        "Rule: A broken build blocks everyone; fix or revert immediately before continuing feature work.",
        "Why does leaving a CI build broken for days degrade team engineering discipline?"
    ),
    (
        "How do you handle feedback that your communication is too verbose or technical for executives?",
        "Adopt the Pyramid Principle: Start with the executive summary and bottom-line recommendation in the first two sentences. Provide high-level business impact, and keep detailed technical architectures and logs in an optional appendix for those who request it.",
        "Intermediate",
        "Concept",
        "The Pyramid Principle:\nExecutive recommendation first -> Key supporting arguments second -> Deep technical details in appendix.",
        "Why do executives prefer summary conclusions over detailed implementation walks?"
    ),
    (
        "What do you do when you are assigned a task that lacks sufficient technical documentation?",
        "Treat it as an opportunity to be the pioneer: 1) Explore the codebase and run experiments. 2) Ask targeted questions to senior peers. 3) Write down the complete setup and workflow documentation as you go, leaving a clear trail for the next engineer.",
        "Easy",
        "Scenario",
        "Pioneering documentation turns an initial obstacle into a lasting company asset.",
        "How does writing documentation while exploring help solidify your own understanding?"
    ),
    (
        "How do you handle imposter syndrome when joining a team of extremely experienced developers?",
        "1) Remember that the company hired you because they saw strong potential and solid fundamentals. 2) Treat seniors as mentors and learn from their experience. 3) Focus on being reliable on your assigned scope, asking smart questions, and steadily expanding your domain knowledge.",
        "Easy",
        "Concept",
        "Embrace being the learner: Everyone on the team was once a beginner facing their first codebase.",
        "Why do experienced teams value enthusiastic, humble learners over know-it-alls?"
    ),
    (
        "How do you maintain focus during long, monotonous data entry or repetitive testing tasks?",
        "1) Use the Pomodoro Technique: 25 minutes of intense focus followed by a 5-minute break. 2) Look for ways to automate the repetitive parts using scripts, macros, or automated testing tools. 3) Automating tedious tasks solves the monotony permanently while improving engineering tooling.",
        "Easy",
        "Practical",
        "Whenever faced with boring repetitive tasks, look for opportunities to automate them with code.",
        "How does automating manual testing tasks improve developer productivity?"
    ),
    (
        "What would you do if you see a teammate consistently working through lunch and looking exhausted?",
        "Invite them out for a quick 20-minute break: 'Hey, I'm grabbing lunch/coffee; come join me, let's step away from the monitors for a bit.' Sometimes people just need permission or an invitation to take a healthy break from high-stress work.",
        "Easy",
        "Scenario",
        "Thoughtful peer check-ins foster a caring, human team culture that prevents burnout.",
        "Why is stepping away from the computer beneficial for both mental health and debugging?"
    ),
    (
        "What is the single most important quality of a great software engineer in your opinion?",
        "Curiosity combined with humility: Curiosity drives you to understand how systems work under the hood and learn continuously; humility keeps you receptive to code reviews, ready to admit mistakes, and eager to collaborate effectively with others.",
        "Easy",
        "Concept",
        "Curiosity fuels continuous mastery; humility ensures great teamwork and egoless programming.",
        "Why is high intelligence without humility detrimental in collaborative engineering teams?"
    )
]

with open("scripts/hr_part3.py", "w", encoding="utf-8") as f:
    f.write("# scripts/hr_part3.py\n")
    f.write("hr_questions_part3 = [\n")
    for q in hr_part3:
        f.write(f"    {repr(q)},\n")
    f.write("]\n")

print(f"Total HR questions part 3: {len(hr_part3)}")
