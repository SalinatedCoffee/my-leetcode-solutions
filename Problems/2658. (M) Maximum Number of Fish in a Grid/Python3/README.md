## 2658. (M) Maximum Number of Fish in a Grid

### `solution.py`
`grid` is a 2D list of non-negative integers, where each cell can be either land or water containing fish. If `grid[i][j]` is `0`, it is a land cell. Otherwise, it is a water cell containing `grid[i][j]` number of fish. A fisherman can start at any water cell on `grid`, and can catch all of the fish in the cell. The fisherman can then move to any *adjacent water cell*, catching all of the fish in that cell as well. Our task is to determine the maximum number of fish that the fisherman can catch.  
Immediately, we can see that a fisherman can only catch all of the fish in a single body of water in `grid`. If we can group all cells into separate bodies of water, we can compute the number of fish for each body of water and return the largest value. There are many ways that this can be achieved, but here we will opt to implement a union-find based approach to solve this problem. The premise is simple; we first iterate over `grid` to group each water cell, and the make a second pass to compute the total number of fish in each body of water. Once the computation is complete, we simply return the largest value.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the dimensions of `grid`. `grid` is iterated over exactly twice, and during both passes, each cell interacts with the DSU data structure(calls `ufind`) at most twice. A single find operation on a DSU containing $k$ elements requires $O(\alpha(k))$ time to complete, where $\alpha$ is the inverse Ackermann function. Since the inverse Ackermann function can be considered as $O(1)$, the overall time complexity of this solution will be $O(mn\cdot\alpha(mn)) = O(mn)$. The space complexity is also $O(mn)$, due to the DSU(p) and `sums`.  
  

