# 06 - DSA: Think in Logic, Not Just Code

Interviewers check approach: clarify -> brute -> optimize -> complexity -> edge -> code -> test.

## Big-O Cheat (memorize)
- Array access O(1), search O(n), push/pop O(1), shift O(n)
- Object/Map get/set O(1)
- Binary search O(log n), sort O(n log n), nested loops O(n^2)
- BFS/DFS O(V+E), hash O(1) avg
- Space: in-place O(1) vs copy O(n)

## Patterns + When to Use
1. HashMap freq -> Two Sum, duplicates, anagrams
2. Two pointers -> sorted array, palindrome, container water
3. Sliding window -> longest substring K distinct, max sum subarray
4. Stack -> valid parentheses, next greater, min stack
5. Fast/slow -> cycle, middle of list
6. Binary search -> rotated array, first/last
7. BFS (queue) -> shortest path, level order; DFS (stack/rec) -> paths, islands
8. Heap -> top K, merge K lists
9. DP basics -> climb stairs, coin change (if asked, give memo version)

## 15 Must-Do (with optimal idea)

1. **Two Sum** - Map complement: `for(i,x){if(map.has(t-x))return...;map.set(x,i)}` O(n)
2. **Valid Parentheses** - Stack push open, pop match `pairs={')':'('}` O(n)
3. **Best Time Stock** - minPrice track, max profit O(n)
4. **Contains Duplicate** - Set size vs len O(n)
5. **Group Anagrams** - key sorted word in Map O(n*k log k)
6. **Top K Frequent** - Map count + bucket/heap O(n log k)
7. **Product Except Self** - prefix+suffix O(n) no div
8. **Longest Substring No Repeat** - sliding window + Set O(n)
9. **3Sum** - sort + two pointers skip dups O(n^2)
10. **Merge Intervals** - sort start then merge O(n log n)
11. **Reverse Linked List** - prev/curr iterative O(n)
12. **Cycle Detect** - Floyd fast/slow O(n)
13. **Binary Search** - `while(l<=r){m=(l+r)>>1}` O(log n)
14. **Number Islands** - DFS flood fill count O(m*n)
15. **Climb Stairs** - `dp[i]=dp[i-1]+dp[i-2]` O(n) O(1) space

## JS Snippets to Write Blind
```js
// two sum
function twoSum(a,t){const m=new Map();for(let i=0;i<a.length;i++){const c=t-a[i];if(m.has(c))return[m.get(c),i];m.set(a[i],i)}}
// valid paren
function isValid(s){const st=[],m={')':'(',']':'[','}':'{'};for(const c of s){if('([{'.includes(c))st.push(c);else if(st.pop()!==m[c])return false}return !st.length}
// bfs
function bfs(g,s){const q=[s],v=new Set([s]);while(q.length){const n=q.shift();for(const nb of g[n]??[])if(!v.has(nb)){v.add(nb);q.push(nb)}}return[...v]}
```

## How to Speak While Coding
1. "Can input be empty/large? Sorted?"
2. "Brute is O(n^2), we can do O(n) with map because..."
3. "Time X, space Y because..."
4. Test: `[]`, `[1]`, dups, negative, large.

## SQL-flavored Logic (often in backend round)
- 2nd highest, dedupe `ROW_NUMBER() OVER(PARTITION BY email)`, running total `SUM() OVER(ORDER BY date)`.
