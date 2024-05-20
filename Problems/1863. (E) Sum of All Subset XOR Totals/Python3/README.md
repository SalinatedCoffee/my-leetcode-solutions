## 1863. (E) Sum of All Subset XOR Totals

### `solution.py`
Looking at the problem constraints, it looks like we can simply try computing the XOR sum of every possible subset of `nums` and calculate the total. This can be easily achieved through recursion, where we try both including and excluding a certain value of `nums` before recursing on the remaining elements. The function `recurse` takes two arguments; `idx`, the index of the element in `nums` currently being considered, and `xor`, the XOR sum of all previous elements. Given these two values, `recurse` will return the XOR total of all subsets of `nums[idx:]` where the previous XOR sum is `xor`. When `recurse` is called, we first check the value of `idx`. If it is equal to `len(nums)`, we have run out of values to examine and so we return the XOR sum `xor`. Otherwise, we try both choices as briefly mentioned earlier. We try recursing on the remaining elements of `nums` once without adding `nums[idx]` to the XOR sum, and once with. This simply translates to the expression `recurse(idx+1, xor) + recurse(idx+1, xor^nums[idx])`, which we can directly return.  
By definition of `recurse`, the value we want is the return value of `recurse(0, 0)`.  

#### Conclusion
This solution has a time complexity of $O(2^n)$ where $n$ is the length of `nums`. Looking at the recursion tree, each element branches off into two choices. Since there are $n$ elements in `nums`, the number of branches(which corresponds to the number of subsets) is $2^n$, bringing the overall time complexity to $O(2^n)$. The space complexity is $O(n)$, due to the recursion stack having a max height of $O(n)$.  
  

