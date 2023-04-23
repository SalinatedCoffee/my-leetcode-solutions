## 1416. (H) Restore The Array

### `solution.py`
A naïve brute-force approach will most definately take too long. We can see that the problem can easily be broken down to smaller subproblems, so here we will be attempting a bottom-up dynamic programming approach.  
Firstly, we need to establish the relation between a problem and its subproblem. Say we have a list `dp` where `dp[i]` is the number of ways that a prefix `s[:i]` can be split into valid integers. What are the possible transitions we can make from `dp[i]`? Let's first consider `dp[i+1]`, where we consider the character after the prefix. If `s[i:i+1]` is a valid integer, we can simply add `dp[i]` to `dp[i+1]` since the number of splits for `s[:i]` will still be valid. The same can be said for `dp[i+2]`, `dp[i+3]` and so on, until we find a substring `s[i:i+m]` that is larger than `k`. We repeat this for all `i` starting at `0` and ending at `len(s)`, then the answer will be stored in `dp[-1] == dp[n]`.  

#### Conclusion
This solution has a time complexity of $O(n\log k)$, where $n$ is the length of `s` and $k$ is `k`. Both outer and inner loops iterate along `s`, but the inner loop exits when the substring becomes larger than `k`. Since a digit is added to the substring for every iteration of the inner loop, the number increases by a magnitude, hence taking $O(\log k)$ time instead of $O(k)$. The space complexity is $O(n) as `dp` is `len(s)` long.  
  

