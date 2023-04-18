## 2218. (H) Maximum Value of K Coins From Piles

### `solution.py`
A brute-force solution will be too slow, since the number of coin combinations that we would have to consider would be $_\text{total number of coins}\text{C}_k$. Instead we can establish a recursive relation between the original problem and smaller sub-problems, which we can solve first. We eventually want the value corresponding to the scenario where we choose `k` coins from all `n = len(piles)` piles. In the previous step, we could have chosen 0 coins from the `n`th pile, and `k` coins from piles `1..n-1`. Or, we could have chosen 1 coin from the `n`th pile, and `k-1` coins from piles `1..n-1`. The choices continue until we could have chosen `k` coins from the `n`th pile and 0 coins from piles `1..n-1`. Either way, we want the largest value among these choices as we want to maximize the final sum of all selected coins.  
We initialize a 2D list `dp` where `dp[i][j]` contains the maximum value of `j` coins selected from piles `piles[:i]`. The desired value will be stored in `dp[n][k]`, so we start computing values of `dp` starting at `dp[1][1]` and moving towards `dp[n][k]` row-first. We do not start at `dp[0][0]` since selecting coins from no columns and selecting no coins from previous columns would result in values of zero. For each pile `i`, we consider the scenario where we are selecting `0..k` coins among all piles up to that pile. For each scenario `j`, we try choosing `0..j` coins from the `i`th pile.  
After the outer loop exits the desired value will be stored in `dp[n][k]`, which we return.  

#### Conclusion
The time complexity for this solution is $O(kt)$, where $k$ is `k` and $t$ is the total number of coins in `piles`. The outer and innermost `for` loops are $O(t)$, hence the running time of $O(kt)$. The space complexity is $O(kn)$ where $n$ is the length of `piles`. `dp` is a 2D list with dimensions $k*n$.  
  

