# JS Frontend - 200 Q&A

## JavaScript (1-100)

1. **What is closure in JavaScript?**
   Explanation: A closure is a function bundled with its outer lexical scope, so it remembers outer variables even after the outer function returns.
   Example: `const counter=(()=>{let n=0; return ()=>++n})(); counter(); // 1,2...`
   Use: Used in browser for private state, currying, memoization, and event handlers retaining config.
   Tip/Mistake: Don't create closures in loops with `var` without block scope — you'll capture the same variable; use `let` or IIFE.
2. **How does the event loop work?**
   Explanation: JS is single-threaded; the call stack runs sync code, then microtasks (promises) drain, then one macrotask (timer/I/O) runs, repeating.
   Example: `console.log(1); setTimeout(()=>console.log(2),0); Promise.resolve().then(()=>console.log(3)); // 1,3,2`
   Use: Explains why `fetch.then` runs before `setTimeout` and why long loops block UI rendering.
   Tip/Mistake: Don't block the loop with heavy sync work; chunk it or offload to Web Worker.
3. **What is a Promise and its states?**
   Explanation: A Promise represents a future value with states pending → fulfilled or rejected, settled once and immutable after.
   Example: `fetch('/api').then(r=>r.json()).catch(e=>console.error(e)).finally(()=>hideSpinner());`
   Use: Used for all browser async work — fetch, IndexedDB, dynamic imports — chaining dependent calls.
   Tip/Mistake: Forgetting to `return` inside `.then` breaks chaining; always return value or promise.
4. **What is async/await?**
   Explanation: `async` returns a promise, `await` pauses the function until the promise settles, letting async code read like sync code.
   Example: `async function load(){ try{ const r=await fetch('/api'); return await r.json(); }catch(e){ toast(e.message); } }`
   Use: Standard in projects for sequential API calls, form submits, and readable error handling with try/catch.
   Tip/Mistake: Don't `await` in a loop for independent calls — use `Promise.all`; and never forget try/catch or unhandled rejection.
5. **What is debounce?**
   Explanation: Debounce waits until calls pause for `wait` ms before running once, collapsing rapid events into one execution.
   Example: `const deb=(fn,ms)=>{let t; return (...a)=>{clearTimeout(t); t=setTimeout(()=>fn(...a),ms)}}; input.oninput=deb(search,300);`
   Use: Search-box API calls, window resize recalculation, and autosave in browser apps.
   Tip/Mistake: Don't debounce without cleanup in React — clear timeout on unmount or you'll setState on unmounted component.
6. **What is throttle?**
   Explanation: Throttle ensures a function runs at most once per interval, ignoring or queueing extra calls during the window.
   Example: `const thr=(fn,ms)=>{let last=0; return (...a)=>{const n=Date.now(); if(n-last>ms){last=n; fn(...a)}}}; window.onscroll=thr(save,200);`
   Use: Scroll handlers, mousemove parallax, and resize listeners where continuous feedback is needed but rate-limited.
   Tip/Mistake: Don't use debounce for scroll progress — you'll get no updates until stop; use throttle instead.
7. **What is prototypal inheritance?**
   Explanation: Objects inherit directly from other objects via an internal prototype link; property lookup delegates up the chain.
   Example: `const a={greet(){return 'hi'}}; const b=Object.create(a); b.greet(); // hi via prototype`
   Use: Powers `class`, array/object methods, and sharing behavior across components without copying.
   Tip/Mistake: Don't mutate `__proto__` per instance in hot code — it's slow; use `Object.create` or `class extends`.
8. **What is the prototype chain?**
   Explanation: When you read `obj.prop`, JS checks the object, then its prototype, recursively up to `Object.prototype` then null.
   Example: `arr.hasOwnProperty('length'); // found via Array.prototype → Object.prototype`
   Use: Explains why all arrays share `map` and why adding to `Array.prototype` affects every array in the page.
   Tip/Mistake: Don't add enumerable props to `Object.prototype` — it breaks `for...in` everywhere; use `Object.defineProperty`.
9. **How to handle CORS errors?**
   Explanation: Browsers block cross-origin reads unless the server returns `Access-Control-Allow-Origin`; preflight OPTIONS checks non-simple requests.
   Example: `// server (Express): app.use(cors({origin:'https://app.com', credentials:true})); // client: fetch(url,{credentials:'include'})`
   Use: Needed when frontend on Vercel calls API on Render with cookies or custom `Authorization` headers.
   Tip/Mistake: Don't try to fix CORS with `mode:'no-cors'` — it hides the response; fix server headers or use same-origin proxy.
10. **localStorage vs sessionStorage vs cookies?**
   Explanation: localStorage persists ~5MB per origin, sessionStorage is per-tab lifetime, cookies (~4KB) are sent with every HTTP request.
   Example: `localStorage.setItem('theme','dark'); sessionStorage.setItem('draft','x'); document.cookie='tok=abc; Secure; SameSite=Lax';`
   Use: localStorage for theme/cart, sessionStorage for tab wizard state, cookies for auth tokens read by server.
   Tip/Mistake: Don't store JWT/secrets in localStorage — XSS can steal it; use HttpOnly cookies for tokens.
11. **What is hoisting?**
   Explanation: Declarations are registered before execution: `function` fully hoisted, `var` hoisted as undefined, `let/const` hoisted but in TDZ.
   Example: `console.log(a); // undefined var a=1; console.log(b); // ReferenceError let b=2;`
   Use: Explains why you can call function declarations before definition but not arrow-function consts.
   Tip/Mistake: Don't rely on hoisting — declare with `let/const` at top and use function declarations consistently.
12. **var vs let vs const?**
   Explanation: `var` is function-scoped and re-declarable, `let` is block-scoped reassignable, `const` is block-scoped binding that can't be reassigned.
   Example: `for(let i=0;i<3;i++){setTimeout(()=>console.log(i))} // 0,1,2 but var gives 3,3,3`
   Use: Use `const` by default, `let` for counters, never `var` in modern browser code.
   Tip/Mistake: `const` doesn't freeze objects — `const o={}; o.x=1` works; use `Object.freeze` for immutability.
13. **== vs ===?**
   Explanation: `==` coerces types before comparing, `===` requires same type and value with no coercion.
   Example: `0=='0' // true, 0==='0' // false; null==undefined // true, null===undefined // false`
   Use: Always use `===` in code reviews; the only idiomatic `==` is `x==null` to check null/undefined together.
   Tip/Mistake: Don't use `==` with objects — it can call `valueOf`; lint with `eqeqeq` to enforce `===`.
14. **What is event bubbling vs capturing?**
   Explanation: Capturing travels window→target, target phase runs, then bubbling travels target→window; both traverse ancestors.
   Example: `parent.addEventListener('click',fn,true); // capture child.addEventListener('click',e=>e.stopPropagation()); // stop bubble`
   Use: Capture for early interception, bubble for delegation; modal overlay close uses bubble check on `e.target`.
   Tip/Mistake: Forgetting `stopPropagation` causes double handlers (button inside card both fire); check `e.currentTarget` vs `target`.
15. **What is event delegation?**
   Explanation: Attach one listener on a parent and branch on `event.target.closest()` instead of many listeners on children.
   Example: `ul.onclick=e=>{const li=e.target.closest('li'); if(li) toggle(li.dataset.id)};`
   Use: Todo lists, tables, dynamic search results where children are added/removed without rebinding.
   Tip/Mistake: Don't use `e.target` directly — clicks on inner icons miss; use `closest(selector)`.
16. **How does `this` work?**
   Explanation: `this` depends on call site: method call → object, plain call → undefined (strict) else window, arrow → lexical outer, `new` → instance.
   Example: `const o={n:1,f(){return this.n}}; o.f(); //1 const g=o.f; g(); // undefined const h=()=>this;`
   Use: Component methods, DOM handlers where `this` is the element for regular functions but not arrows.
   Tip/Mistake: Don't use arrow as object method expecting dynamic `this` — it inherits, so `this` will be wrong.
17. **call vs apply vs bind?**
   Explanation: All set `this` explicitly: `call` invokes now with comma args, `apply` invokes now with array args, `bind` returns a bound function.
   Example: `fn.call(user,'a','b'); fn.apply(user,['a','b']); const f2=fn.bind(user); f2('a');`
   Use: Borrowing methods (`[].slice.call(args)`), partial application, and fixing callbacks passed to event listeners.
   Tip/Mistake: Don't `bind` inside render loops — creates new function each render; bind once in constructor/module scope.
18. **Arrow function vs regular function?**
   Explanation: Arrows have lexical `this`, no `arguments`, no `prototype`, can't be `new`; regular functions have dynamic `this` and can construct.
   Example: `btn.onclick=()=>this.save(); // keeps outer this class A{ run(){setTimeout(function(){this.x},100)} } // this lost`
   Use: Arrows for array callbacks and promise chains; regular functions for object methods and constructors.
   Tip/Mistake: Don't use arrow for prototype methods needing `this` or `arguments` — use shorthand method syntax.
19. **What is currying?**
   Explanation: Currying converts `f(a,b)` into `f(a)(b)`, allowing partial application and specialized reusable functions.
   Example: `const add=a=>b=>a+b; const add5=add(5); add5(3); //8`
   Use: Configurable validators, loggers (`log(level)(msg)`), and HOC factories in frontend codebases.
   Tip/Mistake: Don't over-curry everything — it hurts readability; use it where partial reuse actually happens.
20. **What is memoization?**
   Explanation: Cache pure-function results keyed by arguments so repeated calls return instantly without recomputation.
   Example: `const memo=(fn)=>{const c=new Map(); return (...a)=>{const k=JSON.stringify(a); return c.has(k)?c.get(k):c.set(k,fn(...a)).get(k)}};`
   Use: Expensive filters, formatting, and derived selector calculations in data-heavy dashboards.
   Tip/Mistake: Don't memoize with unbounded keys on huge args — memory leak; add LRU limit or `useMemo` deps.
21. **Shallow vs deep copy?**
   Explanation: Shallow copies top level only (nested refs shared); deep copies clone nested objects recursively.
   Example: `const s={...o}; // shallow const d=structuredClone(o); // deep const j=JSON.parse(JSON.stringify(o)); // deep-lossy`
   Use: Shallow for React state spread updates; deep for duplicating form drafts with nested addresses.
   Tip/Mistake: JSON clone drops Dates/functions/undefined and throws on circular; prefer `structuredClone`.
