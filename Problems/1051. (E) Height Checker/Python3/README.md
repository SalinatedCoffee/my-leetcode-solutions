## 1051. (E) Height Checker

### `solution.py`
As `heights` can at most contain 100 elements, we can simply sort `heights` to get the array `expected`. Both arrays are then iterated over simultaneously, incrementing a counter whenever the two values do not match.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `heights`. `heights` is sorted to create `expected`, which takes $O(n\log n)$ time to complete using Python's built in sort. The space complexity is $O(n)$, also due to the sorting step.  
  

