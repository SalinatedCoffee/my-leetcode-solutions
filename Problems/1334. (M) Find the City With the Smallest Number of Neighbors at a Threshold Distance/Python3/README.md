## 1334. (M) Find the City With the Smallest Number of Neighbors at a Threshold Distance

### `solution.py`
In a graph with `n` nodes(0-indexed) and weighted undirected edges `edges` where an edge `(u, v, w)` has `u` as the source node, `v` as the destination node, and `w` as its weight, we are asked to find a node with the smallest number of reachable nodes. A node is reachable from another node when the shortest path between them have a length of at most `distanceThreshold`. We obviously want to find the distance of the shortest paths between a node and all other nodes, for every node in the graph. We could simply choose any path-finding algorithm and run it for each node in the graph, but since the [Floyd-Warshall](https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm) algorithm finds the shortest distance matrix for all nodes without any modifications we can run it once and iterate over the distance matrix.  
`edges` is iterated over first in order to initialize the distance matrix `dists`. Floyd-Warshall is then run on the initialized distance matrix, after which we iterate from the `0`th node to the `n-1`th node, using the updated distance matrix `dists` to determine whether a node meets the specified criteria.  

#### Conclusion
This solution has a time complexity of $O(n^3)$, where $n$ is `n`(the number of nodes in the graph). Initializing `dists` takes $O(n^2)$ time, while the edge relaxation step takes $O(n^3)$ time. After this step, the entirety of `dists` is iterated over in order to determine the desired node, which requires $O(n^2)$ time to complete. Thus, the overall time complexity of this solution is $O(n^3)$. The space complexity is $O(n^2)$.  
  

