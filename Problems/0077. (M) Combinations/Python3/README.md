## 77. (M) Combinations

### `solution.py`
This problem can be solved with a backtracking algorithm, where the recursive function 'backs out' of the current recursion branch when an answer cannot possibly exist after the current step. Here there are two backtracking conditions; when the current list of items has `k` elements, and when the next item to be inserted is larger than `n`.  
The solution shown here could be further optimized by exiting early when it is impossible to achieve a list of length `k` based on the value to be inserted next.  

#### Conclusion
This solution has a time complexity of $O(2^n)$, where $n$ is `n`. The recursive algorithm tries selecting `k` values in the range $[1, n]$, and `k` can at most be equel to `n` - hence the running time of $O(2^n)$. The space complexity is $O(k)$ (excluding the return value `self.ret`) since the recursion tree will have at most a depth of `k`.  
  

