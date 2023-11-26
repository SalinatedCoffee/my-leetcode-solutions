## 1685. (M) Sum of Absolute Differences in a Sorted Array

### `solution.py`
As the array is already sorted in ascending order, we can see that we could use prefix sums to compute the desired value at each element instead of taking the brute force approach. If we know the sum of all elements up to the `i`th element, we can easily compute the compound difference by subtracting the prefix sum from `nums[i]*(i+1)`. The same principle can be applied to the latter section of the array, where we swap the terms and subtract `nums[i]*(n-i)` from the sum of the subarray `nums[i:]`. This partial sum can also be computed using the prefix sums by subtracting the prefix sum up to the `i-1`st element from the prefix sum of the entirety of `nums`.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the length of `nums`. Precomputing the prefix sums for each element takes $O(n)$ time, and storing these values will use $O(n)$ memory.  
  

### `solution_2.py`
The last element in the prefix sums from the previous solution is simply the sum of all elements in `nums`. We also notice that when we compute the sum of differences for an element `i`, we *only* use the prefix sum up to that element. Hence, we can compute the prefix sum simultaneously as we compute the difference sums for each element. The other prefix sum that is used is that of the last element, which is the sum of `nums` as mentioned earlier. We iterate along `nums` while keeping track of `pre`, which is the prefix sum up to the current element.  

#### Conclusion
This solution has a time complexity of $O(n)$, and a space complexity of $O(1)$. We do not precompute the prefix sum and instead use a single integer to store the prefix sum up to the current element in `nums` being examined.  
  

