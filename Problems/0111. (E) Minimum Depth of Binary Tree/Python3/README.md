## 111. (E) Minimum Depth of Binary Tree

### `solution.py`
There are two ways to determine the minimum depth of a leaf node. We can either traverse all existing leaf nodes of a tree, or traverse the tree in such a way so that shallower leaf nodes are traversed first. Here we implement the latter by using the iterative flavor of BFS, which traverses the tree in level order therby guaranteeing that the shallowest leaf nodes are touched first. Because of this property of BFS, we can return early as soon as a leaf node has been encountered.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the given tree. The space complexity is also $O(n)$.  
  

