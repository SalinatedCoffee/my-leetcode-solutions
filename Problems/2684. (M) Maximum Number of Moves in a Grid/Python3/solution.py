class Solution:
  def maxMoves(self, grid: List[List[int]]) -> int:
    # bottom-up dynamic programming (tabulation)

    m, n = len(grid), len(grid[0])
    # dp[i][j] is max number of possible moves starting at grid[i][j]
    dp = [[0]*n for _ in range(m)]
    for j in range(n-2, -1, -1):
      for i in range(m):
        if i > 0:
          dp[i][j] = max(dp[i][j], dp[i-1][j+1] + 1) if grid[i][j] < grid[i-1][j+1] else dp[i][j]
        dp[i][j] = max(dp[i][j], dp[i][j+1] + 1) if grid[i][j] < grid[i][j+1] else dp[i][j]
        if i < m-1:
          dp[i][j] = max(dp[i][j], dp[i+1][j+1] + 1) if grid[i][j] < grid[i+1][j+1] else dp[i][j]

    return max([row[0] for row in dp])

