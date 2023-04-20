## 662. (M) Maximum Width of Binary Tree

### `solution.py`
Because of how the width is defined in the problem, we need to somehow keep track of the horizontal position of the nodes within their respective depths. We could use BFS and leverage how it traverses a tree, but we can implement a more general approach that involves labeling nodes with their heap indices. When a binary tree is stored as a heap the nodes are stored in an array, where the children of the $n$th node are stored as the $2n$th and $2n+1$th elements in the array. Now we can keep a dictionary that maps a depth to its smallest and largest heap indices, which we can use to determine the largest width once the traversal has completed.  
The implementation is simple, we traverse the tree (iterative DFS is used here) while keeping track of the nodes' depth and heap index information. Once the traversal has completed we iterate over the values of dictionary `width` to compute the maximum width of the tree.  
  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the number of nodes in the given tree. DFS touches every node exactly once, and computing the maximum width can at most take $n$ time. The space complexity is also $O(n)$.  
  

