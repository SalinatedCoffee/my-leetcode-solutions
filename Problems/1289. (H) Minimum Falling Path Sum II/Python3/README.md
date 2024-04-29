## 1289. (H) Minimum Falling Path Sum II

### `solution.py`
Assume we already knew the minimum falling path(MFP) sums for some row `i`. If we wanted to compute the MFP sums for the `i-1`th row, this would be trivial to compute as we simply need to select the smallest values in the `i`th row not in the same column(for example, the value of `grid[i-1][j]` would depend on those in `grid[i][:j]` and `grid[i][j+1:]`). Because we can solve smaller subproblems to build up to the desired answer, this problem can be solved with a dynamic programming based solution.  
The function `recurse` takes 2 parameters `r` and `c`, and will return the sum of the MFP starting at `grid[r][c]`. If `r == len(grid) - 1`, we have reached the last row and thus we simply return the value of the current square `grid[r][c]`. Otherwise, we try all cells in the `r+1`th row except for `grid[r+1][c]`, selecting the smallest value. Because we can start at any column in the first row, we compute the MFP sums for all cells in the first row and return the smallest value.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is the length of one 'side' of `grid`(which is square). Each state in the recurrence relation is represented by 2 parameters, both of which are bound by $n$. Computing each state takes $O(1)$ time, putting the overall time complexity at $O(n^2)$. The space complexity is also $O(n^2)$, since the value of all states are memoized in memory.  
  

