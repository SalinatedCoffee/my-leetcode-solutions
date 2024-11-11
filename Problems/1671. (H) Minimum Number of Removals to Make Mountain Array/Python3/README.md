## 1671. (H) Minimum Number of Removals to Make Mountain Array

### `solution.py`
Given the list of positive integers `nums`, we are asked to return the minimum number of elements that can be removed to make `nums` a 'mountain array'. A mountain array is a list of integers where there exists an index `i` such that `0 < i < len(nums)` and `nums[0] < nums[1] < ... < nums[i-1] < nums[i]` and `nums[i] > nums[i+1] > ... > nums[-2] > nums[-1]`. `nums` has a length of at least 3. It is not immediately obvious as to what approach we should be taking for this problem, except for the fact that a brute force approach would be prohibitively inefficient. We are asked to determine the *minimum number of removals* in order to make `nums` a mountain array. In other words, we want to leave as many elements of `nums` as we can intact when making it a mountain array. A mountain array involves a single 'peak', where the elements are strictly decreasing moving towards the left and strictly increasing moving towards the right. This means that a mountain array can be split into three parts; the prefix that contains elements that are strictly increasing, the peak element, and lastly the suffix, which contains elements that strictly decrease. If we know the length of the longest increasing subsequence for `nums[:i]` and the longest decreasing subsequence for `nums[i+1:]` for all possible `i`, we can easily determine the length of the longest mountain array in `nums`, which we can use to compute the number of minimum removals required to make `nums` a mountain array.  
The longest increasing subsequence is a well known problem in computer science, and can be solved in linear-logarithmic time through the binary search version of the algorithm. Essentially, we maintain an ordered list of elements of the current longest increasing subsequence while iterating over the list being searched. For each element of the list, we use binary search to identify where the element would fit inside the current LIS. If it is larger than the largest element in the LIS, it is appended to the LIS, extending it by 1. Otherwise, the element is inserted into the LIS at the index identified during the binary search step. Because the algorithm scans through the original list from left to right, we can trivially modify the algorithm to identify the LIS length for each prefix of `nums` by recording the length of the current LIS at every index. We can also reuse this algorithm to compute the length of the LDS of each suffix by reversing `nums`, running the modified algorithm, and reversing the resulting list of LDS lengths. If `lis_lens` is a list of LIS lengths where `lis_lens[i]` is the length of the LIS in `nums[:i+1]` and `lds_lens` is a list of LDS lengths where `lds_lens[i]` is the length of the LDS in `nums[i:]`, the number of removals required to make `nums` a mountain array with a peak at `nums[i]` is simply `len(nums) - (lis_lens[i] + lds_lens[i]) + 1`.  
The function `lis` takes a single argument `arr`, and returns a list containing the length of the LIS in each prefix of `arr`. `lis` is first called with `nums` to compute the LIS lengths, and a second time with `nums` reversed to compute the LDS lengths. The returned list of LDS lengths is reversed to bring it back in line with the original indices of the suffixes. We then consider all possible peaks for `nums`, but only for cases that would result in a valid mountain array(left and right side of the peak contain at least 1 element). The number of removals required to make `nums` a mountain array at that peak is computed by evaluating the previously described expression, and the smallest value among them is returned.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$, where $n$ is the length of `nums`. Computing the LIS lengths for each and every prefix of `nums` requires $O(n\log n)$ time to complete, as a binary search on the current LIS(which length is bound by $n$) is performed for each and every element of `nums`. The same algorithm is used to compute the LDS lengths, which means that the LIS/LDS computation step requires O(n\log n)$ time to complete. Reversing `nums` and the original list of LDS lengths both finished in $O(n)$ time each, as well as the computation of the minimum number of removals required. Hence, the overall time complexity of this solution is $O(n\log n)$. The space complexity is $O(n)$, as the lists containing the LIS/LDS lengths are kept in memory until the algorithm exits.  
  
