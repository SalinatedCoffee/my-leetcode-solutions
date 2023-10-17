## 746. (E) Min Cost Climbing Stairs

### `solution.py`
The problem can clearly be solved with a dynamic programming approach, but we will need to make sure that we are handling the states correctly since the starting state is technically outside `cost`. Say we already know the minimum cost of climbing to steps `0` to `i` from the start. To compute the minimum cost of climbing to step `i+1` then, we know that either one of two things could have happened in the previous step. It either took 2 steps to reach `i+1`, or only 1 step. Either way we want to minimize the total cost of climbing, and so we should be selecting the choice that has the lower cost between the two. We memoize the computed cost in a list `dp`, where `dp[i]` contains the minimum cost required to climb from the start to step `i`.  
Once the cost for each and every state has been computed, we have to remember to return the smaller cost between `dp[-1]` and `dp[-2]` since the 'top' of the stairs can be reached from either the very last step or the second last step.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the length of `cost`. There are $n$ states that have to be computed, and each computation takes $O(1)$ time. The space complexity is also $O(n)$, since we memoize the results in the list `dp` which is $O(n)$ long.  
  

### `solution_2.py`
The previous solution can easily be converted into a bottom-up algorithm, as `dp[i]` relies on the values `dp[i+1]` and `dp[i+2]`. Starting with `dp[n-1]`, we can incrementally compute value of `dp` until we reach `dp[0]`. Similar to the first solution, we have to remember to return the minimum value between `dp[0]` and `dp[1]` since we can start climbing from either the first step or the second one.  

#### Conclusion
The time and space complexity of this solution is also $O(n)$, but can be space-optimized further down to $O(1)$ by exploiting the fact that `dp[i]` depends on *only* the values `dp[i+1]` and `dp[i+2]`.  
  
