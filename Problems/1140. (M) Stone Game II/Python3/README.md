## 1140. (M) Stone Game II

### `solution.py`
Since the total number of stones does not change regardless of how a game is played, it can be said that a player trying to maximize their score is effectively the same as trying to minimize the other player's score. For this problem, we want to maximize Alice's score and thus need to perform different actions based on who's turn it is. Assume that the function $r(p, i, m)$ returns the maximum score of Alice for a game that starts with player $p$ (where $p = 0$ is Alice and the other, Bob), using the last $i$ piles of stones, and $M = m$. When $p = 0$, the score for the current move is the sum of stones in piles from $i$ up to $i + x$. This is then added with the return value of the next state, which would be $r(1, i+x, \text{max}(m,x))$. In the opposite case, we simply ignore the score of the current turn since Bob will take them, denying them to Alice. Alice wants to maximize return values of $r$, and Bob wants to do otherwise. Thus Alice chooses the maximum value among all possible calls to $r$ in the current turn, and Bob chooses the minimum value.  
We store the return values of $r$ in `dp` to avoid recomputing known values. The value we want will be stored in `dp[0][0][1]`, which is equivalent to the function call $r(0,0,1)$.  

#### Conclusion
This solution has a time complexity of $O(n^3)$, where $n$ is the length of `piles`. The value of two out of three parameters of $r$ can be at most $n$, and at each call to $r$ we try all possible values for $x$ which is also bound by $n$. The space complexity is $O(n^2)$.  
  

