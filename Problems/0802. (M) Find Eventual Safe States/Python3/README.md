## 802. (M) Find Eventual Safe States

### `solution.py`
The goal is to determine whether all paths starting at a node leads to a node with no outgoing edges, for every node. This in essence simply translates to finding nodes that do not lead to a cycle in the graph. We can detect cycles with DFS, by keeping track of the visited nodes in the current path separately. This is different than the usual set of visited nodes, as this will keep track of the nodes visited in the current path being traversed rather than all nodes that have been touched over the entire traversal. DFS traverses down a path until it terminates, after which it will backtrack and traverse down a branching path that was most recently ignored. Due to this, it is essential that we keep track of the traversed nodes in the current path separately as in order to detect a cycle we need that information to determine whether a node is relevant or not. Since we want to remember which nodes lead to a cycle we do not reinitialize the two visited sets between DFS traversals.  
Once all the traversals have been completed, we simply return a list of nodes that are not marked as leading to a cycle.  

#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ is the number of edges in the graph, and $n$ is the number of nodes. Because the set of visited nodes is preserved between DFS runs, the entire graph will be traversed over once. The running time of DFS is $O(|V|+|E|)$, where $|V| = n$ is the number of vertices (nodes) in the graph and $|E| = m$ is the number of edges. The space complexity is $O(n)$ since the recursion stack will at most be $O(n)$ deep, and `visited` and `cur_visited` both use $O(n)$ memory each.  
  

