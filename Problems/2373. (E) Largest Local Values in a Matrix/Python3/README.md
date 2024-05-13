## 2373. (E) Largest Local Values in a Matrix

### `solution.py`
The simplest solution by far would be to simply scan each and every 3x3 grid in `grid`, storing the maximum value in the appropriate location in the 2D list to be returned. If `n == len(grid)`, the resulting list should have a side length of `n - 2`. Thinking about each 3x3 matrix as the coordinates of their center cell, we can see that the maximum value of a matrix centered at `grid[i][j]` should be stored in `ret[i-1][j-1]`, where `ret` is the 2D list that we are returning.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is the side length of `grid`. There are $O(n^2)$ 3x3 matricies in `grid`, with each one taking $O(1)$ time to scan through. The space complexity is $O(1)$.  
Perhaps a slightly more efficient solution can be implemented by reducing the number of redundant scans that are performed on `grid`. The return list could be used to store intermediate maximums for each 3x3 matrix, allowing us to perform incremental scans instead of scanning a matrix in its entirety.  

