## 958. (M) Check Completeness of a Binary Tree

### `solution.py`
A binary tree can be expressed as an array, where the children of node at index `i` are stored at indices `2*i+1` and `2*i+2`, respectively. If we allow a 'child' of a leaf node to occupy a space in the array, we can see that the length of the array of nodes for an incomplete tree with `n` nodes will be either equal to or larger than `n` (0-indexed) since the 'child' nodes of a leaf will take up space and 'push' the other nodes to the right. Using this property we can traverse a tree via DFS and determine whether the given tree is complete or not. If at a node we know the index of that node and the total number of nodes in the tree it is trivial to check if the tree is complete. Otherwise we recurse on the left and right subtrees passing index values of `2*i+1` and `2*i+2` respectively, as mentioned previously.  

#### Conclusion
This solution has a time and space complexity of $O(n)$ where $n$ is the number of nodes in the tree. DFS visites each node exactly once, and the maximum recursion depth is $n$ as the given tree may not be balanced.  
  

