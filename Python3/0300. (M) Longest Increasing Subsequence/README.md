## 300. (M) Longest Increasing Subsequence

### `solution.py`
Intuition tells us that we may solve this problem through dynamic programming, since we could devise an algorithm that computes the LIS length at a certain element based on previously computed values.  
We first intialize a list `dp` of length `len(nums)` with `1` as its values (minimum length of a subsequence is 1). `dp` contains the LIS lengths ending at a specific index; that is, `dp[i]` contains the LIS length of all subsequences in the range `nums[0:i]` that ends with `nums[i]`. To populate `dp[i]` we know that we must examine all elements in the range `dp[0:i]`, since we are looking for the longest possible subsequence length ending at index `i`. A nested loop can do the trick, where the outer loop (loop variable `i`) iterates over `nums` and the inner loop (loop variable `f`) over `dp[0:i]`. At each step we first check if `nums[i]` is larger than `nums[f]` (valid subsequence) and if so, we check whether `dp[f]+1` is larger than `dp[i]` (new subsequence is larger than current longest). Only when the two conditions evaluate to true do we update the value at `dp[i]` to `dp[j]+1`.  
After exiting the loop, we return the largest value stored in `dp` (as the longest subsequence may not end with `nums[-1]`).  
  
#### Conclusion
This solution takes $O(n^2)$ time to run and uses $O(n)$ space, where $n$ is the length of `nums`.  
  

### `solution_2.py`
The follow-up question asks if we could solve this problem in $O(n\log n)$ time instead. If we could, intuition tells us that there is a high possibility that some kind of binary search is involved since the desired time complexity has a logarithmic term.  
Leaving this thought alone for a while, let's see if there exists a fundamentally different approach to the one used in the first solution. We could save the subsequences explicitly, keeping multiple lists in memory and appending `nums[i]` if it is larger than the last element in those lists. If `nums[i]` is smaller, we can create a new list prefixed with the longest subsequence ending with `nums[i]`. It does seem however that this approach would not be very efficient, even compared to the first solution. What we can do here is notice that we're only interested in the *length* of the LIS, not the subsequence itself. Thus we can *collapse* these lists into a single list, where instead of creating a new list whenever `nums[i]` is smaller we replace the largest element smaller than `nums[i]` - *overlaying* the 'new' subsequence on top of the older one. To figure out which element needs to be replaced we may use binary search (`bisect.bisect_left()`).  
Once we are finished iterating over `nums`, the length of the 'subsequence' list is the length of the LIS of `nums`.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$, as requested by the follow-up question. We iterate over `nums` and at every step we perform a binary search, which scales with $n$. The space complexity is $O(n)$, since the subsequence list can at most have length $n$.  
  

