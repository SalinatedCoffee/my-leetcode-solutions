## 1347. (M) Minimum Number of Steps to Make Two Strings Anagram

### `solution.py`
Because we can change *any* character in `t` to *any* letter, we essentially need to find the number of operations to change the letter frequency count of `t` to match that of `s`. Thankfully, `s` and `t` have the same length, and there are no operations that would affect the length of `t`. This makes this problem considerably easier, as we can simply compute the number of required operations given the frequency counts of both strings. As mentioned above, `s` and `t` have the same length, and so it is guaranteed to be possible to convert `t` into an anagram of `s`. More specifically, if `t` has less of some letter than `s`, it is **guaranteed** that there will be an equal number of 'excess' letters in `t` that can be changed to fill the deficit fot that letter, since `s` and `t` have equal lengths. Thus, we can simply count the number of characters that `t` has a deficit of compared to `s`, and that will be the desired answer.  
We first generate the letter frequencies of both strings using Python `Counter`s(ASCII-based lists would also suffice). Next, we iterate over all unique letters in `s`. If the frequency of that letter in `s` is larger than that of `t`, we have found a deficit, and so we add the deficit amount to the sum `ret`. Once all letters in `s` have been accounted for, we can directly return `ret`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`(and consequently `t`). Counting the frequency of each character in `s` and `t` takes $O(n)$ time each. Determining the deficit takes $O(1)$ time as there can only be 26 unique letters in `s`, hence the overall time complexity of $O(n)$. The space complexity is $O(1)$ as the `Counter`s will only contain 26 key-value pairs.  
  

