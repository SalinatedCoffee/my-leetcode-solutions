## 3349. (E) Adjacent Increasing Subarrays Detection I

### `solution.py`
Given the array of integers `nums` and positive integer `k`, we are asked to determine whether there are two adjacent subarrays of length `k` that are both strictly increasing within `nums`.  
Immediately we can see that this problem can be solved through a sliding window approach. When maintaining a window of length `k`, we can trivially determine whether there is an adjacent subarray preceding the current window by keeping track of a single metric. If the last element of the current window is the `i`th element of `nums`, it can have at most 2 adjacent subarrays of length `k`; one that begins at the `i - k - k`th element and ends at the `i - k`th, and another that begins at the `i + 1`th element and ends at the `i + 1 + k`th. Depending on the direction by which the window is slided, we can trivially see that we would have already examined (and thus have information) on one of these two subarrays. Assuming a typical direction of left-to-right, this subarray would be `nums[i-k-k:i-k+1]`. If this subarray and the current window are both strictly increasing, we know that `nums` satisfies the given condition and we can return `True`.    

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. `nums` is essentially traversed twice; once to update `upper`, and once to update `lower`. Since each update happens at most $n$ times and a single update completes in $O(1)$ time, the overall time complexity is $O(n)$. The space complexity is $O(1)$.  
  