22. **What is IIFE?**
   Explanation: An IIFE `(function(){...})()` defines and runs immediately, creating a private scope without polluting globals.
   Example: `(()=>{const secret='x'; window.api={get:()=>secret}})();`
   Use: Legacy script isolation before modules, one-off init, and avoiding var leakage in old browser bundles.
   Tip/Mistake: Don't need IIFE in modules — top-level scope is already private; use ES modules instead.
23. **What is strict mode?**
   Explanation: `'use strict'` enables stricter parsing: no implicit globals, `this` stays undefined, throws on silent errors and duplicates.
   Example: `'use strict'; x=1; // ReferenceError instead of global function f(a,a){} // SyntaxError`
   Use: Default in ES modules and classes; catches sloppy assignments in large frontend codebases.
   Tip/Mistake: Don't assume sloppy `this`-to-window inside modules — strict keeps it undefined and breaks old code.
24. **What is Temporal Dead Zone?**
   Explanation: TDZ is the span from block entry until `let/const` initialization where any access throws ReferenceError.
   Example: `{ console.log(x); // ReferenceError let x=2; }`
   Use: Explains why `typeof` guard still throws for let before declaration in browser console.
   Tip/Mistake: Don't reference state variables before declaration order in modules; declare/ import at top.
25. **What are higher-order functions?**
   Explanation: Functions that take or return functions, enabling abstraction like `map`, `withAuth`, or retry wrappers.
   Example: `const withLog=fn=>(...a)=>{console.log(a); return fn(...a)}; [1,2].map(withLog(x=>x*2));`
   Use: Array transforms, Express middleware, React HOCs, and logging wrappers.
   Tip/Mistake: Don't create new HOF inside render without memo — new fn identity triggers child re-renders.
26. **What is a pure function?**
   Explanation: Pure means same input → same output with no outside mutation, network, or random side effects.
   Example: `const sum=(a,b)=>a+b; // pure vs let t=0; const add=n=>t+=n; // impure`
   Use: Reducers, formatters, and selectors that must be testable and cacheable.
   Tip/Mistake: Don't hide Date.now()/Math.random() inside supposedly pure utils — inject them as args for testability.
27. **Explain map vs forEach vs reduce?**
   Explanation: `map` transforms to new array, `forEach` runs side effects returning undefined, `reduce` folds to any accumulator.
   Example: `const ids=users.map(u=>u.id); users.forEach(u=>save(u)); const total=cart.reduce((s,i)=>s+i.price,0);`
   Use: map for rendering lists, forEach for DOM side effects, reduce for totals/grouping.
   Tip/Mistake: Don't use `forEach` with async/await expecting sequence — it doesn't await; use `for...of`.
28. **What is destructuring?**
   Explanation: Destructuring unpacks arrays/objects into variables with defaults, rest, renaming, and nesting in one pattern.
   Example: `const {name:n='?', address:{city}={}, tags:[t,...rest]}=user;`
   Use: Props unpacking, API response handling, and clean function params `function Card({title})`.
   Tip/Mistake: Destructuring missing nested path throws — provide defaults `= {}` for optional objects.
29. **Spread vs rest?**
   Explanation: Spread expands an iterable into places, rest collects remaining items into an array; same `...` opposite direction.
   Example: `fn(...args); const arr=[...a,...b]; function sum(...nums){return nums.reduce((s,n)=>s+n,0)}`
   Use: Merging state, cloning arrays, forwarding props `{...props}`, variadic utils.
   Tip/Mistake: Spread is shallow — nested objects still shared; don't assume deep clone.
30. **What is optional chaining `?.`?**
   Explanation: `?.` short-circuits to undefined if left is null/undefined instead of throwing on property access or call.
   Example: `user?.address?.city ?? 'N/A'; api?.get?.(); arr?.[0];`
   Use: Safely rendering API data where nested fields may be missing before load.
   Tip/Mistake: Don't overuse to hide bugs — if object should exist, validate early instead of `?.` everywhere.
31. **What is nullish coalescing `??`?**
   Explanation: `??` returns right side only for null/undefined, preserving falsy 0/''/false unlike `||`.
   Example: `const page=input??1; // 0 stays 0 const name=userName||'anon'; // '' becomes anon`
   Use: Defaults for counts, pagination, and form values where 0/empty string are valid.
   Tip/Mistake: Don't mix `??` with `&&/||` without parens — syntax error; write `(a??b)||c` explicitly.
32. **Set vs Map vs Object?**
   Explanation: Set holds unique values, Map holds key→value with any key type and insertion order, Object only string/symbol keys with prototype.
   Example: `[...new Set([1,1,2])]; // [1,2] const m=new Map([[obj,v]]); m.get(obj);`
   Use: Set for dedupe/tags, Map for caches keyed by objects/DOM nodes, Object for JSON-shaped records.
   Tip/Mistake: Don't use plain `{}` as map with user keys — `__proto__` collision; use `Map` or `Object.create(null)`.
33. **What is WeakMap/WeakSet?**
   Explanation: Weak collections hold object keys weakly, allowing GC, are non-iterable and have no size.
   Example: `const cache=new WeakMap(); cache.set(domNode,{h:10}); // auto-freed when node removed`
   Use: Private metadata, DOM-to-data caches that must not prevent garbage collection.
   Tip/Mistake: Don't use primitives as keys or expect `.size`/iteration — it throws / is undefined.
34. **What are generators?**
   Explanation: `function*` can pause with `yield`, returning an iterator that resumes lazily one value at a time.
   Example: `function* ids(){let i=0; while(true) yield ++i} const g=ids(); g.next().value; //1`
   Use: Lazy sequences, paginated iterators, and custom `Symbol.iterator` implementations.
   Tip/Mistake: Don't forget `yield*` to delegate — plain `yield` of iterator nests it instead of flattening.
35. **What is Symbol?**
   Explanation: Symbol is a unique primitive ideal for non-colliding property keys; `Symbol.for` uses a shared global registry.
   Example: `const ID=Symbol('id'); obj[ID]=1; for(const k in obj){} // skipped, use Object.getOwnPropertySymbols`
   Use: Library metadata, `Symbol.iterator` custom iteration without name clashes.
   Tip/Mistake: Symbols are skipped by JSON and `for...in` — don't use them for data you need to serialize.
36. **What is BigInt?**
   Explanation: BigInt (`123n`) holds arbitrary-precision integers beyond `Number.MAX_SAFE_INTEGER` without precision loss.
   Example: `const big=9007199254740991n+1n; // exact Number(big)>9007199254740991 // true`
   Use: IDs, timestamps in nanoseconds, and financial cents where 64-bit ints matter.
   Tip/Mistake: Can't mix BigInt and Number (`1n+1` throws) — convert explicitly with `Number()`/`BigInt()`.
37. **Why is 0.1+0.2 !== 0.3?**
   Explanation: Decimals are binary floating-point approximations, so 0.1+0.2 yields 0.30000000000000004.
   Example: `(0.1+0.2).toFixed(1)==='0.3'; // true Math.abs(a-b)<Number.EPSILON // safe compare`
   Use: Cart totals and progress bars need rounding before display/comparison.
   Tip/Mistake: Don't use raw floats for money — store cents as integers or use decimal library.
38. **What is JSON and its limits?**
   Explanation: JSON is text format with `stringify/parse`; it drops functions/undefined/Symbol, stringifies Dates, throws on circular.
   Example: `JSON.stringify({a:1, f:()=>{}}); // '{"a":1}' JSON.stringify(o); // TypeError if circular`
   Use: API bodies and localStorage persistence of plain data.
   Tip/Mistake: Don't assume JSON round-trip preserves Date — revive with `new Date(s)` or use structuredClone.
39. **How does fetch work?**
   Explanation: `fetch` returns a promise of Response; it rejects only on network failure, not HTTP 4xx/5xx, so check `response.ok`.
   Example: `const r=await fetch('/api'); if(!r.ok) throw new Error(r.status); const data=await r.json();`
   Use: All browser GET/POST calls replacing XHR.
   Tip/Mistake: Forgetting `response.ok` check treats 404 as success; always guard before `.json()`.
40. **fetch vs axios?**
   Explanation: fetch is native but manual (no timeout, manual JSON/errors); axios adds interceptors, timeout, auto-JSON, and cancellation.
   Example: `axios.get('/api',{timeout:5000}); // auto throws on 4xx vs fetch needs manual`
   Use: fetch for simple same-origin calls; axios for token refresh interceptors and upload progress.
   Tip/Mistake: Don't assume axios is always smaller — it adds bundle weight; use fetch + tiny wrapper if size matters.
41. **How to cancel a fetch?**
   Explanation: Pass an `AbortController.signal` to fetch; calling `abort()` rejects with AbortError, usable for cleanup.
   Example: `const c=new AbortController(); fetch(url,{signal:c.signal}); c.abort(); // cancels`
   Use: Cancel stale searches on new keystroke and fetches on React `useEffect` cleanup.
   Tip/Mistake: Don't ignore AbortError — filter `if(e.name!=='AbortError') showError(e)` to avoid false error toasts.
42. **Callback hell and how to avoid?**
   Explanation: Nested callbacks for sequential async steps hurt readability and error handling; flatten with promises/async.
   Example: `// bad: a(()=>b(()=>c())) // good: await a(); await b(); await c();`
   Use: Refactor legacy geolocation/FS callbacks into promise helpers.
   Tip/Mistake: Don't mix callbacks and promises without wrapping — promisify once with `new Promise` or `util.promisify`.
43. **Promise.all vs allSettled vs race vs any?**
   Explanation: `all` fails fast on first reject, `allSettled` waits for all outcomes, `race` takes first settled, `any` takes first fulfilled.
   Example: `await Promise.all([p1,p2]); // both must succeed const s=await Promise.allSettled([p1,p2]);`
   Use: all for dependent parallel loads, allSettled for dashboards, race for timeouts, any for fastest mirror.
   Tip/Mistake: `Promise.all` with one reject discards others — use allSettled when partial results matter.
44. **What are microtasks vs macrotasks?**
   Explanation: Microtasks (promise.then, queueMicrotask, MutationObserver) drain before render; macrotasks (setTimeout, I/O) run one per loop turn.
   Example: `setTimeout(()=>console.log('macro'),0); queueMicrotask(()=>console.log('micro')); // micro first`
   Use: Explains render timing and why promise callbacks see updated DOM before timeout.
   Tip/Mistake: Starving the loop with recursive microtasks blocks painting — yield with setTimeout/rAF.
