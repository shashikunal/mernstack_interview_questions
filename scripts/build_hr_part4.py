# scripts/build_hr_part4.py

hr_part4 = [
    # Fresher Interview Scenarios & Behavioral Excellence
    (
        "What do you do if you realize mid-interview that you took the wrong algorithmic approach?",
        "Don't panic or freeze. Calmly acknowledge it to the interviewer: 'I realize my current greedy approach will fail on test cases with negative weights; let me step back and transition to a dynamic programming table approach.' Interviewers evaluate self-awareness, agility, and grace under pressure.",
        "Intermediate",
        "Scenario",
        "Composed pivot:\nRecognize flaw out loud -> Explain why it fails -> State new approach -> Proceed with confidence.",
        "Why do interviewers value a candidate who spots their own mistake more than someone who stubbornly defends a broken solution?"
    ),
    (
        "How do you prepare for behavioral (HR) rounds compared to technical coding rounds?",
        "Technical rounds test syntax, data structures, and architecture; behavioral rounds test character, collaboration, communication, and emotional resilience. Prepare 4-5 core STAR stories from college projects, hackathons, or internships that can be adapted to questions on conflict, leadership, failure, and deadlines.",
        "Easy",
        "Concept",
        "Prepare versatile STAR stories covering:\n- A project success under pressure\n- A technical failure and what you learned\n- A interpersonal disagreement resolved\n- A time you took initiative",
        "Why is it risky to walk into an HR round without prepared STAR stories?"
    ),
    (
        "What are the top 3 soft skills that differentiate an average developer from a great one?",
        "1) Clear communication: the ability to explain complex technical ideas simply and write clean documentation. 2) Empathy: understanding the user's frustration and teammates' workloads. 3) Adaptability: embracing new tools and shifting priorities with enthusiasm rather than complaint.",
        "Easy",
        "Concept",
        "Triad of excellence:\nClear communication + Empathy for users/peers + Adaptability to change.",
        "Why do engineering leaders emphasize soft skills as the primary catalyst for senior promotions?"
    ),
    (
        "How do you evaluate whether a company has a great engineering culture during your interview?",
        "Ask targeted questions: 1) 'How often do you deploy code to production?' (CI/CD maturity). 2) 'How do code reviews and testing work in the team?' (Quality standards). 3) 'What happens when a production bug slips through?' (Blameless culture vs finger-pointing). 4) 'What learning budgets or mentorship do freshers receive?'",
        "Easy",
        "Practical",
        "Green flags:\n- Continuous deployment\n- Mandatory peer code reviews\n- Blameless post-mortems\n- Structured fresher onboarding",
        "Why is a blameless post-mortem culture a sign of high engineering maturity?"
    ),
    (
        "How do you write a polite follow-up or thank-you note after an interview?",
        "Send an email within 24 hours: 1) Thank the interviewer for their time. 2) Mention a specific topic you enjoyed discussing (e.g. 'I really enjoyed our discussion on React concurrency and Redis caching'). 3) Reiterate your enthusiasm for the role and team mission.",
        "Easy",
        "Practical",
        "Template:\n'Dear [Name], Thank you for your time today. I really enjoyed learning about the team's upcoming migration to micro-frontends. Our conversation reinforced my excitement about the role. Best regards, [Your Name]'",
        "Why does a thoughtful thank-you email reinforce a positive final impression?"
    ),
    (
        "When is it acceptable to take on 'Technical Debt' in a project?",
        "Technical debt is like financial debt: acceptable when taken on intentionally for an urgent business milestone (such as a critical investor demo or market launch window) with a clear, scheduled plan to repay it in the following sprint. It is unacceptable when accrued through carelessness or lack of testing.",
        "Intermediate",
        "Concept",
        "Deliberate debt: Launch MVP on time, but file refactoring tickets immediately for the next sprint.",
        "What is the difference between deliberate technical debt and accidental sloppy code?"
    ),
    (
        "How do you handle working with a remote peer who rarely replies to messages?",
        "1) Avoid passive-aggressive pings. 2) Check if your messages are too long or vague; make questions clear with explicit yes/no or choice options. 3) Schedule a brief 10-minute sync at a mutually convenient time. 4) If project delivery is blocked, politely flag the dependency in the team standup.",
        "Intermediate",
        "Scenario",
        "Remedies:\nSimplify messages with explicit choices -> Schedule short face-to-face sync -> Flag blockers openly in standup.",
        "Why do clear binary choices (e.g. 'Should we do A or B?') get faster replies than open-ended essays?"
    ),
    (
        "What is your approach to pair programming with someone who prefers working alone?",
        "1) Start with empathy and respect their personal working style. 2) Propose the 'Driver-Navigator' pattern for just 30-45 minutes on a specific challenging module. 3) Focus on how pairing catches edge cases and shares domain context quickly. 4) Allow independent time for straightforward tasks.",
        "Easy",
        "Practical",
        "Driver-Navigator model:\nDriver writes the code; Navigator reviews, looks up documentation, and considers edge cases.",
        "How does pair programming accelerate knowledge transfer across a team?"
    ),
    (
        "What would you do if your manager asks for a delivery estimate on a technology you don't know?",
        "1) Do not provide an uninformed guess under pressure. 2) Request a short 'spike' (e.g. 1 day of research and prototyping) to evaluate the technology and understand setup hurdles. 3) Provide a grounded estimate based on findings from the spike.",
        "Intermediate",
        "Scenario",
        "Engineering Best Practice: Use a time-boxed 'Spike' to build a mini-prototype before committing to an estimate.",
        "What is a 'Spike' in Agile/Scrum methodology?"
    ),
    (
        "How do you give credit to open-source libraries when demonstrating your project?",
        "Be transparent and proud of using open-source: 'For authentication, we integrated Passport.js, and for chart visualizations, we leveraged Chart.js. This allowed our team to focus our engineering hours on building custom recommendation algorithms and smooth UI workflows.'",
        "Easy",
        "Concept",
        "Open-source acknowledgment shows industry savvy: leveraging existing tools to accelerate business value.",
        "Why is building everything from scratch often a sign of inexperience rather than skill?"
    ),
    (
        "What should you do if an interviewer asks an inappropriate personal question (e.g. marital status, religion)?",
        "Remain calm and redirect gracefully to professional qualifications: 'I prefer to keep my personal life separate from my work, but I can assure you I am 100% committed and excited to dedicate my full focus and energy to this engineering role.'",
        "Intermediate",
        "Scenario",
        "Polite deflection protects personal boundaries while keeping the focus on technical competence.",
        "Why are personal lifestyle questions legally prohibited in hiring in many jurisdictions?"
    ),
    (
        "How do you explain the difference between a Junior Engineer and a Senior Engineer?",
        "A junior engineer needs tasks broken down, asks for guidance, and focuses on implementing syntax correctly. A senior engineer identifies problems before they happen, designs systems for reliability and scale, balances business trade-offs, and elevates the entire team through mentorship.",
        "Easy",
        "Concept",
        "Junior focuses on 'How to build it right'; Senior focuses on 'What should we build and why'.",
        "How does a junior engineer begin transitioning towards mid-level and senior capabilities?"
    ),
    (
        "What do you do if you notice your team's test suite takes 45 minutes to run and slows everyone down?",
        "1) Profile the test suite to find the slowest tests. 2) Separate slow end-to-end (E2E) browser tests from fast unit tests. 3) Parallelize test execution across multiple runners in CI. 4) Mock heavy database I/O where unit tests don't require real database roundtrips.",
        "Intermediate",
        "Practical",
        "Test optimization:\nUnit tests (instant) -> Integration tests (parallelized) -> E2E tests (nightly or pre-release).",
        "What is the 'Test Pyramid' and why should fast unit tests outnumber slow UI tests?"
    ),
    (
        "How do you handle receiving a job offer with an exploding deadline (e.g. 48 hours to accept)?",
        "1) Express genuine gratitude for the offer. 2) Politely request an extension: 'Thank you so much for this offer! I am very excited about the role. To make this significant career decision thoughtfully, would it be possible to extend the decision deadline until next Tuesday?' Most companies grant reasonable extensions.",
        "Easy",
        "Scenario",
        "Polite extension request shows professional composure and allows you to evaluate your options calmly.",
        "Why do reputable companies usually grant reasonable offer deadline extensions?"
    ),
    (
        "What is your philosophy on working with Artificial Intelligence tools (like ChatGPT or GitHub Copilot)?",
        "View AI as an accelerator, not a crutch. Use it for boilerplate generation, regex drafting, explaining unfamiliar error messages, and brainstorming test cases. Always read, understand, and verify AI-generated code line-by-line; never commit code you cannot personally explain and debug.",
        "Easy",
        "Concept",
        "Golden rule of AI assistance:\nAccelerate boilerplate, but own every single line of logic and security in production.",
        "What are the risks of blindly pasting AI code into production without understanding it?"
    ),
    (
        "How do you ensure you stay humble as you gain experience and recognition?",
        "Remember that technology evolves rapidly; what you know today will change in three years. Respect the contributions of cross-functional partners (designers, QA, product managers, support teams) who make software successful. Focus on mentoring others as you grow.",
        "Easy",
        "Concept",
        "Humility keeps you open to learning from anyone and prevents the hubris that causes critical blind spots.",
        "How does arrogance in technical leaders lead to poor product decisions?"
    ),
    (
        "How do you handle an unexpected production bug reported 10 minutes before you are scheduled to leave for the day?",
        "1) Assess the severity immediately: If it is a P0 critical blocker (e.g. checkout broken, security leak), stay and help the on-call team triage and stabilize it. 2) If it is a minor non-blocking P2 bug, log reproduction details in a ticket and tackle it first thing the next morning.",
        "Easy",
        "Scenario",
        "Triage severity:\nCritical P0 = Step up to stabilize; Minor P2 = Document ticket and address first thing tomorrow.",
        "Why is severity triage essential for preventing unnecessary late-night panics?"
    ),
    (
        "What do you do if you disagree with the company's choice of technology stack?",
        "1) Focus on building deep mastery of the chosen stack; business goals and team familiarity often drive stack choices over personal developer preferences. 2) Appreciate that real-world companies value stability and developer hiring availability. 3) Learn the stack's unique strengths.",
        "Easy",
        "Concept",
        "Professional perspective:\nGreat engineers solve problems effectively in any language, whether it's Python, Go, Java, or Node.",
        "Why do enterprises often prefer mature, established stacks over trendy new frameworks?"
    ),
    (
        "How do you manage personal anxiety when giving your first technical presentation to the entire engineering team?",
        "1) Practice your slides and code walk 3 times beforehand. 2) Remember that your teammates want you to succeed. 3) Keep slides visual and concise. 4) If asked a question you don't know, say with confidence: 'That is a great question; I haven't tested that scenario yet, but I will check and share in the team channel.'",
        "Easy",
        "Practical",
        "Preparation tips:\nRehearse transitions + Audience is on your side + Confidently admit what you will look into.",
        "Why is 'I will find out and follow up' much better than making up a false answer?"
    ),
    (
        "What is your approach to handling customer data privacy when testing in local development?",
        "Never use real production customer data (passwords, emails, phone numbers, credit cards) in local dev environments. Use synthetic data generators (like Faker.js) or anonymized/obfuscated data dumps to ensure compliance with privacy laws.",
        "Easy",
        "Practical",
        "Data hygiene:\nUse Faker.js for development; keep production PII strictly confined to encrypted production environments.",
        "Why does using real user data on local laptops pose serious compliance and leak risks?"
    ),
    (
        "How do you approach a situation where you feel your contribution is being overlooked by leadership?",
        "1) Avoid passive-aggressive resentment. 2) Document your achievements and deliverables in a structured 'Wins / Brag Document'. 3) In your scheduled 1-on-1 with your manager, review your contributions objectively: 'Over the last quarter, I delivered features X, Y, and improved test coverage by 20%. I'd love to discuss how I can take on more visible responsibilities.'",
        "Intermediate",
        "Scenario",
        "Self-advocacy framework:\nDocument facts in a Brag Sheet -> Share in 1-on-1 -> Align on next-level goals.",
        "Why is maintaining a personal 'Brag Document' essential for performance reviews?"
    ),
    (
        "What would you do if a teammate frequently pushes code directly to the main branch, bypassing pull requests?",
        "1) Don't accuse them angrily. 2) Mention the risk politely: 'Hey, when code is pushed directly, our CI checks and peer reviews are skipped, which caused an unintended staging crash yesterday.' 3) Configure branch protection rules in GitHub (requiring 1 review and passing CI) to automate compliance for everyone.",
        "Intermediate",
        "Scenario",
        "Best practice: Enforce standards through automated GitHub branch protection rules rather than manual policing.",
        "What branch protection settings are standard for production repositories?"
    ),
    (
        "How do you approach learning a new programming language or framework over a weekend?",
        "1) Read the 'Quickstart' or tutorial in the official documentation. 2) Implement a non-trivial CRUD application (e.g. a Task Manager with authentication and database persistence). 3) Compare its paradigms (e.g. Go goroutines vs Node event loop) against what you already know.",
        "Easy",
        "Practical",
        "Hands-on learning:\nOfficial tutorial -> Build working CRUD project -> Compare idioms with existing knowledge.",
        "Why does building a real project teach faster than watching passive video lectures?"
    ),
    (
        "What do you do when you are in a meeting where everyone else is quiet and nobody volunteers an idea?",
        "Step up with a polite starter: 'If no one objects, I can share a preliminary thought to get our brainstorm started...' Offering an initial draft gives the team something concrete to react to and breaks the ice for collaborative discussion.",
        "Easy",
        "Scenario",
        "Courage to propose the first rough draft often unlocks creative discussion in quiet meetings.",
        "Why is proposing an imperfect initial idea better than prolonged silence?"
    ),
    (
        "How do you maintain enthusiasm for coding after a tiring day of work?",
        "Balance is essential: Recognize that you don't need to code 24/7 to be a great engineer. Recharge through physical exercise, reading, cooking, or spending time with family. Maintaining diverse interests outside coding prevents burnout and keeps your mind sharp.",
        "Easy",
        "Concept",
        "Recharging outside technology sustains a 30-year engineering career.",
        "Why is sustained intellectual recovery necessary for high cognitive performance?"
    ),
    (
        "What is your approach to participating in company hackathons or innovation days?",
        "1) Form a cross-functional team with a designer and product peer if possible. 2) Brainstorm a real pain point experienced by customers or internal developers. 3) Build a working, clickable MVP rather than slides. 4) Deliver an energetic, user-focused demo.",
        "Easy",
        "Practical",
        "Hackathon strategy:\nFocus on working MVP -> Show user impact -> Keep presentation energetic and concise.",
        "How do company hackathons help junior developers gain company-wide visibility?"
    ),
    (
        "How do you handle being given contradictory technical guidance by two senior mentors?",
        "1) Avoid playing them against each other. 2) Invite both to a brief 10-minute whiteboard session or Slack thread: 'Mentor A recommended pattern X for scalability, while Mentor B suggested pattern Y for fast iteration. Could we look at the trade-offs together for this module?' Let them collaborate on the final recommendation.",
        "Intermediate",
        "Scenario",
        "Bring mentors together transparently to harmonize architectural guidance.",
        "Why does transparent alignment eliminate confusion when working with multiple mentors?"
    ),
    (
        "What do you do if you notice an outdated instruction in the company's developer setup guide?",
        "Fix it immediately: clone the documentation repo, update the outdated command, test it on a clean machine or terminal, and submit a pull request: 'docs: update Node version requirement and seed command in README'. Teammates will thank you.",
        "Easy",
        "Practical",
        "The Boy Scout rule applies to documentation: Improve the setup guide as soon as you find an error.",
        "Why is updating developer documentation one of the easiest ways for a fresher to make an immediate impact?"
    ),
    (
        "How do you handle receiving an unexpected critical message from a customer in a public community channel?",
        "1) Remain polite, empathetic, and professional. 2) Do not argue or make defensive excuses publicly. 3) Acknowledge the issue: 'Thank you for flagging this; we want to get this resolved for you. Could you DM me your account ID so our team can investigate immediately?'",
        "Easy",
        "Scenario",
        "Public de-escalation: Empathy + Professional acknowledgment + Move to private channel for sensitive investigation.",
        "Why should customer troubleshooting involving account details always be handled in private DMs?"
    ),
    (
        "What is your philosophy on writing reusable code versus writing simple, one-off code?",
        "Follow the Rule of Three: Write it once. If you need it a second time, copy it. Only when you need it a third time should you abstract it into a reusable function or component. Premature abstraction often introduces unnecessary complexity before requirements are clear.",
        "Intermediate",
        "Concept",
        "The Rule of Three:\nDon't abstract prematurely; wait until three identical use cases clearly demonstrate the common pattern.",
        "Why is premature abstraction often worse than minor code duplication?"
    ),
    (
        "How do you prepare for your annual or semi-annual performance review?",
        "1) Gather data from your Brag Document: features shipped, bugs fixed, PRs reviewed, and metrics improved. 2) Review past feedback and demonstrate how you acted on it. 3) Articulate clear goals for the next cycle and express interest in expanding your responsibilities.",
        "Easy",
        "Practical",
        "Review preparation:\nObjective data + Addressed past feedback + Future growth goals.",
        "Why should performance reviews contain zero surprises if 1-on-1s have been regular?"
    ),
    (
        "How do you handle working with an API that has no documentation and an unresponsive author?",
        "1) Inspect the API endpoint using Postman or browser network inspector. 2) Test various HTTP methods (GET, POST, OPTIONS) and examine response headers and JSON schemas. 3) Write small automated integration tests asserting the behavior you discover, creating documentation through code.",
        "Intermediate",
        "Practical",
        "API reverse-engineering: Network inspection -> Postman probing -> Document through integration tests.",
        "How do integration tests serve as living documentation for poorly documented APIs?"
    ),
    (
        "What would you do if you notice a teammate feeling isolated in a remote work setting?",
        "Set up an informal 15-minute virtual coffee catch-up: 'Hey, wanted to check in and see how you are doing! No work talk, just catching up.' Feeling connected to teammates reduces isolation and creates strong psychological safety in remote teams.",
        "Easy",
        "Scenario",
        "Human connection in remote teams requires intentional, informal outreach.",
        "Why is deliberate informal social interaction vital for remote engineering teams?"
    ),
    (
        "How do you handle working under a manager whose technical background is in a different domain (e.g., hardware or marketing)?",
        "1) Appreciate their domain strengths (business strategy, user acquisition, stakeholder management). 2) Translate technical decisions into business impacts (revenue, latency, churn, risk). 3) Keep status updates focused on progress towards business objectives.",
        "Easy",
        "Concept",
        "Bridge the domain gap by speaking the language of business value rather than deep compiler internals.",
        "Why is translating technical outcomes into business metrics a valuable career skill?"
    ),
    (
        "What do you do if you suspect you are developing repetitive strain injury (RSI) or wrist pain?",
        "1) Take it seriously immediately; nerve injuries take months to heal if ignored. 2) Review your desk ergonomics (elbow angle at 90 degrees, neutral wrist position). 3) Switch to an ergonomic keyboard or vertical mouse. 4) Inform your manager to explore ergonomic equipment allowances.",
        "Easy",
        "Practical",
        "Proactive ergonomic intervention protects your physical health and long-term career productivity.",
        "Why do technology companies provide ergonomic assessments for software engineers?"
    ),
    (
        "How do you approach learning complex architectural patterns like Event-Driven Architecture or CQRS as a junior?",
        "1) Start with the fundamental problem they solve (e.g., decoupling services, scaling reads independently of writes). 2) Build a minimal proof-of-concept with Node.js and EventEmitter or RabbitMQ. 3) Read high-level architecture case studies from tech companies like Netflix and Uber.",
        "Intermediate",
        "Concept",
        "Learning advanced architecture:\nUnderstand the problem first -> Build mini prototype -> Study production case studies.",
        "Why should you understand the problem an architecture pattern solves before using it?"
    ),
    (
        "What would you do if a product manager asks you to deliver a feature by tomorrow that realistically takes 4 days?",
        "Be transparent, calm, and solution-oriented: 'Building the complete feature with error handling and tests will take 4 days. If we must demonstrate something tomorrow, I can deliver a working UI mock with static data for the demo, and ship the real backend integration by Thursday. Would that work?'",
        "Intermediate",
        "Scenario",
        "Offer a realistic compromise (UI demo now, production backend later) without making false promises.",
        "Why is committing to impossible deadlines a trap that damages developer credibility?"
    ),
    (
        "How do you handle being assigned to fix a production bug in code you know nothing about?",
        "1) Don't panic. 2) Reproduce the bug in your local environment using the exact steps in the ticket. 3) Place debugger breakpoints or logs to trace where the state turns invalid. 4) Write a failing unit test that reproduces the bug, then fix the code until the test passes.",
        "Intermediate",
        "Practical",
        "TDD debugging loop:\nReproduce -> Trace -> Write failing test -> Fix code -> Verify test passes.",
        "Why does writing a failing test before fixing a bug guarantee that you truly solved the issue?"
    ),
    (
        "What is your philosophy on asking questions during engineering all-hands or Q&A sessions?",
        "Prepare respectful, constructive, and forward-looking questions that benefit the wider team (e.g. engineering strategy, customer feedback, upcoming technical initiatives). Avoid using all-hands sessions for personal complaints or minor operational grievances.",
        "Easy",
        "Concept",
        "Company Q&A etiquette:\nForward-looking, strategic questions elevate team discussions and show business maturity.",
        "What makes a question constructive during an executive Q&A?"
    ),
    (
        "What advice would you give to a fresher starting their software engineering career tomorrow?",
        "1) Master the fundamentals of JavaScript, HTTP, and data structures. 2) Write tests for your code; reliability earns trust faster than speed. 3) Ask questions with clear context rather than suffering in silence. 4) Stay curious, stay humble, and enjoy building things that help people.",
        "Easy",
        "Concept",
        "Foundational mastery + Test reliability + Clear communication + Lifelong curiosity.",
        "Why is enjoying the process of problem-solving the greatest secret to a rewarding engineering career?"
    )
]

with open("scripts/hr_part4.py", "w", encoding="utf-8") as f:
    f.write("# scripts/hr_part4.py\n")
    f.write("hr_questions_part4 = [\n")
    for q in hr_part4:
        f.write(f"    {repr(q)},\n")
    f.write("]\n")

print(f"Total HR questions part 4: {len(hr_part4)}")
