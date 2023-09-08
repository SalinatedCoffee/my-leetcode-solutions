## 118. (E) Pascal's Triangle

### `solution.py`
To compute some non-trivial value, we need access to 2 values in the previous row. If we left-justify the rows to make the reasoning easier, we could say that the value of `tri[i][j]`, where `i` is the row number and `j` is the `j`-th value in that row (both 0-indexed), is simply `tri[i-1][j-1] + tri[i-1][j]`. The obvious order of computation is to start from the top row and work our way down - as the solution requires to return the entire triangle, by the time we start generating row `i` we would already have the values in row `i-1`.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is `numRows`. A pascal triangle with $n$ rows means that the $n$th row has $n$ elements, hence the overall time complexity of $O(n^2)$. The space complexity is $O(1)$, excluding the memory required to store `ret`(which uses $O(n^2)$ space).  
