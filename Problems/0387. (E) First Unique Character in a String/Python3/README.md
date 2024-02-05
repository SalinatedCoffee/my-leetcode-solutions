## 387. (E) First Unique Character in a String

### `solution.py`
We are asked to return the index of the first *unique* character in the string `s`, where `s` only consists of lowercase English letters. In order to determine whether a character appears multiple times in `s` we **must** examine the entirety of `s`, telling us that the optimal solution runs in linear time. Before doing so, we initialize a dictionary `seen` which will contain the smallest index of all unique characters in `s`. If the index for a character is `len(s)`, it indicates that that character is not unique in `s`. While iterating over `s` we first check whether the current character is in `seen`. If it is, the current character is not unique in `s` and as such we set the value in `seen` as `len(s)`. Otherwise, we simply create a new key-value pair in `seen` where the current character is the key and the index of said character the value. Once all characters in `s` have been examined, we simply look through all values in `s` and return the smallest. If the smallest value is `len(s)`, there are no unique characters in `s`, so we return `-1` as requested by the problem.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `s`. `s` is iterated over exactly once, and processing a single character takes $O(1)$ time to complete. The space complexity is $O(1)$. `s` only contains lowercase English letters, of which there are 26 unique characters. Thus `seen` can contain at most 26 key-value pairs, hence the constant space complexity.  
  

