## 230. (M) Kth Smallest Element in a BST

### `solution.py`
Since this is a BST we know that an inorder traversal will present the nodes in ascending sorted order. Thus, we can implement an inorder traversal that stops after `k` nodes. This solution implements the iterative version of inorder traversal.  

#### Conclusion
The time complexity is $O(n + k) = O(n + n) = O(n)$, where $n$ is the number of nodes in the BST, and $k$ is the supplied argument `k`. In the worst case of an unbalanced BST where all nodes are skewed to the left, all nodes will be added to `nodes` after which a node will be popped from it `k` times. The space complexity is $O(n)$.  
##### Follow-up
We can layer a doubly linked list on top of the tree (creating something akin to a [B+ tree](https://en.wikipedia.org/wiki/B%2B_tree)), where nodes are arranged in ascending sorted order. Now the time complexity of retrieving the kth smallest element is reduced to $O(k)$, without significantly impacting the performance of insert and delete operations.  
  

