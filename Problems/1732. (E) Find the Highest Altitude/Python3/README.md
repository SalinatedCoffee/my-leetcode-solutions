## 1732. (E) Find the Highest Altitude

### `solution.py`
The altitude at a certain stop `i` is simply the sum of all deltas up to stop `i`. Thus we can simply iterate through `gain` while computing the prefix sum up to the current index, and return the largest value.  
  
#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `gain`. Prefix sums are computed for all stops in `gain`, hence the running time of $O(n)$. The space complexity is $O(1)$.  
