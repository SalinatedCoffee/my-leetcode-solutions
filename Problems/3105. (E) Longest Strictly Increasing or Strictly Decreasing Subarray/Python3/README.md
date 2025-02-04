## 3105. (E) Longest Strictly Increasing or Strictly Decreasing Subarray

### `solution.py`
Given the list of positive integers `nums`, we are asked to return the length of the longest strictly increasing or decreasing subarray. As `nums` is tiny, we can take a brute force approach that iterates over all adjacent element pairs of `nums`. We keep track of the monotonic subarray lengths using 2 separate variables. `a` represents the length of the ascending subarray ending with the current element, and `d` represents the length of the descending subarray. Depending on the size comparison between the element pair, the appropriate length is incremented and reset to `1`. Once all pairs have been examined, we simply return the longest observed length.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

