## 349. (E) Intersection of Two Arrays

### `solution.py`
We simply need to convert the two arrays into sets, and return the intersection of the two sets cast into a list.  

#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ and $n$ are the lengths of `nums1` and `nums2`, respectively. Converting both lists into sets takes $O(m+n)$ time, and computing the intersection takes $O(m)$ (or $O(n)$) time. As the size of the intersection is bound by $m$ and $n$, it stands to reason that converting the intersection into a list will take $O(m)$ or $O(n)$ time as well. The space complexity is also $O(m+n)$.  
  

