## 1727. (M) Largest Submatrix With Rearrangements

### `solution.py`
A brute force solution that actually reorders the columns to search for the largest submatrix is obviously not feasible. Instead we need to devise a method that does so without modifying `matrix`. First off, we know that we need at least 2 pieces of information about the `1`s in the matrix. We need to know the length of a run of column-wise consecutive `1`s, as well as the position of that run within its column. Let's say we preprocess `matrix` into a 2D list of tuples that contain the length of a run of `1`s and the position of that run within its column.   

#### Conclusion
we store entire processed 2d list in memory but obviously can be optimized to only store 1 row  
  

### `solution_2.py`
without sorting  

#### Conclusion
\<Content\>  
  

