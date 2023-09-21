## 1658. (M) Minimum Operations to Reduce X to Zero

### `solution.py`
Instead of finding the minimum length prefix + suffix that sums up to `x`, we can flip the problem on its head and find the maximum length subarray that adds up to `target = sum(nums) - x`, which is much easier than the original problem. We can take a sliding window approach here, where we greedily expand the window as much as possible and shrinking it only when the window sum exceeds that of `target`. The maximum window length is only updated whenever the window sum is *exactly* equal to `target` - if this length is never updated even after we have finished processing `nums`, this means that there is no window that sums up to `target`, and thus a prefix + suffix pair that sums up to `x` does not exist in `nums`.  

#### Conclusion
The time complexity is $O(n)$, where $n$ is the length of `nums`. Two pointers are advanced through `nums`, with the worst case being that both pointers move along the entierety of the array - hence the linear running time. The space complexity is $O(1)$.  
  

