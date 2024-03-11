## 2540. (E) Minimum Common Value

### `solution.py`
The most easiest way to approach this problem is to convert the two lists into sets, compute the intersection of those sets, and then iterate over said intersection to determine the smallest value. If the intersection is the empty set, we simply return `-1`.  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ and $n$ are the lengths of `nums1` and `nums2`, respectively. The list conversions are linear time operations, as well as computing the intersection of the resulting sets. The space complexity is also $O(m+n)$.  
  

### `solution_2.py`
We can make use of the fact that `nums1` and `nums2` are already in ascending order, to implement a more optimized solution than the previous one. Assume we are currently looking at the `i`th element of `nums1` and `j`th element of `nums2`, where all elements before the current ones have already been examined. If `nums1[i] != nums2[j]`, it is the case that `nums1[i]` is either larger than `nums2[j]`, or smaller. For the former, it would be logical to say that we should advance `j` by `1` since `nums2` is arranged in ascending order, and as such we should try searching for a match to `nums1[i]` by looking at the value in `nums2` that is immediately larger than `nums2[j]`. The same argument can be used for the latter, with the difference being that `i` is incremented instead. Whenever `nums1[i] == nums2[j]`, it is guaranteed to be the first discovered common value between the two lists, and consequently the smallest common value since both lists are arranged in ascending order.  

#### Conclusion
The time complexity of this solution is $O(m+n)$. Each list is essentially iterated over exactly once, with each iteration taking constant time to process. The space complexity is $O(1)$, as only a handful of variables with a fixed size are used over the entire runtime of the solution.  
  

