## 2779. (M) Maximum Beauty of an Array After Applying Operation

### `solution.py`
Given the list of integers `nums` and non-negative integer `k`, we can perform an operation on each element of `nums` per the following rules:  

- The value of `nums[i]` can be replaced with any integer in the range `[nums[i] - k, nums[i] + k]`.  
- An operation may be performed on a single element at most once.  

Our task is to determine the length of the longest subsequence containing equal elements after applying any number of operations on the elements of `nums`. Going back to the rules, we know that we can replace a number with *any* number in the appropriate range. This means that some elements `nums[i]` and `nums[j]` can be part of the same subsequence if `2*k >= abs(nums[i] - nums[j])` evaluates to true. Using this property, our task essentially becomes finding the longest subsequence of `nums` such that the difference between the two extreme values is less than or equal to `2*k`. At this point, we realize that we are looking for valid sub*sequences* - because we do not care about whether the elements are adjacent to each other nor their order, we can simply sort `nums` and run a sliding window algorithm on top of it. As long as difference between the first and last items of the window is less than `2*k`, it is a valid window. If the current window is no longer valid after adding an element to the right, we contract the window from the left until it becomes valid again(and vice versa). Once the entirety of `nums` has been examined, we simply return the length of the longest observed window.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$, where $n$ is the length of `nums`. `nums` is sorted prior to the sliding window step, which takes $O(n\log n)$ time to complete using Python's built in sort. The sliding window step takes $O(n)$ time since adding and removing a single element to the window is completed in $O(1)$ time. The space complexity is $O(n)$, due to the sorting step.  
  

