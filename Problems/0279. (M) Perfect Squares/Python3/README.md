## 279. (M) Perfect Squares

### `solution.py`
As we want to find the *minimum* number of squares that `n` can be decomposed into, a greedy algorithm will not work. One example of when such an approach would fall apart is when `n = 12`. A greedy algorithm would decompose 12 into the 4 squares 9, 1, 1, and 1. The optimal solution however, would be the 3 squares 4, 4, and 4. Hence we should be taking a dynamic programming approach to this problem, where we try multiple decompositions at some integer and select the choice that yields the fewer number of squares.  
For some integer `n`, we incrementally try subtracting every perfect square smaller than or equal to `n`. If `n` is `0`, we simply return `0` as it cannot be decomposed. Among these recursive calls we take the one that returns the smallest value, and return that value + 1.  

#### Conclusion
The time complexity of this solution is $O(n\sqrt n)$, where $n$ is `n`. `numSquares` is evaluated for all integers `i` in the range `[0, n]`, and evaluating `numSquares(i)` requires $O(\sqrt n)$ time to complete. The space complexity is $O(n)$, as all intermediate values of `numSquares` are memoized in memory.  
  


### `solution_2.py`
The previous solution can trivially be rewritten as a bottom-up algorithm, where we start at 0 and incrementally build up to `n`. We first initialize a list `dp` of length `n + 1`. `dp[i]` will contain the smallest number of perfect squares that `i` can be decomposed into. For every integer `i` from `0` to `n`, we update all possible `dp[i+sq]`, where `sq` is a perfect square and `(i + sq) <= n`. If `dp[i+sq] < (dp[i] + 1)`, we leave `dp[i+sq]` as is. Otherwise, we overwrite it with `dp[i] + 1`. Once all integers have been considered, the answer will be the value stored in `dp[n]`.  

#### Conclusion
The time and space complexity of this solution is identical to that of the previous solution.  
  

