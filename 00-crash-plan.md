# TOMORROW Interview - 1-Day Crash Plan (1 YOE Full-Stack MERN/.NET)

> For 1-year candidates: interviewers test fundamentals + hands-on project + debugging, NOT architecture. Say "I built/fixed" with 1 concrete example per topic. Skip deep Saga/microservices/AKS - just overview.

## How to use this pack
Folder has 7 files:
1. `01-frontend.md` - JS/TS, HTML, CSS
2. `02-react-redux.md` - React, Redux
3. `03-backend.md` - Node+Express OR .NET
4. `04-database.md` - MongoDB / Postgres
5. `05-bonus-next-nest-cloud.md` - Next.js, NestJS, Azure/GCP
6. `06-dsa.md` - DSA logic round
7. `07-git-hr-mock.md` - Git + HR + 2 mock rounds

## Today Schedule (6-8 hours)

**Block 1 [90 min]: JS + React (highest ROI)**
- JS: closures, event loop, `this`, promises, debounce/throttle, `==` vs `===`
- React: hooks rules, useEffect cleanup, virtual DOM, controlled vs uncontrolled, performance
- Do: explain aloud 20 questions from 01 + 02

**Block 2 [60 min]: Redux + Backend core**
- Redux Toolkit flow, thunk vs saga, normalize state
- Node event loop, middleware, JWT auth, error handling OR .NET middleware, DI, JWT
- Do: whiteboard auth flow + 1 CRUD API design

**Block 3 [60 min]: DB + DSA**
- Mongo indexing/aggregation vs Postgres joins/indexes/ACID
- DSA: Two Sum, Valid Parentheses, LRU concept, BFS/DFS, Big-O of array/object ops
- Do: code 5 problems on paper without autocomplete

**Block 4 [60 min]: Bonus + Git**
- Next.js SSR/SSG/ISR, NestJS modules/guards, Azure App Service vs GCP Cloud Run
- Git: rebase vs merge, resolve conflict, cherry-pick, stash
- Do: 07-git mock commands

**Block 5 [60 min]: 2 Full Mocks (30 min each)**
- Mock A in `07-git-hr-mock.md` - E-commerce product listing
- Mock B - Auth + rate-limit API design
- Record yourself, 2-min answers max

**Tonight [30 min]: Cheat Sheet**
- Memorize: event loop diagram, React render cycle, JWT flow, ACID vs BASE, Big-O table, `git status/log/diff` + STAR stories

## 10 Must-Know for Tomorrow (1 YOE level - explain + 1 project example each)
1. Explain event loop with `setTimeout(()=>{},0)` + promise example + where you used async/await
2. Closure counter + debounce implementation (search box you built)
3. `useEffect` cleanup + dependency bug you fixed (infinite loop/stale data)
4. Redux Toolkit: slice + store + `createAsyncThunk` - or Context you used, why?
5. Node middleware chain + global error handler OR .NET DI + middleware pipeline + 1 API you built
6. JWT login flow, where you stored token + logout handling
7. Mongo embed vs reference / Postgres JOIN + 1 schema you designed + index you added
8. Next.js server vs client components (basic) - only if in resume, else just SSR vs CSR line
9. Big-O + HashMap + solve Two Sum + Valid Parentheses blind (easy-medium only for 1 YOE)
10. Tell me about project - STAR with metrics: what broke, what you did, result (load time, bug count)

## Last-Minute Tips
- Think aloud in logic round, state brute force then optimize
- For code: clarify edge cases, state complexity
- For system: ask scope first, then DB choice, then API
- No blank answers: say "I'd approach it by..."
