## 2542. (M) Maximum Subsequence Score

### `solution.py`
We are *required* to take `k` pairs of integers, which means that we should be selecting pairs where the value in `nums2` is as large as possible. This is because the minimum value of all selections in `nums2` will be used as the multiplier, hence it is optimal to keep this value as large as possible. There will however, be instances where it is optimal to select a pair with a smaller value than the minimum of the current selection. For example, consider `nums1 = [10, 1], nums2 = [1, 2], k = 1`. The pair `(1, 2)` at index `1` has the larger value of `nums2`, but selecting the pair at index `0` will yield the largest score since the value of `nums1` is large enough to offset the loss from only multiplying by `1` instead of `2`. Thus our rough algorithm is as follows: greedily select k number of pairs with the largest `num2` values, then examine remaining pairs in descending `nums2` order. The last question we need to answer is what selected pair should be evicted when considering a new pair. If we sort the two input arrays in ascending order according to `nums2` and iterate along them in reverse order(thereby examining the largest `nums2` values first), it stands to reason that we should evict the pair with the smallest value of `nums1` since we want to minimize the potential score loss that would occur. We can store the `nums1` values in a min heap so that we can access this score in constant time.    

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `nums1` and `nums2`. Sorting both arrays takes $O(n\log n)$ time, after which they are iterated over once, and a single iteration step takes $O(\log n)$ time to compute due to heap operations. The space complexity is $O(n)$.  
  
