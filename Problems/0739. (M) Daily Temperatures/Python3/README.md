## 739. (M) Daily Temperatures

### `solution.py`
The time complexity of the brute force solution is quadratic, and involves scanning `temperatures` for every element in `temperatures`. Sorting `temperatures` does not help since the values are not unique. Rephrasing the problem, we are essentially being asked to find the index of the first temperature higher than the `i`-th temperature towards the right of `i`, for all `i`. This should now be easily recognizable as a monotonic stack problem for those with prior experience with the data structure. As we want to find the first **larger** item towards the **right**, we want to iterate over `temperatures` in *reverse* while maintaining a monotonically *decreasing* stack.  
We first initialize a list of length `len(temperatures)` `ret` with `0`s. The empty stack `stack` is also initialized. `temperatures` is then iterated in reverse, where for each temperature items are popped off of the stack until the value on the top is higher than the current temperature. If the stack is not empty after this step, then the top of the stack is the first value higher than the current temperature, and we update `ret` with the appropriate value. We then push the current temperature on the stack, and move on to the next value in `temperatures`.  

#### Conclusion
The time and space complexity of this solution is $O(n)$. `temperatures` is iterated over once, and each value in `temperatures` takes $O(1)$ time to process. `stacks` is kept in memory and can at most contain $n$ items(when `temperatures` strictly increases), hence the linear space complexity.  
  

