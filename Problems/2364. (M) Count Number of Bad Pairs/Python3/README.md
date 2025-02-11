## 2364. (M) Count Number of Bad Pairs

### `solution.`
`nums` is a list of positive integers. A pair of elements `nums[i]` and `nums[j]` is considered a bad pair if `i < j` and `j - i != nums[j] - nums[i]` evaluate to true. Given `nums`, we are asked to determine the total number of bad pairs.  
Looking at the problem constraints, we can see that a brute force approach is not possible. We can come up with a better solution by realizing the fact that the number of bad pairs is simply the number of total pairs subtracted by the number of non-bad pairs. A non-bad(good) pair would be a pair of element where the expression `j - i == nums[j] - nums[i]` evaluates to true. Since the expression is now an equality instead of an inequality, we can arrange the terms to get `j - nums[j] == i - nums[i]`. At this point we can see that we could trivially determine the number of good pairs containing `nums[j]` if we had access to the number of elements `i` where `i - nums[i]` is equal to `j - nums[j]`. This would however overcount the number of good pairs, since a pair must also satisfy the inequality `i < j`. In order to address this issue, we can simply iterate over `nums` from the left towards the right while maintaining the number of elements up to the current one for each value of `i - nums[i]`.  
We first initialize an empty dictionary `diff`, where the value of `diff[i]` will be the number of observed elements `nums[j]` where `j - nums[j] == i`. As we iterate over `nums`, we compute the value of `i - nums[i]` and retrieve the corresponding value from `diff`. This is the number of good pairs containing `nums[i]` in the prefix `nums[:i]`, but we actually want the number of bad pairs; which is simply `i - diff[i -nums[i]]`. We add this value to the total count, increment the appropriate value in `diff` by `1`, and continue onto the next element.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `nums`. `nums` is iterated over exactly once, and since each element is processed in $O(1)$ time, the overall time complexity comes out to be $O(n)$. The space complexity is also $O(n)$, due to the dictionary `diff`.  
  

