# React + Redux - 200 Q&A

1. **What is React?**
Concept: React is a JavaScript library for building UIs using declarative components that re-render efficiently when state changes.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

2. **What is JSX?**
Concept: JSX is syntax extension that lets you write HTML-like code in JS, compiled to `React.createElement()` calls.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `React.createElement()` — e.g. `React.createElement()` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

3. **Functional vs class components?**
Concept: Functional components are functions using hooks for state/effects; class components use `this.state` and lifecycle methods and are now mostly legacy.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `this.state` — e.g. `this.state` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

4. **What are props?**
Concept: Props are read-only inputs passed from parent to child to configure rendering and behavior.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

5. **What is state?**
Concept: State is component-owned mutable data that triggers re-render when updated via setter.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `const [count, setCount] = useState(0); setCount(c => c + 1)` triggers a re-render.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

6. **Props vs state?**
Concept: Props are passed in and immutable by child, state is internal and mutable via `setState` to control interactivity.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `setState` — e.g. `setState` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

7. **What is prop drilling?**
Concept: Prop drilling is passing props through many intermediate components that don't use them just to reach a deep child.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

8. **How to avoid prop drilling?**
Concept: Use Context API, composition with `children`, Redux/Zustand, or component composition to pass data directly.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `children` — e.g. `children` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

9. **What is component composition?**
Concept: Composition builds UI by nesting components via `children` or slots instead of inheritance.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `children` — e.g. `children` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

10. **What is the `children` prop?**
Concept: `children` is a special prop containing nested JSX, used for wrappers like Layout, Card, or Modal.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `children` — e.g. `children` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

11. **How to do conditional rendering?**
Concept: Use `&&`, ternary `? :`, early return, or variable holding JSX based on state/props.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `&&` `? :` — e.g. `&&` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

12. **Why use `key` in lists?**
Concept: `key` gives each list item stable identity so React can diff, reorder, and preserve state correctly.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `key` — e.g. `key` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

13. **Controlled vs uncontrolled components?**
Concept: Controlled inputs are driven by React state via `value + onChange`; uncontrolled use DOM/ref with `defaultValue`.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `value + onChange` `defaultValue` — e.g. `value + onChange` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

14. **What is lifting state up?**
Concept: Lifting state up moves shared state to the closest common ancestor and passes it down via props.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `const [count, setCount] = useState(0); setCount(c => c + 1)` triggers a re-render.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

15. **What is `defaultProps` / default parameters?**
Concept: Defaults provide fallback prop values when parent omits them; modern code uses JS default parameters.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

16. **What is PropTypes?**
Concept: PropTypes runtime-checks prop types in development to catch wrong props; TypeScript largely replaces it.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

17. **What are Fragments?**
Concept: Fragments `<></>` group multiple elements without adding extra DOM nodes.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `<></>` — e.g. `<></>` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

18. **What is a Higher-Order Component (HOC)?**
Concept: An HOC is a function taking a component and returning an enhanced component, e.g. `withAuth(Component)`.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `withAuth(Component)` — e.g. `withAuth(Component)` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

19. **What is render props pattern?**
Concept: Render props shares logic by passing a function as prop/child that receives data and returns JSX.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

20. **Presentational vs container components?**
Concept: Presentational components render UI from props; container components handle state, fetching, and logic.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

21. **What is PureComponent / `React.memo`?**
Concept: They shallow-compare props to skip re-renders when props unchanged, optimizing performance.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `export default memo(Row)` + `useMemo/useCallback` for stable props to skip renders.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

22. **When to use `React.memo`?**
Concept: Use it for pure, often-rerendered child components with stable props to avoid wasted renders.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `export default memo(Row)` + `useMemo/useCallback` for stable props to skip renders.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

23. **Why must keys be stable, not index?**
Concept: Index keys break on insert/reorder causing wrong state reuse and input focus bugs; use unique ids.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `{users.map(u => <Row key={u._id} user={u}/>)}` — stable id, never index or random.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

24. **How to pass data parent to child?**
Concept: Pass via props like `<Child user={user} />` and read it in child.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `<Child user={user} />` — e.g. `<Child user={user} />` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

25. **How to pass data child to parent?**
Concept: Pass a callback prop like `onSelect` down, child calls it with data to lift up.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `onSelect` — e.g. `onSelect` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

26. **How to set default prop values in functions?**
Concept: Use destructuring defaults: `function Btn({type = 'button'})`.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `function Btn({type = 'button'})` — e.g. `function Btn({type = 'button'})` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

27. **What is props destructuring?**
Concept: It unpacks props directly in signature: `function User({name, age})` for cleaner code.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `function User({name, age})` — e.g. `function User({name, age})` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

28. **What is spread props `{...props}`?**
Concept: It forwards all props at once, useful for wrappers and HOCs.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

29. **Can you mutate state directly?**
Concept: No, mutate via setter to trigger render; direct mutation won't re-render and causes stale UI.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `const [count, setCount] = useState(0); setCount(c => c + 1)` triggers a re-render.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

30. **How to update object state correctly?**
Concept: Copy then update: `setUser(p => ({...p, age: 30}))` to keep immutability.
Why it matters: it controls how data flows and UI stays predictable, so bugs from shared mutable state are avoided.
Code example: `setUser(p => ({...p, age: 30}))` — e.g. `setUser(p => ({...p, age: 30}))` used directly in a component.
Project use: e.g. in a MERN dashboard, presentational cards receive props from container pages that own fetched state.
Mistake/tip: don't mutate props/state directly or use array index as key; keep data immutable and use unique ids.

