## 1639. (H) Number of Ways to Form a Target Given a Dictionary

### `solution.py`
We can start computing the number of ways to form a prefix of `target` and gradually work our way towards the entire string. The intermediate values will be stored in a 2D list `dp`, where `dp[i][j]` contains the number of ways to construct `target[:i]` (in other words, a prefix of `target` of length `i`) using `j` columns of `words`. First we need to establish the state transitions for the DP table. Say we know the value of `dp[i][j]`. Transitioning to `dp[i+1][j]` would not make sense as we cannot use an additional letter from the `j` columns to form `target[:i+1]`, per the problem specification. Transitioning to `dp[i][j+1]` would mean adding another column to form `target[:i]`. This simply means that we have skipped the `j`th column, and thus `dp[i][j+1] += dp[i][j]`. The last transition to `dp[i+1][j+1]` means we have choose the character `target[i]` in the `j`th column. There may be multiple instances of `target[i]` in that column, which we multiply by the value of the pre-transition state to get the total number of possible ways to form the prefix with the given number of columns - this is simply `dp[i+1][j+1] = count(target[i], j) * dp[i][j]`, where `count(c,i)` returns the frequency of character c in the `i`th column of `words`.  
Now we may start at `dp[0][0]` and move towards `dp[len(target)][len(words[0])]`, which we can do using nested for loops.  

#### Conclusion
The time complexity is $O(kn+km) = O(k(n+m))$ where $k$ is the length of `words[0]`, $n$ is the length of `target`, and $m$ is the length of `words`. The space complexiy is $O(26k+mk) = O(mk)$.  
  

