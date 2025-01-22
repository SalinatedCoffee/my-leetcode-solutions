## 2661. (M) First Completely Painted Row or Column

### `solution.py`
We are given a list of integers `arr`, and a `m*n` 2D list of integers `mat`. Both lists contain all integers in the range `[1, m*n]`. Starting with the first item of `arr`, the cell of `mat` that contains the same value as that item is 'painted'. As we continue to paint cells, we are asked to return the index of the first element of `i` that when painted fully paints either a row or column of `mat`.  
The problem can be easily solved by using a few dictionaries. When given a number, we want to quickly access the corresponding cell in `mat`. This can be achieved by using a dictionary, storing the cell value as the key and the cell's coordinates in `mat` as the value. We also need to determine whether painting a cell will result in a fully painted row or column, which can be done simply by keeping track of the number of painted cells in each row and column.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the dimensions of `mat`. Although `arr` will never be fully iterated over given the problem constraints, the time it will take to iterate over `arr` until a solution is found still scales with the length of `arr`, which is $mn$. Preprocessing `mat` to map cell values to their coordinates also requires $O(mn)$ time, putting the overall time complexity of the solution at $O(mn)$. The space complexity is $O(mn+m+n)$, due to the dictionaries `v2c`($O(mn)$), `row`($O(m)$), and `col`($O(n)$).  
  

