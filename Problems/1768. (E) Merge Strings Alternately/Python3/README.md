## 1768. (E) Merge Strings Alternately

### `solution.py`
This is a simple problem where we need to iterate over both strings in an alternate manner. A straightforward approach is to maintain a pointer for each string, and increment them alternately. Once one pointer has reached the end of its string we simply append the remainder of the other string, if it exists.  

#### Conclusion
This solution has a time and space complexity of $O(m+n)$ where $m$ and $n$ are the length of `word1` and `word2`, respectively.  
  

