## 304. (M) Range Sum Query 2D - Immutable

### `solution.py`
`matrix` is a 2D list representing a matrix of integers. Given `matrix`, we are asked to design and implement the class `NumMatrix` that takes `matrix` upon instantiation and offers the method `sumRegion` that returns the sum of any rectangular region within `matrix` in $O(1)$ time. `sumRegion` should accept 4 integers - `row1`, `col1`, `row2`, and `col2`. The region of which the sum should be returned is the rectangle where its upper-leftmost square is `matrix[row1][col1]` and lower-rightmost square is `matrix[row2][col2]`.  
Since we want to compute the sum of values across a rectangular region of `matrix`, we can precompute the 'rectangular prefix sum' of `matrix` upon initialization, which will allow us to compute the sum of values for *any* rectangular region in `matrix` in constant time. The idea is simple; if we want the sum across the area bound by upper-left square `(i, j)` and lower-right square `(k, l)`, we can simply take the area sum of the square `(0, 0)`, `(k, l)`, subtract from it the sum of `(0, 0)`, `(i-1, l)` and `(0, 0)`, `(k, j-1)`, and add back the over-subtracted area sum of `(0, 0)`, `(i-1, j-1)`.  

#### Conclusion
Instantiation of a `NumMatrix` object takes $O(mn)$ time to complete, where $m$ and $n$ are the dimensions of `matrix`. The 'rectangle prefix sum' is computed for each and every cell in `matrix`; and with each value taking constant time to compute, the initialization step requires $O(mn)$ time to complete. Calls to `NumMatrix.sumRegion` each finishes in $O(1)$ time as required, since the retrieval of the sums of the 4 areas and the final computation all take $O(1)$ time to finish.  
A `NumMatrix` object will use $O(mn)$ memory during its lifetime.  

