## 238. (M) Product of Array Except Self

### `solution.py`
The naïve solution is to just iterate across `nums` for every element, resulting in a running time of $O(n^2)$ with $n$ being the length of `nums`. We can do better however, by remembering that multiplication is commutative ($ab = ba$). At an element, we can 'split' `nums` into three parts. A subarray left to the element, the element itself, and the subarray right to the element. To get the desired product then, we simply need to multiply the products of the left and right subarrays. We can compute the left-hand product trivially by filling a list of length `len(nums)` with the cumulative products of `nums`. Then we can iterate through `nums` in reverse order while computing the cumulative product, which will be the product of the right-hand subarray.  
  
#### Conclusion
This solution runs in $O(n)$ time and $O(n)$ space, where $n$ is the length of list `nums`.  
  

