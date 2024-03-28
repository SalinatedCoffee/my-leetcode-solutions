## 41. (H) First Missing Positive

### `solution.py`
The trivial solution is to simply store all positive values into a set, and incrementally check every positive integer against that set. However, we are asked to implement a solution that does not use extra memory. Due to this restriction, approaches that involve sorting `nums` also become infeasible.  
One method that we can use is to modify the given input. While this should be avoided whenever possible in practice, it should be okay in an interview / evaluation setting as long as it is clearly communicated that such an approach is allowed.  
We are only interested in the positive values in `nums`, which means that we do not care about negative values or `0`. Any values that are larger than `len(nums)` can also be disregarded, since the largest value that can be missing is `len(nums) + 1`. Iterating over `nums` then, we set each value to `1` if it is either negative, `0`, or larger than `len(nums)`. Because we have 'sanitized' `nums` using `1` as the sanitized value, we also need to explicitly check if `1` already exists in `nums`. If `nums` before the sanitization did not contain `1`, we can immediately return `1`, as it is the smallest possible integer that can be missing. Then, we iterate over the modified `nums` once more, flipping the sign of `nums[nums[i]-1]` if it is not already negative. Finally, we iterate over `nums` one last time, returning the current index whenever `nums[nums[i]-1]` is not negative.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. `nums` is iterated over thrice, with each value taking constant time to process. The space complexity is $O(1)$ if excluding the reuse of `nums`(use of *auxillary* space), or $O(n)$.  
  
  