31. **What are hooks?**
Concept: Hooks are functions like `useState`, `useEffect` that let functional components use state and lifecycle.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useState` `useEffect` — e.g. `useState` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

32. **What are Rules of Hooks?**
Concept: Call only at top level and only in React components/custom hooks, never in loops, conditions, or plain functions.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

33. **What does `useState` do?**
Concept: `useState` adds state to functional components: `const [count,setCount]=useState(0)`.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useState` `const [count,setCount]=useState(0)` — e.g. `useState` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

34. **What is lazy initial state?**
Concept: Pass a function `useState(()=>expensive())` so init runs once, not every render.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useState(()=>expensive())` — e.g. `useState(()=>expensive())` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

35. **What is functional update in `useState`?**
Concept: `setCount(c=>c+1)` uses latest state, safe for batching and rapid updates.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `setCount(c=>c+1)` — e.g. `setCount(c=>c+1)` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

36. **What is state batching?**
Concept: React groups multiple `setState` calls in one event/effect into a single re-render for performance.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `setState` — e.g. `setState` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

37. **What does `useEffect` do?**
Concept: `useEffect` runs side effects like fetching, subscriptions, timers after render.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useEffect` — e.g. `useEffect` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

38. **What is dependency array in `useEffect`?**
Concept: It lists values the effect depends on; effect re-runs only when they change.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useEffect(() => { fetchUsers(); return () => controller.abort(); }, [page])` with cleanup.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

39. **What does empty `[]` deps mean?**
Concept: Effect runs once after mount, like `componentDidMount` for init fetch/subscribe.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `componentDidMount` — e.g. `componentDidMount` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

40. **What happens with missing deps?**
Concept: Stale closures and missed updates; lint `exhaustive-deps` warns to include all used values.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `exhaustive-deps` — e.g. `exhaustive-deps` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

41. **What is effect cleanup?**
Concept: Return a function from `useEffect` to unsubscribe, clear timers, or abort fetch on unmount/re-run.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useEffect` — e.g. `useEffect` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

42. **`useEffect` vs `useLayoutEffect`?**
Concept: `useEffect` runs async after paint; `useLayoutEffect` runs sync before paint for DOM measurements.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useEffect` `useLayoutEffect` — e.g. `useEffect` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

43. **How to fetch data in `useEffect`?**
Concept: Call async function inside, track loading/error, and abort with `AbortController` in cleanup.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `AbortController` — e.g. `AbortController` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

44. **Why does effect run twice in StrictMode dev?**
Concept: StrictMode intentionally mounts-unmounts-remounts to surface cleanup bugs; production runs once.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useEffect(() => { fetchUsers(); return () => controller.abort(); }, [page])` with cleanup.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

45. **What does `useContext` do?**
Concept: `useContext(MyContext)` reads nearest Provider value and re-renders when it changes.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useContext(MyContext)` — e.g. `useContext(MyContext)` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

46. **`createContext` vs `useContext`?**
Concept: `createContext` creates the context object; `useContext` consumes its value in a component.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `createContext` `useContext` — e.g. `createContext` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

47. **What does `useRef` do?**
Concept: `useRef` holds a mutable `.current` box persisting across renders without causing re-renders.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useRef` `.current` — e.g. `useRef` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

48. **How to use `useRef` for DOM?**
Concept: Attach `<input ref={inputRef}/>` then `inputRef.current.focus()` to access DOM directly.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `<input ref={inputRef}/>` `inputRef.current.focus()` — e.g. `<input ref={inputRef}/>` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

49. **How does `useRef` persist values?**
Concept: Store timers/ids/prev values in ref; updates don't trigger render unlike state.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `const ref = useRef(null); <input ref={ref}/> ; ref.current.focus()` without re-rendering.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

50. **What does `useMemo` do?**
Concept: `useMemo(()=>compute(a),[a])` caches expensive calculation result until deps change.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useMemo(()=>compute(a),[a])` — e.g. `useMemo(()=>compute(a),[a])` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

51. **What does `useCallback` do?**
Concept: `useCallback(fn,[deps])` caches function identity so memoized children don't re-render unnecessarily.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useCallback(fn,[deps])` — e.g. `useCallback(fn,[deps])` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

52. **`useMemo` vs `useCallback`?**
Concept: `useMemo` memoizes a value; `useCallback` memoizes a function (equivalent to `useMemo(()=>fn)`).
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useMemo` `useCallback` — e.g. `useMemo` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

53. **When should you use `useMemo`?**
Concept: For heavy computations, referential-stable objects passed to memoized children, or expensive filtering/sorting.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `const sorted = useMemo(() => items.sort((a,b)=>a-b), [items])` caches heavy work.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

54. **When should you NOT use `useMemo`?**
Concept: Don't wrap cheap work everywhere; it adds memory/complexity and rarely fixes slowness alone.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `const sorted = useMemo(() => items.sort((a,b)=>a-b), [items])` caches heavy work.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

55. **What does `useReducer` do?**
Concept: `useReducer(reducer,init)` manages complex state transitions via `dispatch({type})` like Redux-lite.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useReducer(reducer,init)` `dispatch({type})` — e.g. `useReducer(reducer,init)` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

56. **`useState` vs `useReducer`?**
Concept: `useState` for simple independent values; `useReducer` for related state, state machines, or predictable updates.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useState` `useReducer` — e.g. `useState` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

57. **What is `useImperativeHandle`?**
Concept: It customizes ref exposed via `forwardRef`, e.g. exposing `focus()` or `reset()` from child.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `forwardRef` `focus()` — e.g. `forwardRef` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

58. **What is `useTransition`?**
Concept: `useTransition` marks non-urgent updates (`startTransition`) to keep UI responsive during heavy renders.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useTransition` `startTransition` — e.g. `useTransition` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

