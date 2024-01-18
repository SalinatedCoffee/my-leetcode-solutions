## 70. (E) Climbing Stairs

### `solution.py`
The most obvious approach would be a dynamic programming based solution. At each stair we can either climb `1` step or `2` steps. If there are `i` stairs left to climb, the number of ways to climb all the stairs would simply be the sum of the ways to climb `i-1` stairs and `i+2` stairs. The number of ways to climb `0` stairs is `1`, and the number of ways to climb a negative number of stairs is `0`, for obvious reasons.  
We define a function `recurse(r)` that will return the number of ways to climb `r` stairs. As described previously, we return `1` if `r == 0` or `0` if `r < 0`. If `r` falls under neither of those cases, we return the value of `recurse(r-1) + recurse(r-2)`. By definition the return value of `recurse(n)` will be the answer, which we can directly return.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is `n`. There are $n$ recursive states in our recurrence relation, where each state takes constant time to compute. The space complexity is $O(1)$.  
A micro-optimization could be made by unwrapping `recurse()` and making `climbStairs` itself recursive.  
  


### `solution_2.py`
As is usually the case with top-down DP algorithms, the previous solution can also be implemented as a bottom-up algorithm, eliminating recursion overhead. This time the state values will be stored in the list `dp`, where `dp[i]` is the number of ways to climb `i` stairs. `dp[0]` and `dp[1]` are initialized as `1`, since there is only one way to climb 0 and 1 stairs. We then compute `dp[i]` where `1 <= i <= n` by adding `dp[i-1]` and `dp[i-2]`. Once all values for `dp` have been computed, `dp[n]` will contain the value we want.  

#### Conclusion
As with the previous solution, the time and space complexity for this solution is $O(n)$.  
  


### `solution_3.py`
If you had a sneaking suspicion that this problem could be solved through basic math, you would be correct! The crux of the problem is realizing that we can use the combination formula to directly compute the number of ways to climb the stairs. Say we wanted to compute the number of ways to climb `5` stairs, but can only climb 2 steps once. If we try all possible ways by hand, we get `2, 1, 1, 1`, `1, 2, 1, 1`, `1, 1, 2, 1`, and `1, 1, 1, 2`. This is simply $_4C_1$, since we are selecting when to take 2 steps out of 4 possible moves. Building up from here, we can now easily compute the number of ways of climbing `5` steps where we must climb 2 steps exactly twice, which is $_3C_2$(`2, 2, 1`, `2, 1, 2`, `1, 2, 2`). Generalizing, if we want to compute the number of ways of climbing `i` stairs, we simply need to compute the total sum of selecting `j` from `k` moves for all possible `j`. As climbing 2 steps at once effectively 'merges' 2 moves of 1 steps into one, `j` would be in the range `0 <= j <= i // 2 + 1`.  

#### Conclusion
This solution has a time complexity of $O(n)$, since the loop will run $\lfloor n / 2\rfloor + 1$ times. The space complexity is $O(1)$.  
  

