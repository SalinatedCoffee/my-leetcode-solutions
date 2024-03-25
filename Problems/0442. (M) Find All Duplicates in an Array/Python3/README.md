## 442. (M) Find All Duplicates in an Array

### `solution.py`
The problem can trivially be solved by using a hash map(or a simple array, since we know the range of the entries in `nums`). Unfortunately, we are asked to implement an algorithm that does not use any extra memory, making this approach no longer viable. We can instead turn our attention to `nums` itself; we know that all elements in `nums` are in the range `[1, len(nums)]`, which tells us that we could mark items in `nums` in some way to indicate that an element has been discovered. In order to achieve this without modifying the element's information, we can simply change its sign to negative. As we iterate over `nums`, we check the value of `nums[nums[i]-1]`(since the values of `nums` is 1-indexed). If that value is already negative, it means the value `i` has already been discovered in `nums`, so we append that value to the list to be returned. Otherwise, we negate the value to indicate that `i` has been discovered.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. `nums` is iterated over once, and processing each value takes $O(1)$ time. The space complexity is $O(1)$, as required by the problem.  
  
