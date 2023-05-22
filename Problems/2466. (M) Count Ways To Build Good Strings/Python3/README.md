## 2466. (M) Count Ways To Build Good Strings

### `solution.py`

We may append runs of `0`s or `1`s freely, allowing us to simply count the number of ways we can reach integers in the range `[low, high]` by adding up `zeros` or `ones`. Intuition tells us that we could take a dynamic programming approach to this problem since the number of ways to produce a string of some length `i` would depend on values that are less than `i`. Examining the case where we want the number of ways to generate a string of length `i` then, we know there are two possibilities. Either the string ends with a run of `0`s of length `zeros`, or `1`s of length `ones`. If we assume we have a list `dp` where `dp[i]` contains the number of ways to construct a string of length `i`, the value of `dp[i]` would simply be `dp[i-ones] + dp[i-zeros]` according to our reasoning.  

The length of `dp` should be `high+1`, since we also want to account for strings of length 0. We initialize `dp[0]` to `1`, as there is only one way to construct an empty string. Then we iterate from `1` to `high`, while performing the steps described earlier. Once the loop exists, the desired value will be the sum of values from `dp[low]` to `dp[high]`.  

#### Conclusion

This solution has a time and space complexity of $O(n)$, where $n$ is simply `high`.  


