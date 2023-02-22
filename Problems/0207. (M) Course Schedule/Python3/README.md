## 207. (M) Course Schedule

### `solution.py`
We first start off by immediately noticing that a course sequence is not feasible if it has a cycle in it, as the prerequisites would never be satisfiable. So we need to traverse the course sequence graph as defined in `prerequisites` and determine if it contains a cycle, which relates to [topological sort](https://en.wikipedia.org/wiki/Topological_sorting). A modified version of DFS may be used here, where nodes are marked as either unvisited, temporarily visited, or permanently visited. If a temporary node is revisited, that indicates that a cycle is present in the graph.  
One more thing to remember is that the graph may not be connected, so we need to run the algorithm on all available sources.  
  
#### Conclusion
The solution has a time complexity of $O(|E|+|V|)$, where $|E|$ is the number of prerequisite pairs and $|V|$, the number of courses. The space complexity is $O(|V|)$ as the recursion stack will at most have a depth of $|V|$.  
  

