## 64. (M) Minimum Path Sum

### `solution.py`
Intuition tells us that we can solve this by using bottom-up dynamic programming. We can only move in two directions, which means that at a certain square there are only two previous squares we could have come from - the one above or the one on the left. Then, it becomes obvious that we want to choose the square that has the smaller sum among the two.  
So we initialize a 2D list `dp` with the same dimensions as `grid`. The value of `dp[i][j]` will be the sum of the smallest path taken from `grid[0][0]` to `grid[i][j]`. The first column and row are initizlized with the cumulative sums of the first column and row of `grid`, respectively. We then fill in the values of `dp` moving towards the bottom-right(for this solution, row-first). The desired value will be stored in `dp[-1][-1]`.  

#### Conclusion
This solution has a time and space complexity of $O(mn)$ where $m$ and $n$ are the dimensions of `grid`, since the instantiation and tabulation of `dp` takes $O(mn)$ time and space.  
  

