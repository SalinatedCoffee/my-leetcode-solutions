## 206. (E) Reverse Linked List

### `solution.py`
In order to reverse a singly linked node, we simply need to make the node point to the node that points to it. A iterative solution can be trivially implemented by maintaining 2 pointers during iteration; one pointing to the previous node, and another pointing to the current node being processed. We temporarily store the reference to the next node of the current, after which we make the current node point to the previous node instead. Then the two pointers are updated, with the current node now being the previous node and the temporarily stored next node the current. When the pointer to the current node `cur` points to `None`, we have reached the end of the list and we return the pointer to the previous node `prev`. Note that this also handles the case where an empty list is given; the while block will be skipped entirely, returning the initial value of `prev`, which is `None`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the number of nodes in the linked list that has the node `head` as its head. The linked list is iterated over once, and each node takes $O(1)$ time to reverse. The space complexity is $O(1)$ as we only use a handful of variables of a fixed size.  
  

