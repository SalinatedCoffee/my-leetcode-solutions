## 120. (M) Triangle

### `solution.py`
Given a 'triangular' 2D list `triangle`(`len(triangle[0]) == 0`, `len(triangle[1]) == 1`, ... `len(triangle[n-1]) == n`), we are asked to return the minimum sum of the values in a path from `triangle[0][0]` to any value in `triangle[-1]`. From an element `triangle[r][c]`, we are only allowed to move to `triangle[r+1][c]` or `triangle[r+1][c+1]`.  
Our immediate thought should be to try dynamic programming. Setting up the recurrence relation is very straightforward since we can only move to `triangle[r][c]` from `triangle[r-1][c]` and `triangle[r-1][c-1]`. If `f(r, c)` represents the minimum sum of values in the path between `triangle[0][0]` to `triangle[r][c]`, the value for `f(r, c)` would be the minimum of the discussed values plus `triangle[r][c]`. If `r` and `c` are both zero, the return value is simply `triangle[0][0]`. The desired value is the minimum value among `f(n-1, c)`, where `c` is in the range `[0, n)`.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is the 'height' of `triangle`(or simply `len(triangle)`). The intermediate results are computed for each and every element in `triangle`, and since each computation completes in $O(1)$ time, the overall time complexity comes out to be $O(n^2)$. The space complexity is also $O(n^2)$, as all intermediate values are kept in memory.  
  

### `solution_2.py`
We can convert the previous solution into a bottom-up algorithm by flipping the recurrence relation. Instead of `f(r, c)` being the sum of path `triangle[0][0]` to `triangle[r][c]`, we change it so that it represents the sum of a path starting anywhere in `triangle[-1]` and ending at `triangle[r][c]`. The value of `f(r, c)` now depends on `f(r+1, c)` and `f(r+1, c+1)`, with the values of `f(n-1, c)` simply being the elements in `triangle[-1]`. In this recurrence relation, the value of `f(0, 0)` is the one we want.  
Now that we have a bottom-up recurrence relation, we can instantiate a 2D list (or dictionary, as we have done in this case) and tabluate the intermediate results in there. The value of `dp[r][c]` will be the minimum sum of a path between `triangle[-1]` and `triangle[r][c]`. As mentioned above, we initialize the values of `dp[n-1]` with `triangle[-1]`. Starting from the second to last row of `triangle` and moving up towards the first, we compute and store the values in `dp` using the recurrence relation. Once all values have been computed, we simply return the value `dp[0][0]`.  

#### Conclusion
The time and space complexity of this solution are identical to the previous solution, but will be faster in practice since it does not perform any recursive function calls.


### `solution_3.py`
The previous solution can be further optimized in terms of space, by realizing that `f(r, c)` only depends on the values in row `r+1`. `dp` can be 'collapsed' vertically into 2 1D lists `dp1` and `dp2`. `dp1` will contain the intermediate values pertaining to the current row `i`, while `dp2` will contain the values for the `i+1`-th row. The tabulation process is identical to the previous solution, except that we 'swap' `dp1` and `dp2` after tabulating each row.  

#### Conclusion
The time complexity is identical to the previous solution, and the space complexity is $O(n)$.  

