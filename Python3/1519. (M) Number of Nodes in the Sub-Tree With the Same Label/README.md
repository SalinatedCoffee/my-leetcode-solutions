## 1519. (M) Number of Nodes in the Sub-Tree With the Same Label

### `solution.py`
This problem is similar to #1443 in that the nodes may not be sequentially numbered (and indeed, there are test cases that check for this) and so we will also take a similar approach by generating an adjacency list for all nodes. Then we need to realize that we want to perform DFS since the count of a node's label depends on the letter counts of its subtrees. Thus we can devise a recursive algorithm where the return value is the label count of all descendants, and the base case is when a node is a leaf. During the recursive case we take the sum of label counts of all subtrees, increment the current node's label count by 1, and finally update the current label count in the return list.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the number of nodes since we traverse all nodes in the tree. The space complexity is $O(n+E)$ where $E$ is the number of edges since we keep the adjacency list in memory which is the dominating factor. `dfs()` uses constant memory at reach recursion level (at most, 2 lists of length 26 are kept in memory), and reaches a maximum recursion depth of $h$ (the height of the tree).  
