## 930. (M) Binary Subarrays With Sum

### `solution.py`
The brute force solution would involve checking the sum of all possible subarrays of `nums`. If the sums are computed in a linear fashion, this approach would take $O(n^3)$ time to compute. A better approach can be taken by realizing that we can use prefix sums to quickly compute the number of subarrays that sum up to a specific value. At the `i`th value of `nums`, if we know the sum of the subarray `nums[:i+1]` and the number of prefixes that sum up to `goal - sum(nums[:i+1])`, we can trivially count the number of subarrays that add up to `goal` that ends with `nums[i]`. The sum can be computed as we iterate over `nums`, and the number of subarrays that add up to a certain sum can be stored in a dictionary for fast retrieval.  
We first initialize the dictionary `psum_counts`, which will store key-value pairs where the key is the sum and the value the number of prefix arrays that sum up to that value. Because we want to account for the case where the prefix array starting at `nums[0]` sums up to `goal`, we need to remember to set `psum_counts[0] = 1`. As we iterate over `nums`, we first update the current prefix sum, after which we check whether that sum is larger than or equal to `goal`. If it is, we find the number of prefixes that add up to the difference between `goal` and the current sum, and add that to `ret`, which is the total number of prefixes that sum up to `goal`. Finally, we update the number of prefixes for the current sum, after which we move on to the next element in `nums`.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the length of `nums`. `nums` is iterated over exactly once, with each element taking constant time to process. `psum_counts` can at most contain $n$ key-value pairs, hence the linear space complexity.  
  


### `solution_2.py`
If you had the sneaking suspicion that a solution could be written without using a dictionary, you would be right! We can write a sliding window based approach that does away with the dictionary, allowing us to optimize the space complexity down to $O(1)$.  
The base principle is similar to the previous solution, which is that we can compute the number of desired subarrays by using a count of some sort that pertains to the previous elements. Returning to the problem description, we know that the elements in `nums` can only be either a `0` or a `1`. Obviously, a `0` would not change the sum of the window. Thus, if a window sums up to `goal`, we can also determine the number of *suffix* subarrays of that window if we know the number of leading `0`s within that window. We contract the window whenever the window sum is larger than `goal` or the first element in the window is `0`. As the window is contracted we count the number of leading `0`s, as well as updating the window sum. After the window has finished contracting (or not contracted at all) we check whether the current window sums up to `goal`, adding the appropriate amount to `ret` based on the number of leading zeros.  

#### Conclusion
The time complexity of this solution is $O(n)$. The space complexity is $O(1)$, as we only use a handful of fixed-size variables during the entire running time.  
  

