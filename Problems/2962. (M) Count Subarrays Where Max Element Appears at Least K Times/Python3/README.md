## 2962. (M) Count Subarrays Where Max Element Appears at Least K Times

### `solution.py`
We are asked to count the number of subarrays that contain at least `k` occurrences of the largest element in `nums`. Intuition tells us that we can take a sliding window based approach to solve this problem, since the problem involves counting subarrays that satisfy some condition based on their contents.  
First, we identify the largest element in `nums`. We can then start iterating over `nums`, incrementally expanding the window and contracting the window when there are *more than* `k` occurrences of the maximum value of `nums` within the window. The reason for this is that because we are interested in the **largest** value in `nums`, any subarrays that have more than `k` max values will be included in the count if we keep the window to strictly include exactly `k` occurrences. For example, assume we have the array `nums = [1, 1, 3, 1, 3, 3]` and `k = 2`, and the window is currently `[4, 5]` (0-indexed). The subarrays that extend to the left of the current window would be `[1,1,3,1,3,3]`, `[1,3,1,3,3]`, `[3,1,3,3]`, `[1,3,3]`, and `[3,3]`. Note that the set of subarrays include the case where the window contains more than `k` max values. We also need to make sure that the window is as 'tight' as possible, as in the first and last elements of the window should be the max elements of `nums`. Given the starting position of the window `l` (0-indexed), the number of valid subarrays that extend to the left of the window is simply `l + 1`.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. `nums` is at most iterated over twice, with each element taking constant time to process. The space complexity is $O(1)$, as we only use a handful of fixed size variables.  
  

