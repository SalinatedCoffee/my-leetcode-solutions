## 2215. (E) Find the Difference of Two Arrays

### `solution.py`
This is a trivial problem to solve (given the generous problem constraints) and thus has multiple valid approaches. Here we will be using sets since they allow us to access elements in constant time and disallows duplicates, which we do not want.  
We first initialize two sets and store the contents of `nums1` and `nums2`, which will eliminate any duplicates. Then we iterate over the elements of each set, adding it to a list if it is not present in the other set.  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ and $n$ are the length of `nums1` and `nums2`, respectively. Generating the set representations of both lists takes $O(m+n)$ time, after which they are iterated over once each where every iteration takes $O(1)$ time to run. The space complexity is also $O(m+n)$ since the sets `s1` and `s2` can contain at most $m$ and $n$ elements.  
  

