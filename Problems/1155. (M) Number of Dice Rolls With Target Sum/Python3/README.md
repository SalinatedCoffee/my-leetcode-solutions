## 1155. (M) Number of Dice Rolls With Target Sum

### `solution.py`
We are asked to count the number of ways to roll `target` using `n` `k`-sided dice. To make things simpler, we can change this problem slightly so that we roll a single dice `n` times instead of rolling `n` dice at once. From this new perspective it becomes quite obvious that this problem can be solved using dynamic programming.  
If we know the number of ways that some number `i` can be rolled by rolling a `k`-sided dice `j` times, we can also compute the number of ways of rolling each value in `[i + r for r in range(1, k+1)]` with `j+1` rolls. Thus we can set up a recurrence relation where each state is represented by two integers, where one represents the number of remaining dice rolls and the other the remainder of `target`. The base cases are when either or both values are `0`. Say that the recursive function `recurse(rolls, rem)` returns the number of ways to roll `rem` using `rolls` rolls of a `k`-sided dice. If `rem` *and* `rolls` are `0`, it means that we have used all rolls given to us to roll *exactly*  `target`, so we return `1`. If either one of `rem` *or* `rolls` is `0`, we return `0` since this would mean that we have either exhausted all rolls without reaching `target`, or we have exceeded `target` with remaining rolls. Otherwise, we simply try rolling every possible value by calling `recurse(rolls-1, rem-i)` for all possible `i` and return the sum of all return values.  
By definition of `recurse` we want the return value of `recurse(n, target)`, which we can return directly.  

#### Conclusion
The time complexity of this solution is $O(nt)$, where $n$ is `n` and $t$ is `target`. Each state of the recurrence relation is represented by two integers, where one is bound by $n$ and the other by $t$. The return value of every possible state is computed, with each computation taking $O(1)$ time - hence the overall time complexity of $O(nt)$. The space complexity is also $(nt)$ as we memoize the return value of every call to `recurse`.  
  

