# scripts/build_coding_part4.py
"""
Builds 27 more practical JavaScript Coding interview questions to reach 215+ total.
"""

coding_part4 = [
    (
        "Coding: Implement a polyfill for Array.prototype.indexOf.",
        "Problem: Return the first index at which element can be found or -1.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "Array.prototype.myIndexOf = function(searchElement, fromIndex = 0) {\n  let start = fromIndex >= 0 ? fromIndex : Math.max(0, this.length + fromIndex);\n  for (let i = start; i < this.length; i++) {\n    if (this[i] === searchElement) return i;\n  }\n  return -1;\n};",
        "What happens if fromIndex is negative?"
    ),
    (
        "Coding: Implement a polyfill for Array.prototype.lastIndexOf.",
        "Problem: Return the last index at which element can be found or -1.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "Array.prototype.myLastIndexOf = function(searchElement, fromIndex = this.length - 1) {\n  let start = fromIndex >= 0 ? Math.min(fromIndex, this.length - 1) : this.length + fromIndex;\n  for (let i = start; i >= 0; i--) {\n    if (this[i] === searchElement) return i;\n  }\n  return -1;\n};",
        "Does search proceed forwards or backwards?"
    ),
    (
        "Coding: Implement a polyfill for String.prototype.endsWith.",
        "Problem: Determine whether a string ends with the characters of a specified string.\nTime Complexity: O(k)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "String.prototype.myEndsWith = function(searchString, endPosition = this.length) {\n  const pos = Math.min(Math.max(0, endPosition), this.length);\n  const start = pos - searchString.length;\n  if (start < 0) return false;\n  return this.substring(start, pos) === searchString;\n};",
        "What is the default endPosition?"
    ),
    (
        "Coding: Implement a polyfill for String.prototype.startsWith.",
        "Problem: Determine whether a string begins with the characters of a specified string.\nTime Complexity: O(k)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "String.prototype.myStartsWith = function(searchString, position = 0) {\n  const pos = Math.max(0, position);\n  return this.substring(pos, pos + searchString.length) === searchString;\n};",
        "What is the return type?"
    ),
    (
        "Coding: Implement Function.prototype.bind with 'new' operator support.",
        "Problem: Polyfill bind that correctly binds `this` and supports instantiating with `new`.\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Advanced",
        "Coding",
        "Function.prototype.myFullBind = function(context, ...bindArgs) {\n  const fn = this;\n  function bound(...callArgs) {\n    const isNew = this instanceof bound;\n    return fn.apply(isNew ? this : context, [...bindArgs, ...callArgs]);\n  }\n  bound.prototype = Object.create(fn.prototype);\n  return bound;\n};",
        "Why is `this instanceof bound` checked?"
    ),
    (
        "Coding: Implement Object.entries polyfill.",
        "Problem: Return array of given object's own enumerable string-keyed property [key, value] pairs.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function myObjectEntries(obj) {\n  const res = [];\n  for (const k of Object.keys(obj)) {\n    if (Object.prototype.hasOwnProperty.call(obj, k)) res.push([k, obj[k]]);\n  }\n  return res;\n}",
        "Does Object.entries include inherited prototype properties?"
    ),
    (
        "Coding: Implement Object.values polyfill.",
        "Problem: Return array of given object's own enumerable string-keyed property values.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function myObjectValues(obj) {\n  return Object.keys(obj).map(k => obj[k]);\n}",
        "Does Object.values preserve numeric property ordering?"
    ),
    (
        "Coding: Implement Object.fromEntries polyfill.",
        "Problem: Transform list of key-value pairs into an object.\nExample: [['a', 1], ['b', 2]] -> { a: 1, b: 2 }\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function myObjectFromEntries(iterable) {\n  const obj = {};\n  for (const [k, v] of iterable) obj[k] = v;\n  return obj;\n}",
        "Can this accept a Map as input?"
    ),
    (
        "Coding: Convert snake_case string to camelCase.",
        "Problem: Convert 'hello_world_variable' to 'helloWorldVariable'.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function snakeToCamel(str) {\n  return str.replace(/_([a-z])/g, (_, letter) => letter.toUpperCase());\n}",
        "What does the regex capture group match?"
    ),
    (
        "Coding: Convert camelCase string to snake_case.",
        "Problem: Convert 'helloWorldVariable' to 'hello_world_variable'.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function camelToSnake(str) {\n  return str.replace(/[A-Z]/g, letter => `_${letter.toLowerCase()}`);\n}",
        "How do you handle consecutive uppercase letters?"
    ),
    (
        "Coding: Format number as currency (e.g. 1234567.89 -> '$1,234,567.89').",
        "Problem: Format number with commas for thousands and 2 decimal places.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function formatCurrency(num) {\n  return '$' + num.toFixed(2).replace(/\\B(?=(\\d{3})+(?!\\d))/g, ',');\n}",
        "What does `\\B` match in regex?"
    ),
    (
        "Coding: Truncate string with ellipsis if length exceeds limit.",
        "Problem: Truncate string and append '...' if length > maxLen.\nExample: truncate('Hello World', 8) -> 'Hello...'\nTime Complexity: O(1)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function truncate(str, maxLen) {\n  if (str.length <= maxLen) return str;\n  return str.slice(0, maxLen - 3) + '...';\n}",
        "What happens if maxLen <= 3?"
    ),
    (
        "Coding: Count vowels and consonants in a string.",
        "Problem: Return { vowels, consonants } count for alphanumeric string.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function countLetters(str) {\n  let vowels = 0, consonants = 0;\n  for (const c of str.toLowerCase()) {\n    if (/[a-z]/.test(c)) {\n      if ('aeiou'.includes(c)) vowels++;\n      else consonants++;\n    }\n  }\n  return { vowels, consonants };\n}",
        "How are digits and spaces ignored?"
    ),
    (
        "Coding: Check if a string contains balanced brackets of type () only.",
        "Problem: Return true if all parentheses are balanced.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function isBalanced(str) {\n  let count = 0;\n  for (const c of str) {\n    if (c === '(') count++;\n    else if (c === ')') count--;\n    if (count < 0) return false;\n  }\n  return count === 0;\n}",
        "Why is `count < 0` an early exit condition?"
    ),
    (
        "Coding: Capitalize First Letter of Each Word in a sentence.",
        "Problem: Convert 'the quick brown fox' to 'The Quick Brown Fox'.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function titleCase(str) {\n  return str.replace(/\\b[a-z]/g, c => c.toUpperCase());\n}",
        "What does `\\b` match in regex?"
    ),
    (
        "Coding: Find the longest word in a sentence.",
        "Problem: Return the longest word in string.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function findLongestWord(str) {\n  const words = str.match(/\\w+/g) || [];\n  let longest = '';\n  for (const w of words) {\n    if (w.length > longest.length) longest = w;\n  }\n  return longest;\n}",
        "What happens if two words share the longest length?"
    ),
    (
        "Coding: Find all prime numbers up to n.",
        "Problem: Return array of all primes <= n using Sieve of Eratosthenes.\nTime Complexity: O(n log log n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function getPrimes(n) {\n  const isPrime = new Array(n + 1).fill(true);\n  isPrime[0] = isPrime[1] = false;\n  for (let i = 2; i * i <= n; i++) {\n    if (isPrime[i]) {\n      for (let j = i * i; j <= n; j += i) isPrime[j] = false;\n    }\n  }\n  const primes = [];\n  for (let i = 2; i <= n; i++) if (isPrime[i]) primes.push(i);\n  return primes;\n}",
        "What is the first prime number?"
    ),
    (
        "Coding: Calculate Power x^n (Binary Exponentiation).",
        "Problem: Implement pow(x, n) in O(log n) time.\nTime Complexity: O(log n)\nSpace Complexity: O(1)",
        "Intermediate",
        "Coding",
        "function myPow(x, n) {\n  if (n === 0) return 1;\n  let exp = Math.abs(n), base = x, res = 1;\n  while (exp > 0) {\n    if (exp % 2 === 1) res *= base;\n    base *= base;\n    exp = Math.floor(exp / 2);\n  }\n  return n < 0 ? 1 / res : res;\n}",
        "How is negative exponent handled?"
    ),
    (
        "Coding: Convert decimal number to binary string without toString(2).",
        "Problem: Convert positive integer to binary string.\nTime Complexity: O(log n)\nSpace Complexity: O(log n)",
        "Easy",
        "Coding",
        "function toBinary(n) {\n  if (n === 0) return '0';\n  let res = '';\n  while (n > 0) {\n    res = (n % 2) + res;\n    n = Math.floor(n / 2);\n  }\n  return res;\n}",
        "What is the binary representation of 13?"
    ),
    (
        "Coding: Convert binary string to decimal integer without parseInt(str, 2).",
        "Problem: Convert binary string to decimal integer.\nTime Complexity: O(n)\nSpace Complexity: O(1)",
        "Easy",
        "Coding",
        "function binaryToDecimal(bStr) {\n  let num = 0;\n  for (let i = 0; i < bStr.length; i++) {\n    num = num * 2 + Number(bStr[i]);\n  }\n  return num;\n}",
        "What is the decimal value of '1101'?"
    ),
    (
        "Coding: Check if two arrays contain the same elements regardless of order.",
        "Problem: Return true if arr1 and arr2 are permutations of each other.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function areArraysEqual(arr1, arr2) {\n  if (arr1.length !== arr2.length) return false;\n  const count = new Map();\n  for (const x of arr1) count.set(x, (count.get(x) || 0) + 1);\n  for (const x of arr2) {\n    if (!count.has(x) || count.get(x) === 0) return false;\n    count.set(x, count.get(x) - 1);\n  }\n  return true;\n}",
        "Why use Map instead of sorting?"
    ),
    (
        "Coding: Remove falsy values from array (compact).",
        "Problem: Filter out false, null, 0, '', undefined, and NaN.\nTime Complexity: O(n)\nSpace Complexity: O(n)",
        "Easy",
        "Coding",
        "function compact(arr) {\n  return arr.filter(Boolean);\n}",
        "Why does `filter(Boolean)` filter out all falsy values?"
    ),
    (
        "Coding: Get difference between two arrays (elements in A not in B).",
        "Problem: Return array of elements present in a but not in b.\nTime Complexity: O(n + m)\nSpace Complexity: O(m)",
        "Easy",
        "Coding",
        "function difference(a, b) {\n  const setB = new Set(b);\n  return a.filter(x => !setB.has(x));\n}",
        "What is the time complexity of Set.has()?"
    ),
    (
        "Coding: Get symmetric difference between two arrays.",
        "Problem: Return elements present in either array but not in both.\nTime Complexity: O(n + m)\nSpace Complexity: O(n + m)",
        "Easy",
        "Coding",
        "function symmetricDifference(a, b) {\n  const setA = new Set(a), setB = new Set(b);\n  return [...a.filter(x => !setB.has(x)), ...b.filter(x => !setA.has(x))];\n}",
        "What is symmetric difference of [1, 2] and [2, 3]?"
    ),
    (
        "Coding: Calculate Levenshtein Distance (Edit Distance) between two strings.",
        "Problem: Return minimum operations (insert, delete, substitute) to convert s1 to s2.\nTime Complexity: O(m * n)\nSpace Complexity: O(n)",
        "Intermediate",
        "Coding",
        "function minDistance(s1, s2) {\n  const m = s1.length, n = s2.length;\n  let dp = Array.from({ length: n + 1 }, (_, i) => i);\n  for (let i = 1; i <= m; i++) {\n    const next = [i];\n    for (let j = 1; j <= n; j++) {\n      if (s1[i - 1] === s2[j - 1]) next[j] = dp[j - 1];\n      else next[j] = 1 + Math.min(dp[j], next[j - 1], dp[j - 1]);\n    }\n    dp = next;\n  }\n  return dp[n];\n}",
        "How is space optimized from O(m * n) to O(n)?"
    ),
    (
        "Coding: Minimum Path Sum in 2D Grid.",
        "Problem: Find path from top-left to bottom-right minimizing sum of numbers along path.\nTime Complexity: O(m * n)\nSpace Complexity: O(n)",
        "Intermediate",
        "Coding",
        "function minPathSum(grid) {\n  const m = grid.length, n = grid[0].length;\n  const dp = new Array(n).fill(Infinity);\n  dp[0] = 0;\n  for (let r = 0; r < m; r++) {\n    dp[0] += grid[r][0];\n    for (let c = 1; c < n; c++) {\n      dp[c] = grid[r][c] + Math.min(dp[c], dp[c - 1]);\n    }\n  }\n  return dp[n - 1];\n}",
        "What are the allowed movements at each cell?"
    ),
    (
        "Coding: Implement a simple LRU (Least Recently Used) Cache.",
        "Problem: Design data structure supporting get(key) and put(key, value) in O(1) time.\nTime Complexity: O(1) get & put\nSpace Complexity: O(capacity)",
        "Intermediate",
        "Coding",
        "class LRUCache {\n  constructor(capacity) {\n    this.capacity = capacity;\n    this.cache = new Map();\n  }\n  get(key) {\n    if (!this.cache.has(key)) return -1;\n    const val = this.cache.get(key);\n    this.cache.delete(key);\n    this.cache.set(key, val);\n    return val;\n  }\n  put(key, val) {\n    if (this.cache.has(key)) this.cache.delete(key);\n    this.cache.set(key, val);\n    if (this.cache.size > this.capacity) {\n      const oldestKey = this.cache.keys().next().value;\n      this.cache.delete(oldestKey);\n    }\n  }\n}",
        "Why does JavaScript Map preserve key insertion order?"
    )
]

print(f"Total Coding Part 4 questions created: {len(coding_part4)}")

with open('scripts/coding_part4.py', 'w', encoding='utf-8') as f:
    f.write('"""\nscripts/coding_part4.py\nFourth batch of practical fresher JavaScript Coding interview questions.\n"""\n\n')
    f.write('coding_part4_items = [\n')
    for item in coding_part4:
        f.write(f"    {repr(item)},\n")
    f.write(']\n')

print("Saved to scripts/coding_part4.py")
