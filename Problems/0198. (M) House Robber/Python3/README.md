## 198. (M) House Robber

### `solution.py`
Intuition tells us we could take a dynamic programming approach to this problem as a decision at some position requires information from previous decisions. Examining this relationship, we see that at a house we can do one of two things; steal from this house or don't steal. If we steal, we couldn't have stolen from the previous house as that would trip the alarm. If we don't steal, we could have stolen from the previous house. So the decision to steal or not to steal would depend on which nets us the most loot, which would be loot up to the previous house vs loot up to the house 2 houses back + the loot at the current house. Before we start stealing we have no loot and there is no house to steal from, so the total loot would be 0. At the first house we have no loot and there are no previous decisions to look back on, so we just steal from it. Starting from the second house, we can look at the two prior decisions and select the one that would yield more loot.  

#### Conclusion
This solution takes $O(n)$ time and space where $n$ is the number of houses. We fill all elements of `dp`, which is $n+1$ long.  
  
  

### `solution_2.py`
This solution improves upon the first by noticing that at the `i`-th house we only look at values of `dp[i-1]` and `dp[i-2]`, and thus can eschew the list `dp` and store those values in two integers instead.  

#### Conclusion
The solution has a time complexity of $O(n)$ and a space complexity of $O(1)$.  
  
