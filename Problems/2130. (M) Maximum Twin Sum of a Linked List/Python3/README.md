## 2130. (M) Maximum Twin Sum of a Linked List

### `solution.py`
There are many ways to approach this problem, where the easiest being to simply store references to all nodes in a list. For this solution we store the nodes in a deque and pop from both sides of it to access a node pair, but storing them in a list and accessing nodes by indices instead would also be a valid approach (with possibly less overhead of push/popping items).  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the number of nodes in the given linked list. `nodes` will at most contain $n$ items, and every node is touched exactly twice.  
  

### `solution_2.py`
If we are allowed to modify the input, we can avoid using extra memory by reversing one half of the linked list. Here we use two pointers where `fast` moves at double the speed of `slow` to find the middle node of the linked list. From there, we re-traverse the first half while reversing it. Then we may simply traverse both halves simultaneously while computing the sum of node pairs.  

#### Conclusion
The time complexity is $O(n)$ since the linked list is traversed twice (excluding the reversal step). The space complexity is $O(1)$.  
  

