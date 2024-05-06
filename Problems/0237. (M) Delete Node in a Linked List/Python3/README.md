## 237. (M) Delete Node in a Linked List

### `solution.py`
Given a reference to a node in a linked list, we are asked to delete the given node from its list. As we are not given a reference to the head of the linked list we cannot remove `node` directly since we do not have a reference to the previous node. Instead, we can overwrite the target node with its successor(which is guaranteed to exist) and delete the successor.  

#### Conclusion
The solution has a time and space complexity of $O(1)$.  
  

