## 3217. (M) Delete Nodes From Linked List Present in Array

### `solution.py`
Given the node `head`, the head node of a singly linked list and list of unique integers `nums`, we are asked to remove all nodes that have a value that appears in `nums` from the linked list. We can trivially solve this problem by simply converting `nums` into a set and iterating over the linked list, removing a node if its value appears in `nums`. A sentinel node is added before `head` to make the deletions a little bit easier.  

#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ is the length of `nums` and $n$ is the length of the linked list that has `head` as its head node. Instantiating a set using the contents of `nums` takes $O(m)$ time, and the traversal step that follows requires $O(n)$ time to complete since it visits all nodes in the linked list with each node taking $O(1)$ time to process. The space complexity is $O(m)$, due to the set `delete`.  
  

