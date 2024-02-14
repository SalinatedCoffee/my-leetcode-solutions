class Solution:
  def kInversePairs(self, n: int, k: int) -> int:
    # space-optimized bottom-up dynamic programming (tabulation)
    
    mod = 10**9 + 7
    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(2, n + 1):
      for j in range(1, k + 1):
        dp[j] = (dp[j] + dp[j - 1]) % mod
      for j in range(k, i - 1, -1):
        dp[j] = (dp[j] - dp[j - i]) % mod
    
    return dp[-1]