45. **What does setTimeout(fn,0) do?**
   Explanation: It queues `fn` as a macrotask after current stack and all microtasks, yielding to browser paint/handlers first.
   Example: `setTimeout(()=>heavyChunk(),0); // lets spinner paint first`
   Use: Break long loops, defer non-critical work until UI updates.
   Tip/Mistake: Don't assume 0ms exact — browsers clamp to ~4ms and throttle in background tabs.
46. **What is the DOM?**
   Explanation: The DOM is the live tree API for HTML; query with `querySelector`, update text with `textContent` to avoid parsing HTML.
   Example: `const el=document.querySelector('#list'); el.textContent='hi'; // safe vs innerHTML`
   Use: Vanilla widgets, portals, and direct focus/measurement outside React.
   Tip/Mistake: `innerHTML` with user data causes XSS — use `textContent` or DOMPurify.
47. **What is Virtual DOM?**
   Explanation: A JS object diff of UI; frameworks compare prev vs next tree and patch only changed real DOM nodes in batches.
   Example: `// React: setState → re-render VDOM → diff → update only <li> changed`
   Use: Efficient list/table re-renders without manual DOM diffing.
   Tip/Mistake: Virtual DOM isn't free — bad `key`s cause full re-mounts; use stable IDs not index.
48. **What is Shadow DOM?**
   Explanation: Encapsulated subtree attached via `attachShadow` that scopes styles and events away from main document.
   Example: `el.attachShadow({mode:'open'}).innerHTML='<style>p{color:red}</style><p>hi</p>';`
   Use: Web components and embeddable widgets that must not leak CSS.
   Tip/Mistake: `mode:'closed'` blocks outside access for testing — prefer open unless secrecy needed.
49. **What is XSS and prevention?**
   Explanation: XSS injects attacker scripts via unsanitized input; escape output, use `textContent`, set CSP, sanitize HTML.
   Example: `el.textContent=userInput; // safe DOMPurify.sanitize(dirtyHTML); // for rich text`
   Use: Comments, chat, and CMS previews rendering user HTML.
   Tip/Mistake: Never `innerHTML` template strings with user data or allow inline `onclick` — use sanitizer + CSP.
50. **What is CSRF and prevention?**
   Explanation: CSRF tricks a logged-in browser into sending forged state-changing requests using ambient cookies.
   Example: `// server: Set-Cookie: sess=..; SameSite=Lax + validate CSRF token header on POST`
   Use: Protect bank transfer / settings forms in cookie-auth MERN apps.
   Tip/Mistake: GET must never mutate — use POST with token + SameSite; check Origin header.

51. **How to store JWT securely?**
   Explanation: Store JWT in HttpOnly Secure SameSite cookies so JS cannot read it, with short access expiry plus rotating refresh token.
   Example: `res.cookie('tok',jwt,{httpOnly:true,secure:true,sameSite:'lax',maxAge:900000});`
   Use: MERN auth where browser auto-sends cookie and XSS cannot steal token via localStorage.
   Tip/Mistake: Don't put JWT in localStorage or URL — XSS/log leaks steal it; add CSRF token for cookie auth.
52. **What is Content Security Policy?**
   Explanation: CSP is an HTTP header allow-listing script/style sources to block inline scripts and XSS payloads.
   Example: `Content-Security-Policy: default-src 'self'; script-src 'self' https://cdn.com; object-src 'none'`
   Use: Production frontend to block injected scripts even if attacker sneaks HTML in.
   Tip/Mistake: Don't just add `unsafe-inline` to fix errors — it defeats CSP; move code to external files with nonces.
53. **What are ES Modules?**
   Explanation: ESM uses static `import/export` with strict mode, hoisted imports, live bindings, deferred execution, and tree-shaking.
   Example: `// utils.js export const sum=(a,b)=>a+b; // app.js import {sum} from './utils.js';`
   Use: Browser `<script type="module">`, Vite/webpack bundling with dead-code elimination.
   Tip/Mistake: Don't forget `.js` extension in browser ESM or mix default/named incorrectly — imports will fail silently.
54. **CommonJS vs ESM?**
   Explanation: CommonJS uses sync `require/module.exports` with runtime resolution; ESM uses async-static `import/export` analyzable at build time.
   Example: `const fs=require('fs'); module.exports={x}; // CJS vs import fs from 'fs'; export const x=1; // ESM`
   Use: CJS for legacy Node, ESM for browsers and modern Node with top-level await and tree-shaking.
   Tip/Mistake: Don't `require` ESM or use `__dirname` in ESM — use `import.meta.url` and async import().
55. **What is immutability and why?**
   Explanation: Immutability creates new objects instead of mutating, so reference equality detects changes reliably.
   Example: `setUser({...user, name:'Ann'}); // new ref vs user.name='Ann'; // same ref, React misses`
   Use: React/Redux state updates, time-travel debugging, and memoization.
   Tip/Mistake: Don't mutate state then spread — nested mutation already corrupted prev state; copy at each level.
56. **What is `new` keyword doing?**
   Explanation: `new` creates empty object linked to constructor prototype, binds `this`, runs constructor, returns object unless object returned.
   Example: `function U(n){this.n=n} U.prototype.hi=function(){return this.n}; const u=new U('A');`
   Use: Explains class instantiation and why forgetting `new` gives undefined `this`.
   Tip/Mistake: Arrow functions can't be `new` — TypeError; use regular function/class for constructors.
57. **Classes vs prototypes?**
   Explanation: `class` is syntax sugar over prototypes with constructor, extends, super, and methods on prototype, plus `#private` fields.
   Example: `class A extends B{ #x=1; constructor(){super();} get(){return this.#x}}`
   Use: React class legacy, models/services sharing methods without per-instance copies.
   Tip/Mistake: Class methods aren't bound — passing `obj.method` as callback loses `this`; bind or use arrow field.
58. **What are getters/setters?**
   Explanation: `get/set` intercept property reads/writes to compute or validate while keeping property syntax.
   Example: `const u={_n:'', get name(){return this._n}, set name(v){if(!v)throw new Error('req'); this._n=v}};`
   Use: Form models, computed fullName, and validation on assignment.
   Tip/Mistake: Don't do heavy async work in getters — they look sync and surprise callers; use methods.
59. **What is Proxy?**
   Explanation: Proxy wraps an object with traps like get/set/has to intercept operations for validation or reactivity.
   Example: `const p=new Proxy({n:1},{set(t,k,v){if(k==='n'&&v<0)throw new Error('neg'); t[k]=v; return true}});`
   Use: Vue 3 reactivity, validation layers, logging access in devtools.
   Tip/Mistake: Proxy adds overhead and breaks `===` identity assumptions — don't proxy hot paths blindly.
60. **What is Reflect?**
   Explanation: Reflect provides default object operations as functions, matching Proxy traps for clean forwarding.
   Example: `const p=new Proxy(t,{get(t,k,r){console.log(k); return Reflect.get(t,k,r)}});`
   Use: Inside proxy traps to preserve correct `this` and default behavior.
   Tip/Mistake: Don't reimplement defaults manually — use Reflect to avoid subtle `this`/prototype bugs.
61. **What are iterators/iterables?**
   Explanation: Iterable implements `Symbol.iterator` returning iterator with `next()->{value,done}` consumed by for...of/spread.
   Example: `const range={[Symbol.iterator](){let i=0; return {next:()=>({value:i++,done:i>3})}}}; [...range];`
   Use: Custom paginated collections and lazy data structures in UI code.
   Tip/Mistake: Don't return non-iterator from Symbol.iterator — for...of throws; always return object with next().
62. **for...of vs for...in?**
   Explanation: `for...of` iterates values of iterables (arrays, Map), `for...in` enumerates string keys including inherited.
   Example: `for(const v of [10,20]){} // values for(const k in {a:1}){} // 'a'`
   Use: for...of for lists/DOM NodeLists, for...in only for plain objects with hasOwn check.
   Tip/Mistake: Never use for...in on arrays — order not guaranteed and includes extras; use for...of or forEach.
63. **What is error handling best practice?**
   Explanation: Throw Error objects, catch at boundaries with try/catch, log with context, and listen to global handlers.
   Example: `try{await save()}catch(e){logger.error('save failed',{cause:e}); toast('Save failed')} window.onerror=(m,s)=>report(m);`
   Use: Form submits, fetch layers, and RUM error reporting in production.
   Tip/Mistake: Don't swallow errors with empty catch — at least log; silent fails are undebuggable.
64. **throw string vs Error?**
   Explanation: Throwing Error preserves stack, name, and cause chain; throwing strings loses debugging context.
   Example: `throw new Error('No user',{cause:{id}}); // good vs throw 'No user'; // bad, no stack`
   Use: All project throws should be Error subclasses for Sentry filtering.
   Tip/Mistake: Don't `throw err.response` raw — wrap in Error with message so stack isn't lost.
65. **What is memo/debounce in React context?**
   Explanation: Debounce delays calls until pause; `useMemo/useCallback` cache values/functions by deps to avoid recompute/re-render.
   Example: `const q=useMemo(()=>filter(list,term),[list,term]); const search=useMemo(()=>debounce(fetch,300),[fetch]);`
   Use: Search inputs firing APIs and expensive derived lists.
   Tip/Mistake: Wrong deps cause stale data — include all reactive values or use refs for latest callback.
66. **What is stale closure?**
   Explanation: A callback captures old state/props because closure froze values at creation time, not latest render.
   Example: `useEffect(()=>{const id=setInterval(()=>console.log(count),1000); return ()=>clearInterval(id)},[]); // count stuck`
   Use: Explains why timers/handlers in React show outdated state.
   Tip/Mistake: Fix with functional `setCount(c=>c+1)`, refs, or correct dep array — don't just disable exhaustive-deps.
67. **What are Web Workers?**
   Explanation: Workers run JS in background threads with no DOM access, communicating via postMessage to keep UI responsive.
   Example: `const w=new Worker('calc.js'); w.postMessage(data); w.onmessage=e=>render(e.data);`
   Use: Image processing, CSV parsing, and heavy sorting without freezing browser.
   Tip/Mistake: Can't touch DOM inside worker — do compute there, render on main thread.
68. **What are Service Workers?**
   Explanation: Service workers are proxy scripts intercepting network for offline cache, push, and background sync over HTTPS.
   Example: `self.addEventListener('fetch',e=>{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)))})`
   Use: Offline-first PWA, precaching app shell, and instant repeat loads.
   Tip/Mistake: Aggressive cache-first without versioning serves stale app — version caches and clean on activate.
