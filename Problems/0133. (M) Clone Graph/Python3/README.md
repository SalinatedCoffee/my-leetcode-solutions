## 133. (M) Clone Graph

### `solution.py`
Getting to all of the original nodes is the easy part, we can use any traversal algorithm that touches all nodes and edges in the graph. Here we will be implementing the solution using BFS. The (slightly) trickier part is copying the nodes and accessing them later. We obviously want only one copy of each node, which fortunately is analogous to keeping a set of visited nodes. If a node's copy exists (that is, a node has been visited) we only want to add the edge between the current (copied) node and it. If it doesn't, we create a new `Node` object and add it to a dictionary keyed with its value.  
After the traversal exists we simply return the copied node with a value of `1` per the problem description.  
  
#### Conclusion
The time complexity of this solution is $O(|V|+|E|)$, where $|V|$ is the number of nodes and $|E|$ the number of edges in the graph. The space complexity is $O(|V|)$, as `copied` will hold one copy of all nodes in the original graph.  
  

