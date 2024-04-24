## 78. (M) Subsets

### `solution.py`
Given a list of unique values `nums`, we want to generate the superset of `nums`. We can trivially solve this problem with recursion, where we recurce twice on each value; once with the value included in the set, and another without. The function `recurse` will take a single value `i`, which will be the index of the element in `nums` currently being considered. If `i == len(nums)`, we have examined all elements in `nums` so we add the current set of values `cur` to the return list `ret`. Otherwise, we first call `recurse(i+1)` to account for the case where `nums[i]` is not included in the set, and then add `nums[i]` to `cur` and call `recurse(i+1)` again. Before returning, we need to remember to remove `nums[i]` from `cur` as we are done examining `nums[i]` and should return `cur` to its previous state.  
To start the recursion we need to call `recurse(0)`, as we are examining the contents of `nums` from left to right.  

#### Conclusion
The time complexity of this solution is $O(2^n)$ where $n$ is the length of `nums`. For a single subset, each value in `nums` can be in either one of two states. It is included in the subset, or it is not. Since we want to find all possible subsets, the time complexity becomes $O(2^n)$. The space complexity is $O(n)$, as the call stack of the recursive calls and the current set `cur` will be at most $O(n)$ big.  
  

