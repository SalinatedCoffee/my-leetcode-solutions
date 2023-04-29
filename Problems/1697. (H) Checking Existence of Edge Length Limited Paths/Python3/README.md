## 1697. (H) Checking Existence of Edge Length Limited Paths

### `solution.py`
A naïve solution that traverses the graph for each and every query would be slow and inefficient, since it would redundantly traverse over some edges multiple times. Instead, we can generate a new graph that only includes the traversable edges given the distance limit of a query. While this may also seem like it would result in redundant computation, we can avoid having to generate a new graph from scratch for every query by sorting the list of queries by distance limit. This way we can reuse the graph (represented here by a union-find data structure) across queries since the set of traversable edges will only increase as we iterate across the sorted list of queries. We may also sort the list of edges by the edge weight, which allows us to avoid examining edges that we have already included in the graph.  
Now we can iterate over the list of sorted queries, while adding traversable edges to the graph and checking whether the source and destination nodes are connected during each iteration.  

#### Conclusion
This solution has a time complexity of $O(n + e\log e + q\log q)$ where $n$ is the number of nodes, $e$ is the length of `edge_list`, and $q$ is the length of `queries`. Operations on the union-find data structure will take $O(n)$ across the entire running time of the solution, and `edge_list` and `queries` are sorted, which is a linearithmic operation. The space complexity is $O(n+q)$ since `edge_list` and `queries` are sorted in-place (Timsort uses $O(n)$ additional space during runtime) and the union-find data structure uses $O(n)$ space. We also store the original indices for the queries in order to construct the return list, which takes $O(q)$ space.  
  

