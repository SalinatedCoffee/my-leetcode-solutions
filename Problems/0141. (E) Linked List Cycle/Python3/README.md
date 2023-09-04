## 141. (E) Linked List Cycle

### `solution.py`
The naïve solution is slow, but trivial - we simply maintain a list of all previously traversed nodes, and whenever we move on to the next node we check it against this list to determine if it has been traversed before. However, there is a much faster solution that also has constant space complexity as suggested by the follow-up question. We traverse the list using two pointers, where one pointer will traverse one node each turn and the other two nodes per turn. This way, if the list does indeed have a cycle, these two pointers will eventually point to the same node at which point we can simply return `True`. If the faster pointer becomes `None` at any point in the traversal, the list is acyclic and we return `False`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of the linked list starting with node `head`. The linked list is traversed in a linear fashion, and at each node we perform a fixed number of operations that take constant time. The space complexity is $O(1)$, as requested by the follow-up question.  
  