69. **What is WebSocket?**
   Explanation: WebSocket upgrades HTTP to persistent full-duplex TCP via ws/wss for low-latency bidirectional messages.
   Example: `const ws=new WebSocket('wss://api/chat'); ws.onmessage=e=>addMsg(e.data); ws.send('hi');`
   Use: Chat, live prices, collaborative editing where polling is too slow.
   Tip/Mistake: Don't assume connection stays — implement heartbeat + exponential reconnect.
70. **Polling vs SSE vs WebSocket?**
   Explanation: Polling repeats requests, SSE streams server→client text via EventSource with auto-reconnect, WebSocket is bidirectional.
   Example: `const es=new EventSource('/stream'); es.onmessage=e=>tick(e.data); // SSE`
   Use: Polling for simple status, SSE for feeds/notifications, WebSocket for chat/games.
   Tip/Mistake: Don't use WebSocket for one-way feeds — SSE is simpler and works over plain HTTP.
71. **What is IntersectionObserver?**
   Explanation: Async observer fires when element crosses viewport threshold without costly scroll listeners.
   Example: `const io=new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting&&load(e.target)),{rootMargin:'200px'}); io.observe(img);`
   Use: Lazy images, infinite scroll, and view analytics.
   Tip/Mistake: Don't forget `unobserve/disconnect` after load — leaks observers on long pages.
72. **What is MutationObserver?**
   Explanation: Watches DOM subtree changes (childList/attributes) asynchronously in batches.
   Example: `new MutationObserver(m=>console.log(m)).observe(root,{childList:true,subtree:true});`
   Use: Editors, third-party widget hooks, and auto-enhancing dynamically injected HTML.
   Tip/Mistake: Mutating DOM inside callback without guard causes infinite loop — disconnect or filter.
73. **What is ResizeObserver?**
   Explanation: Notifies when observed element's content box resizes, ideal for component-level responsiveness.
   Example: `new ResizeObserver(es=>chart.resize(es[0].contentRect.width)).observe(card);`
   Use: Responsive charts, text truncation, dashboards independent of window size.
   Tip/Mistake: Changing observed size inside callback loops — use requestAnimationFrame and guard.
74. **How to do deep equality?**
   Explanation: Recursively compare types, keys, and values handling Dates/Maps; libraries handle cycles and edge cases.
   Example: `_.isEqual(a,b); // true deep vs JSON.stringify(a)===JSON.stringify(b); // fragile`
   Use: Memo checks, test assertions, dirty-form detection.
   Tip/Mistake: JSON compare fails on key order/undefined/functions — use lodash isEqual or fast-deep-equal.
75. **How to clone with functions/dates?**
   Explanation: `structuredClone` clones Dates/Maps/Sets/typed arrays but not functions/DOM; lodash cloneDeep handles more.
   Example: `const c=structuredClone({d:new Date(), m:new Map()}); // types kept`
   Use: Duplicating calendar events and editor state with real types.
   Tip/Mistake: structuredClone throws on functions/DOM nodes — extract or use custom clone for those.
76. **What is Number() vs parseInt?**
   Explanation: `Number` converts entire string strictly or NaN, `parseInt` parses leading int with radix ignoring trailing junk.
   Example: `Number('12px'); // NaN parseInt('12px',10); // 12 Number(''); // 0`
   Use: Number for strict form validation, parseInt for extracting prefixes like '100px'.
   Tip/Mistake: Always pass radix to parseInt — `parseInt('08')` was octal in old browsers.
77. **What is NaN and isNaN vs Number.isNaN?**
   Explanation: NaN is the only value not equal to itself; global isNaN coerces, Number.isNaN checks without coercion.
   Example: `isNaN('hi'); // true (coerced) Number.isNaN('hi'); // false Number.isNaN(0/0); // true`
   Use: Validate numeric inputs after Number() conversion.
   Tip/Mistake: Check with `Number.isNaN(v)` not `v===NaN` — latter is always false; use `Number.isFinite` for full check.
78. **What is Object.freeze vs seal?**
   Explanation: `freeze` blocks add/update/delete, `seal` blocks add/delete but allows updating existing writable props; both shallow.
   Example: `const o=Object.freeze({a:1}); o.a=2; // silent/throw, stays 1`
   Use: Config constants and enum-like objects protected from mutation.
   Tip/Mistake: Nested objects still mutable — deep-freeze manually if needed.
79. **Object.create(null) why?**
   Explanation: Creates object with no prototype, so keys like `toString/__proto__` are safe data not inherited methods.
   Example: `const m=Object.create(null); m['__proto__']='x'; // safe data, no pollution`
   Use: Counters, caches keyed by user input where prototype pollution is risk.
   Tip/Mistake: No `hasOwnProperty/toString` available — use `Object.hasOwn(m,k)` or Map.
80. **What is optional catch binding?**
   Explanation: ES2019 allows `catch{}` without param when error value is unused, reducing lint noise.
   Example: `try{JSON.parse(s)}catch{fallback()}; // no (e) needed`
   Use: Fallback parsing/feature detection where reason doesn't matter.
   Tip/Mistake: Don't omit param when you need logging — include `(e)` and report it.
81. **What are template literals?**
   Explanation: Backticks allow `${expr}` interpolation, multiline, and tagged functions that receive strings + values for escaping.
   Example: "const s=`Hi ${name}`; const safe=sql`SELECT * WHERE id=${id}`; // tag can escape"
   Use: Dynamic URLs/messages and safe SQL/CSS builders via tags.
   Tip/Mistake: Nesting backticks without escaping breaks — use helper functions for complex templates.
82. **What is short-circuit evaluation?**
   Explanation: `&&` returns first falsy or last truthy, `||` returns first truthy; useful for guards and defaults.
   Example: `user && show(user); const name=input||'Guest'; {isAdmin && <Panel/>}`
   Use: Conditional rendering and defaulting in JSX.
   Tip/Mistake: `0||default` discards valid 0 — use `??` when 0/'' are valid.
83. **What is typeof null?**
   Explanation: `typeof null` returns 'object' due to legacy implementation bug kept for compatibility.
   Example: `typeof null==='object'; // true const isNull=v=>v===null; // correct`
   Use: Interview trivia and reminder to check null explicitly.
   Tip/Mistake: Don't use typeof to detect null/arrays — use `===null` and `Array.isArray`.
84. **How to check array?**
   Explanation: `Array.isArray` reliably detects arrays across frames/realms where instanceof fails.
   Example: `Array.isArray([]); // true Array.isArray(iframe.contentWindow.Array); // still true`
   Use: Validating API payloads before `.map` to avoid runtime crash.
   Tip/Mistake: `typeof []` is object — always guard API lists with Array.isArray.
85. **How to flatten array?**
   Explanation: `flat(depth)` flattens nested arrays, `flatMap` maps then flattens one level efficiently.
   Example: `[1,[2,[3]]].flat(2); // [1,2,3] tags.flatMap(t=>t.split(','));`
   Use: Normalizing nested categories and tag lists for rendering.
   Tip/Mistake: `flat(Infinity)` on huge/deep data can blow stack/memory — limit depth.
86. **How to remove duplicates?**
   Explanation: Set dedupes primitives by SameValueZero; for objects dedupe by key using Map.
   Example: `[...new Set([1,1,2])]; // [1,2] [...new Map(users.map(u=>[u.id,u])).values()]; // by id`
   Use: Tag inputs, filter facets, merging API pages.
   Tip/Mistake: Set won't dedupe objects — `{a}!=={a}`; dedupe by id string.
87. **How to group data?**
   Explanation: Bucket items by key with reduce or `Object.groupBy` (ES2024) for reports and sections.
   Example: `Object.groupBy(users,u=>u.role); // {admin:[...]} // fallback: arr.reduce((m,x)=>{(m[x.role]??=[]).push(x); return m},{})`
   Use: Grouping orders by status and messages by date in dashboards.
   Tip/Mistake: Keys become strings — grouping by object needs Map, not plain object.
88. **What is timing attack safe compare?**
   Explanation: Naïve string compare returns early, leaking length via timing; constant-time compare is backend concern.
   Example: `// Node: crypto.timingSafeEqual(Buffer.from(a),Buffer.from(b)); // frontend: don't compare secrets`
   Use: Mention in auth discussion — delegate token/signature checks to server.
   Tip/Mistake: Don't implement crypto checks in browser JS — observable timing + exposed code; call backend.
89. **How to handle large lists performantly?**
   Explanation: Render only visible window (virtualize), paginate, use stable keys, memo rows, avoid inline props.
   Example: `// react-window: <FixedSizeList height={500} itemCount={n} itemSize={35}>{Row}</FixedSizeList>`
   Use: 10k-row tables, chat histories, and autocomplete dropdowns.
   Tip/Mistake: Index as key with sorting causes state mix-up — use id keys and `React.memo`.
90. **What is critical rendering path?**
   Explanation: Steps HTML→CSSOM→render tree→layout→paint→composite; sync scripts/CSS block first paint.
   Example: `<link rel="preload" href="font.woff2" as="font" crossorigin> <script defer src="app.js">`
   Use: Optimize LCP by inlining critical CSS and deferring non-critical JS.
   Tip/Mistake: Large sync head scripts delay paint — defer/async and code-split.
91. **async vs defer scripts?**
   Explanation: Both download parallel; async executes immediately unordered, defer executes ordered after parsing before DOMContentLoaded.
   Example: `<script async src="ads.js"></script> <script defer src="app.js"></script>`
   Use: async for independent ads/analytics, defer for app needing DOM/order.
   Tip/Mistake: defer preserves order but multiple async don't — don't use async for dependent scripts.
92. **How to lazy load images?**
   Explanation: `loading="lazy"` defers offscreen images natively; add width/height to avoid CLS and IntersectionObserver fallback.
   Example: `<img src="a.jpg" loading="lazy" width="800" height="600" alt="...">`
   Use: Feeds, blogs, product grids for faster initial load.
   Tip/Mistake: Don't lazy-load LCP hero — it delays largest paint; eager-load hero with fetchpriority=high.
93. **What is requestAnimationFrame?**
   Explanation: rAF runs callback before next repaint (~60fps), paused in background, ideal for smooth visual updates.
   Example: `function tick(t){el.style.transform=`+"`translateX(${t/10}px)`"+`; requestAnimationFrame(tick)} requestAnimationFrame(tick);`
   Use: Animations, canvas games, scroll-linked effects.
   Tip/Mistake: Don't use setInterval for animation — jank/tearing; use rAF + transform/opacity only.
