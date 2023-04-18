class Solution:
  def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(piles)
    # dp[i][j] contains max. value of j coins picked from i piles
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
      for coins in range(0, k+1):
        c_sum = 0
        for c_coins in range(0, min(len(piles[i-1]), coins)+1):
          if c_coins > 0:
            c_sum += piles[i-1][c_coins-1]
          dp[i][coins] = max(dp[i][coins], dp[i-1][coins-c_coins]+c_sum)
    
    return dp[n][k]

