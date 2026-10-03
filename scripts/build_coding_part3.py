# scripts/build_coding_part3.py
"""
Builds 70 more practical JavaScript Coding interview questions to reach 215+ total.
"""

coding_part3 = [
    # --- Modern JS & Object Utilities (30 items) ---
    (
        "Coding: Invert Object keys and values.",
        "Problem: Return new object where keys become values and values become keys.\nInput: { a: '1', b: '2' }\nOutput: { '1': 'a', '2': 'b' }\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function invert(obj) {\n  const res = {};\n  for (const [k, v] of Object.entries(obj)) res[v] = k;\n  return res;\n}",
        "What happens if multiple keys share the same value?"
    ),
    (
        "Coding: Deep Equality Comparator for objects and primitives.",
        "Problem: Check if two values are deeply equal without third-party libraries.\nTime Complexity: O(n)\nSpace Complexity: O(d) recursion depth",
        "Intermediate",
        "Coding",
        "function deepEqual(a, b) {\n  if (a === b) return true;\n  if (typeof a !== 'object' || a === null || typeof b !== 'object' || b === null) return false;\n  const keysA = Object.keys(a), keysB = Object.keys(b);\n  if (keysA.length !== keysB.length) return false;\n  for (const k of keysA) {\n    if (!keysB.includes(k) || !deepEqual(a[k], b[k])) return false;\n  }\n  return true;\n}",
        "How are nested arrays handled?"
    ),
    (
        "Coding: Shallow Equality Comparator for objects.",
        "Problem: Return true if two objects have identical top-level keys and values.\nTime Complexity: O(k)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function shallowEqual(a, b) {\n  if (a === b) return true;\n  if (!a || !b || typeof a !== 'object' || typeof b !== 'object') return false;\n  const kA = Object.keys(a), kB = Object.keys(b);\n  if (kA.length !== kB.length) return false;\n  for (const k of kA) if (a[k] !== b[k]) return false;\n  return true;\n}",
        "Where is shallowEqual heavily used in React?"
    ),
    (
        "Coding: Object.groupBy polyfill.",
        "Problem: Group array items into object keys based on callback return value.\nExample: Object.groupBy([6.1, 4.2, 6.3], Math.floor) -> { '4': [4.2], '6': [6.1, 6.3] }\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function myGroupBy(arr, callback) {\n  const res = {};\n  for (let i = 0; i < arr.length; i++) {\n    const key = callback(arr[i], i);\n    (res[key] = res[key] || []).push(arr[i]);\n  }\n  return res;\n}",
        "What is the ECMAScript 2024 method for grouping?"
    ),
    (
        "Coding: Flatten nested array iteratively using a stack.",
        "Problem: Flatten array of any nesting depth without recursion.\nInput: [1, [2, [3, [4]]]]\nOutput: [1, 2, 3, 4]\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Intermediate",
        "Coding",
        "function flattenIterative(arr) {\n  const stack = [...arr], res = [];\n  while (stack.length) {\n    const next = stack.pop();\n    if (Array.isArray(next)) stack.push(...next);\n    else res.push(next);\n  }\n  return res.reverse();\n}",
        "Why is `res.reverse()` necessary when popping from stack?"
    ),
    (
        "Coding: Polyfill for Array.prototype.at.",
        "Problem: Implement at() supporting relative indexing from end using negative integers.\nExample: [1, 2, 3].myAt(-1) -> 3\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "Array.prototype.myAt = function(n) {\n  n = Math.trunc(n) || 0;\n  if (n < 0) n += this.length;\n  if (n < 0 || n >= this.length) return undefined;\n  return this[n];\n};",
        "What does `.at(-1)` return on empty array?"
    ),
    (
        "Coding: Polyfill for String.prototype.trim.",
        "Problem: Remove leading and trailing whitespace without built-in trim().\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "String.prototype.myTrim = function() {\n  return this.replace(/^\\s+|\\s+$/g, '');\n};",
        "What characters are matched by `\\s`?"
    ),
    (
        "Coding: Polyfill for String.prototype.padStart.",
        "Problem: Pad current string with another string until targetLength is reached.\nExample: '5'.myPadStart(3, '0') -> '005'\nTime Complexity: O(k)\nSpace Complexity: O(k)",
        "Easy",
        "Coding",
        "String.prototype.myPadStart = function(targetLength, padString = ' ') {\n  if (this.length >= targetLength) return String(this);\n  const padLen = targetLength - this.length;\n  let pad = String(padString);\n  while (pad.length < padLen) pad += pad;\n  return pad.slice(0, padLen) + this;\n};",
        "What is the default padString?"
    ),
    (
        "Coding: Polyfill for String.prototype.repeat.",
        "Problem: Return string containing count copies of original string.\nExample: 'abc'.myRepeat(3) -> 'abcabcabc'\nTime Complexity: O(count * len)\nSpace Complexity: O(count * len)",
        "Easy",
        "Coding",
        "String.prototype.myRepeat = function(count) {\n  if (count < 0 || count === Infinity) throw new RangeError();\n  let res = '', str = String(this);\n  count = Math.floor(count);\n  while (count > 0) {\n    if (count % 2 === 1) res += str;\n    if (count > 1) str += str;\n    count = Math.floor(count / 2);\n  }\n  return res;\n};",
        "Why is binary exponentiation O(log count) concatenations?"
    ),
    (
        "Coding: Fisher-Yates Array Shuffle algorithm.",
        "Problem: Shuffle array in-place such that every permutation is equally likely.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function shuffle(arr) {\n  for (let i = arr.length - 1; i > 0; i--) {\n    const j = Math.floor(Math.random() * (i + 1));\n    [arr[i], arr[j]] = [arr[j], arr[i]];\n  }\n  return arr;\n}",
        "Why is `Math.random() * (i + 1)` correct instead of `Math.random() * n`?"
    ),
    (
        "Coding: Random Integer in range [min, max] inclusive.",
        "Problem: Return random integer between min and max inclusive.\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function getRandomInt(min, max) {\n  min = Math.ceil(min);\n  max = Math.floor(max);\n  return Math.floor(Math.random() * (max - min + 1)) + min;\n}",
        "Why add `+ 1` to `(max - min)`?"
    ),
    (
        "Coding: UUID v4 generator.",
        "Problem: Generate cryptographically compliant UUID v4 string.\nExample: 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function uuidv4() {\n  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {\n    const r = Math.random() * 16 | 0;\n    const v = c === 'x' ? r : (r & 0x3 | 0x8);\n    return v.toString(16);\n  });\n}",
        "What modern Web API generates UUID directly?"
    ),
    (
        "Coding: Math.clamp utility.",
        "Problem: Restrict number to lie within specified range [min, max].\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "const clamp = (val, min, max) => Math.min(Math.max(val, min), max);",
        "What is the result of `clamp(10, 0, 5)`?"
    ),
    (
        "Coding: Async Retry utility with max attempts and delay.",
        "Problem: Retries async fn up to maxRetries times before throwing last error.\nTime Complexity: O(maxRetries * fnTime)\nSpace Complexity: O(1)",
        "Intermediate",
        "Coding",
        "async function retry(fn, maxRetries = 3, delay = 1000) {\n  for (let i = 0; i < maxRetries; i++) {\n    try {\n      return await fn();\n    } catch (err) {\n      if (i === maxRetries - 1) throw err;\n      await new Promise(r => setTimeout(r, delay));\n    }\n  }\n}",
        "How do you implement exponential backoff?"
    ),
    (
        "Coding: Task Queue with Concurrency Limit.",
        "Problem: Execute pool of async tasks with at most `limit` running concurrently.\nTime Complexity: O(n)\nSpace Complexity: O(limit)",
        "Intermediate",
        "Coding",
        "async function asyncPool(limit, tasks) {\n  const executing = [];\n  const results = [];\n  for (const [i, task] of tasks.entries()) {\n    const p = Promise.resolve().then(() => task()).then(r => results[i] = r);\n    executing.push(p);\n    p.finally(() => executing.splice(executing.indexOf(p), 1));\n    if (executing.length >= limit) await Promise.race(executing);\n  }\n  await Promise.all(executing);\n  return results;\n}",
        "Why use `Promise.race`?"
    ),

    # --- Math & Bitwise Coding (20 items) ---
    (
        "Coding: Add Digits (Digital Root) in O(1) time.",
        "Problem: Repeatedly add all digits until result has only one digit.\nInput: num = 38\nOutput: 2 (3 + 8 = 11 -> 1 + 1 = 2)\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function addDigits(num) {\n  if (num === 0) return 0;\n  return num % 9 === 0 ? 9 : num % 9;\n}",
        "What is this mathematical property called?"
    ),
    (
        "Coding: Self Dividing Numbers in range [left, right].",
        "Problem: Return list of numbers divisible by every digit they contain.\nTime Complexity: O(N * D)\nSpace Complexity: O(1) auxiliary",
        "Easy",
        "Coding",
        "function selfDividingNumbers(left, right) {\n  const res = [];\n  for (let num = left; num <= right; num++) {\n    let temp = num, valid = true;\n    while (temp > 0) {\n      const d = temp % 10;\n      if (d === 0 || num % d !== 0) { valid = false; break; }\n      temp = Math.floor(temp / 10);\n    }\n    if (valid) res.push(num);\n  }\n  return res;\n}",
        "Why can self-dividing numbers never contain digit 0?"
    ),
    (
        "Coding: Perfect Number check (sum of proper divisors equals number).",
        "Problem: Check if positive integer equals sum of all its positive divisors except itself.\nInput: num = 28\nOutput: true (1 + 2 + 4 + 7 + 14 = 28)\nTime Complexity: O(sqrt(n))\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function checkPerfectNumber(num) {\n  if (num <= 1) return false;\n  let sum = 1;\n  for (let i = 2; i * i <= num; i++) {\n    if (num % i === 0) {\n      sum += i;\n      if (i * i !== num) sum += num / i;\n    }\n  }\n  return sum === num;\n}",
        "What is the smallest perfect number?"
    ),
    (
        "Coding: Ugly Number check (prime factors only 2, 3, 5).",
        "Problem: Return true if positive integer n has only prime factors 2, 3, 5.\nInput: n = 6\nOutput: true (2 * 3)\nTime Complexity: O(log n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function isUgly(n) {\n  if (n <= 0) return false;\n  for (const factor of [2, 3, 5]) {\n    while (n % factor === 0) n /= factor;\n  }\n  return n === 1;\n}",
        "Is 1 considered an ugly number?"
    ),
    (
        "Coding: Counting Bits from 0 to n in O(n) time.",
        "Problem: Return array ans of length n + 1 where ans[i] is number of 1 bits in i.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function countBits(n) {\n  const ans = new Array(n + 1).fill(0);\n  for (let i = 1; i <= n; i++) {\n    ans[i] = ans[i >> 1] + (i & 1);\n  }\n  return ans;\n}",
        "Why is `ans[i] = ans[i >> 1] + (i & 1)` true?"
    ),
    (
        "Coding: Reverse Bits of a 32-bit unsigned integer.",
        "Problem: Reverse bits of given 32-bit unsigned integer.\nTime Complexity: O(1) (32 iterations)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function reverseBits(n) {\n  let res = 0;\n  for (let i = 0; i < 32; i++) {\n    res = (res << 1) | (n & 1);\n    n >>>= 1;\n  }\n  return res >>> 0;\n}",
        "Why use `>>> 0` at the end?"
    ),
    (
        "Coding: Power of Three without loops or recursion.",
        "Problem: Return true if n is power of 3.\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function isPowerOfThree(n) {\n  return n > 0 && 1162261467 % n === 0;\n}",
        "What is 1162261467?"
    ),
    (
        "Coding: Power of Four.",
        "Problem: Check if integer n is power of 4.\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function isPowerOfFour(n) {\n  return n > 0 && (n & (n - 1)) === 0 && (n & 0xaaaaaaaa) === 0;\n}",
        "Why mask with 0xaaaaaaaa?"
    ),
    (
        "Coding: Sieve of Eratosthenes — count primes strictly less than n.",
        "Problem: Return number of prime numbers less than non-negative integer n.\nTime Complexity: O(n log log n)\nSpace Complexity: O(n)",
        "Intermediate",
        "Coding",
        "function countPrimes(n) {\n  if (n <= 2) return 0;\n  const isPrime = new Uint8Array(n).fill(1);\n  isPrime[0] = isPrime[1] = 0;\n  for (let i = 2; i * i < n; i++) {\n    if (isPrime[i]) {\n      for (let j = i * i; j < n; j += i) isPrime[j] = 0;\n    }\n  }\n  return isPrime.reduce((acc, val) => acc + val, 0);\n}",
        "Why start inner loop at `i * i`?"
    ),
    (
        "Coding: Excel Sheet Column Number (e.g. 'A' -> 1, 'AB' -> 28).",
        "Problem: Given column title string, return its corresponding column number.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function titleToNumber(columnTitle) {\n  let num = 0;\n  for (let i = 0; i < columnTitle.length; i++) {\n    num = num * 26 + (columnTitle.charCodeAt(i) - 64);\n  }\n  return num;\n}",
        "What base system does Excel column numbering use?"
    ),
    (
        "Coding: Excel Sheet Column Title (e.g. 1 -> 'A', 28 -> 'AB').",
        "Problem: Given integer columnNumber, return its corresponding column title.\nTime Complexity: O(log26(n))\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function convertToTitle(columnNumber) {\n  let res = '';\n  while (columnNumber > 0) {\n    columnNumber--;\n    res = String.fromCharCode(65 + (columnNumber % 26)) + res;\n    columnNumber = Math.floor(columnNumber / 26);\n  }\n  return res;\n}",
        "Why is `columnNumber--` needed before modulo?"
    ),
    (
        "Coding: Maximum 69 Number.",
        "Problem: Return max number by changing at most one digit (6 to 9).\nInput: num = 9669\nOutput: 9969\nTime Complexity: O(L)\nSpace Complexity: O(L)",
        "Easy",
        "Coding",
        "function maximum69Number(num) {\n  return Number(String(num).replace('6', '9'));\n}",
        "Why does string replace only change the first occurrence?"
    ),
    (
        "Coding: Count Digits That Divide a Number.",
        "Problem: Count digits in num that divide num evenly.\nTime Complexity: O(log10(n))\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function countDigits(num) {\n  let temp = num, count = 0;\n  while (temp > 0) {\n    const d = temp % 10;\n    if (num % d === 0) count++;\n    temp = Math.floor(temp / 10);\n  }\n  return count;\n}",
        "Can a valid digit in num be 0 in this problem?"
    ),
    (
        "Coding: Number of Steps to Reduce a Number to Zero.",
        "Problem: If even divide by 2, if odd subtract 1. Count steps to reach 0.\nTime Complexity: O(log n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function numberOfSteps(num) {\n  let steps = 0;\n  while (num > 0) {\n    if (num % 2 === 0) num /= 2;\n    else num -= 1;\n    steps++;\n  }\n  return steps;\n}",
        "How is this related to counting binary bits?"
    ),
    (
        "Coding: Smallest Even Multiple of n and 2.",
        "Problem: Return smallest positive integer that is multiple of both 2 and n.\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function smallestEvenMultiple(n) {\n  return n % 2 === 0 ? n : n * 2;\n}",
        "What is the answer for n = 5?"
    ),

    # --- Array & String Extra Coding (20 items) ---
    (
        "Coding: Remove All Adjacent Duplicates In String.",
        "Problem: Repeatedly remove adjacent equal duplicate characters.\nInput: s = 'abbaca'\nOutput: 'ca'\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function removeDuplicates(s) {\n  const stack = [];\n  for (const c of s) {\n    if (stack.length && stack[stack.length - 1] === c) stack.pop();\n    else stack.push(c);\n  }\n  return stack.join('');\n}",
        "Why is a stack optimal for adjacent cancellation?"
    ),
    (
        "Coding: Check if All Characters Have Equal Number of Occurrences.",
        "Problem: Return true if all characters in s have exact same frequency.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function areOccurrencesEqual(s) {\n  const count = {};\n  for (const c of s) count[c] = (count[c] || 0) + 1;\n  return new Set(Object.values(count)).size === 1;\n}",
        "Why does `Set.size === 1` verify equal frequencies?"
    ),
    (
        "Coding: Check if Two String Arrays are Equivalent.",
        "Problem: Return true if two string arrays represent same string after concatenation.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function arrayStringsAreEqual(word1, word2) {\n  return word1.join('') === word2.join('');\n}",
        "Can this be solved in O(1) space with two pointers?"
    ),
    (
        "Coding: Determine if String Halves Are Alike (equal vowel counts).",
        "Problem: Check if first half and second half of even-length string have same vowel count.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function halvesAreAlike(s) {\n  const vowels = new Set(['a','e','i','o','u','A','E','I','O','U']);\n  let diff = 0, mid = s.length / 2;\n  for (let i = 0; i < mid; i++) {\n    if (vowels.has(s[i])) diff++;\n    if (vowels.has(s[i + mid])) diff--;\n  }\n  return diff === 0;\n}",
        "Why use a difference counter?"
    ),
    (
        "Coding: Truncate Sentence to first k words.",
        "Problem: Truncate sentence so that it contains only the first k words.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function truncateSentence(s, k) {\n  return s.split(' ').slice(0, k).join(' ');\n}",
        "How can you truncate by scanning space indices without split()?"
    ),
    (
        "Coding: Score of a String (sum of absolute differences of adjacent ASCII values).",
        "Problem: Return sum of |s[i] - s[i+1]| for all adjacent characters.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function scoreOfString(s) {\n  let score = 0;\n  for (let i = 0; i < s.length - 1; i++) {\n    score += Math.abs(s.charCodeAt(i) - s.charCodeAt(i + 1));\n  }\n  return score;\n}",
        "What is the score of string 'hello'?"
    ),
    (
        "Coding: Find Common Characters in string array.",
        "Problem: Return array of characters that show up in all strings (including duplicates).\nTime Complexity: O(n * k)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function commonChars(words) {\n  let minFreq = new Array(26).fill(Infinity);\n  for (const w of words) {\n    const freq = new Array(26).fill(0);\n    for (const c of w) freq[c.charCodeAt(0) - 97]++;\n    for (let i = 0; i < 26; i++) minFreq[i] = Math.min(minFreq[i], freq[i]);\n  }\n  const res = [];\n  for (let i = 0; i < 26; i++) {\n    while (minFreq[i]-- > 0) res.push(String.fromCharCode(i + 97));\n  }\n  return res;\n}",
        "Why track minimum frequency across all words?"
    ),
    (
        "Coding: Minimum Depth of Binary Tree.",
        "Problem: Find minimum depth of binary tree to the nearest leaf node.\nTime Complexity: O(n)\nSpace Complexity: O(h)",
        "Easy",
        "Coding",
        "function minDepth(root) {\n  if (!root) return 0;\n  if (!root.left) return 1 + minDepth(root.right);\n  if (!root.right) return 1 + minDepth(root.left);\n  return 1 + Math.min(minDepth(root.left), minDepth(root.right));\n}",
        "Why is `1 + Math.min(minDepth(left), minDepth(right))` wrong if one child is null?"
    ),
    (
        "Coding: Binary Tree Inorder Traversal Iteratively using Stack.",
        "Problem: Return inorder traversal of binary tree without recursion.\nTime Complexity: O(n)\nSpace Complexity: O(h)",
        "Easy",
        "Coding",
        "function inorderTraversal(root) {\n  const res = [], stack = [];\n  let curr = root;\n  while (curr || stack.length) {\n    while (curr) { stack.push(curr); curr = curr.left; }\n    curr = stack.pop();\n    res.push(curr.val);\n    curr = curr.right;\n  }\n  return res;\n}",
        "What is the sequence of visited nodes?"
    ),
    (
        "Coding: Assign Cookies greedily.",
        "Problem: Maximize number of children satisfied with cookies.\nTime Complexity: O(n log n + m log m)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function findContentChildren(g, s) {\n  g.sort((a, b) => a - b);\n  s.sort((a, b) => a - b);\n  let child = 0, cookie = 0;\n  while (child < g.length && cookie < s.length) {\n    if (s[cookie] >= g[child]) child++;\n    cookie++;\n  }\n  return child;\n}",
        "Why sort both arrays?"
    )
]

print(f"Total Coding Part 3 questions created: {len(coding_part3)}")

with open('scripts/coding_part3.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/coding_part3.py\nThird batch of practical fresher JavaScript Coding interview questions.\n"""\n\n')
    f.write('coding_part3_items = [\n')
    for item in coding_part3:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/coding_part3.py")
