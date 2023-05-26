class Solution:
  def new21Game(self, n: int, k: int, maxPts: int) -> float:
    # bottom-up dynamic programming (tabulation)

    # dp[i] is probability of obtaining score i
    dp = [0] * (n + 1)
    dp[0] = 1
    s = 1 if k else 0
    
    for i in range(1, n + 1):
      dp[i] = s / maxPts
      if i < k:
        s += dp[i]
      if i - maxPts >= 0 and i - maxPts < k:
        s -= dp[i - maxPts]

    return sum(dp[k:])

