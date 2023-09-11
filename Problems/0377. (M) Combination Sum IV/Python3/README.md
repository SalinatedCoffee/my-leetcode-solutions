## 377. (M) Combination Sum IV

### `TLE.py`
As combinations with different orderings (which is just a permutation) are considered different, we can simply 'count down' (or up) by subtracting all possible values in `nums` from `target` until we reach `0`. However, upon examining the recurion tree we can quickly see that the running time of this algorithm will be $O(m^k)$ (where $m$ is the length of `nums` and $k$ is the value of `target // min(nums)`) and will fail to pass with TLE.  

#### Conclusion
The time complexity is $O(m^k)$, and the space complexity is $O(k)$.  


### `solution.py`
It is obvious that a dynamic programming approach is viable here, since if we know the number of combinations that add up to some number `i` it is trivial to determine that of `i+1`. In fact, the value for `i` depends on the values of `i - num for nums in nums`. Hence, if we compute the values starting at `1` up to `target`, we can save time by reusing previously computed values.  
We first initialize a list `dp` of length `target + 1` with `0`s. `dp[i]` will contain the number of combinations that add up to `i`. All of the values `num` in `nums` can be used by themselves on `0` to add up to their respective values. We account for this by setting `dp[num] = 1` for all `num` in `nums`. Now we simply iterate along the range `[1, target]` and compute the value of `dp[i]`. As previously described, the value of `dp[i]` is the sum of all possible `dp[i-num]`, which is trivially computed.  
Once the iteration is over the desired value will be `dp[target]`, which we can directly return.  

#### Conclusion
This solution has a time complexity of $O(nm)$, where $n$ is the length of `nums` and $m$ is `target`. We compute the combination count for all values from `1` to `target`, and for each computation we iterate through `nums` exactly once. Hence, the overall time complexity is $O(nm)$. The space complexity is $O(m)$, since `dp` has a length of $m + 1$.  
