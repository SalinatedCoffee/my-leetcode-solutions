## 872. (E) Leaf-Similar Trees

### `solution.py`
We essentially want to traverse the leaves in both trees in identical order(eg. left to right) and compare the ordering between the two given trees. Because the ordering of the leaves is defined as the 'horizontal' ordering instead of the vertical, we want to traverse the tree in a way that we would encounter the leaves in that ordering. BFS would be a poor fit for this problem as it would traverse the tree level by level, which is not at all what we want. Instead, we can use DFS to traverse the tree, keeping track of each leaf as they are encountered.  
The function `dfs(node, leaves)` takes a `TreeNode` and a list as its argument. It first tries to recurse down `node`'s children, and if `node` is determined to be a leaf, `node.val` is added onto `leaves`. We make one call to `dfs` for each tree, and compare the list of leaf nodes. If at any point a mismatch is found, we immediately return `False`. Otherwise, we return `True`.

#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ and $n$ are the number of nodes in the tree rooted at `root1` and `root2`, respectively. Performing DFS takes $O(|E|+|V|)$ time, and the entirety of each tree is traversed using DFS. The space complexity is also $O(m+n)$ as the number of leaves in either tree is $O(m)$ and $O(n)$, which is stored in lists `a` and `b`.  
  

