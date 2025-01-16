## 2425. (M) Bitwise XOR of All Pairings

### `solution.py`
Given the lists of non-negative integers `nums1` and `nums2`, we are asked to determine the XOR sum of the list of all value pairs between the two lists XORed. For example, if `nums1 = [1, 2]` and `nums2 = [3, 4]`, there are 4 possible pairs of values. Listing them out, we would get `(1, 3)`, `(1, 4)`, `(2, 3)`, and `(2, 4)`. XORing each pair would result in the list `[2, 5, 1, 6]`, which has the XOR sum of `2 ^ 5 ^ 1 ^ 6 == 0`.  
We can immediately see that a brute force approach will not work given the problem constraints. By exploiting a property of the bitwise XOR operation, we can implement a dramatically faster algorithm. Recall that XORing a value with itself will result in the value of `0`. XORing `0` with a non-zero value yields the non-zero value itself. This means that if we were to continuously XOR a value with itself, the value will switch between `0` and the value itself depending on the number of XORs that have been performed. Simply put, XORing a value with itself an odd number of times will result in `0`, while doing to an even number of times will result in the value itself. Returning to the problem description, we notice that a value will be XORed multiple times; more specifically, any element in `nums1` will be XORed `len(nums2)` times(and vice versa). Thus, if the length of `nums2` is *even*, the values in `nums1` will not contribute to the final result.  
Implementing this solution is trivial. We look at the length of `nums1` to determine whether the XOR sum of `nums2` should be computed, and vice versa. The resulting values are then XORed themselves, after which the result is returned.  

#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ and $n$ are the lengths of `nums1` and `nums2`. In the worst case, the XOR sum of `nums1` and `nums2` must be computed, which is a linear time operation that scales with the length of the list. The space complexity is $O(1)$.  
  

