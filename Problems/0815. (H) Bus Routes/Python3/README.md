## 815. (H) Bus Routes

### `solution.py`
Identifying this problem as a graph problem is easy, and the implementation is mostly straightforward as well. Thinking about each bus route as a node, where two nodes that share one or more stops are connected by an edge, we can determine the length of the shortest path between `source` and `target` using BFS.  
We first need to convert `routes` into an adjacency list that we can use. When given a stop, we want to know which bus routes we can take at that stop since the origin and destination are given to us as stops rather than bus routes. Initializing a `defaultdict` `adj`, we populate the dictionary so that `adj[i]` contains a list of all bus routes that contain the stop `i`. Now we can start traversing the graph using BFS, starting at `source` with a distance of `0`. There are two subtleties that require attention during the traversal. One is that we need to keep track of the visited **routes** instead of stops in order to use less memory(failing to do so will result in MLE), and another is that we need to use `routes` to gain access to the list of stops given a certain bus route. Popping a stop off of the queue, if that stop is `target` we immediately return the associated distance. Because we are traversing the graph using BFS, it is guaranteed that the travelled distance whenever a node is first encountered is the shortest distance to that node. Otherwise, we look through the bus routes that also go through the current stop, and enqueue the stops in the bus routes *that have not yet been visited*. If the `while` loop exists, it means that a path does not exist between `source` and `target`, and so we return `-1`.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ is the length of the longest `routes[i]` and $n$ is the length of `routes`. The space complexity is also $O(mn)$.  
  