94. **What is requestIdleCallback?**
   Explanation: Schedules low-priority work during idle periods with timeout fallback, not blocking input/paint.
   Example: `requestIdleCallback(()=>sendAnalytics(),{timeout:2000}); // fallback: setTimeout if unsupported`
   Use: Analytics flush, prefetch, non-urgent indexing.
   Tip/Mistake: Not supported in Safari — always provide setTimeout fallback.
95. **How to measure frontend performance?**
   Explanation: Combine lab (Lighthouse) with field Web Vitals LCP/INP/CLS via PerformanceObserver and RUM.
   Example: `new PerformanceObserver(l=>l.getEntries().forEach(e=>report(e))).observe({type:'largest-contentful-paint',buffered:true});`
   Use: CI budgets and production monitoring dashboards.
   Tip/Mistake: Don't optimize only lab scores — field data on slow devices matters more.
96. **What is memory leak in JS?**
   Explanation: Leaks are retained refs preventing GC: forgotten listeners/timers, detached DOM held in vars, growing caches.
   Example: `useEffect(()=>{const h=()=>{}; window.addEventListener('resize',h); return ()=>window.removeEventListener('resize',h)},[]);`
   Use: SPA navigation where listeners/intervals accumulate.
   Tip/Mistake: Always cleanup in effect return and AbortController; snapshot heap in DevTools to find retainers.
97. **How to debug async code?**
   Explanation: Use DevTools async stacks, await breakpoints, console.trace, and Network tab for fetch/CORS inspection.
   Example: `console.trace('state'); // stack debugger; await promise; // breakpoint across await`
   Use: Tracking unhandled rejections and race conditions.
   Tip/Mistake: console.log of promises shows pending — await or `.then(console.log)` to see value.
98. **What is JSONP and why obsolete?**
   Explanation: JSONP loaded cross-origin data via `<script>` callback before CORS, but allows arbitrary code execution.
   Example: `<script src="https://api?callback=handle"></script> // server returns handle({...})`
   Use: Historical only — understand legacy integrations.
   Tip/Mistake: Never use JSONP now — use CORS/fetch; JSONP is XSS by design.
99. **What is same-origin policy?**
   Explanation: SOP blocks cross-origin DOM reads and fetch responses by scheme/host/port unless CORS/postMessage allows.
   Example: `iframe.contentDocument // blocked cross-origin window.postMessage({x},'https://other.com'); // allowed channel`
   Use: Explains iframe access errors and fetch CORS failures.
   Tip/Mistake: Don't disable web security flags to bypass — configure server CORS or same-origin proxy.
100. **Cookies attributes for MERN auth?**
   Explanation: Use HttpOnly Secure SameSite=Lax/Strict short-lived access + httpOnly refresh, Path=/, proxied API to avoid CORS.
   Example: `res.cookie('rt','...',{httpOnly:true,secure:true,sameSite:'lax',path:'/api/auth',maxAge:7*864e5});`
   Use: Production MERN with frontend and API same-site via proxy.
   Tip/Mistake: SameSite=None requires Secure HTTPS — localhost without HTTPS will drop the cookie.

## TypeScript (101-140)

101. **Why use TypeScript in MERN?**
   Explanation: TS adds static types catching API mismatches early, with autocomplete and safe refactors across frontend/backend contracts.
   Example: `interface User{id:string;name:string} const get=async():Promise<User[]>=> (await fetch('/api/users')).json();`
   Use: Shared DTOs between React and Express preventing field-name drift.
   Tip/Mistake: Don't leave everything `any` — strict mode value is lost; type API boundaries first.
102. **interface vs type?**
   Explanation: `interface` declares extendable object shapes with merging; `type` aliases any shape including unions/primitives/mapped.
   Example: `interface A{id:string} interface B extends A{age:number} type ID=string|number;`
   Use: interface for props/models, type for unions, tuples, and utility compositions.
   Tip/Mistake: interface can't express unions — use type for `Status='a'|'b'` variants.
103. **What is any vs unknown vs never?**
   Explanation: `any` disables checks, `unknown` requires narrowing before use, `never` means impossible/no return.
   Example: `const u:unknown=JSON.parse(s); if(typeof u==='string') u.toUpperCase(); function fail():never{throw new Error()}`
   Use: unknown for parsed JSON, never for exhaustive switches and throwing helpers.
   Tip/Mistake: Avoid `any` in PRs — prefer unknown + guard to keep safety.
104. **What are generics?**
   Explanation: Generics parameterize types with `<T>` preserving exact input/output types across reusable functions/components.
   Example: `function first<T>(a:T[]):T|undefined{return a[0]} first<string>(['a']);`
   Use: Typed fetch wrappers, lists, and `useState<T>` in projects.
   Tip/Mistake: Don't use generic when concrete suffices — over-generic signatures hurt inference.
105. **What is Partial<T>?**
   Explanation: Partial makes all properties optional, ideal for patch/update payloads.
   Example: `function patch(id:string,p:Partial<User>){Object.assign(cache[id],p)} patch('1',{name:'Bo'});`
   Use: PATCH forms where only edited fields are sent.
   Tip/Mistake: Partial is shallow — nested objects still required; use deep-partial helper if needed.
106. **What is Required<T>?**
   Explanation: Required makes all properties required, opposite of Partial, ensuring complete configs.
   Example: `type Cfg={host?:string;port?:number}; const c:Required<Cfg>={host:'a',port:80};`
   Use: Final validated config after defaults merged.
   Tip/Mistake: Required on unions distributes oddly — apply per-member if needed.
107. **What is Pick<T,K>?**
   Explanation: Pick selects a subset of keys into a new type for DTOs and minimal props.
   Example: `type Card=Pick<User,'id'|'name'>; // {id,name} const c:Card={id:'1',name:'A'};`
   Use: Table rows and public API shapes exposing only safe fields.
   Tip/Mistake: Pick with misspelled key errors — use `keyof` autocomplete to avoid drift.
108. **What is Omit<T,K>?**
   Explanation: Omit removes keys, e.g. stripping password before sending user to client.
   Example: `type Safe=Omit<User,'password'|'hash'>; const s:Safe={id:'1',name:'A'};`
   Use: Sanitizing DB models into client responses.
   Tip/Mistake: Omit still exposes extra if base has index signature — explicitly pick safe fields for security.
109. **What is Record<K,V>?**
   Explanation: Record builds dictionary types mapping key union to value type with full checking.
   Example: `const counts:Record<string,number>={clicks:2}; counts['views']=5;`
   Use: Lookup tables, i18n dictionaries, and caches.
   Tip/Mistake: Plain Record allows any string — use literal union `Record<Role,number>` for closed keys.
110. **What is Exclude/Extract?**
   Explanation: Exclude removes members from a union, Extract keeps only matching members for filtering literals.
   Example: `type A=Exclude<'a'|'b'|'c','a'>; // 'b'|'c' type B=Extract<'a'|1,'a'>; // 'a'`
   Use: Deriving allowed event names or narrowing API status variants.
   Tip/Mistake: They work on unions only — wrapping non-union does nothing; check with hover.
111. **What is ReturnType/Parameters?**
   Explanation: They infer function return and args tuple, useful for wrappers/HOCs without duplicating signatures.
   Example: `function f(a:string,n:number){return {a,n}} type R=ReturnType<typeof f>; type P=Parameters<typeof f>;`
   Use: Typing higher-order helpers and mocked handlers.
   Tip/Mistake: Overloads infer only last signature — type each overload explicitly if needed.
112. **What is Awaited<T>?**
   Explanation: Awaited recursively unwraps Promise types to the resolved value for async typings.
   Example: `type U=Awaited<Promise<User>>; // User type R=Awaited<ReturnType<typeof fetchUser>>;`
   Use: Typing `use()` data and chained async helpers.
   Tip/Mistake: Don't double-wrap `Promise<Awaited<...>>` — unwrap once at boundary.
113. **What are enums vs union literals?**
   Explanation: Enums emit runtime objects, unions are compile-only strings; unions produce smaller bundles.
   Example: `type Dir='up'|'down'; // erased enum DirE{Up,Down} // emits JS object`
   Use: Prefer unions for API payloads and props; enums for legacy interop needing runtime mapping.
   Tip/Mistake: Numeric enums allow reverse mapping surprises — use string unions or `as const` objects.
114. **What is tuple?**
   Explanation: Tuple is fixed-length array with per-position types, e.g. coordinate pairs.
   Example: `const p:[string,number]=['x',1]; const e=Object.entries(o) as [string,unknown][];`
   Use: Entries, ranges, and useState-like pairs.
   Tip/Mistake: `push` can bypass length check — use `readonly [A,B]` or `as const` for strict tuples.
115. **What is type narrowing?**
   Explanation: Narrowing refines broad types via typeof/in/instanceof/truthiness so TS knows the exact branch.
   Example: `function f(v:string|number){if(typeof v==='string') return v.toUpperCase(); return v.toFixed(1)}`
   Use: Handling API unions and nullable DOM refs safely.
   Tip/Mistake: Truthiness narrows `''/0` away — check `!=null` when 0/'' are valid.
116. **What is discriminated union?**
   Explanation: Union sharing a literal `type`/`kind` field enabling exhaustive switch with compiler-checked branches.
   Example: `type S={t:'ok';v:number}|{t:'err';e:string}; switch(s.t){case 'ok':return s.v; case 'err':throw new Error(s.e)}`
   Use: API results, Redux actions, and form states.
   Tip/Mistake: Misspelled discriminant breaks narrowing — use literal type + `never` exhaustiveness check.
117. **What is type guard?**
   Explanation: Predicate `x is T` tells compiler a check narrows to T for custom validation.
   Example: `const isU=(v:unknown):v is User=>!!v&&(v as User).id!==undefined; if(isU(x)) x.name;`
   Use: Validating fetch data and filtering arrays `list.filter(isU)`.
   Tip/Mistake: Guard lying (wrong predicate) defeats safety — keep runtime check in sync with type.
118. **What is type assertion?**
   Explanation: `as` overrides compiler inference without runtime conversion; use after validation, not to silence errors.
   Example: `const el=document.getElementById('a') as HTMLInputElement; el.value; // after null check`
   Use: DOM elements and JSON after zod validation.
   Tip/Mistake: `as` doesn't convert — `123 as unknown as string` still number at runtime; validate/convert.
