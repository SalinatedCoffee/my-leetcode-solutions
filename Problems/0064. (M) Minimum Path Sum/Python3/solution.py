class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(grid)
    m = len(grid[0])

    # value of dp[i][j] is sum of minimum path from grid[0][0] to grid[i][j]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(1, n):
      dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, m):
      dp[0][j] = dp[0][j-1] + grid[0][j]

    # fill dp towards bottom-right
    for i in range(1, n):
      for j in range(1, m):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[-1][-1]

