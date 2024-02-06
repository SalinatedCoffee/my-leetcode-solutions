## 49. (M) Group Anagrams

### `solution.py`
We want to group the strings in `strs` so that all strings in each group are an anagram of each other. A word is an anagram of another when it has exactly the same number of each unique letter as the other word. Hence, if we can somehow convert a string to a form that represents the frequency count of each letter, we can simply pass this into a dictionary to group the strings. Since a list (or a dictionary) is not a hashable object in Python, we need to represent the frequency count with a string instead. One method that is both easy to understand and simple to implement would be to simply concatenate a letter and its count, in alphabetic order. For example, the string `"abbcd"` would be represented as `"a1b2c1d1"`. Using this method, strings that are anagrams of each other will be represented by the same string, and thus will have identical hash values.  
The `defaultdict` `groups` is initialized, with `list` as the default constructor. `groups[cmpr]` will be a list of strings that are represented by the frequency string `cmpr`. `strs` is then iterated over, where a frequency count is generated for each string `s` after which it is converted into string form. The appropriate list in `groups` is then retrieved using the frequency string, and the string `s` is appended to the end of that list. Once the entierety of `strs` has been examined, we simply return the list of all values in `groups`.  

#### Conclusion
The time complexity of this solution is $O(mn)$, where $m$ is the average length of all strings in `strs`, and $n$ is the length of `strs`. We generating the frequency string for every string in `strs`, with each generation taking $O(m)$ time on average. The space complexity is $O(n)$ since `groups` will contain $n$ strings by the time when the `return` statement is executed.  
  

