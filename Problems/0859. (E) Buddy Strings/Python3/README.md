## 859. (E) Buddy Strings

### `solution.py`
We must compare both strings character by character in order to determine if they are a valid pair or not, which is trivial to implement. The edge case is when both strings are identical, but also only contain at most 1 of each letter (such as `s = goal = alhwc`). Since a swap **must** be made, we can intuitively see why this is invalid. Thus, we need to keep track of the frequency of each letter as well as the number of mismatching pairs.  

#### Conclusion
The time complexity is $O(n)$, where $n$ is the length of `s` (and thus also `goal`). The space complexity is $O(1)$ since `src` and `tgt` will at most contain 26 key-value pairs.  
  

