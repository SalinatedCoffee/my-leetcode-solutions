## 2140. (M) Solving Questions With Brainpower

### `TLE.py`
Intuition tells us that we could take a dynamic programming approach to this problem, as it seems like there is some kind of relationship between the elements. Iterating over `questions`, we can either solve the current problem and skip ahead a few, or skip the current question and move on to the next one. Say we have a list `dp` where `dp[i]` contains the maximum score achieved by solving questions in the range `questions[:i]`. If we solve `questions[i]` then, we would need to scan all values in `dp[:i-1]` to find the maximum score among problems that are *solvable*; that is, previous problems that can be solved while not skipping the `i`th question. This can be trivially checked by evaluating `questions[j][1] < i - j`.  
After the outer loop exits, we scan through `dp` in order to find the largest value, which we return.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is the length of `questions`. The space complexity is $O(n)$, since `dp` has a length of $n$.  
  

### `solution.py`
The first solution, while correct, is too slow for large inputs and results in a TLE. How can we optimize the previous solution? In the inner loop we had to iterate over *all* elements up to the current one since solving a question `j` with 2 skips still meant that we had to check question `j+1`. What would happen if we redefine `dp` so that `dp[i]` contains the maximum score solving questions in `questions[i:]`? Using this definition we would have to fill `dp` backwards, since `dp[i]` would now depend on values in `dp[i+1:]`.  
Let's examine the state transitions in more detail. As we have already established, there are two possible actions that we can take at some problem `i`. If we solve the question, the score would be `questions[i][0] + dp[i + questions[i][1] + 1]` since we must skip over `questions[i][1]` problems by solving the current one. If we skip the question, the current score simply becomes `dp[i+1]`. Since we are *maximizing* the total score, we should update `dp[i]` by selecting the larger of the two scores.  
By the new definition of `dp` described above, the value we want would be stored in `dp[0]`, which we return once we finish iterating over `questions`.  

#### Conclusion
The time complexity is $O(n)$ as we iterate over `questions` once, and each iteration takes constant time. The space complexity is also $O(n)$.  
  