59. **What is `useDeferredValue`?**
Concept: It defers a value (like search query) to keep input fast while list updates in background.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

60. **What is `useId`?**
Concept: `useId` generates stable unique ids for accessibility attributes like `label htmlFor`.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useId` `label htmlFor` — e.g. `useId` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

61. **What is a custom hook?**
Concept: A custom hook is a `use*` function extracting reusable stateful logic, e.g. `useFetch`, `useAuth`.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `use*` `useFetch` — e.g. `use*` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

62. **Why must custom hooks start with `use`?**
Concept: The `use` prefix lets React lint rules and runtime enforce hook rules and state association.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `use` — e.g. `use` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

63. **Can hooks be called conditionally?**
Concept: No, call order must be stable; put conditions inside hooks, not hooks inside conditions.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

64. **What is `useDebugValue`?**
Concept: It shows custom-hook label in React DevTools for easier debugging.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

65. **What is `useSyncExternalStore`?**
Concept: It subscribes to external stores (Redux/Zustand) with concurrent-safe tearing-free reads.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

66. **What is `useInsertionEffect`?**
Concept: It runs before DOM mutations for CSS-in-JS style injection; rarely used in app code.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useEffect(() => { fetchUsers(); return () => controller.abort(); }, [page])` with cleanup.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

67. **How to share logic via hooks vs HOC?**
Concept: Custom hooks share logic without component nesting/props collision, preferred over HOCs/render props now.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

68. **What is stale closure problem?**
Concept: Effect/callback captures old state/props because function closed over render-time values.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

69. **How to fix stale closures?**
Concept: Add deps, use functional updates, use ref for latest value, or move function inside effect.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

70. **How to handle events in `useEffect`?**
Concept: In React 18 use `useEffectEvent` pattern or define handler inside effect to avoid unnecessary re-subscribes.
Why it matters: hooks tie state and side-effects to the render cycle, so missing deps or unstable call order causes stale data and extra renders.
Code example: `useEffectEvent` — e.g. `useEffectEvent` used directly in a component.
Project use: e.g. in a MERN app, a `useFetchUsers` custom hook encapsulates loading/error state reused across admin and dashboard pages.
Mistake/tip: don't call hooks conditionally or omit deps; enable `eslint-plugin-react-hooks` and prefer functional updates `setX(v=>...)`.

71. **What are class lifecycle methods?**
Concept: `constructor`, `render`, `componentDidMount`, `componentDidUpdate`, `componentWillUnmount` for init/update/cleanup.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `constructor` `render` — e.g. `constructor` used directly in a component.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

72. **What is `componentDidMount` equivalent?**
Concept: `useEffect(()=>{...},[])` runs once after mount for fetching or subscriptions.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `useEffect(()=>{...},[])` — e.g. `useEffect(()=>{...},[])` used directly in a component.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

73. **What is `componentWillUnmount` equivalent?**
Concept: Cleanup return in `useEffect`: `return ()=>clearInterval(id)`.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `useEffect` `return ()=>clearInterval(id)` — e.g. `useEffect` used directly in a component.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

74. **What is Virtual DOM?**
Concept: Virtual DOM is a lightweight JS tree representation React diffs to minimize real DOM updates.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

75. **What is reconciliation?**
Concept: Reconciliation is React's algorithm comparing old/new trees to compute minimal DOM mutations.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

76. **How does diffing work?**
Concept: It compares by type and key at same level, reuses DOM nodes when type matches, recreates otherwise.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

77. **What is React Fiber?**
Concept: Fiber is React's reconciler architecture enabling interruptible, prioritized, concurrent rendering.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

78. **How do keys help reconciliation?**
Concept: Keys match children across renders so moves/updates preserve state instead of remounting.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `{users.map(u => <Row key={u._id} user={u}/>)}` — stable id, never index or random.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

79. **Why do unstable keys cause bugs?**
Concept: Random keys each render force remount, losing input state, focus, and hurting performance.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `{users.map(u => <Row key={u._id} user={u}/>)}` — stable id, never index or random.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

80. **What is a re-render?**
Concept: Re-render is React re-invoking component function to get new JSX after state/props/context change.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

81. **What triggers re-render?**
Concept: State setter, parent re-render, context change, or hook like `useReducer` dispatch.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `useReducer` — e.g. `useReducer` used directly in a component.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

82. **What is hydration?**
Concept: Hydration attaches event listeners to server-rendered HTML in SSR/Next.js to make it interactive.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

83. **CSR vs SSR?**
Concept: CSR renders in browser after JS loads; SSR renders HTML on server for faster FCP and SEO.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

84. **What is StrictMode?**
Concept: `<StrictMode>` dev-only wrapper surfacing side-effect, legacy API, and unsafe lifecycle issues.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `<StrictMode>` — e.g. `<StrictMode>` used directly in a component.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

85. **What are Error Boundaries?**
Concept: Class components with `getDerivedStateFromError/componentDidCatch` catching render errors and showing fallback UI.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `getDerivedStateFromError/componentDidCatch` — e.g. `getDerivedStateFromError/componentDidCatch` used directly in a component.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

86. **Why can't functional components be Error Boundaries?**
Concept: No hook equivalent exists yet; must use class component for error boundary.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

