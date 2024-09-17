## 2419. (M) Longest Subarray With Maximum Bitwise AND

### `solution.py`
Given the list of integers `nums`, we are asked to find the length of the longest subarray where the bitwise AND of all of its contents is equal to the largest bitwise AND among all possible subarrays of `nums`. That is, if the largest bitwise AND of the subarrays of `nums` is `k`, we want to find the largest value of `i - j` where the bitwise AND of all values in `nums[i:j+1]` equals `k` and `i <= j`. At first glance the problem seems much more complicated than it actually is, until we realize that it is impossible for a value resulting from bitwise ANDing two integers to be strictly greater than either values. In other words, for any positive integers `a` and `b` the value of `a & b` can never be larger than either `a` or `b`. If we generalize this to a subarray of integers we can say that the bitwise AND of the contents of that subarray is always less than or equal to the largest value of the subarray. On the other hand subarrays of length 1 are allowed, which means that the largest bitwise AND value of the subarrays of `nums` is actually just the largest value in `nums`. For the bitwise AND of a subarray to equal that of a certain value, *all* of its elements must also be equal to that value. This means that if the largest subarray bitwise AND value is `k`, we need to find the length of the longest subarray of `nums` that only contains `k`. Both steps are easy to implement, and will not be described here.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `nums`. Finding the largest integer in `nums`, as well as finding the longest subarray each takes $O(n)$ time to complete. The space complexity is $O(1)$.  
  