119. **What is non-null assertion `!`?**
   Explanation: `!` tells compiler a nullable is defined, but throws at runtime if actually null.
   Example: `const el=document.querySelector('input')!; // asserts exists el.focus();`
   Use: Sparingly for root elements known to exist.
   Tip/Mistake: Overuse hides null bugs — prefer `?.` + early throw `if(!el) throw`.
120. **What is `strict` in tsconfig?**
   Explanation: `strict` enables strictNullChecks, noImplicitAny, and strict function checks catching null/any bugs.
   Example: `{"compilerOptions":{"strict":true,"strictNullChecks":true}} // s:string|null needs check`
   Use: Mandatory for production MERN to catch API nulls at build.
   Tip/Mistake: Enabling suddenly surfaces hundreds of errors — migrate incrementally with `// @ts-expect-error`.
121. **What is noImplicitAny?**
   Explanation: Errors when TS can't infer a type, forcing explicit annotations on params and API data.
   Example: `function f(x){} // Error under noImplicitAny function f(x:string){} // ok`
   Use: Keeps Express handlers and utils typed instead of silent any.
   Tip/Mistake: Don't silence with `:any` — use `unknown` + narrow or proper interface.
122. **What are declaration (.d.ts) files?**
   Explanation: `.d.ts` files provide types for JS libs without bundling code, via `declare module`.
   Example: `declare module 'legacy-lib'{export function init(o:string):void} // + @types install`
   Use: Typing untyped npm packages in frontend builds.
   Tip/Mistake: Wrong declare signatures cause runtime mismatch — verify against docs/tests.
123. **What are mapped types?**
   Explanation: Mapped types transform each key via `[K in keyof T]` to build Partial/Readonly-style utilities.
   Example: `type RO<T>={readonly [K in keyof T]:T[K]}; type N={ [K in 'a'|'b']:number };`
   Use: Building form readonly states and API flag maps.
   Tip/Mistake: Forgetting modifiers `-?/+readonly` leads to optional surprises — be explicit.
124. **What are conditional types?**
   Explanation: Types branching on `T extends U ? X : Y` for inference-driven library typings.
   Example: `type IsStr<T>=T extends string?'yes':'no'; type A=IsStr<'hi'>; // 'yes'`
   Use: Utility libraries and prop inference.
   Tip/Mistake: Unions distribute — wrap in `[T]` to disable distribution when needed.
125. **What does `infer` do?**
   Explanation: `infer` extracts inner type inside conditional, e.g. unwrapping Promise element.
   Example: `type Un<T>=T extends Promise<infer U>?U:T; type X=Un<Promise<number>>; // number`
   Use: Unwrapping API generics and function returns.
   Tip/Mistake: `infer` only valid in conditional extends — place correctly or compiler errors.
126. **What are decorators?**
   Explanation: `@Dec` annotations add metadata to classes/members, used by Angular/Nest with experimental flag.
   Example: `@Component({selector:'a'}) class A{} // + "experimentalDecorators":true`
   Use: DI and routing in Nest/Angular backends paired with React frontend.
   Tip/Mistake: Decorator order/execution is subtle — keep them thin and test metadata.
127. **What is namespace vs module?**
   Explanation: `namespace` is legacy internal grouping; ES `import/export` modules are standard with file scope.
   Example: `namespace Old{export const x=1} // avoid vs export const x=1; import {x} from './m';`
   Use: Always use ESM in React; namespaces only for legacy `.d.ts`.
   Tip/Mistake: Mixing namespaces and modules confuses bundlers — migrate to ESM imports.
128. **How to type fetch response?**
   Explanation: Use generic wrapper returning `Promise<T>` plus runtime validation (zod) since `as T` is unchecked.
   Example: "async function get<T>(u:string):Promise<T>{const r=await fetch(u); if(!r.ok)throw new Error(); return await r.json() as T}"
   Use: All typed API layers in React Query/SWR services.
   Tip/Mistake: `as T` alone trusts server — validate with zod `schema.parse(await r.json())`.
129. **How to type React props/state?**
   Explanation: Define `interface Props`, type `useState<User|null>(null)` and events like `ChangeEvent<HTMLInputElement>`.
   Example: `interface P{title:string;onC:(id:string)=>void} function C({title}:P){const [n,setN]=useState('');}`
   Use: Every component/prop contract for autocomplete and safe refactors.
   Tip/Mistake: Overusing `React.FC` adds implicit children — prefer direct params `function C(p:P)`.
130. **How to type Express request in shared types?**
   Explanation: Share interfaces in common package and type `Request<Params,Res,Body,Query>` end-to-end.
   Example: `import {Request} from 'express'; interface B{name:string} (req:Request<{},{},B>)=>req.body.name; // typed`
   Use: Monorepo MERN where frontend and backend import same `UserDTO`.
   Tip/Mistake: Forgetting generic order causes mistyped body — check `<Params,ResBody,ReqBody,Query>`.
131. **What is covariance issue with arrays?**
   Explanation: TS arrays are unsoundly covariant, allowing assignment that can fail at runtime; readonly mitigates.
   Example: `const a:readonly string[]=['x']; // can't push wrong type let b:string[]=[...a];`
   Use: Function args accepting lists without risking mutation.
   Tip/Mistake: Don't mutate shared arrays — accept `readonly T[]` in utils.
132. **What is `readonly`?**
   Explanation: `readonly` prevents reassignment at compile time for props/arrays; `Readonly<T>` maps over object.
   Example: `interface U{readonly id:string} const u:Readonly<User>=...; // u.name='x' error`
   Use: Immutable Redux state and config objects.
   Tip/Mistake: Compile-only — runtime can still mutate; freeze if enforcement needed.
133. **What is `satisfies` operator?**
   Explanation: `satisfies` checks value against type without widening, preserving literals better than `as`.
   Example: `const c={mode:'dark'} satisfies {mode:string}; // keeps 'dark' literal c.mode; // 'dark'`
   Use: Config objects where literal inference matters for downstream unions.
   Tip/Mistake: `as` widens/erases — use satisfies for validation + narrow literals.
134. **What is `keyof`?**
   Explanation: `keyof T` is union of property names enabling type-safe dynamic access.
   Example: `function get<T,K extends keyof T>(o:T,k:K):T[K]{return o[k]} get(user,'name'); // typed`
   Use: Sort/filter builders and generic form handlers.
   Tip/Mistake: `keyof` includes methods — constrain with `K extends keyof T & string` if needed.
135. **What is intersection type?**
   Explanation: `A & B` requires all props of both, used for mixins and HOC prop merging.
   Example: `type Props=Base & {extra:string}; // must have both const p:Props={...base,extra:'x'};`
   Use: Combining auth props with component props.
   Tip/Mistake: Conflicting prop types become `never` — resolve overlaps explicitly with Omit.
136. **What are access modifiers?**
   Explanation: TS `public/private/protected` are compile-only, JS `#priv` is runtime-enforced truly private.
   Example: `class A{#s=1; get(){return this.#s}} // real privacy vs private x=1; // erased`
   Use: Encapsulating service internals in frontend classes.
   Tip/Mistake: TS private still accessible via bracket at runtime — use `#` for secrets.
137. **How to handle third-party untyped lib?**
   Explanation: Install `@types/pkg` or add `declare module` shim then wrap with typed helper for safety.
   Example: `declare module 'cool-lib'{export function f(s:string):number} import {f} from 'cool-lib';`
   Use: Legacy jQuery plugins in React migration.
   Tip/Mistake: Don't `any` the whole lib — type only used surface and add tests.
138. **What is tsconfig paths alias?**
   Explanation: `paths` maps `@/*` to `src/*` for clean imports; must mirror bundler alias.
   Example: `{"paths":{"@/*":["src/*"]}} // import {x} from '@/utils'; // + vite resolve.alias`
   Use: Large frontend to avoid `../../../` hell.
   Tip/Mistake: TS-only alias breaks runtime — sync vite/webpack/jest alias or imports fail.
139. **What is isolatedModules?**
   Explanation: Forces `import type` for types so single-file transpilers (esbuild/SWC) can safely drop types per file.
   Example: `import type {User} from './t'; // erased vs import {User} // error if only type`
   Use: Required with Vite/esbuild to avoid re-export type errors.
   Tip/Mistake: Re-exporting types without `export type` breaks isolatedModules builds.
140. **How to migrate JS to TS gradually?**
   Explanation: Enable `allowJs`, rename to `.ts` incrementally, type shared models/API layer first with strict off then on.
   Example: `{"allowJs":true,"checkJs":false} // rename utils.js→.ts, add User interface`
   Use: Brownfield MERN migration without big-bang rewrite.
   Tip/Mistake: Don't enable strict on day one — fix any-loose code module by module.

## HTML (141-170)

141. **What is semantic HTML?**
   Explanation: Semantic tags convey meaning (header/main/article) improving SEO, accessibility tree, and readability over div soup.
   Example: `<header><nav>..</nav></header><main><article><h1>Title</h1></article></main><footer>..</footer>`
   Use: Blog/CMS layouts where outline and landmarks drive SEO and screen readers.
   Tip/Mistake: Don't wrap everything in divs — use landmarks; only one `<main>` and one `<h1>` per page.
142. **Why use header/main/footer/nav?**
   Explanation: They define landmarks that screen readers jump to and search engines use for page structure.
   Example: `<nav aria-label="Primary"><a href="/">Home</a></nav><main id="content">..</main>`
   Use: App shells with skip-link `<a href="#content">Skip</a>` for keyboard users.
   Tip/Mistake: Multiple mains or navs without aria-label confuse AT — label each nav.
143. **article vs section vs div?**
   Explanation: article is standalone syndicatable content, section is themed group with heading, div is meaningless styling hook.
   Example: `<article><h2>Post</h2></article><section><h2>Comments</h2></section><div class="wrap">..</div>`
   Use: News cards (article), homepage blocks (section), layout wrappers (div).
   Tip/Mistake: section without heading is a div — add heading or use div.
144. **What is doctype?**
   Explanation: `<!DOCTYPE html>` triggers standards mode for consistent CSS layout; missing doctype triggers quirks mode.
   Example: `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"></head></html>`
   Use: Every page first line to avoid box-model differences.
   Tip/Mistake: Comments before doctype can trigger quirks in old IE — keep doctype line 1.
145. **Essential meta tags?**
   Explanation: charset, viewport, and description control encoding, responsive scaling, and search snippet.
   Example: `<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="..">`
   Use: All MERN public pages plus OG tags for share previews.
   Tip/Mistake: Missing viewport breaks mobile — text appears tiny and media queries misfire.
