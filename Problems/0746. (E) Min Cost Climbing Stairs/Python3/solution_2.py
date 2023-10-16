class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(cost)
    # dp[i] is cost of climbing to top from step i
    dp = [0] * (n+1)
    dp[-2] = cost[-1]
    for i in range(n-2, -1, -1):
      dp[i] = cost[i] + min(dp[i+1], dp[i+2])
    
    return min(dp[0], dp[1])

