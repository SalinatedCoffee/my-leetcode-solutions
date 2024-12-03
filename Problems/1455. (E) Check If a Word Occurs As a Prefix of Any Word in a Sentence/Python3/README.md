## 1455. (E) Check If a Word Occurs As a Prefix of Any Word in a Sentence

### `solution.py`
Given a sentence as the string `sentence`, we are asked to determine the minimum index of a word in the sentence that has `searchWord` as its prefix. `sentence` contains only lowercase English letters and whitespaces, and `searchWord` contains only lowercase English letters and is not the empty string. We can easily split `sentence` into a list of words by using the `string.split()` method, which returns an iterable containing substrings resulting from splitting `sentence` using a single whitespace as the delimiter. We then iterate over this iterable, comparing each word with `searchWord`. If a match is found, we immediately return the index of the current word. Otherwise, the iteration will exit normally, at which point we return `-1` as requested by the problem.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `sentence`. Splitting `sentence` into a list of its constituent words requires $O(n)$ time to complete, as well as iterating over the list of words and comparing them against `searchWord`. The space complexity is also $O(n)$, as the list of words is kept in memory until the algorithm exits.  
  

