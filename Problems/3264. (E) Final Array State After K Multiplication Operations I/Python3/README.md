## 3264. (E) Final Array State After K Multiplication Operations I

### `solution.py`
`k` operations are to be performed on the list of integers `nums`, with each step involving taking the smallest value(taking the value with the smaller index if there are multiple) and multiplying it by `multiplier`. Our task is to return `nums` after all `k` operations have been performed.  
This problem can be trivially solved by using a min heap. We extend each value of `nums` with its index and populate a min heap with the resulting tuples. For each operation, we pop off an item off of the heap, multiply the value, and push the new tuple back onto the heap. After repeating this step `k` times, we reconstruct `nums` using the index attached to each value.  

#### Conclusion
The time complexity of this solution is $O(n\log n + k\log n)$, where $n$ is the length of `nums` and $k$ is `k`. Initializing the heap of values and reconstructing `nums` after `k` operations are $O(n\log n)$ time operations. For each operation, we remove from and add an item to the heap. Since the heap contains $n$ elements, each removal/addition takes $O(\log n)$ time to complete, which means that it will require $O(k\log n)$ time to perform all `k` operations. The space complexity is $O(n)$, due to the min heap `nums`.  
  

