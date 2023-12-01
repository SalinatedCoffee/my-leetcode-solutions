## 1662. (E) Check If Two Strings are Equivalent

### `solution.py`
The easiest method is to simply compare the concatenation of all strings in `word1` and `word2`. This can easily be achived by using Python's built in `string.join()` method.  

#### Conclusion
This solution has a time and space complexity of $O(m+n)$ where $m$ and $n$ are the number of characters in `word1` and `word2`, respectively. `string.join()` is a linear time operation, and is performed once each on `word1` and `word2`. The concatenated strings will be held in memory to evaluate `==`, which will use $O(m+n)$ space.  
  


### `solution_2.py`
A better solution would be to compare `word1` and `word2` directly, without concatenating their contents. To do this, we must keep track of 4 indices. One each for the current position within `word1` and `word2`, and one each for that within the current element in `word1` and `word2`. We simply iterate along `word1` and `word2` simultaneously, comparing each character within `word1[i]` and `word2[i]`. When we reach the end of either of these strings, we reset the appropriate character index to `0`, and advance the corresponding element index by `1`. The comparisons are then continued, and the process is repeated. Whenever a mismatch is found, we return `False` immediately. If the outer `while` loop exits normally, it still may be the case that `word1` and `word2` have different lengths(for example, `"abcd"` and `"abcdef"`). To account for this we check all four indices to verify whether the entirety of `word1` and `word2` have been examined. If so we return `True`, or `False` otherwise.  

#### Conclusion
The time complexity of this solution is $O(\text{min}(m,n))$, since we only compare the 'comparable' portions of `word1` and `word2`. The space complexity of $O(1)$, as we only keep 6 integers in memory instead of the concatenations of `word1` and `word2`.  
  

