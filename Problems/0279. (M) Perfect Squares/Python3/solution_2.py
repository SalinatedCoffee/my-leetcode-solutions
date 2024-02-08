class Solution:
  def numSquares(self, n: int) -> int:
    # bottom-up dynamic programming (tabulation)
    
    dp = [n] * (n + 1)
    dp[0] = 0

    for i in range(n):
      j = 1
      while (i + j**2) <= n:
        dp[i+j**2] = min(dp[i+j**2], 1 + dp[i])
        j += 1

    return dp[-1]