87. **Mount vs update vs unmount?**
Concept: Mount is first insert, update is re-render from new data, unmount is removal with cleanup.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

88. **What is concurrent rendering?**
Concept: Concurrent rendering lets React pause/resume/prioritize work to keep urgent input responsive.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

89. **What is `key` remount trick?**
Concept: Changing `key` forces fresh mount to reset state, e.g. `<Form key={userId}/>`.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `key` `<Form key={userId}/>` — e.g. `key` used directly in a component.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

90. **Child re-render when parent re-renders?**
Concept: Yes by default all children re-render unless memoized with `memo` and stable props.
Why it matters: React minimizes real DOM work via diffing, so understanding reconciliation directly affects performance and state preservation.
Code example: `memo` — e.g. `memo` used directly in a component.
Project use: e.g. in a MERN product list, stable keys and memoization keep scroll position and input focus intact during updates.
Mistake/tip: don't generate random keys each render or ignore StrictMode double-effects; always return cleanup for subscriptions/timers.

91. **What is Redux?**
Concept: Redux is a predictable global store with single state, actions, and pure reducers.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createSlice({name:'cart', initialState, reducers:{add:(s,a)=>{s.items.push(a.payload)}}})` + `useSelector/useDispatch`.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

92. **When to use Redux vs Context?**
Concept: Redux for complex shared state, caching, DevTools, middleware; Context for simple low-frequency values like theme/auth.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `<AuthContext.Provider value={user}><App/></Provider>` + `useContext(AuthContext)` to consume.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

93. **What is Redux Toolkit (RTK)?**
Concept: RTK is official Redux toolkit with `configureStore`, `createSlice`, and RTK Query to cut boilerplate.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `configureStore` `createSlice` — e.g. `configureStore` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

94. **What is `configureStore`?**
Concept: It creates store with DevTools, thunk, and combined reducers preconfigured.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

95. **What is `createSlice`?**
Concept: `createSlice({name,initialState,reducers})` generates actions + reducer with Immer-powered mutable syntax.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createSlice({name,initialState,reducers})` — e.g. `createSlice({name,initialState,reducers})` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

96. **How does Immer help in RTK?**
Concept: Immer lets you write `state.count++` safely by producing immutable updates under the hood.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `state.count++` — e.g. `state.count++` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

97. **What are actions in Redux?**
Concept: Actions are `{type,payload}` objects describing what happened, dispatched to reducers.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `{type,payload}` — e.g. `{type,payload}` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

98. **What are reducers?**
Concept: Reducers are pure functions `(state,action)=>newState` specifying how state updates.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `(state,action)=>newState` — e.g. `(state,action)=>newState` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

99. **What is `useSelector`?**
Concept: `useSelector(s=>s.cart.items)` reads slice state and re-renders when selected value changes.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `useSelector(s=>s.cart.items)` — e.g. `useSelector(s=>s.cart.items)` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

100. **What is `useDispatch`?**
Concept: `useDispatch()` returns `dispatch` to send actions/thunks to the store.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `useDispatch()` `dispatch` — e.g. `useDispatch()` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

101. **Why keep reducers pure?**
Concept: Pure reducers are predictable, testable, and enable time-travel without side effects.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `export default memo(Row)` + `useMemo/useCallback` for stable props to skip renders.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

102. **What is Redux Thunk?**
Concept: Thunk is middleware letting actions be async functions for API calls before dispatching.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createSlice({name:'cart', initialState, reducers:{add:(s,a)=>{s.items.push(a.payload)}}})` + `useSelector/useDispatch`.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

103. **What is `createAsyncThunk`?**
Concept: It generates pending/fulfilled/rejected actions for async logic with automatic lifecycle handling.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createAsyncThunk('u/fetch', async()=>api.get('/users'))` or `useGetUsersQuery(page)` with tags.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

104. **How to handle loading in `createAsyncThunk`?**
Concept: Handle `pending/fulfilled/rejected` in `extraReducers` to set `status` and `error`.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `pending/fulfilled/rejected` `extraReducers` — e.g. `pending/fulfilled/rejected` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

105. **How to access state in thunk?**
Concept: Use `thunkAPI.getState()` and `rejectWithValue()` for custom error payloads.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `thunkAPI.getState()` `rejectWithValue()` — e.g. `thunkAPI.getState()` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

106. **Thunks vs sagas?**
Concept: Thunks are simple promise-based; sagas use generators for complex cancellation/workflows but add complexity.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createAsyncThunk('u/fetch', async()=>api.get('/users'))` or `useGetUsersQuery(page)` with tags.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

107. **What is RTK Query?**
Concept: RTK Query is data-fetching/caching layer in RTK with auto hooks, deduping, polling, and invalidation.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createAsyncThunk('u/fetch', async()=>api.get('/users'))` or `useGetUsersQuery(page)` with tags.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

108. **How to define RTK Query API?**
Concept: Use `createApi({reducerPath,baseQuery:fetchBaseQuery({baseUrl}),endpoints})`.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createApi({reducerPath,baseQuery:fetchBaseQuery({baseUrl}),endpoints})` — e.g. `createApi({reducerPath,baseQuery:fetchBaseQuery({baseUrl}),endpoints})` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

109. **What is `fetchBaseQuery`?**
Concept: Lightweight fetch wrapper handling baseUrl, headers, auth prep, and query string.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createAsyncThunk('u/fetch', async()=>api.get('/users'))` or `useGetUsersQuery(page)` with tags.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

