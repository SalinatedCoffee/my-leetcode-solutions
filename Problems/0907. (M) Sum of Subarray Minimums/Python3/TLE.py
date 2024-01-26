class Solution:
  def sumSubarrayMins(self, arr: List[int]) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(arr)
    ret = 0
    mod = 10**9 + 7

    for i in range(n):
      # dp[j] is minimum value of arr[i:j+1]
      dp = arr[i]
      for j in range(i, n):
        dp_j = min(dp, arr[j])
        ret += dp_j
        dp = dp_j

    return ret % mod

