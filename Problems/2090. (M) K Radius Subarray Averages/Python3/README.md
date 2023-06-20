## 2090. (M) K Radius Subarray Averages

### `solution.py`
Instead of manually recomputing the subarray sum for each index, we can use prefix sums to avoid performing redundant operations. If we precompute prefix sums `p_sums` for all elements in `nums`, where `p_sums[i]` is the prefix sum excluding `nums[i]` (that is, the sum of subarray `nums[:i]`) we can easily compute the K-radius subarray sum for any valid index. For some index `i` in the range $k < i < n-k$, the K-radius sum for `i` is simply `p_sums[i+k+1] - p_sums[i-k]`. As we established earlier `p_sums[i]` is the prefix sum **excluding** `nums[i]`, and thus `p_sums[i+k+1]` will be the prefix sum that includes the `i+k`th element of `nums`. We now know how to compute the subarray sum for each valid index, and know the length of the subarray as `k` is given to us, which is everything we need to compute an integer average.  
  

#### Conclusion
This solution takes $O(n)$ time to run, where $n$ is the length of `nums`. Precomputing the prefix sums for all values of `nums`, initializing `ret`, and computing the integer averages each take $O(n)$ time. The space complexity is also $O(n)$ due to `p_sums` and `ret`.  


