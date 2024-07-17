## 1110. (M) Delete Nodes and Return Forest

### `solution.py`
Given the root of a binary tree and the list of integers `to_delete`, we are asked to return a list of root nodes of the forest created by removing all nodes with values in `to_delete` from the original tree. When a node is removed we need to make sure that it is unlinked from its parent, and that its children are added to the list of roots(unless they too need to be deleted). We can traverse the tree using recursive DFS while removing nodes at the same time, since the recursion stack will hold the context of all ancestors of the current node regardless of whether it has been deleted. To do this, we need 2 more pieces of information along with the reference to the node currently being considered. We need a reference to its parent, and which child the current node is. This way when a node has to be removed we can easily access its parent and unlink the appropriate child.  
The function `recurse` has 3 parameters `node`, `parent`, and `left`. When it is first called, it determines whether `node` is a root by checking the value of `parent`. If it is `None` and `node.val` is not in `to_delete`, `node` is indeed a root and is added to the list of root nodes `self.ret`. `node` is then unlinked from `parent` if it needs to be deleted, after which `recurse` is called on the children of `node`. Once the traversal is completed, `self.ret` will contain the root nodes of the forest created by deleting nodes from the original given tree.  

#### Conclusion
This solution has a time complexity of $O(n + m)$ where $n$ is the number of nodes and $m$ is the length of `to_delete`. Initializing a set using the contents of `to_delete` takes $O(m)$ time, with the following DFS step taking $O(n)$ time to complete. The space complexity is also $O(n + m)$, due to the recursion stack and the set `to_delete_set`.  
  

