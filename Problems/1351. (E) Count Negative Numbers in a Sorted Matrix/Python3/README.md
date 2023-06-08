## 1351. (E) Count Negative Numbers in a Sorted Matrix

### `solution.py`
Since all rows and columns are sorted in descending order, we can avoid having to scan all elements in `grid`. If some value `grid[i][j]` is negative, that guarantees that all elements to the 'right' are also negative (`grid[i][j:]`) as well as all elements 'below' it(`grid[k][j] for k in range(i, m)]`). Consequently, elements in the entire lower-right partial matrix bound by these rows and columns will also be negative. Hence, we can keep track of the position of the leftmost negative number in a row and start scanning towards the left from that position in the next row. For example if `grid = [[2, -1, -2], [-1, -2, -3]]`, the leftmost negative number `-1` is in row `0` and column `1`. As mentioned previously, this guarantees that `grid[i][j]` is also negative for values $0 \leq i \leq m$ and $1 \leq j \leq n$ where $m = 1$ and $n = 2$(0-indexed $2 \times 3$ 2D array). Thus in the next row we may start scanning from index `0` (column `0`) towards the left.  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ and $n$ are the dimensions of the matrix. Since we start iterating along a row from where the previous row left off, the inner for loop will only iterate $n$ times. The space complexity is $O(1)$.  
  