110. **Query vs mutation in RTK Query?**
Concept: Query is GET cached read via `useGetUsersQuery`; mutation is write via `useAddUserMutation`.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `useGetUsersQuery` `useAddUserMutation` — e.g. `useGetUsersQuery` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

111. **How does caching work in RTK Query?**
Concept: It caches by endpoint+args, dedupes concurrent requests, and shares data across components.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createAsyncThunk('u/fetch', async()=>api.get('/users'))` or `useGetUsersQuery(page)` with tags.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

112. **What are tags in RTK Query?**
Concept: `providesTags/invalidatesTags` auto-refetch queries when mutations change related data.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `providesTags/invalidatesTags` — e.g. `providesTags/invalidatesTags` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

113. **How to add auth token in RTK Query?**
Concept: Use `prepareHeaders` in `fetchBaseQuery` to inject JWT from store/localStorage.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `prepareHeaders` `fetchBaseQuery` — e.g. `prepareHeaders` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

114. **How to handle pagination with RTK Query?**
Concept: Pass page args `useGetPostsQuery(page)` and merge cache or use `serializeQueryArgs`.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `useGetPostsQuery(page)` `serializeQueryArgs` — e.g. `useGetPostsQuery(page)` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

115. **Polling/refetch in RTK Query?**
Concept: Use `pollingInterval`, `refetchOnFocus`, `refetchOnReconnect` options.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `pollingInterval` `refetchOnFocus` — e.g. `pollingInterval` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

116. **How to normalize Redux state?**
Concept: Use `createEntityAdapter` for `{ids,entities}` normalized collections with CRUD helpers.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createEntityAdapter` `{ids,entities}` — e.g. `createEntityAdapter` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

117. **Why normalize state?**
Concept: Avoids duplication, enables O(1) updates, and keeps relational MERN data consistent.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `const [count, setCount] = useState(0); setCount(c => c + 1)` triggers a re-render.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

118. **What is selector memoization?**
Concept: Use `createSelector` (Reselect) to compute derived data only when inputs change.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createSelector` — e.g. `createSelector` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

119. **How to structure Redux folders?**
Concept: Feature folders with `slice.js`, `api.js`, `selectors.js`, e.g. `features/cart/cartSlice.js`.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `slice.js` `api.js` — e.g. `slice.js` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

120. **How to persist Redux state?**
Concept: Use `redux-persist` or manual localStorage sync for cart/auth, rehydrating on load.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `redux-persist` — e.g. `redux-persist` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

121. **How to reset store on logout?**
Concept: Dispatch root reset action returning `initialState` or clear persisted slices.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `initialState` — e.g. `initialState` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

122. **Redux DevTools benefits?**
Concept: Time-travel, action inspection, state diffing for faster debugging.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createSlice({name:'cart', initialState, reducers:{add:(s,a)=>{s.items.push(a.payload)}}})` + `useSelector/useDispatch`.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

123. **How to type Redux with TypeScript?**
Concept: Infer `RootState/AppDispatch` from store and use typed `useAppSelector/useAppDispatch`.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `RootState/AppDispatch` `useAppSelector/useAppDispatch` — e.g. `RootState/AppDispatch` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

124. **How to connect MERN backend to Redux?**
Concept: Thunks/RTK Query call Express `/api/*` endpoints, store JWT, handle 401 logout.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `/api/*` — e.g. `/api/*` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

125. **How to handle errors globally in RTK?**
Concept: Use `rejectWithValue`, `transformErrorResponse`, and middleware/toast for display.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `rejectWithValue` `transformErrorResponse` — e.g. `rejectWithValue` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

126. **What is optimistic update in RTK Query?**
Concept: Update cache immediately via `onQueryStarted` + `updateQueryData`, rollback on failure.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `onQueryStarted` `updateQueryData` — e.g. `onQueryStarted` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

127. **How to cancel RTK Query request?**
Concept: It auto-aborts on unmount/arg change; manual abort via `promise.abort()` from hook result.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `promise.abort()` — e.g. `promise.abort()` used directly in a component.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

128. **Can you use Redux without Toolkit?**
Concept: Yes but requires manual store, action constants, and immutable spreads; RTK is recommended.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createSlice({name:'cart', initialState, reducers:{add:(s,a)=>{s.items.push(a.payload)}}})` + `useSelector/useDispatch`.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

129. **How to test Redux slice?**
Concept: Call reducer with actions and assert state; test thunks with mock store/msw.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createSlice({name:'cart', initialState, reducers:{add:(s,a)=>{s.items.push(a.payload)}}})` + `useSelector/useDispatch`.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

130. **Zustand vs Redux?**
Concept: Zustand is lighter with less boilerplate; Redux Toolkit better for large teams, DevTools, RTK Query.
Why it matters: centralized predictable state with pure reducers makes complex MERN flows debuggable, testable, and cacheable.
Code example: `createSlice({name:'cart', initialState, reducers:{add:(s,a)=>{s.items.push(a.payload)}}})` + `useSelector/useDispatch`.
Project use: e.g. in a MERN shop, cart/auth/orders live in RTK slices with RTK Query caching product lists and invalidating on mutations.
Mistake/tip: don't put derived/duplicate data in store or write impure reducers; use `createEntityAdapter` + `createSelector` and tags for invalidation.

131. **What is React Router?**
Concept: React Router enables SPA navigation with routes, params, and history without full reloads.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `<Route path="/users/:id" element={<User/>}/>` + `useParams()/useNavigate()` for nav.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

