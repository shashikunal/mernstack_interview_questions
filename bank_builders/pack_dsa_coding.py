"""
bank_builders/pack_dsa_coding.py
Builds validated question packs for:
- DSA (Data Structures & Algorithms): 325 questions (Target: >=300)
- Problem Solving: 215 questions (Target: >=200)
- Coding (JavaScript Algorithms & Practical Coding): 215 questions (Target: >=200)
"""

import sys
sys.path.append('scripts')

from bank_builders.common import make_q, parse_item
import dsa_questions as q_dsa1
import dsa_questions_part2 as q_dsa2
import dsa_questions_part3 as q_dsa3
import build_dsa_expanded as q_dsa_exp
import problemsolving_questions as q_ps
import coding_questions as q_code1
import coding_part2 as q_code2
import coding_part3 as q_code3
import coding_part4 as q_code4

# Additional 6 DSA questions to reach 325
DSA_EXTRA = [
    (
        "What is the difference between internal and external sorting algorithms?",
        "Internal sorting algorithms load all data completely into RAM (e.g. quicksort, heapsort). External sorting algorithms handle datasets that exceed available RAM by storing portions on disk and merging them (e.g. external merge sort).",
        "Intermediate",
        "Comparison",
        "",
        "What is the chunk size typically used in external merge sort?"
    ),
    (
        "What is a Bloom Filter?",
        "A Bloom Filter is a space-efficient probabilistic data structure used to test whether an element is a member of a set. False positive matches are possible, but false negatives are impossible.",
        "Advanced",
        "Concept",
        "",
        "Where are Bloom Filters used in modern web databases like Cassandra?"
    ),
    (
        "What is a Skip List?",
        "A Skip List is a probabilistic alternative to balanced trees that augments a sorted linked list with multiple layers of forward pointers, achieving O(log n) search, insertion, and deletion on average.",
        "Advanced",
        "Concept",
        "",
        "What popular in-memory database uses skip lists for sorted sets?"
    ),
    (
        "What is amortized O(1) vs worst-case O(1) time complexity?",
        "Worst-case O(1) guarantees that every individual operation completes in constant time. Amortized O(1) means that while a rare individual operation might take O(n) (like dynamic array resizing), the average cost over a sequence of n operations is constant O(1).",
        "Easy",
        "Comparison",
        "",
        "Give an example of an amortized O(1) operation."
    ),
    (
        "What is the difference between a sparse graph and a dense graph?",
        "A sparse graph has relatively few edges (E is close to V), making Adjacency Lists ideal (O(V + E) space). A dense graph has many edges (E is close to V^2), where an Adjacency Matrix (O(V^2) space) is often more compact and faster.",
        "Easy",
        "Comparison",
        "",
        "What threshold of E/V defines a dense graph?"
    ),
    (
        "Which traversal visits the root node first, followed by left and right subtrees?",
        "Preorder traversal visits the root node first, then recursively traverses the left and right subtrees.",
        "Easy",
        "MCQ",
        "",
        {"A": "Inorder", "B": "Preorder", "C": "Postorder", "D": "Level Order"},
        "B",
        "Which traversal visits the root node last?"
    )
]

