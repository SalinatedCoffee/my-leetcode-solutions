## 876. (E) Middle of the Linked List

### `solution.py`
This problem can be trivially solved by iterating over the list while storing references to the nodes in a list, but a more optimal solution can be implemented by using the 'tortoise and hare' method. 2 pointers are maintained, where one is advanced by 1 node and the other by 2 nodes. Whenever the faster pointer reaches the end of the list, the slower pointer will be pointing to the desired node. One detail to keep in mind is that we are asked to return the 'second' middle node if the list is of even length. Advancing the two pointers already achieves this, but it also returns the node after the middle node if the list has an odd length. To address this issue we simply add another check in the while loop, which is to check whether the next node of the fast pointer is not `None`. If it is `None`, it means that the fast node is the last node, and we exit the while loop.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the number of nodes in the given linked list. The space complexity is $O(1)$.  
  

