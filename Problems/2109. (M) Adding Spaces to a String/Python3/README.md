## 2109. (M) Adding Spaces to a String

### `solution.py`
Given the string `s` and list of non-negative integers `spaces`, we are asked to insert whitespaces in `s` according to `spaces` and return the resulting string. A whitespace should be inserted into `s` for each value in `spaces`, with each whitespace being inserted before the character at index `spaces[i]` for all possible `i`. For example, if `s = "aquickbrownfox"` and `spaces = [1, 6, 11]`, the resulting string would be `"a quick brown fox"`. `spaces` is guaranteed to be sorted.  
We can trivially solve this problem by using a list and two pointers. The resulting string will be constructed in the list character by character. One pointer will point to the character in `s` currently being considered, and another will point to the index in `spaces` that should be inserted next. For each character, we check its index against the current value in `spaces`. A single whitespace is appended to the list only if these two values match, with the pointer for `spaces` being incremented by `1` afterwards. The current character of `s` is then appended onto the list, and these steps are repeated until all characters of `s` have been examined. The list of characters is then concatenated into a single string before being returned.  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ is the length of `s` and `m` is the length of `spaces`. Each pointer iterates over the entirety of the iterable it is referencing, which means that `s` and `spaces` are traversed exactly once. The completed string will have a length of `m+n`, and concatenating it will naturally require $O(m+n)$ time to complete. The space complexity is also $O(m+n)$, due to the list of characters `res` in which the resulting string is constructed.  
  

