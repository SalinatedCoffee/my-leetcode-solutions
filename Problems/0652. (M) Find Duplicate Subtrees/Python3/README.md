## 652. (M) Find Duplicate Subtrees

### `solution.py`
Recursion is a tree problem's best friend, and by intuition we know that we could recursively get the left and right subtrees of a node and try matching it against previously seen subtrees. Admittedly my first try was a failure, where I tried to match a subtree through the current node's structure (value of node and its children) and whether if the left and right subtrees were duplicates. This however raised false positives on partial matches as the recursive function returned `True` on `None` nodes, thus falsely matching subtrees with extra leaf nodes.  
To explicitly match the entire subtree then, I decided to recursively construct an inorder string representation (with delimiters) of a subtree. Inorder was chosen specifically to avoid confusion with values comprised of the same number such as `[11,1,111]` - for example, the preorder representation of this tree would be `"111111."`, which is not a representation that is exclusive to this tree. Then the problem becomes trivial, where we implement a recursive DFS traversal that recursively retrieves the inorder string representations of the subtrees and uses that to see whether a duplicate has previously been encountered. We also use a dictionary keyed with the string representation of a subtree as the resulting list of nodes cannot contain duplicate subtrees.  

#### Conclusion
This solution has a running time of $O(n)$ where $n$ is the number of nodes in the given tree. The DFS traversal visits each node exactly once, hence the time complexity of $O(n)$. The space complexity is $O(n^2)$ since `self.seen` may contain subtrees rooted at each node, and the worst case length of the string representation is $n$ (the root).  
  

