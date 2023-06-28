class Solution:
  def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(locations)
    mod = 10**9 + 7
    # dp[i][j] is number of paths from i with j fuel
    dp = [[0] * (fuel+1) for _ in range(n)]
    dp[finish] = [1] * (fuel+1)

    for i in range(fuel+1):
      for j in range(0, n):
        for k in range(0, n):
          if k == j:
            continue
          trip = abs(locations[j] - locations[k])
          if trip <= i:
            dp[j][i] += dp[k][i - trip]
            dp[j][i] %= mod
    
    return dp[start][fuel]

