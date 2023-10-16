class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    # top-down dynamic programming (memoization)

    n = len(cost)
    # dp[i] is minimum cost of climbing from start to step i
    dp = [float('inf')] * n

    def recurse(i):
      if i < 0:
        return 0
      if dp[i] != float('inf'):
        return dp[i]
      dp[i] = cost[i] + min(recurse(i-1), recurse(i-2))

      return dp[i]

    recurse(n-1)

    return min(dp[-1], dp[-2])

