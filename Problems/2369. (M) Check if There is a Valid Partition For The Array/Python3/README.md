## 2369. (M) Check if There is a Valid Partition For The Array

### `solution.py`

If we know that the prefix subarray `nums[:i]` has a valid partition, we can also say that `nums[:i+2]` and/or `nums[:i+3]` also have a valid partition depending on whether `nums[i:i+2]` and/or `nums[i:i+3]` can be considered valid according to the conditions given to us in the problem description. Because we have determined that there is a clear relationship between the original problem and its smaller subproblems, we can take a dynamic programming based approach to this problem.  

As established earlier, we can say whether an array is valid based on two pieces of information; the 'partitionability' of its prefix subarrays, and the validity of the smallest partitions that comes after those prefixes. The problem gives us 3 cases for a valid partition. 2 adjacent elements are equal, or 3 adjacent elements are equal, or 3 adjacent elements strictly increase with a difference of `1`. Assume we are considering some index `i`, where we want to determine if `nums[:i+1]` has a valid partition. According to the 3 cases the partitionability of `nums[:i+1]` depends on 3 values: the partitionability of `nums[:i-1]` and the evaluation of `nums[i] == nums[i-1]`, the partitionability of `nums[:i-2]` and the evauation of `nums[i] == nums[i-1] == nums[i-2]`, and the partitionability of `nums[:i-2]` and the evaluation of `nums[i] == nums[i-1]+1 == nums[i-2]+2`. `nums[:i+1]` is partitionable if **any** of these 3 cases evaluate to `True`, and so we can string these expressions together with logical ORs.  

The base case is when `i < 0` or `i == 0`. If `i < 0`, it means we are checking for the partitionability of an empty string, which is always `True`. If `i == 0`, it means that we are checking for the partitionability of a string with only 1 element, which is always `False`.  

#### Conclusion

This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. There can be at most $n$ possible states in the recursive function described above, for each of which we perform a fixed number of operations to compute its value. The space complexity is also $O(n)$.  


