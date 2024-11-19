## 2461. (M) Maximum Sum of Distinct Subarrays With Length K

### `solution.py`
Given the list of integers `nums`, and integer `k`, we are asked to determine the largest sum among all subarrays of length `k` that contains only distinct elements. Intuition tells us that we can use a sliding window approach to efficiently compute the sum of each subarray, and a dictionary to keep track of the contents of the current window. If the number of key-value pairs in the dictionary is equal to `k`, the subarray is valid, and we attempt to update the previously seen maximum subarray sum.  
The contents of the current window will be stored in the `Counter` `w_nums`, where the keys are the unique values within the window and values the number of appearances of each unique value within the window. `w_sum` will represent the sum of all elements in the window, and `res` will be the largest sum amongst all valid subarrays oberved up to now. `w_nums` and `w_sum` are initialized using the prefix subarray `nums[:k]`, and `res` is initialized to either `w_sum` or `0`, depending on the number of key-value pairs in `w_nums`. The sliding window step can now begin, where we slide the window to the right by `1` and check whether the window is valid. If `w_nums` contains exactly `k` key-value pairs, we compare `w_sum` and `res`, updating the value of the latter variable accordingly. Once all subarrays have been considered, `res` will contain the desired value.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. There are $n - k + 1$ subarrays of length $k$ within `nums`, and since sliding the window by `1`, as well as validating the contents of each window each require $O(1)$ time to complete, the overall time complexity comes out to be $O(n)$. The space complexity is $O(n)$, due to `w_nums`.  
  

