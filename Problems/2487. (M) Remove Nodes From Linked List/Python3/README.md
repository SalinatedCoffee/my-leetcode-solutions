## 2487. (M) Remove Nodes From Linked List

### `solution.py`
Given the head of a singly linked list, we are asked to remove any nodes where there exists a node with a larger value to its right. Immediately we can see that we can use a monotonic stack to store nodes as we traverse the list, linking these nodes back into a linked list after all nodes in the original have been examined. We first initialize a sentinel node with the value `float('inf')` that will allow us to avoid having to implement edge case handling. After linking this node to `head`, we start traversing the linked list, popping from the stack any nodes with value less than that of the current node `cur`. Once the list has been traversed `stack` will contain all relevant nodes in descending order, allowing us to link them in that order back into a linked list. The next node of the sentinel node is the head of the new linked list, which we can return directly.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of the linked list with the node `head` as its head node. The linked list is traversed exactly once, and operations on the stack can happen $O(n)$ time over the course of this traversal. As the linking operation after the traversal also takes $O(n)$ time, the overall time complexity for this solution is $O(n)$. The space complexity is also $O(n)$, due to `stack`.  
  

