class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    # bottom-up dynamic programming (tabulation)

    # sanity check
    if obstacleGrid[0][0]:
      return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    # dp[i][j] is number of unique paths from start to obstacleGrid[i][j]
    dp = [[0]*n for _ in range(m)]
    for i in range(m):
      if obstacleGrid[i][0]:
        break
      dp[i][0] = 1
    for i in range(n):
      if obstacleGrid[0][i]:
        break
      dp[0][i] = 1

    for i in range(1, m):
      for j in range(1, n):
        if obstacleGrid[i][j]:
          continue
        dp[i][j] += dp[i-1][j] + dp[i][j-1]
    
    return dp[-1][-1]

