## 2684. (M) Maximum Number of Moves in a Grid

### `solution.py`
Given the 2D list of positive integers `grid`, we are asked to return the max number of moves possible starting at any cell in the first column. At some cell `grid[i][j]`, we can move to `grid[i-1][j+1]`, `grid[i][j+1]`, or `grid[i+1][j+1]` if the value of the current cell `grid[i][j]` is strictly less than that of the cell that we have moved to.  
Intuition tells us that we could take a dynamic programming based approach, as we could easily compute the maximum number of moves for the cell `grid[i][j]` using the values for `grid[i-1][j+1]`, `grid[i][j+1]`, and `grid[i+1][j+1]`. This is one of the rare problems where the bottom up approach is easier to implement; if we have a 2D list `dp` where the value of `dp[i][j]` is the maximum number of moves starting at `grid[i][j]`, we can compute the value of `dp[i][j]` using previously computed values. If a move is possible(the value of `grid[i][j]` is strictly less than the cells we are moving to) the resulting number of moves by moving to that cell is simply the corresponding `dp` value of the next cell + `1`. All possible choices are considered, among which the largest value is selected. Once `dp` has been fully populated, we iterate over the first column and return the largest value.  

#### Conclusion
This solution has a time complexity of $O(mn)$ where $m$ and $n$ are the dimensions of `grid`. The dimensions of `dp` are identical to those of `grid`, and evaluating the value for a single cell requires $O(1)$ time to complete as there are a limited number of possible moves at a given cell. Thus, the overall time complexity of this solution is $O(mn)$. The space complexity is also $O(mn)$, as `dp` is kept in memory until the algorithm completes.  
  

