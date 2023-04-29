## 1372. (M) Longest ZigZag Path in a Binary Tree

### `solution.py`
We are asked to find the length of the longest zig-zag path in a given binary tree. Traversing the tree is trivial, but how can we traverse the tree in a zig-zag motion? The trick here is realizing that we do not have to explicitly traverse the tree in such a fashion, but instead updating the length of the current path being traversed depending on the most recently taken direction. For example, say we have a binary tree that looks like this: `[0,1,2,None,4,None,None]`. Examining the path `0`,`1`,`4`, the first leg (`0`,`1`) is obviously a valid path with a length of 1. The next leg (`1`,`4`) combined with the previous leg is also a valid path, since node `1` itself is a *left* child of its parent and we moved to the *right* of node `1` to node `4`. Thus, during a binary tree traversal we only need one piece of additional information to determine whether a path is zig-zaging or not - and that is whether the current node is the left or right child of its parent. If it is the left child, we can recurse on the left child passing it a path length of 1 since the zig-zag 'chain' is broken and the leg is the first leg of whatever path it is a part of. The right child can be recursed on in a similar fashion, passing the current path length + 1 instead.  
A simple recursive DFS solution will be sufficient here, where the recursive function `dfs()` takes three arguments; the current node being traversed, the node's position relative to its parent (left or right child node), and the current path length. We then change the parameters of the recursive calls based on the value of the second argument.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the number of nodes in the tree. DFS touches all nodes in the tree exactly once, and the recursion stack can at most be $n$ long as the tree is not guaranteed to be balanced.  
  

