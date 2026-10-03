# 01 - Frontend: JavaScript / TypeScript / HTML / CSS

## JavaScript - Top 25 Q&A (with 1-line answers)

1. **var vs let vs const?**
   var=function-scoped+hoisted+reassignable, let/const=block-scoped, const=no reassignment. Prefer const.
2. **Closure? Example?**
   Function remembers outer scope. `function outer(){let c=0; return ()=>++c}` - used for private state, debounce, memoize.
3. **Event loop? Micro vs macro?**
   Call stack -> microtasks (Promise.then, queueMicrotask) drain first -> macrotask (setTimeout, setInterval). `Promise.resolve().then` beats `setTimeout 0`.
4. **Hoisting?**
   var/functions hoisted (undefined / full def), let/const in TDZ. Function declaration > var.
5. **`this`? Arrow vs regular?**
   Regular: caller-dependent. Arrow: lexical `this`. Use arrow for callbacks, regular for methods needing dynamic this.
6. **== vs ===?**
   `==` coerces, `===` strict. Always `===` except `x == null` to check null/undefined.
7. **Promises vs async/await?**
   Promise chain `.then/.catch`, async/await is syntax sugar. Always `try/catch`, use `Promise.all` for parallel, `allSettled` if partial fail ok.
8. **Promise.all vs allSettled vs race vs any?**
   all=fail-fast, allSettled=wait all, race=first settled, any=first fulfilled.
9. **Debounce vs throttle? Write debounce?**
   Debounce=wait idle, throttle=limit rate. Search box=debounce, scroll/resize=throttle.
   `const debounce=(fn,d)=>{let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>fn(...a),d)}}`
10. **Deep copy? structuredClone vs JSON?**
    `structuredClone(obj)` best. `JSON.parse(JSON.stringify())` loses Dates/functions/undefined. Shallow: `{...obj}`.
11. **Event delegation?**
    One listener on parent, use `e.target.closest()`. For dynamic lists, saves memory.
12. **call/apply/bind?**
    Invoke with explicit this. call=comma args, apply=array, bind=returns fn. Use for borrowing methods.
13. **Prototype + inheritance?**
    Objects link via `__proto__` to `prototype`. `class` is sugar over prototypes.
14. **Currying?**
    `const add=a=>b=>a+b`. For partial application, HOCs.
15. **Memoization?**
    Cache by args. `Map` + JSON key. React `useMemo` is same idea.
16. **Nullish ?? vs ||? Optional chaining?**
    `??` only null/undefined, `||` any falsy. `?.` short-circuits null. `user?.profile?.name ?? 'Guest'`.
17. **Map vs Object? Set?**
    Map=any key+ordered+size, Object=string keys. Set=unique. Use Map for freq count.
18. **Garbage collection? Memory leak?**
    Mark-and-sweep. Leaks: forgotten timers, detached DOM, global vars, unremoved listeners. Cleanup in useEffect return.
19. **CORS?**
    Browser blocks cross-origin without `Access-Control-Allow-Origin`. Fix server-side, not client. Preflight OPTIONS for non-simple.
20. **LocalStorage vs Session vs Cookie?**
    Local=5MB persistent, Session=tab-only, Cookie=sent per request (~4KB, use HttpOnly for token).
21. **XSS vs CSRF fix?**
    XSS=escape/sanitize + CSP + avoid dangerouslySetInnerHTML. CSRF=SameSite cookie + CSRF token.
22. **Rest vs Spread?**
    Rest collects `...args` in params, Spread expands `[...arr]`.
23. **Pure function? Side effect?**
    Same input same output, no mutation. Prefer for testability.
24. **Temporal Dead Zone?**
    let/const inaccessible before declaration -> ReferenceError.
25. **How JS handles async without blocking?**
    Single-thread + libuv/event loop offloads I/O, callbacks queued.

## TypeScript - Top 12

1. **interface vs type?** interface=extendable object shape, type=union/intersection/primitives. Use interface for objects, type for unions.
2. **any vs unknown vs never?** any=opt-out, unknown=must narrow, never=unreachable. Prefer unknown.
3. **Generics example?** `function first<T>(a:T[]):T{return a[0]}` - reusable typed.
4. **Utility types?** `Partial<T>`, `Pick<T,K>`, `Omit<T,K>`, `Record<K,V>`, `ReturnType`, `Awaited`.
5. **Enums vs union?** Prefer `type Status='idle'|'loading'` over enum for bundles.
6. **Narrowing?** `if(typeof x==='string')`, `in`, discriminated union with `kind` field.
7. **strict null checks?** Forces `?` and guards. Catches null bugs at compile.
8. **`as` + non-null `!` danger?** Bypasses check, avoid. Use guards.
9. **Decorators?** `@Injectable()` in Nest/Angular - metadata for DI.
10. **How to type Express req?** `Request<Params,ResBody,ReqBody,Query>` + extend with user: `interface AuthReq extends Request{user?:JwtPayload}`.
11. **Covariance gotcha?** Function param bivariance - use strictFunctionTypes.
12. **d.ts?** Declaration files for JS libs.

## HTML - Top 8
1. **Semantic tags?** header/nav/main/section/article/footer - SEO+a11y.
2. **DOCTYPE? Standards vs quirks?** `<!DOCTYPE html>` triggers standards.
3. **defer vs async?** defer=ordered after parse, async= ASAP unordered. Use defer for dependent scripts.
4. **Meta viewport?** `<meta name=viewport content="width=device-width,initial-scale=1">` for responsive.
5. **Form validation?** `required/pattern/type=email` + `novalidate` for custom JS.
6. **Accessibility?** label-for, alt, roles, aria-*, keyboard focus, contrast.
7. **SEO basics?** title/meta description, h1 once, semantic, og tags, sitemap.
8. **Shadow DOM?** Encapsulated DOM for web components.

## CSS - Top 12
1. **Box model?** content+padding+border+margin. `box-sizing:border-box` includes padding/border in width.
2. **Specificity order?** inline > id > class/attr/pseudo-class > element. `!important` last resort.
3. **Flex vs Grid?** Flex=1D (nav, centering), Grid=2D (layouts). Center: `display:flex;align-items:center;justify-content:center`.
4. **Position?** static/relative/absolute(fixed anchor)/fixed(viewport)/sticky(scroll hybrid).
5. **z-index + stacking?** Only on positioned + z-index/opacity/transform create context.
6. **Responsive units?** rem (root) over px, %/vw/vh, `clamp(1rem,2vw,2rem)`. Media: mobile-first `min-width`.
7. **Pseudo class vs element?** `:hover` state vs `::before` creates node. `::before{content:''}` needs content.
8. **BEM?** Block__Element--Modifier - avoids specificity wars.
9. **CSS variables?** `--primary:blue; color:var(--primary)` - theming.
10. **Reflow vs repaint?** Reflow=layout (width), repaint=pixels (color). Transform/opacity = compositor only, fastest.
11. **How to truncate?** `white-space:nowrap;overflow:hidden;text-overflow:ellipsis` + multiline with line-clamp.
12. **Dark mode?** `prefers-color-scheme` + CSS vars swap.

## 5-min Drills
- Write debounce + throttle from memory
- Explain `Promise.all` fail case fix
- Center div 3 ways (flex/grid/absolute)
