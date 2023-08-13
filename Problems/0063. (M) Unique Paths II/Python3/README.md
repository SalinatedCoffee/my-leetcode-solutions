## 63. (M) Unique Paths II

### `solution.py`
For problems like this where we are asked to count the number of unique paths between two points, a bottom-up dynamic programming approach is usually easier to come up with compared to a top-down one. This problem is one of the easier ones as the robot can only move in two directions every turn. Say the robot is at some square `obstacleGrid[i][j]`. Previously the robot could have come from the square above it or the one to its left, which are squares `obstacleGrid[i-1][j]` and `obstacleGrid[i][j-1]`, respectively. If we know the number of paths from `obstacleGrid[0][0]` to these two previous locations, the number of unique paths to `obstacleGrid[i][j]` would simply be the sum of these two values. That is, if the number of paths are stored in a 2D list `dp` where `dp[i][j]` is the number of unique paths between squares `(0,0)` and `(i,j)`, the value of `dp[i][j]` can be computed with the expression `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. Of course the robot can only traverse squares that do not have an obstacle on them, so we only update `dp[i][j]` if `obstacleGrid[i][j] != 1`.  
When we initialize `dp`, the first row and column (`dp[i][0]` and `dp[0][j]`) should be initialized to `1`, since the number of paths between `(0,0)` and these squares are trivially `1`. However we need to remember to skip initializing all squares after an obstacle has been found, since these squares cannot possibly be reached by the robot.  
This solution already handles the case where an obstacle is on the starting square, but will still tabulate `dp` with `0`s. We can reduce the best case time complexity from $O(mn)$ to $O(1)$ by adding a simple sanity check before we start doing anything.  
The desired value will be stored in `dp[-1][-1]`, which we can immediately return.  

#### Conclusion
The time complexity is $O(mn)$, where $m$ and $n$ are the dimensions of `obstacleGrid`. There are `mn` states in our recurrence relation, which we perform a fixed number of operations for each state. The space complexity is also $O(mn)$, but could be optimized to $O(\text{min}(m,n))$ since the recurrence relation only relies on the row or column that immediately precedes a state.  
  