146. **How to make responsive HTML?**
   Explanation: Combine viewport meta, fluid containers, and responsive images; structure with semantic containers.
   Example: `<meta name="viewport" content="width=device-width,initial-scale=1"><img srcset="s.jpg 480w,l.jpg 800w" sizes="(max-width:600px) 480px,800px">`
   Use: Landing pages tested at 320px width.
   Tip/Mistake: Fixed-width divs + missing viewport cause horizontal scroll — use max-width:100%.
147. **Important form input types?**
   Explanation: Typed inputs (email/url/number/date/file) give native validation, keyboards, and pickers.
   Example: `<input type="email" required><input type="number" min="1" max="9"><input type="date">`
   Use: Signup/checkout forms reducing custom JS validation.
   Tip/Mistake: `type=number` still returns string — parse with `Number()` and don't rely solely on client validation.
148. **label vs placeholder?**
   Explanation: label is persistent accessible name linked via for/id; placeholder is hint that vanishes and isn't read reliably.
   Example: `<label for="e">Email</label><input id="e" placeholder="you@mail.com">`
   Use: All forms for a11y and password-manager autofill.
   Tip/Mistake: Placeholder-only forms fail a11y/UX — always include visible label.
149. **How does native form validation work?**
   Explanation: required/pattern/type trigger browser bubbles; style with :invalid and customize via setCustomValidity.
   Example: `<input required pattern="[0-9]{5}" id="z"><script>z.setCustomValidity('5 digits')</script>`
   Use: Quick checkout validation before custom React handling.
   Tip/Mistake: `novalidate` disables all native UI — only use when fully replacing with accessible custom errors.
150. **What is accessibility (a11y)?**
   Explanation: a11y ensures keyboard/screen-reader use via semantics, labels, focus, contrast, and ARIA only when native lacks.
   Example: `<button aria-expanded="false">Menu</button><img alt="Chart trend">`
   Use: Government/e-commerce apps requiring WCAG compliance.
   Tip/Mistake: `div onclick` without role/tabindex is inaccessible — use button.
151. **What are ARIA roles?**
   Explanation: ARIA describes custom widgets (dialog/slider) with roles/states when native elements can't be used.
   Example: `<div role="dialog" aria-modal="true" aria-label="Login"><button>Close</button></div>`
   Use: Custom dropdowns/modals where native dialog/select insufficient.
   Tip/Mistake: First rule of ARIA: use native `<button><dialog>` instead — ARIA doesn't add behavior/focus.
152. **How to optimize SEO HTML?**
   Explanation: One h1, logical headings, title/description, semantic tags, alt, canonical, and fast mobile HTML.
   Example: `<title>Shop – Shoes</title><link rel="canonical" href="https://x/p"><h1>Shoes</h1><img alt="Red shoe">`
   Use: Marketing/blog MERN pages needing indexing.
   Tip/Mistake: Multiple h1s and empty alt on informative images hurt ranking and a11y.
153. **script async vs defer vs normal?**
   Explanation: Normal blocks parsing, async runs ASAP unordered, defer runs ordered after parse before DOMContentLoaded.
   Example: `<script src="a.js" defer></script><script src="ads.js" async></script>`
   Use: defer for app bundle, async for analytics.
   Tip/Mistake: document.write in deferred scripts fails — avoid it entirely.
154. **link vs @import?**
   Explanation: `<link>` loads CSS in parallel, `@import` inside CSS is sequential and blocks rendering.
   Example: `<link rel="stylesheet" href="app.css"> <!-- good --> <!-- avoid: @import url('x.css') -->`
   Use: Head stylesheets for fast first paint.
   Tip/Mistake: @import chains delay paint — bundle with Vite instead.
155. **canvas vs svg?**
   Explanation: Canvas is raster pixel buffer via JS for games; SVG is vector DOM scalable with CSS/a11y.
   Example: `<svg viewBox="0 0 10 10"><circle cx="5" cy="5" r="4"/></svg> <canvas id="g" width="300"></canvas>`
   Use: Canvas for photo filters/games, SVG for icons/charts.
   Tip/Mistake: Canvas text isn't selectable/a11y — provide fallback description.
156. **How to embed video/audio?**
   Explanation: Use video/audio with multiple sources, controls, preload metadata, and track captions.
   Example: `<video controls preload="metadata"><source src="a.mp4" type="video/mp4"><track kind="captions" src="c.vtt" srclang="en"></video>`
   Use: Course/ethnography media with a11y captions.
   Tip/Mistake: Autoplay with sound is blocked — mute + playsinline if autoplay needed.
157. **What is iframe use and risk?**
   Explanation: iframe embeds external pages but risks clickjacking/XSS; sandbox and X-Frame-Options mitigate.
   Example: `<iframe src="https://pay.com" sandbox="allow-scripts allow-same-origin" title="Pay"></iframe>`
   Use: Payments, maps, and embeds isolated from parent.
   Tip/Mistake: Never sandbox without title or allow-top-navigation blindly — enables tabnabbing.
158. **What are data-* attributes?**
   Explanation: `data-*` stores custom per-element data readable via `dataset` without globals.
   Example: `<li data-id="42">..</li><script>li.dataset.id; // "42"</script>`
   Use: Passing IDs to delegated handlers and e2e selectors.
   Tip/Mistake: Don't store JSON with quotes unescaped — use `JSON.parse` carefully or state store.
159. **What are HTML entities?**
   Explanation: Entities like `&lt; &amp;` render reserved chars safely without parsing as markup.
   Example: `<p>&lt;div&gt; &amp;copy;</p> <!-- shows <div> -->`
   Use: Docs/blogs showing code snippets.
   Tip/Mistake: Double-escaping shows `&amp;lt;` literally — escape once on output.
160. **What is picture/srcset?**
   Explanation: srcset/sizes serve resolution variants, picture+source enables art direction by media/type.
   Example: `<picture><source media="(max-width:600px)" srcset="m.webp"><img src="d.jpg" alt=".."></picture>`
   Use: Hero images with mobile crop and WebP fallback.
   Tip/Mistake: Missing `sizes` makes browser assume 100vw — wasted bytes; always pair with srcset.
161. **How to improve HTML performance?**
   Explanation: Defer scripts, lazy media, preload fonts, minify, avoid deep nesting and forced reflows.
   Example: `<img loading="lazy"><link rel="preload" href="f.woff2" as="font" crossorigin>`
   Use: Content pages targeting LCP <2.5s.
   Tip/Mistake: Deeply nested tables/divs slow layout — flatten and batch DOM writes.
162. **What is dialog element?**
   Explanation: Native `<dialog>` modal with showModal() gives top-layer, focus trap, and Esc handling.
   Example: `<dialog id="d"><form method="dialog"><button>Close</button></form></dialog><script>d.showModal()</script>`
   Use: Confirm/login modals without libraries.
   Tip/Mistake: `show()` is non-modal — use showModal for true modal + `::backdrop` styling.
163. **How to make table accessible?**
   Explanation: Use caption, thead/th with scope, and associate headers for screen-reader navigation.
   Example: `<table><caption>Orders</caption><thead><tr><th scope="col">ID</th></tr></thead><tbody>..</tbody></table>`
   Use: Admin data grids.
   Tip/Mistake: Tables for layout break SR flow — use CSS grid; keep tables for data.
164. **What is details/summary?**
   Explanation: Native disclosure widget toggling without JS, keyboard accessible with marker styling.
   Example: `<details><summary>FAQ</summary><p>Answer</p></details>`
   Use: FAQs and filters without accordion libs.
   Tip/Mistake: Hiding marker without affordance confuses users — keep visual indicator.
165. **button vs div onclick?**
   Explanation: button provides keyboard, focus, disabled, and role free; div needs manual ARIA/handlers.
   Example: `<button type="button" onclick="save()">Save</button> <!-- handles Enter/Space -->`
   Use: All clickable actions in apps.
   Tip/Mistake: Missing `type="button"` inside form submits accidentally — always set type.
166. **What is autocomplete attribute?**
   Explanation: Hints like email/new-password guide autofill, password managers, and mobile keyboards.
   Example: `<input autocomplete="email"><input type="password" autocomplete="new-password">`
   Use: Checkout/auth forms for faster UX.
   Tip/Mistake: Wrong token (e.g. off on login) breaks managers — use standard tokens.
167. **How to handle file upload HTML?**
   Explanation: Use file input with accept/multiple plus multipart form and client size check before upload.
   Example: `<form enctype="multipart/form-data"><input type="file" accept="image/*" multiple></form>`
   Use: Avatar/bulk import flows.
   Tip/Mistake: Trusting accept alone — validate type/size on client and server.
168. **What is target=_blank risk?**
   Explanation: New tab keeps `opener` access enabling tabnabbing redirect; `rel=noopener noreferrer` severs it.
   Example: `<a href="https://x" target="_blank" rel="noopener noreferrer">Docs</a>`
   Use: External docs links.
   Tip/Mistake: Forgetting rel on user-generated links is exploitable — lint for it.
169. **What is lang attribute?**
   Explanation: `<html lang>` declares language for screen-reader pronunciation, spellcheck, and SEO.
   Example: `<html lang="en"><p lang="fr">Bonjour</p></html>`
   Use: Multilingual sites.
   Tip/Mistake: Wrong lang mispronounces content — set per-section for mixed language.
170. **What are web components basics?**
   Explanation: Custom elements + shadow DOM + template/slot create reusable encapsulated tags.
   Example: `customElements.define('my-card',class extends HTMLElement{connectedCallback(){this.attachShadow({mode:'open'}).innerHTML='<slot></slot>'}});`
   Use: Design-system widgets shared across frameworks.
   Tip/Mistake: Missing `super()` in constructor throws — call super first.

## CSS (171-200)

171. **What is Flexbox?**
   Explanation: 1D layout via `display:flex` aligning items on main/cross axes with justify/align and gap.
   Example: `.nav{display:flex;justify-content:space-between;align-items:center;gap:12px}`
   Use: Navbars, centering, and row/column toolbars.
   Tip/Mistake: Forgetting `flex-wrap` causes overflow — add wrap or `min-width:0` for shrinking children.
172. **What is CSS Grid?**
   Explanation: 2D grid with rows/columns/areas and auto-fit for responsive tracks.
   Example: `.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}`
   Use: Page layouts and card galleries.
   Tip/Mistake: Fixed `1fr 1fr 1fr` overflows mobile — use auto-fit/minmax.
