## 91. (M) Decode Ways

### `solution.py`
We can clearly take a dynamic programming approach for this problem as it can be broken down into clearly defined subproblems. For example if we know the number of ways that `s[i:]` can be decoded, we can also determine the number of ways that `s[i-1:]` and `s[i-2:]` can be decoded.  
The recursive function `recurse(i)` will return the number of ways that `s[i:]` can be decoded. If `i >= len(s)`, then it should return `1` as there is only one way to decode an empty string. If `s[i]` is the character `'0'`, we immediately return `0` since `'0'` does not map to any letter, which means that the string cannot possibly be decoded into a string of letters. Otherwise, we try decoding one digit at `i` - which means we recurse on the next character, `recurse(i+1)`. If `i+1` is not the last letter, and the substring `s[i:i+2]` can be decoded, we call `recurse(i+2)`. The return values of the two (or one) recursive calls are added together and returned.  
As we want the number of ways to decode the entirety of `s`, the return value of `recurse(0)` will be the desired answer.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. The recursive states are represented by a single integer in the interval $[0, n]$. Since we compute the return value of every possible state, and processing each state takes $O(1)$ time, the overall time complexity is $O(n)$. The space complexity is also $O(n)$, as we use `functools.cache` to memoize the return value of each state in memory.  
  

