## 867. (E) Transpose Matrix

### `solution.py`
As transposing a matrix flips each element's row and column indices, we need only do the same for all elements in `matrix`. We first allocate a 2D list `ret` with `len(matrix[0])` rows and `len(matrix)` columns, as we cannot perform the transpose in-place. Then for every element `matrix[i][j]` in `matrix`, we store them in `ret[j][i]`. `ret` is then returned after all items have been processed.  

#### Conclusion
This solution has a time complexity of $O(mn)$ where $m$ and $n$ are the dimensions of `matrix`. The space complexity is $O(1)$, excluding `ret`.  
  