132. **How to define routes v6?**
Concept: Use `<BrowserRouter><Routes><Route path="/users/:id" element={<User/>}/></Routes>`.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `<BrowserRouter><Routes><Route path="/users/:id" element={<User/>}/></Routes>` — e.g. `<BrowserRouter><Routes><Route path="/users/:id" element={<User/>}/></Routes>` used directly in a component.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

133. **How to get URL params?**
Concept: `useParams()` returns `:id`; `useSearchParams()` handles `?page=2`.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `useParams()` `:id` — e.g. `useParams()` used directly in a component.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

134. **How to navigate programmatically?**
Concept: `const nav=useNavigate(); nav('/login',{state})` or `<Navigate>` for redirects.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `const nav=useNavigate(); nav('/login',{state})` `<Navigate>` — e.g. `const nav=useNavigate(); nav('/login',{state})` used directly in a component.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

135. **How to protect routes?**
Concept: Wrap in `<RequireAuth>` checking token/context, redirecting to `/login` if missing.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `<RequireAuth>` `/login` — e.g. `<RequireAuth>` used directly in a component.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

136. **What is nested routing?**
Concept: Child `<Route>` inside parent with `<Outlet/>` for layouts like dashboard sidebar.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `<Route>` `<Outlet/>` — e.g. `<Route>` used directly in a component.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

137. **What is `Outlet`?**
Concept: `Outlet` renders matched child route inside parent layout component.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `Outlet` — e.g. `Outlet` used directly in a component.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

138. **How to handle 404?**
Concept: Add `<Route path="*" element={<NotFound/>}/>` as catch-all.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `<Route path="*" element={<NotFound/>}/>` — e.g. `<Route path="*" element={<NotFound/>}/>` used directly in a component.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

139. **How to lazy-load routes?**
Concept: `const Admin=React.lazy(()=>import('./Admin'))` with `<Suspense>` plus router for code-splitting.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `const Admin=React.lazy(()=>import('./Admin'))` `<Suspense>` — e.g. `const Admin=React.lazy(()=>import('./Admin'))` used directly in a component.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

140. **How to scroll to top on route change?**
Concept: Use `ScrollToTop` component with `useLocation` + `useEffect` calling `window.scrollTo(0,0)`.
Why it matters: SPA routing keeps navigation instant without reloads while preserving state and enabling deep-linkable URLs.
Code example: `ScrollToTop` `useLocation` — e.g. `ScrollToTop` used directly in a component.
Project use: e.g. in a MERN app, `/dashboard/*` layout with `<Outlet/>`, protected `<RequireAuth/>`, and lazy-loaded admin routes.
Mistake/tip: don't hardcode full-page links with `<a>` or forget `*` 404 route; use `Link/useNavigate` and sync page/filters to search params.

141. **Controlled form example?**
Concept: `const [v,setV]=useState(''); <input value={v} onChange={e=>setV(e.target.value)}/>`.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `const [v,setV]=useState(''); <input value={v} onChange={e=>setV(e.target.value)}/>` — e.g. `const [v,setV]=useState(''); <input value={v} onChange={e=>setV(e.target.value)}/>` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

142. **How to handle multi-input forms?**
Concept: Single state object with `name` attribute: `setForm(f=>({...f,[e.target.name]:e.target.value}))`.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `name` `setForm(f=>({...f,[e.target.name]:e.target.value}))` — e.g. `name` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

143. **How to validate forms?**
Concept: Manual checks, or libraries like React Hook Form + Zod/Yup for schema validation.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `<input value={v} onChange={e=>setV(e.target.value)} />` — controlled input pattern.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

144. **Why use React Hook Form?**
Concept: Uncontrolled-based, fewer re-renders, built-in validation, easy MERN integration.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `<input value={v} onChange={e=>setV(e.target.value)} />` — controlled input pattern.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

145. **How to submit form to Express API?**
Concept: `onSubmit` preventDefault, POST via fetch/axios/RTK mutation, handle loading/errors.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `onSubmit` — e.g. `onSubmit` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

146. **How to handle file uploads?**
Concept: Use `FormData` with `<input type="file">` and `multipart/form-data` to Multer backend.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `FormData` `<input type="file">` — e.g. `FormData` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

147. **How to show form errors?**
Concept: Store `errors` object from validation/backend and render under inputs conditionally.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `errors` — e.g. `errors` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

148. **How to reset form?**
Concept: Reset state to initial or `reset()` in React Hook Form after success.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `reset()` — e.g. `reset()` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

149. **How to debounce search input?**
Concept: `useDeferredValue` or `setTimeout` in `useEffect` / lodash `debounce` before API call.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `useDeferredValue` `setTimeout` — e.g. `useDeferredValue` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

150. **How to prevent double submit?**
Concept: Disable button on `isLoading`, use idempotency key or ignore while pending.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `isLoading` — e.g. `isLoading` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

151. **GET vs POST in forms?**
Concept: GET for search filters in URL; POST for creates/updates with body.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `<input value={v} onChange={e=>setV(e.target.value)} />` — controlled input pattern.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

152. **How to handle select/checkbox/radio?**
Concept: Control `value/checked` in state; checkbox groups use array toggle logic.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `value/checked` — e.g. `value/checked` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

153. **What is Formik?**
Concept: Formik manages form state/validation/submission, now often replaced by React Hook Form.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `<input value={v} onChange={e=>setV(e.target.value)} />` — controlled input pattern.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

154. **How to integrate reCAPTCHA?**
Concept: Add widget, send token with form, verify server-side in Express before processing.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

