## 74. (M) Search a 2D Matrix

### `solution.py`
The problem wants us to implement a solution that runs in $O(\log(mn))$ time, which means that we cannot flatten `matrix` into a 1D list. `matrix` is however, already sorted in such a way that the values monotonically increase going left to right, top to bottom. Because of this we can easily map a 1D index to its corresponding index pair for `matrix`. For instance, if `matrix` has the dimensions $3\times 4$ and we want to the `6`th smallest element (0-indexed), the element will be in the `6 // 4 = 1`st row and the `6 % 4 == 2`nd column. Using this we can apply binary search on `matrix`, where the initial search space is the range `[0, m*n-1]` where `m == len(matrix)` and `n == len(matrix[0])`.  

#### Conclusion
This solution has a time complexity of $O(\log(mn))$, where $m$ and $n$ are the dimensions of `matrix`. The space complexity is $O(1)$.  
  

