## 1626. (M) Best Team With No Conflicts

### `solution.py`
This is an extension of problem 300, Longest Increasing Subsequence. To make things easier we can first sort the players primarily by age, then by score. Then we can see that we need to find a strictly increasing subsequence that would yield the highest score. We memoize intermediate results in `dp`, where `dp[i]` contains the highest score among rosters in the range `[0,i]` ending with player `i`. Then we iterate over `l_sorted` (loop variable `i`), computing values of `dp` for all indices in the range `[0, i]` (loop variable `j`). At player `j` we compare the score to player `i`, and only consider updating `dp[i]` if the score of `i` is greater than or equal to that of `j`. This is because in a valid roster players of the same age can have the same score, but can't have a score lower than the current player since that would invalidate previously computed values in `dp`. Whenever `j` and `i` passes the aforementioned check we update `dp[i]` *if* player `i`'s score plus the highest roster score at player `j` (`dp[j]`) is greater than the previously recorded best at player `i` (`dp[i]`).  
The desired result is the largest value stored in list `dp`.  

#### Conclusion
The time complexity for this solution is $O(n^2)$ where $n$ is the number of players, since for each player `i` we traverse all indices from `0` up to `i-1`. In terms of space complexity the solution uses $O(n)$ space as `dp` has a length of $n$.  
  
