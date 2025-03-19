## 1415. (M) The k-th Lexicographical String of All Happy Strings of Length n

### `solution.py`
A 'happy' string is a string comprised of only `a`s, `b`s, or `c`s, and `s[i] != s[i+1]` for all possible `i` in the range `0 <= i < len(s)-1`. Given the positive integers `n` and `k`, we are asked to return the `k`th lexicographically small happy string with length `n`.  
Because `n` and `k` are relatively small, we can explicitly generate all `k` happy strings in ascending lexicographical order. We can generate the strings recursively, starting with the lexicographically smallest string of length `n` and incrementally building up to the `k`th string. Starting with the leftmost character, we try placing each character in the string `abc`, in that order, in the current location. We then move on to the next character, repeating the aforementioned process. If the length of the string is equal to `n`, we increment a counter by `1` to signify that we have generated a string of the desired length. After this counter is incremented we also have to check if the value is equal to `k`. If so, we know that we have just generated the `k`th lexicographically smallest string with length `n`, which is exactly what we want.  
  
#### Conclusion
This solution has a time complexity of $O(kn)$, where $k$ is `k` and $n$ is `n`. The space complexity is $O(n)$.  
  

