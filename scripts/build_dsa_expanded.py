# scripts/build_dsa_expanded.py
"""
Generates 190+ comprehensive DSA questions covering Trees, BST, Heaps, Graphs,
Advanced Stacks & Queues, Sorting & Searching, DP Fundamentals, Tries, and Bit Manipulation.
"""

dsa_expanded_items = [
    # --- Trees & Binary Search Trees (30 items) ---
    (
        "What is the difference between a Binary Tree and a Binary Search Tree (BST)?",
        "In a Binary Tree, each node has at most two children with no ordering constraint. In a Binary Search Tree, for every node, all keys in its left subtree are smaller than the node's key, and all keys in its right subtree are greater.",
        "Easy",
        "Comparison",
        "",
        "What is the time complexity of searching in a balanced BST versus a degenerate BST?"
    ),
    (
        "What is the height of a tree and how is it measured?",
        "The height of a tree is the number of edges on the longest downward path from the root node to a leaf node. An empty tree has height -1, and a single-node tree has height 0.",
        "Easy",
        "Concept",
        "",
        "How does tree height affect the time complexity of search and insertion operations?"
    ),
    (
        "Explain Inorder, Preorder, and Postorder tree traversals.",
        "Inorder traverses Left Subtree -> Root -> Right Subtree (yields sorted order in a BST). Preorder traverses Root -> Left -> Right (used for copying or serializing trees). Postorder traverses Left -> Right -> Root (used for deleting nodes or bottom-up evaluations).",
        "Easy",
        "Concept",
        "// Inorder traversal\nfunction inorder(node) {\n  if (!node) return;\n  inorder(node.left);\n  console.log(node.val);\n  inorder(node.right);\n}",
        "Which traversal is used to evaluate an expression tree?"
    ),
    (
        "What is Level Order Traversal in a Binary Tree?",
        "Level Order Traversal visits nodes level by level from top to bottom and left to right. It is implemented using Breadth-First Search (BFS) with a First-In-First-Out (FIFO) queue.",
        "Intermediate",
        "Concept",
        "function levelOrder(root) {\n  if (!root) return [];\n  const queue = [root];\n  const result = [];\n  while (queue.length > 0) {\n    const node = queue.shift();\n    result.push(node.val);\n    if (node.left) queue.push(node.left);\n    if (node.right) queue.push(node.right);\n  }\n  return result;\n}",
        "What is the space complexity of level order traversal in the worst case?"
    ),
    (
        "What is a balanced binary tree?",
        "A binary tree is balanced if, for every node, the height difference between its left and right subtrees is at most 1. This ensures search, insertion, and deletion remain O(log n).",
        "Intermediate",
        "Concept",
        "",
        "Name two self-balancing binary search trees."
    ),
    (
        "What is a complete binary tree versus a full binary tree?",
        "A full binary tree is one where every node has either 0 or 2 children. A complete binary tree has all levels completely filled except possibly the last level, which is filled from left to right.",
        "Intermediate",
        "Comparison",
        "",
        "Why is the complete binary tree property crucial for implementing binary heaps in arrays?"
    ),
    (
        "How do you find the maximum depth of a binary tree recursively?",
        "The maximum depth of a tree is 1 plus the maximum of the depths of its left and right subtrees. The base case returns 0 when the current node is null.",
        "Easy",
        "Practical",
        "function maxDepth(root) {\n  if (!root) return 0;\n  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));\n}",
        "How can you find the maximum depth iteratively?"
    ),
    (
        "How do you search for an element in a Binary Search Tree?",
        "Start at the root. If the target equals the root's value, return it. If the target is smaller, search the left subtree; if greater, search the right subtree. Repeat until found or null.",
        "Easy",
        "Practical",
        "function searchBST(root, val) {\n  if (!root || root.val === val) return root;\n  return val < root.val ? searchBST(root.left, val) : searchBST(root.right, val);\n}",
        "What is the average and worst-case time complexity of searching a BST?"
    ),
    (
        "How is a new node inserted into a Binary Search Tree?",
        "Compare the new value with the root. If smaller, proceed to the left child; if larger, proceed to the right child. Repeat down the tree until reaching a null pointer, and attach the new node there.",
        "Intermediate",
        "Practical",
        "function insertBST(root, val) {\n  if (!root) return { val, left: null, right: null };\n  if (val < root.val) root.left = insertBST(root.left, val);\n  else if (val > root.val) root.right = insertBST(root.right, val);\n  return root;\n}",
        "Can a standard BST contain duplicate values?"
    ),
    (
        "How do you delete a node with two children from a BST?",
        "Find the node's inorder successor (the smallest node in its right subtree) or inorder predecessor (the largest node in its left subtree), copy its value into the target node, and then recursively delete that successor/predecessor node.",
        "Advanced",
        "Practical",
        "",
        "Why does replacing the node with its inorder successor preserve the BST invariant?"
    ),
    (
        "What is the Lowest Common Ancestor (LCA) in a BST?",
        "The Lowest Common Ancestor of two nodes p and q in a BST is the lowest node that has both p and q as descendants. Starting from the root, if both values are smaller, move left; if both are larger, move right; otherwise, the current node is the LCA.",
        "Intermediate",
        "Practical",
        "function lowestCommonAncestor(root, p, q) {\n  while (root) {\n    if (p.val < root.val && q.val < root.val) root = root.left;\n    else if (p.val > root.val && q.val > root.val) root = root.right;\n    else return root;\n  }\n  return null;\n}",
        "How does LCA differ when the tree is a generic binary tree instead of a BST?"
    ),
    (
        "How do you validate whether a binary tree is a valid BST?",
        "Check that every node's value lies strictly within an allowed range (min, max). Start at the root with (-Infinity, +Infinity). When going left, update max = root.val; when going right, update min = root.val.",
        "Intermediate",
        "Practical",
        "function isValidBST(root, min = -Infinity, max = Infinity) {\n  if (!root) return true;\n  if (root.val <= min || root.val >= max) return false;\n  return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);\n}",
        "Why is checking only root.left < root and root.right > root insufficient?"
    ),
    (
        "How do you check if two binary trees are identical?",
        "Two binary trees are identical if both roots are null, or both nodes have the same value and their left subtrees are identical and their right subtrees are identical.",
        "Easy",
        "Practical",
        "function isSameTree(p, q) {\n  if (!p && !q) return true;\n  if (!p || !q || p.val !== q.val) return false;\n  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);\n}",
        "What is the time complexity of isSameTree?"
    ),
    (
        "How do you invert or mirror a binary tree?",
        "Swap the left and right child pointers of the current node, then recursively invert the left subtree and right subtree.",
        "Easy",
        "Practical",
        "function invertTree(root) {\n  if (!root) return null;\n  const temp = root.left;\n  root.left = invertTree(root.right);\n  root.right = invertTree(temp);\n  return root;\n}",
        "What is the space complexity of inverting a binary tree?"
    ),
    (
        "What is a symmetric (mirror) binary tree?",
        "A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree. Node values must match, and the left child of one side must match the right child of the other.",
        "Intermediate",
        "Concept",
        "function isSymmetric(root) {\n  function check(t1, t2) {\n    if (!t1 && !t2) return true;\n    if (!t1 || !t2 || t1.val !== t2.val) return false;\n    return check(t1.left, t2.right) && check(t1.right, t2.left);\n  }\n  return !root || check(root.left, root.right);\n}",
        "How can you check tree symmetry iteratively?"
    ),
    (
        "What is the diameter of a binary tree?",
        "The diameter (or width) of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.",
        "Intermediate",
        "Concept",
        "",
        "How do you compute the diameter in O(n) time during a single postorder traversal?"
    ),
    (
        "What is an AVL Tree?",
        "An AVL tree is a self-balancing binary search tree where the difference between heights of left and right subtrees for any node cannot be more than 1. When unbalanced, rotations (LL, RR, LR, RL) restore balance.",
        "Advanced",
        "Concept",
        "",
        "What is the worst-case lookup time in an AVL tree?"
    ),
    (
        "What is a Red-Black Tree?",
        "A Red-Black Tree is a self-balancing BST where each node is colored red or black, satisfying color rules that ensure no path from root to leaf is more than twice as long as any other path.",
        "Advanced",
        "Concept",
        "",
        "Why do standard libraries like Java TreeMap use Red-Black trees rather than AVL trees?"
    ),
    (
        "What is the difference between Inorder and Preorder serialization of a tree?",
        "Preorder serialization records the root first followed by left and right subtrees (often recording nulls), allowing unambiguous reconstruction of the binary tree structure.",
        "Intermediate",
        "Comparison",
        "",
        "Can a binary tree be uniquely reconstructed from only its Inorder traversal?"
    ),
    (
        "What is the minimum number of nodes in a binary tree of height h?",
        "A binary tree of height h has at least h + 1 nodes (a degenerate linear chain where each node has only one child).",
        "Easy",
        "Concept",
        "",
        "What is the maximum number of nodes in a binary tree of height h?"
    ),
    (
        "What is the maximum number of nodes at level k of a binary tree?",
        "The maximum number of nodes at level k (where root is level 0) is 2^k.",
        "Easy",
        "Concept",
        "",
        "How many total nodes are in a full binary tree of height h?"
    ),
    (
        "What is a threaded binary tree?",
        "A threaded binary tree makes use of null pointers in leaf nodes to point to the inorder predecessor and successor, enabling traversal without recursion or an auxiliary stack.",
        "Advanced",
        "Concept",
        "",
        "What is the space advantage of a threaded binary tree?"
    ),
    (
        "What is an expression tree?",
        "An expression tree is a binary tree where internal nodes correspond to operators (+, -, *, /) and leaf nodes correspond to operands (numbers or variables).",
        "Intermediate",
        "Concept",
        "",
        "Which traversal of an expression tree produces postfix notation?"
    ),
    (
        "What is the time complexity of finding the minimum element in a BST?",
        "O(h) where h is the tree height. Starting at the root, simply follow the left child pointers until a node with no left child is reached. In a balanced BST this is O(log n); in a skewed BST it is O(n).",
        "Easy",
        "Concept",
        "",
        "How do you find the maximum element in a BST?"
    ),
    (
        "What is tree path sum and how is it checked?",
        "Given a binary tree and an integer targetSum, determine if the tree has a root-to-leaf path such that adding all values along the path equals targetSum.",
        "Intermediate",
        "Practical",
        "function hasPathSum(root, targetSum) {\n  if (!root) return false;\n  if (!root.left && !root.right) return root.val === targetSum;\n  return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);\n}",
        "What is the edge case when targetSum is 0 and root is null?"
    ),
    (
        "What is an inorder successor in a BST?",
        "The inorder successor of a node is the node with the smallest key strictly greater than the given node's key. If the node has a right child, it is the leftmost node in its right subtree.",
        "Intermediate",
        "Concept",
        "",
        "How do you find the inorder successor if the node does not have a right child?"
    ),
    (
        "What is the Morris Traversal algorithm?",
        "Morris Traversal is an algorithm that performs Inorder and Preorder traversals in O(n) time and O(1) auxiliary space by temporarily modifying tree pointers using threading.",
        "Advanced",
        "Concept",
        "",
        "What is the main drawback of Morris Traversal?"
    ),
    (
        "Which of the following traversals outputs BST elements in strictly ascending order?",
        "Inorder traversal visits the left subtree, current node, then right subtree, which yields elements in sorted ascending order for any valid BST.",
        "Easy",
        "MCQ",
        "",
        {"A": "Preorder", "B": "Inorder", "C": "Postorder", "D": "Level Order"},
        "B",
        "How would you traverse a BST in descending order?"
    ),
    (
        "What is the maximum number of leaves in a binary tree of height h?",
        "In a complete binary tree of height h, the leaf level (level h) has at most 2^h leaves.",
        "Easy",
        "MCQ",
        "",
        {"A": "2*h", "B": "2^h", "C": "2^(h+1) - 1", "D": "h^2"},
        "B",
        "What is the relationship between the number of leaves and internal nodes with two children in a full binary tree?"
    ),
    (
        "What is the time complexity to construct a BST from a sorted array of size n with minimum height?",
        "O(n) time. By picking the middle element as root and recursively picking middle elements of left and right halves, a balanced BST is constructed in O(n).",
        "Intermediate",
        "MCQ",
        "",
        {"A": "O(n log n)", "B": "O(n)", "C": "O(n^2)", "D": "O(log n)"},
        "B",
        "What is the height of the constructed BST?"
    ),

    # --- Heaps & Priority Queues (20 items) ---
    (
        "What is a Binary Heap and what are its two main types?",
        "A Binary Heap is a complete binary tree that satisfies the heap property. In a Min-Heap, every parent node is less than or equal to its children (root is minimum). In a Max-Heap, every parent is greater than or equal to its children (root is maximum).",
        "Easy",
        "Concept",
        "",
        "What data structure is typically used to store a binary heap?"
    ),
    (
        "How is a binary heap represented in an array?",
        "For a zero-indexed array: the root is at index 0. For any node at index i: its parent is at Math.floor((i - 1) / 2), its left child is at 2*i + 1, and its right child is at 2*i + 2.",
        "Easy",
        "Concept",
        "",
        "Why is an array representation more cache-friendly than a pointer-based tree representation?"
    ),
    (
        "What is the time complexity of inserting an element into a binary heap?",
        "O(log n) time. The new element is placed at the end of the array (bottom of the tree) and 'bubbled up' (sifted up) by swapping with its parent until the heap property is restored.",
        "Easy",
        "Concept",
        "",
        "What is the worst-case number of swaps during heap insertion?"
    ),
    (
        "What is the time complexity of extracting the minimum or maximum element from a binary heap?",
        "O(log n) time. The root element is removed and replaced by the last element in the array. The new root is then 'sifted down' (bubbled down) by swapping with its smaller child (in Min-Heap) until the heap property is satisfied.",
        "Easy",
        "Concept",
        "",
        "What is the time complexity to simply peek at the root element without removing it?"
    ),
    (
        "What is the time complexity to build a heap from an unordered array of n elements?",
        "O(n) time using Floyd's heap construction algorithm (sifting down from the lowest internal node index (n/2 - 1) up to the root), not O(n log n).",
        "Intermediate",
        "Concept",
        "",
        "Why is building a heap bottom-up O(n) while inserting n elements one-by-one is O(n log n)?"
    ),
    (
        "What is a Priority Queue and how does it relate to a Heap?",
        "A Priority Queue is an abstract data type where each element has a priority, and elements with higher priority are dequeued before lower priority ones. A Binary Heap is the standard, most efficient implementation of a Priority Queue.",
        "Easy",
        "Comparison",
        "",
        "Can a priority queue be implemented using a sorted array or linked list?"
    ),
    (
        "How do you find the Kth largest element in an unsorted array efficiently using a heap?",
        "Maintain a Min-Heap of size K. Iterate through the array. For each element, if the heap has fewer than K items, push it; otherwise, if the element is greater than the heap root (minimum of the top K), extract the root and push the element. The root will be the Kth largest in O(n log k) time.",
        "Intermediate",
        "Practical",
        "",
        "What is the advantage of using a Min-Heap of size K over sorting the entire array?"
    ),
    (
        "What is Heap Sort and what is its time and space complexity?",
        "Heap Sort builds a Max-Heap from the input array, then repeatedly swaps the root (max element) with the last element and heapifies the reduced heap. Time complexity is O(n log n) in all cases, and auxiliary space is O(1) (in-place).",
        "Intermediate",
        "Concept",
        "",
        "Is Heap Sort a stable sorting algorithm?"
    ),
    (
        "What is the difference between a Max-Heap and a Binary Search Tree?",
        "In a Max-Heap, a parent is greater than both children, but there is no ordering between the left and right children. In a BST, left child is less than parent and right child is greater. Lookup in a BST is O(log n), but in a heap it is O(n).",
        "Intermediate",
        "Comparison",
        "",
        "Can you perform an efficient search for an arbitrary key in a binary heap?"
    ),
    (
        "What is a d-ary heap?",
        "A d-ary heap is a generalization of a binary heap where each non-leaf node has up to d children instead of 2. It reduces tree height to log_d(n), speeding up insertion and decrease-key operations.",
        "Advanced",
        "Concept",
        "",
        "How does a 4-ary heap improve cache locality compared to a binary heap?"
    ),
    (
        "What is the decrease-key operation in a priority queue?",
        "The decrease-key operation lowers the value of a key at a given position and sifts it up to restore the heap property in O(log n) time. It is a critical component of Dijkstra's shortest path algorithm.",
        "Advanced",
        "Concept",
        "",
        "Why is decrease-key difficult to implement with standard language priority queue libraries?"
    ),
    (
        "What is a Fibonacci Heap?",
        "A Fibonacci Heap is a priority queue data structure that supports insert, find-min, and decrease-key in O(1) amortized time, and delete/extract-min in O(log n) amortized time.",
        "Advanced",
        "Concept",
        "",
        "Why is Fibonacci heap rarely used in practical software despite superior theoretical complexity?"
    ),
    (
        "How do you merge K sorted linked lists efficiently?",
        "Insert the head node of each of the K lists into a Min-Heap. Repeatedly extract the minimum node, append it to the result list, and insert that node's next element into the heap. Total time is O(N log K) where N is total number of nodes.",
        "Intermediate",
        "Practical",
        "",
        "What would be the time complexity if you merged them sequentially two at a time?"
    ),
    (
        "What is a Treap?",
        "A Treap is a hybrid data structure combining a Binary Search Tree (ordered by keys) and a Heap (ordered by randomly assigned priorities), ensuring expected logarithmic height.",
        "Advanced",
        "Concept",
        "",
        "How does randomized priority prevent a Treap from degenerating into a linked list?"
    ),
    (
        "In a min-heap with n elements, where can the maximum element be located?",
        "The maximum element must be located in one of the leaf nodes, which occupy indices from Math.floor(n / 2) to n - 1 in the array.",
        "Intermediate",
        "MCQ",
        "",
        {"A": "At the root", "B": "At index 1", "C": "In one of the leaf nodes", "D": "At index n/4"},
        "C",
        "How long does it take to find the maximum element in a min-heap?"
    ),
    (
        "What is the index of the parent of a node at index 7 in a 0-indexed binary heap?",
        "Parent index is Math.floor((7 - 1) / 2) = Math.floor(6 / 2) = 3.",
        "Easy",
        "MCQ",
        "",
        {"A": "2", "B": "3", "C": "4", "D": "1"},
        "B",
        "What are the indices of the children of the node at index 3?"
    ),
    (
        "What is the worst-case time complexity of building a heap of n elements using Floyd's algorithm?",
        "Floyd's bottom-up heap construction runs in O(n) worst-case time because higher levels have fewer nodes and lower levels have smaller heights.",
        "Intermediate",
        "MCQ",
        "",
        {"A": "O(log n)", "B": "O(n)", "C": "O(n log n)", "D": "O(n^2)"},
        "B",
        "Why is this faster than repeated insertions?"
    ),
    (
        "Which operation cannot be done in O(log n) time in a standard binary min-heap?",
        "Searching for an arbitrary element takes O(n) because a heap does not maintain ordering between sibling subtrees.",
        "Easy",
        "MCQ",
        "",
        {"A": "Insert", "B": "Extract Min", "C": "Search for arbitrary key", "D": "Decrease Key (given index)"},
        "C",
        "How can you augment a heap to support O(log n) arbitrary key deletion?"
    ),
    (
        "What data structure is best suited to continuously calculate the median of a streaming dataset?",
        "Two heaps: a Max-Heap for the lower half of numbers and a Min-Heap for the upper half, allowing O(1) median retrieval and O(log n) insertion.",
        "Intermediate",
        "Concept",
        "",
        "How do you keep the two heaps balanced in size?"
    ),
    (
        "What is the space complexity of an in-place heap sort?",
        "O(1) auxiliary space, as it rearranges the input array in-place without requiring extra memory allocations.",
        "Easy",
        "Concept",
        "",
        "How does heap sort space complexity compare with merge sort?"
    ),

    # --- Graphs & Graph Algorithms (30 items) ---
    (
        "What is a Graph and what are its fundamental components?",
        "A Graph G = (V, E) is a non-linear data structure consisting of a set of Vertices (nodes) V and a set of Edges E connecting pairs of vertices. Edges can be directed or undirected, and weighted or unweighted.",
        "Easy",
        "Concept",
        "",
        "What is the difference between a dense graph and a sparse graph?"
    ),
    (
        "Compare Adjacency Matrix and Adjacency List representations of a graph.",
        "An Adjacency Matrix is a 2D V x V array where matrix[u][v] indicates an edge; it takes O(V^2) space and checks edge existence in O(1). An Adjacency List stores a list of neighbors for each vertex; it takes O(V + E) space and is preferred for sparse graphs.",
        "Intermediate",
        "Comparison",
        "",
        "When would an Adjacency Matrix be preferred over an Adjacency List?"
    ),
    (
        "What is Breadth-First Search (BFS) on a graph and how is it implemented?",
        "BFS explores vertices level by level starting from a source vertex. It uses a FIFO queue and a visited set to avoid processing vertices more than once. It runs in O(V + E) time.",
        "Easy",
        "Concept",
        "function bfs(graph, start) {\n  const visited = new Set([start]);\n  const queue = [start];\n  while (queue.length) {\n    const node = queue.shift();\n    console.log(node);\n    for (const neighbor of graph[node] || []) {\n      if (!visited.has(neighbor)) {\n        visited.add(neighbor);\n        queue.push(neighbor);\n      }\n    }\n  }\n}",
        "Why is BFS guaranteed to find the shortest path in an unweighted graph?"
    ),
    (
        "What is Depth-First Search (DFS) on a graph and how is it implemented?",
        "DFS explores as deep as possible along each branch before backtracking. It is implemented using recursion (call stack) or an explicit LIFO stack, along with a visited set. Time complexity is O(V + E).",
        "Easy",
        "Concept",
        "function dfs(graph, node, visited = new Set()) {\n  visited.add(node);\n  console.log(node);\n  for (const neighbor of graph[node] || []) {\n    if (!visited.has(neighbor)) {\n      dfs(graph, neighbor, visited);\n    }\n  }\n}",
        "What happens if you do not track visited vertices in a cyclic graph?"
    ),
    (
        "How do you detect a cycle in an undirected graph?",
        "Perform BFS or DFS. During traversal, if you encounter an adjacent vertex that is already visited and is NOT the parent of the current vertex, a cycle exists.",
        "Intermediate",
        "Practical",
        "",
        "Can a Disjoint Set (Union-Find) also detect cycles in an undirected graph?"
    ),
    (
        "How do you detect a cycle in a directed graph?",
        "Use DFS with a recursion stack tracker (or 3-color scheme: White = unvisited, Gray = in current DFS path, Black = fully explored). If a neighbor is in the current recursion stack (Gray), a back-edge and hence a cycle is detected.",
        "Intermediate",
        "Practical",
        "",
        "Why does the undirected cycle detection parent check fail for directed graphs?"
    ),
    (
        "What is Topological Sorting and what type of graph is required?",
        "Topological Sorting is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before vertex v. It is only possible on Directed Acyclic Graphs (DAGs).",
        "Intermediate",
        "Concept",
        "",
        "What real-world engineering problem is modeled by topological sort?"
    ),
    (
        "Explain Kahn's Algorithm for Topological Sort.",
        "Compute in-degrees for all vertices. Enqueue all vertices with in-degree 0. While the queue is not empty, dequeue a vertex, append it to the sorted list, and decrement in-degrees of its neighbors. If a neighbor reaches in-degree 0, enqueue it. If output count < V, a cycle exists.",
        "Intermediate",
        "Concept",
        "",
        "What is the time complexity of Kahn's Algorithm?"
    ),
    (
        "What is Dijkstra's Algorithm and what are its limitations?",
        "Dijkstra's Algorithm finds the shortest path from a single source to all other vertices in a weighted graph with non-negative edge weights using a Min-Priority Queue. It does not work correctly with negative edge weights.",
        "Intermediate",
        "Concept",
        "",
        "What is the time complexity of Dijkstra using a binary heap?"
    ),
    (
        "Why does Dijkstra's Algorithm fail with negative edge weights?",
        "Dijkstra assumes that once a vertex is marked visited (extracted from the priority queue), its shortest distance is finalized. A negative weight edge later in the graph can provide a shorter path, violating this greedy assumption.",
        "Intermediate",
        "Concept",
        "",
        "Which algorithm handles single-source shortest paths with negative edge weights?"
    ),
    (
        "What is the Bellman-Ford Algorithm?",
        "The Bellman-Ford Algorithm computes single-source shortest paths in weighted graphs that may contain negative edge weights. It relaxes all edges V - 1 times in O(V * E) time and can detect negative weight cycles.",
        "Advanced",
        "Concept",
        "",
        "How does Bellman-Ford detect a negative weight cycle on the Vth iteration?"
    ),
    (
        "What is the Floyd-Warshall Algorithm?",
        "Floyd-Warshall is a dynamic programming algorithm that finds shortest paths between all pairs of vertices in a weighted graph in O(V^3) time and O(V^2) space.",
        "Advanced",
        "Concept",
        "",
        "Can Floyd-Warshall detect negative weight cycles?"
    ),
    (
        "What is a Minimum Spanning Tree (MST)?",
        "A Minimum Spanning Tree of a connected, undirected, weighted graph is a subset of edges that connects all vertices together without any cycles and with the minimum possible total edge weight. An MST of V vertices always has V - 1 edges.",
        "Intermediate",
        "Concept",
        "",
        "Can a graph have more than one valid MST?"
    ),
    (
        "Compare Kruskal's and Prim's algorithms for finding an MST.",
        "Kruskal's algorithm sorts all edges by weight and greedily adds edges that do not form a cycle using Disjoint Set Union (DSU) in O(E log E). Prim's algorithm grows a single tree from a starting vertex by picking the minimum weight cut edge using a priority queue in O(E log V).",
        "Intermediate",
        "Comparison",
        "",
        "Which algorithm is better suited for dense graphs?"
    ),
    (
        "What is a Disjoint Set Union (DSU) or Union-Find data structure?",
        "DSU tracks elements partitioned into disjoint subsets. It supports two primary operations: find(x) to find the representative of x's set, and union(x, y) to merge two sets. With path compression and union by rank, operations take nearly O(1) amortized time.",
        "Intermediate",
        "Concept",
        "class DSU {\n  constructor(n) {\n    this.parent = Array.from({ length: n }, (_, i) => i);\n  }\n  find(i) {\n    if (this.parent[i] === i) return i;\n    return (this.parent[i] = this.find(this.parent[i]));\n  }\n  union(i, j) {\n    const rootI = this.find(i);\n    const rootJ = this.find(j);\n    if (rootI !== rootJ) this.parent[rootI] = rootJ;\n  }\n}",
        "What is the Ackermann function relation to DSU time complexity?"
    ),
    (
        "What is a Bipartite Graph?",
        "A graph is Bipartite if its vertices can be divided into two disjoint sets such that every edge connects a vertex in set 1 to a vertex in set 2. A graph is bipartite if and only if it contains no odd-length cycles.",
        "Intermediate",
        "Concept",
        "",
        "How can you check if a graph is bipartite using 2-coloring via BFS?"
    ),
    (
        "What is a Connected Component in an undirected graph?",
        "A Connected Component is a maximal subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.",
        "Easy",
        "Concept",
        "",
        "How do you count the number of connected components using BFS or DFS?"
    ),
    (
        "What is a Strongly Connected Component (SCC) in a directed graph?",
        "A Strongly Connected Component is a maximal subgraph of a directed graph where every vertex is reachable from every other vertex in that subgraph.",
        "Advanced",
        "Concept",
        "",
        "Name an algorithm used to find all SCCs in a directed graph."
    ),
    (
        "What is Tarjan's or Kosaraju's Algorithm?",
        "Both are linear time O(V + E) algorithms to find all Strongly Connected Components in a directed graph. Kosaraju uses two DFS passes with graph transposition, while Tarjan uses a single DFS pass with discovery times and low-link values.",
        "Advanced",
        "Concept",
        "",
        "What is the role of the stack in Tarjan's algorithm?"
    ),
    (
        "What is an in-degree and out-degree of a vertex in a directed graph?",
        "In-degree is the number of incoming edges pointing to the vertex. Out-degree is the number of outgoing edges starting from the vertex.",
        "Easy",
        "Concept",
        "",
        "What is a source node and what is a sink node in a DAG?"
    ),
    (
        "What is the Handshaking Lemma in graph theory?",
        "In every finite undirected graph, the sum of degrees of all vertices is twice the number of edges: sum(deg(v)) = 2 * |E|. As a consequence, the number of vertices with odd degree is always even.",
        "Intermediate",
        "Concept",
        "",
        "Why is the sum of degrees always an even number?"
    ),
    (
        "How do you find the number of islands in a 2D binary grid?",
        "Iterate through each cell. When an unvisited '1' (land) is found, increment the island count and launch a DFS/BFS to visit and mark all 4-directionally adjacent '1's as visited (or change them to '0').",
        "Intermediate",
        "Practical",
        "function numIslands(grid) {\n  let count = 0;\n  for (let r = 0; r < grid.length; r++) {\n    for (let c = 0; c < grid[0].length; c++) {\n      if (grid[r][c] === '1') {\n        count++;\n        dfs(grid, r, c);\n      }\n    }\n  }\n  return count;\n}\nfunction dfs(grid, r, c) {\n  if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] !== '1') return;\n  grid[r][c] = '0';\n  dfs(grid, r + 1, c); dfs(grid, r - 1, c); dfs(grid, r, c + 1); dfs(grid, r, c - 1);\n}",
        "What is the time complexity of the number of islands algorithm?"
    ),
    (
        "What is A* Search Algorithm?",
        "A* is a path search algorithm that finds the shortest path by combining Dijkstra's algorithm with a heuristic function: f(n) = g(n) + h(n), where g(n) is the exact cost from start to n, and h(n) is an admissible heuristic estimate to the goal.",
        "Advanced",
        "Concept",
        "",
        "What does it mean for a heuristic to be 'admissible'?"
    ),
    (
        "Which of the following graph representations requires O(V^2) space regardless of the number of edges?",
        "An Adjacency Matrix always creates a V x V grid of numbers or booleans, taking O(V^2) space even if there are zero edges.",
        "Easy",
        "MCQ",
        "",
        {"A": "Adjacency List", "B": "Adjacency Matrix", "C": "Edge List", "D": "Incidence Matrix"},
        "B",
        "When is an adjacency matrix more space-efficient than an adjacency list?"
    ),
    (
        "Which algorithm is best suited to find the shortest path between two vertices in an unweighted graph?",
        "Breadth-First Search (BFS) explores vertices level by level, ensuring the first time the destination vertex is reached, it is via the shortest path in terms of edge count.",
        "Easy",
        "MCQ",
        "",
        {"A": "DFS", "B": "BFS", "C": "Dijkstra", "D": "Bellman-Ford"},
        "B",
        "Why is Dijkstra unnecessary for unweighted graphs?"
    ),
    (
        "What is the maximum number of edges in a simple undirected graph with V vertices?",
        "In a complete undirected graph without self-loops or multi-edges, every vertex connects to all other V - 1 vertices, giving V * (V - 1) / 2 edges.",
        "Easy",
        "MCQ",
        "",
        {"A": "V", "B": "V * (V - 1)", "C": "V * (V - 1) / 2", "D": "2^V"},
        "C",
        "What is the maximum number of edges in a directed graph?"
    ),
    (
        "A DAG with 5 vertices has a cycle if and only if:",
        "A Directed Acyclic Graph by definition has NO directed cycles. If a cycle is present, it is not a DAG.",
        "Easy",
        "MCQ",
        "",
        {"A": "It has 5 edges", "B": "It contains a back-edge during DFS", "C": "It has multiple sink nodes", "D": "In-degree of all vertices is 1"},
        "B",
        "What type of edge in DFS indicates a cycle?"
    ),
    (
        "What is an articulation point (or cut vertex) in a graph?",
        "An articulation point is a vertex whose removal increases the number of connected components in the graph, effectively disconnecting it.",
        "Advanced",
        "Concept",
        "",
        "How is Tarjan's bridge-finding algorithm related to articulation points?"
    ),
    (
        "What is a bridge in graph theory?",
        "A bridge (or cut edge) is an edge whose removal increases the number of connected components in the graph.",
        "Advanced",
        "Concept",
        "",
        "What is the time complexity to find all bridges using DFS?"
    ),
    (
        "What is an Eulerian Path versus an Eulerian Circuit?",
        "An Eulerian Path visits every edge of a graph exactly once. An Eulerian Circuit is an Eulerian Path that starts and ends on the same vertex. A connected undirected graph has an Eulerian circuit if and only if every vertex has an even degree.",
        "Advanced",
        "Concept",
        "",
        "What is the condition for an Eulerian path to exist in an undirected graph?"
    ),

    # --- Sorting & Searching Deep Dive (25 items) ---
    (
        "What is the difference between a stable and an unstable sorting algorithm?",
        "A stable sorting algorithm preserves the relative order of equal keys in the output. An unstable sort may rearrange equal elements arbitrarily. Merge Sort and Insertion Sort are stable; Quick Sort and Heap Sort are unstable.",
        "Intermediate",
        "Comparison",
        "",
        "Why is stability important when sorting objects with multiple fields?"
    ),
    (
        "Explain Merge Sort and its divide-and-conquer steps.",
        "Merge Sort divides the array into two halves, recursively sorts both halves, and then merges the two sorted halves into a single sorted array. Time complexity is O(n log n) in all cases, and auxiliary space is O(n).",
        "Easy",
        "Concept",
        "function mergeSort(arr) {\n  if (arr.length <= 1) return arr;\n  const mid = Math.floor(arr.length / 2);\n  const left = mergeSort(arr.slice(0, mid));\n  const right = mergeSort(arr.slice(mid));\n  return merge(left, right);\n}",
        "What is the recurrence relation for Merge Sort?"
    ),
    (
        "Explain Quick Sort and how the partition algorithm works.",
        "Quick Sort picks a pivot element, partitions the array so elements smaller than the pivot are on the left and larger on the right, and recursively sorts the sub-arrays. Average time is O(n log n), worst-case is O(n^2), and auxiliary space is O(log n) call stack.",
        "Intermediate",
        "Concept",
        "",
        "How does picking a random pivot prevent worst-case O(n^2) performance?"
    ),
    (
        "Compare Lomuto partition and Hoare partition in Quick Sort.",
        "Lomuto partition uses a single pointer iterating forward and is easier to implement; it does more swaps. Hoare partition uses two pointers converging from both ends and does roughly three times fewer swaps on average.",
        "Intermediate",
        "Comparison",
        "",
        "Which partition scheme is commonly taught in standard textbooks?"
    ),
    (
        "Why is Quick Sort often faster than Merge Sort in practice despite having a worse worst-case?",
        "Quick Sort has excellent cache locality because it operates in-place without copying elements to temporary arrays, and has small constant factors in inner loops.",
        "Intermediate",
        "Concept",
        "",
        "When would you choose Merge Sort over Quick Sort?"
    ),
    (
        "Explain Insertion Sort and identify when it outperforms O(n log n) algorithms.",
        "Insertion Sort builds the sorted array one item at a time by shifting elements. For small arrays (e.g. n < 20) or nearly sorted arrays, Insertion Sort runs in O(n) time and has very low overhead.",
        "Easy",
        "Practical",
        "function insertionSort(arr) {\n  for (let i = 1; i < arr.length; i++) {\n    let key = arr[i];\n    let j = i - 1;\n    while (j >= 0 && arr[j] > key) {\n      arr[j + 1] = arr[j];\n      j--;\n    }\n    arr[j + 1] = key;\n  }\n  return arr;\n}",
        "What hybrid sorting algorithm uses Insertion Sort for small subarrays?"
    ),
    (
        "What is Counting Sort and what are its constraints?",
        "Counting Sort is a non-comparison sorting algorithm that counts occurrences of each distinct integer key in an auxiliary array. It runs in O(n + k) time where k is the range of keys. It is only efficient when the range k is not significantly greater than n.",
        "Intermediate",
        "Concept",
        "",
        "Can Counting Sort sort floating point numbers?"
    ),
    (
        "What is Radix Sort?",
        "Radix Sort sorts numbers digit by digit from least significant digit (LSD) to most significant digit (MSD) using a stable subroutine like Counting Sort. It runs in O(d * (n + b)) where d is digit count and b is the base.",
        "Intermediate",
        "Concept",
        "",
        "What is the difference between LSD and MSD Radix Sort?"
    ),
    (
        "What is the lower bound for comparison-based sorting algorithms?",
        "Any comparison-based sorting algorithm requires at least Omega(n log n) comparisons in the worst case, as proven by the decision tree model (height of decision tree with n! leaves is at least log2(n!) = Theta(n log n)).",
        "Advanced",
        "Concept",
        "",
        "How do Counting Sort and Radix Sort bypass the Omega(n log n) lower bound?"
    ),
    (
        "How do you implement standard Binary Search iteratively?",
        "Maintain left and right pointers. Calculate mid = left + Math.floor((right - left) / 2). If arr[mid] === target, return mid. If target < arr[mid], set right = mid - 1; else set left = mid + 1. Repeat while left <= right.",
        "Easy",
        "Practical",
        "function binarySearch(arr, target) {\n  let left = 0, right = arr.length - 1;\n  while (left <= right) {\n    const mid = left + Math.floor((right - left) / 2);\n    if (arr[mid] === target) return mid;\n    if (arr[mid] < target) left = mid + 1;\n    else right = mid - 1;\n  }\n  return -1;\n}",
        "Why is `left + Math.floor((right - left) / 2)` preferred over `Math.floor((left + right) / 2)`?"
    ),
    (
        "How do you find the first occurrence of an element in a sorted array with duplicates?",
        "Perform binary search. When arr[mid] === target, do not return immediately; record mid as candidate result and continue searching to the left by setting right = mid - 1.",
        "Intermediate",
        "Practical",
        "function findFirst(arr, target) {\n  let left = 0, right = arr.length - 1, res = -1;\n  while (left <= right) {\n    const mid = left + Math.floor((right - left) / 2);\n    if (arr[mid] === target) { res = mid; right = mid - 1; }\n    else if (arr[mid] < target) left = mid + 1;\n    else right = mid - 1;\n  }\n  return res;\n}",
        "How do you modify this to find the last occurrence?"
    ),
    (
        "How do you search in a rotated sorted array?",
        "Calculate mid. One half (either left-to-mid or mid-to-right) must be normally sorted. Check if target lies within the sorted half's boundaries; if so, narrow search to that half, otherwise search the other half. Runs in O(log n).",
        "Intermediate",
        "Practical",
        "",
        "What happens to time complexity if the array contains duplicate elements?"
    ),
    (
        "How do you find a peak element in an array where arr[i] > arr[i-1] and arr[i] > arr[i+1]?",
        "Use binary search. If arr[mid] < arr[mid + 1], a peak is guaranteed to exist on the right side, so set left = mid + 1. Otherwise, a peak exists on the left (including mid), so set right = mid. Takes O(log n).",
        "Intermediate",
        "Practical",
        "",
        "Why is linear scan O(n) not optimal for finding a peak element?"
    ),
    (
        "How do you compute the integer square root of a number using binary search?",
        "Search between 0 and x. For mid, if mid * mid <= x and (mid + 1) * (mid + 1) > x, return mid. Adjust left or right accordingly. Runs in O(log x) time and O(1) space.",
        "Intermediate",
        "Practical",
        "function mySqrt(x) {\n  if (x < 2) return x;\n  let left = 1, right = Math.floor(x / 2), ans = 1;\n  while (left <= right) {\n    const mid = left + Math.floor((right - left) / 2);\n    if (mid * mid <= x) { ans = mid; left = mid + 1; }\n    else right = mid - 1;\n  }\n  return ans;\n}",
        "What edge cases should be tested for square root?"
    ),
    (
        "What is Bubble Sort and what is its optimized best-case time complexity?",
        "Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if in wrong order. With an 'isSwapped' boolean flag, it terminates in O(n) time if the array is already sorted.",
        "Easy",
        "Concept",
        "",
        "What is the average and worst-case number of comparisons in Bubble Sort?"
    ),
    (
        "What is Selection Sort and why is it not adaptive?",
        "Selection Sort repeatedly finds the minimum element from the unsorted subarray and places it at the beginning. It always performs O(n^2) comparisons regardless of initial array ordering.",
        "Easy",
        "Concept",
        "",
        "What is the maximum number of swaps performed by Selection Sort?"
    ),
    (
        "What is Timsort?",
        "Timsort is a hybrid stable sorting algorithm derived from Merge Sort and Insertion Sort. It identifies natural ordered segments ('runs') and merges them. It is the default sorting algorithm in Python and Java arrays.",
        "Advanced",
        "Concept",
        "",
        "What is Timsort's best-case time complexity?"
    ),
    (
        "Which sorting algorithm has a guaranteed worst-case time complexity of O(n log n) and uses O(1) extra space?",
        "Heap Sort runs in O(n log n) worst-case time and sorts completely in-place using O(1) auxiliary space.",
        "Easy",
        "MCQ",
        "",
        {"A": "Merge Sort", "B": "Quick Sort", "C": "Heap Sort", "D": "Insertion Sort"},
        "C",
        "Why is Merge Sort not O(1) extra space?"
    ),
    (
        "Which of the following sorting algorithms is inherently stable?",
        "Merge Sort is stable because during the merge step, when elements are equal, the element from the left subarray is chosen first.",
        "Easy",
        "MCQ",
        "",
        {"A": "Quick Sort", "B": "Heap Sort", "C": "Merge Sort", "D": "Selection Sort"},
        "C",
        "How can an unstable sort be made stable?"
    ),
    (
        "What is the worst-case time complexity of Quick Sort with Lomuto partition when the array is already sorted?",
        "If the last element is chosen as pivot on an already sorted array, the partition produces 0 and n - 1 elements, resulting in O(n^2) time.",
        "Intermediate",
        "MCQ",
        "",
        {"A": "O(n)", "B": "O(n log n)", "C": "O(n^2)", "D": "O(log n)"},
        "C",
        "How does median-of-three pivot selection mitigate this?"
    ),
    (
        "What is Dutch National Flag algorithm used for?",
        "It partitions an array of three distinct keys (like 0s, 1s, and 2s) into three sorted sections in-place in a single pass using three pointers (low, mid, high) in O(n) time and O(1) space.",
        "Intermediate",
        "Practical",
        "function sortColors(nums) {\n  let low = 0, mid = 0, high = nums.length - 1;\n  while (mid <= high) {\n    if (nums[mid] === 0) {\n      [nums[low], nums[mid]] = [nums[mid], nums[low]];\n      low++; mid++;\n    } else if (nums[mid] === 1) {\n      mid++;\n    } else {\n      [nums[mid], nums[high]] = [nums[high], nums[mid]];\n      high--;\n    }\n  }\n}",
        "Who proposed the Dutch National Flag problem?"
    ),
    (
        "What is Interpolation Search and when does it beat Binary Search?",
        "Interpolation search estimates the probe position based on key value: pos = low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low]). For uniformly distributed sorted arrays, it runs in O(log log n) average time.",
        "Advanced",
        "Concept",
        "",
        "What is the worst-case time complexity of Interpolation Search on non-uniform data?"
    ),
    (
        "What is Exponential Search?",
        "Exponential Search finds the range where the element resides by testing powers of 2 (1, 2, 4, 8, ...), then performs Binary Search within that bounded range. Runs in O(log i) where i is the target index.",
        "Intermediate",
        "Concept",
        "",
        "When is exponential search useful for unbounded or infinite lists?"
    ),
    (
        "What is the time complexity to find the median of an unsorted array using Quickselect?",
        "Quickselect finds the k-th smallest element with an average time complexity of O(n) and worst-case of O(n^2).",
        "Intermediate",
        "Concept",
        "",
        "What variant of Quickselect guarantees O(n) worst-case time?"
    ),
    (
        "What is ternary search?",
        "Ternary search divides the search space into three parts using two mid points (mid1, mid2). It is commonly used to find the maximum or minimum of a unimodal function.",
        "Intermediate",
        "Concept",
        "",
        "Why is binary search preferred over ternary search for sorted array lookups?"
    ),

    # --- Dynamic Programming & Recursion Fundamentals (30 items) ---
    (
        "What are the two core prerequisites for solving a problem using Dynamic Programming?",
        "Optimal Substructure (an optimal solution to the problem contains optimal solutions to its subproblems) and Overlapping Subproblems (the same subproblems are solved repeatedly).",
        "Easy",
        "Concept",
        "",
        "Give an example of a problem with optimal substructure that does NOT have overlapping subproblems."
    ),
    (
        "Compare Top-Down (Memoization) and Bottom-Up (Tabulation) Dynamic Programming.",
        "Top-Down uses recursion and caches subproblem solutions in a hash table or array on-demand. Bottom-Up starts from the base cases and iteratively fills a table without recursion overhead or call-stack limits.",
        "Easy",
        "Comparison",
        "",
        "When might Memoization be preferred over Tabulation?"
    ),
    (
        "Explain the Fibonacci sequence problem and compare its naive recursion with DP.",
        "Naive recursion solves fib(n) = fib(n-1) + fib(n-2) with O(2^n) time due to duplicate subtrees. Memoized or Tabulated DP stores results and computes each value once in O(n) time and O(1) space.",
        "Easy",
        "Practical",
        "function fib(n) {\n  if (n <= 1) return n;\n  let prev2 = 0, prev1 = 1;\n  for (let i = 2; i <= n; i++) {\n    const curr = prev1 + prev2;\n    prev2 = prev1;\n    prev1 = curr;\n  }\n  return prev1;\n}",
        "What is the space complexity of naive recursive fibonacci due to the call stack?"
    ),
    (
        "Explain the Climbing Stairs problem and write its recurrence.",
        "You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps. The total distinct ways to reach step n is ways(n) = ways(n-1) + ways(n-2), with base cases ways(1) = 1 and ways(2) = 2. This maps directly to Fibonacci.",
        "Easy",
        "Practical",
        "",
        "How does the recurrence change if you can take 1, 2, or 3 steps?"
    ),
    (
        "Explain the House Robber problem and state its DP state transition.",
        "You cannot rob adjacent houses. Let dp[i] be the maximum money robbed from first i houses. The transition is dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]). Space can be optimized to O(1).",
        "Intermediate",
        "Practical",
        "function rob(nums) {\n  let prev = 0, curr = 0;\n  for (const num of nums) {\n    const temp = Math.max(curr, prev + num);\n    prev = curr;\n    curr = temp;\n  }\n  return curr;\n}",
        "How do you handle the variant where houses are arranged in a circle?"
    ),
    (
        "What is the Coin Change problem (minimum coins) and what is its DP formulation?",
        "Given coins of different denominations and total amount, find the fewest coins needed. Let dp[i] be min coins for amount i. Initialize dp array with Infinity and dp[0] = 0. For each coin c and amount i from c to amount: dp[i] = Math.min(dp[i], 1 + dp[i - c]).",
        "Intermediate",
        "Practical",
        "function coinChange(coins, amount) {\n  const dp = new Array(amount + 1).fill(Infinity);\n  dp[0] = 0;\n  for (const c of coins) {\n    for (let i = c; i <= amount; i++) {\n      dp[i] = Math.min(dp[i], 1 + dp[i - c]);\n    }\n  }\n  return dp[amount] === Infinity ? -1 : dp[amount];\n}",
        "What is the time complexity of Coin Change?"
    ),
    (
        "What is the Coin Change 2 problem (number of combinations)?",
        "Find the number of combinations that make up the amount. Outer loop iterates over coins and inner loop iterates over amounts to ensure combinations (not permutations) are counted.",
        "Intermediate",
        "Concept",
        "",
        "Why does swapping the inner and outer loops compute permutations instead of combinations?"
    ),
    (
        "What is the 0/1 Knapsack problem?",
        "Given weights and values of n items and a knapsack of capacity W, select a subset of items to maximize total value without exceeding W, where each item can either be taken (1) or left (0). Runs in O(n * W) pseudo-polynomial time.",
        "Intermediate",
        "Concept",
        "",
        "Why is 0/1 Knapsack considered NP-complete?"
    ),
    (
        "Why can Fractional Knapsack be solved greedily but 0/1 Knapsack requires DP?",
        "In Fractional Knapsack, items can be broken down, so picking items with the highest value-to-weight ratio greedily is guaranteed to yield the optimal solution. In 0/1 Knapsack, taking a high-ratio item might leave unused capacity that prevents a higher overall total.",
        "Intermediate",
        "Comparison",
        "",
        "What is the time complexity of the Fractional Knapsack greedy algorithm?"
    ),
    (
        "What is the Longest Common Subsequence (LCS) problem?",
        "Given two strings text1 and text2, find the length of their longest common subsequence. If text1[i] === text2[j], dp[i][j] = 1 + dp[i-1][j-1]; otherwise dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]). Runs in O(m * n).",
        "Intermediate",
        "Practical",
        "",
        "How is LCS related to finding the minimum edit distance?"
    ),
    (
        "What is the Longest Increasing Subsequence (LIS) problem?",
        "Find the length of the longest subsequence in an array such that all elements of the subsequence are sorted in strictly increasing order. Standard DP is O(n^2); patience sorting with binary search solves it in O(n log n).",
        "Intermediate",
        "Concept",
        "",
        "How does patience sorting with binary search achieve O(n log n) for LIS?"
    ),
    (
        "What is the Edit Distance (Levenshtein Distance) problem?",
        "Given strings word1 and word2, find the minimum number of operations (insert, delete, replace) to convert word1 to word2. If characters match, dp[i][j] = dp[i-1][j-1]; else 1 + min(insert, delete, replace).",
        "Advanced",
        "Concept",
        "",
        "What is the time and space complexity of Edit Distance?"
    ),
    (
        "What is Kadane's Algorithm for Maximum Subarray Sum?",
        "Kadane's algorithm keeps a running maxEndingHere and global maxSoFar. For each element x: maxEndingHere = Math.max(x, maxEndingHere + x); maxSoFar = Math.max(maxSoFar, maxEndingHere). Runs in O(n) time and O(1) space.",
        "Easy",
        "Practical",
        "function maxSubArray(nums) {\n  let maxSoFar = nums[0], currMax = nums[0];\n  for (let i = 1; i < nums.length; i++) {\n    currMax = Math.max(nums[i], currMax + nums[i]);\n    maxSoFar = Math.max(maxSoFar, currMax);\n  }\n  return maxSoFar;\n}",
        "What does Kadane's algorithm return if all numbers in the array are negative?"
    ),
    (
        "What is the Maximum Product Subarray problem and how does it differ from Kadane's?",
        "Because multiplying two negative numbers yields a positive product, we must track both the current maximum product and the current minimum product at each index. When encountering a negative number, swap max and min.",
        "Intermediate",
        "Concept",
        "",
        "What is the time complexity of Maximum Product Subarray?"
    ),
    (
        "What is the Unique Paths problem on an m x n grid?",
        "A robot starts at top-left (0,0) and can only move down or right to reach bottom-right (m-1, n-1). dp[r][c] = dp[r-1][c] + dp[r][c-1]. Can be computed in O(m * n) time and O(n) space.",
        "Intermediate",
        "Practical",
        "",
        "Can Unique Paths also be solved directly using combinatorics?"
    ),
    (
        "What is the Partition Equal Subset Sum problem?",
        "Determine if an array can be partitioned into two subsets with equal sum. If the total sum is odd, return false. Otherwise, this reduces to 0/1 knapsack where target capacity is sum / 2.",
        "Intermediate",
        "Concept",
        "",
        "What is the boolean state transition for subset sum?"
    ),
    (
        "What is Matrix Chain Multiplication?",
        "Given a sequence of matrices, find the most efficient way to multiply them to minimize scalar multiplications. Solved using DP in O(n^3) time.",
        "Advanced",
        "Concept",
        "",
        "Does matrix multiplication order affect the final resulting matrix?"
    ),
    (
        "What is the Rod Cutting problem?",
        "Given a rod of length n and prices for various lengths, determine the maximum revenue obtainable by cutting up the rod and selling the pieces. dp[i] = Math.max(price[j] + dp[i - j - 1]) for all j < i.",
        "Intermediate",
        "Concept",
        "",
        "Is Rod Cutting an unbounded knapsack problem?"
    ),
    (
        "What is Tail Recursion and why is it important?",
        "Tail Recursion is a recursion where the recursive call is the very last operation executed in the function. Compilers with Tail Call Optimization (TCO) reuse the current stack frame, avoiding stack overflow.",
        "Intermediate",
        "Concept",
        "// Tail recursive factorial\nfunction fact(n, acc = 1) {\n  if (n <= 1) return acc;\n  return fact(n - 1, n * acc);\n}",
        "Does standard JavaScript engines in V8 currently enable tail call optimization?"
    ),
    (
        "What causes a Stack Overflow error in recursive algorithms?",
        "Every recursive call adds a frame to the call stack. If the recursion depth exceeds the maximum call stack limit (e.g. missing or incorrect base case, or deeply nested input), stack overflow occurs.",
        "Easy",
        "Concept",
        "",
        "How can any recursive algorithm be converted into an iterative algorithm?"
    ),
    (
        "Which of the following problems exhibits the Overlapping Subproblems property?",
        "Computing Fibonacci numbers recursively recalculates the exact same fib(n-2) and fib(n-3) multiple times across the recursion tree.",
        "Easy",
        "MCQ",
        "",
        {"A": "Binary Search", "B": "Fibonacci sequence", "C": "Merge Sort", "D": "Finding array maximum"},
        "B",
        "Why does Merge Sort not exhibit overlapping subproblems?"
    ),
    (
        "What is the space complexity of bottom-up Fibonacci with two state variables?",
        "O(1) auxiliary space because it only maintains the two previous values (prev1, prev2) rather than an array of size n.",
        "Easy",
        "MCQ",
        "",
        {"A": "O(n)", "B": "O(1)", "C": "O(log n)", "D": "O(n^2)"},
        "B",
        "What was the space complexity of the recursive approach?"
    ),
    (
        "What is pseudo-polynomial time in Dynamic Programming?",
        "An algorithm whose running time is polynomial in the numeric value of the input (such as capacity W in 0/1 knapsack) rather than the length of the input in bits.",
        "Advanced",
        "Concept",
        "",
        "Why is 0/1 Knapsack not considered strictly polynomial time?"
    ),
    (
        "What is state compression in dynamic programming?",
        "State compression uses bitmasks (integers where bits represent boolean states) to represent subsets, reducing state representations in problems like Traveling Salesperson.",
        "Advanced",
        "Concept",
        "",
        "What is the typical constraint on N for bitmask DP problems?"
    ),
    (
        "What is the Word Break problem?",
        "Given a string s and a dictionary of strings wordDict, determine if s can be segmented into a space-separated sequence of dictionary words using DP in O(n^2) time.",
        "Intermediate",
        "Concept",
        "",
        "How can a Trie optimize the Word Break lookup?"
    ),

    # --- Tries & Advanced String Data Structures (15 items) ---
    (
        "What is a Trie (Prefix Tree) and how does it store strings?",
        "A Trie is a tree-like data structure used to store strings where each node represents a common prefix character. Words sharing a prefix share ancestral nodes, and an isEndOfWord flag marks completed words.",
        "Intermediate",
        "Concept",
        "class TrieNode {\n  constructor() {\n    this.children = {};\n    this.isEnd = false;\n  }\n}",
        "What is the time complexity to insert a word of length L into a Trie?"
    ),
    (
        "What are the time complexities of insert, search, and startsWith in a Trie?",
        "All three operations run in O(L) time, where L is the length of the string being processed, completely independent of the number of words N stored in the Trie.",
        "Intermediate",
        "Concept",
        "",
        "How does Trie search compare with Hash Map string search?"
    ),
    (
        "Why is a Trie preferred over a Hash Map for autocomplete systems?",
        "A Hash Map can only lookup exact matches in O(L). A Trie can find all strings starting with a given prefix in O(prefix_length + k) where k is the number of results, making it ideal for prefix matching and autocomplete.",
        "Intermediate",
        "Comparison",
        "",
        "What is the trade-off of using a Trie compared to a Hash Map?"
    ),
    (
        "How do you implement the startsWith prefix check in a Trie?",
        "Traverse down the tree character by character. If at any point the next character is not in current.children, return false. If all prefix characters are traversed successfully, return true.",
        "Intermediate",
        "Practical",
        "function startsWith(root, prefix) {\n  let curr = root;\n  for (const ch of prefix) {\n    if (!curr.children[ch]) return false;\n    curr = curr.children[ch];\n  }\n  return true;\n}",
        "How is this different from the exact search method?"
    ),
    (
        "What is a Compressed Trie (Radix Tree or Patricia Trie)?",
        "A Compressed Trie merges sequences of single-child nodes into a single edge with a string label, significantly reducing node count and memory consumption.",
        "Advanced",
        "Concept",
        "",
        "Where are radix trees commonly used in modern web routing frameworks?"
    ),
    (
        "What is a Suffix Tree and Suffix Array?",
        "A Suffix Tree is a trie of all suffixes of a string, enabling substring searches in O(m) time. A Suffix Array is a sorted array of all suffixes, providing similar capabilities with less memory overhead.",
        "Advanced",
        "Concept",
        "",
        "How does a suffix array compare in space consumption with a suffix tree?"
    ),
    (
        "How do you implement Trie node deletion for a word?",
        "Recursively traverse to the end of the word, unmark isEnd. If the node has no other children, delete it and backtrack up, deleting ancestor nodes that have no other children and are not ends of other words.",
        "Advanced",
        "Practical",
        "",
        "Why must you check if a node has other children before deleting it?"
    ),
    (
        "Which of the following data structures is most optimal for implementing a predictive text dictionary?",
        "A Trie allows rapid traversal down shared prefixes to suggest completions.",
        "Easy",
        "MCQ",
        "",
        {"A": "Binary Search Tree", "B": "Trie", "C": "Min-Heap", "D": "Linked List"},
        "B",
        "What is the worst-case space complexity of a Trie with alphabet size Sigma?"
    ),
    (
        "What is the time complexity to check if a word of length L exists in a Trie?",
        "O(L) time because each character corresponds to one pointer traversal in the tree.",
        "Easy",
        "MCQ",
        "",
        {"A": "O(1)", "B": "O(L)", "C": "O(N * L)", "D": "O(log N)"},
        "B",
        "Does the number of words stored in the Trie affect lookup time?"
    ),
    (
        "What is the Aho-Corasick algorithm?",
        "Aho-Corasick is a string-searching algorithm that locates elements of a finite set of strings within an input text simultaneously in linear time by augmenting a Trie with failure links.",
        "Advanced",
        "Concept",
        "",
        "How is Aho-Corasick related to the KMP algorithm?"
    ),

    # --- Bit Manipulation Fundamentals (20 items) ---
    (
        "Explain the primary bitwise operators in programming.",
        "AND (&): 1 if both bits are 1; OR (|): 1 if either bit is 1; XOR (^): 1 if bits differ; NOT (~): inverts all bits; Left Shift (<<): shifts bits left (multiplies by 2); Right Shift (>>): shifts bits right (divides by 2).",
        "Easy",
        "Concept",
        "",
        "What is the difference between arithmetic right shift (>>) and logical right shift (>>>)?"
    ),
    (
        "How do you check if a number is even or odd using bit manipulation?",
        "Evaluate `(n & 1)`. If the result is 0, the least significant bit is 0, meaning the number is even. If 1, the number is odd.",
        "Easy",
        "Practical",
        "const isEven = (n) => (n & 1) === 0;\nconst isOdd = (n) => (n & 1) === 1;",
        "Why is `n & 1` often faster than `n % 2`?"
    ),
    (
        "How do you check if an integer is a power of two using bitwise operators?",
        "A power of two has exactly one bit set in binary (e.g. 8 is 1000). Subtracting 1 flips all bits up to that set bit (8 - 1 = 7 is 0111). Therefore, `n > 0 && (n & (n - 1)) === 0` checks if n is a power of two.",
        "Easy",
        "Practical",
        "const isPowerOfTwo = (n) => n > 0 && (n & (n - 1)) === 0;",
        "What is the result of `n & (n - 1)` for any arbitrary integer n?"
    ),
    (
        "How do you find the single non-repeating element in an array where every other element appears twice?",
        "XOR all elements together. Since `x ^ x === 0` and `x ^ 0 === x`, all duplicate pairs cancel each other out, leaving only the unique element in O(n) time and O(1) space.",
        "Easy",
        "Practical",
        "function singleNumber(nums) {\n  let result = 0;\n  for (const num of nums) result ^= num;\n  return result;\n}",
        "Can this technique work if elements appear three times?"
    ),
    (
        "How do you count the number of set bits (1s) in an integer using Brian Kernighan's Algorithm?",
        "Repeatedly clear the least significant set bit using `n = n & (n - 1)` and increment a counter until n becomes 0. The loop runs exactly once per set bit.",
        "Intermediate",
        "Practical",
        "function countSetBits(n) {\n  let count = 0;\n  while (n > 0) {\n    n = n & (n - 1);\n    count++;\n  }\n  return count;\n}",
        "What is the worst-case number of iterations for a 32-bit integer?"
    ),
    (
        "How do you swap two variables without using a temporary variable via XOR?",
        "`a = a ^ b; b = a ^ b; a = a ^ b;`. Note: this fails if a and b refer to the exact same memory address (e.g. arr[i] with same index).",
        "Easy",
        "Practical",
        "let a = 5, b = 9;\na ^= b;\nb ^= a;\na ^= b;\n// now a is 9, b is 5",
        "Why is modern destructuring `[a, b] = [b, a]` preferred in JavaScript?"
    ),
    (
        "How do you turn on (set) the k-th bit of a number?",
        "Use bitwise OR with a mask: `n = n | (1 << k)`.",
        "Easy",
        "Practical",
        "const setBit = (n, k) => n | (1 << k);",
        "How do you clear (turn off) the k-th bit?"
    ),
    (
        "How do you clear (turn off) the k-th bit of a number?",
        "Use bitwise AND with the inverted mask: `n = n & ~(1 << k)`.",
        "Easy",
        "Practical",
        "const clearBit = (n, k) => n & ~(1 << k);",
        "How do you toggle (flip) the k-th bit?"
    ),
    (
        "How do you toggle (flip) the k-th bit of a number?",
        "Use bitwise XOR with a mask: `n = n ^ (1 << k)`.",
        "Easy",
        "Practical",
        "const toggleBit = (n, k) => n ^ (1 << k);",
        "How do you check if the k-th bit is set?"
    ),
    (
        "How do you check if the k-th bit is set?",
        "Check `(n & (1 << k)) !== 0` or `((n >> k) & 1) === 1`.",
        "Easy",
        "Practical",
        "const isBitSet = (n, k) => ((n >> k) & 1) === 1;",
        "What is the 0-indexed position of the least significant bit?"
    ),
    (
        "What is the result of `5 ^ 5`?",
        "The XOR of any number with itself is 0.",
        "Easy",
        "MCQ",
        "",
        {"A": "5", "B": "0", "C": "10", "D": "1"},
        "B",
        "What is `5 ^ 0`?"
    ),
    (
        "What is the result of `1 << 4`?",
        "Shifting 1 left by 4 positions equals 2^4 = 16.",
        "Easy",
        "MCQ",
        "",
        {"A": "4", "B": "8", "C": "16", "D": "32"},
        "C",
        "What is `16 >> 2`?"
    ),
    (
        "What does `n & (-n)` return in two's complement arithmetic?",
        "It isolates the lowest (least significant) set bit of n.",
        "Intermediate",
        "Concept",
        "",
        "How does two's complement represent negative numbers?"
    ),
    (
        "How do you generate all subsets of a set of size n using bit manipulation?",
        "A set of size n has 2^n subsets. Iterate an integer i from 0 to (1 << n) - 1. If the j-th bit of i is set, include the j-th element in the current subset.",
        "Intermediate",
        "Practical",
        "function subsets(nums) {\n  const n = nums.length, total = 1 << n, res = [];\n  for (let i = 0; i < total; i++) {\n    const sub = [];\n    for (let j = 0; j < n; j++) {\n      if ((i >> j) & 1) sub.push(nums[j]);\n    }\n    res.push(sub);\n  }\n  return res;\n}",
        "What is the time complexity of this power set algorithm?"
    ),
    (
        "What is the Hamming Distance between two integers?",
        "The Hamming Distance is the number of positions at which the corresponding bits are different, calculated by taking XOR of the two numbers and counting set bits: `countSetBits(x ^ y)`.",
        "Intermediate",
        "Practical",
        "",
        "What is the Hamming Weight of an integer?"
    ),

    # --- Debugging & Output DSA Questions (25 items) ---
    (
        "What is the output of the following binary search code when searching for 4 in [1, 2, 3, 5]?",
        "The loop terminates when left (3) exceeds right (2) without finding 4, returning -1.",
        "Easy",
        "Output",
        "const arr = [1, 2, 3, 5];\nlet left = 0, right = arr.length - 1;\nlet found = -1;\nwhile (left <= right) {\n  let mid = Math.floor((left + right) / 2);\n  if (arr[mid] === 4) { found = mid; break; }\n  if (arr[mid] < 4) left = mid + 1;\n  else right = mid - 1;\n}\nconsole.log(found);",
        "What would left and right be after loop termination?"
    ),
    (
        "What is wrong with this recursive tree traversal function?",
        "The base case is missing. Without `if (!node) return;`, calling traversal on a leaf node's null children causes a TypeError: Cannot read properties of null.",
        "Easy",
        "Debugging",
        "function traverse(node) {\n  console.log(node.val);\n  traverse(node.left);\n  traverse(node.right);\n}",
        "How do you fix it?"
    ),
    (
        "What is wrong with this binary search loop condition?",
        "Using `left < right` instead of `left <= right` causes the algorithm to fail when the target is at the single remaining element where left === right.",
        "Intermediate",
        "Debugging",
        "function search(arr, target) {\n  let left = 0, right = arr.length - 1;\n  while (left < right) {\n    let mid = Math.floor((left + right) / 2);\n    if (arr[mid] === target) return mid;\n    if (arr[mid] < target) left = mid + 1;\n    else right = mid - 1;\n  }\n  return -1;\n}",
        "What case fails with `left < right`?"
    ),
    (
        "What is the output of this queue simulation?",
        "Enqueues 10 and 20. shift() removes 10. Enqueues 30. shift() removes 20. Output is 20.",
        "Easy",
        "Output",
        "const q = [];\nq.push(10);\nq.push(20);\nq.shift();\nq.push(30);\nconsole.log(q.shift());",
        "What is remaining in the queue?"
    ),
    (
        "What is the output of this stack simulation?",
        "Pushes 1, 2, 3. pop() removes 3. Pushes 4. pop() removes 4. Output is 4.",
        "Easy",
        "Output",
        "const s = [];\ns.push(1);\ns.push(2);\ns.push(3);\ns.pop();\ns.push(4);\nconsole.log(s.pop());",
        "What element is at the top of the stack now?"
    ),
    (
        "What is wrong with this linked list node insertion at head?",
        "`head = newNode;` is executed before linking `newNode.next = head;`, which overwrites head and loses reference to all previous nodes in the list.",
        "Intermediate",
        "Debugging",
        "function insertHead(val) {\n  const newNode = { val, next: null };\n  head = newNode;\n  newNode.next = head;\n}",
        "What is the correct order of pointer assignments?"
    ),
    (
        "What is the output of this postorder evaluation?",
        "Left child is 2, right child is 3, root is 1. Postorder is Left (2) -> Right (3) -> Root (1).",
        "Easy",
        "Output",
        "const root = {\n  val: 1,\n  left: { val: 2, left: null, right: null },\n  right: { val: 3, left: null, right: null }\n};\nconst res = [];\nfunction post(n) {\n  if (!n) return;\n  post(n.left);\n  post(n.right);\n  res.push(n.val);\n}\npost(root);\nconsole.log(res.join(','));",
        "What would preorder produce?"
    ),
    (
        "What is wrong with this memoized fibonacci implementation?",
        "The memo check `if (memo[n])` fails when n = 0 because memo[0] is 0, which is falsy, causing fib(0) to be recalculated repeatedly. It should be `if (n in memo)` or `if (memo[n] !== undefined)`.",
        "Intermediate",
        "Debugging",
        "const memo = {};\nfunction fib(n) {\n  if (n <= 1) return n;\n  if (memo[n]) return memo[n];\n  return memo[n] = fib(n - 1) + fib(n - 2);\n}",
        "Why is checking for undefined safer than truthiness for numeric memo tables?"
    ),
    (
        "What is the output of this bitwise operation?",
        "12 is 1100 in binary. 10 is 1010 in binary. 1100 & 1010 = 1000 in binary, which is 8.",
        "Easy",
        "Output",
        "console.log(12 & 10);",
        "What is 12 | 10?"
    ),
    (
        "What is the output of this bitwise XOR operation?",
        "7 ^ 7 cancels to 0. 0 ^ 9 is 9.",
        "Easy",
        "Output",
        "console.log(7 ^ 9 ^ 7);",
        "Does the order of XOR operations matter?"
    ),
    (
        "What is wrong with this cycle detection in linked list?",
        "Accessing `fast.next.next` throws a TypeError if `fast.next` is null. The loop condition must check `while (fast && fast.next)`.",
        "Intermediate",
        "Debugging",
        "function hasCycle(head) {\n  let slow = head, fast = head;\n  while (fast) {\n    slow = slow.next;\n    fast = fast.next.next;\n    if (slow === fast) return true;\n  }\n  return false;\n}",
        "How do you fix this null reference error?"
    ),
    (
        "What is the time complexity of this nested loop?",
        "Outer loop runs n times. Inner loop runs 1 + 2 + ... + n = n*(n+1)/2 times. Total time complexity is O(n^2).",
        "Easy",
        "Output",
        "let count = 0;\nfor (let i = 0; i < n; i++) {\n  for (let j = 0; j <= i; j++) {\n    count++;\n  }\n}",
        "What would the complexity be if j doubled each step (j *= 2)?"
    ),
    (
        "What is the time complexity when inner loop variable doubles: `for (let j = 1; j < n; j *= 2)`?",
        "The inner loop executes log2(n) times. With the outer loop running n times, the total time complexity is O(n log n).",
        "Easy",
        "Concept",
        "",
        "What is the time complexity if outer loop also doubles: `for (let i = 1; i < n; i *= 2)`?"
    ),
    (
        "What is wrong with this array reversal function?",
        "Looping up to `arr.length` swaps elements back to their original positions, resulting in no change. The loop must stop at `Math.floor(arr.length / 2)`.",
        "Easy",
        "Debugging",
        "function reverse(arr) {\n  for (let i = 0; i < arr.length; i++) {\n    let temp = arr[i];\n    arr[i] = arr[arr.length - 1 - i];\n    arr[arr.length - 1 - i] = temp;\n  }\n  return arr;\n}",
        "What is the output if called on [1, 2, 3]?"
    ),
    (
        "What is the output of this Kadane's algorithm snippet on [-2, 1, -3, 4, -1, 2, 1, -5, 4]?",
        "The maximum subarray is [4, -1, 2, 1] with a sum of 6.",
        "Intermediate",
        "Output",
        "const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];\nlet maxSoFar = nums[0], curr = nums[0];\nfor (let i = 1; i < nums.length; i++) {\n  curr = Math.max(nums[i], curr + nums[i]);\n  maxSoFar = Math.max(maxSoFar, curr);\n}\nconsole.log(maxSoFar);",
        "What would be the output on [-5, -2, -8]?"
    ),
    (
        "What is wrong with this recursive factorial function?",
        "For negative input n, the condition `if (n === 1)` is never reached, resulting in infinite recursion and RangeError: Maximum call stack size exceeded.",
        "Easy",
        "Debugging",
        "function factorial(n) {\n  if (n === 1) return 1;\n  return n * factorial(n - 1);\n}",
        "How should the base case handle 0 and negative inputs?"
    ),
    (
        "What is the output of `Math.floor((0 + 1) / 2)` and why does it matter in binary search of length 2?",
        "Output is 0, which points to the first element. If left = mid + 1, left becomes 1; if right = mid, it stays 0, preventing infinite loops when handled properly.",
        "Easy",
        "Output",
        "console.log(Math.floor((0 + 1) / 2));",
        "What happens when calculating mid in ceiling division?"
    ),
    (
        "What is the output of this stack reversal using recursion?",
        "Recursion unwinds in reverse order, pushing elements back in reversed order: [3, 2, 1].",
        "Intermediate",
        "Output",
        "const stack = [1, 2, 3];\nfunction insertAtBottom(s, val) {\n  if (s.length === 0) { s.push(val); return; }\n  const top = s.pop();\n  insertAtBottom(s, val);\n  s.push(top);\n}\nfunction reverse(s) {\n  if (s.length === 0) return;\n  const top = s.pop();\n  reverse(s);\n  insertAtBottom(s, top);\n}\nreverse(stack);\nconsole.log(stack);",
        "What is the auxiliary space complexity of reversing a stack with recursion?"
    ),
    (
        "What is wrong with this BST insertion check?",
        "If `val === root.val`, standard BST insertion must either ignore duplicates or explicitly increment a frequency count; this code fails to handle equal keys.",
        "Intermediate",
        "Debugging",
        "function insert(root, val) {\n  if (!root) return { val, left: null, right: null };\n  if (val < root.val) root.left = insert(root.left, val);\n  else root.right = insert(root.right, val);\n  return root;\n}",
        "Where do duplicate values go if allowed in a BST?"
    ),
    (
        "What is the output of `console.log(1 << 0)`?",
        "Shifting 1 by 0 positions leaves 1 unchanged. Output is 1.",
        "Easy",
        "Output",
        "console.log(1 << 0);",
        "What is 1 << 1?"
    ),
    (
        "What is the output of `console.log(~0)` in 32-bit signed integer representation?",
        "Inverting all 0s gives 32 ones, which in two's complement represents -1. Output is -1.",
        "Intermediate",
        "Output",
        "console.log(~0);",
        "What is `~5`?"
    ),
    (
        "What is the result of `console.log(~5)`?",
        "Bitwise NOT inverts bits, where `~x === -(x + 1)`. For 5, `-(5 + 1) = -6`.",
        "Easy",
        "Output",
        "console.log(~5);",
        "What is `~(-1)`?"
    ),
    (
        "What is wrong with this two-sum hash map lookup?",
        "It checks `map[diff]` directly, which evaluates to falsy if the complement is stored at index 0 (`map[diff] === 0`), returning false incorrectly.",
        "Intermediate",
        "Debugging",
        "function twoSum(nums, target) {\n  const map = {};\n  for (let i = 0; i < nums.length; i++) {\n    const diff = target - nums[i];\n    if (map[diff]) return [map[diff], i];\n    map[nums[i]] = i;\n  }\n  return [];\n}",
        "How do you correctly check for key presence in an object?"
    ),
    (
        "What is the output of this Map lookup with numeric keys?",
        "JavaScript Map preserves numeric keys without converting them to strings, returning 'found'.",
        "Easy",
        "Output",
        "const map = new Map();\nmap.set(1, 'found');\nconsole.log(map.get(1));",
        "How does this differ from standard object key coercion?"
    ),
    (
        "What is the output of this Set deduplication on array with primitive types?",
        "Set removes duplicates, leaving [1, 2, 3]. Output length is 3.",
        "Easy",
        "Output",
        "const s = new Set([1, 2, 2, 3, 3, 3]);\nconsole.log(s.size);",
        "Does Set deduplicate object references with identical properties?"
    )
]
