## 86. (M) Partition List

### `solution.py`
We want to rearrange the given singly linked list based on the value `x`, where the first partition contains nodes with values smaller than `x` and the second contains nodes with values larger than or equal to `x`. Since the linked list is unsorted, we **must** traverse the entierety of the list in order to identify which nodes to place in which partition. We initialize a pair of pointers for each partition, where one pointer points to a sentinel node and the other points to the tail node of the partition. While traversing the linked list then, we attach the current node to its appropriate partition based on its value. After the traversal has completed, we append the right-side partition to the end of the left-side partition and ensure the tail node points to `None` before returning the `ListNode.next` instance variable of the left partition's sentinel node.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the number of nodes in the linked list that has `head` as its head node. The linked list is traversed once, and only a fixed number of operations are performed for each node. The space complexity is $O(1)$ as we rearrange the nodes in the provided linked list instead of instantiating new ones.  
  

