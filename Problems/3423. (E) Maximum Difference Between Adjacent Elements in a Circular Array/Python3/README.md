## 3423. (E) Maximum Difference Between Adjacent Elements in a Circular Array

### `solution.py`
Given the circular array `nums`, we are asked to return the largest of the difference between two adjacent pairs of values in `nums`. Given an adjacent pair `nums[i]`, `nums[i+1]`, the difference is calculated as `abs(nums[i] - nums[i+1])`. We can easily compute the differences of each and every adjacent pair by simply walking over `nums` in a linear fashion and handling the 'wraparound' pair manually. Fortunately, Python supports negative indices when indexing into a list - which means we can implicitly handle the wraparound case by computing the difference between `nums[i]` and `nums[i-1]`, where `i` is in the range `[0, len(nums))`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

