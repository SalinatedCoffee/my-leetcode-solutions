class Solution:
  def climbStairs(self, n: int) -> int:
    # bottom-up dynamic programming (tabulation)

    # dp[i] is number of ways to climb i stairs
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
      dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]

