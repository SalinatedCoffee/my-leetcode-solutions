## 198. (M) House Robber

### `solution.py`
Intuition tells us we could take a dynamic programming approach to this problem as a decision at some position requires information from previous decisions. Examining this relationship, we see that at a house we have 2 choices to choose from; we can either steal from the current house or not steal. For the former, we couldn't have stolen from the previous house as that would trip the alarm. For the latter, we could have stolen from the previous house. Among these possibilities, we want to select the action that yields the most amount of loot, which would be the amount stolen up to the previous house vs up to the second-previous house + the loot at the current house. The base case is when there are no houses to steal from, in which case we simply return `0`.  

#### Conclusion
This solution has a time and space complexity of $O(n)$ where $n$ is the length of `nums`. We compute the return value of all possible states, of which there are $O(n)$ of. Processing each state takes constant time, hence the overall time complexity is $O(n)$. As these values are kept in memory, the space complexity is also $O(n)$ (the recursion stack will also use $O(n)$ space).  


### `solution_2.py`
The previous solution can be easily rewritten as a bottom-up dynamic programming algorithm. As the top-down solution depends on values of the states to the left (assuming the state variable increases from left to right) we should populate `dp` left-to-right(for this specific problem the direction doesn't actually matter; in the spirit of basing the bottom-up approach on the top-down solution however, we have chosen to implement left-to-right).  

#### Conclusion
The time and space complexity of this solution is identical to the first solution.  
  

### `solution_3.py`
This solution improves upon the previous one by noticing that at the `i`-th house we only look at values of `dp[i-1]` and `dp[i-2]`, and thus can eschew the list `dp` by storing the required values in two integers instead.  

#### Conclusion
The solution has a time complexity of $O(n)$ and a space complexity of $O(1)$.  
  
