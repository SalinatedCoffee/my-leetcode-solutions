## 2331. (E) Evaluate Boolean Binary Tree

### `solution.py`
Given a full binary tree, we are asked to evaluate its contents and return the resulting boolean. The value of a node can be any integer between `0` and `3` inclusive; a value of `0` means that the node's value is `False`, `1` means `True`, `2` means the evaluated value of logical ORing the values of the left and right children, and `3` means the resulting value of logical ANDing the children's values. As typical of tree problems, this one too can be trivially solved by using recursion. If the node's value is `0` or `1`, we simply return the appropriate value as the node is a leaf node. Otherwise, we recurse down both children and use the returned values to evaluate the appropriate logical operation.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the number of nodes in the given binary tree. Recursively traversing a tree with $n$ nodes takes $O(n)$ time, and the compuation performed for each node takes $O(1)$ time. Thus, the overall time complexity will come out to be $O(n)$. The recursion stack is the only component where the memory usage scales according to the size of the input. As the given tree is not guaranteed to be balanced, the size of the recursion stack is $O(n)$.  
  

