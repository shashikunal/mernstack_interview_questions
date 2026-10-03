# 02 - React + Redux

## React - Top 25

1. **Virtual DOM + reconciliation?**
   In-memory diff, updates only changed real nodes via fiber. Keys help list diffing.
2. **Functional vs class? Why hooks?**
   Functional+hooks = less boilerplate, reuse logic via custom hooks, no `this` bugs.
3. **Rules of hooks?**
   Only top-level + only in React fns. Enforced by eslint. No cond/loops.
4. **useState batching?**
   Async batched. `setCount(c=>c+1)` functional form when based on prev. Initial fn `useState(()=>expensive())` runs once.
5. **useEffect vs useLayoutEffect?**
   useEffect=after paint (data fetch), useLayoutEffect=before paint blocking (measure DOM). Cleanup `return ()=>{}` cancels timers/subs.
6. **Missing dep warning fix?**
   Add dep or wrap in useCallback/useMemo. Empty `[]` = mount only. Never suppress blindly.
7. **useMemo vs useCallback vs memo?**
   useMemo=cached value, useCallback=cached fn, memo=cached component. Only for expensive or referential stability.
8. **useRef uses?**
   DOM ref + mutable box that doesn't re-render (timer id, prev value).
9. **Controlled vs uncontrolled?**
   Controlled=value+onChange (validation), uncontrolled=ref/defaultValue (simple/file). Prefer controlled for forms.
10. **Lifting state vs composition?**
    Lift to common parent, or children prop/slots to avoid prop drilling. Context for global.
11. **Prop drilling fix?**
    Composition, Context, state lib. Don't overuse Context for high-frequency.
12. **Keys why? Index as key problem?**
    Stable identity. Index breaks on reorder/insert -> wrong state. Use id.
13. **Re-renders: when + how to cut?**
    State/props/context change, parent re-renders child. Fix: memo, split components, colocate state, useReducer.
14. **useReducer when?**
    Complex transitions, multiple sub-values. `dispatch({type:'add'})` + pure reducer.
15. **Custom hook example?**
    `function useFetch(url){const[d,setD]=useState(null);useEffect(()=>{let c=false;fetch(url).then(r=>r.json()).then(j=>!c&&setD(j));return()=>c=true},[url]);return d}` + abort controller.
16. **Data fetching + race?**
    AbortController cleanup or ignore flag. Use React Query/SWR for cache/retry.
17. **Error boundaries?**
    Class `componentDidCatch` catches render errors. No hook version. For async/event need try/catch.
18. **Portals?**
    `createPortal(node,document.body)` for modal/tooltip outside hierarchy, keeps events.
19. **Suspense + lazy?**
    `const P=lazy(()=>import('./P')); <Suspense fallback>` code-splits.
20. **StrictMode double effects?**
    Dev double-invokes to surface missing cleanup. Fix cleanup, not remove StrictMode.
21. **Context perf pitfall?**
    Every consumer re-renders on value change. Split contexts or memo value `useMemo(()=>({a}),[a])`.
22. **Forms: how handle?**
    Controlled + validate onBlur/submit, or React Hook Form + zod for perf.
23. **Optimize list of 10k?**
    Virtualize (react-window), pagination, memo rows, stable keys.
24. **Hydration error in Next?**
    Server/client mismatch (Date.now, random). Render client-only via `useEffect` or `dynamic(ssr:false)`.
25. **Testing?**
    React Testing Library: test behavior not impl. `render, screen, fireEvent, waitFor`.

## Redux / Toolkit - Top 12
1. **Why Redux? Principles?**
   Single store, read-only state, pure reducers. Predictable for shared/global async state.
2. **Redux Toolkit flow?**
   `createSlice({name,initialState,reducers,extraReducers})` -> `configureStore` -> `Provider` -> `useSelector/useDispatch`.
3. **Immutability with RTK?**
   Write mutable, Immer makes immutable. `state.items.push(x)` ok inside slice.
4. **Async? createAsyncThunk?**
   `createAsyncThunk('u/fetch',async()=>await api())` + pending/fulfilled/rejected in extraReducers. Use `unwrap()` for errors.
5. **Selector perf?**
   `createSelector` memoized. Avoid inline `useSelector(s=>s.a.filter(...))` - memoize.
6. **Thunk vs Saga?**
   Thunk=simple promises, Saga=generator for complex flows (cancel/debounce). Start with thunk.
7. **Normalize state?**
   Store byId: `{ids:[],entities:{}}` via `createEntityAdapter` - avoids nested updates.
8. **RTK Query?**
   Built-in data fetching/caching: `createApi({baseQuery:fetchBaseQuery, endpoints})` - replaces manual thunk for CRUD.
9. **Middleware?**
   Intercepts dispatch (logger/thunk). Order matters.
10. **Redux vs Context vs Zustand?**
    Context=low-freq (theme/auth), Redux=complex shared + devtools + large team, Zustand=lightweight minimal boilerplate.
11. **Persist?**
    redux-persist + whitelist, rehydrate. Don't persist tokens insecurely.
12. **Debug?**
    Redux DevTools time-travel, action log.

## Code to Memorize
```js
// fetch with cleanup
useEffect(()=>{
  const c=new AbortController();
  fetch(url,{signal:c.signal}).then(r=>r.json()).then(setData).catch(e=>{if(e.name!=='AbortError')setErr(e)});
  return ()=>c.abort();
},[url]);
```
```js
// slice
const todosSlice=createSlice({name:'todos',initialState:{items:[],status:'idle'},
 reducers:{add:(s,a)=>{s.items.push(a.payload)}},
 extraReducers:b=>{b.addCase(fetchTodos.fulfilled,(s,a)=>{s.items=a.payload})}})
```

## Likely Tasks Tomorrow
- Todo + filter + localStorage persist
- Search with debounce + abort
- Counter with Redux Toolkit
