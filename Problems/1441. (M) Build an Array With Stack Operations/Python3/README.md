## 1441. (M) Build an Array With Stack Operations

### `solution.py`
Implementing this solution in Python is rather trivial, as Python Lists behave more like vectors instead of arrays in other languages. Because `target` only strictly increases, and the values of `target` are bound by `n`, it is guaranteed that an answer exists for any valid inputs for `target` and `n`.  
This problem can easily be simulated. Because we cannot directly discard unwanted values from the data stream, we must perform a push followed by a pop to get rid of a value. As we are operating on a stack, and the integers from the data stream is always given to us in ascending order, we can reconstruct `target` from the data stream by essentially 'skipping' unwanted values and only taking the relevant ones.  
We only need to keep track of 1 value, which is the next value of the data stream. Iterating over `target`, we compare each value to the data stream, discarding values until the data stream's next value matches that of the current element in `target`. We then perform a single push operation, and move on to the next value in `target`, then rinse and repeat.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is `n`. `n` is not directly used in the solution, but the values of `target` is bound by `n`, which determines the potential number of list extensions(more specifically, the number of push-pop pairs to extend by) that should be performed. The space complexity is $O(1)$, excluding the return list `ret`.  
  

