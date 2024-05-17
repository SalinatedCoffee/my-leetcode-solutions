## 1325. (M) Delete Leaves With a Given Value

### `solution.py`
Given a tree, we want to remove all leaf nodes with a value of `target`. The twist is that we want to also remove the leaf nodes resulting from the initial deletions, and then the ones after that, and so on so forth until there are no nodes that can be removed. Instead of the brute force method of traversing the tree multiple times until no nodes are removed, we can evaluate nodes as we traverse the tree. The key is evaluating a node *after* its children have been processed.  
The first order of business is checking whether `root` is not `None`. If it is not, we recurse down both of its children, assigning the return values back to themselves. Finally, we check whether the current node should be removed by looking at its children and value. If the node should indeed be deleted, we simply return `None`. Otherwise we return `root`, the reference to the current node.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the number of nodes in the given tree. Traversing a tree with $n$ nodes takes $O(n)$ time, and processing each node takes $O(1)$ time, which brings the overall time complexity to $O(n)$. The tree is not guaranteed to be balanced, and thus the height of the tree can be at most $n$. While recursively traversing the tree the amount of memory used by the recursion stack scales with its height, bringing the space complexity to $O(n)$.  
  

