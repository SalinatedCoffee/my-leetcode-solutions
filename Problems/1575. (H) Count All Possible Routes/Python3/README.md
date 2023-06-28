## 1575. (H) Count All Possible Routes

### `solution.py`
Intuition tells us that a dynamic programming approach may be possible for this problem, and so we will try and determine what the states will be and how the transitions would be defined. We know that at our initial state we will be starting at location `start` with `fuel` amount of fuel. For our next leg we can move to any location as long as we have enough fuel to cover the distance to the next location. Thus our states will have two parameters - one for where we will be starting and the fuel remaining at that point in time. If we are currently at position `i` with `f` fuel and decide to move to `k`, the number of paths for the state `i` and `f` will be the its value plus `f` subtracted by the absolute difference between `i` and `k`. If we store the values in a 2D list `dp`, where `dp[i][j]` represents the state where we start at `i` with `j` fuel, this transition can be written as `dp[i][j] += dp[k][j - abs(i - k)]`. We want to compute all valid transitions for every possible value of fuel, and so we use 3 nested loops to incrementally fill `dp`. We start out by computing all transitions with `0` fuel. For each location, we check whether a transition can be made to each other location based on the current fuel(which is `0` for this iteration). We cannot transition from the current location to itself, so we simply skip computation whenever that occurs.  
`dp[finish]` should be initialized with `1`s instead of `0`s, since starting at the goal should be counted as a valid path regardless of the amount of fuel remaining.  
Once all loops have exited, the desired value will be stored in `dp[start][fuel]`, naturally.  

#### Conclusion
The time complexity is $O(n^2\cdot fuel)$, where $n$ is the length of `locations` and $fuel$ is `fuel`. For every possible fuel amount we update all values of `dp[i][fuel]`, which takes $O(n^2)$ time. The space complexity is $O(n\cdot fuel)$ since `dp` is a $n\times fuel$ sized 2D list.  
  

