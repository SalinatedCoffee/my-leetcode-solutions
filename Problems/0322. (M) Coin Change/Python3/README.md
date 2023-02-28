## 322. (M) Coin Change

### `solution.py`
As is mostly the case with such problems, a brute force approach will take too long to run. We can however see that for a certain value, we can look at the minimum number of coins for values that are `coins` less than the current value. The optimal choice is to select the smallest value + 1 here, and this of course translates nicely to a bottom-up dynamic programming solution. We initialize a list `dp` with length `amount + 1`. `dp[i]` will contain the minimum number of coins that add up to `i`, and thus we need to remember to assign `0` to `dp[0]`. Then we incrementally fill `dp` up to `dp[amount]`, which is the value we want.  
  
#### Conclusion
This solution has a running time of $O(vn)$, where $v$ is `amount` and $n$ is the size of `coins`. The space complexity is $O(v)$, as we tabulate intermediate values in `dp` which has a length of `amount`.  
The time and space complexities are not polynomial, but [pseudo-polynomial](https://en.wikipedia.org/wiki/Pseudo-polynomial_time) since it scales with the *value* of `amount` rather than the *size* of `coins`. This tripped me up for the longest time, after which I decided to just give up and implement this approach. This may or may not be an issue in practice, but it certainly would be good to understand the difference and look out for it whenever you can especially in an interview setting.  
  
  
