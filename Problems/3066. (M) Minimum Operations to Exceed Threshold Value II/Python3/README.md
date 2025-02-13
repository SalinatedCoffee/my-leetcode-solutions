## 3066. (M) Minimum Operations to Exceed Threshold Value II

### `solution.py`
Given the array of positive integers `nums`, we are allowed to perform the following steps in a **single** operation:  

- Select the 2 smallest integers `x` and `y` and remove them from `nums`.  
- Add `min(x, y) * 2 + max(x, y)` anywhere in `nums`.  

Our task is to determine the *minimum* number of operations that must be performed until all elements in `nums` are greater than or equal to `k`.  
Because we can only remove the smallest 2 values in `nums` during a single operation, and we want to make sure that all elements of `nums` are larger than or equal to `k`, we can easily solve this problem by converting `nums` into a min heap. We then keep performing operations as long as the smallest element of `nums` is strictly less than `k`. Since `nums` is given such that an answer is guaranteed to exist, we do not have to check for its length.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$, where $n$ is the length of `nums`. Converting `nums` into a min heap requires $O(n\log n)$ time to complete. Adding and removing items from that heap each take $O(\log n)$ time to perform, and in the worst case will occur $n-2$ times. Hence, the simulation step will complete in $O(n\log n)$ time as well. The space complexity is $O(1)$, since we have converted `nums` into a min heap in-place instead of creating a copy. Note that this behavior should be avoided whenever possible. In this case, the space complexity will be $O(n)$.  
  