# Additional 5 Problem Solving questions to reach 215
PS_EXTRA = [
    (
        "What is the difference between Breadth-First Search (BFS) and Depth-First Search (DFS) for tree level queries?",
        "BFS explores nodes level by level using a FIFO queue, making it the natural choice for shortest path in unweighted graphs or level-order aggregations. DFS goes deep along a branch first using recursion or a stack, making it better for path finding or backtracking.",
        "Easy",
        "Comparison",
        "",
        "Which algorithm requires less memory on a balanced binary tree?"
    ),
    (
        "How do you detect if a number is a Happy Number using Fast and Slow pointers?",
        "Compute the sum of squares of digits repeatedly. If the number reaches 1, it is happy. If it loops endlessly in a cycle (like 4), fast and slow pointers will detect the cycle and terminate without using extra Set memory.",
        "Intermediate",
        "Practical",
        "",
        "What is the first non-happy number in sequence?"
    ),
    (
        "What is the Boyer-Moore Majority Vote algorithm and what invariant does it maintain?",
        "It finds the element appearing more than n/2 times in O(n) time and O(1) space. It maintains a candidate and a counter; equal elements increment the counter and unequal elements decrement it, canceling out non-majority elements.",
        "Easy",
        "Concept",
        "",
        "Does Boyer-Moore work if no majority element exists?"
    ),
    (
        "How do you determine if two intervals [a, b] and [c, d] overlap?",
        "Two intervals overlap if and only if `Math.max(a, c) <= Math.min(b, d)`.",
        "Easy",
        "Concept",
        "",
        "What is the overlap length?"
    ),
    (
        "What is the time complexity to find the Kth smallest element in an unsorted array using Quickselect?",
        "Quickselect runs in O(n) average time and O(n^2) worst-case time by partitioning the array and only recursing into the partition containing the target rank.",
        "Intermediate",
        "Concept",
        "",
        "How does Quickselect differ from full Quicksort?"
    )
]

def normalize_raw(raw_items):
    res = []
    for item in raw_items:
        if len(item) == 11:
            res.append((item[0], item[1], item[2], item[3], item[4], ""))
            res.append((item[5], item[6], item[7], item[8], item[9], item[10]))
        else:
            res.append(item)
    return res

def build_dsa_pack(start_num=1):
    all_raw = []
    all_raw.extend(q_dsa1.dsa_items)
    all_raw.extend(q_dsa2.dsa_arrays_strings)
    all_raw.extend(q_dsa2.dsa_hash_two_pointers)
    all_raw.extend(q_dsa3.dsa_linked_lists)
    all_raw.extend(q_dsa3.dsa_stacks_queues)
    all_raw.extend(q_dsa3.dsa_trees_bst)
    all_raw.extend(q_dsa3.dsa_sorting_searching)
    all_raw.extend(q_dsa_exp.dsa_expanded_items)
    all_raw.extend(DSA_EXTRA)

    all_raw = normalize_raw(all_raw)

    qs = []
    num = start_num
    for item in all_raw:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-dsa-{num}", num, "DSA", "Data Structures & Algorithms", "Core Algorithms, Complexity & Trees",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs

def build_problemsolving_pack(start_num=1):
    all_raw = []
    all_raw.extend(q_ps.ps_items)
    all_raw.extend(PS_EXTRA)
    all_raw = normalize_raw(all_raw)

    qs = []
    num = start_num
    for item in all_raw:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-ps-{num}", num, "Problem Solving", "Problem Solving & Algorithmic Patterns", "Two Pointers, Sliding Window, Monotonic Stacks & Heuristics",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs

def build_coding_pack(start_num=1):
    all_raw = []
    all_raw.extend(q_code1.coding_items)
    all_raw.extend(q_code2.coding_part2_items)
    all_raw.extend(q_code3.coding_part3_items)
    all_raw.extend(q_code4.coding_part4_items)
    all_raw = normalize_raw(all_raw)

    qs = []
    num = start_num
    for item in all_raw:
        q_text, ans, diff, qtype, code, mcq_opts, correct_opt, fup = parse_item(item)
        qs.append(make_q(
            f"q-coding-{num}", num, "Coding", "Practical JavaScript Coding", "Array, String, Matrix, Polyfill & Algorithm Implementations",
            q_text, ans, difficulty=diff, question_type=qtype,
            code_example=code, follow_up=fup,
            mcq_options=mcq_opts, correct_option=correct_opt
        ))
        num += 1
    return qs

if __name__ == '__main__':
    dsa = build_dsa_pack()
    ps = build_problemsolving_pack()
    code = build_coding_pack()
    print(f"Built DSA pack: {len(dsa)} questions (Target: >=300)")
    print(f"Built Problem Solving pack: {len(ps)} questions (Target: >=200)")
    print(f"Built Coding pack: {len(code)} questions (Target: >=200)")
