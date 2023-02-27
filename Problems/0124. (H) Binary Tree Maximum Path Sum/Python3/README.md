## 124. (H) Binary Tree Maximum Sum

### `solution.py`
Since a path cannot visit a node more than once, we can immediately see that a path passing through the root of a subtree cannot extend to the subtree's ancestors. Thus we only need to consider the left and right subtree sums at a given node, which maps nicely to recursive DFS traversal. We recursively retrieve the maximum sum of paths starting at the left and right child, then check whether the path that starts in one subtree and ends at the other has a sum larger than the current largest. The return value is the larger sum between the left and right subtree path + current node.  
Note that we can save a lot of hassle by restricting the return value to non-negative values.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the number of nodes in the binary tree. Every node is traversed exactly once, and since the tree is not guaranteed to be balanced the recursion stack can take up to $O(n)$ space.  
  

