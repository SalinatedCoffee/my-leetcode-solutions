## 2290. (H) Minimum Obstacle Removal to Reach Corner

### `solution.py`
A grid contains cells that are either empty of occupied by an obstacle. Each cell in the 2D list representation of the grid `grid` contains a `0` if the cell is empty, or a `1` of it contains an obstacle. Starting at the upper-leftmost cell of the grid, we can travel to the(at most) 4 neighboring empty cells in the cardinal directions of the current cell. Given the 2D list `grid`, our task is to determine the minimum number of obstacles that must be removed from the grid so that the bottom-rightmost cell can be reached.  
Because we are given a grid to traverse, and we want to optimize the number of removed obstacles before reaching the destination, intuition tells us that we would want to utilize an algorithm that finds the shortest path on a graph. BFS would be the obvious first choice as the edge weights are binary(0 to move between empty cells, 1 to travel to an occupied one). The problem with this approach is that it traverses the grid indiscriminately, traveling to a cell regardless of whether it is occupied or not. While moving across the grid, we would want to somehow prioritize exploring empty cells before resorting to occupied cells since we want to minimize the number of obstacles that must be removed. To achieve this, let's first think about the case where we already know the minimum number of obstacles that have to be removed to reach some cell `grid[i][j]` from `grid[0][0]`. Since we know the *minimum* number of removed obstacles, there is no point in revisiting `grid[i][j]`. We can also say that any neighboring cells that are empty will have the same number of removed obstacles as `grid[i][j]`, for obvious reasons. Essentially, among the neighbors of `grid[i][j]`, we want to travel to the empty cells first before considering those that contain an obstacle. The iterative implementation of BFS already uses a queue to store nodes to be traversed in the future - if we use a deque, we can segregate untraveled empty cells from the occupied cells by enqueueing empty cells from one side and occupied cells from the other. If we were to traverse nodes by popping items from the same side as the empty cells are enqueued, we can guarantee that unvisited empty cells will be visited first before traversing occupied ones.  
We prepare for the BFS traversal by initializing the required variables and data structures. The number of rows and columns of `grid`, constant list of unit vectors `vec`, 2D list containing the minimum number of removed obstacles `costs`, and deque of future nodes `nodes`. All values in `costs` are initialized to infinity except for the starting cell `costs[0][0]`, which is initialized to `0` instead. While `nodes` is not empty, we pop a node from the left. We then examine the neighboring cells, ignoring those that are either invalid or already visited. If the cell is empty, we update the corresponding value in `costs` to the current number of removals before enqueueing it on the left side of `nodes`. Otherwise, we update the value in `costs` to the number of removals + `1`, and enqueue the cell on the right side of `nodes`. Once the traversal exits, the value of `costs[-1][-1]` will contain the desired value.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the dimensions of `grid`. Running BFS on a graph with $V$ vertices and $E$ edges requires $O(VE)$ time to complete. Since there are $mn$ vertices and $4mn$ edges, the time required to run BFS on the grid will be $O(mn+4mn) = O(mn)$. The space complexity is also $O(mn)$, due to `nodes` and `costs`.  
  
