## 3243. (M) Shortest Distance After Road Addition Queries

### `solution.py`
There exists `n` cities from city `0` to `n-1`. Initially, the cities are connected by `n-1` directional roads, with each road connecting city `i` to city `i+1`(where `i < n-2`). When given the list of query edges `queries`, we are asked to return a list of resulting values after running each query. A query involves adding the query edge and determining the length of the shortest path between city `0` and city `n-1`. The easiest method would be to add the query edge and run BFS on the graph to determine the shortest distance.  
We implement the function `BFS`, which takes no arguments and returns the distance between node `0` and `n-1` using the current state of the graph. Here, we have opted to implement the iterative version of BFS, using a `deque` as the node queue and `set` to store previously visited nodes. The queries are then processed, adding the edge to the graph before calling `BFS` to determine the shortest distance.  

#### Conclusion
This solution has a time complexity of $O(m(n+m))$, where $n$ is `n` and $m$ is the length of `queries`. Running BFS on a graph with $V$ vertices and $E$ edges requires $O(V+E)$ time to complete. Since the graph contains $n$ nodes and up to $m + n$ edges, we can say that running BFS on the graph will take $O(n+m)$ time to finish. As BFS is run for each and every query, the overall time complexity of this solution comes out to be $O(m(n+m))$. The space complexity is $O(n+m)$, due to the adjacency list `adj` and function `BFS`.  
  

