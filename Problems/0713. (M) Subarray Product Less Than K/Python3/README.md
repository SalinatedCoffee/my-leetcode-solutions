## 713. (M) Subarray Product Less Than K

### `solution.py`
The problem is almost immediately recognizable as a sliding window problem. We incrementally expand the window as we iterate over `nums`, and contract the window if the product of the elements within it is strictly larger than `k`. If we know a window is valid, we can trivially calculate the number of valid subarrays that end with the last element in that window. The reason that we count the subarrays in this manner is to avoid overcounting. If we count **all** subarrays within a given window, and it turns out that adding the next element would not invalidate it, we would recount all subarrays that were counted before the expansion.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. `nums` is essentially iterated over twice, with each element taking $O(1)$ time to process. The space complexity is $O(1)$ since we only use a handful of variables with fixed size.  
  

