## 629. (H) K Inverse Pairs Array

### `solution.py`
Obviously, enumerating all possible orderings for `n` and `k` is not viable. Thus we need to figure out a way to mathematically work out the number of possible enumerations instead. Assume the sequence $1, ..., n$ has exactly $k - 1$ inverse pairs. If we wanted to change this sequence to have exactly $k$ pairs, we could take $n$ and move it in front of the $1$. As $n$ is larger than any other values in the sequence, we have now increased the number of inverse pairs by $n - 1$. We originally wanted to only increase the number of pairs by $1$, and so we must account for the number of overcounted pairs. This is simply the number of sequences using $n-1$ with exactly $k-1-(n-1)=k-n$ pairs, which is a subproblem. Finally, we need to count the number of sequences in the form of $1,...,n$ with $k$ inverse pairs, which is also a subproblem. Using this information, we can set up a recurrence relation which will allow us to implement a top-down dynamic programming algorithm. If the function `recurse(n, k)` returns the number of sequences using integers up to `n` with exactly `k` inverse pairs, moving $n$ to the front of the sequence corresponds to `recurse(n, k-1)`. The number of overcounted sequences is the return value of `recurse(n-1, k-n)`, and the number of sequences in the form $1,...,n$ corresponds to `recurse(n-1, k)`. The base cases are when `k == 0` and `n == 1 or k < 0`. For the former, there is only one way to create a sequence that has no inverse pairs, so we return `1`. For the latter, there are no possible ways of creating a sequence containing an inverse pair with only 1 value, or a sequence with a negative number of inverse pairs. We return `0` in this case.  

#### Conclusion
This solution has a time complexity of $O(nk)$, where $n$ is `n` and $k$ is `k`. There are $nk$ states in total, and we evaluate the value for each and every state with each computation taking constant time. The space complexity is also $O(nk)$, since we memoize the intermediate values in memory.  
  


### `solution_2.py`
The first solution passes, but only barely; sitting at the lower 5th percentile for both runtime and memory. If we examine the recurrence relation, we see that a state only depends on the values for `n-1`. Hence, we can implement a bottom-up solution based on the previous solution and optimize for space by using a 1D list to store intermediate values instead of a 2D list. For every integer `i` from `2` up to `n`, we first start with `1` and work our way up to `k`, computing the value of `dp[j] + dp[j-1]` where `j` is the loop variable. Then we subtract the overcounted sequences by starting at `k` and iterating down to `i`, computing the value of `dp[j] - dp[j-i]`. Once the loop exits, the answer we want will be stored in `dp[k-1]`, which corresponds to the return value of `recurse(n, k)` in the previous solution.  

#### Conclusion
This solution has a time complexity of $O(nk)$, and a space complexity of $O(k)$.  
  

