## 2270. (M) Number of Ways to Split Array

### `solution.py`
The list of integers `nums` can be split into 2 parts between indices `i` and `i+1` only if:  

- The sum of `nums[:i+1]` is greater than or equal to that of `nums[i+1:]`.
- `nums[i+1:]` is not empty(`i+1 < len(nums)-1` is true).  

Given these conditions, we are asked to determine the number of ways that `nums` can be split.  
Since we are splitting `nums` into 2, we know that we can efficiently compute the sum of the latter part if we know the sum of the prefix that ends with `i`. If the value of `pre[i]` is the sum of the prefix `nums[:i]`, the sum of `nums[i+1:]` is simply `pre[-1] - pre[i]`. After precomputing the prefix sums, we iterate over each element in `nums`. Whenever `pre[i]` is greater than or equal to `pre[-1] - pre[i]`, we increment a counter by `1`. Once all elements have been examined, we simply return the counter directly.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. `nums` is iterated over twice; once to compute the prefix sums, and once to count the number of valid splits. Since computing a single prefix sum and determining whether `nums` can be split at a single position each finishes in $O(1)$ time, the overall time complexity of this solution is $O(n + n) = O(n)$. The space complexity is also $O(n)$, due to the list of prefix sums `pre`.  
  

### `solution_2.py`
Looking back at the previous solution, we realize that the evaluation of a split at index `i` only depends on the prefix sum up to `nums[i]` and the sum of the entirety of `nums`(`pre[-1]`). That is, if we were to iterate over `nums` from left to right, we can do away with the list of prefix sums by maintaining a rolling sum up to the current element(the prefix sum) and computing the sum of `nums` beforehand. `pre` now becomes a single integer that represents the sum of all values up to and including the current element of `nums`. Upon moving to a new element `nums[i]`, the value is first added to `pre` before evaluating the split condition described in the write up for the previous solution.  

#### Conclusion
The time complexity of this solution is identical to that of the previous one. The space complexity is $O(1)$ since `pre` is now a single integer instead of a list of length $n$.  
  

