## 1624. (E) Largest Substring Between Two Equal Characters

### `solution.py`
If we reframe the problem, we essentially want the maximum difference between the indices of two identical characters in `s`, where the indices are not equal. Because we know that `s` can only contain lowercase English letters, we can determine the first and last occurrence of each unique letter in `s` and return the largest difference.  
We iterate over `s`, while updating the smallest and largest indices for the current character. Once the iteration exits, we iterate over each index pair while computing the difference between the two indices. Finally, we return the largest difference among those previously computed, or `-1` if no such pair exists for `s`.  

#### Conclusion
The space complexity is $O(nk) = O(26n) = O(n)$, where $n$ is the length of `s`. `s` is iterated over once, and each character in `s` takes constant time to process. The space complexity is $O(k) = O(26) = O(1)$.  
  