173. **Flex vs Grid when to use?**
   Explanation: Flex aligns 1D sequences, Grid structures 2D areas; combine Grid shell with Flex interiors.
   Example: `.page{display:grid;grid-template-columns:240px 1fr} .card{display:flex;gap:8px}`
   Use: Dashboard shell (Grid) with toolbar rows (Flex).
   Tip/Mistake: Nesting Grid everywhere complicates — use Flex for simple centering.
174. **What is specificity?**
   Explanation: Priority ID > class/attr/pseudo-class > element; inline and !important override normal cascade.
   Example: `#id{color:red} /* 1-0-0 beats .c (0-1-0) and div (0-0-1) */`
   Use: Debugging why utility class loses to ID selector.
   Tip/Mistake: ID wars force !important — prefer classes + BEM to keep specificity low.
175. **How to calculate specificity?**
   Explanation: Count (inline,IDs,classes/attrs/pseudo-classes,elements); later rule wins on tie.
   Example: `nav ul li.active a:hover /* 0 IDs, 2 classes, 4 elements */`
   Use: Code-review selector weight.
   Tip/Mistake: `:where()` adds 0 but `:is()` takes max inner — don't confuse them.
176. **What is box model?**
   Explanation: Content + padding + border + margin; `border-box` includes padding/border in width.
   Example: `*{box-sizing:border-box} .box{width:200px;padding:20px;border:5px solid} /* stays 200px */`
   Use: Predictable card sizing.
   Tip/Mistake: Default content-box makes 100%+padding overflow — always set border-box globally.
177. **position static vs relative vs absolute vs fixed vs sticky?**
   Explanation: static flows, relative offsets self, absolute vs positioned ancestor, fixed vs viewport, sticky toggles on scroll.
   Example: `.wrap{position:relative} .tip{position:absolute;top:100%} .bar{position:sticky;top:0}`
   Use: Tooltips, sticky headers, and modals.
   Tip/Mistake: Absolute without positioned parent flies to body — set relative on wrapper.
178. **How does z-index work?**
   Explanation: z-index orders positioned elements; opacity/transform/filter create stacking contexts trapping children.
   Example: `.modal{position:fixed;z-index:50} .drop{position:absolute;z-index:10}`
   Use: Dropdowns over content, modals over all.
   Tip/Mistake: z-index on static does nothing — add position first.
179. **How to center a div?**
   Explanation: Flex or Grid centering handles both axes without hacks.
   Example: `.wrap{display:flex;justify-content:center;align-items:center;min-height:100vh} /* or display:grid;place-items:center */`
   Use: Hero, empty states, and login cards.
   Tip/Mistake: `margin:auto` alone needs flex/grid parent — use place-items for simplest.
180. **rem vs em vs px vs vw/vh?**
   Explanation: px fixed, rem scales with root for a11y, em scales with parent, vw/vh scale with viewport.
   Example: `html{font-size:16px} h1{font-size:2rem} .card{font-size:1em} .hero{height:100vh;width:100vw}`
   Use: rem for type/spacing, vw for fluid hero.
   Tip/Mistake: px-only text ignores user zoom prefs — use rem for fonts.
181. **What is cascade and inheritance?**
   Explanation: Cascade resolves competing rules by origin/specificity/order; inheritance passes color/font to children.
   Example: `body{color:#222;font-family:system-ui} a{color:inherit} /* inherits */`
   Use: Theming via body-level variables.
   Tip/Mistake: Not all props inherit (margin/border don't) — set explicitly or use `inherit`.
182. **display:none vs visibility:hidden vs opacity:0?**
   Explanation: none removes layout and AT, hidden keeps space but non-interactive, opacity keeps space and clicks.
   Example: `.a{display:none} .b{visibility:hidden} .c{opacity:0;pointer-events:none}`
   Use: Conditional panels vs layout-preserving placeholders vs fade transitions.
   Tip/Mistake: opacity:0 still focusable — add visibility/pointer-events for hidden interactive.
183. **What are pseudo-classes vs pseudo-elements?**
   Explanation: Classes style state (`:hover/:nth-child`), elements style parts (`::before/::placeholder`) with `content`.
   Example: `a:hover{color:red} .card::before{content:'';display:block;height:4px}`
   Use: Hover states and decorative badges without extra divs.
   Tip/Mistake: Single colon on elements works legacy but use `::` for elements.
184. **What are CSS transitions vs animations?**
   Explanation: Transitions animate on state change, @keyframes run multi-step loops with timing/iteration control.
   Example: `.btn{transition:transform .2s} .btn:hover{transform:scale(1.05)} @keyframes spin{to{transform:rotate(360deg)}}`
   Use: Hover fades vs loading spinners.
   Tip/Mistake: Animating width/height causes layout jank — animate transform/opacity.
185. **What is transform?**
   Explanation: GPU-friendly translate/rotate/scale without reflow, composited smoothly.
   Example: `.pop{transform:translateY(-4px) scale(1.02)}`
   Use: Drawer slides and hover lifts.
   Tip/Mistake: transform creates containing block for fixed children — fixed inside transformed ancestor sticks.
186. **What are CSS variables?**
   Explanation: Custom props `--x` with `var(--x,fallback)` cascade and change at runtime via JS.
   Example: `:root{--brand:#06f} .btn{background:var(--brand)} document.documentElement.style.setProperty('--brand','#000');`
   Use: Theming and dark mode toggles.
   Tip/Mistake: Variables are case-sensitive and inherit — scope per component to avoid leaks.
187. **How to do responsive design?**
   Explanation: Mobile-first fluid grids plus min-width queries and clamp() type at content breakpoints.
   Example: `@media(min-width:768px){.grid{grid-template-columns:1fr 1fr}} h1{font-size:clamp(1.5rem,4vw,3rem)}`
   Use: Marketing to dashboard adapting 320px→desktop.
   Tip/Mistake: Device-specific breakpoints break on new phones — break where layout breaks.
188. **What is mobile-first?**
   Explanation: Base styles target mobile, then min-width queries enhance upward for simpler cascade and faster mobile.
   Example: `.card{padding:12px} @media(min-width:800px){.card{padding:24px;display:grid}}`
   Use: Default for performance-focused builds.
   Tip/Mistake: Desktop-first max-width overrides pile up — prefer min-width progression.
189. **What is BEM?**
   Explanation: Block__Element--Modifier naming scopes styles and clarifies structure without high specificity.
   Example: `.card{ } .card__title{ } .card__title--large{font-size:2rem}`
   Use: Large codebases avoiding collisions.
   Tip/Mistake: Over-nesting `block__a__b` signals bad split — create new block.
190. **How does Tailwind help?**
   Explanation: Utility classes compose responsive consistent styles quickly with purgeable output.
   Example: `<div class="flex items-center gap-2 p-4 md:grid md:grid-cols-2">..</div>`
   Use: Rapid MERN UI with design tokens.
   Tip/Mistake: Long class strings hurt readability — extract `@apply` components for repeats.
191. **How to handle text overflow?**
   Explanation: Single-line ellipsis needs nowrap+hidden+ellipsis with constrained width; multiline uses line-clamp.
   Example: `.t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:200px} .m{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}`
   Use: Table cells and card titles.
   Tip/Mistake: No width constraint means no ellipsis — set max-width/block.
192. **How to make circle/image responsive?**
   Explanation: aspect-ratio keeps proportion, object-fit crops, max-width scales fluidly.
   Example: `.ava{aspect-ratio:1/1;border-radius:50%;object-fit:cover;width:100px} img{max-width:100%;height:auto}`
   Use: Avatars and product thumbs.
   Tip/Mistake: Fixed height distorts — use aspect-ratio + cover.
193. **What is object-fit?**
   Explanation: Controls how replaced content fills box: cover crops, contain fits, fill stretches.
   Example: `img{width:200px;height:120px;object-fit:cover;object-position:center}`
   Use: Uniform card images with varied sources.
   Tip/Mistake: object-fit needs explicit width/height — otherwise no box to fit.
194. **What is clamp()/min()/max()?**
   Explanation: Fluid functions bounding values without media queries, e.g. responsive type.
   Example: `h1{font-size:clamp(1.25rem,2vw + 1rem,2.5rem)} .w{width:min(100%,600px)}`
   Use: Fluid headings and containers.
   Tip/Mistake: Wrong unit mix breaks calc — keep compatible units inside.
195. **What is aspect-ratio?**
   Explanation: `aspect-ratio:16/9` maintains proportion for media/cards without padding hacks.
   Example: `.video{aspect-ratio:16/9;width:100%;background:#000}`
   Use: Embeds and skeletons preventing CLS.
   Tip/Mistake: Old browsers ignore it — provide min-height fallback if needed.
196. **How to do dark mode?**
   Explanation: Swap custom props via prefers-color-scheme or [data-theme] persisted in localStorage.
   Example: `:root{--bg:#fff} [data-theme="dark"]{--bg:#111} @media(prefers-color-scheme:dark){:root{--bg:#111}}`
   Use: App-wide theming toggle.
   Tip/Mistake: Flash of wrong theme — set theme script in head before paint.
197. **What is :is()/:where()/:has()?**
   Explanation: :is groups with max specificity, :where adds 0, :has styles parent by child.
   Example: `:is(h1,h2){margin:0} :where(ul){padding:0} .card:has(img){gap:12px}`
   Use: Simplifying selectors and conditional card styles.
   Tip/Mistake: :has performance cost on broad selectors — scope narrowly; check Safari support.
198. **How to optimize CSS performance?**
   Explanation: Minimize selectors, avoid @import, animate transform/opacity, purge unused, inline critical CSS.
   Example: `<style>/* critical above-fold */</style><link rel="preload" href="app.css" as="style">`
   Use: LCP-focused production builds.
   Tip/Mistake: `*` and deep descendants (`div div div`) slow matching — keep flat classes.
199. **What is container query?**
   Explanation: `@container` styles component by parent size, not viewport, for truly reusable cards.
   Example: `.wrap{container-type:inline-size} @container(min-width:400px){.card{display:grid}}`
   Use: Design-system cards used in sidebar and main.
   Tip/Mistake: Missing `container-type` means query never fires — set it on parent.
200. **How to prevent layout shift (CLS)?**
   Explanation: Reserve space with width/height/aspect-ratio, preload fonts with display:swap, avoid injecting above fold.
   Example: `<img width="800" height="600" style="aspect-ratio:4/3"> @font-face{font-display:swap}`
   Use: Stable feeds and hero loads with CLS <0.1.
   Tip/Mistake: Lazy injecting banners above content shifts layout — reserve slot or place below.

