## 863. (M) All Nodes Distance K in Binary Tree

### `solution.py`
While the problem itself is simple enough to understand actually implementing a solution is not as easy as it seems, mostly due to two reasons; we do not have immediate access to the target node, and there is no obvious way to propagate the distance to nodes that are not an ancestor of the target node. These problems arise from the fact that we are given a tree, which is a representation of a directed acyclic graph. Thus if we simply convert the tree into an undirected graph and represent it as a adjacency list, we can solve both problems at once. The conversion process is unremarkable, as we just traverse the tree as normal (with iterative DFS being used here) and add an undirected edge between the current node and its children.  
Once the conversion has completed we now need to find nodes that are `k` distance away from the target node, which can be trivially solved with any graph traversal algorithm(though BFS has been used in the provided solution).  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the number of nodes in the given tree. Converting the tree takes $O(n)$ time as we essentially perform a complete traversal over it while doing a fixed number of operation for each node. The traversal step also takes $O(n)$ time by similar logic. The space complexity is $O(n)$ as well since `adj` also grows in size relative to $n$, despite having a fixed size of 501 in one dimension.  
Any other approach that involves adding additional information to the given tree will most likely exhibit identical time and space complexities. A less 'explicit' approach that augments the provided tree with auxiliary data structures (such as a dictionary) instead of generating an entire graph could be a better solution in a more practical context.  

