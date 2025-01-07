## 1408. (E) String Matching in an Array

### `solution.py`
Given the list of strings `words`, we are asked to return a list of the strings in `words` that are a substring of another string in `words`. Because the size constraints on `words` and the strings that it contains is small, we can take a brute force approach that scans through the entirety of `words` for each string. Conveniently, Python's `in` keyword performs substring matching when it is used on a string with a string. For example, `string_a in string_b` searches for an instance of `string_a` in `string_b`, evaluating to `True` if it exists and `False` otherwise.  

#### Conclusion
This solution has a time complexity of $O(n^2m)$, where $n$ is the length of `words` and $m$ is the average length of the strings in `words`. The entirety of `words` is examined for each word in `words`, and a pair of strings will take $O(m)$ time to process as we check whether a string is a substring of the other string. The space complexity is $O(1)$, excluding the returned list `res`.  
  

