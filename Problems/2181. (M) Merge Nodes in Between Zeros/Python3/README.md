## 2181. (M) Merge Nodes in Between Zeros

### `solution.py`
Given the head of a singly linked list that contains integers 'delimited' by `0`s, we are asked to return the head of another linked list where each node contains the sum of the nodes between `0`s in the original list. For example, if the given linked list is `[0, 3, 1, 0, 2, 0]`, the modified list would be `[4, 2]`. It is guaranteed that the value of the head and tail nodes is `0`, no adjacent nodes will both be `0`, and the length of the linked list is at least 3(in other words, the modified list will have at least one node). While the word 'modify' is used in the problem description we do not have to actually reuse the nodes in the given list, but can create new nodes instead. We can easily solve this problem by maintaining 2 pointers; one points to the current node in the given linked list, and the other points to the tail node of the modified linked list. The sum of node values is computed while the original linked list is traversed, and whenever a value of `0` is encountered a new node with the sum as its value is linked to the tail of the modified linked list. Once all nodes in the original list have been examined, we simply return the head of the newly created list.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of the linked list with `head` as its head node. The given linked list is traversed exactly once, and since processing each node takes $O(1)$ time to complete the overall time complexity will be $O(n)$. The space complexity is $O(1)$, excluding the space required to store the nodes that are returned.  
  

### `solution_2.py`
Because the length of the given list is always greater than or equal to the length of the modified list, we can reuse the nodes in the given list instead of instantiating new nodes. The algorithm is mostly the same, with the only difference being what `new_cur` points to. Instead of it pointing to the tail node of the newly created list, we change it so that it points to the last modified node in the original list(which is essentially the tail node of the modified list). Of course, we need to remember to properly terminate the overwritten section of the linked list before returning its head.  

#### Conclusion
The time and space complexity of this solution is identical to the previous solution. In practice however, this solution will be faster and use less memory than the previous one since the overhead of instantiating new `ListNode`s is eliminated.  
  

