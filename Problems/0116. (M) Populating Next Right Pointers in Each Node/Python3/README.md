## 116. (M) Populating Next Right Pointers in Each Node

### `solution.py`
The variable `Node.next` should point to the node in the tree to its right, and on the same level. As such, the most straightforward approach would be to perform a BFS traversal on the tree, while keeping track of the depth of each node. If a node's depth is different than the previously visited node's depth, we set the next pointer of the previous node to `None`, as requested by the problem. Otherwise, we simply make it point to the current node.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the number of nodes in the tree rooted at `root`. Performing a BFS traversal on a tree with $n$ nodes takes $O(n)$ time and each node takes $O(1)$ time to process, hence the overall time complexity of $O(n)$. The queue used to store untraveled nodes can at most contain $2^h$ nodes(which is the number of leaf nodes in a perfect binary tree with height $h$). Because this value is bound by $n$, the overall space complexity becomes $O(n)$.  
  

