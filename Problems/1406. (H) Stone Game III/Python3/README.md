## 1406. (M) Stone Game III

### `solution.py`
Since the sum of all stones is unchanged regardless of how the game is played, it could be said that a player scoring means that the other player loses points. The goal is to maximize the score difference between Alice and Bob. Let `dp` be a list of length `n + 1`, where `n = len(stoneValue)`. The value of `dp[i]` will equal the maximum score difference of a game played with stones `stoneValue[-i:]`. By this definition the value of `dp[n]` will naturally be `0` since a game played with no stones will end up with a score difference of `0`. Consider some value `dp[i]`. If we choose to take 1 stone, the score for the current turn will be `stoneValue[i]` and the next state will be represented by `dp[i+1]`. Both players want to *maximize* the values of `dp`, but in different directions; one wants to maximize it in the positive direction, and the other wants to maximize it in the negative direction. We can simulate this by subtracting the relevant `dp` value from the current turn's score. Remember that values of `dp` is the score *difference* between the two players - that is, $\text{score}_x - \text{score}_y$. By substracting the value of `dp` we essentially flip the difference, which emulates the players taking turns after each other. Thus, `dp[i]` is the value of either `stoneValue[i] - dp[i+1]`, `sum(stoneValue[i:i+2]) - dp[i+2]`, or `sum(stoneValue[i:i+3]) - dp[i+3]`, whichever is the largest.  
The desired value will be stored in `dp[0]`, which represents the maximum score difference for the game played with all stones.  

#### Conclusion
The time and space complexity for this solution is $O(n)$ where $n$ is the length of `stoneValue`.  
  