155. **How to persist draft form?**
Concept: Save to localStorage on change via `useEffect` and restore on mount.
Why it matters: forms are the main MERN write path, so controlled state plus validation decides UX quality and backend data integrity.
Code example: `useEffect` — e.g. `useEffect` used directly in a component.
Project use: e.g. in a MERN Register/Login page, controlled inputs validate client-side then POST to Express with loading and server-error display.
Mistake/tip: don't leave double-submit enabled or mix controlled/uncontrolled; disable while pending and show field-level errors.

156. **What is code-splitting?**
Concept: Splitting bundle via `React.lazy`, dynamic `import()`, and route splitting to load on demand.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `React.lazy` `import()` — e.g. `React.lazy` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

157. **How to memoize expensive lists?**
Concept: `useMemo` for filtered data + `React.memo` rows + stable keys and callbacks.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `useMemo` `React.memo` — e.g. `useMemo` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

158. **How to avoid inline object props?**
Concept: Hoist constants or `useMemo` objects; inline `{}` breaks `memo` shallow compare.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `useMemo` `{}` — e.g. `useMemo` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

159. **How to optimize context re-renders?**
Concept: Split contexts, memoize provider value with `useMemo`, and colocate consumers.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `useMemo` — e.g. `useMemo` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

160. **What is windowing/virtualization?**
Concept: Render only visible rows with `react-window`/`tanstack-virtual` for huge MERN lists.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `react-window` `tanstack-virtual` — e.g. `react-window` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

161. **How to profile React performance?**
Concept: Use React DevTools Profiler and `why-did-you-render` to find wasted renders.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `why-did-you-render` — e.g. `why-did-you-render` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

162. **How to optimize images?**
Concept: Lazy-load, `srcSet`, modern formats, CDN, blur placeholder, fixed dimensions to avoid CLS.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `srcSet` — e.g. `srcSet` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

163. **How to debounce vs throttle?**
Concept: Debounce waits for pause (search), throttle limits rate (scroll/resize).
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

164. **How to cache API responses?**
Concept: RTK Query cache, React Query, or manual `useMemo`/Map; set `Cache-Control` on Express.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `useMemo` `Cache-Control` — e.g. `useMemo` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

165. **How to avoid waterfall fetches?**
Concept: Fetch in parallel with `Promise.all`, colocate queries, or use loader/RTK Query batching.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `Promise.all` — e.g. `Promise.all` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

166. **How to handle large Redux store?**
Concept: Normalize, paginate, use selectors, and avoid storing derived/duplicate data.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `createSlice({name:'cart', initialState, reducers:{add:(s,a)=>{s.items.push(a.payload)}}})` + `useSelector/useDispatch`.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

167. **What is `key` prop performance impact?**
Concept: Stable keys enable DOM reuse; bad keys cause full remounts and lost state.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `<input value={v} onChange={e=>setV(e.target.value)} />` — controlled input pattern.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

168. **SSR performance benefit?**
Concept: Faster first paint/SEO but adds server cost; stream with Suspense/Next.js.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `<input value={v} onChange={e=>setV(e.target.value)} />` — controlled input pattern.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

169. **How to reduce bundle size?**
Concept: Tree-shake, import only needed libs, analyze with `source-map-explorer`, lazy-load routes.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `source-map-explorer` — e.g. `source-map-explorer` used directly in a component.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

170. **How to optimize `useEffect` fetches?**
Concept: Abort on cleanup, dedupe with RTK Query, cache, and avoid strict dep loops.
Why it matters: wasted renders and large bundles hurt interactivity, so memoization, splitting, and caching keep the app fast.
Code example: `useEffect(() => { fetchUsers(); return () => controller.abort(); }, [page])` with cleanup.
Project use: e.g. in a MERN feed with thousands of rows, virtualization plus `useMemo` filtering and route-level code-splitting keep it smooth.
Mistake/tip: don't wrap everything in `useMemo` or pass inline `{}` to memoized children; profile first with React DevTools Profiler.

171. **What is Jest + RTL?**
Concept: Jest is test runner, React Testing Library tests components by user behavior, not internals.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `render(<Login/>); await user.click(screen.getByRole('button')); expect(screen.getByText(/welcome/i)).toBeInTheDocument()`.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

172. **How to test a component?**
Concept: `render(<Login/>)`, `fireEvent/screen`, assert output; mock fetch with MSW.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `render(<Login/>)` `fireEvent/screen` — e.g. `render(<Login/>)` used directly in a component.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

173. **How to test hooks?**
Concept: `renderHook(()=>useCounter())` from RTL, act then assert return values.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `renderHook(()=>useCounter())` — e.g. `renderHook(()=>useCounter())` used directly in a component.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

174. **How to test Redux slice?**
Concept: Dispatch actions to reducer and expect state; test async thunk pending/fulfilled.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `createSlice({name:'cart', initialState, reducers:{add:(s,a)=>{s.items.push(a.payload)}}})` + `useSelector/useDispatch`.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

175. **How to test RTK Query?**
Concept: Mock `fetchBaseQuery`/MSW server and assert hooks loading/data states.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `fetchBaseQuery` — e.g. `fetchBaseQuery` used directly in a component.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

176. **How to mock API in tests?**
Concept: Use `msw` handlers or `jest.mock` axios/fetch to return fixtures.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `msw` `jest.mock` — e.g. `msw` used directly in a component.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

177. **What is snapshot testing?**
Concept: Stores rendered output to detect unintended UI changes; use sparingly.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `render(<Login/>); await user.click(screen.getByRole('button')); expect(screen.getByText(/welcome/i)).toBeInTheDocument()`.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

