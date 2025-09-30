## 2221. (M) Find Triangular Sum of an Array

### `solution.py`
Given a list of values, we can add each adjacent pair of values together and modulo 10 to generate a new list of values. For example, `new_values[0]` would be the value of `old_values[0] + old_values[1]`, `new_values[1]` the value of `old_values[1] + old_values[2]`, and so on. Given the list of integers `nums` then, we are asked to return the last remaining value after applying these steps `len(nums) - 1` times.  
We can easily solve this problem through brute force, simulating each step by iterating over the list of (computed) values. Since the computation of the `i`th value depends on the `i`th and `i+1`-th values in the previous row, we may perform the computation inside `nums` to save on memory usage(in an interview setting, it would be wise to first ask the interviewer if this is allowed). Once the computation is complete, the desired value will be stored in `nums[0]`.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is the length of `nums`. The space complexity is $O(1)$(or $O(n)$ if the input array cannot be modified).  
A faster solution exists for this problem, but is more mathematically involved. If interested, the reader should look into Pascal's Triangles, Lucas' Theorem, and the Chinese Remainder Theorem. Here is a good [writeup](https://leetcode.com/problems/find-triangular-sum-of-an-array/solutions/7234437/swift-combinatorics-o-n-time-o-1-space) describing the approach in detail.  

