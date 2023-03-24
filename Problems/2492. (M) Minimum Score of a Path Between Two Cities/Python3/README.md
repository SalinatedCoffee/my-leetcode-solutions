## 2492. (M) Minimum Score of a Path Between Two Cities

### `solution.py`
An edge can be traversed multiple times, which means that a valid 'path' can contain *all* edges in the graph. The graph may have disconnected components, but we do not care since the problem guarantees that a path exists between nodes `1` and `n`. Thus, we simply need to traverse the graph starting at node `1` and return the smallest edge we encounter.  
We also need to remember to check the edge weight *before* checking if the current node has been visited since we need to touch all edges while avoiding cycles.  

#### Conclusion
This solution has a time complexity of $O(|V|)$ where $|V|$ is the number of nodes in the graph. The space complexity is $O(|E|)$ where $|E|$ is the number of edges in the graph.  
  

