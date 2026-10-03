# DSA + Git/HR - 200 Q&A

> For 1 YOE MERN dev - Big-O, patterns, 15 must-do codes, System Design, Git flow, HR.

## DSA - 100 Q&A

### Big-O (1-10)
1. **What is Big-O?**
  - Approach: Upper bound of growth rate; describes worst-case time/space vs n.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: Upper bound of growth rate; describes worst-case time/space vs n. // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: Upper bound of growth rate; describes worst-case time/space vs n."
2. **O(1) vs O(n) vs O(log n) example?**
  - Approach: `arr[0]` O(1), loop O(n), binary search O(log n).
  - Complexity: O(1); O(n); O(log n) time; see approach for space.
  - Code: JS idea: `arr[0]` O(1), loop O(n), binary search O(log n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: `arr[0]` O(1), loop O(n), binary search O(log n)."
3. **What is O(n^2)?**
  - Approach: Nested loops over n, e.g., bubble sort / all pairs.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: Nested loops over n, e.g., bubble sort / all pairs. // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: Nested loops over n, e.g., bubble sort / all pairs."
4. **What is space complexity?**
  - Approach: Extra memory used; e.g., hashmap O(n), in-place sort O(1).
  - Complexity: O(n); O(1) time; see approach for space.
  - Code: JS idea: Extra memory used; e.g., hashmap O(n), in-place sort O(1). // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: Extra memory used; e.g., hashmap O(n), in-place sort O(1)."
5. **Time of hashmap lookup?**
  - Approach: Avg O(1), worst O(n) on collisions.
  - Complexity: O(1); O(n) time; see approach for space.
  - Code: JS idea: Avg O(1), worst O(n) on collisions. // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: Avg O(1), worst O(n) on collisions."
6. **Time of binary search?**
  - Approach: O(log n) time, O(1) space iterative.
  - Complexity: O(log n); O(1) time; see approach for space.
  - Code: JS idea: O(log n) time, O(1) space iterative. // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: O(log n) time, O(1) space iterative."
7. **What is amortized O(1)?**
  - Approach: Avg over ops, e.g., JS `push` / dynamic array resize doubles.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: Avg over ops, e.g., JS `push` / dynamic array resize doubles. // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: Avg over ops, e.g., JS `push` / dynamic array resize doubles."
8. **Best/Avg/Worst for quicksort?**
  - Approach: Best/Avg O(n log n), worst O(n^2) bad pivot.
  - Complexity: O(n log n); O(n^2) time; see approach for space.
  - Code: JS idea: Best/Avg O(n log n), worst O(n^2) bad pivot. // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: Best/Avg O(n log n), worst O(n^2) bad pivot."
9. **Compare sort complexities?**
  - Approach: Merge O(n log n), Bubble/Insertion O(n^2), Counting O(n+k).
  - Complexity: O(n log n); O(n^2); O(n+k) time; see approach for space.
  - Code: JS idea: Merge O(n log n), Bubble/Insertion O(n^2), Counting O(n+k). // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: Merge O(n log n), Bubble/Insertion O(n^2), Counting O(n+k)."
10. **How to analyze nested + sequential code?**
  - Approach: Sequential = max, nested = multiply; drop constants.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: Sequential = max, nested = multiply; drop constants. // implement with Map/Set/pointers, test on sample.
  - Edge cases: n=0/1, huge n, sorted vs random input, constants dropped but matter in JS.
  - Say: "In interview I'd say: Sequential = max, nested = multiply; drop constants."

### Hashmap / Array / String (11-25)
11. **Two Sum code idea?**
  - Approach: Map `need = target - x`; if in map return indices, else store. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Map `need = target - x`; if in map return indices, else store. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Map `need = target - x`; if in map return indices, else store. O(n)."
12. **Group Anagrams code idea?**
  - Approach: Key = sorted string or 26-count; map key -> list. O(n*k log k).
  - Complexity: O(n*k log k) time; see approach for space.
  - Code: JS idea: Key = sorted string or 26-count; map key -> list. O(n*k log k). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Key = sorted string or 26-count; map key -> list. O(n*k log k)."
13. **Valid Anagram code idea?**
  - Approach: Count freq with map/array 26, compare. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Count freq with map/array 26, compare. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Count freq with map/array 26, compare. O(n)."
14. **Contains Duplicate code idea?**
  - Approach: Set size vs array length; or set lookup loop. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Set size vs array length; or set lookup loop. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Set size vs array length; or set lookup loop. O(n)."
15. **Top K Frequent code idea?**
  - Approach: Count map + bucket array index=freq, take from end. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Count map + bucket array index=freq, take from end. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Count map + bucket array index=freq, take from end. O(n)."
16. **Product Except Self code idea?**
  - Approach: Prefix + suffix passes, output array, no division. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Prefix + suffix passes, output array, no division. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Prefix + suffix passes, output array, no division. O(n)."
17. **Longest Consecutive Sequence code idea?**
  - Approach: Set; only start if `n-1` missing, count forward. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Set; only start if `n-1` missing, count forward. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Set; only start if `n-1` missing, count forward. O(n)."
18. **Subarray Sum Equals K code idea?**
  - Approach: Prefix sum map `{0:1}`, ans += map[sum-k]. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Prefix sum map `{0:1}`, ans += map[sum-k]. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Prefix sum map `{0:1}`, ans += map[sum-k]. O(n)."
19. **First Non-Repeating Char idea?**
  - Approach: Freq map then scan string. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Freq map then scan string. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Freq map then scan string. O(n)."
20. **Isomorphic Strings idea?**
  - Approach: Two maps s->t and t->s to enforce bijection. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Two maps s->t and t->s to enforce bijection. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Two maps s->t and t->s to enforce bijection. O(n)."
21. **Majority Element idea?**
  - Approach: Boyer-Moore vote count, reset on 0. O(n) O(1).
  - Complexity: O(n); O(1) time; see approach for space.
  - Code: JS idea: Boyer-Moore vote count, reset on 0. O(n) O(1). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Boyer-Moore vote count, reset on 0. O(n) O(1)."
22. **Sort Colors (0/1/2) idea?**
  - Approach: Dutch flag: low/mid/high pointers, swap. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Dutch flag: low/mid/high pointers, swap. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Dutch flag: low/mid/high pointers, swap. O(n)."
23. **Rotate Array by k idea?**
  - Approach: Reverse all, reverse 0..k-1, reverse k..end. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Reverse all, reverse 0..k-1, reverse k..end. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Reverse all, reverse 0..k-1, reverse k..end. O(n)."
24. **Move Zeroes idea?**
  - Approach: Slow pointer for non-zero, fill rest 0. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Slow pointer for non-zero, fill rest 0. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: Slow pointer for non-zero, fill rest 0. O(n)."
25. **Max Subarray (Kadane) idea?**
  - Approach: `cur=max(x,cur+x); best=max(best,cur)`. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: `cur=max(x,cur+x); best=max(best,cur)`. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty array/string, single elem, all dupes, negatives, target missing.
  - Say: "In interview I'd say: `cur=max(x,cur+x); best=max(best,cur)`. O(n)."

### Two-Pointers (26-35)
26. **Valid Palindrome idea?**
  - Approach: Lowercase + two pointers skip non-alnum, compare. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Lowercase + two pointers skip non-alnum, compare. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: Lowercase + two pointers skip non-alnum, compare. O(n)."
27. **3Sum idea?**
  - Approach: Sort + for i + l/r pointers, skip dupes. O(n^2).
  - Complexity: O(n^2) time; see approach for space.
  - Code: JS idea: Sort + for i + l/r pointers, skip dupes. O(n^2). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: Sort + for i + l/r pointers, skip dupes. O(n^2)."
28. **Container With Most Water idea?**
  - Approach: l=0,r=end, move shorter, max area. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: l=0,r=end, move shorter, max area. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: l=0,r=end, move shorter, max area. O(n)."
29. **Trap Rain Water idea?**
  - Approach: l/r + lMax/rMax, add min-max-height. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: l/r + lMax/rMax, add min-max-height. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: l/r + lMax/rMax, add min-max-height. O(n)."
30. **Remove Duplicates Sorted idea?**
  - Approach: Slow pointer overwrite, return len. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Slow pointer overwrite, return len. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: Slow pointer overwrite, return len. O(n)."
31. **Two Sum Sorted idea?**
  - Approach: l+r pointers, move by sum vs target. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: l+r pointers, move by sum vs target. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: l+r pointers, move by sum vs target. O(n)."
32. **Merge Sorted Arrays idea?**
  - Approach: Fill from end with i,j,k pointers. O(m+n).
  - Complexity: O(m+n) time; see approach for space.
  - Code: JS idea: Fill from end with i,j,k pointers. O(m+n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: Fill from end with i,j,k pointers. O(m+n)."
33. **Partition Labels idea?**
  - Approach: Last index map, expand partition end. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Last index map, expand partition end. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: Last index map, expand partition end. O(n)."
34. **Reverse String in-place?**
  - Approach: Swap l/r until meet. O(n) O(1).
  - Complexity: O(n); O(1) time; see approach for space.
  - Code: JS idea: Swap l/r until meet. O(n) O(1). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: Swap l/r until meet. O(n) O(1)."
35. **Linked List Cycle detect?**
  - Approach: Slow/fast pointers, meet = cycle. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Slow/fast pointers, meet = cycle. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all same, no valid pair, odd vs even length.
  - Say: "In interview I'd say: Slow/fast pointers, meet = cycle. O(n)."

### Sliding Window (36-45)
36. **Max Sliding Window idea?**
  - Approach: Deque of decreasing indices, pop out-of-window. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Deque of decreasing indices, pop out-of-window. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Deque of decreasing indices, pop out-of-window. O(n)."
37. **Longest Substring No Repeat idea?**
  - Approach: Map + left pointer jump on repeat. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Map + left pointer jump on repeat. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Map + left pointer jump on repeat. O(n)."
38. **Longest Repeating Char Replace idea?**
  - Approach: Count + `window-maxFreq <= k` else shrink. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Count + `window-maxFreq <= k` else shrink. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Count + `window-maxFreq <= k` else shrink. O(n)."
39. **Min Window Substring idea?**
  - Approach: Need/have counts + shrink when valid. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Need/have counts + shrink when valid. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Need/have counts + shrink when valid. O(n)."
40. **Permutation in String idea?**
  - Approach: Fixed window 26-count compare. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Fixed window 26-count compare. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Fixed window 26-count compare. O(n)."
41. **Max Average Subarray k idea?**
  - Approach: Sliding sum window k, max/k. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Sliding sum window k, max/k. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Sliding sum window k, max/k. O(n)."
42. **Longest Subarray Sum <= K (positive)?**
  - Approach: Expand/shrink with sum. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Expand/shrink with sum. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Expand/shrink with sum. O(n)."
43. **Count Anagrams in string?**
  - Approach: Sliding window freq match. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Sliding window freq match. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Sliding window freq match. O(n)."
44. **Sliding Window Maximum vs Two pointers?**
  - Approach: Window = contiguous subarray of size k with deque; two pointers = flexible ends.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: Window = contiguous subarray of size k with deque; two pointers = flexible ends. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Window = contiguous subarray of size k with deque; two pointers = flexible ends."
45. **Best time to Buy/Sell Stock idea?**
  - Approach: Track min price, max `p-min`. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Track min price, max `p-min`. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty, k=0/k>n, all same char, no valid window.
  - Say: "In interview I'd say: Track min price, max `p-min`. O(n)."

### Stack / Queue (46-55)
46. **Valid Parentheses idea?**
  - Approach: Stack push open, pop-check close. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Stack push open, pop-check close. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Stack push open, pop-check close. O(n)."
47. **Min Stack idea?**
  - Approach: Two stacks: val + min-so-far. O(1) ops.
  - Complexity: O(1) time; see approach for space.
  - Code: JS idea: Two stacks: val + min-so-far. O(1) ops. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Two stacks: val + min-so-far. O(1) ops."
48. **Evaluate RPN idea?**
  - Approach: Stack numbers, on op pop 2 compute push. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Stack numbers, on op pop 2 compute push. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Stack numbers, on op pop 2 compute push. O(n)."
49. **Daily Temperatures idea?**
  - Approach: Monotonic decreasing stack, pop while warmer. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Monotonic decreasing stack, pop while warmer. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Monotonic decreasing stack, pop while warmer. O(n)."
50. **Next Greater Element idea?**
  - Approach: Monotonic stack from right + map. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Monotonic stack from right + map. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Monotonic stack from right + map. O(n)."
51. **Largest Rectangle Histogram idea?**
  - Approach: Stack indices + width on pop. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Stack indices + width on pop. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Stack indices + width on pop. O(n)."
52. **Implement Queue with Stacks?**
  - Approach: Push stack + pop stack reverse on demand. Amortized O(1).
  - Complexity: O(1) time; see approach for space.
  - Code: JS idea: Push stack + pop stack reverse on demand. Amortized O(1). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Push stack + pop stack reverse on demand. Amortized O(1)."
53. **Asteroid Collision idea?**
  - Approach: Stack, collide while top>0 and cur<0. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Stack, collide while top>0 and cur<0. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Stack, collide while top>0 and cur<0. O(n)."
54. **Simplify Path idea?**
  - Approach: Split `/`, stack ignore `.`, pop on `..`. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Split `/`, stack ignore `.`, pop on `..`. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Split `/`, stack ignore `.`, pop on `..`. O(n)."
55. **Queue vs Stack in JS?**
  - Approach: Stack `push/pop`, Queue `push/shift` or head pointer to avoid O(n) shift.
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Stack `push/pop`, Queue `push/shift` or head pointer to avoid O(n) shift. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty input, single bracket/node, unbalanced, deeply nested.
  - Say: "In interview I'd say: Stack `push/pop`, Queue `push/shift` or head pointer to avoid O(n) shift."

### Linked List (56-65)
56. **Reverse Linked List idea?**
  - Approach: `prev=null; next=curr.next; curr.next=prev`. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: `prev=null; next=curr.next; curr.next=prev`. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: `prev=null; next=curr.next; curr.next=prev`. O(n)."
57. **Merge Two Sorted Lists idea?**
  - Approach: Dummy + pick smaller, append rest. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Dummy + pick smaller, append rest. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: Dummy + pick smaller, append rest. O(n)."
58. **Detect Cycle Start idea?**
  - Approach: Meet with fast/slow, then start+meet move together. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Meet with fast/slow, then start+meet move together. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: Meet with fast/slow, then start+meet move together. O(n)."
59. **Remove Nth From End idea?**
  - Approach: Fast n ahead, move both, delete. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Fast n ahead, move both, delete. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: Fast n ahead, move both, delete. O(n)."
60. **Middle of List idea?**
  - Approach: Fast 2x slow, slow = middle. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Fast 2x slow, slow = middle. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: Fast 2x slow, slow = middle. O(n)."
61. **Palindrome Linked List idea?**
  - Approach: Find mid, reverse 2nd half, compare. O(n) O(1).
  - Complexity: O(n); O(1) time; see approach for space.
  - Code: JS idea: Find mid, reverse 2nd half, compare. O(n) O(1). // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: Find mid, reverse 2nd half, compare. O(n) O(1)."
62. **LRU Cache idea?**
  - Approach: Hashmap + doubly linked list, move-to-head on use. O(1).
  - Complexity: O(1) time; see approach for space.
  - Code: JS idea: Hashmap + doubly linked list, move-to-head on use. O(1). // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: Hashmap + doubly linked list, move-to-head on use. O(1)."
63. **Add Two Numbers idea?**
  - Approach: Traverse with carry, dummy head. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Traverse with carry, dummy head. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: Traverse with carry, dummy head. O(n)."
64. **Intersection of Lists idea?**
  - Approach: Two pointers switch heads, meet at intersect. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Two pointers switch heads, meet at intersect. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: Two pointers switch heads, meet at intersect. O(n)."
65. **Singly vs Doubly list?**
  - Approach: Singly next only; doubly prev+next, more memory but O(1) delete given node.
  - Complexity: O(1) time; see approach for space.
  - Code: JS idea: Singly next only; doubly prev+next, more memory but O(1) delete given node. // implement with Map/Set/pointers, test on sample.
  - Edge cases: null head, single node, two nodes, cycle, no intersection.
  - Say: "In interview I'd say: Singly next only; doubly prev+next, more memory but O(1) delete given node."

### Binary Search / Sort (66-75)
66. **Binary Search code idea?**
  - Approach: `while(l<=r){m=(l+r)>>1; compare}`. O(log n).
  - Complexity: O(log n) time; see approach for space.
  - Code: JS idea: `while(l<=r){m=(l+r)>>1; compare}`. O(log n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: `while(l<=r){m=(l+r)>>1; compare}`. O(log n)."
67. **Search Rotated Sorted Array idea?**
  - Approach: Check which half sorted, decide side. O(log n).
  - Complexity: O(log n) time; see approach for space.
  - Code: JS idea: Check which half sorted, decide side. O(log n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: Check which half sorted, decide side. O(log n)."
68. **Find Min Rotated Array idea?**
  - Approach: If `mid>right` go right else left. O(log n).
  - Complexity: O(log n) time; see approach for space.
  - Code: JS idea: If `mid>right` go right else left. O(log n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: If `mid>right` go right else left. O(log n)."
69. **First/Last Position idea?**
  - Approach: Two binary searches for left/right bound. O(log n).
  - Complexity: O(log n) time; see approach for space.
  - Code: JS idea: Two binary searches for left/right bound. O(log n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: Two binary searches for left/right bound. O(log n)."
70. **Sqrt(x) via binary search?**
  - Approach: Search 0..x, `m*m<=x`. O(log n).
  - Complexity: O(log n) time; see approach for space.
  - Code: JS idea: Search 0..x, `m*m<=x`. O(log n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: Search 0..x, `m*m<=x`. O(log n)."
71. **Koko Eating Bananas idea?**
  - Approach: Binary search speed, check hours. O(n log m).
  - Complexity: O(n log m) time; see approach for space.
  - Code: JS idea: Binary search speed, check hours. O(n log m). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: Binary search speed, check hours. O(n log m)."
72. **Merge Intervals idea?**
  - Approach: Sort start, merge if `next.start<=curEnd`. O(n log n).
  - Complexity: O(n log n) time; see approach for space.
  - Code: JS idea: Sort start, merge if `next.start<=curEnd`. O(n log n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: Sort start, merge if `next.start<=curEnd`. O(n log n)."
73. **Insert Interval idea?**
  - Approach: Merge while overlapping, insert. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Merge while overlapping, insert. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: Merge while overlapping, insert. O(n)."
74. **QuickSort vs MergeSort?**
  - Approach: Quick in-place avg O(n log n) unstable; Merge O(n) space stable.
  - Complexity: O(n log n); O(n) time; see approach for space.
  - Code: JS idea: Quick in-place avg O(n log n) unstable; Merge O(n) space stable. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: Quick in-place avg O(n log n) unstable; Merge O(n) space stable."
75. **Binary Search iterative vs recursive?**
  - Approach: Same O(log n); iterative O(1) space avoids stack.
  - Complexity: O(log n); O(1) time; see approach for space.
  - Code: JS idea: Same O(log n); iterative O(1) space avoids stack. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, dupes, rotated pivot at ends, mid overflow, unsorted input.
  - Say: "In interview I'd say: Same O(log n); iterative O(1) space avoids stack."

### BFS/DFS / Tree / Graph (76-85)
76. **DFS vs BFS use?**
  - Approach: DFS path/explore deep (maze, components); BFS shortest unweighted level-order.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: DFS path/explore deep (maze, components); BFS shortest unweighted level-order. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: DFS path/explore deep (maze, components); BFS shortest unweighted level-order."
77. **Invert Binary Tree idea?**
  - Approach: Swap left/right recursively. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Swap left/right recursively. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: Swap left/right recursively. O(n)."
78. **Max Depth Binary Tree idea?**
  - Approach: `1+max(dfs(l),dfs(r))`. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: `1+max(dfs(l),dfs(r))`. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: `1+max(dfs(l),dfs(r))`. O(n)."
79. **Validate BST idea?**
  - Approach: DFS with min/max bounds. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: DFS with min/max bounds. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: DFS with min/max bounds. O(n)."
80. **Level Order Traversal idea?**
  - Approach: Queue BFS per level. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Queue BFS per level. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: Queue BFS per level. O(n)."
81. **Number of Islands idea?**
  - Approach: DFS/BFS flood fill `1`->`0`, count. O(m*n).
  - Complexity: O(m*n) time; see approach for space.
  - Code: JS idea: DFS/BFS flood fill `1`->`0`, count. O(m*n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: DFS/BFS flood fill `1`->`0`, count. O(m*n)."
82. **Clone Graph idea?**
  - Approach: Map old->new + DFS/BFS copy neighbors. O(V+E).
  - Complexity: O(V+E) time; see approach for space.
  - Code: JS idea: Map old->new + DFS/BFS copy neighbors. O(V+E). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: Map old->new + DFS/BFS copy neighbors. O(V+E)."
83. **Course Schedule (cycle) idea?**
  - Approach: Kahn topo / DFS colors; if all visited no cycle. O(V+E).
  - Complexity: O(V+E) time; see approach for space.
  - Code: JS idea: Kahn topo / DFS colors; if all visited no cycle. O(V+E). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: Kahn topo / DFS colors; if all visited no cycle. O(V+E)."
84. **Lowest Common Ancestor BST idea?**
  - Approach: Go left/right or split = answer. O(h).
  - Complexity: O(h) time; see approach for space.
  - Code: JS idea: Go left/right or split = answer. O(h). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: Go left/right or split = answer. O(h)."
85. **Trie insert/search?**
  - Approach: Node children map + end flag; O(L) per word.
  - Complexity: O(L) time; see approach for space.
  - Code: JS idea: Node children map + end flag; O(L) per word. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty tree/graph, single node, skewed tree, disconnected components.
  - Say: "In interview I'd say: Node children map + end flag; O(L) per word."

### 15 Must-Do Codes (86-100)
86. **Two Sum (code)?**
  - Approach: `for(x,i){if(m.has(t-x))return[m.get(t-x),i];m.set(x,i)}` O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: `for(x,i){if(m.has(t-x))return[m.get(t-x),i];m.set(x,i)}` O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: `for(x,i){if(m.has(t-x))return[m.get(t-x),i];m.set(x,i)}` O(n)."
87. **Valid Parentheses (code)?**
  - Approach: Stack + map `) : (`; pop must match. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: Stack + map `) : (`; pop must match. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: Stack + map `) : (`; pop must match. O(n)."
88. **Merge Intervals (code)?**
  - Approach: Sort by 0, push/merge end. O(n log n).
  - Complexity: O(n log n) time; see approach for space.
  - Code: JS idea: Sort by 0, push/merge end. O(n log n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: Sort by 0, push/merge end. O(n log n)."
89. **Best Stock (code)?**
  - Approach: `min=Inf; for(p){min=min(min,p);best=max(best,p-min)}`.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: `min=Inf; for(p){min=min(min,p);best=max(best,p-min)}`. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: `min=Inf; for(p){min=min(min,p);best=max(best,p-min)}`."
90. **Kadane Max Subarray (code)?**
  - Approach: `cur=best=nums[0]; for: cur=max(n,cur+n)` O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: `cur=best=nums[0]; for: cur=max(n,cur+n)` O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: `cur=best=nums[0]; for: cur=max(n,cur+n)` O(n)."
91. **Reverse Linked List (code)?**
  - Approach: `prev=null,cur=head; [cur.next,prev,cur]=[prev,cur,cur.next]`.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: `prev=null,cur=head; [cur.next,prev,cur]=[prev,cur,cur.next]`. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: `prev=null,cur=head; [cur.next,prev,cur]=[prev,cur,cur.next]`."
92. **Cycle Detect (code)?**
  - Approach: `slow=fast=head; while(fast&&fast.next){slow=slow.next;fast=fast.next.next;if(eq)return true}`.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: `slow=fast=head; while(fast&&fast.next){slow=slow.next;fast=fast.next.next;if(eq)return true}`. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: `slow=fast=head; while(fast&&fast.next){slow=slow.next;fast=fast.next.next;if(eq)return true}`."
93. **Binary Search (code)?**
  - Approach: `l=0,r=n-1; while(l<=r){m>>; arr[m]==t?return m: arr[m]<t?l=m+1:r=m-1}`.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: `l=0,r=n-1; while(l<=r){m>>; arr[m]==t?return m: arr[m]<t?l=m+1:r=m-1}`. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: `l=0,r=n-1; while(l<=r){m>>; arr[m]==t?return m: arr[m]<t?l=m+1:r=m-1}`."
94. **Number of Islands (code)?**
  - Approach: DFS 4-dir mark visited; count starts. O(m*n).
  - Complexity: O(m*n) time; see approach for space.
  - Code: JS idea: DFS 4-dir mark visited; count starts. O(m*n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: DFS 4-dir mark visited; count starts. O(m*n)."
95. **Climb Stairs (code)?**
  - Approach: `dp: a=1,b=1; for: [a,b]=[b,a+b]` = fib. O(n) O(1).
  - Complexity: O(n); O(1) time; see approach for space.
  - Code: JS idea: `dp: a=1,b=1; for: [a,b]=[b,a+b]` = fib. O(n) O(1). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: `dp: a=1,b=1; for: [a,b]=[b,a+b]` = fib. O(n) O(1)."
96. **Coin Change (code)?**
  - Approach: `dp[0]=0; dp[i]=min(dp[i-c])+1` O(amount*n).
  - Complexity: O(amount*n) time; see approach for space.
  - Code: JS idea: `dp[0]=0; dp[i]=min(dp[i-c])+1` O(amount*n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: `dp[0]=0; dp[i]=min(dp[i-c])+1` O(amount*n)."
97. **LIS idea?**
  - Approach: DP O(n^2) or patience + binary search O(n log n).
  - Complexity: O(n^2); O(n log n) time; see approach for space.
  - Code: JS idea: DP O(n^2) or patience + binary search O(n log n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: DP O(n^2) or patience + binary search O(n log n)."
98. **House Robber idea?**
  - Approach: `rob/noRob: newRob=max(oldRob,oldNo+nums[i])`. O(n).
  - Complexity: O(n) time; see approach for space.
  - Code: JS idea: `rob/noRob: newRob=max(oldRob,oldNo+nums[i])`. O(n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: `rob/noRob: newRob=max(oldRob,oldNo+nums[i])`. O(n)."
99. **Fibonacci DP idea?**
  - Approach: Memo/iterative `f(n)=f(n-1)+f(n-2)` O(n), naive rec O(2^n).
  - Complexity: O(n); O(2^n) time; see approach for space.
  - Code: JS idea: Memo/iterative `f(n)=f(n-1)+f(n-2)` O(n), naive rec O(2^n). // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: Memo/iterative `f(n)=f(n-1)+f(n-2)` O(n), naive rec O(2^n)."
100. **Debounce vs Throttle code?**
  - Approach: Debounce `clearTimeout+setTimeout`; throttle flag/timestamp gate.
  - Complexity: Linear or log as in approach; space O(1) unless hash/stack used then O(n).
  - Code: JS idea: Debounce `clearTimeout+setTimeout`; throttle flag/timestamp gate. // implement with Map/Set/pointers, test on sample.
  - Edge cases: empty/single, all negative, dupes, amount=0, k larger than input.
  - Say: "In interview I'd say: Debounce `clearTimeout+setTimeout`; throttle flag/timestamp gate."

## System Design - 50 Q&A (101-150)

101. **Monolith vs Microservices for MERN?**
  - Approach: Start monolith; split when teams/scale need independent deploys.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Start monolith; split when teams/scale need independent deploys. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Start monolith; split when teams/scale need independent deploys."
102. **Design URL shortener?**
  - Approach: Hash id (base62) + DB {short->long} + Redis cache + redirect 302.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Hash id (base62) + DB {short->long} + Redis cache + redirect 302. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Hash id (base62) + DB {short->long} + Redis cache + redirect 302."
103. **How to scale Node.js API?**
  - Approach: Stateless + PM2/cluster + LB + Redis cache + read replicas.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Stateless + PM2/cluster + LB + Redis cache + read replicas. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Stateless + PM2/cluster + LB + Redis cache + read replicas."
104. **What is load balancer?**
  - Approach: Distributes traffic (round-robin/least-conn) + health checks.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Distributes traffic (round-robin/least-conn) + health checks. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Distributes traffic (round-robin/least-conn) + health checks."
105. **SQL vs NoSQL for MERN?**
  - Approach: Mongo flexible docs/scale; SQL for joins/ACID transactions.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Mongo flexible docs/scale; SQL for joins/ACID transactions. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Mongo flexible docs/scale; SQL for joins/ACID transactions."
106. **How to design Mongo schema?**
  - Approach: Embed for read-together, reference for large/many; index queries.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Embed for read-together, reference for large/many; index queries. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Embed for read-together, reference for large/many; index queries."
107. **What is indexing?**
  - Approach: B-tree for O(log n) lookup; index filters/sorts, avoid over-index writes.
  - Complexity: O(log n) time; see approach for space.
  - Code: Idea: B-tree for O(log n) lookup; index filters/sorts, avoid over-index writes. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: B-tree for O(log n) lookup; index filters/sorts, avoid over-index writes."
108. **What is sharding vs replication?**
  - Approach: Shard splits data scale writes; replica copies for HA/reads.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Shard splits data scale writes; replica copies for HA/reads. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Shard splits data scale writes; replica copies for HA/reads."
109. **What is caching?**
  - Approach: Store hot data in Redis/CDN with TTL; cache-aside pattern.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Store hot data in Redis/CDN with TTL; cache-aside pattern. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Store hot data in Redis/CDN with TTL; cache-aside pattern."
110. **Redis use cases?**
  - Approach: Session, rate-limit, leaderboard (ZSET), pub/sub, cache.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Session, rate-limit, leaderboard (ZSET), pub/sub, cache. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Session, rate-limit, leaderboard (ZSET), pub/sub, cache."
111. **How JWT auth works?**
  - Approach: Login -> sign JWT -> client sends Bearer -> verify middleware.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Login -> sign JWT -> client sends Bearer -> verify middleware. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Login -> sign JWT -> client sends Bearer -> verify middleware."
112. **Sessions vs JWT?**
  - Approach: Session stateful revocable; JWT stateless scalable, harder revoke (short TTL + refresh).
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Session stateful revocable; JWT stateless scalable, harder revoke (short TTL + refresh). // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Session stateful revocable; JWT stateless scalable, harder revoke (short TTL + refresh)."
113. **Where store JWT in React?**
  - Approach: HttpOnly cookie (XSS-safe); avoid localStorage for access token.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: HttpOnly cookie (XSS-safe); avoid localStorage for access token. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: HttpOnly cookie (XSS-safe); avoid localStorage for access token."
114. **How refresh token flow?**
  - Approach: Short access + long httpOnly refresh; rotate on /refresh.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Short access + long httpOnly refresh; rotate on /refresh. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Short access + long httpOnly refresh; rotate on /refresh."
115. **OAuth2 flow?**
  - Approach: Redirect -> provider login -> code -> exchange token -> fetch profile.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Redirect -> provider login -> code -> exchange token -> fetch profile. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Redirect -> provider login -> code -> exchange token -> fetch profile."
116. **How to paginate large list?**
  - Approach: Cursor (`_id > lastId limit`) over offset for stable perf.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Cursor (`_id > lastId limit`) over offset for stable perf. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Cursor (`_id > lastId limit`) over offset for stable perf."
117. **How to do file upload?**
  - Approach: Client -> S3 presigned URL -> store key in Mongo; CDN serve.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Client -> S3 presigned URL -> store key in Mongo; CDN serve. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Client -> S3 presigned URL -> store key in Mongo; CDN serve."
118. **How to do search (products)?**
  - Approach: Mongo text index for MVP; Elastic/Atlas Search for fuzzy/facets.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Mongo text index for MVP; Elastic/Atlas Search for fuzzy/facets. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Mongo text index for MVP; Elastic/Atlas Search for fuzzy/facets."
119. **Rate limiting design?**
  - Approach: Token bucket in Redis per IP/user, 429 + Retry-After.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Token bucket in Redis per IP/user, 429 + Retry-After. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Token bucket in Redis per IP/user, 429 + Retry-After."
120. **How to handle real-time chat?**
  - Approach: Socket.io rooms + Mongo persist + Redis adapter for multi-node.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Socket.io rooms + Mongo persist + Redis adapter for multi-node. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Socket.io rooms + Mongo persist + Redis adapter for multi-node."
121. **Polling vs SSE vs WebSocket?**
  - Approach: Polling simple, SSE server-push one-way, WS full-duplex real-time.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Polling simple, SSE server-push one-way, WS full-duplex real-time. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Polling simple, SSE server-push one-way, WS full-duplex real-time."
122. **Design Instagram feed?**
  - Approach: Fan-out on write for celebs hybrid; feed service + CDN + cache.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Fan-out on write for celebs hybrid; feed service + CDN + cache. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Fan-out on write for celebs hybrid; feed service + CDN + cache."
123. **Design e-commerce cart/order?**
  - Approach: Cart in Redis/Mongo, order txn in SQL/Mongo txn, queue payment.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Cart in Redis/Mongo, order txn in SQL/Mongo txn, queue payment. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Cart in Redis/Mongo, order txn in SQL/Mongo txn, queue payment."
124. **How to ensure idempotency?**
  - Approach: Client idempotency-key, server dedupe/store result. Safe retries.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Client idempotency-key, server dedupe/store result. Safe retries. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Client idempotency-key, server dedupe/store result. Safe retries."
125. **Message queue use?**
  - Approach: Decouple heavy tasks (email, image) via RabbitMQ/SQS/BullMQ workers.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Decouple heavy tasks (email, image) via RabbitMQ/SQS/BullMQ workers. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Decouple heavy tasks (email, image) via RabbitMQ/SQS/BullMQ workers."
126. **What is CDN?**
  - Approach: Edge cache static assets; lowers latency + origin load.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Edge cache static assets; lowers latency + origin load. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Edge cache static assets; lowers latency + origin load."
127. **CAP theorem?**
  - Approach: Pick 2: Consistency/Availability/Partition tolerance; Mongo CP, Cassandra AP.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Pick 2: Consistency/Availability/Partition tolerance; Mongo CP, Cassandra AP. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Pick 2: Consistency/Availability/Partition tolerance; Mongo CP, Cassandra AP."
128. **What is consistent hashing?**
  - Approach: Ring maps nodes/keys, minimal remap on scale; for caches.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Ring maps nodes/keys, minimal remap on scale; for caches. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Ring maps nodes/keys, minimal remap on scale; for caches."
129. **Horizontal vs vertical scaling?**
  - Approach: Add machines (stateless) vs bigger machine; prefer horizontal.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Add machines (stateless) vs bigger machine; prefer horizontal. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Add machines (stateless) vs bigger machine; prefer horizontal."
130. **How to monitor Node app?**
  - Approach: Health `/health`, Winston logs, Prometheus+Grafana, Sentry, uptime alerts.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Health `/health`, Winston logs, Prometheus+Grafana, Sentry, uptime alerts. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Health `/health`, Winston logs, Prometheus+Grafana, Sentry, uptime alerts."
131. **CI/CD for MERN?**
  - Approach: GitHub Actions lint/test/build -> Docker -> deploy Vercel/Render/EC2.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: GitHub Actions lint/test/build -> Docker -> deploy Vercel/Render/EC2. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: GitHub Actions lint/test/build -> Docker -> deploy Vercel/Render/EC2."
132. **Docker what/why?**
  - Approach: Containerize Node+deps; same env dev/prod, easy scale.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Containerize Node+deps; same env dev/prod, easy scale. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Containerize Node+deps; same env dev/prod, easy scale."
133. **Nginx role?**
  - Approach: Reverse proxy, SSL, static serve, LB to Node upstreams.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Reverse proxy, SSL, static serve, LB to Node upstreams. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Reverse proxy, SSL, static serve, LB to Node upstreams."
134. **How to secure API?**
  - Approach: Helmet, CORS allowlist, validation (zod), rate-limit, sanitize, least-privilege.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Helmet, CORS allowlist, validation (zod), rate-limit, sanitize, least-privilege. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Helmet, CORS allowlist, validation (zod), rate-limit, sanitize, least-privilege."
135. **XSS vs CSRF prevention?**
  - Approach: XSS: escape/CSP/HttpOnly; CSRF: SameSite cookie + CSRF token.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: XSS: escape/CSP/HttpOnly; CSRF: SameSite cookie + CSRF token. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: XSS: escape/CSP/HttpOnly; CSRF: SameSite cookie + CSRF token."
136. **What is N+1 in Mongo/Mongoose?**
  - Approach: Loop populate queries; fix with `$lookup` / single `.populate()`.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Loop populate queries; fix with `$lookup` / single `.populate()`. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Loop populate queries; fix with `$lookup` / single `.populate()`."
137. **How to optimize slow API?**
  - Approach: Profile, add index, cache, paginate, select fields, async workers.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Profile, add index, cache, paginate, select fields, async workers. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Profile, add index, cache, paginate, select fields, async workers."
138. **What is DB transaction?**
  - Approach: Atomic multi-doc ops via Mongo sessions; for order/payment.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Atomic multi-doc ops via Mongo sessions; for order/payment. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Atomic multi-doc ops via Mongo sessions; for order/payment."
139. **How to backup Mongo?**
  - Approach: Atlas snapshots/oplog + mongodump schedule, test restores.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Atlas snapshots/oplog + mongodump schedule, test restores. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Atlas snapshots/oplog + mongodump schedule, test restores."
140. **How to do zero-downtime deploy?**
  - Approach: Blue-green/rolling + health checks + migrate backward-compatible.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Blue-green/rolling + health checks + migrate backward-compatible. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Blue-green/rolling + health checks + migrate backward-compatible."
141. **What is API gateway?**
  - Approach: Single entry: auth, rate-limit, routing to services.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Single entry: auth, rate-limit, routing to services. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Single entry: auth, rate-limit, routing to services."
142. **REST vs GraphQL?**
  - Approach: REST simple cacheable; GraphQL flexible fetch, harder caching/rate-limit.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: REST simple cacheable; GraphQL flexible fetch, harder caching/rate-limit. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: REST simple cacheable; GraphQL flexible fetch, harder caching/rate-limit."
143. **How to version API?**
  - Approach: `/api/v1` + never break; deprecate with headers.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: `/api/v1` + never break; deprecate with headers. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: `/api/v1` + never break; deprecate with headers."
144. **How to handle 10k concurrent?**
  - Approach: LB + auto-scale stateless Node + cache + queue writes + connection pool.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: LB + auto-scale stateless Node + cache + queue writes + connection pool. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: LB + auto-scale stateless Node + cache + queue writes + connection pool."
145. **What is sticky session?**
  - Approach: Pin user to server; avoid via Redis shared session.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: Pin user to server; avoid via Redis shared session. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: Pin user to server; avoid via Redis shared session."
146. **Webhooks design?**
  - Approach: POST event + signature (HMAC), retry with backoff, idempotent receiver.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: POST event + signature (HMAC), retry with backoff, idempotent receiver. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: POST event + signature (HMAC), retry with backoff, idempotent receiver."
147. **How to store passwords?**
  - Approach: bcrypt/argon2 hash + salt; never plain; add pepper/rate-limit.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: bcrypt/argon2 hash + salt; never plain; add pepper/rate-limit. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: bcrypt/argon2 hash + salt; never plain; add pepper/rate-limit."
148. **Env config best practice?**
  - Approach: `.env` + validate, secrets in vault, never commit.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: `.env` + validate, secrets in vault, never commit. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: `.env` + validate, secrets in vault, never commit."
149. **Logging best practice?**
  - Approach: JSON structured, levels, request-id, no PII/secrets.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: JSON structured, levels, request-id, no PII/secrets. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: JSON structured, levels, request-id, no PII/secrets."
150. **Design notification system?**
  - Approach: API -> queue -> workers (push/email/SMS) + prefs + retry/DLQ.
  - Complexity: Bottleneck is DB/network; cache gives O(1) hot path, else O(log n) indexed lookup.
  - Code: Idea: API -> queue -> workers (push/email/SMS) + prefs + retry/DLQ. // e.g. Express middleware / Redis client / indexed Mongo query.
  - Edge cases: cold cache, DB down, hot key, thundering herd, idempotent retry, skewed traffic.
  - Say: "In interview I'd say: API -> queue -> workers (push/email/SMS) + prefs + retry/DLQ."

## Git / HR - 50 Q&A (151-200)

151. **Git init -> push flow?**
  - Approach: `init/add/commit/branch -M main/remote add origin/push -u origin main`.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `init/add/commit/branch -M main/remote add origin/push -u origin main`. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `init/add/commit/branch -M main/remote add origin/push -u origin main`."
152. **Clone vs fork vs pull?**
  - Approach: Clone copy, fork server copy, pull fetch+merge.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Clone copy, fork server copy, pull fetch+merge. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Clone copy, fork server copy, pull fetch+merge."
153. **Add/commit/push meaning?**
  - Approach: Stage, snapshot, upload to remote.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Stage, snapshot, upload to remote. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Stage, snapshot, upload to remote."
154. **Status/log/diff?**
  - Approach: `status` state, `log` history, `diff` changes.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `status` state, `log` history, `diff` changes. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `status` state, `log` history, `diff` changes."
155. **.gitignore for MERN?**
  - Approach: `node_modules/.env/dist/build/coverage`.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `node_modules/.env/dist/build/coverage`. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `node_modules/.env/dist/build/coverage`."
156. **Branch create/switch?**
  - Approach: `checkout -b feat/x` or `switch -c feat/x`; push `-u`.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `checkout -b feat/x` or `switch -c feat/x`; push `-u`. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `checkout -b feat/x` or `switch -c feat/x`; push `-u`."
157. **Merge vs rebase?**
  - Approach: Merge keeps history (merge commit); rebase linear, rewrite — never on shared main.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Merge keeps history (merge commit); rebase linear, rewrite — never on shared main. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Merge keeps history (merge commit); rebase linear, rewrite — never on shared main."
158. **Resolve merge conflict?**
  - Approach: Pull, edit markers, `add/commit`, test, push.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Pull, edit markers, `add/commit`, test, push. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Pull, edit markers, `add/commit`, test, push."
159. **Fetch vs pull?**
  - Approach: Fetch downloads only; pull = fetch+merge.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Fetch downloads only; pull = fetch+merge. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Fetch downloads only; pull = fetch+merge."
160. **Stash use?**
  - Approach: `stash push -m / pop` to save WIP when switching branches.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `stash push -m / pop` to save WIP when switching branches. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `stash push -m / pop` to save WIP when switching branches."
161. **Reset vs revert?**
  - Approach: Reset moves HEAD (local, dangerous); revert new commit undo (safe shared).
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Reset moves HEAD (local, dangerous); revert new commit undo (safe shared). // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Reset moves HEAD (local, dangerous); revert new commit undo (safe shared)."
162. **Amend last commit?**
  - Approach: `commit --amend -m` then `push --force-with-lease` only if private.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `commit --amend -m` then `push --force-with-lease` only if private. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `commit --amend -m` then `push --force-with-lease` only if private."
163. **Cherry-pick?**
  - Approach: Copy one commit to current branch by SHA.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Copy one commit to current branch by SHA. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Copy one commit to current branch by SHA."
164. **Tag/release?**
  - Approach: `tag v1.0.0; push --tags` to mark deploys.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `tag v1.0.0; push --tags` to mark deploys. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `tag v1.0.0; push --tags` to mark deploys."
165. **PR flow?**
  - Approach: Branch -> push -> PR -> review/CI -> squash-merge -> delete branch.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Branch -> push -> PR -> review/CI -> squash-merge -> delete branch. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Branch -> push -> PR -> review/CI -> squash-merge -> delete branch."
166. **Code review checklist?**
  - Approach: Correctness, tests, security, perf, naming, small diff.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Correctness, tests, security, perf, naming, small diff. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Correctness, tests, security, perf, naming, small diff."
167. **Conventional commits?**
  - Approach: `feat:`, `fix:`, `chore:`, `docs:` + scope for changelog.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `feat:`, `fix:`, `chore:`, `docs:` + scope for changelog. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `feat:`, `fix:`, `chore:`, `docs:` + scope for changelog."
168. **Gitflow vs trunk?**
  - Approach: Gitflow develop/release/hotfix; trunk short-lived branches, frequent merge.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Gitflow develop/release/hotfix; trunk short-lived branches, frequent merge. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Gitflow develop/release/hotfix; trunk short-lived branches, frequent merge."
169. **Protect main branch?**
  - Approach: Require PR + approvals + CI pass + no direct push.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Require PR + approvals + CI pass + no direct push. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Require PR + approvals + CI pass + no direct push."
170. **Hotfix flow?**
  - Approach: `hotfix/` from main, fix+test, merge to main+develop, tag.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `hotfix/` from main, fix+test, merge to main+develop, tag. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `hotfix/` from main, fix+test, merge to main+develop, tag."
171. **Undo pushed mistake?**
  - Approach: `revert <sha>` + push; avoid reset/force on shared.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `revert <sha>` + push; avoid reset/force on shared. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `revert <sha>` + push; avoid reset/force on shared."
172. **Squash commits?**
  - Approach: `rebase -i HEAD~n` squash or squash-merge PR for clean history.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: `rebase -i HEAD~n` squash or squash-merge PR for clean history. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: `rebase -i HEAD~n` squash or squash-merge PR for clean history."
173. **Large files in git?**
  - Approach: Don't commit; use S3 + Git LFS if needed.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Don't commit; use S3 + Git LFS if needed. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Don't commit; use S3 + Git LFS if needed."
174. **Mono vs multi repo?**
  - Approach: Mono shared deps/atomic; multi isolated deploys.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Mono shared deps/atomic; multi isolated deploys. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Mono shared deps/atomic; multi isolated deploys."
175. **CI on PR?**
  - Approach: Lint + test + build + preview; block merge on fail.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Run: Lint + test + build + preview; block merge on fail. // verify with `git status` before/after.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Lint + test + build + preview; block merge on fail."
176. **Tell me about yourself?**
  - Approach: 1-yr MERN, 2-3 projects + impact metrics, seeking product team.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — 1-yr MERN, 2-3 projects + impact metrics, seeking product team.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: 1-yr MERN, 2-3 projects + impact metrics, seeking product team."
177. **Why our company?**
  - Approach: Product + stack + scale match; cite feature/release you admire.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Product + stack + scale match; cite feature/release you admire.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Product + stack + scale match; cite feature/release you admire."
178. **Greatest MERN project?**
  - Approach: STAR: problem, MERN + Redis/queue choice, latency/error impact.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — STAR: problem, MERN + Redis/queue choice, latency/error impact.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: STAR: problem, MERN + Redis/queue choice, latency/error impact."
179. **Explain tough bug?**
  - Approach: Repro, logs/bisect, root cause, fix + regression test.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Repro, logs/bisect, root cause, fix + regression test.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Repro, logs/bisect, root cause, fix + regression test."
180. **Tabs vs merge conflict with senior?**
  - Approach: Listen, propose data/test, align on standards, document.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Listen, propose data/test, align on standards, document.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Listen, propose data/test, align on standards, document."
181. **How learn new tech fast?**
  - Approach: Docs -> minimal POC -> integrate -> share notes/PR.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Docs -> minimal POC -> integrate -> share notes/PR.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Docs -> minimal POC -> integrate -> share notes/PR."
182. **Preferred work style?**
  - Approach: Daily async updates, small PRs, ask early after 30-min block.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Daily async updates, small PRs, ask early after 30-min block.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Daily async updates, small PRs, ask early after 30-min block."
183. **Career goals 2yr?**
  - Approach: Mid MERN owning features end-to-end + mentoring.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Mid MERN owning features end-to-end + mentoring.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Mid MERN owning features end-to-end + mentoring."
184. **Why leaving current?**
  - Approach: Seeking larger scale/ownership, no badmouth; grateful framing.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Seeking larger scale/ownership, no badmouth; grateful framing.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Seeking larger scale/ownership, no badmouth; grateful framing."
185. **Strength/weakness?**
  - Approach: Strength shipping + debugging; weakness over-scoping -> now slice MVP.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Strength shipping + debugging; weakness over-scoping -> now slice MVP.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Strength shipping + debugging; weakness over-scoping -> now slice MVP."
186. **How handle deadline pressure?**
  - Approach: Cut scope not quality, communicate risks early, extra tests.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Cut scope not quality, communicate risks early, extra tests.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Cut scope not quality, communicate risks early, extra tests."
187. **How estimate tasks?**
  - Approach: Break subtasks + buffer 20%, clarify unknowns, update on drift.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Break subtasks + buffer 20%, clarify unknowns, update on drift.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Break subtasks + buffer 20%, clarify unknowns, update on drift."
188. **Explain REST to non-tech?**
  - Approach: Menu analogy: client orders (request) kitchen (server) returns dish.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Menu analogy: client orders (request) kitchen (server) returns dish.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Menu analogy: client orders (request) kitchen (server) returns dish."
189. **How debug prod 500?**
  - Approach: Logs/trace-id, repro, recent deploy/flag, fix + rollback + postmortem.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Logs/trace-id, repro, recent deploy/flag, fix + rollback + postmortem.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Logs/trace-id, repro, recent deploy/flag, fix + rollback + postmortem."
190. **How ensure code quality?**
  - Approach: TypeScript, ESLint, tests, PR reviews, edge cases.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — TypeScript, ESLint, tests, PR reviews, edge cases.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: TypeScript, ESLint, tests, PR reviews, edge cases."
191. **Agile experience?**
  - Approach: Sprint planning/standup/retro, Jira, story points, demo.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Sprint planning/standup/retro, Jira, story points, demo.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Sprint planning/standup/retro, Jira, story points, demo."
192. **Remote teamwork?**
  - Approach: Over-communicate async, docs, overlap hours for blockers.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Over-communicate async, docs, overlap hours for blockers.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Over-communicate async, docs, overlap hours for blockers."
193. **Salary expectation?**
  - Approach: Give researched range, prioritize growth/fit, open to discuss.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Give researched range, prioritize growth/fit, open to discuss.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Give researched range, prioritize growth/fit, open to discuss."
194. **Questions to ask interviewer?**
  - Approach: Team stack, on-call, code review, growth, success metrics.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Team stack, on-call, code review, growth, success metrics.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Team stack, on-call, code review, growth, success metrics."
195. **Handle feedback/criticism?**
  - Approach: Thank, clarify, act fast, follow up — example improved PR.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Thank, clarify, act fast, follow up — example improved PR.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Thank, clarify, act fast, follow up — example improved PR."
196. **Side projects?**
  - Approach: Mention deployed link + tech + users; keep code clean.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Mention deployed link + tech + users; keep code clean.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Mention deployed link + tech + users; keep code clean."
197. **Low test coverage legacy?**
  - Approach: Add tests for touched code, critical paths first, CI gate.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Add tests for touched code, critical paths first, CI gate.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Add tests for touched code, critical paths first, CI gate."
198. **Missed deadline story?**
  - Approach: Own it, early flag, replan MVP, process fix (smaller slices).
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Own it, early flag, replan MVP, process fix (smaller slices).
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Own it, early flag, replan MVP, process fix (smaller slices)."
199. **Deploy checklist?**
  - Approach: Tests green, env set, migrate safe, health check, rollback plan.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Tests green, env set, migrate safe, health check, rollback plan.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Tests green, env set, migrate safe, health check, rollback plan."
200. **Why hire you for MERN?**
  - Approach: Ship fast, know Node+React+Mongo patterns, own prod issues end-to-end.
  - Complexity: O(1) command cost; real cost is history-rewrite risk / team coordination.
  - Code: Script: STAR 30s — Ship fast, know Node+React+Mongo patterns, own prod issues end-to-end.
  - Edge cases: private vs shared branch, pushed vs local, conflict, detached HEAD, large files.
  - Say: "In interview I'd say: Ship fast, know Node+React+Mongo patterns, own prod issues end-to-end."
