## 1337. (E) The K Weakest Rows in a Matrix

### `solution.py`
This problem can trivially be solved by taking the sum of each row and pushing them into a min-heap with their corresponding row indices. We can then pop `k` elements out of the heap which will give us the first `k` rows with the smallest number of soldiers.  
Because the soldiers are 'left justified', we can also use binary search to optimize the counting step down to logarithmic time instead of linear. However, the problem constraints are small enough to the point where such an optimization would yield minimal improvements. As a matter of fact Python's `sum()` is (most likely) implemented in C, where as a homebrew implementation of binary search or the built-in `bisect` module will be written in Python. Given the constraint that each row can at most have a length of 100, the former approach would most likely outperform the latter in most cases.  

#### Conclusion
This solution has a time complexity of $O(mn + m\log m)$, where $m$ and $n$ are the dimensions of `mat`. We take the summation of each row and push them into a min-heap. There are $m$ rows with $n$ elements, so the summation step will take $O(mn)$ time and pushing these sums into the heap will take $O(m\log m)$ time. The space complexity is $O(m)$, as the heap will at most contain $m$ items.  
  

