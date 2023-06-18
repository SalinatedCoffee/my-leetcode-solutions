## 2328. (H) Number of Increasing Paths in a Grid

### `solution.py`
At some cell with coordinates `(i, j)`, the number of valid paths to reach that cell will be the sum of the number of paths to get to its valid neighbors plus 1(since we count a single cell as a valid path). However, as there is no clear dependence relation between the cells that we can easily utilize, there may be instances where a path count needs to be updated because it was computed with outdated information. Looking at a simple example, say `grid = [[1, 1], [2, 3]]`. If we initially reach `grid[1][1]` through `grid[1][0]`, the number of paths for `grid[1][1]` would be `2` since `grid[1][0]` has `1` path, and `grid[1][1]` also has `1` path. But now say we reach `grid[1][0]` through `grid[0][0]`. The path count for `grid[1][0]` is now `2`, by the same logic we used for `grid[1][1]` previously. If we perform the computation for `grid[1][1]` now, the number of paths would be `3` instead of `2`. This problem arises because we traversed `grid[1][0]` first, which has a larger value than `grid[0][0]`. If we had traversed `grid[0][0]` first, we would have gotten to a count of `3` in one traversal instead of two. Hence, we can **sort** the cells based on their values in ascending order, and compute the number of paths starting with the cell with the smallest value. At a cell we update the path count for its valid neighbors and do the same for the next cell in the sorted list.  
Once we have finished iterating over the sorted list of cells, we can take the sum of the path counts for all cells and simply return that number.  

#### Conclusion
This solution has a time complexity of $O(mn\log(mn))$, where $m$ and $n$ are the dimensions of `grid`. There are $mn$ cells total, and sorting them takes $O(mn\log(mn))$ time. The computation step performs a fixed number of operations for each cell, and thus will take $O(mn)$ time. The space complexity is $O(mn)$.  
  
  

### `solution_2.py`
There is of course, a way to solve this problem without having to resort to sorting. As mentioned in the previous solution, the number of valid paths ending at some cell depends on the values of its neighboring cells. That is, if a neighboring cell exists and has a smaller value than the target cell, we can add that to the total number of paths to the target cell. Now that we have a clear idea of what the state transitions will look like, we can start implementing a top-down dynamic programming solution. We will memoize the intermediate results in a 2D list `dp`, where `dp[i][j]` will store the number of paths ending in `grid[i][j]`. `recurse(i, j)` will return the number of valid paths that end in `grid[i][j]`. If the number for that cell has already been computed (`dp[i][j] != 0`) we can simply return that value. If not, it recurses on its valid neighbors. As with the previous solution we want the number of valid paths to **all** cells, and thus need to take the sum of all initial calls to `recurse()`.  

#### Conclusion
The time complexity of this solution is $O(mn)$, since all values of `dp` (which is an $m\times n$ 2D list) are computed once. The space complexity is also $O(mn)$, as `dp` uses $O(mn)$ space, and the size of the recursion stack is also $O(mn)$.  
  
