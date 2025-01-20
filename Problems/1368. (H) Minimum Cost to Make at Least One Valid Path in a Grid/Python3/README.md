## 1368. (H) Minimum Cost to Make at Least One Valid Path in a Grid

### `solution.py`
On a `m*n` grid, each cell has a sign pointing to the 4 cardinal directions. From a cell, we can move to a neighboring cell only if the sign on the current cell points to it. The direction that each sign points to are as follows:  

- If the value is `1`, it is pointing to the cell to the right.  
- If the value is `2`, it is pointing to the cell on the left.  
- If the value is `3`, it is pointing to the cell below it.  
- If the value is `4`, it is pointing to the cell above it.  

We are allowed to change the sign of a cell to any other sign at most once, but we can also change the sign of any number of cells. Given these conditions and the `m*n` 2D list representation of the grid `grid`, we are asked to determine the fewest number of signs that can be changed to reach the bottom-rightmost cell starting at the upper-leftmost cell.  
While the problem may seem daunting at first glance, we can start by tackling it piece by piece. For starters, we know that if we wanted to move from a cell to a neighbor that its sign is not point to, we *must* change the sign of the current cell. Because we want the minimum number of *sign changes*, we can see that the grid translates into a weighted directed graph rather well, with each cell becoming a vertex connected to their neighbors via edges. If moving from a cell to a neighbor does not require a sign change, the weight of the corresponding edge is `0`. Otherwise, the edge should have a weight of `1`. Once we convert `grid` into a graph as described, we can determine the minimum cost of a path between the source and destination by enlisting the help of a graph traversal algorithm. Since we are working with weighted edges, one's first instinct may be to use Dijkstra's algorithm. While this certainly is a viable approach, it is not that difficult to see that the overhead of the priority queue would be for nought as an edge can only have a weight of either `0` or `1`. Instead, we can use a deque to store future nodes, adding a node to the left or right depending on the weight of the edge being traversed. If we pop nodes from the left of the deque, nodes added to the left of the deque will be popped off first. Thus, if we add a node to the left if the edge has a weight of `0`, we can prioritize the traversal of nodes that require less cost to visit.  
We initialize an `m*n` 2D list `dist` with `float('inf')`, in which we will keep track of the minimum cost required to reach each cell from the source. After initializing the cost of the cell at `(0, 0)` to `0`, we start a BFS traversal at the source node. For each visited cell, we examine its neighbors. If the neighbor is not out of bounds of the grid, and the cost of the current path taken to reach it is less than the previous cost, we visit that neighbor. Before adding it to the deque, we examine the weight of the edge being traversed. If the edge has a weight of `0`, the neighbor is added to the left of the deque. Otherwise, it is added to the right. Once the traversal finishes, we simply return the cost of reaching the destination stored in `dist`.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the dimensions of `grid`. Converting `grid` into a graph, as well as traversing said graph using BFS each require $O(mn)$ time to complete. The space complexity is also $O(mn)$, due to `adj` and `dist`.  
  

