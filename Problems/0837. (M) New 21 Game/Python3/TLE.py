class Solution:
  def new21Game(self, n: int, k: int, maxPts: int) -> float:
    # bottom-up dynamic programming (tabulation)

    # dp[i] is probability of obtaining score i
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
      for j in range(1, maxPts + 1):
        if i - j >= 0 and i - j < k:
          dp[i] += dp[i - j] / maxPts

    return sum(dp[k:])

