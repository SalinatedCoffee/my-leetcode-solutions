## 1143. (M) Longest Common Subsequence

### `solution.py`
While the LCS is a classic dynamic programming problem, we can still deduce that we can take this approach by realizing that given a pair of characters in `text1` and `text2`, we can incrementally compute the LCS length for the remainder of the strings if we know the LCS length up to that pair of characters.  
Let us assume that the LCS length between the prefix substrings `text1[:i]` and `text2[:i]` is `l`. Examining `text1[i]` and `text2[j]`, we have a few choices. We can either 'keep' the `i`th character and examine the `j+1`th one, keep the `j`th and examine the `i+1`th, or, if the `i`th and `j`th characters match, keep both and examine the `i+1`th and `j+1`th characters. Either way we should keep the choice that yields the longest common subsequence. This relationship is easily implemented with a recursive function, and is also trivial to convert to a top-down dynamic programming solution by memoizing the results to the recursive function.  
The desired value is the return value of `recurse(0,0)`, as we want the LCS length of the entierety of both strings.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the lengths of `text1` and `text2`. Each dynamic programming state has 2 parameters, where one is in the range $[0,m]$ and the other in the range $[0,n]$. We compute the values for all possible states, which takes constant time - hence the overall time complexity of $O(mn)$. The space complexity is also $O(mn)$, as `@cache` will have to store of $mn$ values while the recursion stack can be at most $m+n$ deep.  
  

### `solution_2.py`
We can also take a bottom-up approach by examining the state transitions in further detail. Computing the value for the state `(i,j)` requires the values of `(i+1,j+1)`, `(i+1,j)`, and `(i,j+1)`. The base cases for these states are when `i == len(text1)` or `j == len(text2)`, where the value should be `0` since a common subsequence cannot exist if either of the strings are empty. If we start at the state `(m-1,n-1)`, we can guarantee that we will have all the values required in computing a state as long as we do so going right to left (in the context of `i`), and bottom to top(in the context of `j`). Storing the values of the states in a 2D list `dp`, where `dp[i][j]` will be the length of the LCS between `text1[i:]` and `text2[j:]`, the value of `dp[0][0]` will by definition be the one we want.  

#### Conclusion
This solution also has a time and space complexity of $O(mn)$, but will run significantly faster (and use less memory) than the top-down solution by virtue of not relying on a recursive function.  
  

### `solution_3.py`
The previous solution can be improved upon even further by noticing that a state only depends on those immediately 'adjacent' to it. That is, because the value of `dp[i][j]` only depends on `dp[i+1][j]`, `dp[i][j+1]`, and `dp[i+1][j+1]` we do not have to keep the value of all states in memory, but instead only those that are relevant.  
As we have chosen to compute values row-first, we can keep 2 rows in memory - the current row being processed, and the row that was processed in the previous step(which corresponds to `i` and `i+1`, respectively). Once a row has finished processing we swap it with the previous row, as the 'current' row has now become the 'previous' one.  

#### Conclusion
The time complexity of this solution is still $(mn)$, but the space complexity is now $O(n)$. Note that this can be reduced even further still to $O(\text{min}(m,n))$ by choosing the shorter string to be represented as the 'row' and making the proper modifications to the code.  
  
An excellent (and more formal) explanation can be found [here](https://www.ics.uci.edu/~eppstein/161/960229.html) for those who are interested.  
