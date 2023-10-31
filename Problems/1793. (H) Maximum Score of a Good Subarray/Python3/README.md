## 1793. (H) Maximum Score of a Good Subarray

### `solution.py`
The score of a subarray is simply the product of its smallest value and its length. A good subarray is one that contains `nums[k]`, and we are asked to determine the largest score across all good subarrays. Because we know that any subarray we should be considering *must* contain `nums[k]`, we can simply fan out starting at `nums[k]` and search for the largest score possible.  
Starting at `nums[k]`, we compare either ends of the window and greedily expand into the side that has the larger value. We update the subarray minimum value and maximum score accordingly, and continue expanding until the window fills up the entirety of `nums`.  

#### Conclusion
The time complexity is $O(n)$, where $n$ is the length of `nums`. `nums` is essentially traversed exactly once, and when a new value is introduced into the expanding window, we only perform a handful of $O(1)$-time operations. The space complexity is $O(1)$.  
  

