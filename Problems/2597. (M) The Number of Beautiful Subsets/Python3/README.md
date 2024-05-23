## 2597. (M) The Number of Beautiful Subsets

### `solution.py`
The most straightforward approach in solving this problem is backtracking, using a set to keep track of the current subset. For each element there are 2 choices that can be made. Either we simply skip that element and move onto the next, or we add it to the subset if possible. `recurse` takes one argument `idx`, which represents the index of the element in `nums` currently being considered. If `idx == len(nums)`, there are no elements left to consider, and we return `1` if the subset is not empty. Otherwise, we check whether the values `nums[idx] - k` and `nums[idx] + k` are not in the subset. If so, we add the `nums[idx]` to the subset and recurse on the next element `idx + 1`. Once this recursive call returns, we also need to remember to restore the subset to the state prior to adding `nums[idx]` as we still need to account for the case where `nums[idx]` is skipped. Once this is done, we can recurse on `idx + 1` one more time and return the sum of these values. By definition of `recurse`, the value we want is the return value of `recurse(0)`, which we can return directly.  

#### Conclusion
This solution has a time complexity of $O(2^n)$, where $n$ is the length of `nums`. All possibilities are explored when considering the elements of `nums`, and since each value can have 2 choices at most, the total number of subsets that can exist is $2^n$. The space complexity is $O(n)$, both due to the recursion stack and the set used to store the currently selected elements.  
  