178. **How to test forms?**
Concept: Fill with `userEvent.type/click`, submit, assert validation messages and API call.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `userEvent.type/click` — e.g. `userEvent.type/click` used directly in a component.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

179. **How to test routing?**
Concept: Render inside `MemoryRouter` with initial entries and assert navigation.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `MemoryRouter` — e.g. `MemoryRouter` used directly in a component.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

180. **How to test `useEffect` fetch?**
Concept: Mock API, render, `await screen.findByText()` for async data, assert cleanup.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `await screen.findByText()` — e.g. `await screen.findByText()` used directly in a component.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

181. **Unit vs integration vs E2E?**
Concept: Unit tests single fn/component, integration tests flow with store/router, E2E (Cypress/Playwright) tests real browser.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

182. **How to test performance?**
Concept: Measure render counts, Profiler timings, Lighthouse, and assert memo prevents re-render.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `<input value={v} onChange={e=>setV(e.target.value)} />` — controlled input pattern.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

183. **How to run coverage?**
Concept: `npm test -- --coverage` and enforce thresholds in CI for critical slices/utils.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `npm test -- --coverage` — e.g. `npm test -- --coverage` used directly in a component.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

184. **How to test MERN auth flow?**
Concept: Mock `/api/login` returning JWT, assert token stored and protected route renders.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `/api/login` — e.g. `/api/login` used directly in a component.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

185. **What is Cypress/Playwright?**
Concept: E2E tools driving real browser to test login, CRUD, and checkout flows.
Why it matters: behavior-driven tests with mocked APIs catch regressions in UI, store, and routing before production.
Code example: `render(<Login/>); await user.click(screen.getByRole('button')); expect(screen.getByText(/welcome/i)).toBeInTheDocument()`.
Project use: e.g. in a MERN project, RTL tests render pages with mock store/router and MSW for `/api/*`, asserting user-visible outcomes.
Mistake/tip: don't test implementation details or real network; query by role/text, mock with MSW, and await async UI with `findBy*`.

186. **How to handle CORS in MERN?**
Concept: Enable `cors({origin:frontendUrl,credentials:true})` on Express and match fetch `credentials`.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `cors({origin:frontendUrl,credentials:true})` `credentials` — e.g. `cors({origin:frontendUrl,credentials:true})` used directly in a component.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

187. **How to store JWT securely?**
Concept: Prefer httpOnly cookie over localStorage to mitigate XSS; use short expiry + refresh.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `cors({origin:FE_URL, credentials:true})` + axios interceptor on 401 clearing auth and routing to `/login`.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

188. **How to handle 401 in frontend?**
Concept: Interceptor catches 401, clears auth slice, redirects to login with toast.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `cors({origin:FE_URL, credentials:true})` + axios interceptor on 401 clearing auth and routing to `/login`.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

189. **How to manage env vars in React?**
Concept: `VITE_*` or `REACT_APP_*` vars; never expose secrets, only public keys/URLs.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `VITE_*` `REACT_APP_*` — e.g. `VITE_*` used directly in a component.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

190. **How to handle loading/error UX?**
Concept: Show skeletons/spinners, error boundaries + retry, and empty states for lists.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

191. **Vite vs CRA?**
Concept: Vite is faster dev/build with ESM/HMR; CRA is deprecated and slower.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

192. **How to deploy MERN frontend?**
Concept: Build `npm run build`, serve `dist` via Netlify/Vercel/Nginx with API proxy.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `npm run build` `dist` — e.g. `npm run build` used directly in a component.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

193. **How to do SEO in SPA?**
Concept: Use SSR/Next.js, meta tags with `react-helmet`, sitemap, and pre-rendering.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `react-helmet` — e.g. `react-helmet` used directly in a component.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

194. **How to implement infinite scroll?**
Concept: IntersectionObserver triggering next page fetch, appending to RTK Query/cache list.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

195. **How to implement search + filter?**
Concept: Controlled query state, debounced API call with `?q=&sort=&page=`, cache by args.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `?q=&sort=&page=` — e.g. `?q=&sort=&page=` used directly in a component.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

196. **How to handle websockets in React?**
Concept: `useEffect` opens socket.io, listens, updates state/Redux, disconnects in cleanup.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `useEffect` — e.g. `useEffect` used directly in a component.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

197. **How to do optimistic UI for MERN CRUD?**
Concept: Update Redux/cache instantly, call API, rollback + toast on failure.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: see minimal snippet in concept — copy it into a small demo component to verify behavior.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

198. **How to handle pagination UI?**
Concept: Track `page/limit/total`, disable prev/next at bounds, sync page to URL search params.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `page/limit/total` — e.g. `page/limit/total` used directly in a component.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

199. **Props/state interview tip for 1 YOE?**
Concept: Show small demo: lifted state, memoized child, Context/RTK for global, and controlled form.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `const [count, setCount] = useState(0); setCount(c => c + 1)` triggers a re-render.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.

200. **Redux Toolkit interview tip for 1 YOE?**
Concept: Explain slice + `createAsyncThunk`/RTK Query flow, tags/invalidation, and selector memoization with example.
Why it matters: frontend decisions (auth, CORS, loading UX, deploy) determine how reliably the React app integrates with Express/Mongo.
Code example: `createAsyncThunk` — e.g. `createAsyncThunk` used directly in a component.
Project use: e.g. in a MERN deployment, Vite build served on Vercel/Netlify talks to Express API with httpOnly-cookie JWT and CORS credentials.
Mistake/tip: don't store JWT in localStorage or expose secrets in `VITE_*`; use httpOnly cookies, short expiry, and 401 interceptor to logout.
