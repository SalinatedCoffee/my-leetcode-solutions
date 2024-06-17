## 945. (M) Minimum Increment to Make Array Unique

### `solution.py`
Given a list of integers `nums`, we are asked to determine the minimum number of operations required to make the values in `nums` unique. A single operation involves **incrementing** a value by `1`. Because we cannot decrease the value of an element, we can sort `nums` in ascending order and greedily increase the values to make them unique. If `nums` is in ascending order and we know that the values in `nums[:i]` are unique, there are 3 cases for `nums[i]`. It can be less than, equal to, or larger than `nums[i-1]`. When `nums[i]` is less than `nums[i-1]`, we know that the `i-1`st element has been incremented since `nums` has been sorted in ascending order. We also know that the minimum value has been added to the `i-1`st value to make it unique, which means that `nums[i]` already exists in the subarray `nums[:i]`. Since we also want to perform the minimum number of increments to make `nums[i]` unique, we increment `nums[i]` to `nums[i-1] + 1`. If `nums[i-1] == nums[i]`, we simply increment `nums[i]` by `1` to make it unique. For the last case where `nums[i]` is larger than `nums[i-1]`, we simply do nothing as `nums[i]` is already unique.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$ where $n$ is the length of `nums`. Sorting `nums` takes $O(n\log n)$ using Python's built in sort. `nums` is then iterated over exactly once, with each element taking $O(1)$ time to process. The space complexity is $O(n)$, due to the sorting step.  
  

