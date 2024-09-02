## 2022. (E) Convert 1D Array Into 2D Array

### `solution.py`
We are asked to 'collapse' the 1D list `original` into a 2D list having `m` rows and `n` columns. If `original` cannot be collapsed to the given dimensions, we are asked to return an empty list. This problem can be trivially solved through a combination of list comprehension and list slices, which can be implemented in a single line with the help of a ternary operator that checks whether `m` and `n` are valid in terms of `original`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `original`. The contents of `original` are copied over into the new 2D list, which requires $O(n)$ time to complete. The space complexity of $O(1)$, excluding the memory required to store the newly generated 2D list.  
  

