## 2185. (E) Counting Words With a Given Prefix

### `solution.py`
Given the list of strings `words` and string `pref`, we are asked to determine the number of elements of `words` that has `pref` as a prefix. Because the problem constraints are relatively small, we can trivially solve this problem through a brute force approach. We simply iterate over `words` while comparing `pref` against each string. If `pref` is indeed a prefix of a string, we increment a counter by `1`.  

#### Conclusion
This solution has a time complexity of $O(n\cdot\max(m, k))$, where $n$ is the length of `words`, $m$ is the average length of the elements of `words`, and $k$ is the length of `pref`. All strings are examined, and the time required to verify a single string scales linearly with the length of the string or the length of `pref`, whichever is shorter. The space complexity is $O(k)$, as the relevant portion of each string is sliced when comparing it against `pref`.  
  

