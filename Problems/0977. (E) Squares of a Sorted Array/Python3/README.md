## 977. (E) Squares of a Sorted Array

### `solution.py`
We simply need to square each elements in `nums`, and then sort the resulting list before returning it(note that the sorting can also be performed before the squaring).  

#### Conclusion
The time complexity of this solution is $O(n\log n)$, where $n$ is the length of `nums`. Python's built in 'sorted' function takes $O(n\log n)$ time to sort an array of length $n$, hence the time complexity. The space complexity is $O(n)$, also due to the sorting step.  
  

