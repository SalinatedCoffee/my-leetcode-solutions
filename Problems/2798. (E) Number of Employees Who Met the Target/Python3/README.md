## 2798. (E) Number of Employees Who Met the Target

### `solution.py`
We simply need to iterate over `hours` while counting the number of elements larger than or equal to `target`. This can be trivially solved by using `functools.reduce()` after preprocessing the first element of `hours`.  

#### Conclusion
The time complexity of this solution is $O(n)$. The space complexity is $O(1)$.  
  

