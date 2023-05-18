## 1557. (M) Minimum Number of Vertices to Reach All Nodes

### `solution.py`

The minimum number of vertices in this problem translates to the number of disconnected components in the graph. We must be able to reach all nodes while keeping the number of source nodes to a minimum - and so it stands to reason that the absolute minimum number of source nodes would be equal to the number of connected components in the given graph. However, the graphs in this problem are directed and thus we cannot simply count the components and return that number as-is. The main problem is that when two nodes are connected by an edge, it is not necessarily true that one node is reachable from the other node. For example, if we have two nodes `1` and `2`, and a directed edge `[1, 2]`, we can reach node `2` from node `1` but not the other way around. In other words, if a node has an *incoming* edge, it can be said that it is reachable through some other node. Nodes that do not have an incoming edge would mean that we must traverse that node separately since it is unreachable by any other node in the graph. Thus we can simply count the number of nodes that do not have any incoming edges, which is the desired return value. Since the graph is acyclic, a component is guaranteed to have at least one such node, which makes this approach possible.  

The actual implementation is simple. We construct an adjacency list `adj` where `adj[i]` is the list of nodes that have outgoing edges into nodes `i`. Then iterating over `adj`, we count the number of empty lists and return that number.  

#### Conclusion

This solution has a time complexity of $O(|E| + |V|)$ where $E$ is the number of edges in the graph, which is the length of `edges` and $V$ is `n`. We iterate over `edges` once while populating `adj`, and later iterate over `adj` once in the counting step. The space complexity is also $O(|E| + |V|)$ since `adj` uses space for nodes with no incoming edges due to how it is initialized.  


