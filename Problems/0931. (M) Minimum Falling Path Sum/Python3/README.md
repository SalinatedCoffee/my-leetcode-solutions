## 931. (M) Minimum Falling Path Sum

### `solution.py`
This problem is yet another garden variety dynamic programming problem. Defining the recurrence relation, if we have a function $f(i, j)$ that returns the minimum path sum starting at `matrix[i][j]`, we can compute the value of $f(i, j)$ by choosing the smallest value among $f(i+1, j-1)$, $f(i+1, j)$, and $f(i+1, j+1)$ and adding that to `matrix[i][j]`. The base cases are of course, when `i == n - 1` and when `j < 0` or `j >= n`. The former indicates that we have reached the last row, and as such the cost of reaching the destination is simply the value of the square itself(`matrix[i][j]`). For the latter, we are out of bounds of `matrix` which means that the current path is invalid. Thus, we return an arbitrairly large number.  

#### Conclusion
The time and space complexity of this solution is $O(n^2)$, where $n$ is the size of `matrix`. There are $n^2$ states in our recurrence relation, and it takes $O(1)$ time to compute each state. The value of each state is kept in memory, hence the quadratic space complexity.  
  


### `solution_2.py`
The previous solution can be easily rewritten as a bottom-up algorithm, where we store the state values in a 2D list (`dp`) instead of using `functools.cache` to memoize the return value of each function call. The last row of `dp` is initialized with the values of the last row of `matrix`, since the path sum of reaching the end of a path from the last row is simply the value of the square itself. We then iterate in reverse starting from the second-last row, where the value of `dp[i][j]` is `matrix[i][j] + min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])`. Once the entirety of `dp` has been populated, the value we want is the smallest value in the first row of `dp`.  

#### Conclusion
The time and space complexity of this solution is identical to the previous solution.  
  

