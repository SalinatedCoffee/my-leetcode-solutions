## 59. (M) Spiral Matrix II

### `solution.py`

This problem is a near carbon copy of [problem #54](../../0054.%20(M)%20Spiral%20Matrix/Python3/README.md). As a matter of fact, it is slightly easier than this problem as we only need to worry about square matrices. If `n` is odd the center-most element will be left uninserted, but this can be trivially solved. Here we simply initialize the return 2D list `ret` with the value `n**2`, so that the center element already contains the correct value if `n` is odd.  

#### Conclusion

This problem has a time complexity of $O(n^2)$, where $n$ is just `n`.  The space complexity is also $O(n^2)$, including the return object.  

  

  
