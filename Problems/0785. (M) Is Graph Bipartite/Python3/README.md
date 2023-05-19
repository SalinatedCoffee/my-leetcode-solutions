## 785. (M) Is Graph Bipartite?

### `solution.py`

When a bipartite graph is partitioned into two groups, there should be no edges between nodes of the same group. That is, the source node and destination node of *all* edges cannot be in the same set. Using this property, we can take a DFS-based approach where we 'color' nodes in an alternate fashion as the graph is traversed (2-coloring). The order of the coloring does not matter even if the graph has disconnected components, because the graph is undirected which guarantees that a DFS traversal will fully color a connected component of which the source node is a part of.  

We store the colorings in the list `coloring`, which is initialized to `None`. Then, we attempt a DFS traversal starting at each and every node. During traversal we simply skip a node if it has already been traveled (`coloring[i] is not None`) or return `False` immediately if the current node is already colored but has a different color than expected.  

When the outer for loop has exited we know that the graph is 2-colorable, and thus is bipartite.  

#### Conclusion

The time complexity of this solution is $O(|V|)$, where $|V|$ is the number of nodes in the given graph (which is the length of `graph`). We perform a DFS traversal which takes $O(|V|)$ time, hence the total running time of the same order. The space complexity is also $O(|V|)$, since we use `graph` as-is without generating a separate adjacency list, and `coloring` has a length of $|V|$.  


