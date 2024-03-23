## 22. (M) Generate Parentheses

### `solution.py`
This problem can quite obviously be solved by use of backtracking. If we know that we can either open or close a parenthesis we can try both and recurse further down on each resulting string.  
We define a function `recurse`, which takes 3 parameters `cur`, `hanging`, and `rem`. `cur` is the string of parentheses that has been generated up to this point, `hanging` is the number of open parentheses that needs to be closed in `cur`, and `rem` is the number of parentheses that can be opened. If `hanging` is not `0`, we know that we can append a `)` to the end of `cur` to close off an open parenthesis. Now `hanging` is `hanging-1`, and `rem` is not changed, so we call `recurse(cur+')', hanging-1, rem)`. If `rem` is not `0`, we now that we can append a `(` to the end of `cur` to open a parenthesis that would need to be closed some time in the future. In this case `hanging` becomes `hanging+1`, and `rem` becomes `rem-1`, so we call `recurse(cur+'(', hanging+1, rem-1)`. Finally, if `hanging` and `rem` are both `0`, `cur` is a valid set of `n` parenthesis pairs and we append `cur` to the return list `ret`.  
To populate `ret`, we simply call `recurse("", 0, n)`.  

#### Conclusion
This solution has a time complexity of $O(2^n)$. A valid string consists of $2n$ characters, and for each character there are 2 choices that can be made(which is admittedly a gross oversimplification). The space complexity is $O(n)$, as the recursion stack can be at most $2n$ tall.  
  

