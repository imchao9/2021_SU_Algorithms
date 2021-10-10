---
typora-root-url: img
---



[TOC]



### Array Cheat Sheet

- **Quick summary**: a collection that stores elements in order and looks them up by index.
- **Also known as**: fixed array, static array.
- Important facts:
  - <u>Stores elements sequentially, one after another.</u>
  - Each array element has an index. <u>Zero-based indexing is used most often</u>: the first index is 0, the second is 1, and so on.
  - Is created with a fixed size. Increasing or decreasing the size of an array is impossible.
  - Can be one-dimensional (linear) or multi-dimensional.
  - Allocates memory space contiguously for all its elements.
- **Pros:**
  - Ensures <u>constant time access by index</u>.
  - Constant time append (insertion at the end of an array).
- **Cons:**
  - Fixed size that can't be changed.
  - Search, insertion and deletion are `O(n)`. After insertion or deletion, all subsequent elements are moved one index further.
  - Can be memory intensive when capacity is underused.
- **Notable uses :**
  - The String data type that represents text is implemented in programming languages as an array that consists of a sequence of characters plus a terminating character.
- **Time complexity (worst case):**
  - Access: `O(1)`
  - Search: `O(n)`
  - Insertion: `O(n)` (append: `O(1)`)
  - Deletion: `O(n)`
- See also:
  - [A Gentle Refresher Into Arrays and Strings](https://algodaily.com/lessons/a-gentle-refresher-into-arrays-and-strings/?view=article)
  - [Interview Problems: Easy Strings](https://algodaily.com/categories/easy-strings)
  - [Interview Problems: Basic Arrays](https://algodaily.com/categories/arrays)
  - [Interview Problems: Medium Arrays](https://algodaily.com/categories/medium-arrays)



### Linked-List Cheat Sheet

- **Quick summary**: a linear collection of elements ordered by links instead of physical placement in memory.
- **Important facts:**
  - Each element is called a node.
    - The first node is called the ***head***.
    - The last node is called the ***tail***.
  - Nodes are sequential. Each node stores a reference (pointer) to one or more adjacent nodes:
    - In a **singly linked list**, each node stores a reference to the next node.
    - In a **doubly linked list**, each node stores references to both the next and the previous nodes. This enables traversing a list backwards.
    - In a **circularly linked list**, the tail stores a reference to the head.
  - Stacks and queues are usually implemented using linked lists, and less often using arrays.
- **Pros:**
  - Optimized for fast operations on both ends, which ensures constant time insertion and deletion.
  - Flexible capacity. Doesn't require setting initial capacity, can be expanded indefinitely.
- **Cons:**
  - Costly access and search.
  - Linked list nodes don't occupy continuous memory locations, which makes iterating a linked list somewhat slower than iterating an array.
- **Notable uses:**
  - Implementation of stacks, queues, and graphs.
- **Time complexity (worst case):**
  - Access: `O(n)`
  - Search: `O(n)`
  - <u>Insertion:</u> `O(1)`
  - Deletion: `O(1)`
- See also:
  - [What Is the Linked List Data Structure?](https://algodaily.com/lessons/what-is-the-linked-list-data-structure?view=article)
  - [Implement a Linked List](https://algodaily.com/challenges/implement-a-linked-list/?view=article)
  - [Interview Problems: Linked Lists](https://algodaily.com/categories/linked-lists)



### Hash Map Cheat Sheet

- **Quick summary**: <u>unordered collection that maps keys to values using hashing.</u>

- **Also known as**: hash, hash map, map, unordered map, dictionary, associative array.

- **Important facts:**

  - Stores data as key-value pairs.
  - Can be seen as an evolution of arrays that removes the limitation of sequential numerical indices and allows using flexible keys instead.
  - For any given non-numeric key, *hashing* helps get a numeric index to look up in the underlying array.
  - If hashing two or more keys returns the same value, this is called a ***hash collision*.** To mitigate this, instead of storing actual values, the underlying array may hold references to linked lists that, in turn, store and return all values with the same hash.
  - A *set* is a variation of a hash table that stores keys but not values.

- **Pros:**

  - Keys can be of many data types. The only requirement is that these data types are hashable.
  - Average search, insertion and deletion are `O(1)`.

- **Cons:**

  - Worst-case lookups are `O(n)`.
  - No ordering means <u>looking up minimum and maximum values is expensive.</u>
  - Looking up the value for a given key can be done in constant time, but looking up the keys for a given value is `O(n)`.

- Notable uses:

  - Caching.
  - Database partitioning.

- **Time complexity (worst case):**

  - Access: `O(n)`
  - Search: `O(n)`
  - Insertion: `O(n)`
  - Deletion: `O(n)`

- See also:

  - [Interview Problems: Hash Maps](https://algodaily.com/categories/hash-maps)
  - https://algodaily.com/categories/hash-maps

  

### Binary Search Tree Cheat Sheet

- **Quick summary**: a kind of binary tree where nodes to the left are smaller, and nodes to the right are larger than the current node.
- **Important facts:**
  - Nodes of a binary search tree (BST) are ordered in a specific way:
    - All nodes to the left of the current node are smaller (or sometimes smaller or equal) than the current node.
    - All nodes to the right of the current node are larger than the current node.
  - Duplicate nodes are usually not allowed.
- Pros:
  - Balanced BSTs are moderately performant for all operations.
  - Since BST is sorted, reading its nodes in sorted order can be done in `O(n)`, and search for a node closest to a value can be done in `O(log(n))`
- Cons:
  - Same as trees in general: no constant time operations, performance degradation in unbalanced trees.
- Time complexity (worst case):
  - Access: `O(n)`
  - Search: `O(n)`
  - Insertion: `O(n)`
  - Deletion: `O(n)`
- Time complexity (average case):
  - Access: `O(log(n))`
  - Search: `O(log(n))`
  - Insertion: `O(log(n))`
  - Deletion: `O(log(n))`
- See also:
  - [An Intro to Binary Trees and Binary Search Trees](https://algodaily.com/lessons/an-intro-to-binary-trees-and-search-trees)
  - [Interview Problems: Binary Search Trees](https://algodaily.com/categories/binary-search-trees)
  - https://algodaily.com/categories/arrays





## Algorithms should I choose for a coding question?

If input array is sorted then

- Binary search
- Two pointers

If asked for all permutations/subsets then
- Backtracking

If given a tree then
- DFS
- BFS

If given a graph then
- DFS
- BFS

If given a linked list then
- Two pointers

If recursion is banned then
- Stack

If must solve in-place then
- Swap corresponding values
- Store one or more different values in the same pointer

If asked for maximum/minumum subarray/subset/options then
- Dynamic programming

If asked for top/least K items then
- Heap

If asked for common strings then
- Map
- Trie

Else
- Map/Set for O(1) time & O(n) space
- Sort input for O(nlogn) time and O(1) space
