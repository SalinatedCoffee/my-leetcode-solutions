## 1038. (M) Binary Search Tree to Greater Sum Tree

### `solution.py`
Given a binary search tree, we are asked to convert it to a 'greater tree' where the value of each node is the sum of all nodes with values greater than that node in the original BST. If the given tree was a *binary tree*, this problem would have been significantly more difficult. Thankfully, we are given a binary *search* tree, where all nodes in the right subtree of a node has values greater than that of the parent node. We can simply traverse the tree with DFS, visiting the nodes in descending order of their values while maintaining a global sum of values of visited nodes. Visiting the nodes in descending order of their values will guarantee that the global sum is the sum of all nodes with values greater than the current, which allows us to trivially compute the desired value for each node.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the tree rooted at `root`. Traversing a tree with $n$ nodes using DFS takes $O(n)$ time, and because each node takes $O(1)$ time to process, the overall time complexity comes in at $O(n)$. The space complexity is $O(n)$, due to the recursion stack.  
  

