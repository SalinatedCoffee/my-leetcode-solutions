## 2050. (H) Parallel Courses III

### `solution.py`
All courses must be completed, and as such the time it takes to satisfy the prerequisites of some course `i` will be the *maximum* value of the paths ending with `i`. Generalizing, we can now see that we simply want to find the path with the largest sum of node labels. This can be achieved through a combination of recursive DFS and top-down dynamic programming. We define a recursive function `recurse(i)`, where the return value is the sum of the maximum path starting at node `i`. At some node `i` we recurse on its neighbors, retrieving their maximum costs. Among those costs we choose the largest, and return the sum of that cost with the cost of the current node. Note that we do not have to concern ourselves with cycle checking, as the problem guarantees that the given course graph is a DAG, and all courses can be completed.  
Now that we can determine the maximum costing path starting at a single node, we can simply run this algorithm starting at every node in the graph and return the largest value.  

#### Conclusion
The time complexity of this solution is $O(n+e)$, where $n$ is `n` and $e$ is the length of `relations`. We iterate along the entirety of `relations` in order to convert it into an adjacency list, after which we traverse the graph using DFS, which takes $O(n)$ time. The space complexity is also $O(n+e)$. `recurse()` has $n$ states memoized in memory, and the adjacency list `graph` will use $O(e)$ memory since it will contain every edge within `relations`.  
  

