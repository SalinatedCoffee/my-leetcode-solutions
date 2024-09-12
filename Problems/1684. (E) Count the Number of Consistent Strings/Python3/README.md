## 1684. (E) Count the Number of Consistent Strings

### `solution.py`
A word in the list `words` is considered consistent if all unique characters in the word also appears in the string `allowed`. Given `words` and `allowed` then, we are asked to return the number of words in `words` that are consistent. We can easily solve this problem by using Python sets, which conveniently support set-like comparison operations. Among these, we can use the less than or equal operator to determine whether a set is a subset of another set. For example, `set(A) <= set(B)` will evaluate to `True` if all elements in `set(A)` also exist in `set(B)`.  
We first initialize the set `whitelist`, passing in `allowed` as the argument. `words` is then filtered by the expression `set(word) <= whitelist` for each string `word` in `words`, removing `word` from `words` if the expression evaluates to `False`. Once this step completes, all strings remaining in `words` are consistent, and we simply need to return its length.  

#### Conclusion
This solution has a time complexity of $O(nk)$, where $n$ the length of `words` and $k$ is the average length of the strings within `words`. The set `whitelist` is first instantiated using the contents of `allowed`, but since `allowed` only contains unique lowercase English letters its length can be at most 26 and can be considered as being constant. `words` is then iterated over to check the consistency of each word, which is accomplished by converting the word into a set and comparing it with `whitelist`. Unlike `allowed`, a string in `words` *can* contain duplicate letters, meaning that the maximum length of a word is longer than 26 characters. Thus we introduce a new term $k$ representing the average length of a word in `words`. The space complexity is $O(l)$, where $l$ is the length of the longest string in `words`. The size of the set `whitelist` has a fixed upper bound, but the temporary set generated from each word in `words` does not.  
  

